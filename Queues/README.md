# The Queue Abstract Data Type

The queue abstract data type is defined by the following structure and operations. 
A queue is structured as an ordered collection of items which are added at one end, called the *rear*, and removed from the other end, called the *front*. 
Queues maintain a **FIFO** ordering property. The queue operations are given below.

1. `Queue()` creates a new queue that is empty. It needs no parameters and returns an empty queue.
2. `enqueue(item)` adds a new item to the rear of the queue. It needs the item and returns nothing.
3. `dequeue()` removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
4. `is_empty()` tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
5. `size()` returns the number of items in the queue. It needs no parameters and returns an integer.
