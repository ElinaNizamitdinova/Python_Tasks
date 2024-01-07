# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером) 

n=[int(x) for x in input().split()]
count=0
result=[]
for i in range(0,len(n)-1):
    if n[i]<n[i+1]:
        count+=1
        result.append(str(n[i])+" < "+str(n[i+1]))
print(count,":",result)
            
