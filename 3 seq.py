number1 = input('Введи числа через разделитель для списка 1: ')
separ = number1[1]

num1 = number1.split(separ)
print(num1)

number2 = input('Введи числа через разделитель для списка 2: ')
separ = number2[1]

num2 = number2.split(separ)
print(num2)

print('Результат')
for n1 in num1[:]:
    if n1 in num2:
        num1.remove(n1)
print(num1)
