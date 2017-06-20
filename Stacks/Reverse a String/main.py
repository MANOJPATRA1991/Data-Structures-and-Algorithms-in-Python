from test import testEqual
from Stacks.stack1 import Stack

def revstring(mystr):
    # your code here
    s=Stack()
    for i in range (0,len(mystr)):
        s.push(mystr[i])
    newstr=''
    while not s.isEmpty ():
        newstr += s.pop ()
    return newstr
testEqual(revstring('apple'),'elppa')
testEqual(revstring('x'),'x')
testEqual(revstring('1234567890'),'0987654321')
