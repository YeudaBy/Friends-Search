import re
from typing import Union
import requests
from pyrogram import Client, filters
from pyrogram.raw.base import reply_markup
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


def dt_to_ht(deltatime: str) -> str:
    return re.search(r"0:(?P<ht>[0-9]{2}:[0-9]{2})\.[0-9]+", deltatime).groupdict().get("ht")


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
            switch_pm_parameter="StamString"
        )
        return

    if raw_results["count"] == 0:
        query.answer(
            cache_time=0,  # TODO remove
            results=[],
            switch_pm_text=lang_msg(query, 'no_results'),
            switch_pm_parameter="StamString"
        )
    results = [
        InlineQueryResultArticle(
            title=f"{lang_msg(query, 'session')} {i['episode']} {lang_msg(query, 'episode')} {i['season']} • {dt_to_ht(i['start'])}",
            description=i["content"],
            thumb_url=random.choice(friends_icons),
            input_message_content=InputTextMessageContent(
                f"📺 {lang_msg(query, 'session')} {i['episode']} {lang_msg(query, 'episode')} {i['season']}\n"
                f"🕓 **{dt_to_ht(i['start'])}\n💬 {i['content']}**"
            ),
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(lang_msg(query, "inline_btn"),
                                     switch_inline_query_current_chat=""),
                InlineKeyboardButton(lang_msg(query, "share_btn"),
                                     switch_inline_query=query.query)
            ]])
        ) for i in raw_results["results"]
    ]
    query.answer(results,
                 switch_pm_text=f"{lang_msg(query, 'results_count')}: {str(raw_results['count'])}",
                 switch_pm_parameter="count")


app.run()
