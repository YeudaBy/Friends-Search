from typing import List
from re import sub

from DB.insert import (Subtitle, db_session, Episode)


class Parse:
    def __init__(self, result: Subtitle):
        self.content = result.content
        self.start = result.start.__str__()
        self.end = result.end.__str__()
        self.episode = result.episode.iid
        self.season = result.episode.season.iid


def clean_text(text: str) -> str:
    return sub(r"[!,.\(\)\-]", "", text)


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
    query = clean_text(query.lower())
    episode = make_episode(episode, season)

    result = Subtitle.select(lambda i: query in i.content.lower()).order_by(lambda i: i.episode.iid)

    if episode:
        result = list(filter(lambda i: i.episode.iid == episode, result))
        print(len(result))

    return [item for item in result]

print(len(search("how you doin")))