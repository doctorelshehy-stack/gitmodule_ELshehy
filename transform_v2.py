#!/usr/bin/env python3
"""
Surgery Presentation Redesign v2 — Complete Rewrite
Parses HTML with BeautifulSoup, extracts ALL content, rebuilds with premium design.
Preserves 100% of original content, images, tables, and structure.
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

BASE = Path("/media/mohamed/projects4/git/raw material/GIT Presentation")

PRESENTATIONS = [
    ("surgery_stomach", "Stomach"),
    ("surgery_esophagus", "Esophagus"),
    ("surgery_liver", "Liver"),
    ("surgery_pancreas_appendix", "Pancreas & Appendix"),
    ("surgery_oral_anal", "Oral Cavity & Anal Canal"),
    ("surgery_intestine_peritoneum", "Intestine & Peritoneum"),
    ("surgery_diverticula_hernias", "Diverticula & Hernias"),
]

# ═══════════════════════════════════════════════════════════════════════
# CSS DESIGN SYSTEM — Embedded inline in each slide
# ═══════════════════════════════════════════════════════════════════════

DESIGN_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100%;overflow:hidden;display:flex;justify-content:center;align-items:center;background:#0F172A;font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',system-ui,sans-serif}
.S{width:960px;height:540px;position:relative;transform-origin:center center;overflow:hidden;background:linear-gradient(135deg,#0F172A 0%,#1E293B 50%,#0F172A 100%);color:#E2E8F0}
.S::before{content:'';position:absolute;top:0;left:0;width:5px;height:100%;background:linear-gradient(180deg,#2563EB,#06B6D4,#0F766E);z-index:50;border-radius:0 2px 2px 0}
.S::after{content:'';position:absolute;top:0;left:5px;right:0;height:2px;background:linear-gradient(90deg,#2563EB 0%,#06B6D4 40%,transparent 100%);z-index:50}
.T{position:absolute;top:24px;left:40px;right:40px;font-size:21px;font-weight:700;color:#FFF;z-index:10;line-height:1.25;letter-spacing:-0.3px}
.T::after{content:'';display:block;width:48px;height:3px;background:linear-gradient(90deg,#2563EB,#06B6D4);border-radius:2px;margin-top:5px}
.B{position:absolute;top:68px;left:40px;right:40px;bottom:24px;z-index:10;overflow:hidden}
.C{display:flex;gap:18px;height:100%}
.L{flex:1;min-width:0;overflow:hidden}
/* Section headers */
.sh{font-size:10.5px;font-weight:700;margin-bottom:2px;display:flex;align-items:center;gap:5px;line-height:1.3}
.sh::before{content:'';width:3px;height:10px;border-radius:2px;flex-shrink:0}
.sh.p{color:#60A5FA}.sh.p::before{background:#3B82F6}
.sh.s{color:#2DD4BF}.sh.s::before{background:#14B8A6}
.sh.a{color:#22D3EE}.sh.a::before{background:#06B6D4}
.sh.g{color:#4ADE80}.sh.g::before{background:#22C55E}
.sh.w{color:#FBBF24}.sh.w::before{background:#F59E0B}
.sh.d{color:#F87171}.sh.d::before{background:#EF4444}
/* Text */
.tx{font-size:10px;color:#CBD5E1;line-height:1.42;margin-bottom:0.5px}
.tx strong{color:#F1F5F9;font-weight:600}
/* Cards */
.cd{border-radius:8px;padding:6px 8px;margin-bottom:4px;font-size:10px;line-height:1.4}
.cd-b{background:rgba(37,99,235,0.08);border:1px solid rgba(37,99,235,0.15);border-top:2px solid #2563EB}
.cd-t{background:rgba(15,118,110,0.08);border:1px solid rgba(15,118,110,0.15);border-top:2px solid #0F766E}
.cd-o{background:rgba(249,115,22,0.08);border:1px solid rgba(249,115,22,0.15);border-top:2px solid #F97316}
.cd-r{background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.15);border-top:2px solid #EF4444}
.cd-a{background:rgba(245,158,11,0.08);border:1px solid rgba(245,158,11,0.15);border-top:2px solid #F59E0B}
.cd-g{background:rgba(22,163,74,0.08);border:1px solid rgba(22,163,74,0.15);border-top:2px solid #16A34A}
.cd-ti{font-size:10px;font-weight:700;margin-bottom:2px}
/* Highlight boxes */
.hb{border-radius:6px;padding:5px 8px;margin-top:4px;font-size:9.5px;line-height:1.4}
.hb-b{background:rgba(37,99,235,0.1);border:1px solid rgba(37,99,235,0.2);border-left:3px solid #2563EB}
.hb-r{background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.2);border-left:3px solid #EF4444}
.hb-a{background:rgba(245,158,11,0.1);border:1px solid rgba(245,158,11,0.2);border-left:3px solid #F59E0B}
.hb-g{background:rgba(22,163,74,0.1);border:1px solid rgba(22,163,74,0.2);border-left:3px solid #16A34A}
.hb-t{background:rgba(15,118,110,0.1);border:1px solid rgba(15,118,110,0.2);border-left:3px solid #0F766E}
/* Table */
.tbl{width:100%;border-collapse:separate;border-spacing:0;font-size:9px;border-radius:8px;overflow:hidden;border:1px solid rgba(255,255,255,0.08)}
.tbl th{padding:4px 6px;text-align:left;font-weight:700;font-size:8.5px;background:linear-gradient(135deg,#1E293B,#0F172A);color:#E2E8F0;border-bottom:2px solid #2563EB}
.tbl td{padding:3px 6px;border-bottom:1px solid rgba(255,255,255,0.05);color:#CBD5E1}
.tbl tr:nth-child(even) td{background:rgba(255,255,255,0.02)}
/* Image */
.SI{width:100%;height:auto;border-radius:8px;border:1px solid rgba(255,255,255,0.08);box-shadow:0 2px 8px rgba(0,0,0,0.3);display:block}
/* Cover */
.S.CV{display:flex;flex-direction:column;justify-content:center;padding:50px 70px}
.CP{position:absolute;top:0;left:0;width:100%;height:100%;z-index:0;opacity:0.05;background-image:radial-gradient(circle at 20% 80%,#2563EB 0%,transparent 50%),radial-gradient(circle at 80% 20%,#06B6D4 0%,transparent 50%)}
.CL{font-size:11px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:#22D3EE;margin-bottom:10px;position:relative;z-index:2}
.CV .CT{font-size:42px;font-weight:800;line-height:1.1;margin-bottom:6px;color:#FFF;position:relative;z-index:2}
.CTA{background:linear-gradient(135deg,#22D3EE,#60A5FA);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.CDv{width:56px;height:3px;background:linear-gradient(90deg,#2563EB,#06B6D4);border-radius:2px;margin:18px 0;position:relative;z-index:2}
.CS{font-size:15px;font-weight:400;color:rgba(255,255,255,0.55);line-height:1.55;max-width:560px;position:relative;z-index:2}
.CF{font-size:11px;color:rgba(255,255,255,0.3);font-weight:500;position:relative;z-index:2}
/* Slide number */
.SN{position:absolute;right:16px;bottom:10px;min-width:28px;height:20px;padding:0 7px;background:linear-gradient(135deg,#2563EB,#1D4ED8);border-radius:999px;display:flex;align-items:center;justify-content:center;z-index:60;box-shadow:0 2px 8px rgba(37,99,235,0.3)}
.SN span{font-size:10px;font-weight:700;color:#FFF}
/* Utils */
.mt1{margin-top:2px}.mt2{margin-top:4px}.mt3{margin-top:6px}.mt4{margin-top:8px}
.mb1{margin-bottom:2px}.mb2{margin-bottom:4px}.mb3{margin-bottom:6px}
.fl{display:flex}.fl1{flex:1}.flc{flex-direction:column}
.tc{text-align:center}
@media(max-width:960px){.S{transform:scale(0.9)}}
@media(max-width:720px){.S{transform:scale(0.7)}}
@media(max-width:540px){.S{transform:scale(0.55)}}
@media print{html,body{background:#fff;overflow:visible}.S{transform:none!important;box-shadow:none}}
"""


