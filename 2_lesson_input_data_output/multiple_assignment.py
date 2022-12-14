# Множественное присваивание
# В языке Python можно за одну инструкцию присваивания изменять значение сразу нескольких переменных. Делается это так:

name, surname = 'Timur', 'Guev'
print(f'Имя: {name}, Фамилия: {surname}')

# Этот код можно записать и так

name = 'Timur'
surname = 'Guev'
print(f'Имя: {name}, Фамилия: {surname}')


# Отличие двух способов состоит в том, что множественное присваивание в первом способе присваивает значение двум
# переменным одновременно.
# Если требуется считать текст с клавиатуры и присвоить его в качестве значения переменным, то можно написать так:


name, surname = input('Введите имя: '), input('Введите фамилию: ')
print(f'Имя: {name}, Фамилия: {surname}')

# ------------------------------------------------------------------------------------------------------------

# В данном примере в одну переменную можно положить большое значение и получить список
name_surname = map(str, input('Введите имя и фамилию через пробел: ').split())
print(list(name_surname))
print(type(list(name_surname)))
