import re
from typing import Union
import requests
from pyrogram.types import (Message, InlineQuery)
from Bot.db import get_lang, create_user
from Bot.strings import strings


def request_by_sentence(query: str) -> dict:
    endpoint = f"http://127.0.0.1:5000/sentence/search?query={query}"
    return requests.get(endpoint).json()


def request_by_id(_id: int) -> dict:
    endpoint = f"http://127.0.0.1:5000/api/sentence/{_id}"
    return requests.get(endpoint).json()


def lang_msg(msg_obj: Union[Message, InlineQuery], msg_to_rpl: str) -> Union[str, bool]:
    msg = strings.get(msg_to_rpl)
    if not msg:
        return False
    lang_client = get_lang(msg_obj.from_user.id)
    if msg.get(lang_client):
        return msg[lang_client]
    else:
        return msg["en"]


def dt_to_ht(timedelta: str) -> str:
    """ convert timedelta to human time """
    return re.search(r"0:(?P<ht>[0-9]{2}:[0-9]{2})\.[0-9]+", timedelta).groupdict().get("ht")
