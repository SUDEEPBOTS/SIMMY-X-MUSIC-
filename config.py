# --------------------------------------------------------------------------
# Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
# SimmyMusic — High-Performance Telegram Voice Chat Music & Video Engine
# Licensed under the MIT License. See LICENSE in the project root for details.
# --------------------------------------------------------------------------

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ===============================================
# Telegram API Credentials
# ===============================================
API_ID = int(getenv("API_ID", 0)) if getenv("API_ID") else 0
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)

# ===============================================
# Bot Administration & Ownership
# ===============================================
OWNER_ID = int(getenv("OWNER_ID", 0)) if getenv("OWNER_ID") else 0
OWNER_USERNAME = getenv("OWNER_USERNAME", "heartstealer_x")
LOGGER_ID = int(getenv("LOGGER_ID", 0)) if getenv("LOGGER_ID") else 0

BOT_USERNAME = getenv("BOT_USERNAME", "SimmyMusicBot")
BOT_NAME = getenv("BOT_NAME", "Simmy Music")

# ===============================================
# Database & Streaming Configuration
# ===============================================
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# ===============================================
# Heroku / Cloud Deployment
# ===============================================
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# ===============================================
# Git Upstream Configuration
# ===============================================
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/SUDEEPBOTS/SIMMY-X-MUSIC-")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# ===============================================
# Community & Support Channels
# ===============================================
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/heartstealer_x")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+N08m5L1mCTU2NTE1")

# ===============================================
# Assistant Management
# ===============================================
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# ===============================================
# Music Platform Resolvers
# ===============================================
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# ===============================================
# Pyrogram String Sessions
# ===============================================
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# ===============================================
# Dynamic State Containers
# ===============================================
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ===============================================
# UI Asset Badges & Artwork
# ===============================================
START_IMG_URL = getenv("START_IMG_URL", "https://raw.githubusercontent.com/SUDEEPBOTS/SIMMY-X-MUSIC-/main/assets/banner.png")
PING_IMG_URL = getenv("PING_IMG_URL", "https://raw.githubusercontent.com/SUDEEPBOTS/SIMMY-X-MUSIC-/main/assets/banner.png")

PLAYLIST_IMG_URL = "https://raw.githubusercontent.com/SUDEEPBOTS/SIMMY-X-MUSIC-/main/assets/banner.png"
STATS_IMG_URL = "https://raw.githubusercontent.com/SUDEEPBOTS/SIMMY-X-MUSIC-/main/assets/banner.png"
TELEGRAM_AUDIO_URL = "https://raw.githubusercontent.com/SUDEEPBOTS/SIMMY-X-MUSIC-/main/assets/banner.png"
TELEGRAM_VIDEO_URL = "https://raw.githubusercontent.com/SUDEEPBOTS/SIMMY-X-MUSIC-/main/assets/banner.png"
STREAM_IMG_URL = "https://raw.githubusercontent.com/SUDEEPBOTS/SIMMY-X-MUSIC-/main/assets/banner.png"
SOUNCLOUD_IMG_URL = "https://raw.githubusercontent.com/SUDEEPBOTS/SIMMY-X-MUSIC-/main/assets/banner.png"
YOUTUBE_IMG_URL = "https://raw.githubusercontent.com/SUDEEPBOTS/SIMMY-X-MUSIC-/main/assets/banner.png"
SPOTIFY_ARTIST_IMG_URL = "https://raw.githubusercontent.com/SUDEEPBOTS/SIMMY-X-MUSIC-/main/assets/banner.png"
SPOTIFY_ALBUM_IMG_URL = "https://raw.githubusercontent.com/SUDEEPBOTS/SIMMY-X-MUSIC-/main/assets/banner.png"
SPOTIFY_PLAYLIST_IMG_URL = "https://raw.githubusercontent.com/SUDEEPBOTS/SIMMY-X-MUSIC-/main/assets/banner.png"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")
