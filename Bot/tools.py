from random import choice
from re import search
from typing import Union, Tuple
from requests import get, post
from pyrogram.types import (Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
from Bot.db import get_lang, create_user, get_favorite_ids
from Bot.strings import strings, friends_images
from dotenv import load_dotenv
from os import getenv

load_dotenv()

# base_url = "https://api.friends-search.com"
base_url = "http://192.168.165.99:8080/"
headers = {'User-Agent': getenv("BOT_USER_AGENT")}


def request_by_sentence(query: str) -> dict:
    endpoint = f"{base_url}/sentence/search?query={query}&language=ag"
    return get(endpoint).json()


def request_by_id(_id: int) -> dict:
    endpoint = f"{base_url}/sentence/{_id}"
    return get(endpoint, headers=headers).json()


def report_on_id(_id: int) -> dict:
    endpoint = f"{base_url}/sentence/report"
    return post(endpoint, data={'id': _id}).json()


def lang_msg(msg_obj: Union[Message, InlineQuery, CallbackQuery], msg_to_rpl: str) -> str:
    create_user(msg_obj.from_user.id, msg_obj.from_user.language_code)
    msg = strings.get(msg_to_rpl)
    if not msg:
        return "Msg not set"
    lang_client = get_lang(msg_obj.from_user.id)
    if msg.get(lang_client):
        return msg[lang_client]
    else:
        return msg["en"]


def dt_to_ht(timedelta: str) -> str:
    """ convert timedelta to human time """
    return search(r"(\d:)(?P<ht>\d{2}:\d{2})(.\d*)", timedelta).groupdict().get("ht")


def random_img():
    return choice(friends_images)


def get_sentence_result(sid: int, msg_obj) -> InlineQueryResultArticle:
    raw_res = request_by_id(sid)
    season = raw_res['season']
    episode = raw_res['episode']
    lang = raw_res['lang_name']
    result = InlineQueryResultArticle(
        title=f"{lang_msg(msg_obj, 'session')} {season} {lang_msg(msg_obj, 'episode')} {episode} • {dt_to_ht(raw_res['start'])} • {lang}",
        description=raw_res["content"],
        thumb_url=random_img(),
        input_message_content=InputTextMessageContent(
            message_text=get_sentence_msg(raw_res["id"], msg_obj)[0],
        ),
        reply_markup=get_sentence_msg(raw_res["id"], msg_obj)[1]
    )
    return result


def get_sentence_msg(sid: int, msg_obj) -> Tuple[str, InlineKeyboardMarkup]:
    raw_res = request_by_id(sid)
    season = raw_res['season']
    episode = raw_res['episode']
    start_time = raw_res['start']
    end_time = raw_res['end']

    id_str = str(sid)
    msg_txt = f"**✅ {lang_msg(msg_obj, 'results_title')}**\n\n" \
              f"**📺 {lang_msg(msg_obj, 'appear_at')}:** `{lang_msg(msg_obj, 'session')} {season} {lang_msg(msg_obj, 'episode')} {episode}`\n" \ 
              f"**🕓 {lang_msg(msg_obj, 'time')}:** `{dt_to_ht(start_time)}` ⇿ `{dt_to_ht(end_time)}`\n**💬 {lang_msg(msg_obj, 'sentence')}:** `{raw_res['content']}`"
    msg_kb = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(lang_msg(msg_obj, "inline_btn"),
                                     switch_inline_query_current_chat=""),
                InlineKeyboardButton("ℹ",
                                     callback_data="r/" + id_str),
                InlineKeyboardButton(lang_msg(msg_obj, "share_btn"),
                                     switch_inline_query=id_str)
            ],
            [
                InlineKeyboardButton("⏪",
                                     callback_data=str(sid - 1 if get_lang(msg_obj.from_user.id) != "he" else sid + 1)),
                InlineKeyboardButton("❤" if not get_favorite_ids(msg_obj.from_user.id) or sid not in get_favorite_ids(
                    msg_obj.from_user.id) else "💔",
                                     callback_data="f/" + id_str),
                InlineKeyboardButton("⏩",
                                     callback_data=str(sid + 1 if get_lang(msg_obj.from_user.id) != "he" else sid - 1))
            ]
        ]
    )
    return msg_txt, msg_kb


def change_lang_buttons(qid: str):
    return InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("❌", callback_data=f"n/{qid}"),
            InlineKeyboardButton("✅", callback_data=f"y/{qid}")
        ]]
    )


lang_buttons = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton("🇺🇸", callback_data="l/en"),
        InlineKeyboardButton("🇮🇱", callback_data="l/he"),
        InlineKeyboardButton("🇫🇷", callback_data="l/fr"),
        InlineKeyboardButton("❌", callback_data="l/close"),
    ]]
)


def start_buttons(msg):
    return InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("🔎", switch_inline_query_current_chat=""),
            InlineKeyboardButton("㊗", callback_data="change_lang"),
            InlineKeyboardButton("🌐", url="https://friends-search.com/"),
            InlineKeyboardButton("❤", callback_data="favs"),
            InlineKeyboardButton("♻",
                                 url=f"https://t.me/share/url?url={lang_msg(msg, 'encode_url')}@Friends_SearchBot"),
            InlineKeyboardButton("❌", callback_data="close_msg")
        ]]
    )


close_msg_buttons = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton("🔎", switch_inline_query_current_chat=""),
        InlineKeyboardButton("❌", callback_data="close_msg")
    ]]
)
