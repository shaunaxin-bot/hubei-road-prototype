import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

replacements = {
    "（包含：（一）数据采集与接入 至 （五）数据共享与发布 总体要求）": "（包含：（一）数据采集与接入、（二）数据资源盘点、（三）标准数据仓建设、（四）数据质量稽查与评估、（五）数据共享与发布）",
    "（一）数据采集与接入 至 （五）数据共享与发布 详细要求": "（包含：（一）数据采集与接入、（二）数据资源盘点、（三）标准数据仓建设、（四）数据质量稽查与评估、（五）数据共享与发布）",
    "（对应：（五）数据共享与发布 中的自动分级与匹配流转）": "（对应：（五）数据共享与发布）",
    "（对应：（三）标准数据仓建设 及 （五）数据共享与发布中的安全底线）": "（对应：（三）标准数据仓建设）"
}

# Apply the text replacements inside span tags for safety
spans = soup.find_all('span', class_='font-normal')
for span in spans:
    span_text = span.get_text()
    for old, new in replacements.items():
        if old in span_text:
            # We recreate the span text
            span.string = span_text.replace(old, new)
            break

# Also, there's a specific fix needed for row 7 which contains:
# <a href="#sec1-5">1. 数据资源目录</a> 章节<br/>及 <a href="#sec1-3-3">第二部分：AI治理工具</a> 项下：<br/><span class="font-normal">（对应：（二）数据资源盘点）</span>
# I want to change it to just <a href="#sec1-3-3">第二部分：AI治理工具</a> 章节下详细要求：<br/><span class="font-normal">（对应：（二）数据资源盘点）</span>

tds = soup.find_all('td')
for td in tds:
    if '1. 数据资源目录' in str(td) and '第二部分：AI治理工具' in str(td) and '（对应：（二）数据资源盘点）' in str(td):
        # We replace the content of this specific td
        td.clear()
        
        a_tag = soup.new_tag('a', href='#sec1-3-3', **{'class': 'text-brand-600 hover:underline'})
        a_tag.string = "第二部分：AI治理工具"
        td.append(a_tag)
        
        td.append(" 章节下详细要求：")
        td.append(soup.new_tag('br'))
        
        span_tag = soup.new_tag('span', **{'class': 'font-normal'})
        span_tag.string = "（对应：（二）数据资源盘点）"
        td.append(span_tag)

# Another fix: ensure "章节下详细编号：" or "功能补充要求：" becomes " 章节" or " 章节下详细要求："
# Let's just fix "章节下详细编号："
for td in tds:
    content_str = str(td)
    if '章节下详细编号：' in content_str:
        new_content = content_str.replace('章节下详细编号：', '章节')
        td_new = BeautifulSoup(new_content, 'html.parser').td
        td.replace_with(td_new)
    if '功能补充要求：' in content_str:
        new_content = content_str.replace('功能补充要求：', '章节')
        td_new = BeautifulSoup(new_content, 'html.parser').td
        td.replace_with(td_new)
    if '项下：' in content_str:
        new_content = content_str.replace('项下：', '章节')
        td_new = BeautifulSoup(new_content, 'html.parser').td
        td.replace_with(td_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Cleaned up cross-reference texts.")
