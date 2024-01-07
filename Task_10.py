
# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть
coins =[int(x) for x in input().split()]
countZero=countOne=0
for i in coins:
    if int(i) ==0:
        countZero+=1
    else:
        countOne+=1
if countZero>countOne:
    print(countOne)
else:
    print(countZero)