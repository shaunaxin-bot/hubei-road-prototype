import sys
import docx

doc_path = r'C:\AIprojects\roaddata\hubei\release\project\资料\数据治理工程招标技术要求0803.docx'
try:
    doc = docx.Document(doc_path)
    # just print the lines, using utf-8 stdout
    sys.stdout.reconfigure(encoding='utf-8')
    for p in doc.paragraphs:
        text = p.text.strip()
        if text:
            print(text)
except Exception as e:
    print("Error:", e)
