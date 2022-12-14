# Тема урока: логические операторы

# Логическое умножение and
# Логическое сложение or
# Логическое отрицание not
# Решение задач
# Аннотация. Изучим способ работы логических операторов в Python и приоритетность их выполнения.
#
# Логические операторы
# Как быть в ситуации, когда у нас есть несколько условий? В Python есть три логических оператора, которые позволяют
# создавать сложные условия:
#
# and — логическое умножение;
# or — логическое сложение;
# not — логическое отрицание.
# Оператор and
# Предположим, мы написали программу для учеников от двенадцати лет, которые учатся по крайней мере в 7 классе.
# Доступ к ней тем, кто младше, надо запретить. Следующий код решает поставленную задачу:

age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
if age >= 12 and grade >= 7:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

# --------------------------------------------------------------------------------------------------------------

# Мы объединили два условия при помощи оператора and. Оно означает, что в этом ветвлении блок кода выполняется только
# при выполнении обоих условий одновременно!

# Оператор and может объединять произвольное количество условий:

age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and city == 'Москва':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

# --------------------------------------------------------------------------------------------------------------

# Это таблица истинности для оператора and. В ней перечислены выражения, соединённые оператором and, показаны все
# возможные комбинации истинности и ложности и приведены результирующие значения выражений.
#
#   a     b     a and b
# False	False	False
# False	True	False
# True	False	False
# True	True	True

# Как показывает таблица, чтобы значение выражения с оператором and было истинным, должны быть истинными
# оба (все) объединенные им условия.

# --------------------------------------------------------------------------------------------------------------

# Оператор or
# Оператор or также применяется для объединения условий. Однако, в отличие от and, для выполнения блока кода достаточно
# выполнения хотя бы одного из условий.
#
# city = input('В каком городе вы живете?: ')
# if city == 'Москва' or city == 'Санкт-Петербург' or city == 'Екатеринбург':
#     print('Доступ разрешен.')
# else:
#     print('Доступ запрещен.')
# Доступ будет разрешен в случае, если хотя бы одно из условий выполнится.
#
# Это таблица истинности для оператора or. В ней перечислены выражения, соединённые оператором or, показаны все
# возможные комбинации истинности и ложности и приведены результирующие значения выражений.

#    a    b     a or b
# False	False	False
# False	True	True
# True	False	True
# True	True	True
# Для того, чтобы выражение or было истинным, требуется, чтобы хотя бы одно условие оператора or было истинным.
# При этом не имеет значения, истинным или ложным является второе выражение.
#
# Логическое выражение X and Y истинно, если оба значения X и Y истинны.
#
# Логическое выражение X or Y истинно, если хотя бы одно из значений X и Y истинно.
#
# Мы можем использовать оба логических оператора одновременно:
#
# age = int(input('Сколько вам лет?: '))
# grade = int(input('В каком классе вы учитесь?: '))
# city = input('В каком городе вы живете?: ')
# if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'):
#     print('Доступ разрешен.')
# else:
#     print('Доступ запрещен.')
# Такой код проверяет, что возраст учеников от двенадцати лет и учатся они по крайней мере в 7 классе и живут в Москве
# или Санкт-Петербурге.

# --------------------------------------------------------------------------------------------------------------

# Оператор not
# Оператор not позволяет инвертировать (т.е. заменить на противоположный) результат логического выражения. Например,
# следующий код:
#
# age = int(input('Сколько вам лет?: '))
# if not (age < 12):
#     print('Доступ разрешен.')
# else:
#     print('Доступ запрещен.')
# полностью эквивалентен коду:
#
# age = int(input('Сколько вам лет?: '))
# if age >= 12:
#     print('Доступ разрешен.')
# else:
#     print('Доступ запрещен.')
# В первом примере мы поместили выражение age < 12 в скобки для того, чтобы было чётко видно, что мы применяем оператор
# not к значению выражения age < 12, а не только к переменной age.
#
# Таблица истинности для оператора not:

# a      not a
# False	True
# True	False

# --------------------------------------------------------------------------------------------------------------

# Приоритеты логических операторов
# Логические операторы, подобно арифметическим операторам (+, -, *, /), имеют приоритет выполнения.
# Приоритет выполнения следующий:
#
# в первую очередь выполняется логическое отрицание not;
# далее выполняется логическое умножение and;
# далее выполняется логическое сложение or.
# Для явного указания порядка выполнения условных операторов используют скобки.
#
# Примечания
# Примечание 1. Частой ошибкой у начинающих программистов является путаница логических операторов and и or.
# Рассмотрим два условия:

# if x > 1 and x < 100:
# if x > 1 or x < 100:

# Верным является только первое условие. В нём проверяется, что число xx находится в диапазоне от 1 до 100, другими
# словами, x \in (1; \, 100)x∈(1;100). Второе условие проверяет, что число xx или больше 1, или меньше 100. Однако
# такому условию удовлетворяет любое число!
#
# Примечание 2. Другую частую ошибку видим в следующем примере кода:

