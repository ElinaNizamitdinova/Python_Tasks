# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
A=int(input("Введите число A "))
fZero,fOne=0,1
count=2
while fZero + fOne < A:
    fZero,fOne =fOne,fOne+fZero
    count+=1
if fZero + fOne == A:
    print(count+1)
else:
    print("число А не является числом Фибоначчи")