# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0


from itertools import zip_longest

def delete_pow(string: str):
    string = string[:string.find('^')] + string[string.find('^')+2:]
    if '^' in string:
        return delete_pow(string)
    else: return string

def get_coefs_from_poly(string: str):
    string = string.replace('*x', '')
    string = string.replace(' ', '')
    return string.split('+')

with open('file_5_1.txt', 'r') as f:
    polynomial_1 = ''.join(f.readlines()).replace(' = 0', '')

with open('file_5_2.txt', 'r') as f:
    polynomial_2 = ''.join(f.readlines()).replace(' = 0', '')

k = len(polynomial_1.split(' + ')) - 1

arr = [f'*x^{i} + ' for i in range(k, 1, -1)]
arr.append('*x + ')

coef_1 = list(map(int, get_coefs_from_poly(delete_pow(polynomial_1))))
coef_2 = list(map(int, get_coefs_from_poly(delete_pow(polynomial_2))))
coef_3 = list(map(str, list(map(lambda x, y: x + y, coef_1, coef_2))))
result_arr = [list(i) for i in list(zip_longest(coef_3, arr, fillvalue=''))]

result = ''
for i in result_arr:
    result += ''.join(i)

with open('file_5_final.txt', 'w') as f:
    f.write(f'({polynomial_1}) + ({polynomial_2}) = {result}')