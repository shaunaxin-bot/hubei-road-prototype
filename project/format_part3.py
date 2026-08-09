import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

# 1. Update table header
th_elems = soup.find_all('th')
for th in th_elems:
    if th.get_text() == '评分标准（极高排他性用词与组合约束）':
        th.string = '评分标准'

# 2. Add IDs to the table rows in sec3-1
sec3_1 = soup.find(id='sec3-1')
if sec3_1:
    trs = sec3_1.find_all('tr')
    # The first row with rowspan is "一、企业综合实力"
    # To reliably add IDs, we can check the td content
    for tr in trs:
        td = tr.find('td')
        if td:
            text_val = td.get_text(strip=True).replace('\n', '')
            if '一、企业综合实力' in text_val:
                tr['id'] = 'sec3-1-1'
                tr['class'] = tr.get('class', []) + ['scroll-mt-6']
            elif '二、类似案例' in text_val:
                tr['id'] = 'sec3-1-2'
                tr['class'] = tr.get('class', []) + ['scroll-mt-6']
            elif '三、技术实力' in text_val:
                tr['id'] = 'sec3-1-3'
                tr['class'] = tr.get('class', []) + ['scroll-mt-6']
            elif '四、项目团队' in text_val:
                tr['id'] = 'sec3-1-4'
                tr['class'] = tr.get('class', []) + ['scroll-mt-6']

# 3. Modify sidebar menu
tree_doc3 = soup.find(id='tree-doc3')
if tree_doc3:
    # Find the old single link for 商务评分标准
    old_link = None
    for a in tree_doc3.find_all('a', recursive=False):
        if '商务评分标准' in a.get_text():
            old_link = a
            break
            
    if old_link:
        new_menu_html = """
        <div class="bg-white rounded-lg p-1.5 border border-slate-100/60 shadow-xs space-y-0.5 mb-1">
            <div class="flex items-center justify-between p-1 rounded-md hover:bg-slate-50 cursor-pointer text-slate-800 font-bold" onclick="toggleAccordion('acc-doc3-biz')">
                <span class="flex items-center space-x-2 truncate">
                    <i class="fa-solid fa-caret-down text-slate-400 text-sm transition-transform transform" id="acc-doc3-biz-icon"></i>
                    <i class="fa-solid fa-scale-balanced text-amber-600 text-sm shrink-0 w-4 text-center"></i>
                    <span class="text-sm truncate">商务评分标准</span>
                </span>
            </div>
            <div class="pl-2 space-y-0.5 border-l border-brand-100 ml-1.5 pt-0.5" id="acc-doc3-biz">
                <a class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700" href="#sec3-1-1"><span class="truncate">一、企业综合实力</span></a>
                <a class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700" href="#sec3-1-2"><span class="truncate">二、类似案例</span></a>
                <a class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700" href="#sec3-1-3"><span class="truncate">三、技术实力</span></a>
                <a class="dir-item flex items-center space-x-2 py-1 px-1.5 rounded-md text-slate-600 text-sm hover:text-brand-700" href="#sec3-1-4"><span class="truncate">四、项目团队</span></a>
            </div>
        </div>
        """
        new_menu = BeautifulSoup(new_menu_html, 'html.parser')
        old_link.replace_with(new_menu.div)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Done.")
