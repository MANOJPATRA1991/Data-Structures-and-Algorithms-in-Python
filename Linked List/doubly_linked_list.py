class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DLL(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
            new_element.prev = current
        else:
            self.head = new_element

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next.prev = new_element
                    current.next = new_element
                    new_element.prev = current
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head.prev = new_element
            self.head = new_element

    def delete(self, value):
        current = self.head
        while current.value != value and current.next:
            current = current.next
        if current.value == value:
            if current.prev:
                current.next.prev = current.prev
                current.prev.next = current.next
                current.prev = None
                current.next = None
            else:
                self.head = current.next
                current.next.prev = None
                current.next = None

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

dll = DLL(e1)
dll.append(e2)
dll.append(e3)

dll.insert(e4, 3)

dll.delete(1)
print(dll.get_position(1).value)
