import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

count = content.count('评估标准')
content = content.replace('评估标准', '评分标准')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Replaced {count} instances.")
