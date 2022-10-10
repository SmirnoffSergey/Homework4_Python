# Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.


n = int(input('Enter the integer number N = '))
num = n
divisor = 2
list_of_divisors = []

while num > 1:
   while num % divisor == 0:
      list_of_divisors.append(divisor)
      num //= divisor
   divisor +=1
print()

print(f'The simple divisors of number {n} are: {list_of_divisors}')