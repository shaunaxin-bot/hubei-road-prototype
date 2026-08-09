import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

new_contents = {
    'sec1-3-3-1': """
<div class="bg-indigo-50/30 border border-indigo-100 p-4 rounded-lg space-y-3 scroll-mt-6" id="sec1-3-3-1">
<h3 class="text-lg font-bold text-slate-800 mb-1">1、数据采集与接入</h3>
<p class="text-slate-700 leading-tight">依托AI智能化能力，简化全省公路各类数据的归集接入工作。针对公路养护、桥梁监测、交通调查、工程建设、台账报表、现场巡检等各类业务数据，无需人工逐条整理录入，可自动汇总整合各类零散、格式不一的业务资料。同时能够自动甄别无效、重复、错误数据，规范统一数据格式，实现各类业务数据高效、完整、合规归集，大幅减少人工整理工作量，全面拓宽公路数据归集覆盖面。</p>
</div>
""",
    'sec1-3-3-2': """
<div class="bg-indigo-50/30 border border-indigo-100 p-4 rounded-lg space-y-3 scroll-mt-6" id="sec1-3-3-2">
<h3 class="text-lg font-bold text-slate-800 mb-1">2、数据资源盘点</h3>
<p class="text-slate-700 leading-tight">借助AI智能梳理功能，高效完成全省公路全域数据资产盘点工作。系统可自动梳理各业务处室、各业务系统的现有数据资源，清晰区分养护、统计、投资、桥隧、路网运行等各类业务数据的归属、用途、更新频率。快速排查长期闲置、重复冗余、互不连通的“数据孤岛”资源，自动分类整理形成完整清晰的公路数据资源清单，替代传统人工逐条摸排的方式，让全省公路数据家底一目了然。</p>
</div>
""",
    'sec1-3-3-3': """
<div class="bg-indigo-50/30 border border-indigo-100 p-4 rounded-lg space-y-3 scroll-mt-6" id="sec1-3-3-3">
<h3 class="text-lg font-bold text-slate-800 mb-1">3、标准数据仓建设</h3>
<p class="text-slate-700 leading-tight">利用AI智能适配功能，助力搭建全省统一的公路标准数据资源库。针对各业务系统数据名称不统一、统计口径不一致、指标相互不匹配的行业痛点，智能比对梳理不同业务数据的异同，统一规范各类业务指标名称和统计标准。自动匹配整合分散在各平台的业务数据，按照统一标准规整汇总，彻底解决以往各系统数据“同名不同义、同义不同名”的问题，建成口径统一、规范标准的公路数据底座。</p>
</div>
""",
    'sec1-3-3-4': """
<div class="bg-indigo-50/30 border border-indigo-100 p-4 rounded-lg space-y-3 scroll-mt-6" id="sec1-3-3-4">
<h3 class="text-lg font-bold text-slate-800 mb-1">4、数据质量稽查与评估</h3>
<p class="text-slate-700 leading-tight">通过AI智能核查能力，常态化开展公路数据自查自纠与质量评估工作。可自动比对跨系统、跨业务的同源数据，精准排查数据缺失、数值异常、逻辑矛盾、前后不一致等各类问题，自动标记问题数据、梳理问题清单。同时从数据完整性、准确性、时效性等维度，自动开展质量打分评估，精准定位数据问题源头，为各业务处室整改优化数据、夯实数据质量提供明确依据，实现数据质量闭环管控。</p>
</div>
""",
    'sec1-3-3-5': """
<div class="bg-indigo-50/30 border border-indigo-100 p-4 rounded-lg space-y-3 scroll-mt-6" id="sec1-3-3-5">
<h3 class="text-lg font-bold text-slate-800 mb-1">5、数据共享与发布</h3>
<p class="text-slate-700 leading-tight">依托AI智能服务能力，安全、便捷推进公路数据共享复用。在严守数据安全底线的前提下，自动区分普通数据、重要数据和核心数据，做好数据安全防护处理。结合各业务工作需求，精准匹配可共享的数据资源，简化数据查询、取数、统计流程，支持各处室快速调取所需业务数据。同时统一数据输出和对外发布口径，既保障数据安全合规，又有效打破部门数据壁垒，提升公路数据服务业务、支撑决策的整体效能。</p>
</div>
"""
}

for sec_id, new_html in new_contents.items():
    old_div = soup.find(id=sec_id)
    if old_div:
        new_div = BeautifulSoup(new_html, 'html.parser').div
        old_div.replace_with(new_div)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully replaced content for all 5 sections again.")
