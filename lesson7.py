# exercise 1
class Matrix:
    def __init__(self, l1, l2):
        self.list1 = l1
        self.list2 = l2

    def __str__(self):
        print("Первая матрица")
        print(str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list1])))
        print("Вторая матрица")
        print(str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list2])))
# получается достаточно громоздко, но иначе не понимаю, как вывести обе матрицы через return

    def __add__(self):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.list1)):
            for j in range(len(self.list2[0])):
                result[i][j] = self.list1[i][j] + self.list2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in result]))


m1 = Matrix([[5, 8, 10], [-10, -5, -3], [13, 19, 22]], [[5, 2, 0], [10, 5, 3], [7, 1, -2]])
m1.__str__()
print("Сумма 2х матриц" '\n', m1.__add__())

# exercise 2
#2.1
class Clothes():
    def __init__(self, V, H):
        self.size = V
        self.height = H
    def exp(self):
        exp_all = (self.size / 6.5 + 0.5) + (2 * self.height + 0.3)
        print('Общий расход ткани = ', exp_all)

class Coat(Clothes):
    def exp(self):
        exp1 = self.size / 6.5 + 0.5
        print('Размер ткани на пальто = ', exp1)

class Suit(Clothes):
    def exp(self):
        exp2 = 2 * self.height + 0.3
        print('Размер ткани на костюм = ', exp2)

c = Coat (6.5, 5)
c.exp()
s = Suit(6.5, 5)
s.exp()
clothes = Clothes(6.5, 5)
clothes.exp()

#2.2
class Clothes():
    def __init__(self, V, H):
        self.size = V
        self.height = H

    @property
    def exp(self):
        return f'Общий расход ткани = {(self.size / 6.5 + 0.5) + (2 * self.height + 0.3)}'

class Coat(Clothes):
    def exp(self):
        return f'Размер ткани на пальто = {self.size / 6.5 + 0.5}'

class Suit(Clothes):
    def exp(self):
        return f'Размер ткани на костюм = {2 * self.height + 0.3}'

c = Coat (6.5, 5)
print(c.exp())
s = Suit(6.5, 5)
print(s.exp())
clothes = Clothes(6.5, 5)
print(clothes.exp)

# exercise 3
class Cell():
    def __init__(self, value):
        self.value = int(value)

    def __add__(self, other):
        return f'Сумма клеток = {self.value + other.value}'

    def __sub__(self, other):
        sub = self.value - other.value
        if sub > 0:
            return f'Разница количества ячеек = {sub}'
        else:
            return f'Операция невозможна. Разница количества ячеек меньше 0'

    def __mul__(self, other):
        return f'Произведение количества ячеек = {self.value * other.value}'

    def __truediv__(self, other):
        return f'Деление количества ячеек = {self.value // other.value}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.value / row)):
            result += f'{"*" * row}''\n'
        result += f'{"*" * (self.value % row)}'
        return result

cell1 = Cell(25)
cell2 = Cell(30)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(6))
print(cell2.make_order(15))