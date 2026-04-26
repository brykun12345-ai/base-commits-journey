#!/usr/bin/env python3
"""Reads ROADMAP.md and prints unchecked tasks."""
from pathlib import Path

def next_tasks():
    text = Path('ROADMAP.md').read_text(encoding='utf-8')
    tasks = [l.strip() for l in text.splitlines() if l.strip().startswith('- [ ]')]
    if tasks:
        print("Pending roadmap tasks:")
        for t in tasks:
            print(" ", t)
    else:
        print("All roadmap tasks complete!")

if __name__ == '__main__':
    next_tasks()
