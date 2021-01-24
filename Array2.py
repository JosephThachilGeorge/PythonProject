from array import *

arr= array("i",[])

x= int(input("Enter the range of array"))

for i in range(x):
    y = int(input("Enter the the value"))

    arr.append(y)

for j in arr:
  print(j)

z = int(input("Enter the value that you want for index"))

print(arr.index(z))






