import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the remaining titles in Option 1
replacements = {
    "4. 数据资产运营能力凭证：": "4. 数据治理与应用服务凭证：",
    "1. 数据治理与数据资产入表全链条业绩：": "1. 数据治理与应用全链条业绩："
}

for old, new in replacements.items():
    text = text.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed the titles.")
