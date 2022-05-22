#exercise 1

a = 5
b = 10
print(a + b)

a = 10
b = 15
print(a * b)

name = input("What is your name: ")
age = input("How old are you: ")
print('What is your name: ', name, 'How old are you: ', age)

a = input('Name: ')
b = input('Age: ')
c = input('Birthplace: ')
print(f'Name: {a},Age: {b}, Birthplace: ,{c}')

a = input('Name: ')
b = int(input('Age: '))
if b >= 30:
    print("Welcome on board")
else:
    print('You are too young!')

#exercise 2

a = int(input("Напишите время в секундах: "))
b = a // 3600
c = (a - 3600 * b) // 60
d = (a - 3600 * b - 60 * c)
print("%02d:%02d:%02d" % (b, c, d))

#exercise 3
a = input('Введите число: ')
b = int(a)
c = int(a + a)
d = int (a + a + a)
print(b + c + d)

#exercise 4

a = int(input('Введите целое положительное число: '))
result = 0
while a > 0:
    b = a % 10
    if b > result:
        result = b
    a = a // 10
print(result)

#exercise 5

a = int(input('Выручка компании: '))
b = int(input('Издержки компании: '))
if a > b:
    print('Финансовый результат вашей компании: ', a - b)
    print('Рентабильность компании в %: ', (a - b) / a * 100)
    c = int(input('Численность вашей компании: '))
    print('Прибыль вашей компании на 1 человека: ', (a - b) / c)
else:
    print('Финансовый результат вашей компании: ', a - b)
    print('У вас убытки!')

#exercise 6

a = int(input('Сколько км вы пробежали в 1 день: '))
b = int(input("Цель пробежки в км: "))
day = 1
while a <= b:
     a = a * 1.1
     day += 1
print('Ваше цель достижима через: ', day, 'дней')







