#!/usr/bin/env python3
"""Generate comprehensive HTML slides for Hepatocellular Jaundice (File 06)."""

import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
IMGS_DIR = os.path.join(OUT_DIR, "imgs")
os.makedirs(IMGS_DIR, exist_ok=True)

# ── Palette #10 (教育与图表) ──
C_DARK = "#264653"
C_TEAL = "#2a9d8f"
C_GOLD = "#e9c46a"
C_ORANGE = "#f4a261"
C_CORAL = "#e76f51"
C_WHITE = "#ffffff"
C_BG = "#f8f9fa"
C_CARD = "#edf2f4"
C_TEXT = "#1a1a2e"
P = {"dark": C_DARK, "teal": C_TEAL, "gold": C_GOLD, "orange": C_ORANGE, "coral": C_CORAL, "white": C_WHITE, "bg": C_BG, "card": C_CARD, "text": C_TEXT}


def scale_snippet():
    return '''<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
html, body { margin:0; padding:0; width:100%; height:100%; overflow:hidden; display:flex; justify-content:center; align-items:center; background:#000; }
.slide-content { width:960px; height:540px; position:relative; transform-origin:center center; }
</style>
<script>
function scaleSlide(){const s=document.querySelector('.slide-content');if(!s)return;const sx=window.innerWidth/960;const sy=window.innerHeight/540;const sc=Math.min(sx,sy);s.style.width='960px';s.style.height='540px';s.style.transform='scale('+sc+')';s.style.transformOrigin='center center';s.style.flexShrink='0';}
window.addEventListener('load',scaleSlide);window.addEventListener('resize',scaleSlide);
</script>'''

def top_bar_svg():
    return '<svg aria-hidden="true" style="position:absolute;top:0;left:0;z-index:1;" width="960" height="540" viewBox="0 0 960 540">' \
           '<rect x="0" y="0" width="960" height="6" fill="' + C_DARK + '"/></svg>'

def page_badge(num):
    return '<svg aria-hidden="true" style="position:absolute;right:32px;bottom:24px;z-index:20;" width="40" height="28" viewBox="0 0 40 28">' \
           '<rect x="0" y="0" width="40" height="28" rx="4" fill="' + C_TEAL + '" opacity="0.85"/>' \
           '<text x="20" y="19" text-anchor="middle" fill="' + C_WHITE + '" font-size="14" font-weight="700" font-family="\'Times New Roman\',Times,serif;">' + str(num).zfill(2) + '</text></svg>'

def section_label(text):
    return '<p style="position:absolute;top:10px;left:60px;z-index:5;font-family:\'Times New Roman\',Times,serif;font-size:13px;font-weight:700;color:' + C_TEAL + ';letter-spacing:1px;">' + text + '</p>'

def slide_title(text):
    return '<p style="position:absolute;top:23px;left:60px;z-index:5;font-family:\'Times New Roman\',Times,serif;font-size:27px;font-weight:700;color:' + C_DARK + ';">' + text + '</p>'

def gold_sep(top=86):
    return '<div style="position:absolute;top:' + str(top) + 'px;left:60px;width:70px;height:3px;z-index:5;background:' + C_GOLD + ';border-radius:1.5px;"></div>'

def html_head(title):
    return '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>' + title + '</title>\n' + scale_snippet() + '\n</head>\n<body>\n' \
           '<div class="slide-content" style="width:960px;height:540px;position:relative;background:' + C_BG + ';font-family:\'Times New Roman\',Times,serif;color:' + C_TEXT + ';overflow:hidden;">\n' \
           '<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:' + C_WHITE + ';z-index:0;"></div>\n' + top_bar_svg()

def html_foot():
    return '</div>\n</body>\n</html>'

def bullet(text, color=C_DARK):
    return '<tr><td style="width:16px;vertical-align:top;padding:2px 4px 2px 0;"><span style="color:' + C_CORAL + ';font-size:16px;">▸</span></td>' \
           '<td style="vertical-align:top;padding:2px 0;font-size:14px;color:' + color + ';line-height:1.5;">' + text + '</td></tr>'

def sub_bullet(text):
    return '<tr><td style="width:16px;vertical-align:top;padding:1px 4px 1px 0;"></td>' \
           '<td style="vertical-align:top;padding:1px 0;font-size:13px;color:' + C_DARK + ';line-height:1.4;padding-left:16px;">' \
           '<span style="color:' + C_TEAL + ';font-size:14px;">▪</span> ' + text + '</td></tr>'


# ════════════════════════════════════════════════
# SLIDE 01 — COVER
# ════════════════════════════════════════════════
def slide_01():
    h = [
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>Cover — Hepatocellular Jaundice</title>\n',
        scale_snippet(),
        '\n</head>\n<body>\n',
        '<div class="slide-content" style="width:960px;height:540px;position:relative;background:' + C_BG + ';font-family:\'Times New Roman\',Times,serif;color:' + C_TEXT + ';overflow:hidden;">\n',
        '<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:' + C_DARK + ';z-index:0;"></div>\n',
        '<div style="position:absolute;top:0;left:0;width:960px;height:540px;z-index:1;background:radial-gradient(ellipse at 70% 50%, rgba(42,157,143,0.3) 0%, transparent 70%);"></div>\n',
        '<svg aria-hidden="true" style="position:absolute;top:0;left:0;z-index:2;" width="960" height="540" viewBox="0 0 960 540">\n',
        '  <rect x="0" y="0" width="12" height="540" fill="' + C_GOLD + '"/>\n',
        '  <circle cx="820" cy="80" r="120" fill="none" stroke="' + C_TEAL + '" stroke-width="1" opacity="0.3"/>\n',
        '  <circle cx="820" cy="80" r="180" fill="none" stroke="' + C_TEAL + '" stroke-width="0.5" opacity="0.15"/>\n',
        '  <rect x="70" y="130" width="80" height="5" rx="2.5" fill="' + C_GOLD + '"/>\n',
        '  <line x1="70" y1="400" x2="400" y2="400" stroke="' + C_TEAL + '" stroke-width="0.5" opacity="0.3"/>\n',
        '</svg>\n',
        '<p style="position:absolute;top:100px;left:70px;z-index:5;font-family:\'Times New Roman\',Times,serif;font-size:28px;color:' + C_GOLD + ';font-weight:400;letter-spacing:2px;opacity:0.9;">TROPICAL SUPPORT 41</p>\n',
        '<p style="position:absolute;top:150px;left:70px;z-index:5;font-family:\'Times New Roman\',Times,serif;font-size:48px;color:' + C_WHITE + ';font-weight:700;line-height:1.1;">Hepatocellular<br><span style="color:' + C_GOLD + ';">Jaundice</span></p>\n',
        '<p style="position:absolute;top:280px;left:70px;z-index:5;font-family:\'Times New Roman\',Times,serif;font-size:18px;color:' + C_TEAL + ';font-weight:400;">Gastroenterology Module — Tropical Medicine</p>\n',
        '<p style="position:absolute;top:320px;left:70px;z-index:5;font-family:\'Times New Roman\',Times,serif;font-size:14px;color:rgba(255,255,255,0.6);">Dr. Ayman Saker — Comprehensive Review with Clinical Management Guidelines</p>\n',
        '<svg aria-hidden="true" style="position:absolute;bottom:40px;right:50px;z-index:5;" width="60" height="60" viewBox="0 0 60 60">\n',
        '  <circle cx="30" cy="30" r="28" fill="none" stroke="' + C_GOLD + '" stroke-width="1.5" opacity="0.5"/>\n',
        '  <text x="30" y="35" text-anchor="middle" fill="' + C_GOLD + '" font-size="14" font-weight="700" font-family:\'Times New Roman\',Times,serif;" opacity="0.8">06</text>\n',
        '</svg>\n',
        html_foot()
    ]
    return ''.join(h)
