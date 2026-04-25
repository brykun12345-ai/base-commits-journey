"""checks for broken markdown links"""
import re, sys
from pathlib import Path

def find_links(text):
    return re.findall(r'\[.*?\]\((http[^)]+)\)', text)

def check_file(path):
    text = Path(path).read_text(encoding='utf-8')
    return find_links(text)

if __name__ == '__main__':
    for f in Path('docs').rglob('*.md'):
        links = check_file(f)
        for l in links:
            print(f'{f}: {l}')

