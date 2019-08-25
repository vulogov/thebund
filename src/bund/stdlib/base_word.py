##
##
##
import uuid

class BASE_WORD:
    def __init___(self, name=[]):
        if len(name) == 0:
            self.name = [self.__class__.__name__.lower()]
        self.m = {}
        self.local_init()
    def local_init(self):
        pass
    def register2(self, name, a_check, b_check, code):
