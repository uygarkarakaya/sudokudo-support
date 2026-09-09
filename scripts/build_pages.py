"""Prepare static HTML for GitHub Pages, including project-site URL prefixes."""
import os
from pathlib import Path
import re
import shutil

source = Path('dist')
output = Path('_site')
base = '/' + os.environ.get('PAGES_BASE_PATH', '').strip('/')
base = '' if base == '/' else base
if not re.fullmatch(r'(?:/[A-Za-z0-9._-]+)*', base):
    raise ValueError('PAGES_BASE_PATH must be an empty string or a URL path')

if output.exists():
    shutil.rmtree(output)
shutil.copytree(source, output)

def rewrite(match):
    attribute, path = match.groups()
    if path.startswith('//'):
        return match.group(0)
    path = re.sub(r'^/(privacy|support)(?=#|$)', r'/\1/', path)
    return f'{attribute}="{base}{path}"'

for page in output.glob('*.html'):
    html = re.sub(r'(href|src)="(/[^\"]*)"', rewrite, page.read_text())
    if page.stem in ('privacy', 'support'):
        destination = output / page.stem / 'index.html'
        destination.parent.mkdir(exist_ok=True)
        destination.write_text(html)
        page.unlink()
    else:
        page.write_text(html)
(output / '.nojekyll').touch()
print(f'GitHub Pages site prepared in _site (base path: {base or "/"})')
