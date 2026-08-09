import os
import re

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Use regex to remove all instances of （提升：...） and （降低：...）
# Also need to handle cases where there might be a space, but my script didn't add spaces.
new_text = re.sub(r'（(?:提升|降低)：.*?）', '', text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Removed all bracketed explanations.")
