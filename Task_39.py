import random 

n = int(input("Введите длину первого массива "))
list1=[random.randint(1,15) for _ in range(n)]
print(list1)
m = int(input("Введите длину второго массива "))
list2=[random.randint(1,15) for _ in range(n)]
print(list2)
data= [i for i in list1 if i not in list2]
print(data)