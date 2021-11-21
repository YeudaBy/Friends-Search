import srt
from pony.orm import *
from datetime import timedelta
# import os

db = Database()


class Subtitle(db.Entity):
    content = Required(str)
    start = Required(timedelta)
    end = Required(timedelta)
    episode = Required("Episode")


class Episode(db.Entity):
    iid = PrimaryKey(str)
    season = Required("Season")
    subtitles = Set(Subtitle)


class Season(db.Entity):
    iid = PrimaryKey(int)
    episodes = Set(Episode)


db.bind(provider='sqlite', filename='Friends.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


# @db_session
# def insert_subs(file):
#     name = file
#     # print(name, file)
#     sea, epi = name.split("-")
#     print(sea, epi)
#     season = Season.get(iid=int(sea))
#     if not season:
#         season = Season(iid=int(sea))
#     episode = Episode(iid=file, season=season)
#     subs = list(srt.parse(open(file, "r")))
#     for line in subs:
#         Subtitle(content=line.content,
#                  start=line.start,
#                  end=line.end,
#                  episode=episode)
#     commit()
#

# path = "Files/s10/"
# os.chdir(path)
# for file in os.listdir():
#     insert_subs(file)
#     print(file, "insert success!")
