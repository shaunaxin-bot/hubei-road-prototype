import os
import re

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(<div[^>]*class="[^"]*?border-slate-200[^"]*"[^>]*>\s*<(?:h3|strong|h4)[^>]*>\s*1\.\d\.\d\.?\s+)', re.IGNORECASE)

def replacer(match):
    full_match = match.group(1)
    div_match = re.search(r'<div[^>]*>', full_match)
    if not div_match:
        return full_match
    
    div_tag = div_match.group(0)
    
    # We want to replace it only if it doesn't already have bg-blue-50
    if 'bg-blue-50' in div_tag:
        return full_match
        
    new_class = 'bg-blue-50/80 border-l-4 border-brand-600 p-4 rounded-r-lg space-y-1 scroll-mt-6'
    new_div_tag = re.sub(r'class="[^"]*"', f'class="{new_class}"', div_tag)
    
    return full_match.replace(div_tag, new_div_tag)

new_content = pattern.sub(replacer, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replaced instances:", len(pattern.findall(content)))
