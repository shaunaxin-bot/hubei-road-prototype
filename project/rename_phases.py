import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    "1. 启动攻坚期": "（一）启动攻坚期",
    "2. 全面推进期": "（二）全面推进期",
    "3. 提质深化期": "（三）提质深化期"
}

new_text = text
for old, new in replacements.items():
    new_text = new_text.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Renamed phases to use bracketed numbers.")
