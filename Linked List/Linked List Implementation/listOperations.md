# LISTS

A list is a collection of items where each item holds a relative position with respect to the others. 

The list can be ordered or unordered.

## The Unordered List Abstract Data Type

1. `List()` creates a new list that is empty. It needs no parameters and returns an empty list.
2. `add(item)` adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list.
3. `remove(item)` removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
4. `search(item)` searches for the item in the list. It needs the item and returns a boolean value.
5. `isEmpty()` tests to see whether the list is empty. It needs no parameters and returns a boolean value.
6. `size()` returns the number of items in the list. It needs no parameters and returns an integer.
7. `append(item)` adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.
8. `index(item)` returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.
9. `insert(pos,item)` adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.
10. `pop()` removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.
11. `pop(pos)` removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.

## The Ordered List Abstract Data Type

1. `OrderedList()` creates a new ordered list that is empty. It needs no parameters and returns an empty list.
2. `add(item)` adds a new item to the list making sure that the order is preserved. It needs the item and returns nothing. Assume the item is not already in the list.
3. `remove(item)` removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
4. `search(item)` searches for the item in the list. It needs the item and returns a boolean value.
5. `isEmpty()` tests to see whether the list is empty. It needs no parameters and returns a boolean value.
6. `size()` returns the number of items in the list. It needs no parameters and returns an integer.
7. `index(item)` returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.
8. `pop()` removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.
9. `pop(pos)` removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.

## Analysis of Linked List

To analyze the complexity of the linked list operations, we need to consider whether they require traversal. Consider a linked list that has *n* nodes. The `isEmpty` method is **O(1)** since it requires one step to check the head reference for None. `size`, on the other hand, will always require *n* steps since there is no way to know how many nodes are in the linked list without traversing from head to end. Therefore, `length` is **O(n)**. *Adding an item to an unordered list in the beginning* will always be **O(1)** since we simply place the new node at the head of the linked list. However, `search` and `remove`, as well as `add` for an ordered list, all require the traversal process. Although on average they may need to traverse only half of the nodes, these methods are all **O(n)** since in the worst case each will process every node in the list.


