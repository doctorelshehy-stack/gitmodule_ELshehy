#!/usr/bin/env python3
import sys, re
sys.path.insert(0, "/media/mohamed/projects4/git/raw material/GIT Presentation")
from bs4 import BeautifulSoup
from transform_v2 import find_content_columns, process_column_content

html = open("/media/mohamed/projects4/git/raw material/GIT Presentation/surgery_pancreas_appendix/slides/slide-04.html").read()
soup = BeautifulSoup(html, "lxml")
cols = find_content_columns(soup)
print(f"Columns found: {len(cols)}")
for i, col in enumerate(cols):
    s = col.get("style", "")
    top = re.search(r"top:(\d+)px", s)
    left = re.search(r"left:(\d+)px", s)
    right = re.search(r"right:(\d+)px", s)
    width = re.search(r"width:(\d+)px", s)
    top_v = top.group(1) if top else "?"
    left_v = left.group(1) if left else "-"
    right_v = right.group(1) if right else "-"
    width_v = width.group(1) if width else "-"
    print(f"  Col {i}: top={top_v} left={left_v} right={right_v} width={width_v}")
    blocks = process_column_content(col)
    print(f"    blocks: {len(blocks)}")
    for b in blocks[:3]:
        print(f"      type={b['type']} preview={b['html'][:60]}")
