import math
"""Создание программы на Python для решения квадратного уравнения"""
# Квадратное уравнение имеет следующий вид: a * x ** 2 + b * x + c = 0
# Уравнение возможно решить через дескриминант d = b ** 2 - 4 * a * c
# Если d > 0: уравнение имеет 2 корня, (-b ± math.sqrt(d)) / (2 * a)
# Если d == 0: уравнение имеет один корень, -b / 2 * a
# Если d < 0: уравнение не имеет корней
# a != 0 - это строгое условие для выполнения квдратного уравнения
print('Для решения квадратного уравнения a * x ** 2 + b * x + c = 0, введите коэффициенты a, b, c.')
a = input('Введите a: ')
b = input('Введите b: ')
c = input('Введите c: ')

symbol = '!@#$%ˆ?/<>,&*(){}[]'
def symbol_check(val):
    if val.isalpha():
        return False
    for i in val:
        if i in symbol:
            return False
    return True
def type_check(vars):
    for i in vars:
        if i == '.':
            return float(vars)
    return int(vars)
def zero_check(var):
    if var == 0:
        return 0
    return var
if symbol_check(a) and symbol_check(b) and symbol_check(c):
    a = type_check(a)
    b = type_check(b)
    c = type_check(c)
    # or
    # a = float(a)
    # b = float(b)
    # c = float(c)
    while a != 0:
        def disk(a, b, c):
            d = b ** 2 - 4 * a * c
            return d
        d = disk(a, b, c)
        # print(f'Дискриминант равен: {round(d, 5)}')
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print(f'Уравнение имеет два корня: {round(zero_check(x1), 5)} и {round(zero_check(x2), 5)}')
            break
        elif d == 0:
            x = -b / (2 * a)
            print(f'Уравнение имеет один корень: {round(zero_check(x), 5)}')
            break
        else:
            print('Уравнение не имеет корней')
            break
    else:
        print('Это не квадратное уравнение')
else:
    print('Некорректный ввод! Вводите целые числа и десятичные (через точку)')

