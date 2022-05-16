count_number = int(input('Введите количество чисел: '))
numb = []
for i in range(count_number):
   numb.append( int(input('Введите число: ')))
numb.sort()
print(numb)

