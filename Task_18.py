import random
n =int(input("Введите длину списка "))
list_1 = [random.randint(1,15) for _ in range(n)]
print(list_1)
k = int(input("Введите значение к "))

newK=0
fl=True
for i in list_1:
    if i==k and fl:
        print(i)
        fl=False
moreK=k+1
lessK=k+1
while fl:
    for i in list_1:
        if i==moreK or i==lessK:
            print(i)
            fl=False
    moreK+=1
    lessK-=1
