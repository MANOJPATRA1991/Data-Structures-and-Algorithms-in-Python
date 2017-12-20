class Stack:
    """
    Creates a Stack data structure
    Attributes:
        items(List): A list instance to store stack items
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Checks if stack is empty
        Returns:
            Boolean: Indicates if stack is empty
        """
        return self.items == []

    def push(self, item):
        """
        Push item into the stack
        Item(any): Item to push
        """
        self.items.append(item)

    def pop(self):
        """
        Pop item from the stack
        """
        return self.items.pop()

    def peek(self):
        """
        Peek last item in the stack
        """
        return self.items[len(self.items) - 1]

    def size(self):
        """
        Get the size of the stack
        Returns:
            Integer: Size of the stack
        """
        return len(self.items)

