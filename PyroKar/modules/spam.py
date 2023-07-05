# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
from threading import Event

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import BLACKLIST_CHAT, BOTLOG_CHATID
from config import CMD_HANDLER as cmd
from PyroKar.helpers.basic import edit_or_reply
from PyroKar.utils.misc import extract_args

from .help import add_command_help


@Client.on_message(
    filters.me & filters.command(["spam", "dspam"], cmd)
)
async def spam_cmd(client, message):
    if message.command[0] == "spam":
        if message.reply_to_message:
            spam = await edit_or_reply(message, "`Processing...`")
            try:
                quantity = int(message.text.split(None, 2)[1])
                spam_text = message.text.split(None, 2)[2]
            except Exception as error:
                return await spam.edit(error)
            await asyncio.sleep(1)
            await message.delete()
            await spam.delete()
            for _ in range(quantity):
                await client.send_message(
                    message.chat.id,
                    spam_text,
                    reply_to_message_id=message.reply_to_message.id,
                )
                await asyncio.sleep(0.3)
        elif len(message.command) < 3:
            await edit_or_reply(message, f"**Gunakan format:\n`{cmd}spam [jumlah] [pesan]`**")
        else:
            spam = await edit_or_reply(message, "`Processing...`")
            try:
                quantity = int(message.text.split(None, 2)[1])
                spam_text = message.text.split(None, 2)[2]
            except Exception as error:
                return await spam.edit(error)
            await asyncio.sleep(1)
            await message.delete()
            await spam.delete()
            for _ in range(quantity):
                await client.send_message(message.chat.id, spam_text)
                await asyncio.sleep(0.3)
    elif message.command[0] == "dspam":
        if message.reply_to_message:
            if len(message.command) < 3:
                return await edit_or_reply(
                    message,
                    f"**Gunakan format:\n`{cmd}dspam[jumlah] [waktu delay] [balas pesan]`**",
                )
            spam = await edit_or_reply(message, "`Processing...`")
            try:
                quantity = int(message.text.split(None, 3)[1])
                delay_msg = int(message.text.split(None, 3)[2])
            except Exception as error:
                return await spam.edit(error)
            await asyncio.sleep(1)
            await message.delete()
            await spam.delete()
            for _ in range(quantity):
                await message.reply_to_message.copy(message.chat.id)
                await asyncio.sleep(delay_msg)
        else:
            if len(message.command) < 4:
                return await edit_or_reply(
                    message,
                    f"**Gunakan format:\n`{cmd}dspam[jumlah] [waktu delay] [balas pesan]`**",
                )
            spam = await edit_or_reply(message, "`Processing...`")
            try:
                quantity = int(message.text.split(None, 3)[1])
                delay_msg = int(message.text.split(None, 3)[2])
                spam_text = message.text.split(None, 3)[3]
            except Exception as error:
                return await spam.edit(error)
            await asyncio.sleep(1)
            await message.delete()
            await spam.delete()
            for _ in range(quantity):
                await client.send_message(message.chat.id, spam_text)
                await asyncio.sleep(delay_msg)


add_command_help(
    "spam",
    [
        ["spam <jumlah spam> <text>", "Mengirim teks secara spam dalam obrolan!!"],
        [
            "dspam <jumlah> <waktu delay> <balas pesan>",
            "Mengirim teks spam dengan jangka delay yang ditentukan!",
        ],
    ],
)