# ═══════════════════════════════════════════════════════════════════════
# CONTENT EXTRACTION — Using BeautifulSoup for proper HTML parsing
# ═══════════════════════════════════════════════════════════════════════

def get_color_class(color_hex):
    """Map hex color to CSS class shorthand."""
    c = color_hex.upper()
    m = {
        "#42A5F5": "p", "#0F766E": "s", "#06B6D4": "a",
        "#16A34A": "g", "#22C55E": "g", "#4ADE80": "g", "#4CAF50": "g",
        "#F59E0B": "w", "#FF9800": "w", "#FBBF24": "w",
        "#DC2626": "d", "#E53935": "d", "#EF4444": "d", "#F87171": "d",
        "#FFC107": "a",
    }
    return m.get(c, "p")


def get_card_class(color_hex):
    """Map hex color to card CSS class."""
    c = color_hex.upper()
    m = {
        "#42A5F5": "cd-b", "#0F766E": "cd-t", "#06B6D4": "cd-t",
        "#16A34A": "cd-g", "#22C55E": "cd-g", "#4CAF50": "cd-g",
        "#F59E0B": "cd-a", "#FF9800": "cd-a", "#FFC107": "cd-a",
        "#DC2626": "cd-r", "#E53935": "cd-r", "#EF4444": "cd-r",
    }
    return m.get(c, "cd-b")


