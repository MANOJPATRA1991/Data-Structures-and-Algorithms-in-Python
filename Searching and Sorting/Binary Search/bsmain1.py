# BINARY SEARCH USING RECURSION


def binary_search(alist, item):
    """
    Binary search
    Args:
        alist: List in which to search
        item: Item to search for
    Returns:
        Boolean: Indicates if item is found or not
    """
    # Base case
    if len(alist) == 0:
        return False
    else:
        # Find the mid value 
        midpoint = len(alist) // 2
        
        # If middle element is what we are searching for
        if alist[midpoint] == item:
            return True
        else:
            # If item is less than the middle element,
            # do a binary search on the left half of the list
            if item < alist[midpoint]:
                return binary_search(alist[:midpoint], item)
            # If item is greater than the middle element,
            # do a binary search on the right half of the list
            else:
                return binary_search(alist[midpoint + 1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
