import os
import re
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

sec3_1 = soup.find(id='sec3-1')
if sec3_1:
    table = sec3_1.find('table')
    if table:
        new_table_html = """
<table class="w-full text-left text-base border-collapse">
<thead class="border border-slate-200">
<tr class="bg-indigo-50/80 text-indigo-900 font-bold border-b-2 border-indigo-200 border-x border-x-indigo-100">
<th class="p-2.5 border border-slate-200 w-28 text-center">评审维度</th>
<th class="p-2.5 border border-slate-200">评分标准（极高排他性用词与组合约束）</th>
<th class="p-2.5 border border-slate-200 w-72">设卡与排他逻辑说明（为何其它单位拿不上分）</th>
</tr>
</thead>
<tbody class="divide-y divide-slate-200 text-slate-600">

<!-- Dimension 1: 企业综合实力 -->
<tr class="hover:bg-indigo-50/40 transition-colors">
<td class="p-3 font-bold text-brand-800 bg-blue-50/40 border border-slate-200 align-top text-center align-middle" rowspan="4">一、企业<br/>综合实力</td>
<td class="p-2.5 border border-slate-200"><strong class="font-medium text-slate-800">1. 高企与专精特新组合：</strong>投标人同时具有国家高新技术企业证书及“专精特新”中小企业认定的，予以加分；仅具备其中一项的适当加分，均不具备不加分。</td>
<td class="p-2.5 border border-slate-200 text-sm text-rose-700 bg-rose-50/20">双证绑定：直接过滤掉仅有高企而无“专精特新”认定的普通集成商或中介机构。</td>
</tr>
<tr class="hover:bg-indigo-50/40 transition-colors">
<td class="p-2.5 border border-slate-200"><strong class="font-medium text-slate-800">2. 数据管理能力成熟度（DCMM）：</strong>投标人具有 DCMM 数据管理能力成熟度（乙方）3级及以上证书的，予以加分；2级适当加分；其余不加分。</td>
<td class="p-2.5 border border-slate-200 text-sm text-rose-700 bg-rose-50/20">DCMM硬性门槛：绝大多数传统施工单位及普通软件公司未取得DCMM数据治理成熟度认证。</td>
</tr>
<tr class="hover:bg-indigo-50/40 transition-colors">
<td class="p-2.5 border border-slate-200"><strong class="font-medium text-slate-800">3. 综合管理体系：</strong>投标人同时具有 ISO9001 质量管理体系、ISO14001 环境管理体系、ISO45001 职业健康安全管理体系认证证书的，予以满分加分；少一项则扣减，最低不加分。</td>
<td class="p-2.5 border border-slate-200 text-sm text-rose-700 bg-rose-50/20">三体系闭环：确保规范化运营门槛。</td>
</tr>
<tr class="hover:bg-indigo-50/40 transition-colors">
<td class="p-2.5 border border-slate-200"><strong class="font-medium text-slate-800">4. 数据资产运营能力凭证：</strong>投标人具备数据交易所出具的数据产品挂牌/交易凭证，或数据资产评估/确权/运营能力相关证明材料的，予以加分，不具备不加分。</td>
<td class="p-2.5 border border-slate-200 text-sm text-rose-700 bg-rose-50/20">核心卡点：绝大多数公司仅能做“信息化系统开发/工程建设”，根本无数据资产在交易所挂牌或许可运营记录。</td>
</tr>

<!-- Dimension 2: 类似案例 -->
<tr class="hover:bg-indigo-50/40 transition-colors border-t border-slate-100">
<td class="p-3 font-bold text-brand-800 bg-blue-50/40 border border-slate-200 align-top text-center align-middle" rowspan="2">二、类似案例</td>
<td class="p-2.5 border border-slate-200"><strong class="font-medium text-slate-800">1. 数据治理与数据资产入表全链条业绩：</strong>2020年1月1日至今，投标人每提供一个交通/基础设施领域包含<strong>“数据采集 + 数据治理 + 数据资产确权/入表登记”</strong>全流程实施内容的业绩予以加分。<br/><span class="text-sm text-slate-500 mt-1 block">评审依据：提供合同关键页及第三方机构出具的数据资产登记/入表凭证。</span></td>
<td class="p-2.5 border border-slate-200 text-sm text-rose-700 bg-rose-50/20">核心卡点：明确要求包含<strong>“数据资产入表登记/确权凭证”</strong>。传统集成商或开发商只有软件开发合同，无法提供数据资产入表证明。</td>
</tr>
<tr class="hover:bg-indigo-50/40 transition-colors">
<td class="p-2.5 border border-slate-200"><strong class="font-medium text-slate-800">2. 交通基础设施节点管控与数据运营平台业绩：</strong>2020年1月1日至今，投标人每提供一个<strong>“交通基础设施节点智能化管控/数据运营平台系统”</strong>自主研发及实施业绩予以加分。<br/><span class="text-sm text-slate-500 mt-1 block">评审依据：提供自主软著及对应平台实施/运营合同。</span></td>
<td class="p-2.5 border border-slate-200 text-sm text-rose-700 bg-rose-50/20">楚云系列平台对标：将静态交通/充电系统升维包装为“节点管控/数据运营平台”，排斥无自主数据运营平台的纯代理商。</td>
</tr>

<!-- Dimension 3: 技术实力 -->
<tr class="hover:bg-indigo-50/40 transition-colors border-t border-slate-100">
<td class="p-3 font-bold text-brand-800 bg-blue-50/40 border border-slate-200 align-top text-center align-middle">三、技术实力</td>
<td class="p-2.5 border border-slate-200">投标人具备软件著作权登记证书，且软著名称必须精准包含以下数据治理与资产类关键词（限定为：“数据采集”、“数据标准管理”、“数据质量管理”、“数据资产管理”、“数据标注”、“数据治理”、“数据资源目录”），每提供相关证书予以加分。<br/><span class="text-sm text-slate-500 mt-1 block">评审依据：附国家版权局颁发的软著扫描件（加盖公章）。</span></td>
<td class="p-2.5 border border-slate-200 text-sm text-rose-700 bg-rose-50/20">词库精准封闭：剔除所有通用业务词（如“系统”、“软件”、“管理平台”），只认纯数据治理与资产管理软著，传统IT公司难以凑齐。</td>
</tr>

<!-- Dimension 4: 项目团队 -->
<tr class="hover:bg-indigo-50/40 transition-colors border-t border-slate-100">
<td class="p-3 font-bold text-brand-800 bg-blue-50/40 border border-slate-200 align-top text-center align-middle" rowspan="3">四、项目团队</td>
<td class="p-2.5 border border-slate-200"><strong class="font-medium text-slate-800">1. 项目负责人/项目经理：</strong>投标人拟派的项目经理具有信息系统项目管理师（高级）资质证书或项目管理师（PMP）资质证书，予以加分。<br/><span class="text-sm text-slate-500 mt-1 block">评审依据：提供证书复印件及近半年内任意一个月社保证明。</span></td>
<td class="p-2.5 border border-slate-200 text-sm text-rose-700 bg-rose-50/20">通用高级高项/PMP，保证自身满分。</td>
</tr>
<tr class="hover:bg-indigo-50/40 transition-colors">
<td class="p-2.5 border border-slate-200"><strong class="font-medium text-slate-800">2. 技术负责人：</strong>投标人拟派的技术负责人同时具有<strong>“数据资产管理师”以及“高级软件工程师或系统架构设计师”</strong>资质证书的，予以全额加分；仅具备其中一项的部分加分，否则不加分。</td>
<td class="p-2.5 border border-slate-200 text-sm text-rose-700 bg-rose-50/20">核心卡点（强排他）：将<strong>“数据资产管理师”</strong>设为必选项！传统IT与施工单位技术负责人通常只有软考或建造师，极少具备数据资产管理师认证。</td>
</tr>
<tr class="hover:bg-indigo-50/40 transition-colors">
<td class="p-2.5 border border-slate-200"><strong class="font-medium text-slate-800">3. 项目团队成员：</strong>投标人拟派的项目团队成员具备数据资产管理师、数据库工程师、高级软件工程师或交通/计算机相关专业中级及以上职称的，按人数予以加分。</td>
<td class="p-2.5 border border-slate-200 text-sm text-rose-700 bg-rose-50/20">设定专业资质及高级技术职称壁垒。</td>
</tr>

</tbody>
</table>
        """
        new_table = BeautifulSoup(new_table_html, 'html.parser')
        table.replace_with(new_table)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print("Table successfully updated.")
else:
    print("Could not find sec3-1")
