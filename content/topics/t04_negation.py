"""Тема 4. Negation: nicht/kein."""

TOPIC = {
    "id": "negation",
    "nr": 4,
    "title": "Отрицание: nicht и kein",
    "short": "Отрицание nicht/kein",
    "title_de": "Negation: nicht/kein",
    "location": "Кёльн, у собора",
    "location_de": "Köln, am Dom",
    "intro": (
        "Бард входит в Кёльн и замирает: над ним поднимается собор. Внутри "
        "нельзя шуметь, и служка строго шепчет: «Hier singt man nicht». "
        "У барда нет денег на ночлег, но это не беда. Он учится говорить "
        "«нет» по-немецки: nicht или kein — от этого зависит, поймут ли его "
        "люди у собора."
    ),
    "listen": (
        "Бард слушает собор: служка шепчет «Hier singt man nicht», нищенка "
        "у входа вздыхает «Ich habe kein Geld», а колокол гудит так, что слов "
        "не нужно. Отрицание звучит даже в тишине: nicht, kein, keine."
    ),
    "theory": [
        {
            "title": "kein — отрицание для существительных",
            "body": (
                "kein ставим перед существительным, если в утверждении был бы "
                "ein или артикля не было вовсе. Оно склоняется как ein:\n\n"
                "Nominativ: kein Sack, keine Kiste, kein Haus\n"
                "Akkusativ: keinen Sack, keine Kiste, kein Haus\n"
                "Множественное число: keine Säcke, keine Kisten, keine Häuser\n\n"
                "Der Barde hat kein Geld. Ich sehe keinen Wirt. Sie singt "
                "keine Lieder.\n\n"
                "Если перед существительным стоит определённый артикль, kein "
                "уже невозможен: Ich kenne den Mann — Ich kenne den Mann nicht."
            ),
        },
        {
            "title": "nicht — для всего остального",
            "body": (
                "nicht отрицает глаголы, прилагательные, наречия, имена "
                "и целые предложения:\n\n"
                "Der Barde singt nicht. Der Dom ist nicht alt. Ich heiße "
                "nicht Peter. Wir fahren nicht nach Köln.\n\n"
                "Короткое правило: если перед существительным нет артикля или "
                "стоит ein — берём kein; во всех остальных случаях (глагол, "
                "прилагательное, имя собственное) — nicht.\n\n"
                "Сравни: Ich sehe keinen Wirt (существительное без артикля) — "
                "Ich sehe den Wirt nicht (существительное с артиклем den)."
            ),
        },
        {
            "title": "Где стоит nicht",
            "body": (
                "nicht стоит в конце предложения или перед тем словом, "
                "которое отрицает:\n\n"
                "Der Barde singt nicht. Ich singe heute nicht. Ich singe nicht "
                "im Dom. Der Dom ist nicht alt. Nicht heute, sondern morgen.\n\n"
                "Перед спрягаемым глаголом в Präsens nicht стоять не может: "
                "«Ich nicht singe» — ошибка, правильно Ich singe nicht.\n\n"
                "kein стоит только перед существительным и никогда "
                "не отрицает прилагательное или глагол: «Der Dom ist kein "
                "alt» — ошибка, правильно Der Dom ist nicht alt."
            ),
        },
    ],
    "song_line": (
        "Am Kölner Dom bleibt meine Stimme still,\n"
        "kein Geld, kein Lied — doch ich lerne, was ich will."
    ),
    "exercises": [
        {
            "id": "negation_1",
            "kind": "gap",
            "prompt": (
                "Бард стоит у собора без денег: «Ich habe ___ Geld für ein "
                "Bier.»"
            ),
            "options": ["keine", "kein", "keinen", "nicht"],
            "answer": 1,
            "explain": (
                "das Geld — средний род, в Akkusativ форма не меняется: kein "
                "Geld. Формы keine и keinen — неверный род, а nicht "
                "не отрицает существительное."
            ),
            "retry": {
                "prompt": "Бард потерял шляпу: «Ich habe ___ Hut.» (der Hut)",
                "options": ["kein", "keine", "keinen", "nicht"],
                "answer": 2,
                "explain": (
                    "der Hut — мужской род, в Akkusativ: keinen Hut. Форма "
                    "kein стоит в Nominativ или перед средним словом."
                ),
            },
        },
        {
            "id": "negation_2",
            "kind": "gap",
            "prompt": (
                "В соборе нельзя шуметь: «Im Dom singen die Leute ___ Lieder.»"
            ),
            "options": ["kein", "keine", "keinen", "nicht"],
            "answer": 1,
            "explain": (
                "die Lieder — множественное число, отрицание — keine. Формы "
                "kein и keinen во множественном числе не бывают."
            ),
            "retry": {
                "prompt": (
                    "Бард ищет ночлег: «Ich suche in Köln ___ Herberge.» "
                    "(die Herberge)"
                ),
                "options": ["kein", "keinen", "keine", "nicht"],
                "answer": 2,
                "explain": (
                    "die Herberge — женский род, Akkusativ: keine Herberge. "
                    "kein и keinen не подходят по роду."
                ),
            },
        },
        {
            "id": "negation_3",
            "kind": "transform",
            "prompt": (
                "Проводник шутит: «Der Dom ist neu.» Бард возражает: собор "
                "не новый."
            ),
            "options": [
                "Der Dom ist kein neu.",
                "Der Dom ist nicht neu.",
                "Der Dom nicht ist neu.",
                "Der Dom ist neu nicht.",
            ],
            "answer": 1,
            "explain": (
                "Прилагательное отрицаем через nicht, оно стоит перед ним: "
                "Der Dom ist nicht neu. kein ставится только перед "
                "существительным."
            ),
            "retry": {
                "prompt": (
                    "Трактирщик говорит: «Der Barde hat eine Laute.» Спой "
                    "то же с отрицанием: у барда нет лютни."
                ),
                "options": [
                    "Der Barde hat nicht Laute.",
                    "Der Barde hat kein Laute.",
                    "Der Barde hat keine Laute.",
                    "Der Barde hat keinen Laute.",
                ],
                "answer": 2,
                "explain": (
                    "eine Laute → keine Laute: женский род, Akkusativ. Формы "
                    "kein и keinen — неверный род, а nicht перед "
                    "существительным не ставится."
                ),
            },
        },
        {
            "id": "negation_4",
            "kind": "error",
            "prompt": "В песне барда одна ошибка — в отрицании. Найди её.",
            "sentence": "Ich habe nicht Geld für ein Bier.",
            "wrong": "nicht",
            "fix": {
                "options": ["keine", "kein", "keinen", "nicht"],
                "answer": 1,
                "explain": "Geld — существительное, его отрицают словом kein.",
            },
            "explain": (
                "Geld — существительное, его отрицают через kein: Ich habe "
                "kein Geld. nicht отрицает глаголы и прилагательные."
            ),
            "retry": {
                "prompt": "В песне барда одна ошибка — в отрицании. Найди её.",
                "sentence": "In der Herberge gibt es nicht Betten.",
                "wrong": "nicht",
                "fix": {
                    "options": ["kein", "keinen", "keine", "nicht"],
                    "answer": 2,
                    "explain": (
                        "die Betten — множественное число, поэтому keine."
                    ),
                },
                "explain": (
                    "die Betten — множественное число, отрицание keine: Es "
                    "gibt keine Betten. nicht перед существительным "
                    "не ставится."
                ),
            },
        },
        {
            "id": "negation_5",
            "kind": "error",
            "prompt": (
                "В песне барда одна ошибка — nicht стоит не на месте. "
                "Найди это слово."
            ),
            "sentence": "Der Barde nicht singt im Dom.",
            "wrong": "nicht",
            "fix": {
                "options": ["nicht singt", "singt nicht", "singt kein", "kein singt"],
                "answer": 1,
                "explain": (
                    "nicht стоит после спрягаемого глагола: Der Barde singt "
                    "nicht im Dom."
                ),
            },
            "explain": (
                "nicht не может стоять перед глаголом: правильно Der Barde "
                "singt nicht im Dom. Глагол в немецком предложении стоит "
                "на втором месте, а nicht — правее него."
            ),
            "retry": {
                "prompt": (
                    "В песне барда одна ошибка — nicht стоит не на месте. "
                    "Найди это слово."
                ),
                "sentence": "Wir nicht singen im Dom.",
                "wrong": "nicht",
                "fix": {
                    "options": ["nicht singen", "singen kein", "singen nicht", "kein singen"],
                    "answer": 2,
                    "explain": "Правильно: Wir singen nicht im Dom.",
                },
                "explain": (
                    "nicht ставится после глагола: Wir singen nicht im Dom. "
                    "Перед глаголом оно стоять не может."
                ),
            },
        },
        {
            "id": "negation_6",
            "kind": "translate",
            "prompt": "Переведи на немецкий: «Я не пою в соборе.»",
            "options": [
                "Ich singe kein im Dom.",
                "Ich nicht singe im Dom.",
                "Ich singe nicht im Dom.",
                "Ich singe nicht in Dom.",
            ],
            "answer": 2,
            "explain": (
                "Глагол отрицаем через nicht, оно стоит после глагола: Ich "
                "singe nicht im Dom. Перед Dom нужен артикль (im = in dem), "
                "а kein стоит только перед существительным."
            ),
            "retry": {
                "prompt": "Переведи на немецкий: «Он не поёт громко.»",
                "options": [
                    "Er singt kein laut.",
                    "Er singt nicht laute.",
                    "Er nicht singt laut.",
                    "Er singt nicht laut.",
                ],
                "answer": 3,
                "explain": (
                    "nicht стоит перед прилагательным laut: Er singt nicht "
                    "laut. kein перед прилагательным невозможен."
                ),
            },
        },
        {
            "id": "negation_7",
            "kind": "mc",
            "prompt": "Бард не знает того человека: «Ich kenne den Mann ___.»",
            "options": ["kein", "keine", "nicht", "keinen"],
            "answer": 2,
            "explain": (
                "Перед Mann стоит определённый артикль den, поэтому kein "
                "невозможен: отрицаем через nicht в конце предложения."
            ),
            "retry": {
                "prompt": (
                    "Бард в новом городе никого не знает: «Ich kenne in Köln "
                    "___ Menschen.»"
                ),
                "options": ["kein", "keinen", "keine", "nicht"],
                "answer": 1,
                "explain": (
                    "Артикля нет, значит нужно kein; der Mensch — мужской "
                    "род, в Akkusativ: keinen Menschen."
                ),
            },
        },
        {
            "id": "negation_8",
            "kind": "order",
            "prompt": "Собери предложение: в соборе люди не поют.",
            "words": ["Im", "Dom", "singen", "die", "Leute", "nicht"],
            "answer": "Im Dom singen die Leute nicht",
            "explain": (
                "Im Dom — обстоятельство на первом месте, глагол второй: "
                "singen. nicht стоит в конце: Die Leute singen nicht."
            ),
            "retry": {
                "prompt": "Собери предложение: у барда нет денег.",
                "words": ["Der", "Barde", "hat", "kein", "Geld"],
                "answer": "Der Barde hat kein Geld",
                "explain": (
                    "kein стоит перед существительным Geld: Der Barde hat "
                    "kein Geld. С существительным слово nicht "
                    "не употребляется."
                ),
            },
        },
    ],
}
