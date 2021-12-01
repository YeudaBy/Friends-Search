from typing import List
from re import sub

from DB.db import (Subtitle, db_session)


class Parse:
    def __init__(self, result: Subtitle):
        self.content = result.content
        self.start = result.start.__str__()
        self.end = result.end.__str__()
        self.episode = result.episode.__str__()
        self.season = result.season.__str__()


def make_episode(episode: int, season: int) -> str:
    return None if not episode and not season else f"{str(season).zfill(2)}-{str(episode).zfill(2)}"


@db_session
def search(
        query: str,
        season: int = None,
        episode: int = None,
) -> List[Subtitle]:
    """
    search sentences on DataBase.
    :param query: sentence to search
    :param season: in specific season, default None.
    :param episode: in specific episode, default None.
    :return: list of results, contain: content, start and end time, and episode
    """
    query = Subtitle.clean_text(query.lower())
    _episode = make_episode(episode, season)

    result = Subtitle.select(lambda i: query in i.raw_content.lower())

    if episode:
        result = list(filter(lambda i: i.episode == episode and i.season == season, result))
        print(len(result))

    return [item for item in result]

# print(len(search("how you doin")))
