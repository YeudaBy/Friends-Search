import re
from typing import List

from flask.json import JSONEncoder
from pony.orm import RowNotFound, exists, select
from DB.db import (Subtitle, db_session, db)


class Query:

    @staticmethod
    @db_session
    def search(
            query: str,
            limit: int = None,
            lang: str = "en"
    ) -> List[Subtitle]:
        """
        search sentences on DataBase.
        :param query: sentence to search
        :param lang: language to search, default None
        :param limit: limit of results count, default 50
        :return: list of results, contain: content, start and end time, and episode
        """
        query = Subtitle.clean_text(query)  # make clear query

        result = Subtitle.select(lambda i: query in i.raw_content)[:limit]

        if lang and lang != "ag":
            result = list(filter(lambda i: i.lang == lang.lower(), result))

        return [item for item in result]

    @staticmethod
    @db_session
    def all_langs() -> dict:
        # results = select(i.lang for i in Subtitle)
        # return list(set(results))
        return {"en": "English", "fr": "Français", "he": "עברית", "ag": "All languages"}

    @staticmethod
    @db_session
    def is_lang_exist(lang: str) -> bool:
        return exists(i for i in Subtitle if i.lang.lower() == lang.lower())

    @staticmethod
    @db_session
    def by_id(_id: int) -> Subtitle:
        return Subtitle.get(id=_id)
        # excepted RowNotFound

    @staticmethod
    @db_session
    def random(lang: str = "en") -> List[Subtitle]:
        res = Subtitle.select_random(limit=10)
        return res


class Parse:
    """ parse sql result to a class """

    def __init__(self, result: Subtitle):
        self.id = result.id
        self.content = self.remove_tags(result.content)
        self.start = result.start
        self.end = result.end
        self.episode = result.episode.__str__()
        self.season = result.season.__str__()
        self.lang = {result.lang: Query.all_langs()[result.lang]}

    def __dict__(self):
        return {
            "id": self.id,
            "content": self.content,
            "season": self.season.__str__(),
            "episode": self.episode.__str__(),
            "start": self.start.__str__(),
            "end": self.end.__str__(),
            "lang": self.lang
        }

    @staticmethod
    def remove_tags(text: str) -> str:
        return re.sub(r"<.*?>", "", text).replace("\n", " ")
