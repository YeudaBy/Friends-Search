from typing import List, Union

from pony.orm import RowNotFound, exists, select

from DB.db import (Subtitle, db_session, db)


class FriendsSearch:

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

        if lang:
            result = list(filter(lambda i: i.lang == lang.lower(), result))

        return [item for item in result]

    @staticmethod
    @db_session
    def all_langs() -> list:
        results = select(i.lang for i in Subtitle)
        return list(set(results))

    @staticmethod
    @db_session
    def is_lang_exist(lang: str) -> bool:
        return exists(i for i in Subtitle if i.lang.lower() == lang.lower())

    @staticmethod
    @db_session
    def by_id(_id: int) -> Union[Subtitle, bool]:
        try:
            return Subtitle.get(id=_id)
        except RowNotFound:
            return False

    @staticmethod
    @db_session
    def random(count: int = 1) -> List[Subtitle]:
        return Subtitle.select_random(limit=count)

