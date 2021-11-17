import os
from pyrogram import Client, filters
from pyrogram.types import *

from TGNRobot.conf import get_str_key
from TGNRobot import pbot

RISHABH_TEXT = "**I am owner of  [LUCY](https://telegra.ph/file/b665b65ee94c1eb7f56b9.jpg) bot"
IMAGE  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("SUPPORT 🔥", url=f"https://t.me/LOCYS"),
        InlineKeyboardButton(" UPDATES💫", url=f"https://t.me/LOCYS"),
      ],[
        InlineKeyboardButton("RISHABH HERE 😏", url="https://t.me/MAFIARishaBH"),
        InlineKeyboardButton("ABOUT ME ⚡", url="https://t.me/RISHABHANANDX"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["rishabh"]))
async def rishabh(pbot, update):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b665b65ee94c1eb7f56b9.jpg",
        caption=f"""**THIS BOT HAS BEEN MADE VAI MAFAI RISHABH**

**ITS JUST MY HARDWORK...**""",
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
