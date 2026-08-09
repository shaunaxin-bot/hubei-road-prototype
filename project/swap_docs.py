import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def swap_blocks(content, start_tag1, end_tag1, start_tag2, end_tag2):
    i1 = content.find(start_tag1)
    e1 = content.find(end_tag1, i1) + len(end_tag1)
    block1 = content[i1:e1]
    
    i2 = content.find(start_tag2)
    e2 = content.find(end_tag2, i2) + len(end_tag2)
    block2 = content[i2:e2]
    
    # We assume block1 comes before block2
    if i1 < i2:
        res = content[:i1] + block2 + content[e1:i2] + block1 + content[e2:]
    else:
        res = content[:i2] + block1 + content[e2:i1] + block2 + content[e1:]
    return res

# 1. Swap Tabs
b1_tab_s = '<button id="tab-doc1"'
b1_tab_e = '<span>招标技术要求</span>\n        </button>'
b2_tab_s = '<button id="tab-doc2"'
b2_tab_e = '<span>实施方案</span>\n        </button>'
content = swap_blocks(content, b1_tab_s, b1_tab_e, b2_tab_s, b2_tab_e)

# Swap tab active classes
content = content.replace('id="tab-doc2" onclick="switchDoc(\'doc2\')" class="nav-tab px-3.5 py-1.5 rounded-lg text-base md:text-base font-medium transition-all duration-200 text-white/80 hover:text-white hover:bg-white/10 flex items-center space-x-1.5"',
                          'id="tab-doc2" onclick="switchDoc(\'doc2\')" class="nav-tab px-3.5 py-1.5 rounded-lg text-base md:text-base font-medium transition-all duration-200 bg-white text-brand-700 shadow-sm font-bold flex items-center space-x-1.5"')
content = content.replace('id="tab-doc1" onclick="switchDoc(\'doc1\')" class="nav-tab px-3.5 py-1.5 rounded-lg text-base md:text-base font-medium transition-all duration-200 bg-white text-brand-700 shadow-sm font-bold flex items-center space-x-1.5"',
                          'id="tab-doc1" onclick="switchDoc(\'doc1\')" class="nav-tab px-3.5 py-1.5 rounded-lg text-base md:text-base font-medium transition-all duration-200 text-white/80 hover:text-white hover:bg-white/10 flex items-center space-x-1.5"')

# 2. Swap Sidebar Trees
b1_tree_s = '<!-- Document 1 Tree Directory -->'
b1_tree_e = '<!-- Document 2 Tree Directory -->'
# find exact end of tree1 which is just before tree2
b1_tree_e_idx = content.find(b1_tree_e)
block1 = content[content.find(b1_tree_s):b1_tree_e_idx]

b2_tree_s = '<!-- Document 2 Tree Directory -->'
b2_tree_e = '<!-- Document 3 Tree Directory -->'
b2_tree_e_idx = content.find(b2_tree_e)
block2 = content[content.find(b2_tree_s):b2_tree_e_idx]

content = content[:content.find(b1_tree_s)] + block2 + block1 + content[b2_tree_e_idx:]

# Swap sidebar hidden classes
content = content.replace('<div class="tree-group space-y-1" id="tree-doc1">', '<div class="tree-group space-y-1 hidden" id="tree-doc1">')
content = content.replace('<div class="tree-group space-y-1 hidden" id="tree-doc2">', '<div class="tree-group space-y-1" id="tree-doc2">')

# 3. Swap Content Sections
b1_cont_s = '<!-- Document 1 Content -->'
b1_cont_e = '<!-- Document 2 Content -->'
b1_cont_e_idx = content.find(b1_cont_e)
block1 = content[content.find(b1_cont_s):b1_cont_e_idx]

b2_cont_s = '<!-- Document 2 Content -->'
b2_cont_e = '<!-- Document 3 Content -->'
b2_cont_e_idx = content.find(b2_cont_e)
block2 = content[content.find(b2_cont_s):b2_cont_e_idx]

content = content[:content.find(b1_cont_s)] + block2 + block1 + content[b2_cont_e_idx:]

# Swap content hidden classes
content = content.replace('<section id="doc1-content" class="doc-view space-y-8">', '<section id="doc1-content" class="doc-view space-y-8 hidden">')
content = content.replace('<section id="doc2-content" class="doc-view space-y-8 hidden">', '<section id="doc2-content" class="doc-view space-y-8">')

# 4. Swap default currentDoc in JS
content = content.replace("let currentDoc = 'doc1';", "let currentDoc = 'doc2';")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
