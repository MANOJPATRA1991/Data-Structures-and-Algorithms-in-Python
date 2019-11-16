def gap_insertion_sort(alist, start, gap):
    """
    Perform insertion sort on sub lists of alist
    created with a gap
    Args:
        alist: List to sort
        start: Start index
        gap:
    """
    for i in range(start+gap, len(alist), gap):
        current_val = alist[i]
        position = i

        while position >= gap and alist[position-gap] > current_val:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = current_val


def shell_sort(alist):
    """
    performs shell sort
    :param alist: a list
    """
    sublist_count = len(alist) // 2

    while sublist_count > 0:
        for num in range(sublist_count):
            gap_insertion_sort(alist, num, sublist_count)

        sublist_count = sublist_count // 2


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(alist)
print(alist)
