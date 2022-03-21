from re import sub
# import srt
from typing import Union

from pony.orm import Database, Required, Optional, Json
from datetime import timedelta, datetime

db = Database()


class Sentence(db.Entity):
    """ main entity """
    content = Required(str)         # content to display
    raw_content = Optional(str)     # content to search
    lang = Required(str)            # language of the content
    start = Required(timedelta)     # time of start
    end = Required(timedelta)       # time of end
    episode = Required(int)
    season = Required(int)
    verified = Optional(bool)       # if the content is verified
    likes = Optional(int)       # count of times that people like the sentence

    @staticmethod
    def clean_text(text: str) -> str:
        """ return raw text without special characters and new lines """
        return sub(r"[$&+,:;=?@#|'<>.\-^*()\[\]{}%!~`_\" \n]", "", text).lower()


class Usage(db.Entity):
    """ sava statistics of usages """
    uri = Required(str)
    user_agent = Required(Json)
    time = Required(datetime)


db.bind(provider='sqlite', filename='DataBases/Friends.sqlite', create_db=True)

db.generate_mapping(create_tables=True)
# set_sql_debug()

