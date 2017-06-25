class Element(object):
    """This class creates elements that can be inserted into an
        OrderedLinkedList instance"""

    def __init__(self, value):
        self.value = value
        self.next = None


class OrderedLinkedList(object):
    """This class can be used to create an Ordered Linked List"""

    def __init__(self, head=None):
        self.head = head

    def search(self, item):
        """search for an item in the ordered linked list
        Args:
            item: An Element instance

        Returns:
            A Boolean"""
        current = self.head
        while current:
            if current.value == item:
                return True
            elif current.value < item:
                current = current.next
            else:
                break
        return False

    def is_empty(self):
        """Checks if the linked list is empty

            Returns:
                A Boolean indicating if the list is empty or not
        """
        return self.head == None

    def get_position(self, position):
        """Returns the element at the position specified

            Args:
                position: A number specifying position at which
                element is to be returned

            Returns:
                An Element instance at the specified position
                within the Linked list
        """
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

    def insert(self, new_element):
        """Inserts a new element in the ordered linked list

            Args:
                new_element: An Element instance
        """
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.value > new_element.value:
                stop = True
            else:
                previous = current
                current = current.next

        if previous is None:
            self.head = new_element
        else:
            new_element.next = current
            previous.next = new_element

    def delete(self, value):
        """Search for a value in the linked list and if found,
            delete it

            Args:
                value: value to delete from the linked list
        """
        current = self.head
        previous = None
        found = False
        while current and  not found:
            if current.value == value:
                found = True
            else:
                previous = current
                current = current.next
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
            current.next = None

    def pop(self):
        """removes the last element from the linked list

        Returns:
            An Element instance
        """
        current = self.head
        previous = None
        while current is not None:
            if current.next:
                previous = current
            current = current.next
        if previous is None:
            print("No elements in list!!")
        else:
            temp = previous.next
            previous.next = None
            return temp

    def size(self):
        """returns the size of the linked list

        Returns: An integer
            """

        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(5)

# Start setting up a LinkedList

# ll here is an instance of the LikedList class that contains a single reference to only the
# first node in the linked list structure
ll = OrderedLinkedList(e1)
ll.insert(e2)
ll.insert(e3)
ll.insert(e4)
ll.insert(Element(4))
print(ll.search(5))
