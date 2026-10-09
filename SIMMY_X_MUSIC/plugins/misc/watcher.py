# --------------------------------------------------------------------------
# Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
# SimmyMusic — High-Performance Telegram Voice Chat Music & Video Engine
# Licensed under the MIT License. See LICENSE in the project root for details.
# --------------------------------------------------------------------------

from pyrogram import filters
from pyrogram.types import Message

from SIMMY_X_MUSIC import app
from SIMMY_X_MUSIC.core.call import RAUSHAN

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await RAUSHAN.stop_stream_force(message.chat.id)
