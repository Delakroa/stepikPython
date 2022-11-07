"""Трехзначное число.
Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.

Формат входных данных
На вход программе подаётся положительное трёхзначное число.

Формат выходных данных
Программа должна вывести два числа с поясняющим текстом: сумма цифр и произведение цифр."""

# Разложили 123 на три числа:

# 123 // 10 = 12
# 12 // 10 = 1
# 12 % 10 = 2
# 123 % 10 = 3

# 1 + 2 + 3 = 6
# 1 * 2 * 3 = 6

number = int(input())
data_num = number // 10
one_num = data_num // 10
two_num = data_num % 10
three_num = number % 10
data_sum = (one_num + two_num) + three_num
data_pro = (one_num * two_num) * three_num
print(f"Первая цифра = {one_num}")
print(f"Вторая цифра = {two_num}")
print(f"Третяя цифра = {three_num}")
print(f"Сумма цифр = {data_sum}")
print(f"Произведение цифр = {data_pro}")
