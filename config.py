import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "")
    API_HASH = getenv("API_HASH", "")
    TOKEN = getenv("TOKEN", "")
    OWNER_ID = getenv("OWNER_ID", "")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "")
    STRING_SESSION = getenv("STRING_SESSION", "") #telethon
    OWNER_USERNAME = getenv("OWNER_USERNAME", "")
    DB_URI = getenv("DATABASE_URL", "")
    DB_URI = DB_URI.replace("postgres", "")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "")
    GBAN_LOGS = getenv("GBAN_LOGS", "")
    SYS_ADMIN = getenv("SYS_ADMIN", "")
    DEV_USERS = getenv("DEV_USERS", "")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CHANNEL = getenv("CHANNEL", "")
    SUPPORT = getenv("SUPPORT", "")
    START_IMG = os.environ.get("START_IMG", "")
    CMD_IMG = os.environ.get("CMD_IMG", "")
    CASH_API_KEY = getenv("CASH_API_KEY", "")
    TIME_API_KEY = getenv("TIME_API_KEY", "")
    WALL_API = getenv("WALL_API", "")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "")
    CF_API_KEY = getenv("CF_API_KEY", "")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
    Obanai_USER = list(map(int, getenv("DEV_USERS", "").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
