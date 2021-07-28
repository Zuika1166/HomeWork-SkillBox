#1
num = int(input('Input number: '))
count = 0
def summa(num, count):
  for i in range(1, num+1):
    count += i
  print('Я знаю, что сумма чисел от 1 до', num, 'равна', count)
summa(num, count)

#2
num = int(input('Input number: '))
def positive():
  print('Ok')

def negative():
  print('Error')

def test(num):
  if num >= 0:
    positive()
  elif num < 0:
    negative()

test(num)


#3
num = int(input('Input number: '))
do = int(input('Вывести сумму его цифр, максимальную или минимальную цифру(input please 1 or 2 or 3: '))
count_one = 0
all_two = 0
def doing(num, do, count_one, all_two):
  if do == 1:
    for i in str(num):
      count_one += int(i)
    print('Сумма чисал числа' , num, 'равна:', count_one)
  elif do == 2:
      pass
  elif do == 3:
    pass
  else:
    print('Введен не правильный номер')
doing(num, do, count_one, all_two)

#4
num = int(input('Введите число: '))
count = 0
while True:
    num = int(input('Введите число: '))
    print(str(num)[::-1])

    if num == 0:
        print('Программа завершена')
        break

#5
string = str(input('Введите текст: '))
num = int(input('Введите цифру которую ищем: '))
world = str(input('Какую букву мы ищем: '))
count_num = 0
count_world = 0
def count_letters(string, num, world, count_num, count_world):
    for i in string:
        if i == str(num):
            count_num += 1
        elif i == world:
            count_world += 1

    print('Количество цифр', str(num) + ':', count_num)
    print('Количество букв', world + ':', count_world)

# 6 (money)
x = int(input('Введите x графика: '))
y = int(input('Введите y графика: '))

def money(x, y):
    if x >= -1 and x <= 1 or y >= -1 and y >= 1:
        print('Монетка где то рядом')
    else:
        print('Монетки нет в области')


money(x, y)

#8
import math
num = int(input('Введите 1 число:'))
num2 = int(input('Введите 2 число: '))
print('НОД чисел', num, 'и', num2, 'равен: ', math.gcd(num, num2))

# Второй вариант сделаный алгоритмом Евлклида
a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
maximum = 0
while a != 0 and b != 0:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a+b)




#9
def rock_paper_scissors():
    #Здесь будет игра "Камень, ножницы, бумага"
    import random
    robot = random.randrange(1, 3+1, +1)
    if robot == 1:
        robot = 'Ножницы'
    elif robot == 2:
        robot = 'Бумага'
    elif robot == 3:
        robot = 'Камень'
    what_do = str(input('Введите (Камень, Ножнцяы, Бумага): '))

    if what_do == robot:
        print('You win')
    elif what_do == 'Камень' and robot == 'Ножницы':
        print('You win')
    elif what_do == 'Ножницы' and robot == 'Бумага':
        print('You win')
    elif what_do == 'Бумага' and robot == 'Камень':
        print('You win')
    else:
        print('You loos')

def quess_the_number():
    #Здесь будет игра "Угадай число"
    number_up = 4
    num = int(input('Введите число: '))
    while num != number_up:
        num = int(input('Введите число: '))
    print('Вы выйграли')

def mainMenu():
    #Здесь главное меню игры
    what_game = int(input('Какую игру вы хотите запустить: \n1. Камень, ножницы, бумага\n2. Угадай число\nВаш ответ: '))
    if what_game == 1:
        rock_paper_scissors()
    elif what_game == 2:
        quess_the_number()
    else:
        print('Не верное число')
mainMenu()







#4
n1 = int(input("Введите целое число: "))
n2 = 0

def num_revers(n1, n2):

    # проверка на дурака
    if n1 == 0:
        print('Программа завершена!')
        exit()

    while n1 > 0:
        # находим остаток - последнюю цифру
        digit = n1 % 10
        # делим нацело - удаляем последнюю цифру
        n1 = n1 // 10
        # увеличиваем разрядность второго числа
        n2 = n2 * 10
        # добавляем очередную цифру
        n2 = n2 + digit

    print('Обратное" ему число:', n2)

num_revers(n1, n2)

# 10
# Вы в спальне. Куда идём?
# 1 — в ванну
# 2 — в коридор

while True:
    print('Вы в спальне. Куда идем?\n1- в ванну\n2- в коридор')
    what = int(input(''))

    if what == 1:
        # На этом моменте не понял как менять варианты  в print()