# generate all the strings of length n drawn from 0...k-1
def k_string(n, k, my_list):
    if n < 1:
        print(my_list)
    else:
        for i in range (0,k):
            if len(my_list) != 0:
                del my_list[n - 1]
            my_list.insert(n - 1, i)
            k_string(n - 1, k, my_list)


def gen(n,k):
    my_list = []
    for x in range(0,n):
        my_list.append(0)
    k_string(n, k, my_list)


gen(2,4)
