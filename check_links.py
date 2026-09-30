import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

imgs = re.findall(r'src=["\']([^"\']+)["\']', html)
print(f"Found {len(imgs)} image/script tags.")
all_ok = True
for src in imgs:
    norm_path = os.path.normpath(src)
    if os.path.exists(norm_path):
        print(f"OK: {src} ({os.path.getsize(norm_path)} bytes)")
    else:
        print(f"MISSING: {src}")
        all_ok = False

if all_ok:
    print("ALL ASSETS VERIFIED SUCCESSFULLY.")
