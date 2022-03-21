from os import listdir, rename
from re import IGNORECASE, match

# rename files name by template
p = "Files/s10/"
for f in listdir(p):
    print(f)
    name = r".*s(?P<s>\d{2})e(?P<e>\d{2}).*"
    data = match(name, f, IGNORECASE).groupdict()
    new_name = f"{p}{data['s']}-{data['e']}"
    rename(p + f, new_name)
    print(f"rename from -{f}- to -{new_name}-")


# @db_session
# def insert_subs(name):
#     # print(name, file)
#     sea, epi = name.split("-")
#     print(sea, epi)
#
#     subs = list(srt.parse(open(name, "r", encoding="ISO-8859-1")))
#
#     for line in subs:
#         if not line.content:
#             continue
#         Subtitle(content=line.content,
#                  raw_content=Subtitle.clean_text(line.content),
#                  start=line.start,
#                  end=line.end,
#                  episode=epi,
#                  season=sea,
#                  lang="fr"
#                  )
#     commit()


# ========== Insert Data to DB =======
# path = "RawFiles/FR/s10"
# os.chdir(path)
# # # for file in os.listdir():
# insert_subs("10-17")
# print("10-17", "insert success!")

# with db_session:
#     for i in Subtitle.select():
#         i.favorited = 0
#     commit()

