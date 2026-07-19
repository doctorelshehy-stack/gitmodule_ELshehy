#!/usr/bin/env python3
"""Debug process_column_content for slide-19"""
import re
from bs4 import BeautifulSoup, Tag, NavigableString

BASE = "/media/mohamed/projects4/git/raw material/GIT Presentation"

html = open(f"{BASE}/surgery_stomach/slides/slide-19.html").read()
soup = BeautifulSoup(html, "lxml")
slide_div = soup.find("div", style=re.compile(r"width:960px.*height:540px"))

# Find content divs
for child in slide_div.children:
    if not isinstance(child, Tag):
        continue
    style = child.get("style", "")
    if "position:absolute" not in (style or ""):
        continue
    top = re.search(r"top:(\d+)px", style)
    if not top:
        continue
    top_val = int(top.group(1))
    if top_val < 100 or top_val > 145:
        continue
    
    print(f"\nContent div: top={top_val}")
    print(f"  Tag: {child.name}")
    print(f"  Children count: {len(list(child.children))}")
    
    for i, ch in enumerate(child.children):
        print(f"  Child [{i}]: type={type(ch).__name__}, is_Tag={isinstance(ch, Tag)}")
        if isinstance(ch, Tag):
            print(f"    name={ch.name}, has_text={bool(ch.get_text(strip=True))}")
            if ch.name == "img":
                print(f"    IMG FOUND: src={ch.get('src','')}")
            elif ch.name == "table":
                print(f"    TABLE FOUND")
            else:
                style2 = ch.get("style", "")
                print(f"    style={style2[:80]}")
        elif isinstance(ch, NavigableString):
            text = str(ch).strip()
            if text:
                print(f"    text='{text[:40]}'")
