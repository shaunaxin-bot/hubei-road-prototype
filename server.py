import os
import sys

import sys
import os
if sys.stdout is None:
    sys.stdout = open(os.devnull, 'w')
if sys.stderr is None:
    sys.stderr = open(os.devnull, 'w')

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

import json
import re

def parse_markdown_rules():
    # Use path relative to server.py: ../../RoadData_KnowledgeBase
    base_path = os.path.normpath(os.path.join(BASE_DIR, "..", "..", "RoadData_KnowledgeBase"))
    paths = {
        "universal": os.path.join(base_path, "02_RuleEngine_业务口径与计算规则库"),
        "scenario": os.path.join(base_path, "03_WorkflowBuilder_多智能体协同场景库")
    }
    
    rules = {}
    lcode_pattern = re.compile(r'\b(L\d{2}[a-zA-Z]?)\b', re.IGNORECASE)
    
    for rule_type, folder in paths.items():
        if not os.path.exists(folder):
            continue
            
        for root, _, files in os.walk(folder):
            for file in files:
                if not file.endswith(".md"):
                    continue
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        
                    sections = re.split(r'(?m)^(#{2,3})\s+', content)
                    current_header = file.replace(".md", "")
                    
                    intro = sections[0]
                    intro_codes = set(l.lower() for l in lcode_pattern.findall(intro))
                    for code in intro_codes:
                        if code not in rules:
                            rules[code] = {"universal": [], "scenario": []}
                        snippet = intro.strip()
                        if snippet:
                            rules[code][rule_type].append({"file": file, "section": "概要", "snippet": snippet})
                            
                    for i in range(1, len(sections), 2):
                        # i is the hashes, i+1 is the content
                        body = sections[i+1]
                        lines = body.split("\n", 1)
                        section_title = lines[0].strip() if len(lines) > 0 else ""
                        section_content = lines[1].strip() if len(lines) > 1 else ""
                        
                        section_codes = set(l.lower() for l in lcode_pattern.findall(section_title + "\n" + section_content))
                        
                        for code in section_codes:
                            if code not in rules:
                                rules[code] = {"universal": [], "scenario": []}
                            snippet_text = section_content.strip()
                            rules[code][rule_type].append({
                                "file": file, 
                                "section": section_title, 
                                "snippet": snippet_text
                            })
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")
                    
    return rules

RULES_CACHE = parse_markdown_rules()

def parse_master_materials():
    path = r"C:\AIprojects\roaddata\RoadData_KnowledgeBase\01_DataMapper_表结构与数据映射引擎\前端业务需求字典\1.5_收集业务要求_主字典(Tab1).md"
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading Tab1: {e}")
        return {}
    
    data = {}
    current_dept = None
    current_doc = None
    
    lines = content.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            dept_name = line.replace("# ", "").strip()
            if "1.5 收集业务要求" not in dept_name:
                current_dept = dept_name
                data[current_dept] = []
        elif line.startswith("## ") and current_dept is not None:
            doc_name = line.replace("## ", "").strip()
            current_doc = {
                "name": doc_name,
                "url": "#",
                "date": "",
                "dataset": "",
                "product": "",
                "agents": [],
                "history": []
            }
            data[current_dept].append(current_doc)
        elif line.startswith("- **") and current_doc is not None:
            match = re.match(r"-\s*\*\*(.*?)\*\*:\s*(.*)", line)
            if match:
                key_cn = match.group(1).strip()
                val = match.group(2).strip()
                
                if key_cn == "提报日期":
                    current_doc["date"] = val
                elif key_cn == "高质量数据集":
                    current_doc["dataset"] = val
                elif key_cn == "数据产品":
                    current_doc["product"] = val
                elif key_cn == "关联智能体":
                    agents_list = []
                    if val:
                        parts = val.split(",")
                        for p in parts:
                            p = p.strip()
                            if not p: continue
                            ap = p.split("|")
                            if len(ap) >= 6:
                                agents_list.append({
                                    "id": ap[0].strip(),
                                    "name": ap[1].strip(),
                                    "type": ap[2].strip(),
                                    "isVeto": ap[3].strip().lower() == "true",
                                    "isCrossBlock": ap[4].strip().lower() == "true",
                                    "blockName": ap[5].strip()
                                })
                    current_doc["agents"] = agents_list
                elif key_cn == "流转历史":
                    hist_list = []
                    if val:
                        parts = val.split(" || ")
                        for p in parts:
                            p = p.strip()
                            if not p: continue
                            hp = p.split("|")
                            if len(hp) >= 4:
                                hist_list.append({
                                    "date": hp[0].strip(),
                                    "desc": hp[1].strip(),
                                    "isVetoTrigger": hp[2].strip().lower() == "true",
                                    "isStandardTrigger": hp[3].strip().lower() == "true"
                                })
                    current_doc["history"] = hist_list
    return data

