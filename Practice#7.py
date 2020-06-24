# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# preparations
import json
textFile = open('practice7.txt', 'r', encoding="UTF-8")
jsonFile = open('practice77.json', 'w', encoding="UTF-8")
finalList = []
companyProfit = {}
averageList = []
average = {}

# reading file and extracting every company's data to the dictionary: name = profit (income - expenses)
for line in textFile:
    companyProfit[line.split()[0]] = int(line.split()[2]) - int(line.split()[3])

# adding all companies' profits to the list (only if positive)
for i in companyProfit:
    if companyProfit[i] > 0:
        averageList.append(companyProfit[i])

# counting the average profit of the companies (only proffitable ones)
average["average_profit"] = sum(averageList) / len(averageList)

# getting companies' data and average profit to the final list
finalList.append(companyProfit)
finalList.append(average)

# dumping final list to the json file
json.dump(finalList, jsonFile)
textFile.close()
jsonFile.close()


# double-check
with open('practice77.json', 'r', encoding="UTF-8") as myFile:
    b = json.load(myFile)
    print(b)