with open("text.txt", encoding="utf-8") as f:
    text = f.read()
    words = text.split()
counter = 0
for i in words:
    if i.istitle():
        counter +=1
result = len(words)/100*counter
print("Процент слов, начинающихся с заглавной буквы: "+"%.2f" % result+"%")
