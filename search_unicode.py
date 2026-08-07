import sys
import io
import re

with open('index_good.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

with io.open('search_out.txt', 'w', encoding='utf-8') as out:
    # also search for unescaped words just in case
    words = ['\\u516c\\u8def', '\\u5f85\\u63a5\\u5165'] # 公路, 待接入
    for word in words:
        idx = text.find(word)
        out.write(f'Found {word}: {idx}\n')
        if idx != -1:
            out.write(text[max(0, idx-200):min(len(text), idx+200)] + '\n')
