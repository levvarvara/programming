#Левченко Варвара, группа 3, вариант 6
import re

def get_text():
    with open('text.txt', encoding='utf-8') as f:
        text = f.read()
    return text

def regular(text):
    match = re.findall(r'загру[зж][ияе]\w*', text)
    return match

def printing(match):
    for element in match:
        print(element)

def main():
    printing(regular(get_text()))

if __name__ == '__main__':
    main()
