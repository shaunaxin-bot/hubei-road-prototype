import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace space-y-8 with empty string for all doc-content sections
text = text.replace('<section class="doc-view space-y-8 hidden" id="doc1-content">', '<section class="doc-view hidden" id="doc1-content">')
text = text.replace('<section class="doc-view space-y-8 hidden" id="doc2-content">', '<section class="doc-view hidden" id="doc2-content">')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Removed extra vertical space for doc1 and doc2.")
