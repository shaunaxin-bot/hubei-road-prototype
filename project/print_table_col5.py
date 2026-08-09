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
            if len(tds) >= 3:
                deliverable = tds[-3].get_text(strip=True) if len(tds) >= 3 else ""
                requirement = tds[-1].get_text(strip=True) if len(tds) >= 1 else ""
                print(f"Row {i}:\n Deliverable: {deliverable}\n Requirement: {requirement}\n")