# ════════════════════════════════════════════════
# SLIDE 02 — TABLE OF CONTENTS
# ════════════════════════════════════════════════
def slide_02():
    items = [
        ("01", "Definition &amp; Classification of Jaundice"),
        ("02", "Differentiation Between Types of Jaundice"),
        ("03", "Pathophysiology of Hepatocellular Jaundice"),
        ("04", "Causes of Hepatocellular Jaundice"),
        ("05", "Diagnosis — Biliary Obstruction vs Liver Disease"),
        ("06", "Clinical Presentations"),
        ("07", "Investigations — Laboratory &amp; Imaging"),
        ("08", "Treatment &amp; Management"),
    ]
    rows = ""
    for i, (num, title) in enumerate(items):
        rows += '<tr>\n'
        rows += '  <td style="width:40px;vertical-align:middle;text-align:center;"><span style="display:inline-block;width:28px;height:28px;line-height:28px;border-radius:50%;background:' + C_TEAL + ';color:' + C_WHITE + ';font-size:12px;font-weight:700;text-align:center;">' + num + '</span></td>\n'
        rows += '  <td style="vertical-align:middle;padding-left:10px;font-size:16px;color:' + C_DARK + ';font-weight:600;">' + title + '</td>\n'
        rows += '</tr>\n'
        if i < len(items) - 1:
            rows += '<tr><td colspan="2"><div style="height:1px;background:' + C_GOLD + ';opacity:0.3;margin:2px 0;"></div></td></tr>\n'

    return html_head("Table of Contents") + '''
''' + section_label("NAVIGATION") + '''
''' + slide_title("Table of Contents") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:100px;left:70px;right:70px;z-index:5;">
  <table style="width:100%;border-collapse:collapse;">
''' + rows + '''
  </table>
</div>
''' + page_badge(2) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 03 — DEFINITION
# ════════════════════════════════════════════════
def slide_03():
    return html_head("Definition of Jaundice") + '''
''' + section_label("SECTION 01 — DEFINITION &amp; CLASSIFICATION") + '''
''' + slide_title("Definition of Jaundice") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">
  <div style="background:''' + C_CARD + ''';border-radius:8px;padding:14px 18px;margin-bottom:14px;">
    <p style="font-family:'Times New Roman',Times,serif;font-size:14px;color:''' + C_TEXT + ''';margin:0;line-height:1.6;">
      <span style="font-weight:700;color:''' + C_CORAL + ''';">❖ Definition</span><br>
      Yellowish discoloration of the skin, sclera and mucous membranes when there is an elevation in the serum total bilirubin level that can be detected clinically.
    </p>
  </div>
  <table style="width:100%;border-collapse:collapse;">
    <tr>
      <td style="width:16px;vertical-align:top;padding:4px 6px 4px 0;"><span style="color:''' + C_TEAL + ''';font-size:16px;">▸</span></td>
      <td style="vertical-align:top;padding:4px 0;font-size:14px;color:''' + C_TEXT + ''';line-height:1.5;">In adults the normal upper limit for total bilirubin level is <span style="font-weight:700;color:''' + C_CORAL + ''';">1.2 mg/dL</span>.</td>
    </tr>
    <tr>
      <td style="width:16px;vertical-align:top;padding:4px 6px 4px 0;"><span style="color:''' + C_TEAL + ''';font-size:16px;">▸</span></td>
      <td style="vertical-align:top;padding:4px 0;font-size:14px;color:''' + C_TEXT + ''';line-height:1.5;">Jaundice only becomes clinically apparent when the total bilirubin rises to greater than <span style="font-weight:700;color:''' + C_CORAL + ''';">2 mg/dL</span>.</td>
    </tr>
    <tr>
      <td style="width:16px;vertical-align:top;padding:4px 6px 4px 0;"><span style="color:''' + C_TEAL + ''';font-size:16px;">▸</span></td>
      <td style="vertical-align:top;padding:4px 0;font-size:14px;color:''' + C_TEXT + ''';line-height:1.5;">First visible in the <span style="font-weight:700;color:''' + C_DARK + ''';">sclera</span> and <span style="font-weight:700;color:''' + C_DARK + ''';">sublingual area</span>.</td>
    </tr>
  </table>
</div>
''' + page_badge(3) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 04 — CLASSIFICATION
# ════════════════════════════════════════════════
def slide_04():
    return html_head("Classification of Jaundice") + '''
''' + section_label("SECTION 01 — DEFINITION &amp; CLASSIFICATION") + '''
''' + slide_title("Classification of Jaundice") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">
  <p style="font-family:'Times New Roman',Times,serif;font-size:16px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 10px 0;">Jaundice is classified according to:</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:12px 14px;border-left:4px solid ''' + C_TEAL + ''';">
      <p style="font-size:15px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 6px 0;">By Bilirubin Type</p>
      <table style="border-collapse:collapse;">
