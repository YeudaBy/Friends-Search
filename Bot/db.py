from typing import Union

from pony.orm import *

db = Database()


class User(db.Entity):
    user_id = PrimaryKey(int)
    lang = Required(str, default="en")
    query_ids = Optional(IntArray)


db.bind(provider='sqlite', filename='Users.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


# set_sql_debug()


@db_session
def create_user(user_id: int, lang="en"):
    if not User.exists(user_id=user_id):
        User(user_id=user_id, lang=lang)


@db_session
def get_lang(user_id):
    user = User.get(user_id=user_id)
    if not user:
        create_user(user_id=user_id)
    return user.lang


@db_session
def update_lang(user_id, lang):
    user = User.get(user_id=user_id)
    if not user:
        create_user(user_id=user_id, lang=lang)
    user.lang = lang
    commit()


@db_session
def update_favorite(user_id: int, query_id: int) -> bool:
    user = User.get(user_id=user_id)
    if not user:
        create_user(user_id)
    favs: list = user.query_ids
    favs.append(query_id) if query_id not in favs else favs.remove(query_id)
    return query_id in favs


@db_session
def get_favorite_ids(user_id) -> Union[list, bool]:
    user = User.get(user_id=user_id)
    if not user:
        create_user(user_id=user_id)
    favs = user.query_ids
    if not favs:
        return False
    return user.query_ids


# create_user(user_id=12345378, lang="en")
# update_usage(12345678)
# update_query(12345678, 123435)
# # update_lang(12345678, "he")
# print(get_stats()["users"])
