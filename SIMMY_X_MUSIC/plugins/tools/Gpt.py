# --------------------------------------------------------------------------
# Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
# SimmyMusic — High-Performance Telegram Voice Chat Music & Video Engine
# Licensed under the MIT License. See LICENSE in the project root for details.
# --------------------------------------------------------------------------

from config import BANNED_USERS
from pyrogram import filters
from pyrogram.enums import ChatAction
from PurviAPI import api
from SIMMY_X_MUSIC import app


@app.on_message(filters.command(["chatgpt", "ai", "ask"]) & ~BANNED_USERS)
async def chatgpt_chat(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text(
            "Example:\n\n`/ai write simple website code using html css, js?`"
        )
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])

    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    results = await api.chatgpt(user_input)
    await message.reply_text(results)


__MODULE__ = "CʜᴀᴛGᴘᴛ"
__HELP__ = """
/advice - ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ ʙʏ ʙᴏᴛ
/ai [ǫᴜᴇʀʏ] - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ᴄʜᴀᴛɢᴘᴛ's ᴀɪ
/gemini [ǫᴜᴇʀʏ] - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ's ɢᴇᴍɪɴɪ ᴀɪ"""
