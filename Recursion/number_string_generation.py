#generate all the strings of length n drawn from 0...k-1
def KString(n, k, mylist):
    if n < 1:
        print(mylist)
    else:
        for i in range (0,k):
            if len(mylist) != 0:
                del mylist[n-1]
            mylist.insert(n-1, i)
            KString(n-1, k, mylist)

def gen(n,k):
    mylist = []
    for x in range(0,n):
        mylist.append(0)
    KString(n,k,mylist)

gen(2,4)