# if age >= 7 and <= 9:

# Запуск такого кода приведет к появлению ошибки во время выполнения программы. Необходимо явно записывать условия:

# if age >= 7 and age <= 9:

# Примечание 3. Не забывайте, что в Python есть удобный способ для проверки принадлежности диапазону. Например,
# следующий код:

# if age >= 7 and age <= 9:

# полностью эквивалентен коду:

# if 7 <= age <= 9:

# Последний код предпочтительнее.
#
# Примечание 4. Оба оператора, and и or, вычисляются по укороченной схеме.
#
# Вот как это работает с оператором and. Если условие слева от оператора and является ложным, то условие справа от него
# не проверяется, так как результат выражения будет гарантированно ложным и проверка оставшегося условия — пустая трата
# процессорного времени.
#
# Аналогично работает оператор or. Если условие слева от оператора or истинное, то условие справа от него не
# проверяется. Действительно, результат будет гарантированно истинным и проверка оставшегося условия станет пустой
# тратой процессорного времени.

# --------------------------------------------------------------------------------------------------------------

# Решение задач
# Задача 1. Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным.
#
# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

num = int(input())
if 100 <= num <= 999:  # num >= 100 and num <= 999
    print('Число является трёхзначным')
else:
    print('Число не является трёхзначным')

# Задача 2. Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.
#
# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

num = int(input())
d3 = num % 10
d2 = num % 100 // 10
d1 = num // 100
if d3 != d2 and d3 != d1 and d2 != d1:
    print('Цифры различны')
else:
    print('Цифры не различны')

# Задача 3. Напишите программу, которая по координатам точки, не лежащей на осях координат, определяет номер
# координатной четверти, в которой она находится.
#
# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')

# --------------------------------------------------------------------------------------------------------------

# Принадлежность 1

# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанному промежутку.
#
# Формат входных данных
# На вход программе подаётся целое число xx.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

x = int(input())
if x > -1 and x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

# --------------------------------------------------------------------------------------------------------------

# Принадлежность 2

# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанным промежуткам.
#
# Формат входных данных
# На вход программе подаётся целое число xx.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

x = int(input())
if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

# --------------------------------------------------------------------------------------------------------------

# Принадлежность 3
#
# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанным промежуткам.
#
# Формат входных данных
# На вход программе подаётся целое число xx.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

# --------------------------------------------------------------------------------------------------------------

# Красивое число.
# Назовем число красивым, если оно является четырехзначным и делится нацело на 77 или на 1717. Напишите программу,
# определяющую, является ли введённое число красивым. Программа должна вывести «YES», если число является красивым,
# или «NO» в противном случае.
#
# Формат входных данных
# На вход программе подаётся натуральное число.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

x = int(input())
if (x % 7 == 0 or x % 17 == 0) and 1000 <= x <= 9999:
    print('YES')
else:
    print('NO')

# --------------------------------------------------------------------------------------------------------------

# Неравенство треугольника.
# Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный
# треугольник с такими сторонами.
#
# Формат входных данных
# На вход программе подаётся три положительных целых числа.
#
# Формат выходных данных
# Программа должна вывести «YES» или «NO» в соответствии с условием задачи.
#
# Примечание. Треугольник существует, если выполняется неравенство треугольника.

a, b, c = int(input()), int(input()), int(input())
if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')

# --------------------------------------------------------------------------------------------------------------

# Високосный год.
# Напишите программу, которая определяет, является ли год с данным номером високосным. Если год является високосным,
# то выведите «YES», иначе выведите «NO».
#
# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
#
# Формат входных данных
# На вход программе подаётся натуральное число.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

year = int(input())
if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')

# --------------------------------------------------------------------------------------------------------------

# Ход ладьи.

# Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли ладья попасть с первой
# клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и
# номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой
# клетки ходом ладьи можно попасть во вторую, или «NO» в противном случае.
#
# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Шахматная ладья ходит по горизонтали или вертикали.

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a1 == a2 or b1 == b2:
    print('YES')
else:
    print('NO')

# --------------------------------------------------------------------------------------------------------------

# Ход короля.

# Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли король попасть с
# первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающий номер столбца
#  и номер строки сначала для первой клетки, потом два для второй клетки. Программа должна вывести "YES", если из первой
# клетки  ходом короля может попасть во вторую, или "NO" в противном случае.

# Формат входных данных.
# На вход программы подаётся четыре числа от 1 до 8

# Формат выходных данных.
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание.
# Шахматный король ходит по горизонтали, вертикали и диагонали, но только на одну клетку.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
x = x2 - x1
y = y2 - y1
if -1 <= x <= 1 and -1 <= y <= 1:
    print("YES")
else:
    print("NO")

# --------------------------------------------------------------------------------------------------------------
