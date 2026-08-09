import os
from bs4 import BeautifulSoup
import re

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

def get_inner_html(element):
    return "".join(str(child) for child in element.contents)

# ================= 1. Parse existing sections =================

# Scope
sec1_1 = soup.find(id='sec1-1')

# Part 1 sources
sec1_2_1 = soup.find(id='sec1-2-1')
sec1_2_2 = soup.find(id='sec1-2-2')
sec1_2_3 = soup.find(id='sec1-2-3')
sec1_2_4 = soup.find(id='sec1-2-4')
sec1_4 = soup.find(id='sec1-4')
sec1_5 = soup.find(id='sec1-5')
sec1_6 = soup.find(id='sec1-6')

# Part 2 sources
# We need to extract the sub-contents of sec1-3 and sec1-3-4
# Let's find the paragraphs in sec1-3
sec1_3 = soup.find(id='sec1-3')
data_ingestion_p = ""
data_cleaning_p = ""
if sec1_3:
    # Based on earlier grep, we have h3 tags: 1.3.1. 数据接入汇聚, 1.3.2. 数据清洗
    h3_1 = sec1_3.find(lambda t: t.name == 'h3' and '1.3.1.' in t.text)
    if h3_1:
        p = h3_1.find_next_sibling('p')
        if p: data_ingestion_p = str(p)
    h3_2 = sec1_3.find(lambda t: t.name == 'h3' and '1.3.2.' in t.text)
    if h3_2:
        p = h3_2.find_next_sibling('p')
        if p: data_cleaning_p = str(p)

sec1_3_3 = soup.find(id='sec1-3-3')
ai_req = ""; ai_res = ""; ai_ingest = ""; ai_schema = ""; ai_qc = ""; ai_eval = ""
if sec1_3_3:
    st_req = sec1_3_3.find(lambda t: t.name == 'strong' and '1.3.3.1' in t.text)
    if st_req: ai_req = str(st_req.find_next_sibling('p'))
    st_res = sec1_3_3.find(lambda t: t.name == 'strong' and '1.3.3.2' in t.text)
    if st_res: ai_res = str(st_res.find_next_sibling('p'))
    st_ing = sec1_3_3.find(lambda t: t.name == 'strong' and '1.3.3.3' in t.text)
    if st_ing: ai_ingest = str(st_ing.find_next_sibling('p'))
    st_sch = sec1_3_3.find(lambda t: t.name == 'strong' and '1.3.3.4' in t.text)
    if st_sch: ai_schema = str(st_sch.find_next_sibling('p'))
    st_qc = sec1_3_3.find(lambda t: t.name == 'strong' and '1.3.3.5' in t.text)
    if st_qc: ai_qc = str(st_qc.find_next_sibling('p'))
    st_ev = sec1_3_3.find(lambda t: t.name == 'strong' and '1.3.3.6' in t.text)
    if st_ev: ai_eval = str(st_ev.find_next_sibling('p'))

sec1_3_4 = soup.find(id='sec1-3-4')
db_warehouse_content = ""
if sec1_3_4:
    h2 = sec1_3_4.find('h2')
    if h2: h2.extract()
    db_warehouse_content = get_inner_html(sec1_3_4)

# Part 3 sources
sec1_7 = soup.find(id='sec1-6') # The HTML ID for 1.7 was sec1-6
if not sec1_7 or "1.7" not in sec1_7.text:
    # If id is not sec1-6, find the div containing "1.7. 其他要求"
    h2_7 = soup.find(lambda t: t.name == 'h2' and '1.7.' in t.text)
    if h2_7: sec1_7 = h2_7.parent
    
accept_req = ""; accept_table = ""
if sec1_7:
    sec1_6_1 = sec1_7.find(id='sec1-6-1')
    if sec1_6_1:
        h3 = sec1_6_1.find('h3')
        if h3: h3.extract()
        accept_req = get_inner_html(sec1_6_1)
        sec1_6_1.extract()
    
    # Find table wrapper
    table_wrapper = sec1_7.find(lambda t: t.name == 'div' and t.has_attr('class') and 'overflow-x-auto' in t['class'])
    if table_wrapper:
        accept_table = str(table_wrapper)

# Strip h2/h3 from sources
def strip_header(el):
    if el:
        h = el.find(['h2', 'h3'])
        if h: h.extract()
        return get_inner_html(el)
    return ""

c_1_2_1 = strip_header(sec1_2_1)
c_1_2_2 = strip_header(sec1_2_2)
c_1_2_3 = strip_header(sec1_2_3)
c_1_2_4 = strip_header(sec1_2_4)
c_1_4 = strip_header(sec1_4)
c_1_5 = strip_header(sec1_5)

# Wait, if sec1-6 was actually 1.7, where was 1.6?
sec1_5_actual = soup.find(lambda t: t.name == 'h2' and '1.5.' in t.text)
c_1_5 = strip_header(sec1_5_actual.parent if sec1_5_actual else None)

sec1_6_actual = soup.find(lambda t: t.name == 'h2' and '1.6.' in t.text)
c_1_6 = strip_header(sec1_6_actual.parent if sec1_6_actual else None)

# ================= 2. Build new tree-doc1 =================
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

