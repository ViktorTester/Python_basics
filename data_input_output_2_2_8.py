print('Как тебя зовут?')
name = input()
print('Привет,', name)

name = input('Как тебя зовут?')
print('Привет,', name)

print('Как тебя зовут?')
name = input()
print('Привет,', name)
name = 'Timur'
print('Привет,', name)
# Можно менять значения переменной

name1 = 'Тимур'
name2 = name1
print(name2)
# Можно присвоить имя другой переменной

name, surname = 'Timur', 'Guev'
print('Имя:', name, 'Фамилия:', surname)

name, surname = input(), input()
print('Имя:', name, 'Фамилия:', surname)
# Можно изменять значение сразу нескольких переменных

name1 = 'Timur'
name2 = 'Gvido'
name1, name2 = name2, name1
# Можно обменять значения переменных