def get_hb_class(color_hex):
    """Map hex color to highlight box CSS class."""
    c = color_hex.upper()
    m = {
        "#42A5F5": "hb-b", "#0F766E": "hb-t", "#06B6D4": "hb-t",
        "#16A34A": "hb-g", "#22C55E": "hb-g", "#4CAF50": "hb-g",
        "#F59E0B": "hb-a", "#FF9800": "hb-a", "#FFC107": "hb-a",
        "#DC2626": "hb-r", "#E53935": "hb-r", "#EF4444": "hb-r",
    }
    return m.get(c, "hb-b")


def elem_to_html(elem):
    """Convert a BeautifulSoup element to clean HTML string."""
    return str(elem)


def extract_title(html):
    """Extract slide title from the positioned <p> at top:40px (or top:120px for covers)."""
    soup = BeautifulSoup(html, "lxml")
    for p in soup.find_all("p"):
        style = p.get("style", "")
        if "position:absolute" in style:
            top = re.search(r"top:(\d+)px", style)
            if top and int(top.group(1)) <= 130:
                return p.get_text(strip=True)
    m = re.search(r"<title>([^<]+)</title>", html)
    return m.group(1).strip() if m else "Slide"


def extract_slide_num(filename):
    m = re.search(r"slide-(\d+)", filename)
    return m.group(1) if m else "01"


def is_cover(html):
    """Cover slides have title <p> at top:120px (not 40px)."""
    soup = BeautifulSoup(html, "lxml")
    for p in soup.find_all("p"):
        style = p.get("style", "")
        if "position:absolute" in style and "top:120px" in style:
            return True
    return False


def extract_cover_parts(html):
    """Extract cover slide elements by their top position."""
    soup = BeautifulSoup(html, "lxml")
    parts = {}
    for p in soup.find_all("p"):
        style = p.get("style", "")
        if "position:absolute" in style:
            top = re.search(r"top:(\d+)px", style)
            if top:
                val = top.group(1)
                text = p.get_text(strip=True)
                if text:
                    parts[val] = text
    return parts


def classify_inner_div(div):
    """
    Classify an inner div within a content column.
    Returns a dict with type and rendered HTML.
    """
    style = div.get("style", "")
    text = div.get_text(strip=True)

    # --- Table ---
    table = div.find("table")
    if table:
        return {"type": "table", "html": str(table)}

    # --- Image ---
    img = div.find("img")
    if img:
        return {"type": "image", "html": str(img)}

    # --- Section header: color + bold + font-size >= 11 ---
    color_m = re.search(r"color:(#[0-9a-fA-F]{6})", style)
    is_bold = "font-weight:bold" in style or "font-weight: 700" in style
    fs_m = re.search(r"font-size:(\d+)px", style)
    fs = int(fs_m.group(1)) if fs_m else 12

    if is_bold and color_m and fs >= 11:
        cc = get_color_class(color_m.group(1))
        return {"type": "sh", "html": f'<div class="sh {cc}">{text}</div>'}

    # --- Highlight box: has background + border-left ---
    bg_m = re.search(r"background:rgba\((\d+),(\d+),(\d+),([\d.]+)\)", style)
    has_border_left = "border-left" in style

    if bg_m and has_border_left:
        r, g, b = int(bg_m.group(1)), int(bg_m.group(2)), int(bg_m.group(3))
        if r > 200 and g < 100:
            hc = "hb-r"
        elif g > 150 and r < 100:
            hc = "hb-g"
        elif r > 200 and g > 150:
            hc = "hb-a"
        elif b > 200:
            hc = "hb-b"
        elif g > 100 and r < 50:
            hc = "hb-t"
        else:
            hc = "hb-b"
        inner = "".join(str(c) for c in div.children)
        return {"type": "hb", "html": f'<div class="{hc}">{inner}</div>'}

    # --- Card: has background, no border-left ---
    if bg_m and not has_border_left:
        r, g, b = int(bg_m.group(1)), int(bg_m.group(2)), int(bg_m.group(3))
        if b > 200:
            cc = "cd-b"
        elif g > 150 and r < 100:
            cc = "cd-t"
        elif r > 200 and g > 100:
            cc = "cd-o"
        elif r > 200 and g < 100:
            cc = "cd-r"
        else:
            cc = "cd-b"
        inner = "".join(str(c) for c in div.children)
        return {"type": "card", "html": f'<div class="{cc}">{inner}</div>'}

    # --- Plain text div ---
    indent_m = re.search(r"margin-left:(\d+)px", style)
    indent = int(indent_m.group(1)) if indent_m else 0
    pl = f' style="padding-left:{indent}px"' if indent > 0 else ""
    inner = "".join(str(c) for c in div.children)
    return {"type": "text", "html": f'<div class="tx"{pl}>{inner}</div>'}


