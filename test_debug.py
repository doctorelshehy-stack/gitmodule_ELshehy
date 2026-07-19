#!/usr/bin/env python3
"""Test debug for content extraction"""
import re
from bs4 import BeautifulSoup

BASE = "/media/mohamed/projects4/git/raw material/GIT Presentation"

html = open(f"{BASE}/surgery_stomach/slides/slide-05.html").read()

# Find all positioned divs
all_divs = re.findall(r'<div style="position:absolute;([^"]*)">(.*?)</div>', html, re.DOTALL)
print(f"Found {len(all_divs)} positioned divs")
for i, (style, content) in enumerate(all_divs):
    print(f"\n--- Div {i} ---")
    print(f"  Style: {style[:100]}")
    # Check for content
    content_preview = re.sub(r'<[^>]+>', '', content)[:100]
    print(f"  Content: {content_preview}")

# Better approach: use regex to extract each positioned div's content
print("\n\n=== APPROACH 2: Find content divs ===")
# Find the content div at top:120px
pattern = r'<div style="position:absolute;top:120px;left:60px;width:(\d+)px[^"]*">(.*?)</div>\s*(?:<div style="position:absolute|</div>\s*</body>)'
matches = re.findall(pattern, html, re.DOTALL)
print(f"Matches: {len(matches)}")
for w, content in matches:
    print(f"  width={w}, content={content[:120]}")
