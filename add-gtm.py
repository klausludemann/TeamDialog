#!/usr/bin/env python3
import re
from pathlib import Path

REPO = "/Users/klausludemann/Documents/GitHub/TeamDialog/docs"
GTM_ID = "GTM-KSFNCKX6"

# GTM Head code
gtm_head = f'''<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','{GTM_ID}');</script>
<!-- End Google Tag Manager -->
'''

# GTM Body code
gtm_body = f'''<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
'''

html_files = [f for f in Path(REPO).rglob('*.html') if 'wp-admin' not in str(f)]
print(f"Found {len(html_files)} HTML files\n")

updated = 0
skipped = 0

for html_file in html_files:
    try:
        content = html_file.read_text(encoding='utf-8')
        
        # Skip if GTM already added
        if 'GTM-KSFNCKX6' in content:
            print(f"⊘ {html_file.name} - Already has GTM")
            skipped += 1
            continue
        
        # Add to <head> (after <head> tag)
        if '<head>' in content:
            content = content.replace('<head>', '<head>\n' + gtm_head, 1)
        else:
            print(f"✗ {html_file.name} - No <head> tag found!")
            continue
        
        # Add to <body> (after <body> tag)
        body_match = re.search(r'<body[^>]*>', content)
        if body_match:
            insert_pos = body_match.end()
            content = content[:insert_pos] + '\n' + gtm_body + content[insert_pos:]
        else:
            print(f"✗ {html_file.name} - No <body> tag found!")
            continue
        
        # Save
        html_file.write_text(content, encoding='utf-8')
        print(f"✓ {html_file.name}")
        updated += 1
        
    except Exception as e:
        print(f"✗ {html_file.name} - Error: {e}")

print(f"\n✅ Done! Updated {updated} files, skipped {skipped}")
print("\nNext: Review in GitHub Desktop, commit, and push!")
