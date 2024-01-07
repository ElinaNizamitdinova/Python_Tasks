k = input()


one=["A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"]
two=["D", "G", "Д", "К", "Л", "М", "П", "У"]
tree=["B", "C", "M", "P","Б", "Г", "Ё", "Ь", "Я"]
four=["F", "H", "V", "W", "Y","Й", "Ы"]
five = ["Ж", "З", "Х", "Ц", "Ч","K" ]
eight=["J", "X","Ш", "Э", "Ю"]
ten=["Q", "Z" ]
k=k.upper()
summ=0
for i in k:
    if i in one:
        summ+=1
    elif i in two:
        summ+=2    
    elif i in tree:
        summ+=3
    elif i in four:
        summ+=4
    elif i in five:
        summ+=5
    elif i in eight:
        summ+=8
    else:
        summ+=10
print(summ)