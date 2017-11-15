#Шифр Цезаря
word = input("Введите слово: ")
for i in word:
    if i != "я" and i != "z":
        print(chr(ord(i) + 1), end = "")
    elif i == "я":
        print("a", end = "")
    elif i == "z":
        print("a", end = "")
