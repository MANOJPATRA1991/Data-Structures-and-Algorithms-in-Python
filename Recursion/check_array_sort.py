#default arguments must follow non-default arguments
def isArraySorted(n, myList=[]):
    if n == 1:
        print(myList)
        return 1
    elif myList[n-1] < myList[n-2]:
        return None
    else:
        print(myList)
        return isArraySorted(n-1, myList[0:n-1])
        

myListe=[1,2,4,3,5]
print(myListe[4])
v=isArraySorted(5, myListe)
print(v)
if isArraySorted(5, myListe)==1:
    print("Array is sorted!")
else:
    print("Array is not sorted!")
          
