from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message

from PyroKar.helpers import *
from PyroKar.helpers.SQL.notes_sql import *
from PyroKar.utils import *
from PyroKar import *
from .help import add_command_help

cmd = [",", ".", "?", "*", "!" "$",]

@Client.on_message(filters.command("notes", cmd) & filters.me)
async def list_notes(client, message):
    user_id = message.from_user.id
    notes = get_notes(str(user_id))
    if not notes:
        return await message.reply("Tidak ada catatan.")
    msg = f"➣ Daftar catatan\n\n"
    for note in notes:
        msg += f"◉ {note.keyword}\n"
    await message.reply(msg)


@Client.on_message(filters.command("delnote", cmd) & filters.me)
async def remove_notes(client, message):
    notename = get_arg(message)
    user_id = message.from_user.id
    if rm_note(str(user_id), notename) is False:
        return await message.reply(
            "Tidak dapat menemukan catatan: {}".format(notename)
        )
    return await message.reply("Berhasil Menghapus Catatan: {}".format(notename))


@Client.on_message(filters.command("save", cmd) & filters.me)
async def simpan_note(client, message):
    keyword = get_arg(message)
    user_id = message.from_user.id
    msg = message.reply_to_message
    if not msg:
        return await message.reply("Tolong balas ke pesan")
    anu = await msg.forward(client.me.id)
    msg_id = anu.id
    await client.send_message(client.me.id,
        f"#NOTE\nKEYWORD: {keyword}"
        "\n\nPesan berikut disimpan sebagai data balasan catatan untuk obrolan, mohon JANGAN dihapus !!",
    )
    await sleep(1)
    add_note(str(user_id), keyword, msg_id)
    await message.reply(f"Berhasil menyimpan note {keyword}")


@Client.on_message(filters.command("get", cmd) & filters.me)
async def panggil_notes(client, message):
    notename = get_arg(message)
    user_id = message.from_user.id
    note = get_note(str(user_id), notename)
    if not note:
        return await message.reply("Tidak ada catatan seperti itu.")
    msg_o = await client.get_messages(client.me.id, int(note.f_mesg_id))
    await msg_o.copy(message.chat.id, reply_to_message_id=message.id)

add_command_help(
    "notes",
    [
        ["save [text/reply]",
            "Simpan pesan ke Group. (bisa menggunakan stiker)"],
        ["get [nama]",
            "Ambil catatan ke tersimpan"],
        ["notes",
            "Lihat Daftar Catatan"],
        ["delnote [nama]",
            "Menghapus nama catatan"],
    ],
    )
