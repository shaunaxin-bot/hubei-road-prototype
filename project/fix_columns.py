import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

phases = ["启动攻坚期", "全面推进期", "提质深化期"]
for phase in phases:
    old = f'<td class="p-2.5 border-r border-slate-100 font-bold text-brand-800 bg-blue-50/30">{phase}</td>'
    new = f'<td class="p-5 border-r-2 border-slate-100 font-black text-indigo-900 bg-gradient-to-b from-indigo-50 to-white text-2xl text-center align-middle shadow-[inset_-3px_0_15px_rgba(0,0,0,0.03)]" style="writing-mode: vertical-rl; letter-spacing: 0.3em;">{phase}</td>'
    content = content.replace(old, new)

times = ["2026.8—2026.9", "2026.9—2026.12", "2026.12—2027.2"]
for time in times:
    old = f'<td class="p-2.5 border-r border-slate-100">{time}</td>'
    new = f'<td class="p-4 border-r-2 border-slate-100 font-extrabold text-slate-700 text-center align-middle bg-slate-50/50 text-lg whitespace-nowrap">{time}</td>'
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
