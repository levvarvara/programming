#Левченко Варвара, группа 3
import collections

#читаем файл, разбиваем на слова
def open_file():
    f = open('text.txt', 'r')
    text = f.read()
    words = text.split()
    return words

#в этой функции слова с omni- и без
def counter():
    words = open_file()
    array = []
    for n in words:
        n = list(n) #разбиваем слово на символы 
        for k in n: #идем по буквам слова
            if n[0:4] == ['o','m','n','i']:
                m = ''.join(n[4::]) #объединяем буквы в слово без приставки, начиная с 5-ой буквы
                n = ''.join(n) #объединяем буквы в слово с приставкой
                array.append(n) #добавляем слово с приставкой в список
                for h in words: #второй раз идем по всем словам; считаем, сколько в тексте без приставки; добавляем каждое совпадающее в список
                    if h == m: 
                        array.append(h)
    return array

#создаем словарь из списка 
def make_dict():
    omni_dict = collections.Counter(counter())
    return omni_dict

#вывод словаря на экран через цикл 
def main():
    omni_dict = make_dict()
    for key, value in omni_dict.items():
        print(key + ': ', value)

if __name__ == '__main__':
    main()



    
    








