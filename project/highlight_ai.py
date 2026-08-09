import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the wrapper and header
old_header = '''<div id="sec1-3-3" class="space-y-3 scroll-mt-6">
            <h3 class="text-base font-bold text-slate-800 flex items-center mb-1">
              <i class="fa-solid fa-robot text-brand-600 mr-2"></i>1.3.3. AI治理工具
            </h3>'''

new_header = '''<div id="sec1-3-3" class="space-y-4 scroll-mt-6 relative rounded-2xl p-6 bg-gradient-to-br from-indigo-50/80 via-white to-purple-50/80 border-2 border-indigo-200 shadow-lg overflow-hidden">
            <div class="absolute top-0 right-0 p-4 opacity-10 pointer-events-none">
              <i class="fa-solid fa-microchip text-8xl text-indigo-600"></i>
            </div>
            <div class="absolute -top-10 -right-10 w-40 h-40 bg-indigo-400/20 rounded-full blur-3xl pointer-events-none"></div>
            <div class="absolute -bottom-10 -left-10 w-40 h-40 bg-purple-400/20 rounded-full blur-3xl pointer-events-none"></div>

            <div class="flex items-center justify-between mb-2 relative z-10">
              <h3 class="text-xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-indigo-700 to-purple-700 flex items-center">
                <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-indigo-600 to-purple-600 flex items-center justify-center mr-3 shadow-md shrink-0">
                  <i class="fa-solid fa-robot text-white text-sm"></i>
                </div>
                1.3.3. AI治理工具 (核心赋能)
              </h3>
              <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-gradient-to-r from-amber-100 to-orange-100 text-amber-700 border border-amber-200 shadow-sm shrink-0">
                <i class="fa-solid fa-fire mr-1 text-orange-500"></i> 重点专项
              </span>
            </div>'''

content = content.replace(old_header, new_header)

# Replace the inner item styling
old_inner_class = 'class="p-3 bg-blue-50/60 rounded-lg border border-blue-200"'
new_inner_class = 'class="p-4 bg-white/80 backdrop-blur-sm rounded-xl border border-indigo-100 shadow-sm hover:shadow-md transition-shadow relative z-10"'
content = content.replace(old_inner_class, new_inner_class)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
