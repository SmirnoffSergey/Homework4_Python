# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001


import math

accuracy = input('Enter the accuracy of calculations in the range from 0.1 to 0.0000000001: ')
fractional_part_length = accuracy.find('1') - accuracy.find('.')
print()

print(f'Value of the number {math.pi} with accuracy up to {accuracy} is {round(math.pi, fractional_part_length)}')