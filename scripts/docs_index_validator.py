"""validates docs README lists all guide files"""
from pathlib import Path
import sys

def validate():
    index = (Path('docs')/'README.md').read_text(encoding='utf-8')
    guides = [f.name for f in Path('docs').glob('*.md') if f.name != 'README.md']
    missing = [g for g in guides if g not in index]
    if missing:
        print('Undocumented guides:', missing)
        return False
    print('Docs index OK')
    return True

if __name__ == '__main__':
    sys.exit(0 if validate() else 1)

