import os

from dotenv import load_dotenv

load_dotenv()

# Бот работает только от имени сообщества (паблика): нужен токен сообщества
# VK_GROUP_TOKEN и включённый Bots Long Poll API. Личный аккаунт не нужен.
GROUP_TOKEN = os.getenv("VK_GROUP_TOKEN", "").strip()

# Необязательно: id сообщества. Если пусто — определяется по токену.
GROUP_ID = os.getenv("VK_GROUP_ID", "").strip()

DB_PATH = os.getenv("DB_PATH", "").strip() or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "bot.db")
API_VERSION = os.getenv("VK_API_VERSION", "").strip() or "5.199"

# Small delay between outgoing messages to reduce flood risk.
try:
    SEND_DELAY = float(os.getenv("SEND_DELAY", "").strip() or "0.4")
except ValueError:
    SEND_DELAY = 0.4
