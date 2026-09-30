import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate section positions
services_pos = html.find('id="sec-services"')
range_pos = html.find('id="sec-range"')
references_pos = html.find('id="sec-references"')
featured_pos = html.find('id="sec-featured"')
footer_pos = html.find('id="sec-footer"')

print(f"Services: {services_pos}")
print(f"Range: {range_pos}")
print(f"References: {references_pos}")
print(f"Featured: {featured_pos}")
print(f"Footer: {footer_pos}")