''' + bullet("Unconjugated (indirect) hyperbilirubinemia") + '''
''' + bullet("Conjugated (direct) hyperbilirubinemia") + '''
      </table>
    </div>
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:12px 14px;border-left:4px solid ''' + C_ORANGE + ''';">
      <p style="font-size:15px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 6px 0;">By Pathological Site</p>
      <table style="border-collapse:collapse;">
''' + bullet("Pre-hepatic (Hemolytic)") + '''
''' + bullet("Hepatic (Hepatocellular)") + '''
''' + bullet("Post-hepatic (Obstructive)") + '''
      </table>
    </div>
  </div>
  <div style="margin-top:16px;background:#fff3e0;border-radius:8px;padding:12px 16px;border:1px solid ''' + C_GOLD + ''';">
    <p style="font-size:13px;color:''' + C_DARK + ''';margin:0;line-height:1.5;">
      <span style="font-weight:700;">Key Point:</span> Hepatocellular jaundice results from hepatic (intrahepatic) pathology where the liver cells are damaged, impairing bilirubin uptake, conjugation, or excretion.
    </p>
  </div>
</div>
''' + page_badge(4) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 05 — DIFFERENTIATION TABLE
# ════════════════════════════════════════════════
def slide_05():
    return html_head("Differentiation Between Types of Jaundice") + '''
''' + section_label("SECTION 01 — DEFINITION &amp; CLASSIFICATION") + '''
''' + slide_title("Differentiation Between Types of Jaundice") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:100px;left:40px;right:40px;z-index:5;bottom:55px;overflow-y:auto;">
  <table style="width:100%;border-collapse:collapse;font-size:10.5px;font-family:'Times New Roman',Times,serif;">
    <thead>
      <tr style="background:''' + C_DARK + ''';color:''' + C_WHITE + ''';">
        <th style="padding:5px 4px;text-align:left;border:1px solid ''' + C_DARK + ''';">Parameter</th>
        <th style="padding:5px 4px;text-align:center;border:1px solid ''' + C_DARK + ''';">Normal</th>
        <th style="padding:5px 4px;text-align:center;border:1px solid ''' + C_DARK + ''';">Pre-hepatic (Hemolytic)</th>
        <th style="padding:5px 4px;text-align:center;border:1px solid ''' + C_DARK + ''';background:''' + C_ORANGE + ''';">Hepatic (Hepatocellular)</th>
        <th style="padding:5px 4px;text-align:center;border:1px solid ''' + C_DARK + ''';">Post-hepatic (Obstructive)</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background:''' + C_WHITE + ''';">
        <td style="padding:4px 4px;border:1px solid #ccc;font-weight:600;color:''' + C_DARK + ''';">Serum total bilirubin</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">&lt;1 mg/dL</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">Increased</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;background:#fff3e0;">Increased</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">Increased</td>
      </tr>
      <tr style="background:''' + C_CARD + ''';">
        <td style="padding:4px 4px;border:1px solid #ccc;font-weight:600;color:''' + C_DARK + ''';">Serum conjugated bilirubin</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">0.1–0.4 mg/dL</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">Normal</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;background:#fff3e0;">Increased ↑↑</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;color:''' + C_CORAL + ''';">Increased ↑↑↑↑</td>
      </tr>
      <tr style="background:''' + C_WHITE + ''';">
        <td style="padding:4px 4px;border:1px solid #ccc;font-weight:600;color:''' + C_DARK + ''';">Serum unconjugated bilirubin</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">0.2–0.7 mg/dL</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;color:''' + C_CORAL + ''';">Increased ↑↑↑↑</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;background:#fff3e0;">Increased ↑↑</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">Normal</td>
      </tr>
      <tr style="background:''' + C_CARD + ''';">
        <td style="padding:4px 4px;border:1px solid #ccc;font-weight:600;color:''' + C_DARK + ''';">Urine bilirubin</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">Absent</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">Absent</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;background:#fff3e0;">Present +</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;color:''' + C_CORAL + ''';">Present +++</td>
      </tr>
      <tr style="background:''' + C_WHITE + ''';">
        <td style="padding:4px 4px;border:1px solid #ccc;font-weight:600;color:''' + C_DARK + ''';">Urine urobilin</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">0.4 mg/day</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">Increased</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;background:#fff3e0;">Decreased</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">Absent</td>
      </tr>
      <tr style="background:''' + C_CARD + ''';">
        <td style="padding:4px 4px;border:1px solid #ccc;font-weight:600;color:''' + C_DARK + ''';">Fecal stercobilin</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">40–280 mg/day</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">Increased</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;background:#fff3e0;">Decreased</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">Absent</td>
      </tr>
      <tr style="background:''' + C_WHITE + ''';">
        <td style="padding:4px 4px;border:1px solid #ccc;font-weight:600;color:''' + C_DARK + ''';">Urine bile salts</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">Absent</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;">Absent</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;background:#fff3e0;">Present +</td>
        <td style="padding:4px 4px;border:1px solid #ccc;text-align:center;color:''' + C_CORAL + ''';">Present +++</td>
      </tr>
    </tbody>
  </table>
  <p style="font-size:10px;color:#666;margin:6px 0 0 0;text-align:center;">Key: ↑↑↑↑ = markedly increased, ↑↑ = moderately increased, + to +++ = degree of presence</p>
</div>
''' + page_badge(5) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 06 — PATHOPHYSIOLOGY OVERVIEW
# ════════════════════════════════════════════════
def slide_06():
    return html_head("Pathophysiology of Hepatocellular Jaundice") + '''
''' + section_label("SECTION 02 — PATHOPHYSIOLOGY") + '''
''' + slide_title("Pathophysiology of Hepatocellular Jaundice") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:14px 16px;border-top:4px solid ''' + C_TEAL + ''';">
      <p style="font-size:15px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 8px 0;">❖ Hepatocellular Uptake</p>
      <table style="border-collapse:collapse;">
