#!/usr/bin/env python3
import re
from pathlib import Path

REPO_PATH = "/Users/klausludemann/Documents/GitHub/TeamDialog/docs"

def remove_complianz(html_files):
    print("Removing Complianz...")
    updated = 0
    
    for html_file in html_files:
        try:
            content = html_file.read_text(encoding='utf-8')
            original = content
            
            # Remove Complianz CSS
            content = re.sub(r'<link[^>]*complianz[^>]*>', '', content, flags=re.IGNORECASE)
            
            # Remove Complianz script
            content = re.sub(r'<script[^>]*>.*?var complianz = \{.*?\};.*?</script>', '', content, flags=re.DOTALL)
            
            # Remove Complianz style
            content = re.sub(r'<style>\.cmplz-hidden\{display:none!important;\}</style>', '', content)
            
            if content != original:
                html_file.write_text(content, encoding='utf-8')
                print(f"✓ {html_file.name}")
                updated += 1
        except Exception as e:
            print(f"✗ {html_file}: {e}")
    
    return updated

def add_simple_banner(html_files):
    print("\nAdding simple cookie notice...")
    
    banner = '''
<style>
.cookie-notice{position:fixed;bottom:0;left:0;right:0;background:#2c3e50;color:#fff;padding:20px;text-align:center;z-index:9999;box-shadow:0 -2px 10px rgba(0,0,0,0.1)}
.cookie-notice p{margin:0 0 15px;font-size:14px}
.cookie-notice button{padding:10px 20px;margin:5px;border:none;border-radius:4px;cursor:pointer;font-size:14px}
.cookie-accept{background:#27ae60;color:#fff}
.cookie-decline{background:#95a5a6;color:#fff}
</style>
<div class="cookie-notice" id="cookieNotice" style="display:none">
<p><strong>🍪 Diese Website verwendet Cookies</strong><br>Wir verwenden Cookies, um Ihnen die beste Erfahrung zu bieten. <a href="datenschutz/" style="color:#3498db">Datenschutzerklärung</a></p>
<button class="cookie-accept" onclick="acceptCookies()">Akzeptieren</button>
<button class="cookie-decline" onclick="declineCookies()">Ablehnen</button>
</div>
<script>
function acceptCookies(){localStorage.setItem('cookieConsent','yes');document.getElementById('cookieNotice').style.display='none'}
function declineCookies(){localStorage.setItem('cookieConsent','no');document.getElementById('cookieNotice').style.display='none'}
if(!localStorage.getItem('cookieConsent')){document.getElementById('cookieNotice').style.display='block'}
</script>
'''
    
    updated = 0
    for html_file in html_files:
        try:
            content = html_file.read_text(encoding='utf-8')
            if 'cookieNotice' not in content and '</body>' in content:
                content = content.replace('</body>', banner + '\n</body>')
                html_file.write_text(content, encoding='utf-8')
                print(f"✓ {html_file.name}")
                updated += 1
        except Exception as e:
            print(f"✗ {html_file}: {e}")
    
    return updated

html_files = [f for f in Path(REPO_PATH).rglob('*.html') if 'wp-admin' not in str(f)]
print(f"Found {len(html_files)} HTML files\n")

removed = remove_complianz(html_files)
added = add_simple_banner(html_files)

print(f"\n✅ Done! Removed from {removed} files, added to {added} files")
print("\nNext: Open GitHub Desktop, review changes, commit & push!")
