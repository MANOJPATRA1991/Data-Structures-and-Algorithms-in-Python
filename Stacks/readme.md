# Stack

The stack abstract data type is defined by the following structure and operations. 
A stack is structured as an ordered collection of items where items are added to and removed from the end called the “top.” Stacks are ordered **LIFO**. 

The stack operations are given below.

1. `Stack()` creates a new stack that is empty. It needs no parameters and returns an empty stack.
2. `push(item)` adds a new item to the top of the stack. It needs the item and returns nothing.
3. `pop()` removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
4. `peek()` returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
5. `isEmpty()` tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
6. `size()` returns the number of items on the stack. It needs no parameters and returns an integer.
