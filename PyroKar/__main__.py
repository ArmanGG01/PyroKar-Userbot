import importlib
from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from PyroKar import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots, app, ids
from PyroKar.helpers.misc import create_botlog, heroku
from PyroKar.modules import ALL_MODULES
MSG_ON = """
💢 **PyroKar-Userbot Udah Aktif** 💢
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
❍▹ **Userbot Version -** `{}`
❍▹ **Ketik** `{}kar` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    print("Memulai PyroKar Userbot..")
    print("Loading Everything.")
    for all_module in ALL_MODULES:
        importlib.import_module("PyroKar.modules" + all_module)
        print(f"Successfully Imported {all_module} ")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("hdiiofficial")
            await bot.join_chat("StoryMan01")
            await bot.join_chat("Pyr0kar")
            await bot.join_chat("TestiAllPaymat")
            await bot.join_chat("obrolansuar")
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
            except BaseException:
                                 pass
            print(f"Started as {bot.me.first_name} | {bot.me.id} ")
            ids.append(bot.me.id)
        except Exception as e:
            print(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("PyroKar").info("Starting PyroKar Userbot")
    install()
    heroku()
    LOOP.run_until_complete(main())
