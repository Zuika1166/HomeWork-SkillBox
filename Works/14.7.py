#1

# OS info is
# uname_result(system='Windows', node='LAPTOP-76POS67P', release='10', version='10.0.19042', machine='AMD64')
#
# Python version is 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] ('64bit', 'WindowsPE')

# #2
# print("Введите первую точку")
#
# x1 = float(input('X: '))
#
# y1 = float(input('Y: '))
#
# print("\nВведите вторую точку")
#
# x2 = float(input('X: '))
#
# y2 = float(input('Y: '))
#
#
#
# x_diff = x1 - x2
#
# y_diff = y1 - y2
#
# if x_diff == 0.00:
#     print('x равно 0, программа не может быть продолжена')
#     exit()
#
#
# k = y_diff / x_diff
#
# b = y2 - k * x2
#
#
#
# print("Уравнение прямой, проходящей через эти точки:")
#
# print("y = ", k, " * x + ", b)

# #3
# def sum_num(num):
#     count = 0
#
#     for i in str(num):
#         count += int(i)
#
#     return count
#
#
# def count_num(num):
#     count = 0
#
#     for i in str(num):
#         count += 1
#     return count
#
# num = int(input('Введите число: '))
#
# print('Сумма цифр:', sum_num(num))
# print('Количество цифр в числе', count_num(num))
# print('Разность суммы и количества цифр:', sum_num(num) - count_num(num))

# #4
# n1 = float(input("Введите целое число: "))
# n2 = 0
#
# while n1 > 0:
#     # находим остаток - последнюю цифру
#     digit = n1 % 10
#     # делим нацело - удаляем последнюю цифру
#     n1 = n1 // 10
#     # увеличиваем разрядность второго числа
#     n2 = n2 * 10
#     # добавляем очередную цифру
#     n2 = n2 + digit
#
# print('"Обратное" ему число:', n2)


# #5
# n = int(input())
# i = 1
# while i <= n:
#     i = i + 1
#     if n % i == 0:
#         print('Наименьший делитель, отличный от еденицы:', i)
#         break