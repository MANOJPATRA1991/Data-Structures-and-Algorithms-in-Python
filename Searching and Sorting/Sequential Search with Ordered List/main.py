def ordered_sequential_search(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            # check if item searched is greater than item at a particiular index
            # stop if true means item searched for is not in the list
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(ordered_sequential_search(testlist, 3))
print(ordered_sequential_search(testlist, 13))
