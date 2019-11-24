from Stacks.stack1 import Stack


class Queue(object):
    def __init__(self, _input, _output):
        self.input = _input
        self.output = _output

    def enqueue(self, item):
        self.input.push(item)

    def dequeue(self):
        if self.output.is_empty():
            while not self.input.is_empty():
                self.output.push(self.input.pop())

        return self.output.pop()


_input = Stack()
_output = Stack()
Q = Queue(_input, _output)

Q.enqueue(1)
Q.enqueue(3)
Q.enqueue(6)
