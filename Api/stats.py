import json
from datetime import datetime
from flask import request
from pony.orm import *

db = Database()


def create(req: request) -> "ApiQuery":
    return ApiQuery(
        content=request.__dict__,
        time=datetime.now()
    )


class ApiQuery(db.Entity):
    content = Required(Json)
    time = Required(datetime)


db.bind(provider='sqlite', filename='stats.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
