#!/usr/bin/env python3
import re
import os
from pathlib import Path

REPO_PATH = "/Users/klausludemann/Documents/GitHub/TeamDialog/docs"

def convert_img_to_picture(match):
    full_tag = match.group(0)
    if '<picture>' in full_tag or 'logo' in full_tag.lower():
        return full_tag
    
    src_match = re.search(r'src=["\']([^"\']+\.(?:jpg|jpeg|png))["\']', full_tag, re.IGNORECASE)
    if not src_match:
        return full_tag
    
    img_src = src_match.group(1)
    webp_src = re.sub(r'\.(jpg|jpeg|png)$', '.webp', img_src, flags=re.IGNORECASE)
    
    picture = f'<picture>\n    <source srcset="{webp_src}" type="image/webp">\n    {full_tag}\n</picture>'
    return picture

def update_html_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content
        pattern = r'<img(?![^>]*logo)[^>]*src=["\'](?:[^"\']*\.(?:jpg|jpeg|png))["\'][^>]*/?>'
        content = re.sub(pattern, convert_img_to_picture, content, flags=re.IGNORECASE)
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error: {filepath}: {e}")
        return False

os.chdir(REPO_PATH)
html_files = [f for f in Path('.').rglob('*.html') if 'wp-admin' not in str(f)]
print(f"Updating {len(html_files)} HTML files...")
updated = sum(1 for f in html_files if update_html_file(f))
print(f"✅ Updated {updated} files!")
