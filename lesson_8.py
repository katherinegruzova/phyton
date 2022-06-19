# exercise 1
import re
class Data:
    def __init__(self, data):
        self.data = str(data)

    @classmethod
    def set_data(cls, obj):
        my_data = obj.data.split('-')
        result = list(map(int, my_data))
        # return f'Текущая дата: {result[0]}.{result[1]}.{result[2]}'
        return f'{result[0]},{result[1]},{result[2]}'

    @staticmethod
    def proof(day, month, year):
        if 31 >= day >= 1:
            if 12 >= month >= 1:
                if 2022 >= year > 0:
                    return f'Эта дата существует!'
                else:
                    return f'Год введен неверно. Введите реальные данные!'
            else:
                return f'Месяц введен неверно. Введите реальные данные!'
        else:
            return f'День введен неверно. Введите реальные данные!'

a = Data('10-10-2021')
print(Data.set_data(a))
b = Data.set_data(a)
day = int(re.findall(r'\d+',b)[0])
month = int(re.findall(r'\d+',b)[1])
year = int(re.findall(r'\d+',b)[2])
print(Data.proof(day, month, year))

#exercise 2
class Del(Exception):
    def __init__(self,txt):
        self.txt = txt
try:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    if num2 == 0:
        raise Del('Деление на 0 невозможно!')
except (ValueError,Del) as err:
    print(err)
else:
    print('Частное двух введенных чисел = ', num1 / num2)

# exercise 3
class Int(Exception):
    pass

my_list = []
while True:
    try:
        el = input('Введите число: ')
        if el == 'stop':
            break
        if not el.isdigit():
            raise Int(el)
    except Int:
        print('Вы ввели буквы. Введите числовое значение')
    else:
        my_list.append(int(el))
print(my_list)

#exercise 4-6
#Toys Production
class Production:
    def __init__(self, volume, defect, sales, price):
            self.volume = int(volume)
            self.defect = int(defect)
            self.sales = int(sales)
            self.price = int(price)
            self.revenue = {'sales': sales, 'price': price}
    def to_produce(self):
        return f'Произведено {self.volume} ед. товара. Из них:' # не получилось однократно добавить фразу "Из них" в строку с выводом цвета - текстовый блок повторяется. ПОэтому добавила сюда
    def to_sent(self):
        warehouse = int(self.volume * ((100 - self.defect) / 100))
        self.warehouse = warehouse
        return f'\nПоставлено на склад {self.warehouse} ед. товара'
    def to_sale(self):
            if self.sales > self.warehouse:
                return f'С учетом складских остатков продано {self.sales} ед. товара'
            else:
                return f'Складких остатков нет. Продано {self.sales} ед. товара'
    def get_revenue(self):
        result = 1
        for el in self.revenue:
            result = result * self.revenue[el]
            self.result = result
        return f'Выручка с продаж {self.sales} ед. товара составила {self.result} рублей'
    def stock_balance(self):
        if self.warehouse < self.sales:
            return f'Необходим пересчет складких остатков. Планируется инвентаризация'
        else:
            return f'На складе остаток в количестве {self.warehouse - self.sales} ед. товара'

class Toys_for_newborn(Production):
    @classmethod
    def get_classname(cls):
        return f'Данные по категории - {cls.__name__}:'
    def colour(self):
        colours = ['голубой', 'розовый', 'желтый']
        quantity = list(map(int,[self.volume * 0.4, self.volume * 0.4, self.volume * 0.2]))
        info = dict(zip(colours, quantity))
        for key, value in info.items():
            print(key, "-", value, 'ед. продукции'';', end=' ')

class Toys_for_kids1_3(Production):
    @classmethod
    def get_classname(cls):
        return f'\nДанные по категории - {cls.__name__}:'
    def colour(self):
        colours = ['желтый', 'красный', 'синий']
        quantity = list(map(int,[self.volume * 0.3, self.volume * 0.35, self.volume * 0.35]))
        info = dict(zip(colours, quantity))
        for key, value in info.items():
            print(key, "-", value, 'ед. продукции'';', end=' ')

class Toys_for_kids3_8(Production):
    @classmethod
    def get_classname(cls):
        return f'\nДанные по категории - {cls.__name__}:'
    def colour(self):
        colours = ['зеленый', 'желтый', 'красный', 'синий']
        quantity = list(map(int,[self.volume * 0.25, self.volume * 0.25, self.volume * 0.25, self.volume * 0.25]))
        info = dict(zip(colours, quantity))
        for key, value in info.items():
            print(key, "-", value, 'ед. продукции'';', end=' ')
    def info(self):
        while True:
            try:
                info = int(input(('Введите количество sku в категории: ')))
            except ValueError:
                print('Данные введены неверно!')
            else:
                print('Средняя цена 1 sku = ', self.result / info)
                break

newborn = Toys_for_newborn(2350, 2.5, 2150, 30)
print(newborn.get_classname())
print(newborn.to_produce())
newborn.colour()
print(newborn.to_sent())
print(newborn.to_sale())
print(newborn.get_revenue())
print(newborn.stock_balance())

kids1_3 = Toys_for_kids1_3(2350, 2.5, 1500, 30)
print(kids1_3.get_classname())
print(kids1_3.to_produce())
kids1_3.colour()
print(kids1_3.to_sent())
print(kids1_3.to_sale())
print(kids1_3.get_revenue())
print(kids1_3.stock_balance())

kids3_8 = Toys_for_kids3_8(2350, 2.5, 1500, 30)
print(kids3_8.get_classname())
print(kids3_8.to_produce())
kids3_8.colour()
print(kids3_8.to_sent())
print(kids3_8.to_sale())
print(kids3_8.get_revenue())
print(kids3_8.stock_balance())
kids3_8.info()

#exercise 7
class Complex_number():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма комплексных чисел равна: {(self.a + other.a)} + {(self.b + other.b)} * i'

    def __mul__(self, other):
        return f'Умножение комплексных чисел равно: {(self.a * other.a - self.b * other.b)} + {(self.a * other.b + self.b * other.a)} * i '

complex1 = Complex_number(1, -3)
complex2 = Complex_number(2, -5)
print(complex1 + complex2)
print(complex1 * complex2)