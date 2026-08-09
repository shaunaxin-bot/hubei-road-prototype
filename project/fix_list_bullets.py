import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_block = '''<ul class="list-disc pl-5 space-y-1 text-slate-600">
                <li><strong>1. 机关处室：</strong>考核业务及数据需求完整度、分管领域数据治理质量、场景及年报应用落地成效；</li>
                <li><strong>2. 市州公路机构：</strong>考核辖区数据归集覆盖率、数据审核合格率、年报上报及时性、基层指导成效；</li>
                <li><strong>3. 县级公路机构：</strong>考核基础数据完整度、实时数据上传时效、数据问题整改完成率。</li>
              </ul>'''

new_block = '''<ul class="list-none pl-1 space-y-1.5 text-slate-600">
                <li><strong class="text-indigo-800">1. 机关处室：</strong>考核业务及数据需求完整度、分管领域数据治理质量、场景及年报应用落地成效；</li>
                <li><strong class="text-indigo-800">2. 市州公路机构：</strong>考核辖区数据归集覆盖率、数据审核合格率、年报上报及时性、基层指导成效；</li>
                <li><strong class="text-indigo-800">3. 县级公路机构：</strong>考核基础数据完整度、实时数据上传时效、数据问题整改完成率。</li>
              </ul>'''

content = content.replace(old_block, new_block)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
