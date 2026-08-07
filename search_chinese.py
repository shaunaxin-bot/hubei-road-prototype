import sys
import io
import re

with open('index_good.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

with io.open('search_out.txt', 'w', encoding='utf-8') as out:
    chinese_chars = re.findall(r'[\u4e00-\u9fff]+', text)
    if chinese_chars:
        out.write(f'Found {len(chinese_chars)} blocks of Chinese characters.\n')
        # Print a few samples
        for i, block in enumerate(chinese_chars[:20]):
            out.write(f'Sample {i}: {block}\n')
    else:
        out.write('NO Chinese characters found at all!\n')
