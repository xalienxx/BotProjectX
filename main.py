import psutil
import shutil
import time
from utils_bot import *
from typing import Text
import re
import os
import math
import json
import heroku3
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from pyrogram.types import ReplyKeyboardMarkup

bot = Client(
    "my_bot",
    api_id=10027898,
    api_hash="c9fec38e3977983d2079069962c26206",
    bot_token="5271107256:AAFjtvI6IoSsTDECxbR2zG-WnoI4ZPPrSzs",)

KeyboardZ = ReplyKeyboardMarkup(
    [
        ["Start", "Help", "Login", "DC"],
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["Test Audio"],
        ["Follow", "Ping", "Status"],
        ["Maintainers"]

    ],
    resize_keyboard=True)


@bot.on_message((filters.command("start") | filters.regex('Start')) & filters.private & ~filters.edited)
def command(bot, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="""Hi Test Buttn!""",
        parse_mode="html",
        reply_markup=KeyboardZ)

@bot.on_message(filters.incoming & filters.command("run"))
def command(bot, message):
    bot.send_message(message.chat.id, "Bot Alive")
    bot.send_dice(message.chat.id, "🏀")
    
@bot.on_message(filters.incoming & filters.command("image"))
def command(bot, message):
    bot.send_photo(message.chat.id, "https://telegra.ph/file/4089e363161303efe4b79.png", ttl_seconds=10)
  
@bot.on_message(filters.incoming & (filters.command("audio") | filters.regex('Test Audio')) )
    bot.send_audio(message.chat.id, "https://mikasalinkgen.herokuapp.com/663/Love+Me+Now+-+John+Legend+%5BUSSM11606983%5D+%28128%29.mp3")
  

@bot.on_inline_query()
def answer(client, inline_query):
    inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="Hunter's DataBase",
                input_message_content=InputTextMessageContent(
                    "Hunters DataBase"
                ),
                url="https://t.me/HuntersDataBase",
                description="Mostly Sci-fi Database",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Join Hunter's Database",
                            url="https://t.me/HuntersDataBase"
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="Hunter's Index",
                input_message_content=InputTextMessageContent(
                    "Hunter's Index"
                ),
                url="https://t.me/HuntersIndex",
                description="Hunter DB's Index Channel",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Join Hunter's Index",
                            url="https://t.me/HuntersIndex"
                        )]
                    ]
                )
            )
        ],
        cache_time=1
    )

@bot.on_message(filters.regex("DC"))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.dc_id)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        quote=True
    )

START_TEXT = """ Your Telegram DC Is : `{}`  """

@bot.on_message(filters.regex("Ping"))
async def ping(bot, message):
    start_t = time.time()
    jv = await message.reply_text("....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await jv.edit(f"Ping!\n{time_taken_s:.3f} ms")


StartTime = time.time()

server = heroku3.from_key(HEROKU_API_KEY)
user_agent = (
                'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.149 Mobile Safari/537.36'
            )
accountid = server.account().id
headers = {
  'User-Agent': user_agent,
  'Authorization': f'Bearer {HEROKU_API_KEY}',
  'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
}

path = "/accounts/" + accountid + "/actions/get-quota"

request = requests.get("https://api.heroku.com" + path, headers=headers)

if request.status_code == 200:
  result = request.json()
  total_quota = result['account_quota']
  quota_used = result['quota_used']
  quota_left = total_quota - quota_used
  hours = math.floor(quota_left/3600)
  minutes = math.floor(quota_left/60 % 60)
  days = math.floor(hours/24)
  dyno = f"{days} days ({hours} hours)"


@bot.on_message(filters.private & filters.regex("Status"))
async def stats(bot, update):
    currentTime = readable_time((time.time() - StartTime))
    total, used, free = shutil.disk_usage('.')
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
    recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    timeleft = dyno
    botstats = f'<b>Bot Uptime:</b> {currentTime}\n' \
        f'<b>Total disk space:</b> {total}\n' \
        f'<b>Used:</b> {used}  ' \
        f'<b>Free:</b> {free}\n\n' \
        f'Data Usage:\n<b>Upload:</b> {sent}\n' \
        f'<b>Down:</b> {recv}\n\n' \
        f'<b>CPU:</b> {cpuUsage}% ' \
        f'<b>RAM:</b> {memory}% ' \
        f'<b>Disk:</b> {disk}%' \
        f'<b>Heroku Left:</b> {timeleft}'
    await update.reply_text(botstats)

    
    
bot.run()
