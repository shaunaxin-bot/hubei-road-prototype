import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all 1.1.1.x with 1.3.3.x inside the specific table section.
# I will just replace "1.1.1." with "1.3.3." globally since there are no other 1.1.1.x in the file.
content = content.replace('1.1.1.', '1.3.3.')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Success")
