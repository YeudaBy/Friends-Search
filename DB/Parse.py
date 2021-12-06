
class Parse:
    """ parse sql result to a class """

    def __init__(self, result):
        self.id = result.id
        self.content = result.content.replace("\n", " ")
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
