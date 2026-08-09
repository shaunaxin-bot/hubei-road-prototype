import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('hover:bg-slate-50"', 'hover:bg-indigo-50/40 transition-colors"')
content = content.replace('hover:bg-slate-50><', 'hover:bg-indigo-50/40 transition-colors><')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