''' + bullet("Bilirubin released from the reticuloendothelial system is in unconjugated form (non-soluble).") + '''
''' + bullet("Transported to hepatocytes bound to albumin (accomplishes solubility in blood).") + '''
''' + bullet("The albumin-bilirubin bond is broken, and bilirubin alone enters hepatocytes through carrier-membrane transport.") + '''
''' + bullet("Bound to proteins in the cytosol to decrease efflux of bilirubin back into the plasma.") + '''
      </table>
    </div>
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:14px 16px;border-top:4px solid ''' + C_ORANGE + ''';">
      <p style="font-size:15px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 8px 0;">❖ Conjugation of Bilirubin</p>
      <table style="border-collapse:collapse;">
''' + bullet("Unconjugated bilirubin proceeds to the endoplasmic reticulum.") + '''
''' + bullet("Undergoes conjugation to glucuronic acid.") + '''
''' + bullet("Results in the formation of conjugated bilirubin, which is soluble in the bile.") + '''
''' + bullet('This is rendered by the action of <span style="font-weight:700;color:' + C_CORAL + ';">UDP glucuronosyl transferase</span>.') + '''
      </table>
    </div>
  </div>
  <div style="margin-top:14px;background:#fff3e0;border-radius:8px;padding:10px 14px;border:1px solid ''' + C_GOLD + ''';">
    <p style="font-size:12px;color:''' + C_DARK + ''';margin:0;line-height:1.5;">
      <span style="font-weight:700;">Pathophysiology Summary:</span> In hepatocellular jaundice, damaged hepatocytes have impaired ability to take up, conjugate, and excrete bilirubin, leading to mixed conjugated and unconjugated hyperbilirubinemia.
    </p>
  </div>
</div>
''' + page_badge(6) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 07 — CAUSES: ACUTE HEPATOCELLULAR INJURY
# ════════════════════════════════════════════════
def slide_07():
    return html_head("Causes — Acute Hepatocellular Injury") + '''
''' + section_label("SECTION 03 — CAUSES OF HEPATOCELLULAR JAUNDICE") + '''
''' + slide_title("Causes — Acute Hepatocellular Injury") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">
  <div style="background:''' + C_CARD + ''';border-radius:8px;padding:10px 14px;margin-bottom:12px;border-left:4px solid ''' + C_CORAL + ''';">
    <p style="font-size:14px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 4px 0;">Acute or Subacute Hepatocellular Injury</p>
    <p style="font-size:12px;color:#555;margin:0;">Direct damage to hepatocytes causing impaired bilirubin metabolism</p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
    <div style="background:''' + C_WHITE + ''';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;">
      <table style="border-collapse:collapse;">
''' + bullet('<span style="font-weight:600;">Viral hepatitis</span> — HAV, HBV, HCV, HDV, HEV') + '''
''' + bullet('<span style="font-weight:600;">Hepatotoxins</span> — e.g. ethanol') + '''
''' + bullet('<span style="font-weight:600;">Drugs</span> — e.g. acetaminophen (paracetamol), many others') + '''
''' + bullet('<span style="font-weight:600;">Ischemia</span> — hypoperfusion injury') + '''
      </table>
    </div>
    <div style="background:''' + C_WHITE + ''';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;">
      <table style="border-collapse:collapse;">
''' + bullet('<span style="font-weight:600;">Metabolic disorders</span> — Wilson disease, Reye syndrome') + '''
''' + bullet('<span style="font-weight:600;">Pregnancy-related</span> — acute fatty liver of pregnancy, pre-eclampsia') + '''
''' + bullet('<span style="font-weight:600;">Autoimmune hepatitis</span>') + '''
      </table>
    </div>
  </div>
</div>
''' + page_badge(7) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 08 — CAUSES: CHRONIC HEPATOCELLULAR INJURY
# ════════════════════════════════════════════════
def slide_08():
    return html_head("Causes — Chronic Hepatocellular Injury") + '''
''' + section_label("SECTION 03 — CAUSES OF HEPATOCELLULAR JAUNDICE") + '''
''' + slide_title("Causes — Chronic Hepatocellular Injury") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">
  <div style="background:''' + C_CARD + ''';border-radius:8px;padding:10px 14px;margin-bottom:12px;border-left:4px solid ''' + C_ORANGE + ''';">
    <p style="font-size:14px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 4px 0;">Chronic Hepatocellular Injury</p>
    <p style="font-size:12px;color:#555;margin:0;">Persistent liver damage leading to cirrhosis and chronic jaundice</p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
    <div style="background:''' + C_WHITE + ''';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;">
      <table style="border-collapse:collapse;">
''' + bullet('<span style="font-weight:600;">Viral hepatitis</span> — chronic HBV, HCV') + '''
''' + bullet('<span style="font-weight:600;">Hepatotoxins</span> — e.g. ethanol (alcoholic liver disease)') + '''
''' + bullet('<span style="font-weight:600;">Non-alcoholic steatohepatitis</span> (NASH)') + '''
      </table>
    </div>
    <div style="background:''' + C_WHITE + ''';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;">
      <table style="border-collapse:collapse;">
''' + bullet('<span style="font-weight:600;">Autoimmune hepatitis</span>') + '''
''' + bullet('<span style="font-weight:600;">Metabolic disorders</span> — Wilson disease, hemochromatosis, alpha1-antitrypsin deficiency') + '''
      </table>
    </div>
  </div>
</div>
''' + page_badge(8) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 09 — CAUSES: INTRAHEPATIC CHOLESTASIS
# ════════════════════════════════════════════════
def slide_09():
    return html_head("Causes — Intrahepatic Cholestasis") + '''
