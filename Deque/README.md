# Deque
A deque, also known as a double-ended queue, is an ordered collection of items similar to the queue. 

It has two ends, a front and a rear, and the items remain positioned in the collection. What makes a deque different is the unrestrictive nature of adding and removing items. New items can be added at either the front or the rear. Likewise, existing items can be removed from either end. 

Even though the deque can assume many of the characteristics of stacks and queues, it does not require the LIFO and FIFO orderings that are enforced by those data structures. It is up to us to make consistent use of the addition and removal operations.

The deque operations are given below.

1. `Deque()` creates a new deque that is empty. It needs no parameters and returns an empty deque.
2. `addFront(item)` adds a new item to the front of the deque. It needs the item and returns nothing.
3. `addRear(item)` adds a new item to the rear of the deque. It needs the item and returns nothing.
4. `removeFront()` removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
5. `removeRear()` removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
6. `isEmpty()` tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
7. `size()` returns the number of items in the deque. It needs no parameters and returns an integer.
