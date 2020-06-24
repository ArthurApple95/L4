# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
with open("practice2.txt", "r", encoding="utf-8") as fileName:
    linesNum = 0
    for line in fileName:
        wordsNum = 0
        for word in line.split():
            wordsNum += 1
        linesNum += 1
        print(f"В строке номер {linesNum} есть {wordsNum} слов")
print(f'Общее количество строк в файле: {linesNum}')