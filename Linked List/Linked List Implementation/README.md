### Append to a linked list with O(1) time analysis

To create the append() function with O(1), following implementation is required.

```python
def __init__(self, head=None, last=None):
    self.head = head
    self.last = head

def append(self, new_element):
    """Appends a new element to the linked list

        Args:
            new_element: An Element instance
    """
    current = self.head
    if self.head == self.last:
        current.next = new_element
        self.last = new_element
    else:
        self.last.next = new_element
        self.last = new_element
```
