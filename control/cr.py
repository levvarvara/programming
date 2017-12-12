#вариант 2, Левченко Варвара, группа 3
with open("slov.txt", encoding="UTF-8") as f:
    lines=f.readlines()
text_el = []
list_20 = []
for n in lines:
    n = n.strip()
    el = n.split("|")
    text_el.append(el)


for n in text_el:
    if len(n[0]) >= 20:
        list_20.append(n)
print("В слове по крайне мере 20 символов:")
print()
for n in list_20:
    print(n)


counter = 0
for n in text_el:
    if n[2] != "":
        counter +=1
print()
print("Количество словарных статей с антонимами: ", counter)
print()

print()
list_user = []
user = input("Введите слово: ")
while user!="":
    list_user.append(user)
    user = input("Введите слово: ")
defen = ""
examp = ""
flag = False
for m in list_user:
    for n in text_el:
        if n[0] == m:
            word = n[0]
            defen = ''.join(n[1])
            examp = ''.join(n[3])
            flag = True
    if flag == True:
        print(word + " - " + examp + " - " + defen)
    else:
        print("Слова "+m+" нет в словаре")



