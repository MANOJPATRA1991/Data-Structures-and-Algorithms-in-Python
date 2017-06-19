import ctypes
class Element(object):
    """Creates element of a memory efficient doubly linked list"""
    def __init__(self, value):
        self.value=value
        # XOR of next and previous elements
        self.npx=None

class MemoryEfficientDLL(object):
    def __init__(self, head=None):
        self.head=head
        
    def append(self, new_element):
        current=self.head
        new_element.npx=id(current) ^ 0
        if self.head:
            next=current.npx ^ 0
            current.npx=id(new_element) ^ next
        self.head=new_element
        
    def printList(self, head=None):
        current=self.head
        previous=0
        while current:
            print(current.value)
            next=previous ^ current.npx
            previous=id(current)
            # This function is similar to the cast operator in C.
            # It returns a new instance of type which points to the same memory block as obj.
            # type must be a pointer type, and obj must be an object that can be interpreted as a pointer.
            current=ctypes.cast(next, ctypes.py_object).value

e1=Element(1)
e2=Element(2)
e3=Element(3)
e4=Element(4)
e5=Element(5)
cl=MemoryEfficientDLL()

cl.append(e1)
cl.append(e2)
cl.append(e3)
cl.append(e1)
cl.append(e4)
cl.append(e5)
cl.printList(cl.head)
