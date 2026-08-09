import os
import re

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I will find the specific divs for 1.3.1 and 1.3.2 first as requested by the screenshot
# The user specifically screenshot 1.3.1 and 1.3.2 which were using bg-slate-50 border border-slate-200
# I will change ALL of those grid cards across the document (1.3.1, 1.3.2, 1.4.x, 1.5.x, 1.6.x, 1.7.x)
# Wait, are they all 3rd level? Yes, 1.4.1, 1.5.1, 1.6.1, 1.7.1 are all 3rd level.
# Wait, what about 1.3.4.1? That's 4th level. Should it be changed? The user explicitly said "三级目录" (3rd level).
# I'll manually define the regex replacements for the 3rd level divs to ensure accuracy.

import re

# Find divs containing h3 or strong with 3rd level numbers (e.g. 1.3.1)
# Regex to match the opening div, followed by whitespace, then an inner tag with 1.\d.\d.
pattern = re.compile(r'(<div[^>]*class="[^"]*?(?:bg-slate-50|bg-white)[^"]*border-slate-200[^"]*"[^>]*>\s*<(?:h3|strong|h4)[^>]*>\s*1\.\d\.\d\.?\s+)', re.IGNORECASE)

# We need to replace the class attribute of the matched div.
# Let's do it by finding all matches, then subbing the class.

def replacer(match):
    full_match = match.group(1)
    # Extract the div tag
    div_match = re.search(r'<div[^>]*>', full_match)
    if not div_match:
        return full_match
    
    div_tag = div_match.group(0)
    
    # Replace the class inside the div_tag
    new_class = 'bg-blue-50/80 border-l-4 border-brand-600 p-4 rounded-r-lg space-y-1 scroll-mt-6'
    new_div_tag = re.sub(r'class="[^"]*"', f'class="{new_class}"', div_tag)
    
    return full_match.replace(div_tag, new_div_tag)

new_content = pattern.sub(replacer, content)

# Check 1.7.1 separately because it might not have the scroll-mt-6 on the same div
pattern_171 = re.compile(r'(<div[^>]*class="[^"]*?(?:bg-slate-50|bg-white)[^"]*border-slate-200[^"]*"[^>]*>\s*<(?:h3|strong|h4)[^>]*>\s*1\.7\.1\.?\s+)', re.IGNORECASE)
new_content = pattern_171.sub(replacer, new_content)

# Let's also do 1.7.2 which doesn't have a wrapper div like that, it's just a h3 then a table. Wait, 1.7.2 is the table section. I shouldn't mess with it unless it has a wrapper card. 

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replaced instances:", len(pattern.findall(content)))

