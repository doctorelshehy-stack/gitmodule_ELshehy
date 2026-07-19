#!/usr/bin/env python3
"""Deep content preservation test: compare git originals vs transformed"""
import subprocess
import re
from bs4 import BeautifulSoup
from html import unescape

BASE = "/media/mohamed/projects4/git/raw material/GIT Presentation"

def get_original_text(filepath):
    """Get text content from git-tracked original."""
    rel = filepath.replace(BASE + "/", "")
    result = subprocess.run(
        ["git", "show", f"HEAD:{rel}"],
        capture_output=True, text=True, cwd=BASE
    )
    if result.returncode != 0:
        return None
    soup = BeautifulSoup(result.stdout, "lxml")
    return soup.get_text(" ", strip=True)

def get_new_text(filepath):
    """Get text content from current (transformed) version."""
    with open(filepath) as f:
        html = f.read()
    soup = BeautifulSoup(html, "lxml")
    return soup.get_text(" ", strip=True)

def normalize(text):
    """Normalize whitespace and unicode for comparison."""
    text = unescape(text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# Test a broad sample
test_slides = [
    ("surgery_stomach/slides/slide-01.html", "Cover"),
    ("surgery_stomach/slides/slide-05.html", "Two-col content"),
    ("surgery_stomach/slides/slide-11.html", "Complex two-col"),
    ("surgery_stomach/slides/slide-19.html", "Image slide"),
    ("surgery_stomach/slides/slide-27.html", "Summary"),
    ("surgery_esophagus/slides/slide-01.html", "Cover"),
    ("surgery_esophagus/slides/slide-12.html", "Infectious esophagitis"),
    ("surgery_liver/slides/slide-08.html", "HCC pathology"),
    ("surgery_liver/slides/slide-17.html", "Last slide"),
    ("surgery_oral_anal/slides/slide-03.html", "Sialadenitis"),
    ("surgery_intestine_peritoneum/slides/slide-05.html", "Obstruction"),
    ("surgery_diverticula_hernias/slides/slide-13.html", "Table slide"),
    ("surgery_pancreas_appendix/slides/slide-10.html", "Complex content"),
]

total_ok = 0
total_warn = 0
total_fail = 0

for rel_path, desc in test_slides:
    filepath = f"{BASE}/{rel_path}"
    orig_text = get_original_text(filepath)
    new_text = get_new_text(filepath)
    
    if orig_text is None:
        print(f"  SKIP {rel_path}: cannot read original")
        continue
    
    norm_orig = normalize(orig_text)
    norm_new = normalize(new_text)
    
    # Check key words preserved
    orig_words = set(norm_orig.split())
    new_words = set(norm_new.split())
    missing = orig_words - new_words
    # Filter out trivial differences (single chars, numbers)
    missing_significant = {w for w in missing if len(w) > 3 and not w.isdigit()}
    
    # Check word count ratio
    orig_count = len(norm_orig.split())
    new_count = len(norm_new.split())
    ratio = new_count / orig_count if orig_count > 0 else 0
    
    if len(missing_significant) == 0 and 0.8 <= ratio <= 1.3:
        status = "OK"
        total_ok += 1
    elif len(missing_significant) <= 3 and 0.7 <= ratio <= 1.4:
        status = f"WARN ({len(missing_significant)} missing words)"
        total_warn += 1
        for w in list(missing_significant)[:5]:
            print(f"    Missing: '{w}'")
    else:
        status = f"FAIL ({len(missing_significant)} missing words, ratio={ratio:.2f})"
        total_fail += 1
        for w in list(missing_significant)[:10]:
            print(f"    Missing: '{w}'")
    
    print(f"  {rel_path}: {desc} — {status} (orig:{orig_count}w, new:{new_count}w, ratio:{ratio:.2f})")

print(f"\n{'='*60}")
print(f"RESULTS: {total_ok} OK, {total_warn} WARN, {total_fail} FAIL")
print(f"{'='*60}")
