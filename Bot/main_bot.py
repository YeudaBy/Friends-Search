from pyrogram import Client, filters
from pyrogram.types import (Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery)
from Bot.strings import friends_images
from Bot.db import get_stats, update_lang, get_lang, update_usage, edit_favorite, create_user, get_favorites
from Bot.tools import lang_msg, request_by_sentence, dt_to_ht, request_by_id
import random

app = Client("FriendSearch")


@app.on_message(filters.command(["start", "help", "translate", "history"]) & filters.private)
def start(_, message: Message):
    create_user(user_id=message.from_user.id, lang=message.from_user.language_code)
    if message.command == ["start"]:
        message.reply(lang_msg(message, "start_msg").format(message.from_user.mention))
    elif message.command == ["history"]:
        ids = get_favorites(user_id=message.from_user.id)
        search_history = []
        for _id in ids:
            search_history.append(request_by_id(_id))
        message.reply(lang_msg(message, "history".format(search_history)))
    elif message.command == ["help"]:
        message.reply(lang_msg(message, "help_msg"))
    elif message.command == ["translate"]:
        message.reply(lang_msg(message, "translate_msg"))


@app.on_inline_query()
def search_inline(_, query: InlineQuery):
    raw_results = request_by_sentence(query.query)
    if raw_results.get("error"):
        query.answer(
            results=[],
            switch_pm_text=lang_msg(query, 'query_required'),
            switch_pm_parameter="empty"
        )
        return

    if raw_results["count"] == 0:
        query.answer(
            results=[],
            switch_pm_text=lang_msg(query, 'no_results'),
            switch_pm_parameter="empty"
        )
    results = [
        InlineQueryResultArticle(
            title=f"{lang_msg(query, 'session')} {result['season']} {lang_msg(query, 'episode')} {result['episode']} • {dt_to_ht(result['start'])}",
            description=result["content"],
            thumb_url=random.choice(friends_images),
            input_message_content=InputTextMessageContent(
                f"**✅ {lang_msg(query, 'results_title')}**\n\n"
                f"**📺 {lang_msg(query, 'appear_at')}:** `{lang_msg(query, 'session')} {result['season']} {lang_msg(query, 'episode')} {result['episode']}`\n"
                f"**🕓 {lang_msg(query, 'time')}:** `{dt_to_ht(result['start'])}`\n**💬 {lang_msg(query, 'sentence')}:** `{result['content']}` "
            ),
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(lang_msg(query, "inline_btn"),
                                     switch_inline_query_current_chat=""),
                InlineKeyboardButton(lang_msg(query, "share_btn"),
                                     switch_inline_query=query.query)
            ], [InlineKeyboardButton("❤",
                                     callback_data=str(result['id']))]])
        ) for result in raw_results["results"] if result['id']
    ]
    query.answer(results,
                 cache_time=0,  # TODO remove
                 switch_pm_text=f"{lang_msg(query, 'results_count')}: {str(raw_results['count'])}",
                 switch_pm_parameter="count")


@app.on_callback_query()
def add_to_favorites(_, callback: CallbackQuery):
    if edit_favorite(callback.from_user.id, int(callback.data)):
        callback.answer("Added to fav")
    else:
        callback.answer("Already exists!")


app.run()
