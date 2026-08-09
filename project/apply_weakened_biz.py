import os
from bs4 import BeautifulSoup
import re

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

# 1. Update the concise requirements in the table
deliverable_mapping = {
    "《公路数据采集与接入功能演示确认单及操作录屏》": "初验必备：验证数据自动归集能力",
    "《公路数据共享发布与效能考核实测报告》": "初验必备：验证数据共享流转实效",
    "《公路数据资源盘点台账》": "初验必备：提交数据资源资产台账",
    "《公路标准数据仓配置库和ER图》": "初验必备：提交数仓模型及ER图",
    "《公路数据质量稽查与评估报告》": "初验必备：提交数据质量稽查清单"
}

table_container = soup.find(id='sec1-7-2')
if table_container:
    tbody = table_container.find('tbody')
    if tbody:
        rows = tbody.find_all('tr')
        for row in rows:
            tds = row.find_all('td')
            if len(tds) >= 3:
                deliverable = tds[-3].get_text(strip=True)
                for key, new_req in deliverable_mapping.items():
                    if key in deliverable:
                        tds[-1].string = new_req

# 2. Weaken the business scoring section
tab1 = soup.find(id='biz-tab-1')
if tab1:
    tab_html = str(tab1)
    # Replacements
    replacements = {
        "数据产品挂牌/交易凭证，或数据资产评估/确权/运营能力相关证明材料的": "数据治理成果或数据应用服务相关证明材料的",
        "包含“数据采集 + 数据治理 + 数据资产确权/入表登记”": "包含“数据采集 + 数据治理 + 数据应用平台建设”",
        "第三方机构出具的数据资产登记/入表凭证": "第三方机构出具的数据治理或评估验收凭证",
        "交通基础设施节点管控与数据运营平台业绩": "公路交通综合业务与数据运营平台业绩",
        "交通基础设施节点智能化管控/数据运营平台系统": "公路交通综合业务管理/数据运营平台系统",
        "精准包含以下数据治理与资产类关键词（限定为：“数据采集”、“数据标准管理”、“数据质量管理”、“数据资产管理”、“数据标注”、“数据治理”、“数据资源目录”）": "精准包含以下数据治理类关键词（限定为：“数据集成”、“数据标准管理”、“数据质量管理”、“数据底座”、“数据分析”、“数据治理”、“数据资源目录”）",
        "具有“数据资产管理师”以及“高级软件工程师或系统架构设计师”": "具有“数据治理工程师”或“CDMP（数据管理专业人士）”以及“高级软件工程师或系统架构设计师”",
        "具备数据资产管理师、数据库工程师、高级软件工程师": "具备数据治理工程师、CDMP、数据库工程师、高级软件工程师"
    }
    
    for old, new in replacements.items():
        tab_html = tab_html.replace(old, new)
    
    new_tab1 = BeautifulSoup(tab_html, 'html.parser')
    tab1.replace_with(new_tab1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Modifications applied.")
