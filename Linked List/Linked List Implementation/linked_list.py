
class Element(object):
    """This class creates elements that can be inserted into a
        LinkedList instance"""
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList(object):
    """This class can be used to create a Linked List"""
    def __init__(self, head=None):
        self.head=head

    def append(self, new_element):
        """Appends a new element to the linked list
            
            Args:
                new_element: An Element instance
        """
        current=self.head
        if self.head:
            while current.next:
                current=current.next
            current.next=new_element
        else:
            self.head=new_element

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
        counter=1
        current=self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current=current.next
            counter += 1
        return None

    def search(self, item):
        """search for an item in the linked list
        Args:
            item: An Element instance
        
        Returns:
            A Boolean"""
        current = self.head
        while current:
            if current.value == item:
                return True
            else:
                current = current.next
        return False
    
    def insert(self, new_element, position):
        """Inserts a new element at a specified position in
            the linked list

            Args:
                new_element: An Element instance
                position: A number specifying the position
                    at which the new element is to be inserted
        """
        counter=1
        current=self.head
        if position > 1:
            while current and counter < position:
                if counter == position-1:
                    new_element.next=current.next
                    current.next=new_element
                current=current.next
                counter += 1
        elif position == 1:
            new_element.next=self.head
            self.head=new_element

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
            temp = self.head
            self.head = None
            return temp
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
e4 = Element(4)

# Start setting up a LinkedList

# ll here is an instance of the LikedList class that contains a single reference to only the 
# first node in the linked list structure
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)

print(ll.search(3))
print(ll.search(7))

print(ll.size())
# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print (ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print (ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print (ll.get_position(1).value)
# Should print 4 now
print (ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)

            
        
