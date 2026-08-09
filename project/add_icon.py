import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_header = '''      <div class="flex items-center space-x-3">
        <div class="hidden md:flex items-center space-x-2">
          
        </div>
        <div>
          <h1 class="text-lg font-bold tracking-tight text-white">湖北公路数据治理专项进展汇报</h1>
        </div>
      </div>'''

new_header = '''      <div class="flex items-center space-x-3">
        <div class="w-9 h-9 rounded-xl bg-white/10 border border-white/20 flex items-center justify-center shrink-0 shadow-inner backdrop-blur-sm">
          <i class="fa-solid fa-database text-white/90 text-sm"></i>
        </div>
        <div>
          <h1 class="text-lg md:text-xl font-bold tracking-tight text-white">湖北公路数据治理专项进展汇报</h1>
        </div>
      </div>'''

content = content.replace(old_header, new_header)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Success")
