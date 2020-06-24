# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

limit = randint(5, 15)
i = 0
numbers = []

with open("practice5.txt", "w", encoding="utf-8") as fileName:
    while i < limit:
        fileName.writelines([str(randint(1, 100)), " "])
        i += 1

with open("practice5.txt", "r", encoding="utf-8") as fileName:
    for line in fileName:
        for number in line.split():
            numbers.append(int(number))

print(sum(numbers))
