import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

tab2 = soup.find(id='biz-tab-2')
if tab2:
    new_tab2_html = """
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
            <td class="p-2.5 border border-slate-200 space-y-3">
              <div>1. 投标人具有国家高新技术企业证书的，予以加分，没有不加分；</div>
              <div>2. 投标人具有软件成熟度CMMI5级证书或4级，按级别加分，其余不加分；</div>
              <div>3. 投标人具有<span class="text-blue-600 font-bold">DCMM数据管理能力成熟度（乙方）三级（降低：等级要求从5级降至3级）</span>、<span class="text-rose-600 font-bold">数据安全能力成熟度认证（三级）证书（提升：新增数据安全认证资质要求）</span>，且在有效期内的，每提供一个证书予以加分，不提供不加分。</div>
              <div>4. 投标人具有<span class="text-blue-600 font-bold">ITSS信息技术服务标准符合性证书（运维服务三级）（降低：等级要求从一级降至三级）</span>、ISO9001质量管理体系认证证书、ISO14001环境管理体系认证证书、<span class="text-rose-600 font-bold">ISO45001职业健康安全管理体系认证（提升：新增健康安全体系认证）</span>、<span class="text-rose-600 font-bold">CCRC信息安全服务资质认证（软件安全开发三级）、CCRC信息技术服务资质认证（安全运维三级）（提升：新增双项CCRC安全资质）</span>、<span class="text-rose-600 font-bold">CS信息系统建设和服务能力等级认证（二级）（提升：新增CS资质要求）</span>，且在有效期内的，每提供一个证书予以加分，不提供不加分。</div>
            </td>
          </tr>
          <tr class="hover:bg-slate-50/50">
            <td class="p-3 font-bold text-slate-700 bg-slate-50 border border-slate-200 align-top text-center align-middle">类似案例</td>
            <td class="p-2.5 border border-slate-200 space-y-3">
              <div>1、2020年1月1日至今，投标人每提供一个<span class="text-blue-600 font-bold">相关数据治理业绩（降低：去除了“交通行业”限定，拓宽了行业范围）</span>（建设内容须包含数据治理/<span class="text-rose-600 font-bold">数据资产服务（提升：增加数据资产服务内容）</span>/数据治理平台等相关内容）予以加分。</div>
              <div>2、2020年1月1日至今，投标人每提供一个<span class="text-blue-600 font-bold">交通业务业绩（含智慧交通、数据库开发等）（降低：“公路”扩大为“交通”，并放宽至普通数据库开发，门槛大幅降低）</span>予以加分；不提供不加分。<br/><span class="text-sm text-slate-500 mt-1 block">评审依据：提供有效合同扫描件（合同可提供关键页，如合同首页、建设金额、签字加盖投标人公章页），1、2的业绩不能重复计算。</span></div>
            </td>
          </tr>
          <tr class="hover:bg-slate-50/50">
            <td class="p-3 font-bold text-slate-700 bg-slate-50 border border-slate-200 align-top text-center align-middle">技术实力</td>
            <td class="p-2.5 border border-slate-200 space-y-3">
              <div>1、每具备1个软件著作权登记证书且软著名称包含<span class="text-rose-600 font-bold">“元数据设计”、“大数据量编辑”（提升：限定非常偏门的特定词汇，排他性极强）</span>的，予以加分，没有不加分。<br/><span class="text-sm text-slate-500 mt-1 block">评审依据：附国家版权局颁发的软件著作权登记证书扫描件（加盖公章），且著作权取得日期为发布招标公告之日前取得，否则不加分。</span></div>
              <div>2、<span class="text-rose-600 font-bold">每具备1个发明专利证书且专利名称包含“数据治理”、“数据还原”的，予以加分，没有不加分。（提升：新增高门槛的发明专利要求并限定特定词汇）</span></div>
            </td>
          </tr>
          <tr class="hover:bg-slate-50/50">
            <td class="p-3 font-bold text-slate-700 bg-slate-50 border border-slate-200 align-top text-center align-middle">项目团队</td>
            <td class="p-2.5 border border-slate-200 space-y-3">
              <div><strong class="text-slate-800 block mb-1">项目负责人</strong>项目经理：投标人拟派的项目经理具有信息系统项目管理师资质证书，且是<span class="text-rose-600 font-bold">人力资源与社会保障部/工业与信息化部批准颁发的高级项目经理（提升：发证机关要求更严）</span>，<span class="text-rose-600 font-bold">同时具有PMP证书（提升：要求额外具备PMP国际证书，形成双证卡点）</span>的，提供证书复印件，以及投标人为其缴纳的社保证明（投标截止时间前近半年内任意一个月），予以加分，否则不加分。</div>
              <div><strong class="text-slate-800 block mb-1 mt-2">技术负责人</strong>投标人拟派的技术负责人具有系统架构设计师资质证书，<span class="text-rose-600 font-bold">同时具有高级信息系统项目管理师资质证书（提升：要求技术与管理的双重高级证书）</span>，提供证书复印件，以及投标人为其缴纳的社保证明（投标截止时间前近半年内任意一个月），予以加分，否则不加分。</div>
              <div class="mt-2">投标人拟派的项目团队成员<span class="text-rose-600 font-bold">具有大数据分析师、数据库系统工程师等相关中级及以上职称的（提升：从宽泛的计算机专业变更为特定的大数据/数据库专业认证）</span>，每有一个予以加分。提供证书复印件，以及投标人为其缴纳的社保证明。</div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
    """
    new_tab2 = BeautifulSoup(new_tab2_html, 'html.parser')
    tab2.replace_with(new_tab2.div)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Tab 2 updated.")
else:
    print("Tab 2 not found")
