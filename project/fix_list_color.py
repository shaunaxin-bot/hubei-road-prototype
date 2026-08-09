import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<strong class="text-indigo-800">1. 机关处室：</strong>', '<strong>1. 机关处室：</strong>')
content = content.replace('<strong class="text-indigo-800">2. 市州公路机构：</strong>', '<strong>2. 市州公路机构：</strong>')
content = content.replace('<strong class="text-indigo-800">3. 县级公路机构：</strong>', '<strong>3. 县级公路机构：</strong>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
