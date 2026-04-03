import asyncio
import importlib

from pyrogram import idle

import config
from SIMMY_X_MUSIC import LOGGER, app, userbot
from SIMMY_X_MUSIC.core.call import RAUSHAN
from SIMMY_X_MUSIC.misc import sudo
from SIMMY_X_MUSIC.plugins import ALL_MODULES
from SIMMY_X_MUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 V2 𝐒𝐞𝐬𝐬𝐢𝐨𝐧🤬"
        )

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("SIMMY_X_MUSIC.plugins" + all_module)
    LOGGER("SIMMY_X_MUSIC.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await RAUSHAN.start()
    await RAUSHAN.decorators()
    LOGGER("SIMMY_X_MUSIC").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝗔𝗟𝗣𝗛𝗔♨️\n╚═════ஜ۩۞۩ஜ════╝")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("SIMMY_X_MUSIC").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝗔𝗟𝗣𝗛𝗔♨️\n╚═════ஜ۩۞۩ஜ════╝")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
