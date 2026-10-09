# --------------------------------------------------------------------------
# Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
# SimmyMusic — High-Performance Telegram Voice Chat Music & Video Engine
# Licensed under the MIT License. See LICENSE in the project root for details.
# --------------------------------------------------------------------------

import time

import psutil

from SIMMY_X_MUSIC.misc import _boot_
from SIMMY_X_MUSIC.utils.formatters import get_readable_time


async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)
    UP = f"{get_readable_time(bot_uptime)}"
    CPU = f"{psutil.cpu_percent(interval=0.5)}%"
    RAM = f"{psutil.virtual_memory().percent}%"
    DISK = f"{psutil.disk_usage('/').percent}%"
    return UP, CPU, RAM, DISK
