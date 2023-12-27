import numpy as n

l = [[1,2,3], [4,5,6]]

arr = n.array(l)

x_sum = n.sum(arr, axis=1)

print(x_sum)
