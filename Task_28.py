# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def Sum(n,m):
    if m==0:
        return n
    else:
        n+=1
        m-=1
        return Sum(n,m)

n=int(input("Введите значение n "))
m=int(input("Введите значение m "))
print(Sum(n,m))