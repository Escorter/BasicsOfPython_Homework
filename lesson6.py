'''Домашнее задание к уроку 6 "Основы языка Python". Студент Абрамов Алексей
_______________________________________________________________________________
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный; в рамках метода реализовать переключение
светофора в режимы: красный, жёлтый, зелёный; продолжительность первого
состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего
 (зелёный) — на ваше усмотрение; переключение между режимами должно
 осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.'''

import time


class TrafficLight:
    __color = None  # по заданию требуется создать приватный атрибут класса

    def running(self):
        for i in range(3):
            TrafficLight.__color = 'red'
            print(TrafficLight.__color)
            time.sleep(7)
            TrafficLight.__color = 'yellow'
            print(TrafficLight.__color)
            time.sleep(2)
            TrafficLight.__color = 'green'
            print(TrafficLight.__color)
            time.sleep(5)
            TrafficLight.__color = 'yellow'
            print(TrafficLight.__color)
            time.sleep(2)


a = TrafficLight()
a.running()

'''____________________________________________________________________________
2. Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей 
дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. 
метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.'''


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asfalt(self, height):
        m = self._length * self._width * 25 * height
        print(f'Необходимо {m / 1000} тонн асфальта')


r1 = Road(5000, 20)
r1.asfalt(5)

'''____________________________________________________________________________
3. Реализовать базовый класс Worker (работник).
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса 
Position, передать данные, проверить значения атрибутов, вызвать методы 
экземпляров.'''


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


p1 = Position("Джо", "Байден", "Президент США", {"wage": 8000, "bonus": 3000})
print(p1.position)
print(f"Полное имя: {p1.get_full_name()}")
print(f"Полный доход: {p1.get_total_income()}")

p2 = Position("Василий", "Рыбкин", "Тракторист", {"wage": 500, "bonus": 250})
print(p2.position)
print(f"Полное имя: {p2.get_full_name()}")
print(f"Полный доход: {p2.get_total_income()}")

'''____________________________________________________________________________
4. Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police(булево)
А также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к 
атрибутам, выведите результат. Вызовите методы и покажите результат'''


class Car:
    speed = None  # по заданию нужно создать атрибуты класса
    color = None
    name = None
    is_police = False

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed  # но по заданию же:
        self.color = color  # нужно передать те же атрибуты при создании
        self.name = name  # экземпляра дочернего класса
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 60:
            print("Скорость превышена!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 40:
            print("Скорость превышена!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


c1 = TownCar(65, 'red', 'Mercedes')
print(c1.speed)
print(c1.color)
print(c1.name)
print(c1.is_police)
c1.show_speed()
c1.turn("направо")
c1.go()
c1.stop()

print(34 * "=")

c2 = SportCar(230, 'blue', 'Lamborghini')
print(c2.speed)
print(c2.color)
print(c2.name)
print(c2.is_police)
c2.show_speed()
c2.turn("налево")
c2.go()
c2.stop()

print(34 * "=")

c3 = WorkCar(50, 'yellow', 'Liebherr')
print(c3.speed)
print(c3.color)
print(c3.name)
print(c3.is_police)
c3.show_speed()
c3.turn("направо")
c3.go()
c3.stop()

print(34 * "=")

c4 = PoliceCar(80, 'white', 'Ford', True)
print(c4.speed)
print(c4.color)
print(c4.name)
print(c4.is_police)
c4.show_speed()
c4.turn("в обратном направлении")
c4.go()
c4.stop()

'''____________________________________________________________________________
5. Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод 
выводит сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для 
каждого экземпляра.'''


class Stationery:
    title = None # в задании: определить атрибут класса, а не атрибут экземпляра

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Это ручка")


class Pencil(Stationery):
    def draw(self):
        print("Это карандаш")


class Handle(Stationery):
    def draw(self):
        print("Это маркер")


# экземпляр класса Stationery:
s0 = Stationery()
s0.draw()
# экземпляр класса Pen:
s1 = Pen()
s1.draw()
# экземпляр класса Pencil:
s2 = Pencil()
s2.draw()
# экземпляр класса Handle:
s3 = Handle()
s3.draw()

# бонус: вывод атрибута 'title' класса Stationery для каждого экземпляра:
print(s0.title, s1.title, s2.title, s3.title)
