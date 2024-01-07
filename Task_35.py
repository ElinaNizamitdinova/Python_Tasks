def PrimeNumbers(numbers):
    count=1
    for i in range(1,numbers//2+1):
        if numbers%i==0:
            count+=1
    if count==2:
        return "Yes"
    return "No"
n= int(input("Введите число "))
answer=PrimeNumbers(n)
print(answer)