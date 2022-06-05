# exercise 1
# 1.1
try:
    n1 = int(input('Укажите число a: '))
    n2 = int(input('Укажите число b: '))
    res = n1 / n2
    print(res)
except ZeroDivisionError:
    print('Вы указали неверное значение! Деление на 0 недопустимо!')
except ValueError:
    print('Введите числовое значение!')

#  1.2
def my_first_func():
    try:
        n1 = int(input('Укажите число a: '))
        n2 = int(input('Укажите число b: '))
        print(n1 / n2)
    except ZeroDivisionError:
        print('Вы указали неверное значение! Деление на 0 недопустимо!')
    except (ValueError, NameError):
        print('Введите числовое значение!')
        return
my_first_func()

# exercise 2
def profile(**kwargs):
        return kwargs
a = dict(profile(Name = input('Name :'),
    Surname = input('Surname: '),
    YOB = input('Year of birth: '),
    City = input('City: '),
    Email = input('Email: '),
    Tel = input('Tel: ')
))
print("Profile: "+', '.join(a.values()))


# exercise 3
#3.1
def my_func(a, b, c):
    list = [a, b, c]
    list.sort()
    n1 = list[-1] + list[-2]
    print(n1)
my_func(30, 10, 15)

#3.2
def my_func(a, b, c):
    n1 = max(a, b)
    n2 = max(b, c)
    n3 = n1 + n2
    print(n3)
my_func(12, 15, 35)

# exercise 4
#4.1.1
def my_func1(x, y):
    if x >= 0:
        if y < 0:
            print(x ** y)
        else:
            print("Введите корректные значения!")
    else:
        print("Введите корректные значения!")
my_func1(x = float(input('Введите действительное положительное число: ')),
    y = int(input('Введите целое отрицательное число: '))
         )

#4.1.2
def my_func1():
    x = float(input('Введите действительное положительное число: '))
    y = int(input('Введите целое отрицательное число: '))
    if x >= 0:
        if y < 0:
            print(x ** y)
        else:
            print("Введите корректные значения!")
    else:
        print("Введите корректные значения!")
my_func1()

#4.2
def my_func1(x, y):
    res = 1
    for el in range(0, abs(y)):
        res *= x
    if x >= 0:
        if y < 0:
            return 1 / res
        else:
            print("Введите корректные значения!")
    else:
        print("Введите корректные значения!")

print(my_func1(x = float(input('Введите действительное положительное число: ')),
    y = int(input('Введите целое отрицательное число: '))
         ))

# exercise 5
def my_func2():
    n1 = 0
    while True:
        li = input('Введите несколько чисел: ').split()
        for el in li:
            try:
                if el == '#':
                    print(n1)
                    return
                else:
                    n1 += int(el)
            except ValueError:
                print('Введите числа!')
        print(n1)

my_func2()

# exercise 6 - 7
# 6-7.1
def my_func3():
        l1 = input("Введите текст латинскими буквами: ")
        print(l1.title())

my_func3()

# 6-7.2
def my_func3():
    l1 = input("Введите текст латинскими буквами: ").split()
    for el in l1:
        if ord(el[0]) < 97:
            print('Введите текст латинскими буквами в нижнем регистре!')
        else:
            n1 = chr(ord(el[0]) - 32) + el[1:]
            print(n1)

my_func3()

