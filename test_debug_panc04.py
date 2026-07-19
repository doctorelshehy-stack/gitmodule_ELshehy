#!/usr/bin/env python3
"""Debug: list ALL positioned divs in the original slide-04"""
import re, subprocess
from bs4 import BeautifulSoup, Tag

BASE = "/media/mohamed/projects4/git/raw material/GIT Presentation"
result = subprocess.run(
    ["git", "show", "HEAD:surgery_pancreas_appendix/slides/slide-04.html"],
    capture_output=True, text=True, cwd=BASE
)
soup = BeautifulSoup(result.stdout, "lxml")
slide_div = soup.find("div", style=re.compile(r"width:960px.*height:540px"))

print(f"Slide div found: {slide_div is not None}")
print(f"Direct children of slide_div:")
count = 0
for child in slide_div.children:
    if not isinstance(child, Tag):
        continue
    style = child.get("style", "")
    if "position:absolute" not in (style or ""):
        continue
    count += 1
    top = re.search(r"top:(\d+)px", style)
    left = re.search(r"left:(\d+)px", style)
    right = re.search(r"right:(\d+)px", style)
    width = re.search(r"width:(\d+)px", style)
    top_v = top.group(1) if top else "?"
    left_v = left.group(1) if left else "-"
    right_v = right.group(1) if right else "-"
    width_v = width.group(1) if width else "-"
    text = child.get_text(strip=True)[:40]
    print(f"  [{count}] <{child.name}> top={top_v} L={left_v} R={right_v} W={width_v} text={text}")

print(f"\nTotal positioned elements: {count}")
