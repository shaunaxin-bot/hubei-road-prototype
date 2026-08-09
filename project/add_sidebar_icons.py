import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace for doc1
old_doc1 = '''<a href="#sec1-1" class="dir-item flex items-center space-x-2 p-2 rounded-lg bg-white border border-slate-200/60 text-slate-700 hover:bg-slate-50 hover:text-brand-700 transition-all font-medium shadow-xs">
            
            <span class="truncate">1.1. 数据治理范围</span>
          </a>'''
new_doc1 = '''<a href="#sec1-1" class="dir-item flex items-center space-x-2 p-2 rounded-lg bg-white border border-slate-200/60 text-slate-700 hover:bg-slate-50 hover:text-brand-700 transition-all font-medium shadow-xs">
            <i class="fa-solid fa-bullseye text-indigo-500 text-base w-4 text-center"></i>
            <span class="truncate">1.1. 数据治理范围</span>
          </a>'''

# Replace for doc2
old_doc2 = '''<a href="#sec2-notice" class="dir-item flex items-center space-x-2 p-2 rounded-lg bg-white border border-slate-200/60 text-slate-700 hover:bg-slate-50 transition-all font-medium shadow-xs">
            
            <span class="truncate">印发通知公文</span>
          </a>'''
new_doc2 = '''<a href="#sec2-notice" class="dir-item flex items-center space-x-2 p-2 rounded-lg bg-white border border-slate-200/60 text-slate-700 hover:bg-slate-50 transition-all font-medium shadow-xs">
            <i class="fa-solid fa-envelope-open-text text-rose-500 text-base w-4 text-center"></i>
            <span class="truncate">印发通知公文</span>
          </a>'''

content = content.replace(old_doc1, new_doc1)
content = content.replace(old_doc2, new_doc2)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Success")
