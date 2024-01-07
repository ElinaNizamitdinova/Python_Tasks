# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.

list19=[int(x) for x in input().split()]
K=int(input())
print(list19)
newlist=[]
for i in range(K,len(list19)):
    newlist.append(list19[i])
for i in range(0,K):
    newlist.append(list19[i])
print(newlist)