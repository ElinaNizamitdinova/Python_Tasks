# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).


k= int(input("Введите число k"))

def sum_dividers(number: int):
    dividers = set()
    dividers.add(1)
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            dividers.add(i)
            dividers.add(number // i)

    return sum(dividers)


def find_friendly(max_number: int):
    for i in range(1, max_number + 1):
        var = sum_dividers(i)
        if var <= max_number:
            if sum_dividers(var) == i:
                if i < var:
                    print(i, var)


find_friendly(k)