def parse_agent_to_docs():
    path = r"C:\AIprojects\roaddata\RoadData_KnowledgeBase\01_DataMapper_表结构与数据映射引擎\前端业务需求字典\1.5_智能体与关联材料_反向映射表(Tab2).md"
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading Tab2: {e}")
        return {}
    
    data = {}
    current_agent = None
    
    lines = content.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("## "):
            agent_id = line.replace("## ", "").strip()
            current_agent = {
                "id": agent_id,
                "name": "",
                "docs": []
            }
            data[agent_id] = current_agent
        elif line.startswith("- **") and current_agent is not None:
            match = re.match(r"-\s*\*\*(.*?)\*\*:\s*(.*)", line)
            if match:
                key_cn = match.group(1).strip()
                val = match.group(2).strip()
                if key_cn == "智能体岗位":
                    current_agent["name"] = val
                elif key_cn == "关联材料列表":
                    if val:
                        current_agent["docs"] = [d.strip() for d in val.split(",") if d.strip()]
                    else:
                        current_agent["docs"] = []
    return data

import base64
import urllib.parse
from http.server import SimpleHTTPRequestHandler, HTTPServer

import re

def parse_requirements():
    path = r"C:\AIprojects\roaddata\RoadData_KnowledgeBase\01_DataMapper_表结构与数据映射引擎\前端业务需求字典\1.5_收集业务要求与数据字典.md"
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading requirements: {e}")
        return []
    
    reqs = []
    current_req = None
    
    lines = content.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("## "):
            if current_req:
                reqs.append(current_req)
            current_req = {"id": line.replace("## ", "").strip()}
        elif line.startswith("- **") and current_req:
            match = re.match(r"-\s*\*\*(.*?)\*\*:\s*(.*)", line)
            if match:
                key_cn = match.group(1).strip()
                val = match.group(2).strip()
                
                key_map = {
                    "板块": "block",
                    "岗位/角色": "role",
                    "业务描述": "desc",
                    "安全等级": "level",
                    "高质量数据集": "dataset",
                    "数据产品": "product",
                    "三网四模型价值": "modelValue",
                    "转型价值贡献": "improvement",
                    "关联资料": "docs",
                    "当前状态": "status"
                }
                
                eng_key = key_map.get(key_cn)
                if eng_key:
                    if eng_key == "docs":
                        if val:
                            req_val = [d.strip() for d in val.split(",") if d.strip()]
                        else:
                            req_val = []
                    elif eng_key == "improvement":
                        req_val = val.replace(" ； ", "\n")
                    else:
                        req_val = val
                    current_req[eng_key] = req_val
    if current_req:
        reqs.append(current_req)
    
    # Reconstruct goals array for React UI compatibility
    for r in reqs:
        if "goals" not in r:
            goals = []
            imp = r.get("improvement", "")
            parts = imp.split("\n")
            colors = ["text-emerald-600", "text-blue-600", "text-purple-600"]
            for i, p in enumerate(parts):
                if p.strip():
                    title = "转型价值量化"
                    if "【提质】" in p:
                        title = "聚焦核心履职，提升业务效能"
                    elif "【提效】" in p:
                        title = "优化业务流程，压缩流转时效"
                    color = colors[i % len(colors)]
                    goals.append({"title": title, "desc": p.strip(), "color": color})
            if len(goals) < 3:
                goals.append({"title": "扩大监控覆盖，夯实安全底线", "desc": "核心风险点100%覆盖监控", "color": "text-purple-600"})
            r["goals"] = goals
            
    return reqs



