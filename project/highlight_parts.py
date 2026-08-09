import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

part1_old = '<p class="text-base font-bold text-slate-800 pt-2">第一部分以业务定义数据。旨在从公路业务政策与管理现状出发，摸清家底，将业务规则智能转化为机器可读的数据标准与底座资产。</p>'
part1_new = '''<div class="relative z-10 pt-4 pb-2">
              <div class="flex items-center space-x-3 mb-2">
                <span class="inline-flex items-center justify-center px-3 py-1 rounded-md text-sm font-black bg-indigo-600 text-white shadow-md">第一部分</span>
                <span class="text-lg font-black text-transparent bg-clip-text bg-gradient-to-r from-indigo-800 to-blue-600 tracking-wide">以业务定义数据</span>
              </div>
              <p class="text-base text-slate-700 leading-relaxed border-l-2 border-indigo-200 pl-3 ml-1 mb-2">
                旨在从公路业务政策与管理现状出发，摸清家底，将业务规则智能转化为<strong class="text-indigo-700 font-bold">机器可读的数据标准与底座资产</strong>。
              </p>
            </div>'''

part2_old = '<p class="text-base font-bold text-slate-800 pt-2">第二部分以数据驱动业务。旨在将标准化的海量数据加工为核心资产与指令，打破部门壁垒，直接赋能各业务处室的实战应用与长效考核。</p>'
part2_new = '''<div class="relative z-10 pt-6 pb-2">
              <div class="flex items-center space-x-3 mb-2">
                <span class="inline-flex items-center justify-center px-3 py-1 rounded-md text-sm font-black bg-purple-600 text-white shadow-md">第二部分</span>
                <span class="text-lg font-black text-transparent bg-clip-text bg-gradient-to-r from-purple-800 to-fuchsia-600 tracking-wide">以数据驱动业务</span>
              </div>
              <p class="text-base text-slate-700 leading-relaxed border-l-2 border-purple-200 pl-3 ml-1 mb-2">
                旨在将标准化的海量数据加工为核心资产与指令，打破部门壁垒，直接赋能各业务处室的<strong class="text-purple-700 font-bold">实战应用与长效考核</strong>。
              </p>
            </div>'''

content = content.replace(part1_old, part1_new)
content = content.replace(part2_old, part2_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
