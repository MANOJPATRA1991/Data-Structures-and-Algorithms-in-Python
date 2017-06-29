def toStr(n,base):
   convertString = "0123456789ABCDEF"
   
   # If number less than base, return the charater at position n from convertString 
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))
