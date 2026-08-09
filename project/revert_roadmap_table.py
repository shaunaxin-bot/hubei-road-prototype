import os
import re

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Revert wrapper
content = content.replace(
    '<div class="overflow-hidden mt-3 rounded-2xl border-2 border-indigo-300 shadow-xl bg-white relative z-10">',
    '<div class="overflow-x-auto mt-2 rounded-xl border border-indigo-100 shadow-md bg-white">'
)

# Revert thead
old_head = '''<tr class="bg-gradient-to-r from-indigo-700 to-indigo-600 text-white font-black border-b-4 border-indigo-800 tracking-wider shadow-sm">
                  <th class="p-3 border-r border-indigo-500/50 w-32 text-center text-lg">阶段</th>
                  <th class="p-3 border-r border-indigo-500/50 w-40 text-center text-lg">时间</th>
                  <th class="p-3 text-lg pl-5"><i class="fa-solid fa-list-check mr-2 text-indigo-200"></i>重点工作内容与责任分工</th>
                </tr>'''
new_head = '''<tr class="bg-indigo-50/80 text-indigo-900 font-bold border-b-2 border-indigo-200">
                  <th class="p-2.5 border-r border-slate-100 w-28">阶段</th>
                  <th class="p-2.5 border-r border-slate-100 w-32">时间</th>
                  <th class="p-2.5">重点工作内容与责任分工</th>
                </tr>'''
content = content.replace(old_head, new_head)

# Revert phase columns
phases = ["启动攻坚期", "全面推进期", "提质深化期"]
for phase in phases:
    bad_td = f'<td class="p-5 border-r-2 border-slate-100 font-black text-indigo-900 bg-gradient-to-b from-indigo-50 to-white text-2xl text-center align-middle shadow-[inset_-3px_0_15px_rgba(0,0,0,0.03)]" style="writing-mode: vertical-rl; letter-spacing: 0.3em;">{phase}</td>'
    good_td = f'<td class="p-2.5 border-r border-slate-100 font-bold text-brand-800 bg-blue-50/30">{phase}</td>'
    content = content.replace(bad_td, good_td)

# Revert time columns
times = ["2026.8—2026.9", "2026.9—2026.12", "2026.12—2027.2"]
for time in times:
    bad_td = f'<td class="p-4 border-r-2 border-slate-100 font-extrabold text-slate-700 text-center align-middle bg-slate-50/50 text-lg whitespace-nowrap">{time}</td>'
    good_td = f'<td class="p-2.5 border-r border-slate-100">{time}</td>'
    content = content.replace(bad_td, good_td)

# Revert row padding but keep group
content = content.replace('class="p-4 space-y-2 text-base"', 'class="p-2.5 space-y-1"')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
