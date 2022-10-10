# Задайте последовательность цифр. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


from random import randint

n = int(input('Enter the quantity of numbers in list: '))
list = []
for i in range(n):
    list.append(randint(-5, 5))
print(list)
print()

list_result = []
for i in range(len(list)):
    count = 0
    for j in range(len(list)):
        if list[i] == list[j]:
            count += 1
    if count == 1:
        list_result.append(list[i])
print(list_result)