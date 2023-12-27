name = "anna"

R_name = ""
# for x in name:
#     R_name += x


a = len(name)-1

while 0 <= a:
   print(a)
   R_name +=  name[a]
   a-=1
print(R_name)

if name == R_name:
   print("pelidrome")
else :
   print("not pelidrome")