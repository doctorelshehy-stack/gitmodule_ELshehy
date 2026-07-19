#!/usr/bin/env python3
"""Test v2.1 — table slide + broader testing"""
import sys
sys.path.insert(0, "/media/mohamed/projects4/git/raw material/GIT Presentation")
from transform_v2 import *

BASE = "/media/mohamed/projects4/git/raw material/GIT Presentation"

# Test table slide
print("TABLE SLIDE (diverticula/slide-13):")
html = open(f"{BASE}/surgery_diverticula_hernias/slides/slide-13.html").read()
soup = BeautifulSoup(html, "lxml")
cols = find_content_columns(soup)
print(f"  Columns: {len(cols)}")
for i, col in enumerate(cols):
    blocks = process_column_content(col)
    print(f"  Col {i}: {len(blocks)} blocks")
    for j, b in enumerate(blocks):
        print(f"    [{j}] type={b['type']}, len={len(b['html'])}")

# Generate and check
new_html = transform_slide(html, "slide-13.html")
with open("/tmp/test_slide_13.html", "w") as f:
    f.write(new_html)
new_soup = BeautifulSoup(new_html, "lxml")
print(f"  New text length: {len(new_soup.get_text(strip=True))}")
print(f"  Has table: {'tbl' in new_html}")

# Test ALL slides in stomach (27 slides)
print("\n\nBROAD TEST: surgery_stomach (27 slides)")
import os
slide_dir = f"{BASE}/surgery_stomach/slides"
for fname in sorted(os.listdir(slide_dir)):
    if not fname.endswith(".html"):
        continue
    fpath = f"{slide_dir}/{fname}"
    html = open(fpath).read()
    title = extract_title(html)
    is_c = is_cover(html)
    soup = BeautifulSoup(html, "lxml")
    cols = find_content_columns(soup)
    total_blocks = sum(len(process_column_content(c)) for c in cols)
    status = "COVER" if is_c else f"{len(cols)} cols, {total_blocks} blocks"
    print(f"  {fname}: {title[:40]} — {status}")

# Test a few slides from other presentations
print("\n\nBROAD TEST: Other presentations (sample)")
test_files = [
    ("surgery_esophagus/slides/slide-01.html", "Cover"),
    ("surgery_esophagus/slides/slide-12.html", "Two-col"),
    ("surgery_liver/slides/slide-08.html", "Two-col"),
    ("surgery_oral_anal/slides/slide-03.html", "Two-col"),
    ("surgery_intestine_peritoneum/slides/slide-05.html", "Three-col cards"),
    ("surgery_pancreas_appendix/slides/slide-01.html", "Cover"),
]
for fpath, desc in test_files:
    html = open(f"{BASE}/{fpath}").read()
    title = extract_title(html)
    soup = BeautifulSoup(html, "lxml")
    cols = find_content_columns(soup)
    total_blocks = sum(len(process_column_content(c)) for c in cols)
    print(f"  {fpath}: {title[:40]} — {len(cols)} cols, {total_blocks} blocks [{desc}]")

print("\nDONE")
