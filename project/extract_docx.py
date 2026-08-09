import docx

doc_path = r'C:\AIprojects\roaddata\hubei\release\project\资料\数据治理工程招标技术要求0803.docx'
try:
    doc = docx.Document(doc_path)
    with open('docx_content.txt', 'w', encoding='utf-8') as f:
        for i, p in enumerate(doc.paragraphs):
            text = p.text.strip()
            if text:
                f.write(f"[{i}]: {text}\n")
    print("Extracted to docx_content.txt")
except Exception as e:
    print("Error:", e)
