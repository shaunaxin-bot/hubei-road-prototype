import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace space-x-2 with space-x-0 or remove it
text = text.replace('<div class="flex space-x-2 border-b border-slate-200 mt-3">', '<div class="flex space-x-0 border-b border-slate-200 mt-3">')

# Replace px-4 with px-3 for btn-biz-tab-1
text = text.replace('class="px-4 py-2 font-bold text-brand-600', 'class="px-3 py-2 font-bold text-brand-600')
# Wait, it doesn't have font-bold anymore because I removed it! Let's just use regex or replace specifically around the id
import re
text = re.sub(r'class="px-4([^>]*id="btn-biz-tab-1")', r'class="px-3\1', text)
text = re.sub(r'class="px-4([^>]*id="btn-biz-tab-2")', r'class="px-3\1', text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Reduced spacing between biz tabs.")
