import asyncio
import os
import config
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint
from pyrogram import filters
from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")


@app.on_message(
    command(["سورس سيمو","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://t.me/vd_d_dd/20",
        caption=f"""**╭── • [⌯𝗦𝗨𝗢𝗥𝗖𝗘:NEON](https://t.me/SOURCE_NEON) • ──╮**

**[⌯𝗗𝗘𝗩: NEON](https://t.me/SOURCE_NEON)**

**[⌯𝗦𝗨𝗣𝗣𝗨𝗥𝗧: NEON](https://t.me/R_N_B1)**

**[⌯𝗖𝗛𝗔𝗡𝗡𝗘𝗟: NEON](https://t.me/SOURCE_NEON)**

**[⌯𝗠𝗔𝗞𝗘𝗥: NEON](https://t.me/B72_BOT)**

**╰── • [⌯𝗦𝗨𝗢𝗥𝗖𝗘:NEON](https://t.me/SOURCE_NEON) • ──╯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "HeLp GrUoB.", url=f"https://t.me/R_N_B1"), 
                ],[
                    InlineKeyboardButton(
                        "𝗗𝗘𝗩 VENOM ◍", url=f"https://t.me/SOURCE_NEON"),
                ],[
                    InlineKeyboardButton(
                        "أضغط لاضافه ألبوت لمجموعتك ◍", url=f"https://t.me/?startgroup=true"),
                ],

            ]

        ),

    )
    


@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )



