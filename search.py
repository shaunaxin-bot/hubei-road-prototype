import sys
import io

with open('index_good.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

with io.open('search_out.txt', 'w', encoding='utf-8') as out:
    words = ['公路静态数据', '待接入', '2019年', '年报数据', '年报文件夹']
    for word in words:
        idx = text.find(word)
        out.write(f'Found {word}: {idx}\n')
        if idx != -1:
            out.write(text[max(0, idx-200):min(len(text), idx+200)] + '\n')
