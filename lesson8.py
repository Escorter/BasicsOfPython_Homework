'''Домашнее задание к уроку 8 "Основы языка Python". Студент Абрамов Алексей
_______________________________________________________________________________
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.'''


class Date:
    date = None
    day = None
    month = None
    year = None

    def __init__(self, d):
        Date.date = d

    @classmethod
    def extractor(cls):
        s = cls.date.split("-")
        cls.day = int(s[0])
        cls.month = int(s[1])
        cls.year = int(s[2])
        print(cls.day, cls.month, cls.year)

    @staticmethod
    def month_is_valid():

        if 0 < Date.month <= 12:
            return True
        else:
            return False


Date("23-12-2000")
print(Date.date)  # дата в первоначальном формате
Date.extractor()  # дата после роспуска строки даты
print(Date.month_is_valid())  # проверка на валидность месяца

Date("23-16-2020")
Date.extractor()
print(Date.month_is_valid())

'''____________________________________________________________________________
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на 0.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в кач-ве 
делителя программа должна корректно обработать эту ситуацию и не завершиться 
с ошибкой.'''


class DivError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input("Введите делимое:"))
b = int(input("Введите делитель:"))

try:
    if b == 0:
        raise DivError("Делитель равен 0. На ноль делить нельзя!")
except DivError as err:
    print(err)
else:
    print(f"Результат деления {a} на {b} = {a / b}")

'''____________________________________________________________________________
3. Создайте собственный класс-исключение, который должен проверять содержимое 
списка на наличие только чисел. Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами. 
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, 
пока пользователь сам не остановит работу скрипта, введя, например, команду 
«stop». При этом скрипт завершается, сформированный список с числами выводится 
на экран. Подсказка: для этого задания примем, что пользователь может вводить 
только числа и строки. Во время ввода пользователем очередного элемента 
необходимо реализовать проверку типа элемента. Вносить его в список, только если
 введено число. Класс-исключение должен не позволить пользователю ввести текст 
 (не число) и отобразить соответствующее сообщение. При этом работа скрипта 
 не должна завершаться.'''


class NumError(Exception):
    def __init__(self, txt):
        self.txt = txt


res = []
while True:
    number = input("Введите целое число. Для завершения введите 'stop'")
    if number == 'stop':
        break
    try:
        if number.isdigit():
            res.append(int(number))
        else:
            raise NumError("Вы ввели не число.")
    except NumError as err:
        print(err)
print(res)

'''____________________________________________________________________________
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий 
склад. А также класс «Оргтехника», который будет базовым для классов-наследников
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом 
классе определите параметры, общие для приведённых типов. В классах-наследниках 
реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают 
за приём оргтехники на склад и передачу в определённое подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также 
других данных, можно использовать любую подходящую структуру (например, словарь)

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
 пользователем данных. Например, для указания количества принтеров, отправленных
 на склад, нельзя использовать строковый тип данных. Подсказка: постарайтесь 
реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на 
уроках по ООП.'''


class Storage:
    info = "Склад оргтехники"
    store = {}
    business_dep = {'printer': 0, 'scanner': 0, 'xerox': 0}
    legal_dep = {'printer': 0, 'scanner': 0, 'xerox': 0}
    tech_dep = {'printer': 0, 'scanner': 0, 'xerox': 0}
    printer_count = 0
    scanner_count = 0
    xerox_count = 0


class Equipment:
    color = 'белый'
    brand = 'HP'
    voltage = 220


class Printer(Equipment):
    def __init__(self, paper_size):
        self.paper_size = paper_size

    @classmethod
    def add_to_store(cls, n):
        try:
            n = int(n)
            Storage.printer_count += n
            Storage.store['printer'] = Storage.printer_count
        except ValueError:
            print("Ошибка при добавлении на склад. Кол-во должно быть числом")

    @classmethod
    def transfer_to_dep(cls, dep, n):
        if Storage.printer_count > n:
            dep['printer'] += n
            Storage.printer_count -= n
            Storage.store['printer'] = Storage.printer_count
        else:
            print("На складе недостаточно принтеров")


class Scanner(Equipment):
    def __init__(self, output_file):
        self.output_file = output_file

    @classmethod
    def add_to_store(cls, n):
        try:
            n = int(n)
            Storage.scanner_count += n
            Storage.store['scanner'] = Storage.scanner_count
        except ValueError:
            print("Ошибка при добавлении на склад. Кол-во должно быть числом")

    @classmethod
    def transfer_to_dep(cls, dep, n):
        if Storage.scanner_count > n:
            dep['scanner'] += n
            Storage.scanner_count -= n
            Storage.store['scanner'] = Storage.scanner_count
        else:
            print("На складе недостаточно сканеров")


class Xerox(Equipment):
    def __init__(self, print_speed):
        self.print_speed = print_speed

    @classmethod
    def add_to_store(cls, n):
        try:
            n = int(n)
            Storage.xerox_count += n
            Storage.store['xerox'] = Storage.xerox_count
        except ValueError:
            print("Ошибка при добавлении на склад. Кол-во должно быть числом")

    @classmethod
    def transfer_to_dep(cls, dep, n):
        if Storage.xerox_count > n:
            dep['xerox'] += n
            Storage.xerox_count -= n
            Storage.store['xerox'] = Storage.xerox_count
        else:
            print("На складе недостаточно ксероксов")


p1 = Printer('A4')  # создание экземпляра принтера и выводим инфо про него:
print(f'Принтер {p1.color} {p1.brand}, размер бумаги {p1.paper_size}')

Printer.add_to_store(9)  # отправили на склад 9 принтеров

s1 = Scanner('pdf')
Scanner.add_to_store(6)  # отправили на склад 6 сканеров

x1 = Xerox(30)
Xerox.add_to_store('xerox')  # пытаемся отправить на склад ксерокс с
# указанием кол-ва не числом -> выдает обработанную ошибку
Xerox.add_to_store(4)  # отправили на склад 4 ксерокса

print(Storage.store)  # оборудование на склада

Printer.transfer_to_dep(Storage.legal_dep, 8)  # переместили 8 принтеров в
# юр.деп

Scanner.transfer_to_dep(Storage.legal_dep, 2)  # переместили 2 сканера в юр.деп.

print("Склад:", Storage.store)  # оборудование на складе
print("Юрид. департ.:", Storage.legal_dep)  # оборудование в юрид. департаменте

Printer.transfer_to_dep(Storage.legal_dep, 3)  # хотим переместить в юр. деп.
# еще 3 принтера, но на складе уже нет столько принтеров -> уведомление


'''____________________________________________________________________________
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комп- 
лексное число». Реализуйте перегрузку методов сложения и умножения комплексных 
чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплек-
сные числа), выполните сложение и умножение созданных экземпляров. Проверьте 
корректность полученного результата.'''


class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        print(f"{self.re}+{self.im}i")
        return ""

    def __add__(self, other):
        result = Complex(None, None)
        result.re = self.re + other.re
        result.im = self.im + other.im
        return result

    def __mul__(self, other):
        result = Complex(None, None)
        result.re = self.re * other.re - self.im * other.im
        result.im = self.re * other.im + other.re * self.im
        return result


z1 = Complex(7, 3)  # задаем вещественную и мнимую части числа z1
print(z1)
z2 = Complex(4, 2)  # задаем вещественную и мнимую части числа z2
print(z2)

zs = z1 + z2  # сумма комплексных z1 и z2
print(zs)

zp = z1 * z2  # произведение комплексных z1 и z2
print(zp)
