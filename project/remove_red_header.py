import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_block = '''        <!-- Official Document Notice Header Section -->
        <div id="sec2-notice" class="border-b-2 border-red-500 pb-6 scroll-mt-6">
          <div class="text-center space-y-2">
            <h1 class="text-2xl md:text-3xl font-extrabold text-red-600 tracking-wider">湖北省公路事业发展中心文件</h1>
            <p class="text-base font-semibold text-slate-700">鄂公路发〔2026〕28号</p>
          </div>
          <div class="my-4 border-t border-red-400"></div>'''

new_block = '''        <!-- Official Document Notice Header Section -->
        <div id="sec2-notice" class="scroll-mt-6">'''

content = content.replace(old_block, new_block)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
