import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

# Update rowspans
primary_td = soup.find('td', text=lambda t: t and '初步验收' in t)
if primary_td and primary_td.has_attr('rowspan'):
    primary_td['rowspan'] = '10'

category_td = soup.find('td', text=lambda t: t and '3. 治理过程与成果类' in t)
if category_td and category_td.has_attr('rowspan'):
    category_td['rowspan'] = '3'

# Text replacements
replacements = {
    "《AI治理工具核心功能演示确认单及操作录屏》": "《公路数据采集与接入功能演示确认单及操作录屏》",
    "《湖北省公路全局数据资源资产目录》": "《公路数据资源盘点台账》",
    "《湖北公路智能治理知识基座配置库》": "《公路标准数据仓配置库和ER图》",
    "《公路数据资产质量体检报告》及《数据溯源日志》": "《公路数据质量稽查与评估报告》",
    "《资产分级合规及按组织架构的流转考核实测报告》": "《公路数据共享发布与效能考核实测报告》"
}

for old_text, new_text in replacements.items():
    td = soup.find('td', text=lambda t: t and old_text in t)
    if td:
        # We replace the text in the td. Note that we might just want to set the text directly,
        # but the original had no other tags so replacing is fine.
        td.string = new_text

# Delete rows
rows_to_delete = ["《全链路数仓模型设计蓝图及ER图》", "《数据资产贡献与处室效能考核月报》"]
for target_text in rows_to_delete:
    td = soup.find('td', text=lambda t: t and target_text in t)
    if td:
        # Find parent tr and decompose
        tr = td.find_parent('tr')
        if tr:
            tr.decompose()

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Updated table texts and rowspans.")
