import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')
tab1 = soup.find(id='biz-tab-1')

if tab1:
    spans = tab1.find_all('span', class_=True)
    for span in spans:
        classes = span.get('class', [])
        if 'text-rose-600' in classes or 'text-blue-600' in classes:
            if 'font-bold' in classes:
                classes.remove('font-bold')
                span['class'] = classes

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Removed font-bold from red and blue texts in Option 1.")