''' + section_label("SECTION 03 — CAUSES OF HEPATOCELLULAR JAUNDICE") + '''
''' + slide_title("Causes — Intrahepatic Cholestasis") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">
  <div style="background:''' + C_CARD + ''';border-radius:8px;padding:10px 14px;margin-bottom:12px;border-left:4px solid ''' + C_CORAL + ''';">
    <p style="font-size:14px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 4px 0;">Intrahepatic Cholestasis</p>
    <p style="font-size:12px;color:#555;margin:0;">Impaired bile flow within the liver due to various pathological processes</p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
    <div style="background:''' + C_WHITE + ''';border-radius:6px;padding:10px 12px;border:1px solid #e0e0e0;border-top:3px solid ''' + C_TEAL + ''';">
      <p style="font-size:13px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 6px 0;">Diffuse Infiltrative Disorders</p>
      <table style="border-collapse:collapse;">
''' + bullet("Granulomatous disease") + '''
''' + bullet("Amyloidosis") + '''
''' + bullet("Malignancy (infiltrative liver metastases)") + '''
      </table>
    </div>
    <div style="background:''' + C_WHITE + ''';border-radius:6px;padding:10px 12px;border:1px solid #e0e0e0;border-top:3px solid ''' + C_ORANGE + ''';">
      <p style="font-size:13px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 6px 0;">Inflammation of Intrahepatic Bile Ductules</p>
      <table style="border-collapse:collapse;">
''' + bullet("Primary biliary cirrhosis (PBC)") + '''
''' + bullet("Graft versus host disease") + '''
''' + bullet("Drug-induced cholangiopathy") + '''
      </table>
    </div>
  </div>
  <div style="margin-top:10px;background:''' + C_WHITE + ''';border-radius:6px;padding:10px 12px;border:1px solid #e0e0e0;border-top:3px solid ''' + C_GOLD + ''';">
    <p style="font-size:13px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 6px 0;">Miscellaneous Conditions</p>
    <table style="border-collapse:collapse;">
''' + bullet("Benign recurrent intrahepatic cholestasis") + '''
''' + bullet("Intrahepatic cholestasis of pregnancy") + '''
''' + bullet("Drugs (many, e.g. estrogens, anabolic steroids)") + '''
''' + bullet("Total parenteral nutrition (TPN)") + '''
''' + bullet("Sepsis") + '''
''' + bullet("Atypical presentations of viral or alcoholic hepatitis") + '''
''' + bullet("Postoperative cholestasis") + '''
    </table>
  </div>
</div>
''' + page_badge(9) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 10 — DIAGNOSIS: HISTORY
# ════════════════════════════════════════════════
def slide_10():
    return html_head("Diagnosis — Biliary Obstruction vs Liver Disease (History)") + '''
''' + section_label("SECTION 04 — DIAGNOSIS") + '''
''' + slide_title("Diagnosis — Biliary Obstruction vs Liver Disease") + '''
''' + gold_sep() + '''
<p style="position:absolute;top:60px;left:60px;z-index:5;font-size:13px;color:''' + C_TEAL + ''';font-weight:600;">Features that differentiate biliary tract obstruction from cholestatic liver disease</p>
<div style="position:absolute;top:84px;left:40px;right:40px;z-index:5;bottom:55px;overflow-y:auto;">
  <table style="width:100%;border-collapse:collapse;font-size:12px;font-family:'Times New Roman',Times,serif;">
    <thead>
      <tr>
        <th style="width:25%;padding:6px 8px;text-align:left;background:''' + C_DARK + ''';color:''' + C_WHITE + ''';border:1px solid ''' + C_DARK + ''';">Feature</th>
        <th style="width:37.5%;padding:6px 8px;text-align:left;background:''' + C_TEAL + ''';color:''' + C_WHITE + ''';border:1px solid ''' + C_TEAL + ''';">Favors Biliary Obstruction</th>
        <th style="width:37.5%;padding:6px 8px;text-align:left;background:''' + C_ORANGE + ''';color:''' + C_WHITE + ''';border:1px solid ''' + C_ORANGE + ''';">Favors Liver Disease</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background:''' + C_WHITE + ''';">
        <td style="padding:6px 8px;border:1px solid #ccc;font-weight:700;color:''' + C_DARK + ''';" rowspan="4">History</td>
        <td style="padding:4px 8px;border:1px solid #ccc;">Abdominal pain</td>
        <td style="padding:4px 8px;border:1px solid #ccc;">Malaise, myalgias, arthralgias, suggestive of viral syndrome</td>
      </tr>
      <tr style="background:''' + C_WHITE + ''';">
        <td style="padding:4px 8px;border:1px solid #ccc;">Fever, rigors</td>
        <td style="padding:4px 8px;border:1px solid #ccc;">Known infectious exposure</td>
      </tr>
      <tr style="background:''' + C_WHITE + ''';">
        <td style="padding:4px 8px;border:1px solid #ccc;">Prior biliary surgery</td>
        <td style="padding:4px 8px;border:1px solid #ccc;">Receipt of blood products, intravenous or nasal use of illicit drugs</td>
      </tr>
      <tr style="background:''' + C_WHITE + ''';">
        <td style="padding:4px 8px;border:1px solid #ccc;">Older age</td>
        <td style="padding:4px 8px;border:1px solid #ccc;">—</td>
      </tr>
    </tbody>
  </table>
</div>
''' + page_badge(10) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 11 — DIAGNOSIS: PHYSICAL & INVESTIGATIONS
# ════════════════════════════════════════════════
def slide_11():
    return html_head("Diagnosis — Physical Examination & Investigations") + '''
''' + section_label("SECTION 04 — DIAGNOSIS") + '''
''' + slide_title("Diagnosis — Physical Examination &amp; Investigations") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:100px;left:40px;right:40px;z-index:5;bottom:55px;overflow-y:auto;">
  <table style="width:100%;border-collapse:collapse;font-size:11.5px;font-family:'Times New Roman',Times,serif;">
    <thead>
      <tr>
        <th style="width:22%;padding:5px 8px;text-align:left;background:''' + C_DARK + ''';color:''' + C_WHITE + ''';border:1px solid ''' + C_DARK + ''';">Feature</th>
        <th style="width:39%;padding:5px 8px;text-align:left;background:''' + C_TEAL + ''';color:''' + C_WHITE + ''';border:1px solid ''' + C_TEAL + ''';">Favors Biliary Obstruction</th>
        <th style="width:39%;padding:5px 8px;text-align:left;background:''' + C_ORANGE + ''';color:''' + C_WHITE + ''';border:1px solid ''' + C_ORANGE + ''';">Favors Liver Disease</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background:''' + C_WHITE + ''';">
        <td style="padding:5px 8px;border:1px solid #ccc;font-weight:700;color:''' + C_DARK + ''';" rowspan="5">Physical Examination</td>
        <td style="padding:3px 8px;border:1px solid #ccc;">Fever</td>
        <td style="padding:3px 8px;border:1px solid #ccc;">Exposure to known hepatotoxin</td>
      </tr>
      <tr style="background:''' + C_WHITE + ''';">
        <td style="padding:3px 8px;border:1px solid #ccc;">Abdominal tenderness</td>
        <td style="padding:3px 8px;border:1px solid #ccc;">Family history of liver disease</td>
      </tr>
      <tr style="background:''' + C_WHITE + ''';">
        <td style="padding:3px 8px;border:1px solid #ccc;">Palpable abdominal mass</td>
        <td style="padding:3px 8px;border:1px solid #ccc;">Ascites</td>
      </tr>
      <tr style="background:''' + C_WHITE + ''';">
        <td style="padding:3px 8px;border:1px solid #ccc;">Surgical scar</td>
        <td style="padding:3px 8px;border:1px solid #ccc;">Signs of chronic liver disease (prominent abdominal veins, gynecomastia, spider angiomata, asterixis, encephalopathy)</td>
      </tr>
      <tr style="background:''' + C_WHITE + ''';">
        <td style="padding:3px 8px;border:1px solid #ccc;">Ascites (as presenting sign)</td>
        <td style="padding:3px 8px;border:1px solid #ccc;">Signs of specific liver disease (Kayser-Fleischer rings, xanthelasmas)</td>
      </tr>
      <tr style="background:''' + C_CARD + ''';">
        <td style="padding:5px 8px;border:1px solid #ccc;font-weight:700;color:''' + C_DARK + ''';" rowspan="3">Investigation</td>
        <td style="padding:3px 8px;border:1px solid #ccc;">Predominant elevation of alkaline phosphatase</td>
        <td style="padding:3px 8px;border:1px solid #ccc;">Predominant elevation of serum aminotransferases</td>
      </tr>
      <tr style="background:''' + C_CARD + ''';">
        <td style="padding:3px 8px;border:1px solid #ccc;">Prothrombin time normal or normalizes with vitamin K administration</td>
        <td style="padding:3px 8px;border:1px solid #ccc;">Prolonged prothrombin time that does not correct with vitamin K</td>
      </tr>
      <tr style="background:''' + C_CARD + ''';">
        <td style="padding:3px 8px;border:1px solid #ccc;">Elevated serum lipase</td>
        <td style="padding:3px 8px;border:1px solid #ccc;">Decreased albumin concentration</td>
      </tr>
    </tbody>
  </table>
