#Варя Левченко, группа 3, вариант 6

"""Для каждого предложения длиннее 10 слов напечатать
"Это предложение со словами длины ...", вместо точек подставив среднюю длину
слова в символах в этом предложении, округлив до 1 знака после запятой"""

import re

def get_text():
    with open('text.txt', encoding='utf-8') as f:
        text = f.read()
    return text

def sent(text):
    split_regex = re.compile(r'[.|!|?|…]')
    sent = [re.sub(r'[^\w\s]','',t) for t in split_regex.split(text)]

    return sent

def printing(avarage):
    print('Это предложение со словами длины {:.1f}'.format(avarage))
    
def analisis(sent):
    summ = 0
    for s in range(0,len(sent)):
        sent[s] = [t for t in sent[s].split()]
        if len(sent[s]) >= 10:
            for word in sent[s]:
                summ += len(word)
            avarage = summ/len(sent[s])
            print(' '.join(sent[s]))
            print()
            printing(avarage)
            print()
        summ = 0
    

def main():
    analisis((sent(get_text())))
    
if __name__ == '__main__':
    main()
