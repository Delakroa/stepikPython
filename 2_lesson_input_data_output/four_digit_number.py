"""2.5 Четырёхзначное число

Напишите программу для нахождения цифр четырёхзначного числа.

Формат входных данных
На вход программе подаётся положительное четырёхзначное целое число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

"""

number = int(input())
a = number // 1000
b = (number // 100) % 10
c = (number // 10) % 10
d = number % 10

print(f'Цифра в позиции тысяч равна {a}')
print(f'Цифра в позиции сотен равна {b}')
print(f'Цифра в позиции десятков равна {c}')
print(f'Цифра в позиции единиц равна {d}')