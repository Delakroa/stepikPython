# ���� �����: ������ math

# 1.������ math
# 2.������� �����

# ���������. ���� �������� ������ math, ������� �������� �������������� ������� �� ������ � ������������� �������.

# ������

# ��� ��� ����������, ����� �� ����������� ����� Python �������� ��������� ������������� �������, ������� ��� �����������
# � ������ � �������������. ����� ������� ��������� � ������. � Python ������� ���������� ���������� �������, �������
# ����� ���������� � ����� ����������

# ������ math

# ������ math � ���� �� ������������ � Python. ���� ������ ������������� �������� ���������� ��� ���������� ����������
# � ������������� ������� (������� � ��������� ������).

# ��� ������������� ���� ������� � ������ ��������� ���������� ���������� ������, ��� �������� �������� import:

import math

# ����������� ���

# ����� ����������� ������ �� ����� ������������ ��� �������. ����� �� �����:

# ��������� \sqrt2 (������ ���������� �� ����);
# ��������� ����� 3.83.8 �� ���������� ������ ����� ����� � ����

# ��������������� ����������� ���, �������� ������ �������� ���:

import math

num1 = math.sqrt(2)     # ���������� ����� ����������� �� ����
num2 = math.ceil(3.8)   # ���������� ����� �����
num3 = math.floor(3.8)  # ���������� ����� ����

print(num1)
print(num2)
print(num3)

# � �������:
#
# 1.4142135623730951
# 4
# 3

# ---------------------------------------------------------------------------------------------------------------

# ����������� ����������� �������

# ��� ����� �������� �� ������� ����, ��� ������ ������� �� ��������� ��������� �������� ������ � ������ �����.
# � ������ �������, ���� ������� ������������ ���������� �����, �� ����� ����� (���������� �������� �������� ������
# � ������� �����) ����� ��������� ��������� � ������� � ����� �����������. ��� ����, ����� �� ��������� ��������
# ������ � ������ ����� ��� ������ �������, �� ����� ��������� ���:

from math import *

num1 = sqrt(2)     # ���������� ����� ����������� �� ����
num2 = ceil(3.8)   # ���������� ����� �����
num3 = floor(3.8)  # ���������� ����� ����

print(num1)
print(num2)
print(num3)

# ����� �������, ����������� ������ ��������� �������:

from math import *

# ��������� �� ������ �������� ������ � ������ �����. ��� ����� ������� �����������, ������������� ���������
# ��� ������� ������ math.

# ���� ����� ������������ ������ ��������� ������� ������, �� �� ����� ������������� ������ �� ��������� �������:

from math import sqrt, ceil

# ������ �� ����� �������� ������� sqrt() � ceil() ��� �������� math., ������ �� �� ����� ������� �������
# floor(), ��� ��� ��� �� ����������:

from math import sqrt, ceil

print(sqrt(25))
print(ceil(34.7))

print(floor(12.8))  # �������� � ������, ��� ��� ������� floor �� ����������

# ---------------------------------------------------------------------------------------------------------------

# ������ ������� ������ math

# ������ �������� ����� ������������ ������� ������ math:
#
#
# ����������
# int()	��������� ����� � ������� ����
# round(x)	��������� ����� x �� ���������� ������. ���� ������� ����� ����� ����� 0.5, �� ����� �����������
# �� ���������� ������� �����
#
# round(x, n)	��������� ����� x �� n ������ ����� �����
# floor(x)	��������� ����� x ���� (����)
# ceil(x)	��������� ����� x ����� (��������)
# abs(x)	������ ����� x (���������� ��������)

# �����, ���������, ������� � ���������
# sqrt(x)	���������� ������ ����� x
# pow(x, n)	���������� ����� x � ������� n
# log(x)	����������� �������� ����� x. ��������� ������������ ��������� ����� ����� e
# log10(x)	���������� �������� ����� x. ��������� ����������� ��������� ����� ����� 10
# log(x, b)	�������� ����� x �� ��������� b
# factorial(n)	��������� ������������ ����� n

# �������������
# degrees(x)	����������� ���� x, �������� � ��������, � �������
# radians(x)	����������� ���� x, �������� � ��������, � �������
# cos(x)	������� ���� x, ����������� � ��������
# sin(x)	����� ���� x, ����������� � ��������
# tan(x)	������� ���� x, ����������� � ��������
# acos(x)	���������� ���� � �������� �� 00 �� \pi?, cos �������� ����� x
# asin(x)	���������� ���� � �������� �� - \frac{\pi}{2}?2
# atan2(y, x)	�������� ���� (� ��������) ����� � ������������ (x, y)

# !!!��� ���������� ����������� ����� ����� ��������������� ����� n ** 0.5, ������ math.sqrt(n)!!!

# ---------------------------------------------------------------------------------------------------------------

