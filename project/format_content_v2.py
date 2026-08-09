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

    # --- 1. 基础标准与质量指南 ---
    sec1_2_1 = doc1.find(id='sec1-2-1')
    if sec1_2_1:
        # Strip 1.2.1 from the guideline title
        h4_guideline = sec1_2_1.find('h4')
        if h4_guideline:
            h4_guideline.string = clean_title(h4_guideline.get_text())

        # Find the inner container for the database parts
        inner_container = sec1_2_1.find('div', class_=re.compile('space-y-2'))
        if inner_container:
            # Add transition before the inner container
            transition = soup.new_tag('p')
            transition['class'] = 'text-slate-700 font-bold mt-4 mb-3 border-l-4 border-brand-500 pl-3'
            transition.string = '该指南的落地实施重点包含以下技术建设工作：'
            inner_container.insert_before(transition)

            # Find all cards
            cards = inner_container.find_all('div', recursive=False)
            for idx, card in enumerate(cards, 1):
                # Flatten styling
                card['class'] = 'mt-3 space-y-1'
                title_strong = card.find('strong')
                if title_strong:
                    old_text = title_strong.get_text(strip=True)
                    title_strong.string = f"{idx}. {clean_title(old_text)}"

    # --- 2. 采集接入与共享指南 ---
    sec1_2_2 = doc1.find(id='sec1-2-2')
    if sec1_2_2:
        h4_guideline = sec1_2_2.find('h4')
        if h4_guideline:
            h4_guideline.string = clean_title(h4_guideline.get_text())

        # In sec1-2-2, the original structure didn't have inner cards in the text we saw!
        # Wait, let's look at the old doc1 structure. In the old doc1 structure, 1.5 and 1.6 were outside 1.2.
        # But in my previous massive restructure script, did I put 1.5 and 1.6 inside sec1_2_2?
        # Let's check if there are inner cards in sec1_2_2.
        # It turns out in the previous massive script, I appended sec1-5 and sec1-6 HTML inside sec1-2-2!
        # Let's find those elements inside sec1_2_2. They might have 'id="sec1-5"' etc.
        # Actually, let's just find any divs that have the class "bg-blue-50/50" or similar that act as cards.
        cards = sec1_2_2.find_all('div', id=re.compile(r'sec1-[56]'))
        if cards:
            transition = soup.new_tag('p')
            transition['class'] = 'text-slate-700 font-bold mt-4 mb-3 border-l-4 border-brand-500 pl-3'
            transition.string = '该指南在工程建设中，重点涵盖以下资源的构建与接口对接：'
            cards[0].insert_before(transition)
            for idx, card in enumerate(cards, 1):
                card['class'] = 'mt-3 space-y-1'
                # Find h4 or strong for title
                title_elem = card.find(['h4', 'strong'])
                if title_elem:
                    old_text = title_elem.get_text(strip=True)
                    title_elem.string = f"{idx}. {clean_title(old_text)}"
                    if title_elem.name == 'h4':
                        title_elem.name = 'strong'
                        title_elem['class'] = 'text-slate-800 block mb-1 font-bold'

    # --- Clean up other sections in part 1 ---
    for i in [3, 4]:
        sec = doc1.find(id=f'sec1-2-{i}')
        if sec:
            h4 = sec.find('h4')
            if h4:
                h4.string = clean_title(h4.get_text())

    # --- 3. AI治理工具 ---
    # Find all h4 inside Part 2 and rename them 1. 2. 3.
    # The sections are sec1-3-3-1, sec1-3-3-2, etc.
    for i in range(1, 6):
        sec = doc1.find(id=f'sec1-3-3-{i}')
        if sec:
            # We don't have cards inside here, we just have paragraphs in some of them, and maybe inner divs in others.
            # If there are sub-sections (h4 or h5), renumber them.
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
