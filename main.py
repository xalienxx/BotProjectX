from pyrogram import Client, filters
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

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
        ["Follow", "Ping", "Status"],
        ["Maintainers"]

    ],
    resize_keyboard=True)




@bot.on_message(filters.incoming & filters.command("run"))
def command(bot, message):
    bot.send_message(message.chat.id, "Bot Alive")
    bot.send_dice(message.chat.id, "🏀")
    
@bot.on_message(filters.incoming & filters.command("image"))
def command(bot, message):
    bot.send_photo(message.chat.id, "https://telegra.ph/file/4089e363161303efe4b79.png", ttl_seconds=10)
  
@bot.on_message(filters.incoming & filters.command("audio"))
def command(bot, message):
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


bot.run()
