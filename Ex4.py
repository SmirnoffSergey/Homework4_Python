# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего
# на 1 меньше и так до ноля.
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто
# пропускаем данную итерацию степени.

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0


import random

k = int(input('Enter the degree of the polynomial in list, k = '))
coef_number = [random.randint(-100, 100) for i in range(k+1)]

print(coef_number)
print()

if k != 1:
    polynomial = str(coef_number[0])+'x^' + str(k) + ' '
    count = k - 1
    while count > 1:
        if coef_number[k - count] != 0:
            polynomial += '+ ' + \
                str(coef_number[k - count]) + \
                'x^' + str(count) + ' '
        count -= 1
    if count == 1:
        polynomial += '+ ' + \
            str(coef_number[k - count]) + 'x + ' + \
            str(coef_number[k - count + 1]) + ' = 0'
elif k == 1:
        polynomial = str(coef_number[0]) + \
            'x + ' + str(coef_number[1]) + ' = 0'
print(polynomial)

with open('file_4.txt', 'w') as f:
    f.write(polynomial)