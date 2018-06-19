import re
import collections, os

def get_text(file_name):
    with open(file_name, encoding='windows-1251') as f:
        text = f.read()
    return text

def info(text):
    docid = re.search('<meta.*?="(.*?)".*?docid', text).group(1)
    title = re.search('<title>(.*?)<', text).group(1)
    author = re.search('<meta.*?="(.*?)".*?author', text).group(1)
    created = re.search('<meta.*?="(.*?)".*?created', text).group(1)
    topic = re.search('<meta.*?="(.*?)".*?topic', text).group(1)
    tagging = re.search('<meta.*?="(.*?)".*?tagging', text).group(1)
    meta = [docid, title, author, created, topic, tagging]
    return meta



def list_to_file(info):
    with open('meta_data.csv', 'w') as f:
        f.write("doc_id,title,author,created,topic,tagging\n")
        for p in info:
            if p != (len(info)-1):
                f.write(p + ',')
            else:
                f.write(p)
        f.write('\n')

def main():
    file_list = os.listdir()
    for s in range(0,len(file_list)):
        if re.match(r'_.*?', file_list[s]) != None:
            print(file_list[s])
            meta = info((get_text(file_list[s])))
            print(meta)
            list_to_file(meta)
        else:
            continue

if __name__ == '__main__':
    main()
