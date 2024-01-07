def F(a,result):
        return result*a
    
a = int(input())
b=int(input())
result=1
while b > 0:
        result=F(a,result)
        b-=1
print(result)
