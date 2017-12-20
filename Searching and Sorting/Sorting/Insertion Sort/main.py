def insertion_sort(alist):
    """
    Insertion sort
    Args:
        alist: List to be sorted
    """
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        while position > 0 and \
                alist[position-1] > current_value:
            alist[position], position = \
                alist[position-1], position - 1

        alist[position] = current_value

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print(a_list)