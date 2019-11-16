def sequential_search(alist, item):
    """
    Sequential Search
    Args:
        alist: List in which to search
        item: Item to search for
    Returns:
        Boolean: Indicates if item is found or not
    """
    # Keeps track of item's position
    pos = 0
    # Keeps track of item's discovery
    found = False

    # Keep running the while loop if item is not found 
    # and pos is valid
    while pos < len(alist) and not found:
        if alist[pos] == item:
            # Item found
            found = True
        else:
            # Item not found => move to next position
            pos = pos + 1

    return found


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(testlist, 3))
print(sequential_search(testlist, 13))
