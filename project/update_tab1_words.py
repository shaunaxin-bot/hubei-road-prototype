import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace specific objective phrasing using string replacement

replacements = {
    "（提升：要求双证绑定，过滤普通集成商）": "（提升：增加“专精特新”要求，综合考察企业创新与专业化能力）",
    "（降低：等级要求从基础版的5/4级降至3级，以确保自身达标）": "（降低：等级要求调整为3级，拓宽符合条件的优质供应商范围）",
    "（提升：要求三体系闭环，确保规范化运营门槛）": "（提升：要求三大体系完整覆盖，进一步强化规范化运营标准）",
    "（提升：核心卡点，要求有数据资产交易所挂牌或许可运营记录）": "（提升：重点要求具备数据资产交易所挂牌或相关运营记录）",
    "（提升：楚云系列平台精准对标，排斥纯代理商）": "（提升：强调“智能化管控”与“数据运营平台”研发能力，注重自主创新）",
    "（提升：词库精准封闭，剔除通用业务系统词汇）": "（提升：限定软著涵盖特定核心业务词汇，聚焦数据治理专业度）",
    "（降低：去除了“电子信息行业联合会登记”的严苛限定，采用通用高级资质，保证自身得分）": "（降低：取消“电子信息行业联合会登记”限制，放宽高级别资质认定范围）",
    "（提升：强排他卡点，将“数据资产管理师”设为必选项）": "（提升：新增“数据资产管理师”为必要条件，突出新型资产管理需求）",
    "（提升：设定专业资质及高级技术职称壁垒）": "（提升：对团队成员专业资质与高级技术职称提出更严格标准）"
}

new_text = text
for old, new in replacements.items():
    new_text = new_text.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Replaced unobjective words in Option 1.")
