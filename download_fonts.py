import urllib.request
import re
import os

os.makedirs('fonts', exist_ok=True)
url = 'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
css = urllib.request.urlopen(req).read().decode('utf-8')

faces = re.findall(r"font-family:\s*'([^']+)';.*?font-weight:\s*(\d+);.*?src:\s*url\((https://[^\)]+)\)", css, re.DOTALL)
print(f"Found {len(faces)} font faces")

css_local = []
for fam, wt, src in faces:
    clean_fam = fam.replace(" ", "")
    fname = f"fonts/{clean_fam}-{wt}.woff2"
    urllib.request.urlretrieve(src, fname)
    size = os.path.getsize(fname)
    print(f"Saved {fname} ({size} bytes)")
    css_local.append(f"""@font-face {{
  font-family: '{fam}';
  font-style: normal;
  font-weight: {wt};
  font-display: swap;
  src: url('{fname}') format('woff2');
}}""")

with open('fonts/fonts.css', 'w', encoding='utf-8') as f:
    f.write("\n".join(css_local))
print("Saved fonts/fonts.css")
