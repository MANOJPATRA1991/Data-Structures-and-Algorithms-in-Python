def ordered_sequential_search(alist, item):
    """
    Ordered Sequential Search
    Args:
        alist: List in which to search
        item: Item to search for
    Returns:
        Boolean: Indicates if item is found or not
    """
    # Keeps track of the position of the item
    pos = 0
    # Keeps track of item's discovery
    found = False
    # stop is True if item at pos is greater than the searched item
    stop = False
    
    # Keep searching if pos is valid and
    # item is not found and 
    # next element in the list is less than the searched item
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            # Item found
            found = True
        else:
            # Check if item at index 'pos' is greater than searched item
            if alist[pos] > item:
                # Stop as searched item is not in the list
                stop = True
            else:
                # Item not found and item at 'pos' is less than searched item 
                # => move to next position
                pos = pos+1

    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(ordered_sequential_search(testlist, 3))
print(ordered_sequential_search(testlist, 13))
