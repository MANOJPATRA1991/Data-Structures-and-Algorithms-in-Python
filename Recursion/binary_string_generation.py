#generate binary strings of n-bits recursively
def binary(mylist,n):
    if n<1:
        print(mylist)
    else:
        if len(mylist) != 0:
            del mylist[n-1]
        mylist.insert(n-1,0)
        binary(mylist,n-1)
        if len(mylist) != 0:
            del mylist[n-1]
        mylist.insert(n-1,1)
        binary(mylist,n-1)

def gen(num):
    mylist = []
    for x in range(0,num):
        mylist.append(0)
    binary(mylist, num)

gen(2)
