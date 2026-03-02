"""detects CRLF line endings in text files"""
from pathlib import Path
import sys

def check(path):
    return b'\r\n' in Path(path).read_bytes()

if __name__ == '__main__':
    bad = [str(f) for f in Path('.').rglob('*.md') if check(f)]
    if bad:
        print('CRLF found:', bad)
        sys.exit(1)
    print('Line endings OK')

