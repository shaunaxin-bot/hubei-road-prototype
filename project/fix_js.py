import os
import re
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

scripts = soup.find_all('script')

# Find the tailwind script and remove inner content
tailwind_script = None
for s in scripts:
    if s.has_attr('src') and 'tailwindcss' in s['src']:
        tailwind_script = s
        break

js_code = ""
if tailwind_script and tailwind_script.string:
    js_code = tailwind_script.string
    tailwind_script.string = ""  # clear it

# Find the last script (where our own functions are)
last_script = None
for s in reversed(scripts):
    if not s.has_attr('src'):
        last_script = s
        break

if last_script and js_code:
    last_script.append(js_code)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Fixed JS injection")
else:
    print("Could not find the scripts properly")
