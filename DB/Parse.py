import re


class Parse:
    """ parse sql result to a class """

    def __init__(self, result):
        self.id = result.id
        self.content = self.remove_tags(result.content)
        self.start = result.start
        self.end = result.end
        self.episode = result.episode.__str__()
        self.season = result.season.__str__()
        self.lang = result.lang

    def __dict__(self):
        return {
            "id": self.id,
            "content": self.content,
            "season": self.season.__str__(),
            "episode": self.episode.__str__(),
            "start": self.start.__str__(),
            "end": self.end.__str__(),
            "lang": self.lang
        }

    def __str__(self):
        return self.__dict__().__str__()

    @staticmethod
    def remove_tags(text: str) -> str:
        return re.sub(r"<.*?>", "", text).replace("\n", " ")