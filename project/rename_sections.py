import os
import re

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    "（一）数据需求及资源盘点": "1、数据采集与接入",
    "（二）数据接入与AI自适应导入": "2、数据资源盘点",
    "（三）AI质控": "3、标准数据仓建设",
    "（四）AI数仓": "4、数据质量稽查与评估",
    "（五）数据分级分类和业务考核": "5、数据共享与发布"
}

new_text = text
for old, new in replacements.items():
    new_text = new_text.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Renamed AI governance sub-sections.")
