#!/usr/bin/env python3
"""Test script for transform_v2"""
import sys
sys.path.insert(0, "/media/mohamed/projects4/git/raw material/GIT Presentation")
from transform_v2 import *

BASE_DIR = "/media/mohamed/projects4/git/raw material/GIT Presentation"

# Test 1: Content slide
print("=" * 60)
print("TEST 1: Content slide (stomach/slide-05.html)")
print("=" * 60)
html = open(f"{BASE_DIR}/surgery_stomach/slides/slide-05.html").read()
title = extract_slide_title(html)
print(f"Title: {title}")
content = extract_content_region(html)
if content:
    blocks = parse_content_blocks(content)
    print(f"Blocks found: {len(blocks)}")
    for i, b in enumerate(blocks):
        btype = b.get("type", "text")
        ct = b.get("content", "")
        if isinstance(ct, str):
            ct = ct[:80]
        print(f"  [{i}] type={btype}, content_preview={ct}")
else:
    print("ERROR: No content region found!")

# Test 2: Cover slide
print("\n" + "=" * 60)
print("TEST 2: Cover slide (stomach/slide-01.html)")
print("=" * 60)
html = open(f"{BASE_DIR}/surgery_stomach/slides/slide-01.html").read()
title = extract_slide_title(html)
print(f"Title: {title}")
print(f"Is cover: {is_cover_slide(html)}")
cover_parts = extract_cover_content(html)
print(f"Cover parts: {cover_parts}")

# Test 3: Table slide
print("\n" + "=" * 60)
print("TEST 3: Table slide (diverticula/slide-13.html)")
print("=" * 60)
html = open(f"{BASE_DIR}/surgery_diverticula_hernias/slides/slide-13.html").read()
title = extract_slide_title(html)
print(f"Title: {title}")
content = extract_content_region(html)
if content:
    blocks = parse_content_blocks(content)
    print(f"Blocks found: {len(blocks)}")
    for i, b in enumerate(blocks):
        btype = b.get("type", "text")
        ct = b.get("content", "")
        if isinstance(ct, str):
            ct = ct[:80]
        print(f"  [{i}] type={btype}, content_preview={ct}")

# Test 4: Two-column slide
print("\n" + "=" * 60)
print("TEST 4: Two-column (esophagus/slide-12.html)")
print("=" * 60)
html = open(f"{BASE_DIR}/surgery_esophagus/slides/slide-12.html").read()
title = extract_slide_title(html)
print(f"Title: {title}")
content = extract_content_region(html)
if content:
    blocks = parse_content_blocks(content)
    print(f"Blocks found: {len(blocks)}")
    for i, b in enumerate(blocks):
        btype = b.get("type", "text")
        ct = b.get("content", "")
        if isinstance(ct, str):
            ct = ct[:80]
        print(f"  [{i}] type={btype}, content_preview={ct}")

print("\n" + "=" * 60)
print("ALL TESTS COMPLETE")
print("=" * 60)
