import random

n = int(input()) 
list1= [random.randint(1,5) for _ in range(n)]
print(list1)
maxi=0
mimi=10
for i in list1:
    if i>maxi:
        maxi=i
    if i<mimi:
        mimi=i
print(maxi,mimi)
for i in range(n):
    if list1[i]==maxi:
        list1[i]=mimi
print(list1)