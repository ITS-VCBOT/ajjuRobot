import asyncio
from time import time
from datetime import datetime
from config import BOT_USERNAME
from config import GROUP_SUPPORT, UPDATES_CHANNEL, START_PIC
from Zaid.filters import command
from Zaid.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**๐ฅ๐ ๐๐๐ง ๐๐ฅ๐๐ฒ ๐๐ฎ๐ฌ๐ข๐๐ถ ๐๐ง ๐๐จ๐ฎ๐ซ ๐๐ซ๐จ๐ฎ๐ฉ ๐๐จ๐ข๐๐ ๐๐ก๐๐ญ๐

๐ธ๐๐๐ ๐๐ ๐๐จ ๐๐จ๐ฎ๐ซ ๐๐ซ๐จ๐ฎ๐ฉ ๐๐ง๐ ๐๐ฅ๐๐ฒ ๐๐ฎ๐ฌ๐ข๐ ๐๐ซ๐๐๐ฅ๐ฒ๐ !

๐๐ ๐๐จ๐ฎ ๐๐๐ฏ๐ ๐๐ง๐ฒ ๐๐ฎ๐๐ฌ๐ญ๐ข๐จ๐ง๐ฌ ๐๐ง๐ ๐๐๐ฅ๐ฉ ๐๐ก๐๐ง ๐๐ฆ ๐๐ฒ ๐๐๐ฏ๐๐ฅ๐จ๐ฉ๐๐ซ =  [ใRษชแดแดสไนเฟ](https://t.me/i_ajiT)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ โฐ แดแดแด แดแด แดแด สแดแดส ษขสแดแดแด โฑ โ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐๐๐ฅ๐ฉ & ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ", url=f"https://t.me/ajju_support/20"
                    ),
                    InlineKeyboardButton(
                        "๐๐ฐ๐ง๐๐ซ๐ฅ", url=f"https://t.me/i_ajit"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐๐ฉ๐๐๐ญ๐๐ฌ ๐", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ ๐ซ๐", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7c0d15fe4c1867b0eaaed.jpg",
        caption=f"""๐๐ก๐๐ง๐ค๐ฌ ๐๐จ๐ซ ๐๐๐๐ข๐ง๐? ๐๐ ๐๐จ ๐๐จ๐ฎ๐ซ ๐๐ก๐๐ญ, ๐๐จ๐ซ ๐๐ง๐ฒ ๐๐ฎ๐๐ซ๐ฒ ๐ ๐๐๐ง ๐๐จ๐ข๐ง ๐๐ฎ๐ซ ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ ๐๐ซ๐จ๐ฎ๐ฉ ๐ฅโค๏ธ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐๐จ๐ข๐ง ๐๐๐ซ๐๐ซ๐", url=f"https://t.me/{GROUP_SUPPORT}")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/66433337a6d0e4ed51acf.jpg",
        caption=f"""๐๐๐ซ๐ ๐๐ฌ ๐๐ก๐ ๐๐จ๐ฎ๐ซ๐๐ ๐๐จ๐๐ ๐๐จ๐ซ๐ค ๐๐ง๐ ๐๐ข๐ฏ๐ ๐๐ญ๐๐ซ'๐ฌ โญ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " สแดแดแด โ๏ธ", url=f"https://github.com/ajit-bahari")
                ]
            ]
        ),
    )
