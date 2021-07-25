# #1
# evro = int(input('Введите стоимость покупки в евро: '))
# print(evro, 'евра в рубли: ', round(60.87 * 1.25 * evro,2))
#Zuika


# #2
# import math
# how_numbers = int(input('Введите количество чисел: '))
# for i in range(how_numbers):
#     num = float(input('Введите число: '))
#     round_num_up = math.ceil(num)
#     round_num_down = math.floor(num)
#     if num >= 0:
#         print('x =', round_num_up, '    log(x) =', math.log(round_num_up))
#     else:
#         print('x =', round_num_down, '    exp(x) =', math.exp(round_num_down))

# #4
# Проверял разые варианты и вариант ввода 4444444444444444.4444 выдал 8
# x = float(input('Введите число: '))
# print(int(x * 10) % 10))



# #5
# import math
# radius_world = float(input('Введите радиус случайной планеты: '))
# world = 10.8321 * 10**11
# v = 4/3 * math.pi * radius_world**3
#
# if v < world:
#     print('Объём планеты Земля больше в', round(world / v, 3), 'раз')
# else:
#     print('Объём планеты Земля меньше в (1/' + str(round(world / v, 3)) + ') =', round(v / world, 3), 'раз')
#     #или
#     # print('Объём планеты Земля меньше в (' + str(int(v / world)) + '/' + str(round(world / v, 3)) + ') =', round(v / world, 3), 'раз')


#6
# print('Ввод:')
# start = int(input('Нижняя граница: '))
# stop = int(input('Верхняя граница: '))
# step = int(input('Шаг: '))
#
# print ()
# print('Вывод:')
# print ('C', ' F', '\n')
#
# for count in range (start, stop, step):
#     result = round (count*1.8+32)
#     print (count, '\t', result)
#     if count + step > stop:
#         count = stop
#         result = round (count*1.8+32)
#     print (count, '\t', result)


# #7
# #Не понял как работает логика (может ли конь ходить в данную клетку или нет)
# print('Введите местоположение коня: ')
# place_horse_one = float(input(''))
# place_horse_two = float(input(''))
#
# print('Введите местоположение точки на доске:')
# place_dot_one = float(input(''))
# place_dot_two = float(input(''))
#
# place_horse_one_revers = int(place_horse_one * 10 % 10)
# place_horse_two_revers = int(place_horse_two * 10 % 10)
# place_dot_one_revers = int(place_dot_one * 10 % 10)
# place_dot_two_revers = int(place_dot_two * 10 % 10)
#
#
# print(f'Конь в клетке ({place_horse_one_revers}, {place_horse_two_revers}). Точка в клетке ({place_dot_one_revers}, {place_dot_two_revers}).')

#1