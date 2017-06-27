# Queue implementation using Stack

This Queue class utilizes two stacks: one for storing items during `enqueue` and another for popping items during `dequeue`.
Both the operations have a cost of `O(1)` on an average except a particular situation when the output stack is empty.

When the output stack is empty, we need to copy the input stack in reverse order before performing the `dequeue` operation. this costs `O(n)`