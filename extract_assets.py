import pymupdf
import os

doc = pymupdf.open('PROFİLE ENGLISH.pdf')
os.makedirs('extracted_assets', exist_ok=True)

img_count = 0
for i, page in enumerate(doc):
    image_list = page.get_images(full=True)
    if image_list:
        print(f"Page {i+1} has {len(image_list)} images")
        for j, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            img_filename = f"extracted_assets/p{i+1}_img{j+1}_{xref}.{image_ext}"
            with open(img_filename, "wb") as f:
                f.write(image_bytes)
            img_count += 1

print(f"Extracted {img_count} images to extracted_assets/")
