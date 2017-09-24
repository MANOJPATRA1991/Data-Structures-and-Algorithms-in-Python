# assume rear is at position 0 in the list

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # O(n) performance
    def enqueue(self, items):
        self.items.insert(0, items)

    # O(1)
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# q=Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.items)
# q.dequeue()
# print(q.items)
