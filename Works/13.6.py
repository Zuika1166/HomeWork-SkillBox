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