def short_bubble_sort(alist):
    exchange = True
    pass_num = len(alist) - 1
    while pass_num > 0 and exchange:
        exchange = False
        for i in range(pass_num):
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]

        pass_num = pass_num - 1

alist=[20,30,40,90,50,60,70,120,100,110]
short_bubble_sort(alist)
print(alist)