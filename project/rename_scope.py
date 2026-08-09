import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('1.1. 数据治理范围', '数据治理专项工程范围')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
