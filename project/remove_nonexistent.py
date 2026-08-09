import os
import re

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Specifically fix the table references
replacements = {
    '1.3.3.1（需求调研）至 1.3.3.10（知识库管理）十项详细要求': '（需求调研）至（知识库管理）详细要求',
    '1.3.3.2（智能资源盘点）': '（智能资源盘点）',
    '1.3.3.4（智能数据标准设计）': '（智能数据标准设计）',
    '1.3.3.5（智能数仓模型设计）': '（智能数仓模型设计）',
    '1.3.3.6（智能数据处理）': '（智能数据处理）',
    '1.3.3.8（主动质量控制）': '（主动质量控制）',
    '1.3.3.9（数据资产安全管理）': '（数据资产安全管理）',
    '1.3.3.10（知识库管理）': '（知识库管理）'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Success")
