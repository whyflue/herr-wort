"""Точка входа бота: longpoll VK и отправка сообщений.

Режим работы задаётся в .env переменной BOT_MODE:

* BOT_MODE=group (рекомендуется) — бот отвечает от имени сообщества
  (паблика): нужен токен сообщества VK_GROUP_TOKEN, имя и аватар
  сообщества видны собеседнику, личный аккаунт не используется.
* BOT_MODE=user — бот отвечает от имени обычного аккаунта:
  нужен токен пользователя VK_TOKEN с правом messages.

Запуск:  python main.py
Как получить токен — описано в README.md.
"""

import logging
import random
import sys
import time

import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.longpoll import VkEventType, VkLongPoll

import config
from bot import keyboards
from bot.engine import Engine
from db import Database

log = logging.getLogger("bard")


def setup_logging() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )


def random_id() -> int:
    return random.randint(1, 2 ** 31 - 1)


class Sender:
    """Отправка и правка сообщений. Пауза между отправками снижает риск
    срабатывания антифлуда.

    target — кому отвечаем: в режиме user это id пользователя
    (messages.send → user_id), в режиме group — peer_id диалога
    с сообществом (messages.send → peer_id). Правка всегда идёт по peer_id.

    api — объект vk_api.VkApi (сессия): вызовы идут через api.method(...),
    потому что у vk_method-обёрток иная сигнатура вызова."""

    def __init__(self, api, delay: float, mode: str = "user"):
        self.api = api
        self.delay = max(0.0, delay)
        self.mode = mode
        self._last = {}
        self._sent_at = 0.0

    def _wait(self) -> None:
        pause = self.delay - (time.time() - self._sent_at)
        if pause > 0:
            time.sleep(pause)
        self._sent_at = time.time()

    def push(self, target: int, action: dict) -> None:
        text = action.get("text") or ""
        keyboard = action.get("keyboard")
        packed = keyboards.dumps(keyboard) if keyboard is not None else None
        if action.get("edit") and self._last.get(target):
            params = {"peer_id": target, "message_id": self._last[target],
                      "message": text}
            if packed:
                params["keyboard"] = packed
            try:
                self._wait()
                self.api.method("messages.edit", params)
                return
            except vk_api.exceptions.ApiError as exc:
                log.debug("Правка сообщения не удалась (%s), отправляю новое", exc)
        params = {"random_id": random_id(), "message": text}
        # В режиме сообщества адресат — peer_id диалога, в режиме аккаунта —
        # id пользователя. В личном диалоге эти числа совпадают.
        params["peer_id" if self.mode == "group" else "user_id"] = target
        if packed:
            params["keyboard"] = packed
        message_id = self._send(params)
        if message_id:
            self._last[target] = message_id

    def _send(self, params: dict) -> int:
        for attempt in range(4):
            try:
                self._wait()
                return int(self.api.method("messages.send", params))
            except vk_api.exceptions.ApiError as exc:
                code = getattr(exc, "code", None)
                if code in (6, 9, 10):  # слишком много запросов / антифлуд
                    pause = 1 + 2 * attempt
                    log.warning("VK ограничивает отправку (код %s): пауза %s с", code, pause)
                    time.sleep(pause)
                    continue
                log.error("Отправка не удалась: %s", exc)
                return 0
            except Exception as exc:
                log.error("Сеть подвела при отправке: %s", exc)
                time.sleep(2 + attempt)
        return 0


def build_core():
    """База и движок — общие для обоих режимов, от VK не зависят."""
    db = Database(config.DB_PATH)
    return db, Engine(db)


