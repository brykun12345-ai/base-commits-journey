"""validates required repo files exist"""
from pathlib import Path

REQUIRED = ['README.md','LICENSE','CONTRIBUTING.md','CHANGELOG.md']

def validate(root='.'):
    missing = [f for f in REQUIRED if not (Path(root)/f).exists()]
    if missing:
        print('Missing:', missing)
        return False
    print('Repo structure OK')
    return True

if __name__ == '__main__':
    import sys
    sys.exit(0 if validate() else 1)

