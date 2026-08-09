import os
import re

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace space-y-8 with space-y-0 for doc3-content
text = text.replace('<section class="doc-view space-y-8 hidden" id="doc3-content">', '<section class="doc-view hidden" id="doc3-content">')
# Also remove any space-y-* in doc3-content if it was something else just in case.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Removed extra vertical space.")
