import os
import re
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

doc1 = soup.find(id='doc1-content')

if doc1:
    # -----------------------------
    # Helper to clean up titles
    # -----------------------------
    def clean_title(title_text):
        # Remove patterns like "1.4.1. " or "1.3.3.1. "
        cleaned = re.sub(r'^\d+(\.\d+)+\.?\s*', '', title_text.strip())
        return cleaned

    # -----------------------------
    # 1. 基础标准与质量指南 (sec1-2-1)
    # -----------------------------
    sec1_2_1 = doc1.find(id='sec1-2-1')
    if sec1_2_1:
        # Find the guideline text (which is just plain text or p tags after the h3)
        # We need to restructure this section.
        # Currently, it has the h3, then a p tag (the guideline text), then cards for 1.4.1, 1.4.2, etc.
        
        # Add transition sentence
        transition = soup.new_tag('p')
        transition['class'] = 'text-slate-700 font-bold mt-4 mb-3 border-l-4 border-brand-500 pl-3'
        transition.string = '该指南的落地实施重点包含以下技术建设工作：'
        
        # Find where to insert it: after the guideline text, before the first card.
        # Let's find the first card (div with bg-white border border-slate-100/60 rounded-xl) inside sec1_2_1
        cards = sec1_2_1.find_all('div', class_=re.compile(r'bg-white.*border-slate-100/60.*rounded-xl'))
        
        if cards:
            cards[0].insert_before(transition)
            
            # Flatten the cards and renumber them
            for idx, card in enumerate(cards, 1):
                # Remove card styling
                card['class'] = 'mt-4 space-y-2'
                
                # Update title
                title_h4 = card.find('h4')
                if title_h4:
                    old_text = title_h4.get_text(strip=True)
                    new_text = f"{idx}. {clean_title(old_text)}"
                    
                    title_span = soup.new_tag('span')
                    title_span.string = new_text
                    title_h4.clear()
                    title_h4.append(title_span)
                    title_h4['class'] = 'text-base font-bold text-slate-800'

    # -----------------------------
    # 2. 采集接入与共享指南 (sec1-2-2)
    # -----------------------------
    sec1_2_2 = doc1.find(id='sec1-2-2')
    if sec1_2_2:
        transition = soup.new_tag('p')
        transition['class'] = 'text-slate-700 font-bold mt-4 mb-3 border-l-4 border-brand-500 pl-3'
        transition.string = '该指南在工程建设中，重点涵盖以下资源的构建与接口对接：'
        
        cards = sec1_2_2.find_all('div', class_=re.compile(r'bg-white.*border-slate-100/60.*rounded-xl'))
        if cards:
            cards[0].insert_before(transition)
            for idx, card in enumerate(cards, 1):
                card['class'] = 'mt-4 space-y-2'
                title_h4 = card.find('h4')
                if title_h4:
                    old_text = title_h4.get_text(strip=True)
                    new_text = f"{idx}. {clean_title(old_text)}"
                    title_span = soup.new_tag('span')
                    title_span.string = new_text
                    title_h4.clear()
                    title_h4.append(title_span)
                    title_h4['class'] = 'text-base font-bold text-slate-800'
                    
                # In sec1-2-2, there are sub-sub items that might have (1) style, but we'll leave their current bullet formatting or adjust if they have numbering.

    # -----------------------------
    # 3. AI治理工具 (Part 2)
    # -----------------------------
    # Clean up any h4 or h5 inside part 2 that have old numbers
    for i in range(1, 6):
        ai_sec = doc1.find(id=f'sec1-3-3-{i}')
        if ai_sec:
            # The sections themselves are "（一）", "（二）" - these don't need changing since they are the top level of this part.
            # But the inner cards need flattening and numbering 1, 2, 3
            cards = ai_sec.find_all('div', class_=re.compile(r'bg-white.*border-slate-100/60.*rounded-xl'))
            
            # Since AI sections are often a list of capabilities, we flatten them and number them 1, 2, 3
            for idx, card in enumerate(cards, 1):
                card['class'] = 'mt-4 space-y-2'
                title_h4 = card.find('h4')
                if title_h4:
                    old_text = title_h4.get_text(strip=True)
                    new_text = f"{idx}. {clean_title(old_text)}"
                    title_span = soup.new_tag('span')
                    title_span.string = new_text
                    title_h4.clear()
                    title_h4.append(title_span)
                    title_h4['class'] = 'text-base font-bold text-slate-800'
                    
                # Look for sub-items (h5 or strong tags that might act as subheadings)
                # and number them (1), (2), (3) if they had numbers like 1.3.4.1
                sub_titles = card.find_all('h5')
                for sub_idx, sub in enumerate(sub_titles, 1):
                    old_sub = sub.get_text(strip=True)
                    # If it had a number, replace it. If not, just prepend (1)
                    if re.match(r'^\d+(\.\d+)+\.?\s*', old_sub):
                        new_sub = f"（{sub_idx}）{clean_title(old_sub)}"
                        sub.string = new_sub
                        sub['class'] = 'text-sm font-bold text-slate-700 mt-2'

    with open(file_path, 'w', encoding='utf-8') as f:
        # Use formatter to avoid messing up unicode characters
        f.write(str(soup))
    print("UI and numbering cleanup successful.")
else:
    print("Error: doc1-content not found.")
