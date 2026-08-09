import os
import re
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

# 1. Remove button 2
btn2 = soup.find(id='btn-biz-tab-2')
if btn2:
    btn2.decompose()

# 2. Rename button 3 to button 2
btn3 = soup.find(id='btn-biz-tab-3')
if btn3:
    btn3['id'] = 'btn-biz-tab-2'
    btn3['onclick'] = "switchBizTab('biz-tab-2')"
    btn3.string = '选项二（基础版）'

# 3. Remove content tab 2
tab2 = soup.find(id='biz-tab-2')
if tab2:
    tab2.decompose()

# 4. Rename content tab 3 to tab 2
tab3 = soup.find(id='biz-tab-3')
if tab3:
    tab3['id'] = 'biz-tab-2'

# 5. Fix JS switchBizTab function
script_tag = soup.find_all('script')[-1]
if script_tag and script_tag.string:
    js_code = script_tag.string
    js_code = js_code.replace("['biz-tab-1', 'biz-tab-2', 'biz-tab-3']", "['biz-tab-1', 'biz-tab-2']")
    script_tag.string = js_code

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Option 2 removed and Option 3 renamed to Option 2.")
