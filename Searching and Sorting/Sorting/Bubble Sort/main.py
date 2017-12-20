def bubble_sort(alist):
    """
    Bubble sort
    Args:
        alist: List to be sorted
    """
    for num in range(len(alist)-1, 0, -1):
        un_sorted = True
        for i in range(num):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                un_sorted = False
        # Stop sorting if already sorted
        if un_sorted:
            return

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(a_list)
print(a_list)
