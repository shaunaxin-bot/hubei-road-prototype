import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    text = f.read()

start_str = 'window.__STAGE_TREE_DATA__ : ['
idx1 = text.find(start_str)
if idx1 != -1:
    idx = idx1 + len(start_str) - 1 # index of '['
    depth = 0
    in_string = False
    escape = False
    for i in range(idx, len(text)):
        char = text[i]
        if in_string:
            if escape:
                escape = False
            elif char == '\\\\':
                escape = True
            elif char == '"':
                in_string = False
        else:
            if char == '"':
                in_string = True
            elif char == '[':
                depth += 1
            elif char == ']':
                depth -= 1
                if depth == 0:
                    idx2 = i + 1
                    print('Found end at', idx2)
                    print(text[idx2-50:idx2+20].encode('unicode_escape').decode('utf-8'))
                    
                    new_scenarios = ''',
      { stage: "安全生产责任数据运营", color: "#ef4444", icon: "🛡️", tables: [
        { lcode: "L41", name: "L41（安全隐患排查治理台账）", macroAgent: "AGENT-数据统筹-安全生产责任数据运营中心", subTables: [
          { name: "安全隐患明细表", microAgent: "AGENT-数据统筹-安全生产责任数据运营中心", isCompiled: false }
        ] }
      ] },
      { stage: "公路资产数据运营", color: "#eab308", icon: "🛣️", tables: [
        { lcode: "L51", name: "L51（公路资产动态台账）", macroAgent: "01 规划计划处", subTables: [
          { name: "资产入账明细表", microAgent: "01 规划计划处", isCompiled: false }
        ] }
      ] }'''
                    
                    # Insert the new_scenarios right before the closing bracket of the array
                    new_array = text[idx1:idx2-1] + new_scenarios + text[idx2-1:]
                    new_text = text[:idx1] + new_array + text[idx2:]
                    
                    with codecs.open('index.html', 'w', 'utf-8') as fw:
                        fw.write(new_text)
                    print('Successfully updated index.html')
                    break
