import docx

doc_path = r'C:\AIprojects\roaddata\hubei\release\project\资料\数据治理工程招标技术要求0803.docx'
try:
    doc = docx.Document(doc_path)
    for i, p in enumerate(doc.paragraphs):
        if p.text.strip():
            print(f"[{i}]: {p.text.strip()}")
except Exception as e:
    print("Error reading docx:", e)