# ================= 3. Build new doc1-content =================
new_doc1_html = f'''
<section id="doc1-content" class="doc-view space-y-8 hidden">
  <div class="border-b border-slate-100 pb-4">
    <div class="inline-flex items-center space-x-2 px-3 py-1 bg-brand-50 text-brand-700 rounded-full text-sm font-bold mb-3 border border-brand-100">
      <i class="fa-solid fa-file-contract"></i>
      <span>招标文件附件</span>
    </div>
    <h1 class="text-2xl md:text-3xl font-bold text-slate-900 mt-2">数据治理工程招标技术要求</h1>
  </div>
  
  <div id="sec1-1" class="space-y-3 scroll-mt-6">
    {get_inner_html(sec1_1)}
  </div>

  <!-- Part 1 -->
  <div class="space-y-6">
    <h2 class="text-xl md:text-2xl font-extrabold text-slate-900 border-b-2 border-brand-500 pb-2 flex items-center space-x-2">
      <i class="fa-solid fa-book text-brand-600"></i>
      <span>第一部分：数据指南编制</span>
    </h2>
    
    <div id="sec1-2-1" class="bg-blue-50/50 border border-blue-100 p-4 rounded-lg space-y-3 scroll-mt-6">
       <h3 class="text-lg font-bold text-slate-800 mb-1">（一）基础标准与质量指南</h3>
       {c_1_2_1}
       {c_1_4}
    </div>

    <div id="sec1-2-2" class="bg-blue-50/50 border border-blue-100 p-4 rounded-lg space-y-3 scroll-mt-6">
       <h3 class="text-lg font-bold text-slate-800 mb-1">（二）采集接入与共享指南</h3>
       {c_1_2_2}
       {c_1_5}
       {c_1_6}
    </div>
    
    <div id="sec1-2-3" class="bg-blue-50/50 border border-blue-100 p-4 rounded-lg space-y-3 scroll-mt-6">
       <h3 class="text-lg font-bold text-slate-800 mb-1">（三）安全管控与合规指南</h3>
       {c_1_2_3}
    </div>

    <div id="sec1-2-4" class="bg-blue-50/50 border border-blue-100 p-4 rounded-lg space-y-3 scroll-mt-6">
       <h3 class="text-lg font-bold text-slate-800 mb-1">（四）AI治理工具指南</h3>
       {c_1_2_4}
    </div>
  </div>

  <!-- Part 2 -->
  <div class="space-y-6 mt-10">
    <h2 class="text-xl md:text-2xl font-extrabold text-slate-900 border-b-2 border-brand-500 pb-2 flex items-center space-x-2">
      <i class="fa-solid fa-robot text-brand-600"></i>
      <span>第二部分：AI治理工具</span>
    </h2>
    
    <div id="sec1-3-3-1" class="bg-indigo-50/30 border border-indigo-100 p-4 rounded-lg space-y-3 scroll-mt-6">
      <h3 class="text-lg font-bold text-slate-800 mb-1">（一）数据需求及资源盘点</h3>
      {ai_req}
      {ai_res}
    </div>

    <div id="sec1-3-3-2" class="bg-indigo-50/30 border border-indigo-100 p-4 rounded-lg space-y-3 scroll-mt-6">
      <h3 class="text-lg font-bold text-slate-800 mb-1">（二）数据接入与AI自适应导入</h3>
      {data_ingestion_p}
      {ai_ingest}
    </div>

    <div id="sec1-3-3-3" class="bg-indigo-50/30 border border-indigo-100 p-4 rounded-lg space-y-3 scroll-mt-6">
      <h3 class="text-lg font-bold text-slate-800 mb-1">（三）AI质控</h3>
      {data_cleaning_p}
      {ai_qc}
    </div>

    <div id="sec1-3-3-4" class="bg-indigo-50/30 border border-indigo-100 p-4 rounded-lg space-y-3 scroll-mt-6">
      <h3 class="text-lg font-bold text-slate-800 mb-1">（四）AI数仓</h3>
      {db_warehouse_content}
      {ai_schema}
    </div>

    <div id="sec1-3-3-5" class="bg-indigo-50/30 border border-indigo-100 p-4 rounded-lg space-y-3 scroll-mt-6">
      <h3 class="text-lg font-bold text-slate-800 mb-1">（五）数据分级分类和业务考核</h3>
      {ai_eval}
    </div>
  </div>

  <!-- Part 3 -->
  <div class="space-y-6 mt-10">
    <h2 class="text-xl md:text-2xl font-extrabold text-slate-900 border-b-2 border-brand-500 pb-2 flex items-center space-x-2">
      <i class="fa-solid fa-list-check text-brand-600"></i>
      <span>第三部分：验收标准</span>
    </h2>

    <div id="sec1-7-1" class="bg-emerald-50/50 border border-emerald-100 p-4 rounded-lg space-y-3 scroll-mt-6">
      <h3 class="text-lg font-bold text-slate-800 mb-1">（一）基本验收要求</h3>
      {accept_req}
    </div>

    <div id="sec1-7-2" class="space-y-3 scroll-mt-6 mt-4">
      <h3 class="text-lg font-bold text-slate-800 mb-1">（二）项目验收成果表</h3>
      {accept_table}
    </div>
  </div>
</section>
'''

# Replace in original file
old_tree = soup.find(id='tree-doc1')
old_doc1 = soup.find(id='doc1-content')

# Read file as string and replace using regex/string to preserve formatting of other parts
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

import re
text = re.sub(r'<div class="tree-group space-y-1 hidden" id="tree-doc1">.*?(?=<!-- Document 2 Tree Directory -->)', new_tree_html + '\n\n        ', text, flags=re.DOTALL)

text = re.sub(r'<section id="doc1-content" class="doc-view space-y-8 hidden">.*?</section>', new_doc1_html, text, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Success")
