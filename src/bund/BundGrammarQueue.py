##
##
##
import queue

class BundGrammarQueue:
    def __init__(self):
        self.q = {}
        self.default_queue_name = "__root__"
        self.createQueue("__root__")
    def queue(self, name, auto_create=True):
        if name not in self.q:
            if auto_create:
                self.default_queue_name = name
                return self.createQueue(name)
            else:
                return None
        else:
            return self.q[name]
    def lifo(self, name, auto_create=True):
        if name not in self.q:
            if auto_create:
                self.default_queue_name = name
                return self.createLIFO(name)
            else:
                return None
        else:
            return self.q[name]
    def push(self, data):
        if self.default_queue_name in self.q:
            self.q[self.default_queue_name].put_nowait(data)
        else:
            return False
        return True
    def pull(self):
        if self.default_queue_name in self.q:
            try:
                data = self.q[self.default_queue_name].get_nowait()
            except queue.Empty:
                return None
            return data
        return None
    def createQueue(self, name):
        if name in self.q:
            return False
        self.q[name] = queue.Queue()
        return self.q[name]
    def createLIFO(self, name):
        if name in self.q:
            return False
        self.q[name] = queue.LifoQueue()
        return self.q[name]
