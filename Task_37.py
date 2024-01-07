import random

n=int(input())
numbers=[random.randint(1,15) for _ in range(n)]
print(numbers)
newNum=[]
n-=1
while n >= 0:
    newNum.append(numbers[n])
    n=n-1
print(newNum)



