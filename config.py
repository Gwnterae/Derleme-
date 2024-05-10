import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "25891829")) #ASİSTAN APİ İD
API_HASH = getenv("API_HASH", "86ae507ce3fac59aba36a83d54794c0") #ASİSTAN APİ HASH
BOT_TOKEN = getenv("BOT_TOKEN", "6659155018:AAF-8PgkOXxn3WG-Vk5mvfiJGkbOiU9_9ao9") #BOT TOKEN
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://botmuzik654:muziks@cluster0.5ory5au.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 500))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002085023075")) #LOG GRUBU İD'Sİ -100 İLE BAŞLAMALI
OWNER_ID = int(getenv("OWNER_ID", 6437967819)) #OWNER İD
SAHİB= getenv("SAHİB", "https://t.me/Cankabusunefendisi") #OWNER KULLANICI ADI 
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AHMET1346z/Sonsuz", #REPO LİNKİ
)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/sonsuzsohbet") #DESTEK KANALI LİNKİ
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sonsuzsohbet") #DESTEK GRUBU LİNKİ
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
STRING1 = getenv("STRING_SESSION", "BADC13pa4SV9G7BHsma1cSzBQtS-9yJp7m9k6pSSYvQgT9WLrb8Bn4P3gsII8TKvjNd8ps6939-gIP8Ac50_F_rEWD_F8ZIHxYLZT8Fu2QUyQZIzhtgH90265QKsDqJ1VVfreMPaLeClJn67flZQcBY9h4eSjpHKX6OP3kfx0lc6VcUNnMJbyNQNrTxXzGajVLUlnWRvDbL9egb7KOSNdH9KX7vbHvwY3z-6H4YB8ocl-uRLE0Vgl-gC9qo4CnZuf-N6yBD2Bq_zHfhR4TopoGgtIwXLfAL6cYReiKao2IzPJ0HmN3EeSsGKrf5AGnlww-MNKjJGTRKhtL04DeXH-tqmAAAAAZM1UmY") #ASİSTAN SESSİON
STRING2 = getenv("STRING_SESSION2", "BACyKdyCS8sgrZnOyAg7yryHY-qf6Soso2fZym7YoikVYYlPTz2y688WLy11F_R2hw5hszp-HwENlGlgqPBa1ISAhCzGV-gVc86IXIR_XjMZ23qPi7kz53tqoFgsH3NKXyGSgiF2oENup8_C0iaH8y1hg5xXtUv5ebJPacjOlKQl8HQ_CzU2jzPbTweHPo7Or-0ZwH00xLWtT7jZgJF-cwVcaSSt6T2s9u0RgZsbdFw_NDM5HnaR-03rTyR0oNl8rPBhAkwEed_eBy6XUY7rvnasrNDPkdvIxm74Te3l-FsEHOgsr4AqXQQPG5cKq4BFDTe6MUTStWvq1FCt_akcBx2FAAAAAYQFCX8") #ASİSTAN SESSİON
STRING3 = getenv("STRING_SESSION3", "BAAR78S4NLqdlqG69nBAzx5DzObb3LUOdo5nftJPcx0sFWfT8xMCCH_9Ul0bf7t5rwv1EecPtaW12AcM1HJnMkXEe2cT84il0QSG2a1DhxnZXLFUG_7ra87g1ByU28aB1uswXMTZ5_FFb3stTgSq4eEO-FTLLI_bpLeBdZByfGQc1uKPiTgtw1edyEuRUeQjIU_WRYgTDvFUFYlbkXc2uVuZ07PVXHT8AQykMbysnky37ePv8aNgEofIAokPQ81tOkyvrsDVLRRKPNQeG9CQVQLDO25J-JbMFfOzVGKS0y8esIUo6nF9XhnF5GilziwFNUjEEtdCgz2z0zPj0_uvnxnfAAAAAYev7kc") #ASİSTAN SESSİON
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)
# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/b79290e357a600dc3ab43.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/b79290e357a600dc3ab43.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
