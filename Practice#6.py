# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.

fileName = open("practice6.txt", "r", encoding="utf-8")
my_dict = {}
numbersList = []
for line in fileName:
    for word in line.split():
        for number in word.split('('):
            try:
                numbersList.append(int(number))
            except ValueError:
                pass
    my_dict[line.split()[0]] = sum(numbersList)
    numbersList.clear()
print(my_dict)

