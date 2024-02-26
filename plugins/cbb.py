#Telegram- @StupidBoi69


from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"""<b>```
            ┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓
            ┃ Developer : <a href='tg://user?id={OWNER_ID}'>Stupidboi69</a>
            ┃ Creator: <a href='tg://user?id={OWNER_ID}'> This Person</a>
            ┃ Language : Python3
            ┃ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>
            ┃ Source Code: <a href=https://t.me/Stupidboi69>Talk to him.</a>
            ┃ Main Channel : <a href=https://t.me/Anime_DownLord>​Click Here​</a>
            ┃ Anime DownLoad Group : <a href=https://t.me/Anime_DownLoad_Group>Click Here</a>
            ┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛```</b>""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🌺 Contact him for personal bot 🌸', url=f'https://t.me/Stupidboi69')
                    ],
                    [
                        InlineKeyboardButton("🛟 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
