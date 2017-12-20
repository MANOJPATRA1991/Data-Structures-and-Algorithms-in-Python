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
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    # Item not found
    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(testlist, 3))
print(sequential_search(testlist, 13))