PORT = 8000

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # 核心：设置最严格的反缓存响应头，强制浏览器每次重新请求，杜绝磁盘缓存旧 JS/HTML
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path == '/api/ontology/rules_all':
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            # Return summary of rules for badges
            summary = {k: len(v['universal']) + len(v['scenario']) for k, v in RULES_CACHE.items()}
            self.wfile.write(json.dumps(summary).encode('utf-8'))
            return
        elif self.path.startswith('/api/ontology/rules?'):
            import urllib.parse as _up
            qs = _up.parse_qs(_up.urlparse(self.path).query)
            l_code = qs.get('l_code', [''])[0].lower()
            data = RULES_CACHE.get(l_code, {"universal": [], "scenario": []})
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
            return
        elif self.path.startswith('/api/scenario/rules?'):
            import urllib.parse as _up
            qs = _up.parse_qs(_up.urlparse(self.path).query)
            scen_num = qs.get('scen_num', ['1'])[0]
            
            scen_files = {
                '1': '场景1_汛期预警防御与应急处置.md',
                '2': '场景2_长大桥结构监测数据质量管理.md',
                '3': '场景3(专业)_年报业务.md',
                '4': '场景3(基础)_年报查询.md'
            }
            
            # Use path relative to server.py: ../../RoadData_KnowledgeBase
            scen_base = os.path.normpath(os.path.join(BASE_DIR, "..", "..", "RoadData_KnowledgeBase", "03_WorkflowBuilder_多智能体协同场景库"))
            filepath = os.path.join(scen_base, filename)
            
            content = ""
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(json.dumps({"markdown": content}).encode('utf-8'))
            return
        elif self.path == '/api/get_master_materials':
            data = parse_master_materials()
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
            return
        elif self.path == '/api/get_agent_to_docs':
            data = parse_agent_to_docs()
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
            return
        elif self.path == '/api/get_requirements':
            reqs = parse_requirements()
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(json.dumps(reqs).encode('utf-8'))
        elif self.path == '/api/get_template':
            template_content = ""
            try:
                template_path = r"C:\AIprojects\roaddata\RoadData_KnowledgeBase\03_WorkflowBuilder_多智能体协同场景库\UI与报表模板库\ui_templates.md"
                if os.path.exists(template_path):
                    with open(template_path, "r", encoding="utf-8") as f:
                        template_content = f.read()
            except Exception as e:
                print(f"Error reading template: {e}")
            
            self.send_response(200)
            self.send_header('Content-type', 'text/markdown; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(template_content.encode('utf-8'))
        elif self.path == '/api/get_keys':
            keys = {}
            try:
                config_path = r"C:\AIprojects\roaddata\RoadData_KnowledgeBase\06_Governance_系统治理与开发规范\API与系统配置\API与模型配置.md"
                if os.path.exists(config_path):
                    with open(config_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    import re
                    match = re.search(r"```json\s*(\{.*?\})\s*```", content, re.DOTALL)
                    if match:
                        keys = json.loads(match.group(1))
            except Exception as e:
                print(f"Error reading keys: {e}")
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(json.dumps(keys).encode('utf-8'))
        elif self.path.split('?', 1)[0].startswith('/hubei_'):
            # Serve sqlite databases from the public folder or root
            clean_path = self.path.split('?', 1)[0]
            public_path = os.path.join(BASE_DIR, 'public', clean_path.lstrip('/'))
            if os.path.exists(public_path):
                self.path = '/public' + self.path
            return SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/api/list_years':
            # Step2: 返回 public/ 下已有的年份数据库列表
            public_dir = os.path.join(BASE_DIR, 'public')
            years = []
            if os.path.exists(public_dir):
                import glob, json as _json
                for db_file in sorted(glob.glob(os.path.join(public_dir, 'hubei_*.db'))):
                    meta_file = db_file + '.meta'
                    import re
                    year_match = re.search(r'hubei_(\d{4})', os.path.basename(db_file))
                    if not year_match: continue
                    year = int(year_match.group(1))
                    tables = []
                    if os.path.exists(meta_file):
                        try:
                            meta = _json.load(open(meta_file, encoding='utf-8'))
                            tables = meta.get('tables', [])
                        except:
                            pass
                    if not tables:
                        import sqlite3
                        try:
                            conn = sqlite3.connect(db_file)
                            cursor = conn.cursor()
                            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                            for row in cursor.fetchall():
                                tname = row[0]
                                cursor.execute(f"SELECT COUNT(*) FROM `{tname}`")
                                count = cursor.fetchone()[0]
                                tables.append({'lcode': tname, 'raw': tname, 'rows': count})
                            conn.close()
                        except:
                            pass
                    years.append({'year': year, 'db': db_file, 'tables': tables,
                                  'size_mb': round(os.path.getsize(db_file)/1048576, 1)})
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(json.dumps(years).encode('utf-8'))
        elif self.path.startswith('/api/year_tables'):
            # Step2: 返回指定年份的表名+行数列表
            import urllib.parse as _up
            qs = _up.parse_qs(_up.urlparse(self.path).query)
            year = qs.get('year', [None])[0]
            tables = []
            if year:
                public_dir = os.path.join(BASE_DIR, 'public')
                meta_file = os.path.join(public_dir, f'hubei_{year}.db.meta')
                if os.path.exists(meta_file):
                    try:
                        meta = json.load(open(meta_file, encoding='utf-8'))
                        tables = meta.get('tables', [])
                    except:
                        pass
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(json.dumps(tables).encode('utf-8'))
        else:
            SimpleHTTPRequestHandler.do_GET(self)


    def do_POST(self):
        if self.path == '/api/scan_folder':
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                payload = __import__('json').loads(self.rfile.read(content_length).decode('utf-8'))
                folder_path = payload.get('folderPath', '')
                if not os.path.isdir(folder_path):
                    raise ValueError(f'Invalid folder: {folder_path}')
                public_dir = os.path.join(BASE_DIR, 'public')
                import importlib, sys as _sys
                scripts_dir = os.path.join(BASE_DIR, 'scripts')
                if scripts_dir not in _sys.path:
                    _sys.path.insert(0, scripts_dir)
                import scan_and_import as _sai
                importlib.reload(_sai)
                results = _sai.scan_folder(folder_path, public_dir)
                # tables lists may contain non-serialisable objects; safe convert
                self.send_response(200)
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(__import__('json').dumps({'success': True, 'results': results}).encode('utf-8'))
            except Exception as e:
                print(f'scan_folder error: {e}')
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(__import__('json').dumps({'success': False, 'error': str(e)}).encode('utf-8'))
            return
        elif self.path == '/api/execute_sql':
            # Step 6: 对指定年份的 SQLite 数据库执行 SQL 查询
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                payload = __import__('json').loads(self.rfile.read(content_length).decode('utf-8'))
                sql = payload.get('sql', '').strip()
                year = payload.get('year')
                if not sql:
                    raise ValueError('SQL is empty')
                public_dir = os.path.join(BASE_DIR, 'public')
                # Find the db file for this year
                import glob, sqlite3 as _sqlite3
                if year:
                    db_path = os.path.join(public_dir, f'hubei_{int(year)}.db')
                else:
                    # Use the most recent db
                    dbs = sorted(glob.glob(os.path.join(public_dir, 'hubei_*.db')))
                    db_path = dbs[-1] if dbs else None
                if not db_path or not os.path.exists(db_path):
                    raise FileNotFoundError(f'数据库 {year} 年不存在，请先加载数据')
                conn = _sqlite3.connect(db_path)
                conn.row_factory = _sqlite3.Row
                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                columns = [d[0] for d in cur.description] if cur.description else []
                values = [list(r) for r in rows]
                conn.close()
                result = {'columns': columns, 'rows': values, 'row_count': len(values), 'year': year}
                self.send_response(200)
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(__import__('json').dumps(result).encode('utf-8'))
            except Exception as e:
                print(f'execute_sql error: {e}')
                self.send_response(200)  # Return 200 with error in JSON so frontend can handle
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(__import__('json').dumps({'error': str(e), 'row_count': 0}).encode('utf-8'))
            return
        elif self.path == '/api/save_excel':

            try:
                # Read content length
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length)
                
                # Parse JSON payload
                payload = json.loads(post_data.decode('utf-8'))
                filename = payload.get('filename', 'G107国道里程统计报告.xlsx')
                base64_data = payload.get('base64Data', '')
                
                if not base64_data:
                    raise ValueError("Base64 data is empty.")
                
                # Target output directory
                target_dir = r"C:\AIprojects\roaddata\hubei\customer\上报数据\养护统计年报\workbuddyetc"
                os.makedirs(target_dir, exist_ok=True)
                
                target_file_path = os.path.join(target_dir, filename)
                
                # Decode base64 and write binary
                excel_bytes = base64.b64decode(base64_data)
                with open(target_file_path, "wb") as f:
                    f.write(excel_bytes)
                
                print(f"Successfully saved Excel file to: {target_file_path}")
                
                # Send JSON response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                response = {
                    "success": True,
                    "filename": filename,
                    "path": target_file_path
                }
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                print(f"Error saving Excel file: {e}")
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def translate_path(self, path):
        # 先用默认逻辑得到文件系统路径
        result = SimpleHTTPRequestHandler.translate_path(self, path)
        # 如果文件不存在，尝试在 public/ 子目录中找
        if not os.path.exists(result):
            base = BASE_DIR
            # 取 URL path 的纯文件名部分
            import urllib.parse
            url_path = urllib.parse.urlparse(path).path.lstrip('/')
            candidate = os.path.join(base, 'public', url_path)
            if os.path.exists(candidate):
                return candidate
        return result

def run():
    target_dir = r"C:\AIprojects\roaddata\hubei\customer\上报数据\养护统计年报\workbuddyetc"
    print(f"=======================================================")
    print(f"本地服务器启动就绪，已开启最高级别无缓存模式，端口: {PORT}")
    print(f"Excel 导出目标物理目录已锁定:")
    print(f"  {target_dir}")
    print(f"=======================================================")
    
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    run()
