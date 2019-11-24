from Deque.deque import Deque

# Palindrome: a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run
# s.replace(" ", "")
# s.strip(), s.lstrip(), s.rstrip()


def pal_checker(str):
    char_deque = Deque()

    for ch in str:
        char_deque.add_rear(ch)

    still_equal = True

    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()

        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("ladkjfs"))
print(pal_checker("radar"))
