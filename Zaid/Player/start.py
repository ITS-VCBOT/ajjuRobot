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
        caption=f"""**🔥𝐈 𝐂𝐚𝐧 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜🎶 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭👅

🌸𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐅𝐫𝐞𝐞𝐥𝐲👀 !

𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 =  [々Rɪᴅᴇʀ乂࿐](https://t.me/i_ajiT)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝐇𝐞𝐥𝐩 & 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", url=f"https://t.me/ajju_support/20"
                    ),
                    InlineKeyboardButton(
                        "𝐎𝐰𝐧𝐞𝐫🥀", url=f"https://t.me/i_ajit"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🔔", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💫💖", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7c0d15fe4c1867b0eaaed.jpg",
        caption=f"""𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐀𝐝𝐝𝐢𝐧𝐠 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐂𝐡𝐚𝐭, 𝐅𝐨𝐫 𝐀𝐧𝐲 𝐐𝐮𝐞𝐫𝐲 𝐔 𝐂𝐚𝐧 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 🥀❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐉𝐨𝐢𝐧 𝐇𝐞𝐫𝐞💫👅", url=f"https://t.me/{GROUP_SUPPORT}")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/66433337a6d0e4ed51acf.jpg",
        caption=f"""𝐇𝐞𝐫𝐞 𝐈𝐬 𝐓𝐡𝐞 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 𝐅𝐨𝐫𝐤 𝐀𝐧𝐝 𝐆𝐢𝐯𝐞 𝐒𝐭𝐚𝐫'𝐬 ⭐""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ ⚒️", url=f"https://github.com/ajit-bahari")
                ]
            ]
        ),
    )
