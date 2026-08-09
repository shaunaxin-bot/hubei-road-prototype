import os
import re

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Isolate sidebar
start_idx = content.find('<aside')
end_idx = content.find('</aside>') + 8

sidebar = content[start_idx:end_idx]

# Perform replacements on sidebar
sidebar = sidebar.replace('p-3 text-base space-y-2', 'p-2 text-sm space-y-1.5')
sidebar = sidebar.replace('space-x-2 p-2 rounded-lg', 'space-x-2 py-1 px-2 rounded-md')
sidebar = sidebar.replace('rounded-xl p-2 border', 'rounded-lg p-1.5 border')
sidebar = sidebar.replace('space-y-1">\n', 'space-y-0.5">\n')
sidebar = sidebar.replace('p-1.5 rounded-md hover:bg-slate-50', 'p-1 rounded-md hover:bg-slate-50')
sidebar = sidebar.replace('pl-3 space-y-1 border-l-2 border-brand-100 ml-2 pt-1', 'pl-2 space-y-0.5 border-l border-brand-100 ml-1.5 pt-0.5')
sidebar = sidebar.replace('p-1.5 rounded-md text-slate-600', 'py-1 px-1.5 rounded-md text-slate-600 text-sm')

# additional tweaks
sidebar = sidebar.replace('text-base', 'text-sm')
sidebar = sidebar.replace('w-80', 'w-64') # make the whole sidebar slightly narrower too if it's too loose? No, user just said left menu is too loose. Let's keep width, just compact vertically.
sidebar = sidebar.replace('w-64', 'w-72') # actually w-72 is a good compromise.

content = content[:start_idx] + sidebar + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
