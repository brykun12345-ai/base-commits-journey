"""warns about files over 1 MB"""
from pathlib import Path
import sys

LIMIT = 1024 * 1024

if __name__ == '__main__':
    big = [str(f) for f in Path('.').rglob('*') if f.is_file() and f.stat().st_size > LIMIT]
    if big:
        print('Large files:', big)
        sys.exit(1)
    print('File sizes OK')

