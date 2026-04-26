#!/usr/bin/env python3
"""CLI that suggests the next atomic commit based on PROGRESS.md."""
import sys
from pathlib import Path

def suggest():
    text = Path('PROGRESS.md').read_text(encoding='utf-8')
    lines = [l for l in text.splitlines() if l.startswith('|') and 'pending' in l]
    if lines:
        print("Next task:", lines[0])
    else:
        print("All tasks complete! Consider adding Phase 2.")

if __name__ == '__main__':
    suggest()