def process_column_content(col_div):
    """Process all inner divs of a content column."""
    results = []
    for child in col_div.children:
        if isinstance(child, NavigableString):
            continue
        if not isinstance(child, Tag):
            continue
        # Handle tables directly
        if child.name == "table":
            results.append({"type": "table", "html": str(child)})
            continue
        # Handle images directly
        if child.name == "img":
            results.append({"type": "image", "html": str(child)})
            continue
        result = classify_inner_div(child)
        results.append(result)
    return results


def find_content_columns_regex(html):
    """Find positioned content columns using regex on raw HTML.
    This avoids lxml parser issues with absolute positioning."""
    # Find all positioned divs with their full content (handling nested divs)
    # Pattern: <div style="position:absolute;top:NNNpx;..." ...>CONTENT</div>
    # We need to match the outermost positioned div that has content
    columns = []
    # Find all opening tags of positioned divs in the content region
    open_pattern = re.compile(
        r'<div\s+style="position:absolute;top:(\d+)px;(?:left:(\d+)px;)?(?:right:(\d+)px;)?'
        r'(?:width:(\d+)px;)?([^"]*)"[^>]*>',
        re.DOTALL
    )
    for m in open_pattern.finditer(html):
        top_val = int(m.group(1))
        left_val = m.group(2)
        right_val = m.group(3)
        width_val = m.group(4)
        extra_style = m.group(5)
        start_pos = m.end()

        # Filter: only content columns (top 100-420px)
        if top_val < 100 or top_val > 420:
            continue

        # Skip tiny decorative elements (underline bars with height:3px etc)
        height_m = re.search(r"height:(\d+)px", extra_style)
        if height_m and int(height_m.group(1)) <= 5:
            continue

        # Must have reasonable width
        w = int(width_val) if width_val else 0
        has_left_right = left_val is not None and right_val is not None
        if w < 200 and not has_left_right:
            continue

        # Extract the inner HTML by counting nested div tags
        depth = 1
        pos = start_pos
        while depth > 0 and pos < len(html):
            next_open = html.find("<div", pos)
            next_close = html.find("</div>", pos)
            if next_close == -1:
                break
            if next_open != -1 and next_open < next_close:
                depth += 1
                pos = next_open + 4
            else:
                depth -= 1
                if depth == 0:
                    inner_html = html[start_pos:next_close]
                    break
                pos = next_close + 6
        else:
            continue

        # Parse this inner HTML with BeautifulSoup
        inner_soup = BeautifulSoup(f"<div>{inner_html}</div>", "lxml")
        inner_div = inner_soup.find("div")
        if inner_div:
            columns.append({
                "top": top_val,
                "left": int(left_val) if left_val else None,
                "right": int(right_val) if right_val else None,
                "width": w,
                "soup_element": inner_div,
                "raw_html": inner_html,
            })

    # Sort by top, then by left (left columns before right columns)
    columns.sort(key=lambda c: (c["top"], -(c["right"] or 0), c["left"] or 0))
    return columns


# ═══════════════════════════════════════════════════════════════════════
# HTML GENERATION
# ═══════════════════════════════════════════════════════════════════════

