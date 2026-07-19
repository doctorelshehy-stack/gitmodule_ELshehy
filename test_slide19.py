#!/usr/bin/env python3
import sys
sys.path.insert(0, "/media/mohamed/projects4/git/raw material/GIT Presentation")
from transform_v2 import *

html = open("/media/mohamed/projects4/git/raw material/GIT Presentation/surgery_stomach/slides/slide-19.html").read()
soup = BeautifulSoup(html, "lxml")
cols = find_content_columns(soup)
print(f"Columns: {len(cols)}")
for i, col in enumerate(cols):
    blocks = process_column_content(col)
    s = col.get("style", "")
    top = re.search(r"top:(\d+)px", s)
    print(f"  Col {i}: {len(blocks)} blocks, top={top.group(1) if top else '?'}")
    for b in blocks:
        print(f"    type={b['type']}, html_len={len(b['html'])}")

new = transform_slide(html, "slide-19.html")
print(f"Generated {len(new)} bytes")
with open("/tmp/slide19_new.html", "w") as f:
    f.write(new)
print("Saved to /tmp/slide19_new.html")
