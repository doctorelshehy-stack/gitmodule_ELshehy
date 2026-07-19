#!/usr/bin/env python3
"""Verify content preservation across all presentations"""
import os
import re
from bs4 import BeautifulSoup

BASE = "/media/mohamed/projects4/git/raw material/GIT Presentation"

PRESENTATIONS = [
    "surgery_stomach",
    "surgery_esophagus",
    "surgery_liver",
    "surgery_pancreas_appendix",
    "surgery_oral_anal",
    "surgery_intestine_peritoneum",
    "surgery_diverticula_hernias",
]

total_issues = 0
total_slides = 0

for pres in PRESENTATIONS:
    slides_dir = f"{BASE}/{pres}/slides"
    slide_files = sorted([f for f in os.listdir(slides_dir) if f.endswith(".html")])
    
    print(f"\n{'='*60}")
    print(f"{pres} ({len(slide_files)} slides)")
    print(f"{'='*60}")
    
    for fname in slide_files:
        total_slides += 1
        fpath = f"{slides_dir}/{fname}"
        html = open(fpath).read()
        
        soup = BeautifulSoup(html, "lxml")
        text = soup.get_text(strip=True)
        
        issues = []
        
        # Check basic structure
        if '<div class="S">' not in html and '<div class="S CV">' not in html:
            issues.append("Missing slide container class")
        
        if 'Inter' not in html and 'inter' not in html.lower():
            issues.append("Missing Inter font")
        
        # Check slide number (not on covers)
        if 'CV' not in html:  # not a cover
            if '<div class="SN">' not in html:
                issues.append("Missing slide number")
        
        # Check title is present
        title_match = re.search(r'<title>([^<]+)</title>', html)
        if not title_match:
            issues.append("Missing <title>")
        
        # Check for original Times New Roman (should NOT be present)
        if "Times New Roman" in html:
            issues.append("Still has Times New Roman font")
        
        # Check for original background gradient
        if "linear-gradient(135deg,#1b2838" in html:
            issues.append("Still has original background")
        
        if issues:
            total_issues += len(issues)
            print(f"  {fname}: {', '.join(issues)}")
        else:
            print(f"  {fname}: OK")

print(f"\n{'='*60}")
print(f"SUMMARY: {total_slides} slides, {total_issues} issues")
print(f"{'='*60}")
