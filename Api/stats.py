from requests import get
# from datetime import datetime
# from flask import request
from os import getenv
# from dotenv import load_dotenv
# from pony.orm import Database, db_session, Required, set_sql_debug
#
# db = Database()
# load_dotenv()
#
#
# @db_session
# def create():
#     try:
#         ApiQuery(
#             uri=request.environ.get("RAW_URI"),
#             user_agent=request.environ.get("HTTP_USER_AGENT"),
#             time=datetime.now()
#         )
#     except Exception as e:
#         print(e)
#
#
# class ApiQuery(db.Entity):
#     uri = Required(str)
#     user_agent = Required(str)
#     time = Required(datetime)
#
#
# db.bind(provider='sqlite', filename='stats.sqlite', create_db=True)
# db.generate_mapping(create_tables=True)
# set_sql_debug(True, show_values=True)
#

# with db_session:
#     res = select(i for i in ApiQuery if i.uri == "/")[:]
#     print(res)



