# exercise 1
from sys import argv
# # a1  = per hour output
# # a2 = rate per hour
# # a3 = bonus

def salary():
    path, a1, a2, a3 = argv
    a1, a2, a3 = map(int, argv[1:])
    print((a1 * a2) + a3)
salary()

# exercise 2
l1 = [50, 30, 35, 16, 2, 15, 19, 10, 13, 28, 55, 14, 300]
l2 = [l1[el] for el in range(1, len(l1)) if l1[el] > l1[el-1]]
print(l2)

# exercise 3

l1 = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(l1)

# exercise 4
# 4.1 если оставить по 1 элементу из повторяющихся в списке
l1 = [1, 30, 1, 30, 30, 15, 17, 19, 22, 25, 55, 22, 13, 16, 15]
l2 = []
[l2.append(el) for el in l1 if el not in l2]
print(l2)

# 4.2
l1 = [1, 30, 1, 30, 30, 15, 17, 19, 22, 25, 55, 22, 13, 16, 15]
l2 = [el for el in l1 if l1.count(el) > 1]
l3 = [el for el in l1 if el not in l2]
print(l3)

# exercise 5
from functools import reduce

l1 = [el for el in range(100, 1001) if el % 2 ==0]
res = reduce(lambda x, y: x * y, l1)
print(res)

# exercise 6
#6.1
from itertools import count
for el in count(15, 1):
    print(el)
    if el > 50:
        break


#6.2
from itertools import cycle
l1 = ['Ann', 'Helen', 'Max', 'Gwen', 545, 'apple']
i = 0
for el in cycle(l1):
    print(el)
    i += 1
    if i > 23: # по 4 повторения элементов списка
        break

# exercise 7
from math import factorial

def my_gen(n):
    for el in range(n):
        print(el, end='! = ')
        yield factorial(el)
n = 4
for el in my_gen(n):
    print(el)
