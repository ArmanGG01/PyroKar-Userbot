import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "PyroKar"])

async def join(client):
    try:
        await client.join_chat("obrolansuar")
        await client.join_chat("Karc0de")
    except BaseException:
        pass
