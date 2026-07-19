#!/usr/bin/env python3
"""Debug slides with 0 columns"""
import re
from bs4 import BeautifulSoup

BASE = "/media/mohamed/projects4/git/raw material/GIT Presentation"

problem_slides = [
    "surgery_stomach/slides/slide-20.html",
    "surgery_stomach/slides/slide-23.html",
    "surgery_stomach/slides/slide-16.html",
    "surgery_liver/slides/slide-08.html",
    "surgery_intestine_peritoneum/slides/slide-05.html",
    "surgery_esophagus/slides/slide-01.html",
]

for fpath in problem_slides:
    html = open(f"{BASE}/{fpath}").read()
    soup = BeautifulSoup(html, "lxml")
    
    print(f"\n{'='*60}")
    print(f"FILE: {fpath}")
    print(f"{'='*60}")
    
    # Find all positioned elements
    slide_div = soup.find("div", style=re.compile(r"width:960px.*height:540px"))
    if not slide_div:
        print("  NO SLIDE DIV FOUND")
        continue
    
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
        left_val = left.group(1) if left else ""
        right_val = right.group(1) if right else ""
        width_val = width.group(1) if width else ""
        
        text = child.get_text(strip=True)[:60]
        tag = child.name
        
        pos_str = f"left:{left_val}" if left_val else f"right:{right_val}" if right_val else ""
        print(f"  <{tag}> top={top_val} {pos_str} w={width_val} text={text}")
