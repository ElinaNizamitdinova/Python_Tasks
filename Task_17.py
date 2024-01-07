# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.


listStart =[int(x) for x in input().split()]
listNew=[]
for i in listStart:
    if not i in listNew:
        listNew.append(i)
print(listStart)
print(listNew)
print(len(listNew))