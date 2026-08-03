import json
import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    text = f.read()

idx1 = text.find('window.__STAGE_TREE_DATA__ : [')
idx2 = text.find('];\n        window.__ER_MAPPING__ =', idx1)
if idx2 == -1:
    idx2 = text.find('];\n          window.__ER_MAPPING__ =', idx1)

new_scenarios = '''},
      { stage: "安全生产责任数据运营", color: "#ef4444", icon: "🛡️", tables: [
        { lcode: "L41", name: "L41（安全隐患排查治理台账）", macroAgent: "AGENT-数据统筹-安全生产责任数据运营中心", subTables: [
          { name: "安全隐患明细表", microAgent: "AGENT-数据统筹-安全生产责任数据运营中心", isCompiled: false }
        ] }
      ] },
      { stage: "公路资产数据运营", color: "#eab308", icon: "🛣️", tables: [
        { lcode: "L51", name: "L51（公路资产动态台账）", macroAgent: "01 规划计划处", subTables: [
          { name: "资产入账明细表", microAgent: "01 规划计划处", isCompiled: false }
        ] }
      ]'''

array_content = text[idx1:idx2]
last_brace_idx = array_content.rfind('}')
if last_brace_idx != -1:
    new_array = array_content[:last_brace_idx+1] + new_scenarios + array_content[last_brace_idx+1:]
    new_text = text[:idx1] + new_array + text[idx2:]
    with codecs.open('index.html', 'w', 'utf-8') as f:
        f.write(new_text)
    print('Success')
else:
    print('Failed')
