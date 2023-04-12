import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from YinsRobot.events import register
from YinsRobot import telethn as tbot

yinzver = "2.0.22"
PHOTO = "https://telegra.ph/file/1e6668536f33065817c3b.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm GSID Robot.** \n\n"
  TEXT += "✨ **Saya bekerja dengan benar** \n\n"
  TEXT += f"✨ **Owner : [Idamanmu](https://t.me/Archanistz)** \n\n"
  TEXT += f"✨ **Library Version    :** `{telever}` \n\n"
  TEXT += f"✨ **Telethon Version   :** `{tlhver}` \n\n"
  TEXT += f"✨ **Pyrogram Version   :** `{pyrover}` \n\n"
  TEXT += f"✨ **GSIDRobot Version  :** `{yinzver}` \n\n"
  TEXT += "**Terima Kasih Telah Menambahkan Saya ✨**"
  BUTTON = [[Button.url("Bantuan", "https://t.me/goldensid_bot?start=help"), Button.url("Support", "https://t.me/Zenzproject")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
