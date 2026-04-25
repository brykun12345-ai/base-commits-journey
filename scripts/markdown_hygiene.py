"""checks markdown files for common issues"""
from pathlib import Path
import sys

def check(path):
    lines = Path(path).read_text(encoding='utf-8').splitlines()
    issues = []
    for i, line in enumerate(lines, 1):
        if line.rstrip() != line:
            issues.append(f'line {i}: trailing whitespace')
    return issues

if __name__ == '__main__':
    errors = []
    for f in Path('.').rglob('*.md'):
        for issue in check(f):
            errors.append(f'{f}: {issue}')
    if errors:
        print('\n'.join(errors))
        sys.exit(1)
    print('Markdown hygiene OK')

