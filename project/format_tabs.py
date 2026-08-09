import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

sec3_1 = soup.find(id='sec3-1')

# Extract the existing table (which will become Tab 1)
existing_table_div = sec3_1.find('div', class_='overflow-x-auto')
existing_table_html = str(existing_table_div)

new_tabs_html = f"""
<div class="space-y-4">
  <!-- Tabs Navigation -->
  <div class="flex space-x-2 border-b border-slate-200 mt-3">
    <button onclick="switchBizTab('biz-tab-1')" id="btn-biz-tab-1" class="px-4 py-2 font-bold text-brand-600 border-b-2 border-brand-600 hover:bg-slate-50 transition-colors focus:outline-none">选项一（极高排他版）</button>
    <button onclick="switchBizTab('biz-tab-2')" id="btn-biz-tab-2" class="px-4 py-2 font-medium text-slate-500 hover:text-slate-700 hover:bg-slate-50 border-b-2 border-transparent transition-colors focus:outline-none">选项二（进阶资质版）</button>
    <button onclick="switchBizTab('biz-tab-3')" id="btn-biz-tab-3" class="px-4 py-2 font-medium text-slate-500 hover:text-slate-700 hover:bg-slate-50 border-b-2 border-transparent transition-colors focus:outline-none">选项三（基础常规版）</button>
  </div>

  <!-- Tab 1: Exclusive (existing) -->
  <div id="biz-tab-1" class="tab-content-biz block">
    {existing_table_html}
  </div>

  <!-- Tab 2: Enhanced -->
  <div id="biz-tab-2" class="tab-content-biz hidden">
    <div class="overflow-x-auto rounded-xl border border-slate-200 shadow-md bg-white">
      <table class="w-full text-left text-base border-collapse">
        <thead class="border border-slate-200">
          <tr class="bg-slate-50 text-slate-800 font-bold border-b-2 border-slate-200">
            <th class="p-2.5 border border-slate-200 w-32 text-center">评审维度</th>
            <th class="p-2.5 border border-slate-200">评分标准</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-200 text-slate-600">
          <tr class="hover:bg-slate-50/50">
            <td class="p-3 font-bold text-slate-700 bg-slate-50 border border-slate-200 align-top text-center align-middle">企业<br/>综合实力</td>
            <td class="p-2.5 border border-slate-200 space-y-2">
              <div>1. 投标人具有国家高新技术企业证书的，予以加分，没有不加分；</div>
              <div>2. 投标人具有软件成熟度CMMI5级证书或4级，按级别加分，其余不加分；</div>
              <div>3. <span class="text-rose-600 font-semibold">投标人具有DCMM数据管理能力成熟度（乙方）三级、数据安全能力成熟度认证（三级）证书，且在有效期内的，每提供一个证书予以加分，不提供不加分。</span></div>
              <div>4. 投标人具有ITSS信息技术服务标准符合性证书（运维服务三级）、ISO9001质量管理体系认证证书、ISO14001环境管理体系认证证书、<span class="text-rose-600 font-semibold">ISO45001职业健康安全管理体系认证、CCRC信息安全服务资质认证（软件安全开发三级）、CCRC信息技术服务资质认证（安全运维三级）、CS信息系统建设和服务能力等级认证（二级）</span>，且在有效期内的，每提供一个证书予以加分，不提供不加分。</div>
            </td>
          </tr>
          <tr class="hover:bg-slate-50/50">
            <td class="p-3 font-bold text-slate-700 bg-slate-50 border border-slate-200 align-top text-center align-middle">类似案例</td>
            <td class="p-2.5 border border-slate-200 space-y-2">
              <div>1、2020年1月1日至今，投标人每提供一个<span class="text-rose-600 font-semibold">相关数据治理业绩（建设内容须包含数据治理/数据资产服务/数据治理平台等相关内容）</span>予以加分。</div>
              <div>2、2020年1月1日至今，投标人每提供一个<span class="text-rose-600 font-semibold">交通业务业绩（含智慧交通、数据库开发等）</span>予以加分；不提供不加分。<br/><span class="text-sm text-slate-500 mt-1 block">评审依据：提供有效合同扫描件（合同可提供关键页，如合同首页、建设金额、签字加盖投标人公章页），1、2的业绩不能重复计算。</span></div>
            </td>
          </tr>
          <tr class="hover:bg-slate-50/50">
            <td class="p-3 font-bold text-slate-700 bg-slate-50 border border-slate-200 align-top text-center align-middle">技术实力</td>
            <td class="p-2.5 border border-slate-200 space-y-2">
              <div>1、每具备1个软件著作权登记证书且软著名称包含<span class="text-rose-600 font-semibold">“元数据设计”、“大数据量编辑”</span>的，予以加分，没有不加分。<br/><span class="text-sm text-slate-500 mt-1 block">评审依据：附国家版权局颁发的软件著作权登记证书扫描件（加盖公章），且著作权取得日期为发布招标公告之日前取得，否则不加分。</span></div>
              <div>2、<span class="text-rose-600 font-semibold">每具备1个发明专利证书且专利名称包含“数据治理”、“数据还原”的，予以加分，没有不加分。</span></div>
            </td>
          </tr>
          <tr class="hover:bg-slate-50/50">
            <td class="p-3 font-bold text-slate-700 bg-slate-50 border border-slate-200 align-top text-center align-middle">项目团队</td>
            <td class="p-2.5 border border-slate-200 space-y-2">
              <div><strong class="text-slate-800 block mb-1">项目负责人</strong>项目经理：投标人拟派的项目经理具有信息系统项目管理师资质证书，且是<span class="text-rose-600 font-semibold">人力资源与社会保障部/工业与信息化部批准颁发</span>的高级项目经理，<span class="text-rose-600 font-semibold">同时具有PMP证书</span>的，提供证书复印件，以及投标人为其缴纳的社保证明（投标截止时间前近半年内任意一个月），予以加分，否则不加分。</div>
              <div><strong class="text-slate-800 block mb-1 mt-2">技术负责人</strong>投标人拟派的技术负责人具有系统架构设计师资质证书，<span class="text-rose-600 font-semibold">同时具有高级信息系统项目管理师资质证书</span>，提供证书复印件，以及投标人为其缴纳的社保证明（投标截止时间前近半年内任意一个月），予以加分，否则不加分。</div>
              <div class="mt-2"><span class="text-rose-600 font-semibold">投标人拟派的项目团队成员具有大数据分析师、数据库系统工程师等相关中级及以上职称的</span>，每有一个予以加分。提供证书复印件，以及投标人为其缴纳的社保证明。</div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Tab 3: Basic -->
  <div id="biz-tab-3" class="tab-content-biz hidden">
    <div class="overflow-x-auto rounded-xl border border-slate-200 shadow-md bg-white">
      <table class="w-full text-left text-base border-collapse">
        <thead class="border border-slate-200">
          <tr class="bg-slate-50 text-slate-800 font-bold border-b-2 border-slate-200">
            <th class="p-2.5 border border-slate-200 w-32 text-center">评审维度</th>
            <th class="p-2.5 border border-slate-200">评分标准</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-200 text-slate-600">
          <tr class="hover:bg-slate-50/50">
            <td class="p-3 font-bold text-slate-700 bg-slate-50 border border-slate-200 align-top text-center align-middle">企业<br/>综合实力</td>
            <td class="p-2.5 border border-slate-200 space-y-2">
              <div>1. 投标人具有国家高新技术企业证书的，予以加分，没有不加分；</div>
              <div>2. 投标人具有软件成熟度CMMI5级证书或4级，按级别加分，其余不加分；</div>
              <div>3. DCMM 数据管理能力成熟度（乙方）5级证书或4级，按级别加分，其余不加分；</div>
              <div>4. 投标人具有ITSS信息技术服务标准符合性证书(信息技术服务运行维护一级)、ISO9001质量管理体系认证证书、ISO14001环境管理体系认证证书，且在有效期内的，每提供一个证书予以加分，不提供不加分。</div>
            </td>
          </tr>
          <tr class="hover:bg-slate-50/50">
            <td class="p-3 font-bold text-slate-700 bg-slate-50 border border-slate-200 align-top text-center align-middle">类似案例</td>
            <td class="p-2.5 border border-slate-200 space-y-2">
              <div>1、2020年1月1日至今，投标人每提供一个类似交通行业数据治理业绩（建设内容须包含数据治理/中台/大数据平台等相关内容）予以加分。</div>
              <div>2、2020年1月1日至今，投标人每提供一个公路业务系统业绩予以加分；不提供不加分。<br/><span class="text-sm text-slate-500 mt-1 block">评审依据：提供有效合同扫描件（合同可提供关键页，如合同首页、建设金额、签字加盖投标人公章页），1、2的业绩不能重复计算。</span></div>
            </td>
          </tr>
          <tr class="hover:bg-slate-50/50">
            <td class="p-3 font-bold text-slate-700 bg-slate-50 border border-slate-200 align-top text-center align-middle">技术实力</td>
            <td class="p-2.5 border border-slate-200">
              <div>每具备1个软件著作权登记证书且软著名称包含“数据采集”、“数据标准管理”、“数据质量管理”、“数据资产管理”、“数据标注”、“数据治理”、“数据资源目录”的，予以加分，没有不加分。<br/><span class="text-sm text-slate-500 mt-1 block">评审依据：附国家版权局颁发的软件著作权登记证书扫描件（加盖公章），且著作权取得日期为发布招标公告之日前取得，否则不加分</span></div>
            </td>
          </tr>
          <tr class="hover:bg-slate-50/50">
            <td class="p-3 font-bold text-slate-700 bg-slate-50 border border-slate-200 align-top text-center align-middle">项目团队</td>
            <td class="p-2.5 border border-slate-200 space-y-2">
              <div><strong class="text-slate-800 block mb-1">项目负责人</strong>项目经理：投标人拟派的项目经理具有信息系统项目管理师资质证书，且是中国电子信息行业联合会登记的高级项目经理，提供证书复印件，以及投标人为其缴纳的社保证明（投标截止时间前近半年内任意一个月），予以加分，否则不加分</div>
              <div><strong class="text-slate-800 block mb-1 mt-2">技术负责人</strong>投标人拟派的技术负责人具有系统架构设计师资质证书，提供证书复印件，以及投标人为其缴纳的社保证明（投标截止时间前近半年内任意一个月），予以加分，否则不加分。</div>
              <div class="mt-2">投标人拟派的项目团队成员具有交通/计算机相关专业中级及以上职称的，每有一个予以加分。提供证书复印件，以及投标人为其缴纳的社保证明。</div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""
new_tabs_soup = BeautifulSoup(new_tabs_html, 'html.parser')
existing_table_div.replace_with(new_tabs_soup)

script_tag = soup.find('script')
js_to_inject = """
    function switchBizTab(tabId) {
      document.querySelectorAll('.tab-content-biz').forEach(el => {
        el.classList.add('hidden');
        el.classList.remove('block');
      });
      
      ['biz-tab-1', 'biz-tab-2', 'biz-tab-3'].forEach(id => {
        const btn = document.getElementById('btn-' + id);
        if(btn) {
          btn.className = "px-4 py-2 font-medium text-slate-500 hover:text-slate-700 hover:bg-slate-50 border-b-2 border-transparent transition-colors focus:outline-none";
        }
      });
      
      document.getElementById(tabId).classList.remove('hidden');
      document.getElementById(tabId).classList.add('block');
      
      const activeBtn = document.getElementById('btn-' + tabId);
      if(activeBtn) {
        activeBtn.className = "px-4 py-2 font-bold text-brand-600 border-b-2 border-brand-600 hover:bg-slate-50 transition-colors focus:outline-none";
      }
    }
"""
if script_tag:
    script_tag.append(js_to_inject)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Tabs inserted!")
