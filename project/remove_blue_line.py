import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_class = "bg-blue-50/80 border-l-4 border-brand-600 p-4 rounded-r-lg space-y-1 scroll-mt-6"
new_class = "bg-blue-50/50 border border-blue-100 p-4 rounded-lg space-y-1 scroll-mt-6"

content = content.replace(old_class, new_class)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
