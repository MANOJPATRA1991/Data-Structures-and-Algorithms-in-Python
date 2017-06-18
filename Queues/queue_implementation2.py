from collections import deque
class Queue:
    def __init__(self, head=None):
        self.storage = deque([head])

    def enqueue(self, new_element):
        self.storage.append(new_element)
        pass

    def peek(self):
        return self.storage[0]
        pass 

    def dequeue(self):
        return self.storage.popleft()
        pass
    

