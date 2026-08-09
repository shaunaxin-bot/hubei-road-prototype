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
<p class="text-slate-700 leading-tight">制定《数转项目物联感知设备数据采集与接入要求》，保障外场多功能交调站、集成式气象检测站、视频监控、毫米波雷达等物联感知设备数据的统一、规范、互通。</p>
<p class="text-slate-700 leading-tight">基于公路综合信息平台现有数据仓库，接入本次数字化转型新建的路网运行监测与应急指挥调度、交通流量调查、服务区管理、基础设施监测等业务系统数据，实现业务数据的常态化汇聚接入，形成《数据资源接入清单》。</p>
</div>
""",
    'sec1-3-3-2': """
<div class="bg-indigo-50/30 border border-indigo-100 p-4 rounded-lg space-y-3 scroll-mt-6" id="sec1-3-3-2">
<h3 class="text-lg font-bold text-slate-800 mb-1">2、数据资源盘点</h3>
<p class="text-slate-700 leading-tight">编制完善《湖北省公路事业发展中心数据资源目录》，建立联动更新机制，在应用、数据变化时对数据资源目录进行更新，打造公路中心数据资源“一本帐”。</p>
</div>
""",
    'sec1-3-3-3': """
<div class="bg-indigo-50/30 border border-indigo-100 p-4 rounded-lg space-y-3 scroll-mt-6" id="sec1-3-3-3">
<h3 class="text-lg font-bold text-slate-800 mb-1">3、标准数据仓建设</h3>
<div class="space-y-3 text-base mt-2">
  <div class="p-3 border border-slate-100 rounded-lg bg-slate-50 space-y-1">
    <strong class="text-sm font-bold text-slate-700 block mb-1">原始数据层（ODS）升级</strong>
    <p class="text-slate-600 leading-tight">基于公路综合信息平台现有数据仓库，对原始数据层进行扩展升级，主要构建三类汇集库：涵盖基础属性的公路静态数据汇集库、接入新增外场设备感知的公路动态数据汇集库、包含应急等流程的公路业务数据汇集库。</p>
  </div>
  <div class="p-3 border border-slate-100 rounded-lg bg-slate-50 space-y-1">
    <strong class="text-sm font-bold text-slate-700 block mb-1">数据明细层与汇总层建设</strong>
    <p class="text-slate-600 leading-tight">构建覆盖本次数字化转型新建四大系统的数据明细层；并基于上述业务数据，完善原有综合信息平台相关专题库与指标库，升级数据汇总层。</p>
  </div>
  <div class="p-3 border border-slate-100 rounded-lg bg-slate-50 space-y-1">
    <strong class="text-sm font-bold text-slate-700 block mb-1">数据应用层与专题库建设</strong>
    <p class="text-slate-600 leading-tight">整合存量数据与新增数据，构建“静态数据库-动态业务数据库-专题数据库”架构体系。面向公路养护、路网运行监测、应急指挥、服务区监测与管理、公路资产等特定业务场景，深度加工整合专题数据库，按需为业务系统提供定制化服务支撑。</p>
  </div>
</div>
</div>
""",
    'sec1-3-3-4': """
<div class="bg-indigo-50/30 border border-indigo-100 p-4 rounded-lg space-y-3 scroll-mt-6" id="sec1-3-3-4">
<h3 class="text-lg font-bold text-slate-800 mb-1">4、数据质量稽查与评估</h3>
<p class="text-slate-700 leading-tight">制定《公路数据质量管理指南》，保障数转项目中数据在采集、治理、应用、交换共享等全生命周期的数据质量。</p>
<p class="text-slate-700 leading-tight">开展数据清洗工作，按照规范及指南要求对接入的数据进行清洗转换，对数据进行深度的质量稽查与评估检测，分类出具《数据质量报告》。</p>
</div>
""",
    'sec1-3-3-5': """
<div class="bg-indigo-50/30 border border-indigo-100 p-4 rounded-lg space-y-3 scroll-mt-6" id="sec1-3-3-5">
<h3 class="text-lg font-bold text-slate-800 mb-1">5、数据共享与发布</h3>
<p class="text-slate-700 leading-tight">修订《公路数据共享交换接口指南》，明确API数据服务、批量文件共享、消息订阅、时序数据查询等共享方式的标准，统一数据共享的请求格式、响应参数与错误码等规范。制定《公路数据共享脱敏技术指南》，明确不同共享场景下的脱敏规则，确保共享合规安全。</p>
<p class="text-slate-700 leading-tight">按需开发各类数据发布与共享接口：包括实现与政府侧数据底座的接入共享、高速视频联网平台视频数据接入、将省公路中心各数转任务业务数据共享至政府侧底座，以及实现各地市州、非交投路段数转任务数据的接入与对接发布。</p>
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

print("Successfully replaced content for all 5 sections.")
