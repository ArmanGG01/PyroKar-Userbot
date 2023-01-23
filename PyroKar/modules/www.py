# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import time
from datetime import datetime

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from config import CMD_HANDLER as cmd
from config import BOT_VER, BRANCH as brch
from PyroKar import CMD_HELP, StartTime
from PyroKar.helpers.basic import edit_or_reply
from PyroKar.helpers.constants import WWW
from PyroKar.helpers.PyroHelpers import SpeedConvert
from PyroKar.utils.tools import get_readable_time
from PyroKar.helpers.adminHelpers import DEVS

from .help import add_command_help

modules = CMD_HELP

@Client.on_message(filters.command(["speed", "speedtest"], cmd) & filters.me)
async def speed_test(client: Client, message: Message):
    new_msg = await edit_or_reply(message, "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(filters.command("dc", cmd) & filters.me)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )


@Client.on_message(
    filters.command("ceping", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["ping"], ".") & filters.me)
async def module_ping(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif not message.reply_to_message and len(cmd) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="ping")
            await asyncio.gather(
                message.delete(),
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id
                ),
            )
        except BaseException as e:
            print(f"{e}")


@Client.on_message(
    filters.command("cping", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("kping", cmd) & filters.me)
async def kping(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(message, "8✊===D")
    await xx.edit("8=✊==D")
    await xx.edit("8==✊=D")
    await xx.edit("8===✊D")
    await xx.edit("8===✊D💦")
    await xx.edit("Ahhhhhhhh Akhirnya Keluar Jugak 💦💦")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.reply(
        f"❏ **PONG!!🏓**\n"
        f"├• **Pinger** - `%sms`\n"
        f"├• **Uptime -** `{uptime}` \n"
        f"└• **Owner :** {client.me.mention}" % (duration)
    )

@Client.on_message(filters.command("kar", cmd) & filters.me)
async def ramping(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        "PyRokar-Userbot\n"
        "ㅤㅤStatus : 𝘗𝘳𝘦𝘮𝘪𝘶𝘮\n"
        f"ㅤㅤㅤㅤping bot:"
        f"`%sms` \n"
        f"ㅤㅤㅤㅤmodules:</b> <code>{len(modules)} Modules</code> \n"
        f"ㅤㅤㅤㅤbot version: {BOT_VER} \n"
        f"ㅤㅤㅤㅤbot uptime:"
        f"`{uptime}` \n"
        f"ㅤㅤㅤㅤbranch: {brch} \n\n"
        f"ㅤㅤㅤㅤOwner : {client.me.mention}" % (duration)
    )


add_command_help(
    "speedtest",
    [
        ["dc", "Untuk melihat DC Telegram anda."],
        [
            f"speedtest `atau` {cmd}speed",
            "Untuk megetes Kecepatan Server anda.",
        ],
    ],
)


add_command_help(
    "ping",
    [
        ["ping", "Untuk Menunjukkan Ping Bot Anda."],
        ["kping", "Untuk Menunjukkan Ping Bot Anda ( Beda animasi doang )."],
    ],
)
