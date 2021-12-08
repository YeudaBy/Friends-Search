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
def update_query(user_id, query_id):
    user = User.get(user_id=user_id)
    if not user:
        return False
    if query_id not in user.query_ids:
        user.query_ids.append(query_id)
        commit()


# create_user(user_id=12345678, lang="en")
# update_usage(12345678)
# update_query(12345678, 123435)
# update_lang(12345678, "he")
