# --------------------------------------------------------------------------
# Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
# SimmyMusic — High-Performance Telegram Voice Chat Music & Video Engine
# Licensed under the MIT License. See LICENSE in the project root for details.
# --------------------------------------------------------------------------

from pyrogram import filters
from pyrogram.types import Message

from SIMMY_X_MUSIC import app
from SIMMY_X_MUSIC.core.call import RAUSHAN
from SIMMY_X_MUSIC.utils.database import is_music_playing, music_off
from SIMMY_X_MUSIC.utils.decorators import AdminRightsCheck
from SIMMY_X_MUSIC.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await RAUSHAN.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