</div>
''' + page_badge(11) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 12 — CLINICAL PRESENTATIONS
# ════════════════════════════════════════════════
def slide_12():
    return html_head("Clinical Presentations") + '''
''' + section_label("SECTION 04 — DIAGNOSIS") + '''
''' + slide_title("Clinical Presentations") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:14px 16px;border-top:4px solid ''' + C_TEAL + ''';">
      <p style="font-size:15px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 8px 0;">❖ General Manifestations</p>
      <table style="border-collapse:collapse;">
''' + bullet("Symptoms and signs of chronic liver disease") + '''
''' + bullet("Fatigue, malaise, anorexia") + '''
''' + bullet("Weight loss") + '''
''' + bullet("Right upper quadrant discomfort") + '''
      </table>
    </div>
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:14px 16px;border-top:4px solid ''' + C_ORANGE + ''';">
      <p style="font-size:15px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 8px 0;">❖ Specific Manifestations of Hepatocellular Jaundice</p>
      <table style="border-collapse:collapse;">
''' + bullet("Orange-yellow sclera") + '''
''' + bullet("Pale stool (acholic stool)") + '''
''' + bullet("Dark urine (bilirubinuria)") + '''
      </table>
    </div>
  </div>
  <div style="margin-top:14px;background:#fff3e0;border-radius:8px;padding:12px 16px;border-left:4px solid ''' + C_CORAL + ''';">
    <p style="font-size:14px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 6px 0;">❖ Manifestations of Complications</p>
    <table style="border-collapse:collapse;">
''' + bullet("HCC — Hepatocellular Carcinoma") + '''
''' + bullet("HRS — Hepatorenal Syndrome") + '''
''' + bullet("SBP — Spontaneous Bacterial Peritonitis") + '''
''' + bullet("GI bleeding as hematemesis due to esophageal varices") + '''
    </table>
  </div>
</div>
''' + page_badge(12) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 13 — INVESTIGATIONS: LABORATORY (LFTs)
# ════════════════════════════════════════════════
def slide_13():
    return html_head("Investigations — Laboratory (Liver Function Tests)") + '''
''' + section_label("SECTION 05 — INVESTIGATIONS") + '''
''' + slide_title("Investigations — Laboratory (Liver Function Tests)") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">
  <div style="background:''' + C_CARD + ''';border-radius:8px;padding:10px 14px;margin-bottom:12px;border-left:4px solid ''' + C_TEAL + ''';">
    <p style="font-size:14px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 4px 0;">1) Liver Function Tests — Impaired</p>
    <p style="font-size:12px;color:#555;margin:0;">Typical pattern in hepatocellular jaundice</p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
    <div style="background:''' + C_WHITE + ''';border-radius:6px;padding:10px 12px;border:1px solid #e0e0e0;">
      <table style="border-collapse:collapse;">
''' + bullet('<span style="font-weight:600;">Transaminases (ALT &amp; AST)</span>: Increased — indicate hepatocellular injury') + '''
''' + bullet('<span style="font-weight:600;">Serum albumin</span>: Decreased') + '''
''' + bullet('<span style="font-weight:600;">Serum bilirubin</span>: Increased, mainly indirect (unconjugated) bilirubin') + '''
      </table>
    </div>
    <div style="background:''' + C_WHITE + ''';border-radius:6px;padding:10px 12px;border:1px solid #e0e0e0;">
      <table style="border-collapse:collapse;">
