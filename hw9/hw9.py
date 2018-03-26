#Левченко Варвара, группа 3, вариант 6
import re

def get_text():
    with open('text.txt', encoding='utf-8') as f:
        text = f.read()
    return text

def regular(text):
    match = re.findall(r'загру[зж][ияе]\w*', text)
    return match

def spisok(match):
    mass = []
    for element in match:
        if element in mass:
            continue
        else:
            mass.append(element)   
    return mass

def printing(mass):
    for element in mass:
        print(element)

def main():
    mass = spisok(regular(get_text()))
    printing(mass)

if __name__ == '__main__':
    main()
