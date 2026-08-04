import codecs
import re

html = codecs.open('old_index.html', 'r', 'utf-16').read()
start = html.find('数据运营业务')
if start != -1:
    print(html[start-300:start+2500])
