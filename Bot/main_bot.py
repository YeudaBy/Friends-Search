import re
from typing import Union
import requests
from pyrogram import Client, filters
from pyrogram.types import (Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardButton, InlineKeyboardMarkup)
from Bot.strings import strings, friends_icons
import random

app = Client("FriendSearch")


def request(query: str) -> dict:
    endpoint = f"http://127.0.0.1:5000/api/search?query={query}"
    return requests.get(endpoint).json()


def lang_msg(msg_obj: Union[Message, InlineQuery], msg_to_rpl: str) -> Union[str, bool]:
    msg = strings.get(msg_to_rpl)
    if not msg:
        return False
    lang_client = msg_obj.from_user.language_code
    if msg.get(lang_client):
        return msg[lang_client]
    else:
        return msg["en"]


def dt_to_ht(timedelta: str) -> str:
    """ convert timedelta to human time """
    return re.search(r"0:(?P<ht>[0-9]{2}:[0-9]{2})\.[0-9]+", timedelta).groupdict().get("ht")


@app.on_message(filters.command(["start", "help", "translate"]) & filters.private)
def start(_, message: Message):
    if message.command == ["start"]:
        message.reply(lang_msg(message, "start_msg").format(message.from_user.mention))
    elif message.command == ["help"]:
        message.reply(lang_msg(message, "help_msg"))
    elif message.command == ["translate"]:
        message.reply(lang_msg(message, "translate_msg"))


@app.on_inline_query()
def search_inline(_, query: InlineQuery):
    raw_results = request(query.query)
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
            thumb_url=random.choice(friends_icons),
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
            ]])
        ) for result in raw_results["results"]
    ]
    query.answer(results,
                 cache_time=0,  # TODO remove
                 switch_pm_text=f"{lang_msg(query, 'results_count')}: {str(raw_results['count'])}",
                 switch_pm_parameter="count")


app.run()
