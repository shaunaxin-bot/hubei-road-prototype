import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

doc1 = soup.find(id='doc1-content')
if doc1:
    for child in doc1.find_all(recursive=False):
        if child.has_attr('id'):
            print(f"ID: {child['id']}")
        else:
            h2 = child.find('h2')
            if h2:
                print(f"H2: {h2.text.strip()}")
            else:
                print(f"Tag: {child.name}, Class: {child.get('class')}")
