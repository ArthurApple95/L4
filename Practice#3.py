# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.
my_dict = {}
listNames = []
listSalaries = []
with open("practice3.txt", "r", encoding="utf-8") as fileName:
    for line in fileName:
        my_dict[line.split()[0]] = line.split()[1]
for i in my_dict:
    listSalaries.append(float(my_dict[i]))
    if float(my_dict[i]) < 20000:
        listNames.append(i)
print(f'Средняя величина дохода сотрудников составляет: {sum(listSalaries) / len(listSalaries)}')
print(f'Список сотрудников, чья зарплата ниже 20000: {listNames}')
