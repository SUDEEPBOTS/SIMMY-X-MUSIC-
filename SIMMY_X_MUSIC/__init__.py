# --------------------------------------------------------------------------
# Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
# SimmyMusic — High-Performance Telegram Voice Chat Music & Video Engine
# Licensed under the MIT License. See LICENSE in the project root for details.
# --------------------------------------------------------------------------

from SIMMY_X_MUSIC.core.bot import RAUSHAN
from SIMMY_X_MUSIC.core.dir import dirr
from SIMMY_X_MUSIC.core.git import git
from SIMMY_X_MUSIC.core.userbot import Userbot
from SIMMY_X_MUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = RAUSHAN()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
