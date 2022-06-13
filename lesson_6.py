# exercise 1
#1.1
import time
class TrafficLight:
    def running(self):
        self.__colour = ['красный', 'желтый', 'зеленый']
        print(self.__colour[0])
        time.sleep(7)
        print(self.__colour[1])
        time.sleep(2)
        print(self.__colour[2])
        time.sleep(5)

light = TrafficLight()
light.running()

#1.2
import time
class TrafficLight:
    __colour = ['красный', 'желтый', 'зеленый']
    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__colour[i])
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(2)
            elif i == 2:
                time.sleep(5)
            i += 1

light = TrafficLight()
light.running()

#exercise2
class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
        self._weight = 25
        self._thickness = 5

    def calc(self):
        self._b = (self._lenght * self._width * self._weight * self._thickness) // 1000
        print(f'Масса асфальта = ', self._b, 'т')

road = Road(20, 5000)
road.calc()

#exercise 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        self.full_name = self.name + " " + self.surname
        return self.full_name

    def get_total_income(self):
        self.total_income = sum(self._income.values())
        return self.total_income

pos1 = Position('Ann', 'Stone', 'Manager', 20000, 5000)
print(f'Full name: ', pos1.get_full_name())
print(f'Total salary: ', pos1.get_total_income())

pos2 = Position('John', 'Smith', 'Manager', 30000, 10000)
print(f'Full name: ', pos2.get_full_name())
print(f'Total salary: ', pos2.get_total_income())

#exercise 4
class Car:
    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начала движение'

    def stop(self):
        return f'{self.name} остановилась перед перекрестком'

    def turn(self):
        return f'{self.name} повернула направо'

    def show_speed(self):
        return f'Скорость движения {self.name} - {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Вы привысили скорость движения. Ваша скорость - {self.speed}. Максимально допустимая - 60'
        else:
            return super().show_speed()

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Вы привысили скорость движения. Ваша скорость - {self.speed}. Максимально допустимая - 40'
        else:
            return super().show_speed()
class PoliceCar(Car):
    pass

town1 = TownCar(70, 'white', 'Audi', False)
print(town1.go())
print(town1.stop())
print(town1.turn())
print(town1.show_speed())

sport1 = SportCar(100, 'green', 'Lamb', False)
print(sport1.go())
print(sport1.stop())
print(sport1.turn())
print(sport1.show_speed())

work1 = WorkCar(45, 'black', 'Subaru', False)
print(work1.go())
print(work1.stop())
print(work1.turn())
print(work1.show_speed())

police1 = PoliceCar(60, 'blue', 'Ford', True)
print(police1.go())
print(police1.stop())
print(police1.turn())
print(police1.show_speed())

#exercise 5
class Stationery:
    title = 'Принадлежность'
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('Используйте ручку для внесения комментариев в задание')

class Pencil(Stationery):
    def draw(self):
        return 'Используйте карандаш для подготовки чертежа'

class Handle(Stationery):
    def draw(self):
        return 'Маркером выделите необходимые области для продолжения работы красками'

pen1 = Pen()
# print(pen1.title)
pen1.draw()
pencil1 = Pencil()
# print(pencil1.title)
print(pencil1.draw())
handle1 = Handle()
# print(handle1.title)
print(handle1.draw())
