import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

replacements = [
    {
        "search": "（对应：总体要求）",
        "replace": "（包含：（一）数据采集与接入 至 （五）数据共享与发布 总体要求）"
    },
    {
        "search": "（需求调研）至（知识库管理）详细要求",
        "replace": "（一）数据采集与接入 至 （五）数据共享与发布 详细要求"
    },
    {
        "search": "（按组织架构的场景化资产分级合规和流转考核 - 数据找人）",
        "replace": "（对应：（五）数据共享与发布 中的自动分级与匹配流转）"
    },
    {
        "search": "（智能资源盘点）",
        "replace": "（对应：（二）数据资源盘点）"
    },
    {
        "search": "（智能数据标准设计）<br/>（数据资产安全管理）<br/>（知识库管理）",
        "replace": "（对应：（三）标准数据仓建设 及 （五）数据共享与发布中的安全底线）"
    },
    {
        "search": "（智能数仓模型设计）",
        "replace": "（对应：（三）标准数据仓建设）"
    },
    {
        "search": "（智能数据处理）<br/>（主动质量控制）",
        "replace": "（对应：（四）数据质量稽查与评估）"
    },
    {
        "search": "（按组织架构自动生成用于评价各处室的报表 - 管运营）",
        "replace": "（对应：（四）数据质量稽查与评估 及 （五）数据共享与发布 中的整体效能考核）"
    }
]

# Manual replacements for specific text
for item in replacements:
    text = text.replace(item["search"], item["replace"])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated acceptance table references.")
