num = int(input())
last_digit = num % 10  # последняя цифра числа
first_digit = num // 10  # первая цифра числа

if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')
# Программа,определяющая, состоит ли двузначное число, введенное с клавиатуры, из одинаковых цифр.

num1, num2, num3 = int(input()), int(input()), int(input())
counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
print(counter)
# Программа, которая считывает три числа и подсчитывает количество чётных чисел.

age = int(input())
if 17 <= age <= 18:
    print('Вы ребёнок')
# Программа проверяет возраст