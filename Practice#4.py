# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

# импорт переводчика
from googletrans import Translator

translator = Translator()

# список для перевода и других значений
english = []
dash = []
numbers = []

# открываем файлы для работы
newFile = open("practice4_new.txt", "w", encoding="utf-8")
oldFile = open("practice4.txt", "r", encoding="utf-8")

# достаём слова, которые необходимо перевести, добавляем в список для перевода
for line in oldFile:
    english.append(line.split()[0])
    dash.append(line.split()[1])
    numbers.append(line.split()[2])

# переводим
russian = translator.translate(english, dest='ru')

# записываем данные в новый файл
i = 0
while i < len(english):
    newFile.writelines([russian[i].text, " ", dash[i], " ", numbers[i], "\n"])
    i += 1

# закрываем файлы
newFile.close()
oldFile.close()

print("Перевод завершён")
