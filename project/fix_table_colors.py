import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Row 7 old
r7_old = '<tr class="hover:bg-slate-50 bg-blue-50/20"><td class="p-2 border-r border-slate-100 text-center font-bold">7</td><td class="p-2 border-r border-slate-100 font-bold text-brand-800">核心应用成果</td><td class="p-2 text-slate-800">整合养护年报、国省道交通调查、农村公路统计底层数据源，开发公路年报统计智能查询分析功能，实现数据自动汇总、多维度指标对比、趋势研判、异常预警</td></tr>'
r7_new = '<tr class="hover:bg-slate-50"><td class="p-2 border-r border-slate-100 text-center font-bold">7</td><td class="p-2 border-r border-slate-100 font-medium text-slate-800">核心应用成果</td><td class="p-2">整合养护年报、国省道交通调查、农村公路统计底层数据源，开发公路年报统计智能查询分析功能，实现数据自动汇总、多维度指标对比、趋势研判、异常预警</td></tr>'

# Row 8 old
r8_old = '<tr class="hover:bg-slate-50 bg-blue-50/20"><td class="p-2 border-r border-slate-100 text-center font-bold">8</td><td class="p-2 border-r border-slate-100 font-bold text-brand-800">实施节点</td><td class="p-2 text-slate-800">2026年11—12月完成模块开发试运行，上线年报基础查询；2026年12月—2027年2月迭代优化分析模型，全面推广</td></tr>'
r8_new = '<tr class="hover:bg-slate-50"><td class="p-2 border-r border-slate-100 text-center font-bold">8</td><td class="p-2 border-r border-slate-100 font-medium text-slate-800">实施节点</td><td class="p-2">2026年11—12月完成模块开发试运行，上线年报基础查询；2026年12月—2027年2月迭代优化分析模型，全面推广</td></tr>'

content = content.replace(r7_old, r7_new)
content = content.replace(r8_old, r8_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
