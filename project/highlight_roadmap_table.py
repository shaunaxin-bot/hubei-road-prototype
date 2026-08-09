import os
import re

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make the wrapper pop
content = content.replace(
    '1.5">3. 推进路线与计划</h3>\n          <div class="overflow-x-auto mt-2 rounded-xl border border-indigo-100 shadow-md bg-white">',
    '1.5">3. 推进路线与计划</h3>\n          <div class="overflow-hidden mt-3 rounded-2xl border-2 border-indigo-300 shadow-xl bg-white relative z-10">'
)

# Fix the header of this specific table
old_head = '''<tr class="bg-indigo-50/80 text-indigo-900 font-bold border-b-2 border-indigo-200">
                  <th class="p-2.5 border-r border-slate-100 w-28">阶段</th>
                  <th class="p-2.5 border-r border-slate-100 w-32">时间</th>
                  <th class="p-2.5">重点工作内容与责任分工</th>
                </tr>'''
new_head = '''<tr class="bg-gradient-to-r from-indigo-700 to-indigo-600 text-white font-black border-b-4 border-indigo-800 tracking-wider shadow-sm">
                  <th class="p-3 border-r border-indigo-500/50 w-32 text-center text-lg">阶段</th>
                  <th class="p-3 border-r border-indigo-500/50 w-40 text-center text-lg">时间</th>
                  <th class="p-3 text-lg pl-5"><i class="fa-solid fa-list-check mr-2 text-indigo-200"></i>重点工作内容与责任分工</th>
                </tr>'''
content = content.replace(old_head, new_head)


def replace_row(row_id, phase_name, time_range):
    global content
    
    # 1. Update the phase td
    old_phase_td = f'<td class="p-2.5 border-r border-slate-100 font-bold text-brand-800 bg-blue-50/30">{phase_name}</td>'
    new_phase_td = f'<td class="p-4 border-r-2 border-slate-100 font-black text-indigo-900 bg-gradient-to-b from-indigo-50/80 to-white text-xl text-center align-middle shadow-[inset_-3px_0_15px_rgba(0,0,0,0.03)]"><div class="writing-mode-vertical mx-auto">{phase_name}</div></td>'
    # Fallback without writing-mode if it's horizontal
    new_phase_td = f'<td class="p-4 border-r-2 border-slate-100 font-black text-indigo-900 bg-gradient-to-b from-indigo-50/80 to-white text-lg text-center align-middle shadow-[inset_-3px_0_15px_rgba(0,0,0,0.03)]">{phase_name}</td>'
    content = content.replace(old_phase_td, new_phase_td)
    
    # 2. Update time td
    old_time_td = f'<td class="p-2.5 border-r border-slate-100">{time_range}</td>'
    new_time_td = f'<td class="p-4 border-r-2 border-slate-100 font-extrabold text-slate-700 text-center align-middle bg-slate-50/50 text-base">{time_range}</td>'
    content = content.replace(old_time_td, new_time_td)
    
    # 3. Update the content td spacing
    content = content.replace(f'<tr id="{row_id}" class="hover:bg-indigo-50/40 transition-colors scroll-mt-6">\n                  <td class="p-4', 
                              f'<tr id="{row_id}" class="hover:bg-indigo-50/40 transition-colors scroll-mt-6 group">\n                  <td class="p-4')

content = content.replace('class="p-2.5 space-y-1"', 'class="p-4 space-y-2 text-base"')

# 4. Highlight the outcome texts
def replace_outcome(match):
    text = match.group(1)
    return f'''<div class="mt-4 p-3.5 bg-gradient-to-r from-indigo-50 to-white border-l-4 border-indigo-500 rounded-r-xl shadow-sm group-hover:shadow-md transition-shadow">
                      <span class="text-indigo-900 font-black mb-1.5 flex items-center"><i class="fa-solid fa-flag-checkered mr-2 text-indigo-600"></i>成果物与牵头单位</span>
                      <p class="text-indigo-800 text-sm font-medium leading-relaxed pl-1">{text}</p>
                    </div>'''
content = re.sub(r'<p class="text-slate-500 pt-1 font-semibold">【成果物与牵头单位】：(.*?)</p>', replace_outcome, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
