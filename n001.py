import numpy as n
# data distribution 
arr = n.array([1,2,3,4])
# n.random.shuffle(arr)
# arr2 = n.random.permutation(arr)
# print(arr2)
# print(arr)
# 0-1
# sum of probility 1 
d = n.random.choice(arr, p=[0.1, 0.3, 0.6, 0.0], size=(2,2))
print(d)
# seaborn 










