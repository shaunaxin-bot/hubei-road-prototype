import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

new_tree_html = '''
        <div class="tree-group space-y-1 hidden" id="tree-doc1">
          <a href="#sec1-1" class="dir-item flex items-center space-x-2 py-1 px-2 rounded-md bg-white border border-slate-100/60 text-slate-700 hover:bg-slate-50 hover:text-brand-700 transition-all font-medium shadow-xs">
            <i class="fa-solid fa-bullseye text-indigo-500 text-sm w-4 text-center"></i>
            <span class="truncate">数据治理专项工程范围</span>
          </a>

          <!-- Part 1 -->
          <div class="bg-white rounded-lg p-1.5 border border-slate-100/60 shadow-xs space-y-0.5">
            <div onclick="toggleAccordion('acc-doc1-sec1')" class="flex items-center justify-between p-1 rounded-md hover:bg-slate-50 cursor-pointer text-slate-800 font-bold">
              <span class="flex items-center space-x-2 truncate">
                <i class="fa-solid fa-caret-down text-slate-400 text-sm transition-transform transform" id="acc-doc1-sec1-icon"></i>
                <span class="text-sm truncate">第一部分：数据指南编制</span>
              </span>
            </div>
            <div id="acc-doc1-sec1" class="pl-2 space-y-0.5 border-l border-brand-100 ml-1.5 pt-0.5">
              <a href="#sec1-2-1" class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700"><span class="truncate">（一）基础标准与质量指南</span></a>
              <a href="#sec1-2-2" class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700"><span class="truncate">（二）采集接入与共享指南</span></a>
              <a href="#sec1-2-3" class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700"><span class="truncate">（三）安全管控与合规指南</span></a>
              <a href="#sec1-2-4" class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700"><span class="truncate">（四）AI治理工具指南</span></a>
            </div>
          </div>

          <!-- Part 2 -->
          <div class="bg-white rounded-lg p-1.5 border border-slate-100/60 shadow-xs space-y-0.5">
            <div onclick="toggleAccordion('acc-doc1-sec2')" class="flex items-center justify-between p-1 rounded-md hover:bg-slate-50 cursor-pointer text-slate-800 font-bold">
              <span class="flex items-center space-x-2 truncate">
                <i class="fa-solid fa-caret-down text-slate-400 text-sm transition-transform transform" id="acc-doc1-sec2-icon"></i>
                <span class="text-sm truncate">第二部分：AI治理工具</span>
              </span>
            </div>
            <div id="acc-doc1-sec2" class="pl-2 space-y-0.5 border-l border-brand-100 ml-1.5 pt-0.5">
              <a href="#sec1-3-3-1" class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700"><span class="truncate">（一）数据需求及资源盘点</span></a>
              <a href="#sec1-3-3-2" class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700"><span class="truncate">（二）数据接入与AI自适应导入</span></a>
              <a href="#sec1-3-3-3" class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700"><span class="truncate">（三）AI质控</span></a>
              <a href="#sec1-3-3-4" class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700"><span class="truncate">（四）AI数仓</span></a>
              <a href="#sec1-3-3-5" class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700"><span class="truncate">（五）数据分级分类和业务考核</span></a>
            </div>
          </div>

          <!-- Part 3 -->
          <div class="bg-white rounded-lg p-1.5 border border-slate-100/60 shadow-xs space-y-0.5">
            <div onclick="toggleAccordion('acc-doc1-sec3')" class="flex items-center justify-between p-1 rounded-md hover:bg-slate-50 cursor-pointer text-slate-800 font-bold">
              <span class="flex items-center space-x-2 truncate">
                <i class="fa-solid fa-caret-down text-slate-400 text-sm transition-transform transform" id="acc-doc1-sec3-icon"></i>
                <span class="text-sm truncate">第三部分：验收标准</span>
              </span>
            </div>
            <div id="acc-doc1-sec3" class="pl-2 space-y-0.5 border-l border-brand-100 ml-1.5 pt-0.5">
              <a href="#sec1-7-1" class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700"><span class="truncate">（一）基本验收要求</span></a>
              <a href="#sec1-7-2" class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700"><span class="truncate">（二）项目验收成果表</span></a>
            </div>
          </div>
        </div>
'''

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('<div class="tree-group space-y-1 hidden" id="tree-doc1">')
if start_idx != -1:
    end_idx = text.find('<!-- Document 3 Tree Directory -->', start_idx)
    if end_idx != -1:
        new_text = text[:start_idx] + new_tree_html.strip() + "\n\n        " + text[end_idx:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Success")
    else:
        print("Error: end_idx not found")
else:
    print("Error: start_idx not found")
