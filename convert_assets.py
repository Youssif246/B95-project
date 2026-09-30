import os
from PIL import Image

os.makedirs('assets/extracted', exist_ok=True)

for f in sorted(os.listdir('extracted_assets')):
    if f.endswith(('.png', '.jpeg', '.jpg')):
        src = os.path.join('extracted_assets', f)
        dst = os.path.join('assets/extracted', os.path.splitext(f)[0] + '.png')
        try:
            im = Image.open(src)
            # convert CMYK or RGBA to RGB if needed, or keep RGBA for png
            if im.mode == 'CMYK':
                im = im.convert('RGB')
            im.save(dst, format='PNG')
        except Exception as e:
            print(f"Error converting {f}: {e}")

print("All extracted images converted to sRGB PNG in assets/extracted/")
