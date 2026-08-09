import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '（一）第一步': '第一步',
    '（二）第二步': '第二步',
    '（三）第三步': '第三步',
    '（四）第四步': '第四步'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
