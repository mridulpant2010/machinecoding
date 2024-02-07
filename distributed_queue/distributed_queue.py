from queue import Queue
class DistributedQueue:
    def __init__(self):
        self.storage = {}
        self.queue = Queue()
    
    