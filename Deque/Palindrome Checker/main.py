from Deque.deque import Deque


def pal_checker(str):
    chardeque = Deque()

    for ch in str:
        chardeque.add_rear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.remove_front()
        last = chardeque.remove_rear()

        if first is not last:
            stillEqual = False

    return  stillEqual

print(pal_checker("ladkjfs"))
print(pal_checker("radar"))
