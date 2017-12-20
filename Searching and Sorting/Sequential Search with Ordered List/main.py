def ordered_sequential_search(alist, item):
    """
    Ordered Sequential Search
    Args:
        alist: List in which to search
        item: Item to search for
    Returns:
        Boolean: Indicates if item is found or not
    """
    # Keep track of the position of the item
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            # Check if item searched is greater than item at a particular index
            # Stop if true means item searched for is not in the list
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1
    # Item not found
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(ordered_sequential_search(testlist, 3))
print(ordered_sequential_search(testlist, 13))
