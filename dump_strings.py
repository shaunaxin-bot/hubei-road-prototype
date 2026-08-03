import re
import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    text = f.read()

m = re.search(r'<script>\s*\(\(\)=>{var [a-zA-Z0-9_]+=Object\.create;.*?}\)\(\);\s*</script>', text, re.DOTALL)
if m:
    bundle_text = m.group(0)
    bundle_text = bundle_text.encode('utf-8').decode('unicode_escape', 'ignore')
    
    matches = re.findall(r'"([^"]*[\u4e00-\u9fa5]+[^"]*)"', bundle_text)
    for match in sorted(set(matches)):
        print(match)
else:
    print('Bundle not found!')
