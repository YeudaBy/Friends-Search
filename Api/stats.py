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

# with db_session:
#     ApiQuery(content={"test": "test1"}, time=datetime.now())


def send_reports(_id):
    token = os.getenv("REPORTED_TOKEN")
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id=-1001524768471&text=report-for:%20{_id}"
    req = requests.get(url)
    return req.status_code == 200


print(send_reports(1000))