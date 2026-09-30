import json

with open('pdf_extracted_text.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('all_pdf_text_dump.txt', 'w', encoding='utf-8') as out:
    for p in data:
        out.write(f"\n{'='*30} PAGE {p['page']} {'='*30}\n")
        out.write(p['text'])
        out.write("\n")

print("Dumped all_pdf_text_dump.txt")
