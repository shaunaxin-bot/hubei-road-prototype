import os

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        '【数据指南编制】章节<br><span class="font-normal">（包含：数据基础元与编码指南、数据质量、数据采集、业务域数据、共享交换与安全指南）</span>',
        '<a href="#sec1-2" class="text-brand-600 hover:underline">1.2. 数据指南编制</a> 章节<br><span class="font-normal">（包含：<a href="#sec1-2-1" class="text-brand-600 hover:underline">1.2.1. 基础标准与质量管控</a>、<a href="#sec1-2-2" class="text-brand-600 hover:underline">1.2.2. 采集接入与共享规范</a>、<a href="#sec1-2-3" class="text-brand-600 hover:underline">1.2.3. 安全管控</a>、<a href="#sec1-2-4" class="text-brand-600 hover:underline">1.2.4. AI治理工具规范</a>）</span>'
    ),
    (
        '【数据加工与处理】章节<br><span class="font-normal">（对应：AI治理工具总体建设要求）</span>',
        '<a href="#sec1-3" class="text-brand-600 hover:underline">1.3. 数据加工与处理</a> 章节<br><span class="font-normal">（对应：<a href="#sec1-3-3" class="text-brand-600 hover:underline">1.3.3. AI治理工具</a> 总体要求）</span>'
    ),
    (
        '【其他要求】章节<br><span class="font-normal">（对应：运维保障配套工作小节）</span>',
        '<a href="#sec1-6" class="text-brand-600 hover:underline">1.7. 其他要求</a> 章节<br><span class="font-normal">（对应：<a href="#sec1-6-1" class="text-brand-600 hover:underline">1.7.1. 验收要求</a> 中“运维保障配套工作”）</span>'
    ),
    (
        '【其他要求】章节<br><span class="font-normal">（对应：培训服务配套工作小节）</span>',
        '<a href="#sec1-6" class="text-brand-600 hover:underline">1.7. 其他要求</a> 章节<br><span class="font-normal">（对应：<a href="#sec1-6-1" class="text-brand-600 hover:underline">1.7.1. 验收要求</a> 中“培训服务配套工作”）</span>'
    ),
    (
        '【其他要求】章节<br><span class="font-normal">（对应：保障数据治理体系长效稳定运行）</span>',
        '<a href="#sec1-6" class="text-brand-600 hover:underline">1.7. 其他要求</a> 章节<br><span class="font-normal">（对应：<a href="#sec1-6-1" class="text-brand-600 hover:underline">1.7.1. 验收要求</a> 中“长效稳定运行保障”）</span>'
    ),
    (
        '【AI治理工具】章节下详细编号：<br><span class="font-normal">1.1.1.1（需求调研）至 1.1.1.10（知识库管理）十项详细要求</span>',
        '<a href="#sec1-3-3" class="text-brand-600 hover:underline">1.3.3. AI治理工具</a> 章节下详细编号：<br><span class="font-normal">1.1.1.1（需求调研）至 1.1.1.10（知识库管理）十项详细要求</span>'
    ),
    (
        '【AI治理工具】功能补充要求：<br><span class="font-normal">（按组织架构的场景化资产分级合规和流转考核 - 数据找人）</span>',
        '<a href="#sec1-3-3" class="text-brand-600 hover:underline">1.3.3. AI治理工具</a> 功能补充要求：<br><span class="font-normal">（按组织架构的场景化资产分级合规和流转考核 - 数据找人）</span>'
    ),
    (
        '【数据资源目录】章节<br>及【AI治理工具】项下：<br><span class="font-normal">1.1.1.2（智能资源盘点）</span>',
        '<a href="#sec1-5" class="text-brand-600 hover:underline">1.5. 数据资源目录</a> 章节<br>及 <a href="#sec1-3-3" class="text-brand-600 hover:underline">1.3.3. AI治理工具</a> 项下：<br><span class="font-normal">1.1.1.2（智能资源盘点）</span>'
    ),
    (
        '【AI治理工具】项下：<br><span class="font-normal">1.1.1.4（智能数据标准设计）<br>1.1.1.9（数据资产安全管理）<br>1.1.1.10（知识库管理）</span>',
        '<a href="#sec1-3-3" class="text-brand-600 hover:underline">1.3.3. AI治理工具</a> 项下：<br><span class="font-normal">1.1.1.4（智能数据标准设计）<br>1.1.1.9（数据资产安全管理）<br>1.1.1.10（知识库管理）</span>'
    ),
    (
        '【数据仓库治理】章节<br>及【AI治理工具】项下：<br><span class="font-normal">1.1.1.5（智能数仓模型设计）</span>',
        '<a href="#sec1-3-4" class="text-brand-600 hover:underline">1.3.4. 数据仓库治理</a> 章节<br>及 <a href="#sec1-3-3" class="text-brand-600 hover:underline">1.3.3. AI治理工具</a> 项下：<br><span class="font-normal">1.1.1.5（智能数仓模型设计）</span>'
    ),
    (
        '【AI治理工具】项下：<br><span class="font-normal">1.1.1.6（智能数据处理）<br>1.1.1.8（主动质量控制）</span>',
        '<a href="#sec1-3-3" class="text-brand-600 hover:underline">1.3.3. AI治理工具</a> 项下：<br><span class="font-normal">1.1.1.6（智能数据处理）<br>1.1.1.8（主动质量控制）</span>'
    ),
    (
        '【AI治理工具】功能补充要求：<br><span class="font-normal">（按组织架构自动生成用于评价各处室的报表 - 管运营）</span>',
        '<a href="#sec1-3-3" class="text-brand-600 hover:underline">1.3.3. AI治理工具</a> 功能补充要求：<br><span class="font-normal">（按组织架构自动生成用于评价各处室的报表 - 管运营）</span>'
    ),
    (
        '【验收要求】章节：<br><span class="font-normal">“项目通过初步验收，进入试运行阶段无重大故障”</span>',
        '<a href="#sec1-6-1" class="text-brand-600 hover:underline">1.7.1. 验收要求</a> 章节：<br><span class="font-normal">“项目通过初步验收，进入试运行阶段无重大故障”</span>'
    ),
    (
        '【验收要求】章节：<br><span class="font-normal">“共同对系统的整体性能进行测试”</span>',
        '<a href="#sec1-6-1" class="text-brand-600 hover:underline">1.7.1. 验收要求</a> 章节：<br><span class="font-normal">“共同对系统的整体性能进行测试”</span>'
    ),
    (
        '【验收要求】章节：<br><span class="font-normal">“签署试运行验收报告，进行最终验收按合同支付费用”</span>',
        '<a href="#sec1-6-1" class="text-brand-600 hover:underline">1.7.1. 验收要求</a> 章节：<br><span class="font-normal">“签署试运行验收报告，进行最终验收按合同支付”</span>'
    )
]

for old_str, new_str in replacements:
    if old_str in content:
        content = content.replace(old_str, new_str)
    else:
        print(f"Warning: Could not find '{old_str[:30]}...'")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Success")
