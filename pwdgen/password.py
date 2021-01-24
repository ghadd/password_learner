
import jsonpickle

from typing import Dict


class Password:
    def __init__(self, size: int, config: Dict, contents: str):
        self.__size = size
        self.__config = config
        self.contents = contents
        self.progress = 0

    def save(self):
        with open("/tmp/lastpwd.obj", "w") as file:
            file.write(jsonpickle.dumps(self))

    @staticmethod
    def load():
        try:
            with open("/tmp/lastpwd.obj", "r") as file:
                obj = jsonpickle.loads(file.read())
                return obj
        except IOError as e:
            raise IOError(
                "Could not load any password from previous sessions.")
