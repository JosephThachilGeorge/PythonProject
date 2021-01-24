from array import *

vals= array("i",[5,2,100,10,10])

newArray= array(vals.typecode, (a for a in vals))

for i in newArray:
    print(i)