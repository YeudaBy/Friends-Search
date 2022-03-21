from re import sub
from typing import List, Union
from pony.orm import db_session, commit, select, raw_sql
from requests import get
from sqlite3 import connect

from DB.db import Sentence, Usage
from dotenv import load_dotenv
from os import getenv

load_dotenv()
ADMIN_TOKEN = getenv("ADMIN_TOKEN")


def all_languages() -> dict:
    """ return all language supported """
    return {"en": "English", "fr": "Français", "he": "עברית", "ag": "All languages"}


def is_language_exist(language: str) -> dict:
    """ return True if language supported """
    return dict((k, v) for k, v in all_languages().items() if language.lower() == k or language.lower() == v)


@db_session
def search_sentence(
        query: str,
        limit: int = 50,
        lang: str = "ag"
) -> Union[List[Sentence], bool]:
    """
    search sentences on DataBase.
    :param query: sentence to search
    :param lang: language to search, default None
    :param limit: limit of results count, default 50
    :return: list of results, contain: content, start and end time, and episode
    """
    query = Sentence.clean_text(query)  # make clear query

    result = Sentence.select(lambda i: query in i.raw_content)[:limit]

    if lang and (lang != "ag"):
        result = list(filter(lambda i: i.lang == lang.lower(), result))

    if not result:
        return False

    return [item for item in result]


@db_session
def sentence_by_id(_id: int) -> Union[Sentence, bool]:
    """ return Sentence by specific id """
    return Sentence.get(id=_id) or False


@db_session
def sentence_random(language: str = "ag") -> List[Sentence]:
    """ return 10 random sentences, and only in specific language if is provided"""
    results = []
    if language and (language != "ag"):
        [results.append(i) for i in list(filter(lambda i: i.lang == language.lower(),
                                                Sentence.select_random(limit=100)))[:10]]
        return results
    [results.append(result) for result in Sentence.select_random(limit=10)]
    return results


@db_session
def like_sentence(_id: int) -> bool:
    """ add one more to count of favorites """
    Sentence.get(id=_id).favorited += 1
    commit()
    return True


@db_session
def fix_content(_id: int, new_content: Union[str, bytes], token: str) -> Union[bool, str]:
    """ ADMINS ONLY: fix the content of the sentence
    available only with admin token from .env file """
    if token != ADMIN_TOKEN:
        return False
    sentence = Sentence.get(id=_id)
    sentence.content = str(new_content)
    sentence.raw_content = Sentence.clean_text(str(new_content))
    sentence.verified = True
    commit()
    return sentence.content


@db_session
def verify_content(_id: int, token: str) -> bool:
    """ ADMINS ONLY: set the sentence as verified
        available only with admin token from .env file """
    if token != ADMIN_TOKEN:
        return False
    Sentence.get(id=_id).verified = True
    commit()
    return True


def parse(_object: Sentence) -> Union[dict, bool]:
    """ parse the Sentence object to json """
    if not _object: return False
    data = {
        "content": sub(r"<.*?>", "", _object.content).replace("\n", " "),
        "id": _object.id,
        "language": {
            "language_code": list(is_language_exist(_object.lang).keys())[0],
            "language_name": list(is_language_exist(_object.lang).values())[0]
        },
        "position": {
            "season": _object.season,
            "episode": _object.episode,
            "start": _object.start.__str__(),
            "end": _object.end.__str__()
        },
        "details": {
            "likes": _object.likes,
            "verified": _object.verified,
            # "views": _object.views
        }
    }
    return data


def send_report(_id):
    """ send report to telegram channel """
    token = getenv("REPORTED_TOKEN")
    target = getenv("REPORTS_CHANNEL")
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={target}&text=report-for:%20{_id}\nhttps://api' \
          f'.friends-search.com/sentence/{_id} '
    req = get(url)
    return False if req.status_code != 200 else req.json()["result"]["message_id"]


# ---- Usages -----
Usage_view = Union[List[dict], None]

@db_session
def get_usages_of_methode(methode: str, is_absolute: bool = False) -> Usage_view:
    """ return dict of usages """
    results = select((i for i in Usage if methode == i.uri) if is_absolute else (
        i for i in Usage if methode in i.uri))[:]
    if not results:
        return None
    return [dict(uri=i.uri, time=i.time, user_agent=i.user_agent) for i in results]


def get_usages_of_id(_id: int) -> Usage_view:
    """ return dict usages of specific id """
    uri = f"/sentence/{_id}"
    return get_usages_of_methode(uri, True)


@db_session
def popular_uris() -> Usage_view:
    """ return dict of popular usages """
    db = connect("DataBases/Friends.sqlite")
    db.cursor()
    d = db.execute("SELECT uri, COUNT(uri) AS `value_occurrence` FROM Usage GROUP BY uri LIMIT 10")
    return [dict(uri=i[0], count=i[1]) for i in d]


print(popular_uris())
