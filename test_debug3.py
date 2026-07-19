#!/usr/bin/env python3
"""Debug remaining issues"""
import re
from bs4 import BeautifulSoup

BASE = "/media/mohamed/projects4/git/raw material/GIT Presentation"

# Debug slide-19 (0 blocks)
print("SLIDE-19 (Gastrectomy):")
html = open(f"{BASE}/surgery_stomach/slides/slide-19.html").read()
soup = BeautifulSoup(html, "lxml")
slide_div = soup.find("div", style=re.compile(r"width:960px.*height:540px"))
for child in slide_div.children:
    if not hasattr(child, 'get'):
        continue
    style = child.get("style", "")
    if "position:absolute" not in (style or ""):
        continue
    top = re.search(r"top:(\d+)px", style)
    left = re.search(r"left:(\d+)px", style)
    right = re.search(r"right:(\d+)px", style)
    width = re.search(r"width:(\d+)px", style)
    top_val = top.group(1) if top else "?"
    pos = f"L:{left.group(1)}" if left else f"R:{right.group(1)}" if right else "?"
    w = width.group(1) if width else "?"
    text = child.get_text(strip=True)[:80]
    print(f"  <{child.name}> top={top_val} {pos} w={w} text={text}")

# Check if it has a flex container
print("\n  Inner structure:")
cols = []
for child in slide_div.children:
    if not hasattr(child, 'get'):
        continue
    style = child.get("style", "")
    if "position:absolute" not in (style or ""):
        continue
    top = re.search(r"top:(\d+)px", style)
    if top and 100 <= int(top.group(1)) <= 145:
        cols.append(child)
        print(f"  Content div: top={top.group(1)}")
        # Check for display:flex
        if "display:flex" in style or "display: flex" in style:
            print("    HAS FLEX CONTAINER")
            # Check inner divs
            for inner in child.children:
                if hasattr(inner, 'get'):
                    inner_style = inner.get("style", "")
                    inner_text = inner.get_text(strip=True)[:60]
                    print(f"    Inner: style={inner_style[:60]} text={inner_text}")

# Also check liver/slide-08
print("\n\nLIVER SLIDE-08:")
html = open(f"{BASE}/surgery_liver/slides/slide-08.html").read()
soup = BeautifulSoup(html, "lxml")
slide_div = soup.find("div", style=re.compile(r"width:960px.*height:540px"))
for child in slide_div.children:
    if not hasattr(child, 'get'):
        continue
    style = child.get("style", "")
    if "position:absolute" not in (style or ""):
        continue
    top = re.search(r"top:(\d+)px", style)
    left = re.search(r"left:(\d+)px", style)
    right = re.search(r"right:(\d+)px", style)
    width = re.search(r"width:(\d+)px", style)
    top_val = top.group(1) if top else "?"
    pos = f"L:{left.group(1)}" if left else f"R:{right.group(1)}" if right else "?"
    w = width.group(1) if width else "?"
    text = child.get_text(strip=True)[:80]
    has_flex = "display:flex" in (style or "")
    print(f"  <{child.name}> top={top_val} {pos} w={w} flex={has_flex} text={text}")
