"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position in range(0,2):
        return position
    elif position > 1:
        next = get_fib(position-1) + get_fib(position-2)
        return next
    return -1

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)
