# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

list_1 = [int(x) for x in input().split()]
k = int(input())


count=0
for i in list_1:
    if i==k:
        count+=1
print(count)
print(list_1)
        