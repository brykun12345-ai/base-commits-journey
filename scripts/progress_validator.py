"""validates PROGRESS.md IDs are sequential"""
import re, sys
from pathlib import Path

def validate(path='PROGRESS.md'):
    text = Path(path).read_text(encoding='utf-8')
    ids = [int(m) for m in re.findall(r'P-(\d+)', text)]
    if ids != list(range(1, len(ids)+1)):
        print('Non-sequential IDs:', ids)
        return False
    print(f'Progress IDs OK ({len(ids)} entries)')
    return True

if __name__ == '__main__':
    sys.exit(0 if validate() else 1)

