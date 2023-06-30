# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

from asyncio import sleep

from pyrogram import filters

from . import *


@bots.on_message(filters.me & filters.command("save", cmd))
async def simpan_note(client, message):
    name = get_arg(message)
    user_id = message.from_user.id
    message.chat.id
    msg = message.reply_to_message
    if not msg:
        return await message.reply("`Silakan balas ke pesan.`")
    botlog_chat_id = await get_botlog(user_id)
    if not botlog_chat_id:
        return await message.reply(
            "`Maaf, tidak dapat menemukan ID chat log bot.`\nPastikan Anda Telah Mengtur Log Group Anda"
        )
    anu = await msg.copy(botlog_chat_id)
    msg_id = anu.id
    await client.send_message(
        botlog_chat_id,
        f"#NOTE\nKEYWORD: {name}"
        "\n\nPesan berikut disimpan sebagai data balasan catatan untuk obrolan, mohon jangan dihapus !!",
        reply_to_message_id=anu.id,
    )
    await sleep(1)
    await save_note(user_id, name, msg_id)
    await message.reply(f"**Berhasil menyimpan catatan dengan nama** `{name}`")


@bots.on_message(filters.me & filters.command("get", cmd))
async def panggil_notes(client, message):
    name = get_arg(message)
    user_id = message.from_user.id
    botlog_chat_id = await get_botlog(user_id)
    _note = await get_note(user_id, name)
    if not _note:
        return await message.reply("`Tidak ada catatan seperti itu.`")
    msg = message.reply_to_message or message
    msg_o = await client.get_messages(botlog_chat_id, _note)
    await msg_o.copy(message.chat.id, reply_to_message_id=msg.id)


@bots.on_message(filters.me & filters.command("rm", cmd))
async def remove_notes(client, message):
    name = get_arg(message)
    user_id = message.from_user.id
    deleted = await delete_note(user_id, name)
    if deleted:
        await message.reply(f"**Berhasil Menghapus Catatan:** `{name}`")
    else:
        await message.reply(f"**Tidak dapat menemukan catatan:** `{name}`")


@bots.on_message(filters.me & filters.command("notes", cmd))
async def get_notes(client, message):
    user_id = message.from_user.id
    await get_botlog(user_id)
    _notes = await get_note_names(user_id)
    if not _notes:
        return await message.reply("**Tidak ada catatan.**")
    msg = f"** Daftar catatan**\n\n"
    for note in _notes:
        msg += f"**•** `{note}`\n"
    await message.reply(msg)


__MODULE__ = "notes"
__HELP__ = f"""
✘ Bantuan Untuk Notes

๏ Perintah: <code>{cmd}save</code> [nama catatan] [balas pesan]
◉ Penjelasan: Untuk menyimpan catatan.

๏ Perintah: <code>{cmd}get</code> [nama catatan]
◉ Penjelasan: Untuk mengambil catatan.
           
๏ Perintah: <code>{cmd}rm</code> [nama catatan]
◉ Penjelasan: Untuk menghapus catatan.
           
๏ Perintah: <code>{cmd}notes</code>
◉ Penjelasan: Untuk melihat semua catatan.
"""
