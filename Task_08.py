# Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Выведите yes или no соответственно.



a =  int(input("Введите знвчение n "))
b =  int(input("Введите знвчение n "))
c =  int(input("Введите знвчение n "))
if c%a==0 or c%b==0:
    print("yes")
else:
    print("no")