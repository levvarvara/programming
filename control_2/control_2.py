"""Контрольная работа
Левченко Варя, группа 3, вариант 1"""

import re
def get_text():
    with open('corpora.xml', encoding='utf-8') as f:
        text = f.read()
    return text

def hedding(text):
    hed = re.match(r'.*</teiHeader>',text, re.DOTALL)
    return hed

def counting(hed):
    count = 0
    hed = hed.splitlines()
    for line in hed:
        count += 1
    return count

def hed_to_file(count):
    with open("запись.txt", "w", encoding="utf-8") as f:
        f.write("Количество строк в заголовке:  "+count)

def printing():
    with open("запись.txt", encoding="utf-8") as f:
        text = f.read()
    print(text)

def dictionary(text):
    d = {}

    lemmas = re.findall(r'<w lemma=.*', text)
    for n in lemmas:
        if n in d:  
            d[n] += 1
        else:  
            d[n] = 1
    
    return d

def dict_to_file(d):
    with open("запись.txt", "a", encoding="utf-8") as f:
        for key, value in d.items():
            f.write('\n')
            f.write(key+ ' - ' +str(value))

def main():
    hed = hedding(get_text()).group()
    count = str(counting(hed))
    hed_to_file(count)
    dict_to_file(dictionary(get_text()))
    printing()
    

if __name__ == '__main__':
    main()
