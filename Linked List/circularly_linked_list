class Element(object):
    def __init__(self, value):
        self.value=value
        self.next=None

class CircularlyLinkedList(object):
    def __init__(self, head=None):
        self.head=head

    def append(self, new_element):
        current=self.head
        if self.head:
            while current.next and current.next != self.head:
                    current=current.next
            current.next=new_element
            new_element.next=self.head
        else:
            self.head=new_element
            new_element.next=self.head

    def get_count(self, head):
        count=1
        current=self.head
        while current.next != self.head:
            current=current.next
            count += 1
        return count
    
    def insert(self, new_element, position):
        counter=1
        current=self.head
        if position > 1:
            while current and counter < position:
                if counter <= self.get_count(self.head):
                    if counter == position-1:
                        new_element.next=current.next          
                        current.next=new_element
                    current=current.next
                    counter += 1
        elif position == 1:
            new_element.next=self.head
            while current.next != self.head:
                current=current.next
            current.next=new_element
            self.head=new_element

    def delete(self, value):
        current=self.head
        previous=None
        while current.value != value and current.next != self.head:
            previous=current
            current=current.next
        if current.value == value:
            if previous:
                previous.next=current.next
                current.next=None
            else:
                while current.next != self.head:
                    current=current.next
                current.next=self.head.next
                self.head.next=None
                self.head=current.next
                
    def get_position(self, position):
        counter=1
        current=self.head
        if position < 1:
            return None
        while current and counter <= position:        
            if counter == position:
                return current
            if current.next != self.head:
                current=current.next
                counter += 1
            else:
                return
        return None
    
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

cl = CircularlyLinkedList(e1)
cl.append(e2)

cl.append(e3)

cl.insert(e4,3)

cl.delete(1)

print(cl.get_position(3).next.value)
