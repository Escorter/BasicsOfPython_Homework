'''Домашнее задание к уроку 3 "Основы языка Python". Студент Абрамов Алексей
_______________________________________________________________________________
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.'''

def my_div(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Делитель не может быть равен 0 ({e})!")


a = int(input("Введите a:"))
b = int(input("Введите b:"))
print(my_div(a, b))

'''____________________________________________________________________________
2. Выполнить функцию, которая принимает несколько параметров, описывающих 
данные пользователя: имя, фамилия, год рождения, город проживания, email,
телефон. Функция должна принимать параметры как именованные аргументы. 
Осуществить вывод данных о пользователе одной строкой.'''

def person(name, surname, birth_year, city, email, phone):
    print(f'{name} {surname}, {birth_year} г.р. Проживает в г.{city}, e-mail: '
          f'{email}, телефон: {phone}')


person(city="Стокгольм", birth_year=1965, phone="+46123456789",
       email="e-type@e-type.se", name="Мартин", surname="Эрикссон")

'''____________________________________________________________________________
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента 
и возвращает сумму наибольших двух аргументов.'''

def my_func(a, b, c):
    if a <= b and a <= c:
        s = b + c
    elif b <= a and b <= c:
        s = a + c
    else:
        s = a + b
    return s

'''____________________________________________________________________________
4. Программа принимает действительное положительное число x и целое 
отрицательное число y. Выполните возведение числа x в степень y. Задание 
реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись 
без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в 
степень с помощью оператора **. Второй — более сложная реализация без 
оператора **, предусматривающая использование цикла.'''

def my_func(x, y):
    res = x ** y
    print(res)


def my_func2(x, y):
    res = x
    if y > 0:
        for i in range(y - 1):
            res = res * x
    elif y <= 0:
        for i in range(-y + 1):
            res = res / x
    print(res)

'''____________________________________________________________________________
5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить 
ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых 
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа 
вводится специальный символ, выполнение программы завершается. Если специальный 
символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
 к полученной ранее сумме и после этого завершить программу.'''

def sum_numbers():
    s = 0
    b = True
    while b:
        n = input('Введите числа через пробел. Для выхода введите "$": ')
        m = n.split(' ')
        for i in m:
            if i == "$":
                b = False
                break
            else:
                s += int(i)
        print("Сумма введеных чисел =", s)
    print('Процедура закончена')

'''____________________________________________________________________________
6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
 и возвращающую их же, но с прописной первой буквой. 
 Например, print(int_func(‘text’)) -> Text.'''

def int_func(a):
    b = a.title()
    return b

'''____________________________________________________________________________
7. Продолжить работу над заданием. В программу должна попадать строка из слов, 
разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре. 
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с 
заглавной буквы. Используйте написанную ранее функцию int_func().'''

def int_func(a):
    b = a.title()
    print(b)