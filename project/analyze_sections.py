import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

doc1 = soup.find(id='doc1-content')

def print_children_ids(element, prefix=""):
    for child in element.find_all(recursive=False):
        if child.has_attr('id'):
            print(f"{prefix}ID: {child['id']}")
        elif child.name == 'h2' or child.name == 'h3' or child.name == 'h4':
            print(f"{prefix}{child.name.upper()}: {child.text.strip()}")

print("--- sec1-2 ---")
sec1_2 = soup.find(id='sec1-2')
print_children_ids(sec1_2, "  ")

print("--- sec1-3 ---")
sec1_3 = soup.find(id='sec1-3')
print_children_ids(sec1_3, "  ")

