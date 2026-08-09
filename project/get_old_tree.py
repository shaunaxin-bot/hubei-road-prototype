import os
from bs4 import BeautifulSoup
file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('<div class="tree-group space-y-1 hidden" id="tree-doc1">')
end_idx = text.find('<!-- Document 2 Tree Directory -->', start_idx)
if start_idx != -1 and end_idx != -1:
    print(text[start_idx:end_idx].strip())
else:
    print("Not found")
