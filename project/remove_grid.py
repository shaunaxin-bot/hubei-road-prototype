import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '<div class="grid grid-cols-1 md:grid-cols-2 gap-4">': '<div class="space-y-4">',
    '<div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-base">': '<div class="space-y-3 text-base">',
    '<div class="grid grid-cols-1 md:grid-cols-3 gap-3">': '<div class="space-y-3">'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
