import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_str = '''        <div class="w-8 h-8 rounded-lg bg-white/15 border border-white/20 flex items-center justify-center font-bold text-lg text-white">
          
        </div>'''
new_str = '''        <div class="w-8 h-8 rounded-lg bg-white/15 border border-white/20 flex items-center justify-center font-bold text-lg text-white">
          <i class="fa-solid fa-road text-white/90 text-sm"></i>
        </div>'''

if old_str in content:
    content = content.replace(old_str, new_str)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Success")
else:
    print("Failed to find exact string match.")
