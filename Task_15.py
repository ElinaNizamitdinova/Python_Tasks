# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
N = int(input("Колличество арбузов "))
n=[int(x) for x in input().split()]
mini=n[0]
maxi=n[0]
for i in range(N-1):
    if n[i] > maxi:
        maxi=n[i]
    elif n[i]< mini:
        mini=n[i]
print(mini,maxi)