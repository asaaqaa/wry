import asyncio

import os
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

                
@app.on_message(
    command(["مطورين فينوم ","المطورين","مطورين","مطورين NEON"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/89a4365f15f0e20cd4353.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝗩𝗘𝗡𝗢𝗠  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين NEON ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𝗩𝗘𝗡𝗢𝗠  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "DEV 𝗩𝗘𝗡𝗢𝗠 ", url=f"https://t.me/R_R_B0"), 
                 ],[

                
                    InlineKeyboardButton(
                        "★⌞ 𝗩𝗘𝗡𝗢𝗠  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/SOURCE_NEON"),
                ],

            ]

        ),

    )










@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/89a4365f15f0e20cd4353.jpg",
        caption=f"""**⩹⊷━⌞ 𝗩𝗘𝗡𝗢𝗠  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس NEON\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 𝗩𝗘𝗡𝗢𝗠  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗩𝗘𝗡𝗢𝗠", url=f"https://t.me/R_R_B0"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝗩𝗘𝗡𝗢𝗠  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/SOURCE_NEON"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/89a4365f15f0e20cd4353.jpg",
        caption=f"""**⩹⊷━⌞ 𝗩𝗘𝗡𝗢𝗠  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس NEON\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞ 𝗩𝗘𝗡𝗢𝗠  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗩𝗘𝗡𝗢𝗠", url=f"https://t.me/R_R_B0"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝗩𝗘𝗡𝗢𝗠  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/SOURCE_NEON"),
                ],

            ]

        ),

    )



    
