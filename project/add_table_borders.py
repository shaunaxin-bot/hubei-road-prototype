import os
import re

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace border-r border-slate-100 -> border border-slate-200 in all th/td
def process_cell(match):
    tag = match.group(1) # 'td' or 'th'
    attrs = match.group(2) # attributes string
    
    # If it has the old border, replace it
    if 'border-r border-slate-100' in attrs:
        attrs = attrs.replace('border-r border-slate-100', 'border border-slate-200')
    # Or if it has no border class yet, add it
    elif 'border' not in attrs:
        # Find class="..." and append border border-slate-200
        class_match = re.search(r'class="([^"]*)"', attrs)
        if class_match:
            old_classes = class_match.group(1)
            new_classes = old_classes + ' border border-slate-200'
            attrs = attrs.replace(f'class="{old_classes}"', f'class="{new_classes}"')
        else:
            # Add class attribute
            attrs += ' class="border border-slate-200"'
            
    return f'<{tag}{attrs}>'

content = re.sub(r'<(td|th)([^>]*)>', process_cell, content)

# Also ensure table borders are clearly defined in the header tr
content = content.replace('border-b-2 border-indigo-200', 'border-b-2 border-indigo-200 border-x border-x-indigo-100')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
