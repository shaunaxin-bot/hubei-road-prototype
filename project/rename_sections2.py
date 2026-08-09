import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    "1、数据采集与接入": "（一）数据采集与接入",
    "2、数据资源盘点": "（二）数据资源盘点",
    "3、标准数据仓建设": "（三）标准数据仓建设",
    "4、数据质量稽查与评估": "（四）数据质量稽查与评估",
    "5、数据共享与发布": "（五）数据共享与发布"
}

new_text = text
for old, new in replacements.items():
    new_text = new_text.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Renamed AI governance sub-sections to use bracketed numbers.")
