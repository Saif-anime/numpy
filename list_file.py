# li = ['apple', 'kiwi', 'Banana', 'orange', 'cherry']


# for x in li:
#     if "a" in x:
#         print(x)

# li_reverse = sorted(li, reverse=True)

#li.sort(reverse=True)

# print(li_reverse)
#li.sort()
#print(li)

li = [2,3,1,4,5,6]


for x in range(0, len(li)):
    for j in range(0, len(li)):
        if li[x] < li[j]:
            tmp = li[x]
            li[x] = li[j]
            li[j] = tmp

print(li)








