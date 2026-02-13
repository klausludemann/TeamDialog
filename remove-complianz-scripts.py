#!/usr/bin/env python3
import re
from pathlib import Path

REPO = "/Users/klausludemann/Documents/GitHub/TeamDialog/docs"

html_files = [f for f in Path(REPO).rglob('*.html') if 'wp-admin' not in str(f)]

for html_file in html_files:
    content = html_file.read_text(encoding='utf-8')
    original = content
    
    # Remove Complianz script tags
    content = re.sub(r'<script[^>]*complianz[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    if content != original:
        html_file.write_text(content, encoding='utf-8')
        print(f"✓ {html_file.name}")

print("Done!")
