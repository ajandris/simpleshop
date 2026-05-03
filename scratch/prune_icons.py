import re
import os

css_path = 'static/css/icons.css'
with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace font-face blocks to only use woff2
# We look for the entire @font-face block and replace its src
def clean_font_face(match):
    block = match.group(0)
    # Determine if it's Solid or Regular based on the block content or name
    if 'fa-solid-900' in block or 'Font Awesome 6 Free' in block and 'font-weight:900' in block.replace(' ', ''):
        new_src = 'src:url("../webfonts/fa-solid-900.woff2") format("woff2");'
    elif 'fa-regular-400' in block or 'Font Awesome 6 Free' in block and 'font-weight:400' in block.replace(' ', ''):
        new_src = 'src:url("../webfonts/fa-regular-400.woff2") format("woff2");'
    else:
        # Fallback to solid if unsure
        new_src = 'src:url("../webfonts/fa-solid-900.woff2") format("woff2");'
    
    # Replace all src: lines in this block
    cleaned_block = re.sub(r'src:[^;]+;', new_src, block)
    return cleaned_block

content = re.sub(r'@font-face\s*\{[^}]+\}', clean_font_face, content)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Pruned icons.css successfully.")
