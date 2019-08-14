##
##
##
import uuid

class BASE_WORD:
    def __init___(self, name=[]):
        if len(name) == 0:
            self.name = [self.__class__.__name__.lower()]
