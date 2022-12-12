# Тема урока: числовые типы данных
# 1. Целочисленный тип данных int
# 2. Числа с плавающей точкой float
# 3. Встроенные функции max(), min(), abs()
# 4. Решение задач

# Аннотация. Числовые типы данных. Вспомним особенности работы с целыми числами, научимся работать с числами
# с плавающей точкой. Изучим три встроенные функции для работы с числами max, min, abs.

# ----------------------------------------------------------------------------------------------------------

# Целочисленный тип данных

# Целые числа в Python представлены типом данных int (сокращение int происходит от слова integer). Для определения
# целого числа типа int используется последовательность цифр от 0 до 9.
#
# Явно указанное численное значение в коде программы называется целочисленным литералом. Когда Python встречает
# целочисленный литерал, он создает объект типа int, хранящий указанное значение.

n = 17  # целочисленный литерал
m = 7   # целочисленный литерал

# Целочисленный тип данных int используют не только потому, что он встречается в реальном мире, но и потому,
# что он естественным образом возникает при создании большинства программ.

# ----------------------------------------------------------------------------------------------------------

# Преобразование строки в целое число

# Для преобразования строки в целое число, мы используем команду int():

num = int(input()) # преобразование считанной строки в целое число

# Для преобразования строки в целое число необязательно использовать команду input().

# Следующий код преобразует строку 12345 в целое число:

n = int('12345')  # преобразование строки в целое число

# ----------------------------------------------------------------------------------------------------------

# Целочисленные операторы

# Язык Python предоставляет четыре основных арифметических оператора для работы с целыми числами
# (+, −, *, /), а также три дополнительных (% для остатка, // для целочисленного деления и ** для возведения в степень).
#
# Следующая программа демонстрирует все целочисленные операторы:

a = 13
b = 7

total = a + b
diff = a - b
prod = a * b
div1 = a / b
div2 = a // b
mod = a % b
exp = a ** b

print(a, '+', b, '=', total)
print(a, '-', b, '=', diff)
print(a, '*', b, '=', prod)
print(a, '/', b, '=', div1)
print(a, '//', b, '=', div2)
print(a, '%', b, '=', mod)
print(a, '**', b, '=', exp)

# ----------------------------------------------------------------------------------------------------------

# Длинная арифметика

# Отличительной особенностью языка Python является неограниченность целочисленного типа данных.
# По факту, размер числа зависит только от наличия свободной памяти на компьютере. Это отличает
# Python от таких языков как C++, C, C#, Java где переменные целого типа данных имеют ограничение. Например,
# в языке C# диапазон целых чисел ограничен от -2 ** 63 до 2 ** 63 - 1.

atom = 10 ** 80  # количество атомов во вселенной
print('Количество атомов =', atom)

# Результатом выполнения программы будет число с 81 цифрой:

# Количество атомов = 100000000000000000000000000000000000000000000000000000000000000000000000000000000

# ----------------------------------------------------------------------------------------------------------

# Символ разделитель

# Для удобного чтения чисел можно использовать символ подчеркивания:

num1 = 25_000_000
num2 = 25000000
print(num1)
print(num2)

# ----------------------------------------------------------------------------------------------------------

# Числа с плавающей точкой

# Наравне с целыми числами в Python есть возможность работы с дробными (вещественными) числами.
# 2/3, 2 ,π – являются вещественными и целого типа int недостаточно для их представления.
#
# Дробные (вещественные) числа в информатике называют числами с плавающей точкой.
#
# Для представления чисел с плавающей точкой в Python используется тип данных float.

e = 2.71828  # литерал с плавающей точкой
pi = 3.1415  # литерал с плавающей точкой

# ----------------------------------------------------------------------------------------------------------

# Арифметические операторы

# Язык Python предоставляет четыре основных арифметических оператора для работы с числами с плавающей
# точкой (+, −, *, /) и один дополнительный (** для возведения в степень).
#
# Следующая программа демонстрирует все целочисленные операторы:

a = 13.5
b = 2.0

total = a + b
diff = a - b
prod = a * b
div = a / b
exp = a ** b

print(a, '+', b, '=', total)
print(a, '-', b, '=', diff)
print(a, '*', b, '=', prod)
print(a, '/', b, '=', div)
print(a, '**', b, '=', exp)

# ----------------------------------------------------------------------------------------------------------

# Преобразование между int и float

# Неявное преобразование. Любое целое число (тип int) можно использовать там, где ожидается число с плавающей
# точкой (тип float), поскольку при необходимости Python автоматически преобразует целые числа в числа с
# плавающей точкой.
#
# Явное преобразование. Число с плавающей точкой нельзя неявно преобразовать в целое число. Для такого преобразования
# необходимо использовать явное преобразование с помощью команды int().

num1 = 17.89
num2 = -13.56
num3 = int(num1)
num4 = int(num2)
print(num3)
print(num4)

# Обратите внимание, что преобразование чисел с плавающей точкой в целое производится с округлением в сторону
# нуля, то есть int(1.7) = 1, int(-1.7) = -1.

# ----------------------------------------------------------------------------------------------------------

# Площадь треугольника

# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.

# Формат входных данных
# На вход программе подаётся два числа с плавающей точкой – длины катетов, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести одно число – площадь треугольника.

a = float(input())
b = float(input())
s = 1 / 2 * a * b
print(s)

# ----------------------------------------------------------------------------------------------------------

# Две старушки

# Две старушки идут навстречу друг другу с постоянными скоростями V1 и V2  км/ч. Определите, через какое
# время старушки встретятся, если расстояние между ними равно SS км.

# Формат входных данных
# На вход программе подаются три числа с плавающей точкой S,V1,V2, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести одно число в соответствии с условием задачи.

# Примечание. Это очень быстрые старушки.

s = float(input())
v1 = float(input())
v2 = float(input())
time = s / (v1 + v2)
print(time)

# ----------------------------------------------------------------------------------------------------------

# Обратное число

# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. Если при этом введённое
# с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).

# Формат входных данных
# На вход программе подается одно действительное число.
#
# Формат выходных данных
# Программа должна вывести действительное число обратное данному, либо текст в соответствии с условием задачи.

x = float(input())
if x == 0:
    print("Обратного числа не существует")
elif 1 / x:
    print(x ** -1)

# ----------------------------------------------------------------------------------------------------------

# 451 градус по Фаренгейту

# У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту».
# Напишите программу, которая определяет, какой температуре по шкале Цельсия соответствует указанное значение
# по шкале Фаренгейта.
#
# Используйте формулу для перевода:

# C = 5 / 9 (F - 32)

# Решение:

fahrenheit = float(input())
celsius = 5 / 9 * (fahrenheit - 32)
print(celsius)

# ----------------------------------------------------------------------------------------------------------

# Dog age

# На вход программе подается число nn – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в
# человеческих годах.
#
# Формат входных данных
# На вход программе подаётся натуральное число – количество собачьих лет.
#
# Формат выходных данных
# Программа должна вывести возраст собаки в человеческих годах.
#
# Примечание. В течение первых двух лет собачий год равен 10.510.5 человеческим годам. После этого каждый год собаки
# равен 4 человеческим годам.

dog_age = float(input())
if dog_age > 2:
    human_age = 21 + (dog_age - 2) * 4
    print(human_age)
else:
    print(dog_age * 10.5)

# ----------------------------------------------------------------------------------------------------------

