from pyrogram import Client, filters
from pyrogram.handlers import CallbackQueryHandler, InlineQueryHandler, MessageHandler
from os import getenv
from dotenv import load_dotenv
from Bot.handlers import ask_change_lang, change_language, close_msg, edit_to, ask_to_report, report, search_by_id, \
    search_inline, show_msg
from Bot.favorites import show_favorites, edit_favorites, remove_favorite_from_list

load_dotenv()
app = Client(
    "FriendSearch",
    api_id=int(getenv("API_ID")),
    api_hash=getenv("API_HASH"),
    bot_token=getenv("MAIN_TOKEN")
)

handlers = [
    CallbackQueryHandler(ask_change_lang, filters=filters.regex("^change_lang$")),
    CallbackQueryHandler(show_favorites, filters=filters.regex("^favs$")),
    CallbackQueryHandler(change_language, filters=filters.regex(r"^l/[a-z]+$")),
    CallbackQueryHandler(close_msg, filters=filters.regex("^close_msg$")),
    CallbackQueryHandler(edit_to, filters=filters.regex(r"^\d+$")),
    CallbackQueryHandler(ask_to_report, filters=filters.regex(r"^r/\d+$")),
    CallbackQueryHandler(report, filters=filters.regex(r"^(y|n)/\d+$")),
    CallbackQueryHandler(edit_favorites, filters=filters.regex(r"^f/\d+$")),
    CallbackQueryHandler(remove_favorite_from_list, filters=filters.regex("^rf/\d+$")),
    InlineQueryHandler(search_by_id, filters=filters.regex(r"^\d+$")),
    InlineQueryHandler(search_inline, ~filters.regex(r"^\d+$")),
    MessageHandler(show_msg, filters=filters.regex(r"^/.*") & filters.private)
]

for handler in handlers:
    app.add_handler(handler)

app.run()
