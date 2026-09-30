import os
from PIL import Image

for f in sorted(os.listdir('extracted_assets')):
    if f.endswith(('.png', '.jpeg', '.jpg')):
        p = os.path.join('extracted_assets', f)
        im = Image.open(p)
        print(f"{f}: size={im.size} mode={im.mode} format={im.format}")
