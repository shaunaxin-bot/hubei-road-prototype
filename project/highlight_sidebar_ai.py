import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_link = '''<a href="#sec1-3-3" class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700">
                <span class="truncate">1.3.3. AI治理工具</span>
              </a>'''
new_link = '''<a href="#sec1-3-3" class="dir-item flex items-center space-x-2 py-1 px-2 rounded-md text-brand-700 text-sm font-bold bg-blue-50 border-l-[3px] border-brand-600">
                <span class="truncate">1.3.3. AI治理工具</span>
              </a>'''

content = content.replace(old_link, new_link)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
