import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('数据治理工程评分标准', '数据治理专项评分标准')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