def run_user() -> int:
    if not config.TOKEN:
        log.error("В .env не задан VK_TOKEN. Как получить токен — см. README.md")
        return 1

    session = vk_api.VkApi(token=config.TOKEN)
    vk = session.get_api()
    try:
        me = vk.users.get()[0]
    except Exception as exc:
        log.error("VK не принял токен: %s", exc)
        return 1
    log.info("Бот запущен от имени %s %s (id%s)",
             me.get("first_name"), me.get("last_name"), me.get("id"))

    db, engine = build_core()
    sender = Sender(session, config.SEND_DELAY, mode="user")
    log.info("База: %s. Жду сообщения — напишите боту с другого аккаунта.", config.DB_PATH)

    while True:
        try:
            longpoll = VkLongPoll(session, wait=25)
            for event in longpoll.listen():
                if event.type != VkEventType.MESSAGE_NEW:
                    continue
                if event.from_me or not event.to_me or not event.user_id:
                    continue
                user_id = int(event.user_id)
                if user_id < 0:
                    continue
                text = event.text or ""
                log.info("← %s: %s", user_id, " ".join(text.split())[:120])
                for action in engine.handle(user_id, text):
                    sender.push(user_id, action)
        except KeyboardInterrupt:
            log.info("Остановлено с клавиатуры")
            break
        except Exception as exc:
            log.error("Longpoll упал: %s. Переподключение через 5 с", exc)
            time.sleep(5)

    db.close()
    return 0


def run_group() -> int:
    if not config.GROUP_TOKEN:
        log.error("В .env не задан VK_GROUP_TOKEN. Как получить токен сообщества — "
                  "см. README.md, раздел «Работа от имени сообщества»")
        return 1

    session = vk_api.VkApi(token=config.GROUP_TOKEN)
    vk = session.get_api()
    try:
        group = vk.groups.getById()[0]
        group_id = int(config.GROUP_ID or group.get("id"))
    except vk_api.exceptions.ApiError as exc:
        if getattr(exc, "code", None) == 15:
            log.error("Токен сообщества принят, но у ключа не хватает прав. "
                      "Перевыпустите ключ в сообществе с галочками "
                      "«Управление сообществом» и «Сообщения сообщества»: "
                      "README.md, раздел «Работа от имени сообщества».")
        else:
            log.error("VK не принял токен сообщества: %s", exc)
        return 1
    except Exception as exc:
        log.error("VK не принял токен сообщества: %s", exc)
        return 1
    link = "vk.com/" + (group.get("screen_name") or f"club{group_id}")
    log.info("Бот запущен от имени сообщества «%s» (id%s, %s)",
             group.get("name"), group_id, link)

    db, engine = build_core()
    sender = Sender(session, config.SEND_DELAY, mode="group")
    log.info("База: %s. Жду сообщения — напишите сообществу в личные сообщения.",
             config.DB_PATH)

    while True:
        try:
            longpoll = VkBotLongPoll(session, group_id, wait=25)
            for event in longpoll.listen():
                if event.type != VkBotEventType.MESSAGE_NEW:
                    continue
                if not getattr(event, "from_user", False):
                    continue  # беседы (мультичаты) не обслуживаем
                message = event.message or {}
                peer_id = int(message.get("peer_id") or 0)
                if peer_id <= 0:
                    continue
                text = message.get("text") or ""
                # Ключ состояния — peer_id диалога. В личном диалоге с
                # сообществом это id пользователя, который пишет боту.
                log.info("← %s: %s", peer_id, " ".join(text.split())[:120])
                for action in engine.handle(peer_id, text):
                    sender.push(peer_id, action)
        except KeyboardInterrupt:
            log.info("Остановлено с клавиатуры")
            break
        except vk_api.exceptions.ApiError as exc:
            code = getattr(exc, "code", None)
            if code == 15:
                log.error("VK отказывает в доступе (код 15): у ключа сообщества "
                          "нет права «Управление сообществом» либо в сообществе "
                          "выключен Long Poll API. Что проверить — README.md, "
                          "раздел «Работа от имени сообщества».")
            else:
                log.error("VK API вернул ошибку: %s", exc)
            time.sleep(15)
        except Exception as exc:
            log.error("Longpoll упал: %s. Переподключение через 5 с", exc)
            time.sleep(5)

    db.close()
    return 0


def run() -> int:
    setup_logging()
    mode = config.BOT_MODE
    if mode not in ("user", "group"):
        log.warning("Неизвестный BOT_MODE=%r — работаю в режиме user", config.BOT_MODE)
        mode = "user"
    log.info("Режим работы: %s", mode)
    if mode == "group":
        return run_group()
    return run_user()


if __name__ == "__main__":
    sys.exit(run())
