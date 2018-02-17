#Левченко Варвара, группа 3, вариант 6
import random
def get_dict():
    d = {}
    with open('words.txt', encoding='utf-8') as f:
        for line in f:
            line_n = line.split(',', maxsplit=4)
            line_n = [line.rstrip() for line in line_n]
            d[line_n[0]] = line_n[1::]
    return d  

def get_word_hint(d):
    items = d.popitem()
    word = items[0]
    hint = random.choice(items[1])
    return word, hint
    
def main():
    d = get_dict()
    word_hint = []
    word_hint = get_word_hint(d)
    n = 3
    flag = False
    print(word_hint[1])
    while n != 0:
        print("Осталось попыток: ", n)
        word = input("Введите слово: ")
        if word == word_hint[0]:
            flag = True
            break
        n -= 1
    if flag == False:
        print("Вы проиграли!")
    else:
        print("Вы выиграли!")


if __name__ == '__main__':
    main()
    
            
            
