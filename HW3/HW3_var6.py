#Левченко Варвара, вариант 6
word = input("Enter your word: ")
word_list = list(word)
if word != " ":
    word_v = ""
    print(word)  
    for n in range(len(word_list)-1):
        word_list.pop(0)
        for m in word_list[::]:
            word_v = word_v + str(m)
        print(word_v) 
        word_v = ""  

else:
    print("Empty stroka!")
