import os
import re

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the table wrappers
content = content.replace('overflow-x-auto border border-slate-200 rounded-lg shadow-sm', 
                          'overflow-x-auto rounded-xl border border-indigo-100 shadow-md bg-white')
content = content.replace('overflow-x-auto mt-2', 
                          'overflow-x-auto mt-2 rounded-xl border border-indigo-100 shadow-md bg-white')

# 2. Update the thead rows
# Using regex to find <tr class="bg-slate-100... "> inside theads
def replace_thead_tr(match):
    return '<tr class="bg-indigo-50/80 text-indigo-900 font-bold border-b-2 border-indigo-200">'
content = re.sub(r'<tr class="bg-slate-10[^"]*"', replace_thead_tr, content)

# 3. Soften the cell borders and hover states
content = content.replace('border-slate-200', 'border-slate-100')
content = content.replace('hover:bg-slate-50/80', 'hover:bg-indigo-50/40 transition-colors')

# 4. For some specific text-slate-800 or text-slate-700 in table heads (which we might have missed or are on th tags)
# It's safer to just rely on the tr class cascading, but tailwind requires explicit classes sometimes.
# We'll just leave them, or since we replaced the whole tr class, they should be gone if they were on the tr.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
