#Левченко Варвара, группа 3, вариант 6
#В скольких папках встречается несколько файлов с одним и тем же расширением

import os
from collections import Counter

def ext_count(extentions):
    sorted_ext = Counter(extentions)
    for key, value in sorted_ext.items():
        if value >= 2 and key != '':
            return True

def scan_folders():
    start_path = '.'
    ext_counter = 0
    for root, dirs, files in os.walk(start_path):
        extentions = []
        for file in files:
            filename, file_ext = os.path.splitext(file)
            extentions.append(file_ext)
            if ext_count(extentions) == True:
                ext_counter += 1
    return ext_counter

def main():
    ext_counter = scan_folders()
    print('Несколько файлов с одинаковым расширинием в ', ext_counter, ' папках')

if __name__ == '__main__':
    main()


    
