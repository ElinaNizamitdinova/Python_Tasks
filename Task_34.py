string=input("Введите строку ")
string+=" "
print(string)
symbols={"у","е","ы","а","о","э","и","я","ю"}
count=0
c=[]
for i in string:
    if i in symbols:
        count+=1
    elif i==" ":
        c.append(count)
        count=0
countC=0
for i in c:
    if i==c[0]:
        countC+=1
print(c)
print(countC)
if countC==len(c):
    print("Парам пам-пам")
else:
    print("Пам парам")