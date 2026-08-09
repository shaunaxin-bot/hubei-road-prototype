const fs = require('fs');
const filePath = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html';
let content = fs.readFileSync(filePath, 'utf8');

const newTable = 
            <table class="w-full text-left text-base border-collapse">
              <thead>
                <tr class="bg-slate-100 text-red-600 font-bold border-b border-slate-200">
                  <th colspan="2" class="p-2.5 border-r border-slate-200 text-center w-24">验收阶段</th>
                  <th class="p-2.5 border-r border-slate-200 w-64">交付成果材料名称</th>
                  <th class="p-2.5 border-r border-slate-200">对应招标技术要求项（精确标号）</th>
                  <th class="p-2.5">成果交付要求说明</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-200 text-slate-700">
                <tr class="hover:bg-slate-50/80">
                  <td rowspan="12" class="p-2.5 font-bold text-red-600 border-r border-slate-200 text-center writing-vertical">初步验收</td>
                  <td rowspan="5" class="p-2.5 font-bold text-red-600 border-r border-slate-200 text-center">1. 项目建设与交付类</td>
                  <td class="p-2.5 border-r border-slate-200 font-medium">《四大核心公路数据指南》（包含基础标准、采集接入、安全管控及AI治理规范四本分册）</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【数据指南编制】章节<br><span class="font-normal">（包含：数据基础元与编码指南、数据质量、数据采集、业务域数据、共享交换与安全指南）</span></td>
                  <td class="p-2.5 text-red-600">初验必备：验证顶层数据制度资产是否高质量落地</td>
                </tr>
                <tr class="hover:bg-slate-50/80">
                  <td class="p-2.5 border-r border-slate-200 font-medium">《AI数据治理工具建设方案与需求规格说明书》</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【数据加工与处理】章节<br><span class="font-normal">（对应：AI治理工具总体建设要求）</span></td>
                  <td class="p-2.5 text-red-600">初验必备：验证系统架构部署与 API 接口是否合规</td>
                </tr>
                <tr class="hover:bg-slate-50/80">
                  <td class="p-2.5 border-r border-slate-200 font-medium">《AI治理工具操作手册》（管理员与最终用户版）</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【其他要求】章节<br><span class="font-normal">（对应：运维保障配套工作小节）</span></td>
                  <td class="p-2.5 text-red-600">初验必备：验证是否具备移交及独立运维条件</td>
                </tr>
                <tr class="hover:bg-slate-50/80">
                  <td class="p-2.5 border-r border-slate-200 font-medium">《项目技术培训交付记录》（含课件、签到、实操记录）</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【其他要求】章节<br><span class="font-normal">（对应：培训服务配套工作小节）</span></td>
                  <td class="p-2.5 text-red-600">初验必备：验证培训服务是否真实覆盖各级使用者</td>
                </tr>
                <tr class="hover:bg-slate-50/80">
                  <td class="p-2.5 border-r border-slate-200 font-medium">《驻场维保与大模型持续调优服务承诺书》</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【其他要求】章节<br><span class="font-normal">（对应：保障数据治理体系长效稳定运行）</span></td>
                  <td class="p-2.5 text-red-600">初验必备：验证项目长期售后与模型升级承诺</td>
                </tr>
                <tr class="hover:bg-slate-50/80 border-t border-slate-200">
                  <td rowspan="2" class="p-2.5 font-bold text-red-600 border-r border-slate-200 text-center">2. 平台功能演示类</td>
                  <td class="p-2.5 border-r border-slate-200 font-medium text-red-600">《AI治理工具核心功能演示确认单及操作录屏》</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【AI治理工具】章节下详细编号：<br><span class="font-normal">1.1.1.1（需求调研）至 1.1.1.10（知识库管理）十项详细要求</span></td>
                  <td class="p-2.5 text-red-600">初验必备：现场验证工具的十大核心功能模块完整跑通</td>
                </tr>
                <tr class="hover:bg-slate-50/80">
                  <td class="p-2.5 border-r border-slate-200 font-medium text-red-600">《资产分级合规及按组织架构的流转考核实测报告》</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【AI治理工具】功能补充要求：<br><span class="font-normal">（按组织架构的场景化资产分级合规和流转考核 - 数据找人）</span></td>
                  <td class="p-2.5 text-red-600">初验必备：验证底层数据自动精准推送至对口处室的能力</td>
                </tr>
                <tr class="hover:bg-slate-50/80 border-t border-slate-200">
                  <td rowspan="5" class="p-2.5 font-bold text-red-600 border-r border-slate-200 text-center">3. 治理过程与成果类</td>
                  <td class="p-2.5 border-r border-slate-200 font-medium text-red-600">《湖北省公路全局数据资源资产目录》</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【数据资源目录】章节<br>及【AI治理工具】项下：<br><span class="font-normal">1.1.1.2（智能资源盘点）</span></td>
                  <td class="p-2.5 text-red-600">初验必备：提交工具直连扫描生成的真实电子账本</td>
                </tr>
                <tr class="hover:bg-slate-50/80">
                  <td class="p-2.5 border-r border-slate-200 font-medium text-red-600">《湖北公路智能治理知识基座配置库》</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【AI治理工具】项下：<br><span class="font-normal">1.1.1.4（智能数据标准设计）<br>1.1.1.9（数据资产安全管理）<br>1.1.1.10（知识库管理）</span></td>
                  <td class="p-2.5 text-red-600">初验必备：提交指南入模生成的机器规则库及脱敏策略集</td>
                </tr>
                <tr class="hover:bg-slate-50/80">
                  <td class="p-2.5 border-r border-slate-200 font-medium text-red-600">《全链路数仓模型设计蓝图及ER图》</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【数据仓库治理】章节<br>及【AI治理工具】项下：<br><span class="font-normal">1.1.1.5（智能数仓模型设计）</span></td>
                  <td class="p-2.5 text-red-600">初验必备：提交覆盖 SRC 到 ADS 架构及业务本体结构清单</td>
                </tr>
                <tr class="hover:bg-slate-50/80">
                  <td class="p-2.5 border-r border-slate-200 font-medium text-red-600">《公路数据资产质量体检报告》及《数据溯源日志》</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【AI治理工具】项下：<br><span class="font-normal">1.1.1.6（智能数据处理）<br>1.1.1.8（主动质量控制）</span></td>
                  <td class="p-2.5 text-red-600">初验必备：提交系统基于稽核规则跑出的脏数据排查清单</td>
                </tr>
                <tr class="hover:bg-slate-50/80">
                  <td class="p-2.5 border-r border-slate-200 font-medium text-red-600">《数据资产贡献与处室效能考核月报》</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【AI治理工具】功能补充要求：<br><span class="font-normal">（按组织架构自动生成用于评价各处室的报表 - 管运营）</span></td>
                  <td class="p-2.5 text-red-600">初验必备：提交按组织架构自动生成用于评价各处室的报表</td>
                </tr>
                <tr class="hover:bg-slate-50/80 border-t-2 border-slate-300">
                  <td rowspan="3" class="p-2.5 font-bold text-red-600 border-r border-slate-200 text-center writing-vertical">最终验收</td>
                  <td rowspan="3" class="p-2.5 font-bold text-red-600 border-r border-slate-200 text-center">4. 试运行与终验类</td>
                  <td class="p-2.5 border-r border-slate-200 font-medium text-red-600">《AI治理工具系统试运行总结报告》</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【验收要求】章节：<br><span class="font-normal">“项目通过初步验收，进入试运行阶段无重大故障”</span></td>
                  <td class="p-2.5 text-red-600">终验必备：证明初验后系统在实际业务环境中连续稳定运行</td>
                </tr>
                <tr class="hover:bg-slate-50/80">
                  <td class="p-2.5 border-r border-slate-200 font-medium text-red-600">《系统整体性能与安全测试报告》</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【验收要求】章节：<br><span class="font-normal">“共同对系统的整体性能进行测试”</span></td>
                  <td class="p-2.5 text-red-600">终验必备：包含并发性能测试、接口调用的第三方压测证明</td>
                </tr>
                <tr class="hover:bg-slate-50/80">
                  <td class="p-2.5 border-r border-slate-200 font-medium text-red-600">《数据治理工程项目最终验收报告》</td>
                  <td class="p-2.5 border-r border-slate-200 font-bold text-red-600">【验收要求】章节：<br><span class="font-normal">“签署试运行验收报告，进行最终验收按合同支付费用”</span></td>
                  <td class="p-2.5 text-red-600">终验必备：三方代表联合签字盖章，作为最终付款凭证</td>
                </tr>
              </tbody>
            </table>
;

const oldStart = '<table class="w-full text-left text-base border-collapse">';
const oldEnd = '</table>';
const startIndex = content.indexOf(oldStart);
const endIndex = content.indexOf(oldEnd, startIndex) + oldEnd.length;

if (startIndex !== -1 && endIndex !== -1) {
    const updatedContent = content.substring(0, startIndex) + newTable + content.substring(endIndex);
    fs.writeFileSync(filePath, updatedContent, 'utf8');
    console.log("Success");
} else {
    console.log("Could not find table boundaries.");
}
