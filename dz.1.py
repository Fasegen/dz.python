# Вычислить число c заданной точностью d
n = float(input())
d = float(input())
d = str(d)
d = d.split('.')
d = len(d[1])
print(round(n, d))

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random
n = int(input())
result = [0 for i in range(n)]
koef = random.sample(range(0, 100), n+1)
print(f'Коэф: {koef}')
for i in range(len(result)):
    result[i] = f'{koef[i]}x^{n}'
    n -= 1
result.append(str(koef[-1]))
print(f'{result}')
for elem in result:
    if '^1' in elem:
        result.remove(elem)
        result.insert(-1, elem[:elem.find('^1')])

print(result)

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input())
for i in range(2, n // 2 + 1):
    if n % i == 0:
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            print(i)


# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
x = [2, 5, 8, 8, 3, 0, 3, 2]
y = []
for i in x:
    count = 0
    for j in x:
        if i == j:
            count += 1
        if count == 2:
            break
    if count == 1:
        print(i)
