#!/usr/bin/env python3
"""Test BeautifulSoup parsing of positioned content divs"""
import re
from bs4 import BeautifulSoup

BASE = "/media/mohamed/projects4/git/raw material/GIT Presentation"

html = open(f"{BASE}/surgery_stomach/slides/slide-05.html").read()

soup = BeautifulSoup(html, "lxml")

# Find the slide-content div
slide_div = soup.find("div", class_="slide-content")
if not slide_div:
    # Try finding by style
    slide_div = soup.find("div", style=re.compile(r"width:960px.*height:540px"))

print(f"Slide div found: {slide_div is not None}")

# Find all direct children that are positioned
for child in slide_div.children:
    if hasattr(child, 'get'):
        style = child.get("style", "")
        tag = child.name
        if "position:absolute" in (style or ""):
            # Extract key style properties
            top = re.search(r"top:(\d+)px", style)
            left = re.search(r"left:(\d+)px", style)
            right = re.search(r"right:(\d+)px", style)
            width = re.search(r"width:(\d+)px", style)
            
            top_val = top.group(1) if top else "?"
            pos = f"left:{left.group(1)}" if left else f"right:{right.group(1)}" if right else "?"
            w = width.group(1) if width else "?"
            
            text_preview = child.get_text(strip=True)[:80]
            print(f"\n<{tag}> top={top_val} {pos} width={w}")
            print(f"  Text: {text_preview}")
            
            # For content divs, show inner structure
            if top_val == "120" and tag == "div":
                inner_divs = child.find_all("div", recursive=False)
                print(f"  Inner divs: {len(inner_divs)}")
                for j, inner in enumerate(inner_divs[:3]):
                    inner_style = inner.get("style", "")
                    inner_text = inner.get_text(strip=True)[:60]
                    print(f"    [{j}] style={inner_style[:80]}")
                    print(f"        text={inner_text}")
