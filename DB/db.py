import os
from re import sub

import srt
from pony.orm import *
from datetime import timedelta

db = Database()


class Subtitle(db.Entity):
    content = Required(str)         # content to display
    raw_content = Optional(str)     # content to search
    lang = Required(str)            # language of the content
    start = Required(timedelta)     # time of start
    end = Required(timedelta)       # time of end
    episode = Required(int)
    season = Required(int)

    @staticmethod
    def clean_text(text: str) -> str:
        """ return raw text without special characters and new lines """
        return sub(r"[$&+,:;=?@#|'<>.\-^*()\[\]{}%!~`_\" \n]", "", text).lower()


db.bind(provider='sqlite', filename='DataBases/Friends.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


@db_session
def insert_subs(name):
    # print(name, file)
    sea, epi = name.split("-")
    print(sea, epi)

    subs = list(srt.parse(open(name, "r", encoding="ISO-8859-1")))

    for line in subs:
        Subtitle(content=line.content,
                 raw_content=Subtitle.clean_text(line.content),
                 start=line.start,
                 end=line.end,
                 episode=epi,
                 season=sea,
                 lang="fr"
                 )
    commit()


# ========== Insert Data to DB =======
# path = "RawFiles/FR/s10"
# os.chdir(path)
# for file in os.listdir():
#     insert_subs(file)
#     print(file, "insert success!")