''' + bullet('<span style="font-weight:600;">Prothrombin time (PT)</span>: Prolonged') + '''
''' + bullet('<span style="font-weight:600;">Serum alkaline phosphatase (ALP)</span>: Increased') + '''
      </table>
    </div>
  </div>
  <div style="margin-top:10px;background:#fff3e0;border-radius:8px;padding:8px 12px;border:1px solid ''' + C_GOLD + ''';">
    <p style="font-size:12px;color:''' + C_DARK + ''';margin:0;line-height:1.5;">
      <span style="font-weight:700;">Key Pattern:</span> Hepatocellular injury shows predominant elevation of aminotransferases (ALT/AST) with elevated bilirubin (mainly unconjugated), prolonged PT that does not correct with vitamin K, and decreased albumin — reflecting impaired synthetic function.
    </p>
  </div>
</div>
''' + page_badge(13) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 14 — INVESTIGATIONS: CAUSE OF CIRRHOSIS
# ════════════════════════════════════════════════
def slide_14():
    return html_head("Investigations — Cause of Liver Cirrhosis") + '''
''' + section_label("SECTION 05 — INVESTIGATIONS") + '''
''' + slide_title("Investigations — Cause of Liver Cirrhosis") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">
  <div style="background:''' + C_CARD + ''';border-radius:8px;padding:10px 14px;margin-bottom:12px;border-left:4px solid ''' + C_ORANGE + ''';">
    <p style="font-size:14px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 4px 0;">2) Investigations for the Cause of Liver Cirrhosis</p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
    <div style="background:''' + C_WHITE + ''';border-radius:6px;padding:10px 12px;border:1px solid #e0e0e0;border-top:3px solid ''' + C_TEAL + ''';">
      <p style="font-size:13px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 6px 0;">Viral &amp; Autoimmune Serology</p>
      <table style="border-collapse:collapse;">
''' + bullet("Viral serology: HCV-AB, HBs-Ag") + '''
''' + bullet("Anti-nuclear antibody (ANA)") + '''
''' + bullet("Anti-liver kidney microsomal antibody (Anti-LKM Ab)") + '''
''' + bullet("Anti-smooth muscle antibody (Anti-SMA)") + '''
''' + bullet("Anti-mitochondrial antibody (AMA)") + '''
      </table>
    </div>
    <div style="background:''' + C_WHITE + ''';border-radius:6px;padding:10px 12px;border:1px solid #e0e0e0;border-top:3px solid ''' + C_ORANGE + ''';">
      <p style="font-size:13px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 6px 0;">Metabolic &amp; Other Tests</p>
      <table style="border-collapse:collapse;">
''' + bullet("Lipid profile") + '''
''' + bullet("Serum ceruloplasmin (for Wilson disease)") + '''
''' + bullet("Serum alpha1-antitrypsin level") + '''
      </table>
    </div>
  </div>
</div>
''' + page_badge(14) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 15 — INVESTIGATIONS: IMAGING
# ════════════════════════════════════════════════
def slide_15():
    return html_head("Investigations — Imaging") + '''
''' + section_label("SECTION 05 — INVESTIGATIONS") + '''
''' + slide_title("Investigations — Imaging") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">
  <div style="background:''' + C_CARD + ''';border-radius:8px;padding:10px 14px;margin-bottom:12px;border-left:4px solid ''' + C_TEAL + ''';">
    <p style="font-size:14px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 4px 0;">3) Imaging Modalities</p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
    <div style="background:''' + C_WHITE + ''';border-radius:8px;padding:14px 16px;border:1px solid #e0e0e0;border-top:4px solid ''' + C_TEAL + ''';">
      <p style="font-size:15px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 8px 0;">Abdominal Ultrasound</p>
      <table style="border-collapse:collapse;">
''' + bullet("Detect liver cirrhosis: echopattern, size (shrunken, average, or enlarged)") + '''
''' + bullet("Portal hypertension: dilated portal vein and splenomegaly") + '''
''' + bullet("Presence of ascites") + '''
''' + bullet("Hepatic focal lesions") + '''
      </table>
    </div>
    <div style="background:''' + C_WHITE + ''';border-radius:8px;padding:14px 16px;border:1px solid #e0e0e0;border-top:4px solid ''' + C_ORANGE + ''';">
      <p style="font-size:15px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 8px 0;">Triphasic CT / MRI</p>
      <table style="border-collapse:collapse;">
''' + bullet("For abdomen and pelvis") + '''
''' + bullet("In suspected cases with HCC (Hepatocellular Carcinoma)") + '''
''' + bullet("Provides detailed characterization of liver lesions") + '''
''' + bullet("Assesses vascular involvement and metastasis") + '''
      </table>
    </div>
  </div>
</div>
''' + page_badge(15) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 16 — INVESTIGATIONS: OTHERS & LIVER BIOPSY
# ════════════════════════════════════════════════
def slide_16():
    return html_head("Investigations — Other Modalities & Liver Biopsy") + '''
''' + section_label("SECTION 05 — INVESTIGATIONS") + '''
''' + slide_title("Investigations — Other Modalities &amp; Liver Biopsy") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;height:auto;">
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:14px 16px;border-top:4px solid ''' + C_TEAL + ''';">
      <p style="font-size:15px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 8px 0;">4) Other Modalities</p>
      <table style="border-collapse:collapse;">
''' + bullet('<span style="font-weight:600;">ERCP</span> (Endoscopic Retrograde Cholangiopancreatography)') + '''
''' + bullet('<span style="font-weight:600;">MRCP</span> (Magnetic Resonance Cholangiopancreatography)') + '''
      </table>
      <p style="font-size:12px;color:#555;margin:8px 0 0 0;line-height:1.4;">Both ERCP and MRCP are used to evaluate the biliary tree and pancreatic duct, helping differentiate intrahepatic from extrahepatic cholestasis.</p>
    </div>
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:14px 16px;border-top:4px solid ''' + C_CORAL + ''';">
      <p style="font-size:15px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 8px 0;">5) Liver Biopsy</p>
      <table style="border-collapse:collapse;">
''' + bullet("Performed in selected cases") + '''
''' + bullet("Helps confirm the underlying etiology") + '''
''' + bullet("Assesses degree of fibrosis and inflammation") + '''
''' + bullet("Guides treatment decisions") + '''
      </table>
      <p style="font-size:12px;color:#555;margin:8px 0 0 0;line-height:1.4;">Liver biopsy remains the gold standard for diagnosing certain causes of hepatocellular jaundice when non-invasive tests are inconclusive.</p>
    </div>
  </div>
</div>
''' + page_badge(16) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 17 — TREATMENT
# ════════════════════════════════════════════════
def slide_17():
    return html_head("Treatment & Management") + '''
''' + section_label("SECTION 06 — TREATMENT") + '''
''' + slide_title("Treatment &amp; Management") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:14px 16px;border-top:4px solid ''' + C_TEAL + ''';">
      <p style="font-size:15px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 8px 0;">❖ General Measures</p>
      <table style="border-collapse:collapse;">
