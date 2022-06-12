# exercise 1
f = open('venv\exercise1.txt', 'w+', encoding = 'utf-8')
while True:
    a = input('Введите данные: ')
    if a == '':
        break
    f.write(a+'\n')

f.close()

# exercise 2
lines = 0
words = 0
with open('venv\exercise2.txt', 'r+', encoding = 'utf-8') as f:
     for line in f:
        words1 = line.split()
        lines += 1
        words = len(words1)
        print("В", lines, 'строке', words, 'слов/а')

#exercise 3
d = {}
count = 0
with open('venv\exercise3.txt', 'r+', encoding = 'utf-8') as f:
    for line in f:
        key, value = line.split()
        d[key] = value
        if int(value) < 20000:
            print(f'{key}: зарплата меньше 20000')
    result = [int(item) for item in d.values()]
    for el in result:
        count += el
    print('Средний оклад сотрудников составляет: ', count / len(result))


#exercise 4
dict1 = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('venv\exercise4.txt', 'r+', encoding = 'utf-8') as f, open('venv\exercise4.1.txt', 'w+', encoding = 'utf-8') as g:
    for line in f:
        for key, value in dict1.items():
            line = line.replace(key, value)
        g.write(line)

#exercise 5
with open('venv\exercise5.txt', 'w+', encoding = 'utf-8') as f:
    f.write('5 55 100 200 300')
with open('venv\exercise5.txt', 'r+', encoding='utf-8') as f:
    for line in f:
        numbers = line.split(" ")
        numbers = list(map(int, numbers))
        print(sum(numbers))

#exercise 6
import re
with open ('venv\exercise6.txt', 'r+',encoding = 'utf-8') as f:
    for line in f:
        a = re.findall('[0-9]+', line)
        a = sum(list(map(int, a)))
        aa = str(a)
        b = re.findall('[а-яА-ЯёЁ]{4,}', line)
        for el in b:
            bb = el
        keys = bb.split()
        values = aa.split()
        dictionary = dict(zip(keys, values))
        print(dictionary)

#exercise 7
import json
a = {}
fin = []
with open('venv\exercise7.txt', 'r+', encoding = 'utf-8') as f:
    for line in f:
        firm, property, revenue, costs = line.split()
        a[firm] = int(revenue) - int(costs)
    if a.setdefault(firm) >= 0:
        val = sum(a.values())
        av_prof = val / len(a)
        d = {'average_profit': av_prof}
        fin.append(a)
        fin.append(d)
        print(fin)

    else:
        for i in a.values():
            if i < 0:
                filt = dict(filter(lambda x: x[1] is not i, a.items()))
                val1 = sum(filt.values())
                av_prof1 = val1 / len(filt)
                d1 = {'average_profit': av_prof1}
                fin.append(filt)
                fin.append(d1)
                print(fin)
with open ('data.json', 'w') as file:
    json.dump(fin, file)
    js_data = json.dumps(fin)
    print(js_data)