from typing import Union

from pony.orm import *

db = Database()


class User(db.Entity):
    user_id = PrimaryKey(int)
    lang = Required(str, default="en")
    uses = Optional(int, default=0)
    query_ids = Optional(IntArray)


db.bind(provider='sqlite', filename='Users.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


# set_sql_debug()


@db_session
def create_user(user_id: int, lang):
    if not User.exists(user_id=user_id):
        User(user_id=user_id, lang=lang)
    commit()


@db_session
def get_lang(user_id):
    user = User.get(user_id=user_id)
    if not user:
        return False
    return user.lang


@db_session
def update_lang(user_id, lang):
    user = User.get(user_id=user_id)
    if not user:
        return False
    user.lang = lang
    commit()


@db_session
def update_usage(user_id):
    user = User.get(user_id=user_id)
    if not user:
        return False
    user.uses += 1
    commit()


@db_session
def edit_favorite(user_id: int, query_id: int) -> bool:
    user = User.get(user_id=user_id)
    if not user:
        create_user(user_id)
    favs: list = user.query_ids
    favs.append(query_id) if query_id not in favs else favs.remove(query_id)
    return query_id in favs


@db_session
def get_favorites(user_id) -> Union[list, bool]:
    user = User.get(user_id=user_id)
    if not user:
        return False
    return user.query_ids


@db_session
def get_stats():
    users = select(i for i in User)[:]
    users_count = len(users)
    uses_count = sum(i.uses for i in users)
    return {
        "users": users_count,
        "uses": uses_count
    }

# create_user(user_id=12345378, lang="en")
# update_usage(12345678)
# update_query(12345678, 123435)
# # update_lang(12345678, "he")
# print(get_stats()["users"])
