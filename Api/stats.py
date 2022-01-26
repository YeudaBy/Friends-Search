import requests
from datetime import datetime
from flask import request
import os
from dotenv import load_dotenv
from pony.orm import *

db = Database()
load_dotenv()


@db_session
def create():
    try:
        ApiQuery(
            uri=request.environ.get("RAW_URI"),
            user_agent=request.environ.get("HTTP_USER_AGENT"),
            time=datetime.now()
        )
    except Exception as e:
        print(e)


class ApiQuery(db.Entity):
    uri = Required(str)
    user_agent = Required(str)
    time = Required(datetime)


db.bind(provider='sqlite', filename='stats.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
set_sql_debug(True, show_values=True)


# with db_session:
#     res = select(i for i in ApiQuery if i.uri == "/")[:]
#     print(res)


def send_report(_id):
    token = os.getenv("REPORTED_TOKEN")
    target = os.getenv("REPORTS_CHANNEL")
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={target}&text=report-for:%20{_id}\nhttps://api' \
          f'.friends-search.com/sentence/{_id} '
    req = requests.get(url)
    return False if req.status_code != 200 else req.json()["result"]["message_id"]
