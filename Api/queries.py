from typing import List
from DB.db import (Subtitle, db_session)


class Parse:
    """ parse sql result to a class """
    def __init__(self, result: Subtitle):
        self.content = result.content
        self.start = result.start.__str__()
        self.end = result.end.__str__()
        self.episode = result.episode.__str__()
        self.season = result.season.__str__()


# def make_episode(episode: int, season: int) -> str:
#     """ convert episode and season ints to one string """
#     return None if not episode and not season else f"{str(season).zfill(2)}-{str(episode).zfill(2)}"


@db_session
def search(
        query: str,
        # season: int = None,
        # episode: int = None,
        limit: int = None,
        lang: str = None
            ) -> List[Subtitle]:
    """
    search sentences on DataBase.
    :param query: sentence to search
    :return: list of results, contain: content, start and end time, and episode
    :param lang: language to search, default None
    :param limit: limit of results count, default 50
    """
    query = Subtitle.clean_text(query)  # make clear query

    result = Subtitle.select(lambda i: query in i.raw_content)[:limit]

    if lang:
        result = list(filter(lambda i: i.lang == lang.lower(), result))

    return [item for item in result]
