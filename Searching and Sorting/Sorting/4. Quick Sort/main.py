def quick_sort(alist):
    """
    Function to perform quick sort
    Args:
        alist: List to sort
    """
    quick_sort_helper(alist, 0, len(alist)-1)


def quick_sort_helper(alist, first, last):
    """
    Helper function to sort
    Args:
        alist: List to sort
        first: Start index
        last: Last index
    """
    # Check if list contains more than one element
    # because a list with one element is already sorted
    if first < last:
        # Get the split point to further quick sort
        split_point = partition(alist, first, last)

        # No need to adjust the pivot value (split point).
        # The pivot value is now in its correct place in the list
        # as all elements less than pivot are to the left of pivot
        # and all elements greater than pivot are to the right of pivot

        # Quick sort the left half of pivot value
        quick_sort_helper(alist, first, split_point-1)

        # Quick sort the right half of the pivot value
        quick_sort_helper(alist, split_point+1, last)


def partition(alist, first, last):
    """
    Separate the list
    Args:
        alist: List to partition
        first: Start index
        last: Last index
    """
    # Get the mid index
    mid = (first + last) // 2
    # Get the pivot index
    pivot_index = median_finder(alist, first, last, mid)
    # Exchange pivot with first element
    alist[first], alist[pivot_index] = \
        alist[pivot_index], alist[first]
    # Pivot value is at the beginning
    pivot_value = alist[first]

    left_mark = first + 1
    right_mark = last

    done = False

    while not done:
        # If left marked value is less than
        # pivot value and left mark is to the
        # left of right mark, move forward
        while left_mark <= right_mark and \
                alist[left_mark] <= pivot_value:

            left_mark = left_mark + 1

        # If right marked value is greater than
        # pivot value and left mark is to the
        # left of right mark, move backwards
        while right_mark >= left_mark and \
                alist[right_mark] >= pivot_value:

            right_mark = right_mark - 1

        # If left mark is to the right of right mark, STOP
        if right_mark < left_mark:
            done = True
        else:
            alist[left_mark], alist[right_mark] = \
                alist[right_mark], alist[left_mark]

    # Exchange pivot value with right_mark
    # now pivot is at its correct position
    alist[first], alist[right_mark] = \
        alist[right_mark], alist[first]

    # The pivot value is now in its correct place in the list
    return right_mark


def median_finder(alist, first, last, mid):
    """
    Select pivot value using median of three technique
    Median of three technique selects the mid value of first,
    last and middle element(i.e., the element which lies
    between the other two)
    Args:
        alist: List for which to find pivot value
        first: Start index
        last: Last index
        mid: Middle index
    """
    min_value = min(alist[first], alist[mid], alist[last])
    return alist.index(min_value)


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)
