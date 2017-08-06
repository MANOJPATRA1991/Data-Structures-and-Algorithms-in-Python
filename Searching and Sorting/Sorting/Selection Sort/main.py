def selection_sort(alist):
    for num in range(len(alist)-1, 0, -1):
        max_pos = 0
        for i in range(1, num+1):
            if alist[i] > alist[max_pos]:
                max_pos = i
        alist[num], alist[max_pos] = alist[max_pos], alist[num]

alist = [54,26,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)