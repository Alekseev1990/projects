
import json

lst = []
lst_as_str = json.dumps(lst)
dictionary = {"word":"value"}

help = """
s - поиск слова по словарю
a - добавить новое слово
r - удалить слово
k - вывод всех ключей в словаре
d - вывод всего словаря
q - выход
"""

choice = ''
while choice != 'q':
    choice = input("'h' - справка >>  ")
    if choice == 's':
        word = input("Введите слово: ")
        word = word.lower()  # убрал зависимость вводимого регистра, можно вводить любой регистр1
        with open("dictionary.json", "r", encoding="utf-8") as file:
            res = json.load(file)
        if word in res:
            print(res[word])
        else:
            print("Нет такого слова")
    elif choice == 'a':
        word = input("Введите слово: ")
        value = input("Введите определение: ")
        with open("dictionary.json", "r", encoding="utf-8") as file:
            res = json.load(file)
            res[word] = value
        with open("dictionary.json", "w", encoding="utf-8") as file:
            res1 = json.dump(res, file, indent=2, ensure_ascii=False)
        print("Слово добавлено")
        break
    elif choice == 'r':
        word = input("Введите слово: ")
        with open("dictionary.json", "r", encoding="utf-8") as file:
            res = json.load(file)
        del res[word]
        with open('dictionary.json', 'w') as f:
            json.dump(res, f, indent = 2, ensure_ascii=False)
        print(f'Слово "{word}" удалено')
    elif choice == 'k':
        with open("dictionary.json", "r", encoding="utf-8") as file:
            res = json.load(file)
            sortedDict = sorted(res.items(), key=lambda x: x[0].lower()) #  вывод по алфавиту
            for key, value in sortedDict:
                print(key)
    elif choice == 'd':
        with open('dictionary.json', 'r', encoding='utf-8') as file:
            result = file.read()
        print(result)
    elif choice == 'h':
        print(help)
    elif choice == 'q':
        continue
    else:
        print(f'Нераспознанная команда. Введите команду из справки {help}')
