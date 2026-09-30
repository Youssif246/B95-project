import json

with open('pdf_extracted_text.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    txt = p['text'].strip()
    lines = [line.strip() for line in txt.splitlines() if line.strip()]
    header = ' // '.join(lines[:4]) if lines else '[EMPTY PAGE]'
    print(f"=== Page {p['page']} ===")
    print(header[:150])
    print("Total lines:", len(lines))
