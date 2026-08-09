import os
import re
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')
doc1 = soup.find(id='doc1-content')

if doc1:
    def clean_title(title_text):
        return re.sub(r'^\d+(\.\d+)+\.?\s*', '', title_text.strip())

    # Replace specific top-level guideline titles
    for h4 in doc1.find_all('h4'):
        if re.match(r'^1\.2\.\d+', h4.get_text(strip=True)):
            h4.string = clean_title(h4.get_text(strip=True))

    # --- 1. 基础标准与质量指南 ---
    sec1_2_1 = doc1.find(id='sec1-2-1')
    if sec1_2_1:
        # Find all cards that start with sec1-4-
        cards = sec1_2_1.find_all('div', id=re.compile(r'^sec1-4-\d+'))
        if cards:
            transition = soup.new_tag('p')
            transition['class'] = 'text-slate-700 font-bold mt-4 mb-3 border-l-4 border-brand-500 pl-3'
            transition.string = '该指南的落地实施重点包含以下技术建设工作：'
            cards[0].insert_before(transition)

            for idx, card in enumerate(cards, 1):
                # Remove styling
                card['class'] = 'mt-3 space-y-1'
                title_elem = card.find('strong')
                if title_elem:
                    old_text = title_elem.get_text(strip=True)
                    title_elem.string = f"{idx}. {clean_title(old_text)}"

    # --- 2. 采集接入与共享指南 ---
    sec1_2_2 = doc1.find(id='sec1-2-2')
    if sec1_2_2:
        cards = sec1_2_2.find_all('div', id=re.compile(r'^sec1-[56]'))
        if cards:
            transition = soup.new_tag('p')
            transition['class'] = 'text-slate-700 font-bold mt-4 mb-3 border-l-4 border-brand-500 pl-3'
            transition.string = '该指南在工程建设中，重点涵盖以下资源的构建与接口对接：'
            cards[0].insert_before(transition)

            for idx, card in enumerate(cards, 1):
                card['class'] = 'mt-3 space-y-1'
                title_elem = card.find(['h4', 'strong'])
                if title_elem:
                    old_text = title_elem.get_text(strip=True)
                    title_elem.string = f"{idx}. {clean_title(old_text)}"
                    if title_elem.name == 'h4':
                        title_elem.name = 'strong'
                        title_elem['class'] = 'text-slate-800 block mb-1 font-bold'

    # --- 3. AI治理工具 ---
    for i in range(1, 6):
        sec = doc1.find(id=f'sec1-3-3-{i}')
        if sec:
            h4_elems = sec.find_all('h4')
            for h4_idx, h4 in enumerate(h4_elems, 1):
                old_text = h4.get_text(strip=True)
                h4.string = f"{h4_idx}. {clean_title(old_text)}"
                
            h5_elems = sec.find_all('h5')
            for h5_idx, h5 in enumerate(h5_elems, 1):
                old_text = h5.get_text(strip=True)
                h5.string = f"（{h5_idx}）{clean_title(old_text)}"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Formatting successful.")
else:
    print("doc1-content not found.")
