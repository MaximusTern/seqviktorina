number = input('Введи числа через разделитель: ')
separ = number[1]
print(separ)

num = number.split(separ)
print(num)
num_uniq = []

for i in num:
    if num.count(i) == 1:
        num_uniq.append(i)

print(num_uniq)