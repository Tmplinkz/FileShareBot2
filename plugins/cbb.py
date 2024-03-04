#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>\n○  ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/Dumb_luffy'>LUFFY</a>\n○  ʟᴀɴɢᴜᴀɢᴇ : python 3\n○  Main Channel : <a href=https://t.me/XAnime_Universe>XANIME UNIVERSE</a>\n○  Ongoing Channel : <a href=https://t.me/XAnime_Ongoing> XANIME ONGOING</a>\n</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
