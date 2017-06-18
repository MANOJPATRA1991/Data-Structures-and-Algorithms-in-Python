class Element(object):
    """This class can be used to create elements to insert into linear
        data structures(in this case linked list)"""
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    """This class can be used to create a linked list"""
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        """Append a new element to the end of a linked list

            Args:
                new_element: An instance of class Element"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        """Insert new element as the head of the LinkedList

            Args:
                new_element: An instance of class Element"""
        current = self.head
        if current:
            new_element.next = current
        self.head = new_element
            
        pass

    def delete_first(self):
        """Delete the first (head) element in the LinkedList as return it"""
        current = self.head
        if current:
            self.head = current.next
            current.next = None
        return current
        pass

class Stack(object):
    """Create an instance of class Stack"""
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        """Push (add) a new element onto the top of the stack

            Args:
                new_element: An instance of class Element"""
        self.ll.insert_first(new_element)
        pass

    def pop(self):
        """Pop (remove) the first element off the top of the stack and return it"""
        return self.ll.delete_first()
        pass
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print stack.pop().value
print stack.pop().value
print stack.pop().value
print stack.pop()
stack.push(e4)
print stack.pop().value
