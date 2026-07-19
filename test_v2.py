#!/usr/bin/env python3
"""Test v2 transform on sample slides"""
import sys
sys.path.insert(0, "/media/mohamed/projects4/git/raw material/GIT Presentation")
from transform_v2 import *

BASE = "/media/mohamed/projects4/git/raw material/GIT Presentation"

# Test 1: Two-column content slide
print("=" * 60)
print("TEST 1: Two-column (stomach/slide-05)")
print("=" * 60)
html = open(f"{BASE}/surgery_stomach/slides/slide-05.html").read()
title = extract_title(html)
print(f"Title: {title}")
soup = BeautifulSoup(html, "lxml")
cols = find_content_columns(soup)
print(f"Columns found: {len(cols)}")
for i, col in enumerate(cols):
    blocks = process_column_content(col)
    print(f"  Col {i}: {len(blocks)} blocks")
    for j, b in enumerate(blocks[:3]):
        print(f"    [{j}] type={b['type']}, preview={b['html'][:80]}")

# Test 2: Table slide
print("\n" + "=" * 60)
print("TEST 2: Table (diverticula/slide-13)")
print("=" * 60)
html = open(f"{BASE}/surgery_diverticula_hernias/slides/slide-13.html").read()
title = extract_title(html)
soup = BeautifulSoup(html, "lxml")
cols = find_content_columns(soup)
print(f"Title: {title}, Columns: {len(cols)}")
for i, col in enumerate(cols):
    blocks = process_column_content(col)
    print(f"  Col {i}: {len(blocks)} blocks")
    for j, b in enumerate(blocks):
        print(f"    [{j}] type={b['type']}, preview={b['html'][:80]}")

# Test 3: Cover slide
print("\n" + "=" * 60)
print("TEST 3: Cover (stomach/slide-01)")
print("=" * 60)
html = open(f"{BASE}/surgery_stomach/slides/slide-01.html").read()
title = extract_title(html)
print(f"Title: {title}, Is cover: {is_cover(html)}")
parts = extract_cover_parts(html)
print(f"Parts: {parts}")

# Test 4: Generate and save a sample
print("\n" + "=" * 60)
print("TEST 4: Generate sample output")
print("=" * 60)
html = open(f"{BASE}/surgery_stomach/slides/slide-05.html").read()
new_html = transform_slide(html, "slide-05.html")
# Save to temp for inspection
with open("/tmp/test_slide_05.html", "w") as f:
    f.write(new_html)
print(f"Generated: {len(new_html)} bytes")
print(f"Saved to /tmp/test_slide_05.html")

# Check content preservation
orig_soup = BeautifulSoup(html, "lxml")
new_soup = BeautifulSoup(new_html, "lxml")
orig_text = orig_soup.get_text(strip=True)
new_text = new_soup.get_text(strip=True)
print(f"Original text length: {len(orig_text)}")
print(f"New text length: {len(new_text)}")
# Check key phrases
key_phrases = ["Atrophic", "Definition", "Pathophysiology", "H. pylori"]
for phrase in key_phrases:
    in_orig = phrase in orig_text
    in_new = phrase in new_text
    status = "OK" if in_orig == in_new else "MISSING!"
    print(f"  '{phrase}': orig={in_orig}, new={in_new} [{status}]")

print("\nALL TESTS DONE")
