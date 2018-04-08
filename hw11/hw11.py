#Левченко Варя, группа 3, вариант 6
import re

def get_text():
    with open('wiki_test.txt', encoding='utf-8') as f:
        text = f.read()
    return text

def substitute(text):
    text = re.sub(r'Финл(я|я́)ндия\b','Малайзия',text)
    text = re.sub(r'Финл(я|я́)ндии\b','Малайзии',text)
    text = re.sub(r'Финл(я|я́)ндию\b','Малайзию',text)    
    text = re.sub(r'Финл(я|я́)ндией\b','Малайзией',text)
    return text

def to_file(text):
    with open("wiki_new.txt", "w", encoding="utf-8") as f:
        f.write(text)

def printing():
    with open("wiki_new.txt", encoding="utf-8") as f:
        text = f.read()
    print(text)

def main():
    to_file(substitute(get_text()))
    printing()

if __name__ == '__main__':
    main()
