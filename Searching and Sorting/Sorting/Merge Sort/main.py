def merge_sort(alist):
    print("Splitting ", alist)
    work = [None] * len(alist)
    rec_merge_sort(work, 0, len(alist)-1)


def rec_merge_sort(work, start, end):
    # if list contains only one item,
    # list is already sorted
    if start == end:
        return
    else:
        print(work)
        mid = (start + end) // 2
        rec_merge_sort(work, start, mid)
        rec_merge_sort(work, mid + 1, end)
        merge(work, start, mid + 1, end)


def merge(work, start, end, upper_bound):
    i = 0
    lower_bound = start
    mid = end-1
    # size of list after merge
    n = upper_bound - lower_bound + 1

    # compare two sublists per item
    # and insert in original list
    while start <= mid and end <= upper_bound:
        if alist[start] < alist[end]:
            work[i] = alist[start]
            i = i + 1
            start = start + 1
        else:
            work[i] = alist[end]
            i = i + 1
            end = end + 1

    # if all items from second list are in original list
    # insert all of the items from the first list
    # as list already sorted
    while start <= mid:
        work[i] = alist[start]
        i = i + 1
        start = start + 1

        # if all items from first list are in original list
        # insert all of the items from the second list
        # as list already sorted
    while end <= upper_bound:
        work[i] = alist[end]
        i = i + 1
        end = end + 1

    for k in range(0, n):
        alist[lower_bound+k] = work[k]

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(alist)
print(alist)