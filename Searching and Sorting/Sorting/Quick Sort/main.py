def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist)-1)


def quick_sort_helper(alist, first, last):
    # get the split point to further quick sort
    if first < last:
        split_point = partition(alist, first, last)

        # quick sort the left half of pivot value
        quick_sort_helper(alist, first, split_point-1)
        # quick sort the right half of the pivot value
        quick_sort_helper(alist, split_point+1, last)


def partition(alist, first, last):
    mid = (first + last) // 2
    pivot_index = median_finder(alist, first, last, mid)
    alist[first], alist[pivot_index] = alist[pivot_index], alist[first]
    pivot_value = alist[first]

    left_mark = first + 1
    right_mark = last

    done = False

    while not done:

        while left_mark <= right_mark and alist[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while alist[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]

    alist[first], alist[right_mark] = alist[right_mark], alist[first]

    return right_mark


# select pivot value using median of three technique
def median_finder(alist, first, last, mid):
    if alist[first] < alist[last]:
        if alist[last] < alist[mid]:
            return last
        else:
            return mid
    else:
        if alist[first] < alist[mid]:
            return first
        else:
            return  mid


alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist)
print(alist)