# 1
num = float(input('Введите число: '))
n = 0
while True:
    if num > 1:
        n += 1
        num /= 10 ** n
        if num <= 10:
            print(num, "* 10 ^", n)
            break
    elif num >= 0 or num <= 10:
        num *= 10 ** n
        n += 1
        if num <= 10:
            print(num, "* 10 ^  -", n)
            break

#2
one = int(input('Введите первое число: '))
two = int((input('Введите второе число: ')))
three = int(input('Введите третье число: '))

def max_three(one, two, three):
    max_two = max(one, two)
    print('Максимум из 3 чисел, число:', max(max_two, three))


max_three(one, two, three)

#3
first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
count = 0

def first_num_reverse(first_num, count):
    while first_num > 0:
        # находим остаток - последнюю цифру
        digit = first_num % 10
        # делим нацело - удаляем последнюю цифру
        first_num = first_num // 10
        # увеличиваем разрядность второго числа
        count = count * 10
        # добавляем очередную цифру
        count = count + digit

    return count

def second_num_reverse(second_num, count):
    while second_num > 0:
        # находим остаток - последнюю цифру
        digit = second_num % 10
        # делим нацело - удаляем последнюю цифру
        second_num = second_num // 10
        # увеличиваем разрядность второго числа
        count = count * 10
        # добавляем очередную цифру
        count = count + digit

    return count

print('\nПервое число наоборот:', first_num_reverse(first_num, count))
print('Второе число наоборот:', second_num_reverse(second_num, count))
print('Сумма:', first_num_reverse(first_num, count) + second_num_reverse(second_num, count))
print('\nСумма наоборот:', first_num + second_num)


#второй вариант (карельку изменен def)
first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
count = 0

def num_reverse(num, count):
    while num > 0:
        # находим остаток - последнюю цифру
        digit = num % 10
        # делим нацело - удаляем последнюю цифру
        num = num // 10
        # увеличиваем разрядность второго числа
        count = count * 10
        # добавляем очередную цифру
        count = count + digit

    return count


print('\nПервое число наоборот:', num_reverse(first_num, count))
print('Второе число наоборот:', num_reverse(second_num, count))
print('Сумма:', num_reverse(first_num, count) + num_reverse(second_num, count))
print('\nСумма наоборот:', first_num + second_num)


#4
# Не знаю как вывести порядок
#string = input('Введите строку: ')

string = 123e54    # Пример
count = 0
count_two = ''

print(string)
print()

for i in str(string):
    if i == 'e':
        break
    elif i == '.':
        pass
    else:
        count_two += i

for j in str(string):
    if j != '+':
        count += 1
    else:
        pass
print(count)
print(count_two)

#6
def first_num():
    first_n = int(input("Введите первое число: "))

    first_num_count = 0
    temp = first_n

    while temp > 0:
        first_num_count += 1
        temp = temp // 10
    if first_num_count < 3:
        print("В первом числе меньше трёх цифр.")

    else:
        last_digit = first_n % 10
        first_digit = first_n // 10 ** (first_num_count - 1)
        between_digits = first_n % 10 ** (first_num_count - 1) // 10
        first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
        print('Изменённое первое число:', first_n)

def second_num(first_n, between_Digits):

    second_n = int(input("\nВведите второе число: "))

    second_num_count = 0
    temp = second_n
    while temp > 0:
        second_num_count += 1
        temp = temp // 10

    if second_num_count < 4:
        print("Во втором числе меньше четырёх цифр.")
    else:
        last_digit = second_n % 10
        first_digit = second_n // 10 ** (second_num_count - 1)
        between_Digits = second_n % 10 ** (second_num_count - 1) // 10
        second_n = last_digit * 10 ** (second_num_count - 1) + between_digits * 10 + first_digit

        print('Изменённое второе число:', second_n)

        print('\nСумма чисел:', first_n + second_n)


#8
d_from = 0
d_to = 4
max_danger = float(input('Введите максимальное допустимый уровень опастности: '))

depth = d_from + (d_to - d_from) / 2
danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

if max_danger < 0:
    print('Ошибка! Максимально допустимый уровнь опастности, должно быть больше 0')
else:
    print('Depth:', depth, 'Danger:', danger)

    while abs(danger) > max_danger:
        if danger > 0:
            d_from = depth
        else:
            d_to = depth

        depth = d_from + (d_to - d_from) / 2
        danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
        print('Depth:', depth, 'Danger:', danger)

    print('Приблизительная глубина безопастности кладки', depth, 'м')