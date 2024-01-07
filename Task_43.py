
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.


import random

n = int(input())
list1 = [random.randint(1,15) for _ in range(n)]
print (list1)
result = []
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] == list1[j] and not (list1[i]in result):
            result.append(list1[i])
print(len(result))
print(result)