#Левченко Варвара, группа 3, вариант 6
import re
def get_text():
    with open('wiki2.html', encoding='utf-8') as f:
        text = f.read()
    return text

def regular(text):
    res = re.search(r'>Отряд.*?<a.*?>(.*?)</a>',text)
    res = res.group(1)

    return res

def to_file(res):
    with open("отряды.txt", "a", encoding="utf-8") as f:
        f.write(res+'\n')

def main():
    res = regular(get_text())
    to_file(res)
    with open("отряды.txt", encoding="utf-8") as f:
        text = f.read()
    print(text.strip())


if __name__ == '__main__':
    main()
