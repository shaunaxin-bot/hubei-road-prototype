import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<table class="w-full text-left text-base border-collapse">'
end_marker = '</table>'
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx) + len(end_marker)

table_content = content[start_idx:end_idx]

# Clean up red text and make it look like the original website
table_content = table_content.replace('text-red-600', '')
table_content = table_content.replace('font-bold border-b border-slate-200"', 'font-bold border-b border-slate-200 text-slate-700"')
table_content = table_content.replace('p-2.5 font-bold  border-r', 'p-2.5 font-bold text-slate-800 border-r')
table_content = table_content.replace('class="p-2.5 border-r border-slate-200 font-bold "', 'class="p-2.5 border-r border-slate-200"')
table_content = table_content.replace('class="p-2.5 "', 'class="p-2.5 text-slate-600"')
table_content = table_content.replace('class="p-2.5 font-bold  border-r border-slate-200 text-center align-middle" style="writing-mode: vertical-rl; text-orientation: upright; letter-spacing: 4px;">初步验收</td>', 'class="p-2.5 font-bold text-brand-800 bg-blue-50/40 border-r border-slate-200 text-center align-middle" style="writing-mode: vertical-rl; text-orientation: upright; letter-spacing: 4px;">初步验收</td>')
table_content = table_content.replace('class="p-2.5 font-bold  border-r border-slate-200 text-center align-middle" style="writing-mode: vertical-rl; text-orientation: upright; letter-spacing: 4px;">最终验收</td>', 'class="p-2.5 font-bold text-emerald-800 bg-emerald-50/40 border-r border-slate-200 text-center align-middle" style="writing-mode: vertical-rl; text-orientation: upright; letter-spacing: 4px;">最终验收</td>')

# Format the category cells
table_content = table_content.replace('<td rowspan="5" class="p-2.5 font-bold  border-r border-slate-200 text-center align-middle" style="width: 140px;">1. 项目建设与交付类</td>', '<td rowspan="5" class="p-2.5 font-bold text-slate-700 border-r border-slate-200 text-center align-middle" style="width: 140px;">1. 项目建设与交付类</td>')
table_content = table_content.replace('<td rowspan="2" class="p-2.5 font-bold  border-r border-slate-200 text-center align-middle">2. 平台功能演示类</td>', '<td rowspan="2" class="p-2.5 font-bold text-slate-700 border-r border-slate-200 text-center align-middle">2. 平台功能演示类</td>')
table_content = table_content.replace('<td rowspan="5" class="p-2.5 font-bold  border-r border-slate-200 text-center align-middle">3. 治理过程与成果类</td>', '<td rowspan="5" class="p-2.5 font-bold text-slate-700 border-r border-slate-200 text-center align-middle">3. 治理过程与成果类</td>')
table_content = table_content.replace('<td rowspan="3" class="p-2.5 font-bold  border-r border-slate-200 text-center align-middle">4. 试运行与终验类</td>', '<td rowspan="3" class="p-2.5 font-bold text-slate-700 border-r border-slate-200 text-center align-middle">4. 试运行与终验类</td>')


new_content = content[:start_idx] + table_content + content[end_idx:]
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Success")
