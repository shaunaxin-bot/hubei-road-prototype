import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

table_container = soup.find(id='sec1-7-2')
if table_container:
    tbody = table_container.find('tbody')
    if tbody:
        rows = tbody.find_all('tr')
        for i, row in enumerate(rows):
            tds = row.find_all('td')
            # Extract text to see what row we are in
            print(f"Row {i}:")
            for td in tds:
                print(f"  - {td.get_text(separator=' ', strip=True)[:50]}...")