''' + bullet("Good hydration — maintain adequate fluid intake") + '''
''' + bullet("Ursodeoxycholic acid (UDCA) — to improve bile flow and reduce cholestasis") + '''
      </table>
    </div>
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:14px 16px;border-top:4px solid ''' + C_ORANGE + ''';">
      <p style="font-size:15px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 8px 0;">❖ Treatment of the Cause</p>
      <p style="font-size:13px;font-weight:700;color:''' + C_TEAL + ''';margin:0 0 4px 0;">Liver Cirrhosis</p>
      <table style="border-collapse:collapse;">
''' + bullet('<span style="font-weight:600;">Antiviral treatment</span> for HBV or HCV') + '''
''' + bullet('<span style="font-weight:600;">Corticosteroids</span> and <span style="font-weight:600;">immunosuppressants</span> for autoimmune disease') + '''
      </table>
    </div>
  </div>
  <div style="margin-top:14px;background:#fff3e0;border-radius:8px;padding:10px 14px;border:1px solid ''' + C_GOLD + ''';">
    <p style="font-size:13px;color:''' + C_DARK + ''';margin:0;line-height:1.5;">
      <span style="font-weight:700;">Management Summary:</span> The treatment of hepatocellular jaundice focuses on (1) supportive care with hydration and UDCA, (2) addressing the underlying cause of liver disease (antivirals for viral hepatitis, immunosuppression for autoimmune hepatitis), and (3) managing complications of chronic liver disease such as HCC, HRS, SBP, and variceal bleeding.
    </p>
  </div>
</div>
''' + page_badge(17) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 18 — SUMMARY
# ════════════════════════════════════════════════
def slide_18():
    return html_head("Summary — Key Takeaways") + '''
''' + section_label("SECTION 07 — SUMMARY") + '''
''' + slide_title("Summary — Key Takeaways") + '''
''' + gold_sep() + '''
<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:10px 14px;border-left:4px solid ''' + C_TEAL + ''';">
      <p style="font-size:12px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 4px 0;">Definition &amp; Classification</p>
      <p style="font-size:11px;color:#555;margin:0;line-height:1.4;">Jaundice = bilirubin &gt;2 mg/dL. Classified by bilirubin type (unconjugated/conjugated) or site (pre-hepatic/hepatic/post-hepatic).</p>
    </div>
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:10px 14px;border-left:4px solid ''' + C_ORANGE + ''';">
      <p style="font-size:12px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 4px 0;">Pathophysiology</p>
      <p style="font-size:11px;color:#555;margin:0;line-height:1.4;">Hepatocellular uptake &amp; conjugation impaired. UDP-glucuronosyl transferase conjugates bilirubin in ER.</p>
    </div>
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:10px 14px;border-left:4px solid ''' + C_CORAL + ''';">
      <p style="font-size:12px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 4px 0;">Causes</p>
      <p style="font-size:11px;color:#555;margin:0;line-height:1.4;">Acute/chronic hepatocellular injury (viral, toxins, drugs, metabolic) &amp; intrahepatic cholestasis (infiltrative, inflammatory, miscellaneous).</p>
    </div>
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:10px 14px;border-left:4px solid ''' + C_GOLD + ''';">
      <p style="font-size:12px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 4px 0;">Diagnosis</p>
      <p style="font-size:11px;color:#555;margin:0;line-height:1.4;">History, physical exam &amp; investigations differentiate biliary obstruction from liver disease. Look for signs of chronic liver disease.</p>
    </div>
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:10px 14px;border-left:4px solid ''' + C_TEAL + ''';">
      <p style="font-size:12px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 4px 0;">Clinical Features</p>
      <p style="font-size:11px;color:#555;margin:0;line-height:1.4;">Orange-yellow sclera, pale stool, dark urine. Complications: HCC, HRS, SBP, variceal bleeding.</p>
    </div>
    <div style="background:''' + C_CARD + ''';border-radius:8px;padding:10px 14px;border-left:4px solid ''' + C_ORANGE + ''';">
      <p style="font-size:12px;font-weight:700;color:''' + C_DARK + ''';margin:0 0 4px 0;">Treatment</p>
      <p style="font-size:11px;color:#555;margin:0;line-height:1.4;">Hydration + UDCA + treat cause (antivirals for HBV/HCV, immunosuppressants for autoimmune). Manage complications.</p>
    </div>
  </div>
  <div style="margin-top:12px;background:''' + C_DARK + ''';border-radius:8px;padding:10px 16px;text-align:center;">
    <p style="font-size:14px;color:''' + C_GOLD + ''';font-weight:700;margin:0;">Hepatocellular Jaundice — Complete Review</p>
  </div>
</div>
''' + page_badge(18) + '''
''' + html_foot()


# ════════════════════════════════════════════════
# GENERATE ALL SLIDES
# ════════════════════════════════════════════════
slides = [
    ("slide-01.html", slide_01),
    ("slide-02.html", slide_02),
    ("slide-03.html", slide_03),
    ("slide-04.html", slide_04),
    ("slide-05.html", slide_05),
    ("slide-06.html", slide_06),
    ("slide-07.html", slide_07),
    ("slide-08.html", slide_08),
    ("slide-09.html", slide_09),
    ("slide-10.html", slide_10),
    ("slide-11.html", slide_11),
    ("slide-12.html", slide_12),
    ("slide-13.html", slide_13),
    ("slide-14.html", slide_14),
    ("slide-15.html", slide_15),
    ("slide-16.html", slide_16),
    ("slide-17.html", slide_17),
    ("slide-18.html", slide_18),
]

for fname, func in slides:
    path = os.path.join(OUT_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(func())
    print("OK " + fname)

print("\nAll " + str(len(slides)) + " slides generated in " + OUT_DIR)
