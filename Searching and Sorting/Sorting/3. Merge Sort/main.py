def merge_sort(alist):
    """
    Perform merge sort on a list
    Args:
        alist: List to sort
    """
    print("Splitting ", alist)
    # Temporary list to store sorted list
    work = [None] * len(alist)
    rec_merge_sort(work, start=0, end=len(alist)-1)


def rec_merge_sort(work, start, end):
    """
    Helper function for sorting
    Args:
        work: Temporary list to store the final sorted list
        start: Start index
        end: End index
    """
    # Base case: if list contains only one item,
    # list is already sorted
    if start == end:
        return
    else:
        print(work)
        mid = (start + end) // 2
        rec_merge_sort(work, start, mid)
        rec_merge_sort(work, mid + 1, end)
        merge(work, start, mid + 1, end)


def merge(work, start_left, start_right, upper_bound):
    """
    Helper function to merge two lists
    Args:
        work: Temporary list
        start_left: Start index of left side list
        start_right: Start index of right side list (mid + 1)
        upper_bound: End index of original list
    """
    # Keep track of index in temporary list
    # whose length is the same as the original list
    i = 0
    lower_bound = start_left
    mid = start_right - 1
    # size of list after merge
    n = upper_bound - lower_bound + 1

    # compare two sub lists per item
    # and insert in original list
    while start_left <= mid and start_right <= upper_bound:
        work[i] = min(a_list[start_left], a_list[start_right])
        if work[i] == a_list[start_left]:
            start_left += 1
        else:
            start_right += 1
        i += 1

    # If all items from second list are in original list
    # insert all of the items from the first list
    # as list is already sorted
    while start_left <= mid:
        work[i] = a_list[start_left]
        i += 1
        start_left += 1

    # If all items from first list are in original list
    # insert all of the items from the second list
    # as list is already sorted
    while start_right <= upper_bound:
        work[i] = a_list[start_right]
        i += 1
        start_right += 1

    # Transfer the temporary list "work" back to original
    # list "a_list"
    for k in range(0, n):
        a_list[lower_bound+k] = work[k]


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)
