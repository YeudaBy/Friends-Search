import json


def save_user(uid: int, save_use: bool = True):
    """ save user/chat id to DB """
    if save_use:
        save_uses()
    ids_file = "users.json"
    try:
        with open(ids_file, "r") as oFile:
            users: list = json.load(oFile)
    except FileNotFoundError:
        users = []

    if uid not in users:
        users.append(uid)

    with open(ids_file, "w") as nFile:
        json.dump(users, nFile, indent=4)


def save_uses():
    """ save count of uses to DB """
    uses_file = "uses.txt"
    try:
        with open(uses_file) as usesO:
            uses = int(usesO.read())
    except FileNotFoundError:
        with open(uses_file, "w") as usesO:
            usesO.write("0")
        with open(uses_file) as usesO:
            uses = int(usesO.read())
    uses += 1
    with open(uses_file, "w") as usesO:
        usesO.write(str(uses))
