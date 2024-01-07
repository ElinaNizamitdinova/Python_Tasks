s = int(input("Значение s "))
p = int(input("Значение p "))
num=[]
for i in range(1,p//2+1):
    if p%i==0 and (p//i)+i==s and (not i in num) and (not p//i in num):
        if (p//i)>i:
            print(i,p//i)
        else:
            print(p//i,i)
        num.append(i)
        num.append(p//i)