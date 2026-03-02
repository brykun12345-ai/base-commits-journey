"""checks that each doc starts with an H1"""
from pathlib import Path
import sys

def check(path):
    lines = Path(path).read_text(encoding='utf-8').splitlines()
    return lines and lines[0].startswith('# ')

if __name__ == '__main__':
    bad = [str(f) for f in Path('docs').rglob('*.md') if not check(f)]
    if bad:
        print('Missing H1:', bad)
        sys.exit(1)
    print('Headings OK')

