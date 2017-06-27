from Stacks.stack1 import Stack

class Queue(object):
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def enqueue(self, item):
        self.input.push(item)

    def dequeue(self):
        if self.output.isEmpty():
            while(not self.input.isEmpty()):
                self.output.push(self.input.pop())

        return self.output.pop()

input = Stack()
output = Stack()
Q = Queue(input, output)

Q.enqueue(1)
Q.enqueue(3)
Q.enqueue(6)