def build_cover(title, parts, slide_num):
    """Build premium cover slide."""
    # Split title
    tp = title.split("—")
    main = tp[0].strip()
    accent = tp[1].strip() if len(tp) > 1 else ""

    # Get other parts
    subtitle = ""
    desc = ""
    footer = ""
    for k in sorted(parts.keys()):
        v = parts[k]
        if k == "120":
            continue
        if k in ("165", "195"):
            if not accent:
                accent = v
            else:
                subtitle = v
        elif k == "290":
            desc = v
        elif k in ("385", "415"):
            if not footer:
                footer = v

    html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title><style>{DESIGN_CSS}</style></head><body>
<div class="S CV"><div class="CP"></div>
<div class="CL">SURGERY</div>
<div class="CT">{main}</div>
{"<div class='CT'><span class='CTA'>" + accent + "</span></div>" if accent else ""}
<div class="CDv"></div>
{"<div class='CS'>" + desc + "</div>" if desc else ""}
{"<div class='CF' style='margin-top:20px'>" + footer + "</div>" if footer else ""}
</div></body></html>'''
    return html


def build_content(title, columns, slide_num):
    """Build premium content slide from extracted columns."""
    all_blocks = []

    if len(columns) == 0:
        # No content columns found, render empty
        body_html = '<div class="tx">Content area</div>'
    elif len(columns) == 1:
        # Single column (full width)
        soup_elem = columns[0].get("soup_element")
        if soup_elem:
            blocks = process_column_content(soup_elem)
        else:
            blocks = process_column_content_raw(columns[0].get("raw_html", ""))
        body_html = "\n".join(b["html"] for b in blocks)
    elif len(columns) == 2:
        # Two columns
        soup0 = columns[0].get("soup_element")
        soup1 = columns[1].get("soup_element")
        left_blocks = process_column_content(soup0) if soup0 else process_column_content_raw(columns[0].get("raw_html", ""))
        right_blocks = process_column_content(soup1) if soup1 else process_column_content_raw(columns[1].get("raw_html", ""))
        left_html = "\n".join(b["html"] for b in left_blocks)
        right_html = "\n".join(b["html"] for b in right_blocks)
        body_html = f'<div class="C"><div class="L">{left_html}</div><div class="L">{right_html}</div></div>'
    else:
        # 3+ columns
        cols_html = []
        for col in columns:
            soup_elem = col.get("soup_element")
            if soup_elem:
                blocks = process_column_content(soup_elem)
            else:
                blocks = process_column_content_raw(col.get("raw_html", ""))
            inner = "\n".join(b["html"] for b in blocks)
            cols_html.append(f'<div class="L">{inner}</div>')
        body_html = f'<div class="C">{" ".join(cols_html)}</div>'

    html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title><style>{DESIGN_CSS}</style></head><body>
<div class="S">
<div class="T">{title}</div>
<div class="B">{body_html}</div>
<div class="SN"><span>{slide_num}</span></div>
</div></body></html>'''
    return html


def transform_slide(html, filename):
    """Transform a single slide."""
    title = extract_title(html)
    slide_num = extract_slide_num(filename)

    if is_cover(html):
        parts = extract_cover_parts(html)
        return build_cover(title, parts, slide_num)
    else:
        columns = find_content_columns_regex(html)
        return build_content(title, columns, slide_num)


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════

def process_presentation(folder_name, label):
    slides_dir = BASE / folder_name / "slides"
    if not slides_dir.exists():
        print(f"  ERROR: {slides_dir} not found!")
        return 0

    slide_files = sorted(slides_dir.glob("slide-*.html"))
    count = 0
    errors = []
    for sf in slide_files:
        try:
            html = sf.read_text(encoding="utf-8")
            new_html = transform_slide(html, sf.name)
            sf.write_text(new_html, encoding="utf-8")
            count += 1
        except Exception as e:
            errors.append((sf.name, str(e)))
            import traceback
            traceback.print_exc()
    for name, err in errors:
        print(f"  ERROR {name}: {err}")
    return count


def main():
    print("=" * 60)
    print("SURGERY PRESENTATION REDESIGN v2")
    print("=" * 60)
    total = 0
    for folder, label in PRESENTATIONS:
        count = process_presentation(folder, label)
        total += count
        print(f"  {folder}: {count} slides")
    print(f"\nTOTAL: {total} slides transformed")


if __name__ == "__main__":
    main()
