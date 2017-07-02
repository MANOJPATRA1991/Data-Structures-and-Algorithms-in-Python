from Stacks.stack1 import Stack

r_stack = Stack()


def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    # proceed only if base is positive
    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n%base])
        n = n // base

    result = ""

    while not r_stack.isEmpty():
        result += str(r_stack.pop())

    return result

print(to_str(1453, 16))