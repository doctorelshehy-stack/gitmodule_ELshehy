#!/usr/bin/env python3
"""
Generate all 13 HTML slides for: 04 - Biliary System - Gallstones
Palette 10: #264653 #2a9d8f #e9c46a #f4a261 #e76f51
Font: Times New Roman
Dimensions: 960x540
"""

import os

# Palette colors
C1 = "#264653"  # Dark teal (primary)
C2 = "#2a9d8f"  # Teal green (accent)
C3 = "#e9c46a"  # Gold (highlight)
C4 = "#f4a261"  # Orange (warm accent)
C5 = "#e76f51"  # Coral (alert/important)
WHITE = "#ffffff"
LIGHT_BG = "#f0f7f7"

# Directory
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SLIDES_DIR = os.path.join(OUT_DIR, "slides")

# Appendix A scaling snippet (required in every file)
APPENDIX_A = """<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
html, body { margin:0; padding:0; width:100%; height:100%; overflow:hidden; display:flex; justify-content:center; align-items:center; background:#000; }
.slide-content { width:960px; height:540px; position:relative; transform-origin:center center; }
</style>
<script>
function scaleSlide(){const s=document.querySelector('.slide-content');if(!s)return;const sx=window.innerWidth/960;const sy=window.innerHeight/540;const sc=Math.min(sx,sy);s.style.width='960px';s.style.height='540px';s.style.transform=`scale(${sc})`;s.style.transformOrigin='center center';s.style.flexShrink='0';}
window.addEventListener('load',scaleSlide);window.addEventListener('resize',scaleSlide);
</script>"""


def page_badge(num, total=13):
    """SVG page number badge - bottom right"""
    return f'''<svg style="position:absolute; right:32px; bottom:24px; z-index:50;" width="48" height="28" viewBox="0 0 48 28" aria-hidden="true">
  <rect x="0" y="0" width="48" height="28" rx="14" fill="{C1}" opacity="0.85"/>
  <text x="24" y="19" text-anchor="middle" fill="{WHITE}" font-family="Times New Roman, serif" font-size="14" font-weight="600">{num}</text>
</svg>'''


def write_slide(num, content, filename=None):
    if filename is None:
        filename = f"slide-{num:02d}.html"
    path = os.path.join(SLIDES_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Written: {filename}")


# ============================================================
# SLIDE 01 - COVER PAGE
# ============================================================
slide_01 = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="background: {C1}; overflow:hidden;">
  <!-- Background SVG decoration -->
  <svg style="position:absolute; top:0; left:0; width:960px; height:540px; z-index:0;" viewBox="0 0 960 540" aria-hidden="true">
    <!-- Large circle top-right -->
    <circle cx="780" cy="-80" r="320" fill="{C2}" opacity="0.12"/>
    <!-- Smaller circle -->
    <circle cx="850" cy="120" r="140" fill="{C3}" opacity="0.10"/>
    <!-- Diagonal band -->
    <rect x="-50" y="380" width="1100" height="220" fill="{C2}" opacity="0.08" transform="rotate(-8 480 490)"/>
    <!-- Accent bar left -->
    <rect x="0" y="0" width="8" height="540" fill="{C2}"/>
    <!-- Small decorative circles -->
    <circle cx="100" cy="460" r="40" fill="{C3}" opacity="0.15"/>
    <circle cx="200" cy="500" r="20" fill="{C5}" opacity="0.10"/>
  </svg>

  <!-- Gold accent bar -->
  <div style="position:absolute; top:140px; left:70px; width:80px; height:5px; background:{C3}; border-radius:2px; z-index:5;"></div>

  <!-- Title -->
  <p style="position:absolute; top:158px; left:70px; font-size:52px; font-weight:700; color:{WHITE}; z-index:10; line-height:1.15; letter-spacing:-0.5px;">
    Biliary System
  </p>
  <p style="position:absolute; top:228px; left:70px; font-size:42px; font-weight:700; color:{C3}; z-index:10; line-height:1.15;">
    Gallstones
  </p>

  <!-- Subtitle -->
  <p style="position:absolute; top:300px; left:70px; font-size:20px; color:{WHITE}; opacity:0.85; z-index:10; max-width:520px; line-height:1.5;">
    Classification, Risk Factors, Clinical Presentations,<br>Investigations &amp; Management
  </p>

  <!-- Bottom info bar -->
  <div style="position:absolute; bottom:0; left:0; right:0; height:56px; background:rgba(0,0,0,0.25); z-index:5;"></div>
  <p style="position:absolute; bottom:16px; left:70px; font-size:14px; color:{C3}; z-index:10; font-style:italic;">
    Gastro-enterology &amp; Internal Medicine
  </p>
  <p style="position:absolute; bottom:16px; right:70px; font-size:14px; color:rgba(255,255,255,0.6); z-index:10;">
    GALL BLADDER STONES
  </p>

  <!-- Liver icon (SVG) -->
  <svg style="position:absolute; right:80px; top:100px; z-index:2;" width="200" height="260" viewBox="0 0 200 260" aria-hidden="true">
    <!-- Stylized liver/gallbladder -->
    <ellipse cx="100" cy="100" rx="80" ry="55" fill="{C2}" opacity="0.2"/>
    <ellipse cx="100" cy="95" rx="70" ry="45" fill="{C2}" opacity="0.3"/>
    <!-- Gallbladder -->
    <path d="M 110 130 Q 110 180 100 200 Q 90 180 90 130 Z" fill="{C3}" opacity="0.5"/>
    <ellipse cx="100" cy="125" rx="14" ry="18" fill="{C3}" opacity="0.6"/>
    <!-- Stone inside -->
    <circle cx="100" cy="145" r="6" fill="{C5}" opacity="0.7"/>
    <circle cx="95" cy="155" r="4" fill="{C5}" opacity="0.6"/>
    <circle cx="106" cy="158" r="3" fill="{C5}" opacity="0.5"/>
    <!-- Duct -->
    <line x1="100" y1="200" x2="100" y2="240" stroke="{C2}" stroke-width="4" opacity="0.4"/>
  </svg>
</div>
</body>
</html>'''
write_slide(1, slide_01)


# ============================================================
# SLIDE 02 - TABLE OF CONTENTS
# ============================================================
toc_items = [
    ("01", "Introduction & Bile Composition", "Normal bile components and overview"),
    ("02", "Types of Gallstones", "Cholesterol, Black pigment, Brown pigment"),
    ("03", "Risk Factors", "13 factors for cholesterol gallstone formation"),
    ("04", "Clinical Presentations", "8 presentations from asymptomatic to cancer"),
    ("05", "Investigations", "USG, ERCP, MRCP, CT and more"),
    ("06", "Management", "Cholecystectomy and treatment approaches"),
    ("07", "Chronic Cholecystitis", "Biliary colic, Murphy's sign, treatment"),
    ("08", "Acute Cholecystitis", "Chemical & bacterial inflammation"),
    ("09", "Acute Cholangitis", "Charcot's triad and urgent treatment"),
    ("10", "PTC", "Percutaneous transhepatic cholangiography"),
]

# Build TOC items HTML
toc_html = ""
for i, (num, title, desc) in enumerate(toc_items):
    y = 100 + i * 42
    toc_html += f'''
  <div style="position:absolute; top:{y}px; left:70px; z-index:5;">
    <span style="display:inline-block; width:36px; font-size:18px; font-weight:700; color:{C2};">{num}</span>
    <span style="font-size:16px; font-weight:600; color:{C1};">{title}</span>
    <span style="font-size:12px; color:#666; margin-left:10px;">{desc}</span>
  </div>'''
    # Separator line
    if i < len(toc_items) - 1:
        toc_html += f'''
  <div style="position:absolute; top:{y + 30}px; left:106px; width:740px; height:1px; background:{C2}; opacity:0.2; z-index:1;"></div>'''

slide_02 = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="background: {WHITE}; overflow:hidden;">
  <!-- Left accent bar -->
  <div style="position:absolute; top:0; left:0; width:54px; height:540px; background:{C1}; z-index:2;"></div>
  <div style="position:absolute; top:0; left:54px; width:4px; height:540px; background:{C2}; z-index:2;"></div>

  <!-- Header -->
  <p style="position:absolute; top:36px; left:80px; font-size:32px; font-weight:700; color:{C1}; z-index:10;">Table of Contents</p>
  <div style="position:absolute; top:80px; left:80px; width:100px; height:3px; background:{C2}; border-radius:1.5px; z-index:1;"></div>

  {toc_html}

  {page_badge(2)}
</div>
</body>
</html>'''
write_slide(2, slide_02)


# ============================================================
# SLIDE 03 - Introduction & Bile Composition
# ============================================================
slide_03 = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="background: {LIGHT_BG}; overflow:hidden;">
  <!-- Header bar -->
  <div style="position:absolute; top:0; left:0; right:0; height:60px; background:{C1}; z-index:2;"></div>
  <p style="position:absolute; top:14px; left:60px; font-size:22px; font-weight:700; color:{WHITE}; z-index:10;">Introduction &amp; Bile Composition</p>
  <p style="position:absolute; top:16px; right:60px; font-size:14px; color:{C3}; z-index:10;">Slide 3 of 13</p>

  <!-- Main statement -->
  <div style="position:absolute; top:80px; left:60px; right:60px; z-index:5;">
    <div style="background:{C3}; display:inline-block; padding:6px 16px; border-radius:4px;">
      <span style="font-size:16px; font-weight:700; color:{C1};">Gallstones are the most common abdominal reason for hospital admission</span>
    </div>
  </div>

  <!-- Left column: Normal Bile Composition -->
  <div style="position:absolute; top:130px; left:60px; width:420px; z-index:5;">
    <p style="font-size:20px; font-weight:700; color:{C1}; margin-bottom:10px;">Normal Bile Composition</p>

    <!-- Pie-chart style bars -->
    <div style="margin-bottom:6px;">
      <div style="display:flex; align-items:center; margin-bottom:4px;">
        <span style="width:180px; font-size:14px; color:{C1};">Bile salts</span>
        <div style="flex:1; height:22px; background:rgba(42,157,143,0.2); border-radius:4px; position:relative;">
          <div style="width:70%; height:100%; background:{C2}; border-radius:4px;"></div>
          <span style="position:absolute; right:6px; top:2px; font-size:12px; font-weight:600; color:{WHITE};">70%</span>
        </div>
      </div>
      <div style="display:flex; align-items:center; margin-bottom:4px;">
        <span style="width:180px; font-size:14px; color:{C1};">Phospholipids (Lecithin)</span>
        <div style="flex:1; height:22px; background:rgba(233,196,106,0.3); border-radius:4px; position:relative;">
          <div style="width:22%; height:100%; background:{C3}; border-radius:4px;"></div>
          <span style="position:absolute; left:calc(22% + 4px); top:2px; font-size:12px; font-weight:600; color:{C1};">22%</span>
        </div>
      </div>
      <div style="display:flex; align-items:center; margin-bottom:4px;">
        <span style="width:180px; font-size:14px; color:{C1};">Cholesterol</span>
        <div style="flex:1; height:22px; background:rgba(244,162,97,0.2); border-radius:4px; position:relative;">
          <div style="width:4%; height:100%; background:{C4}; border-radius:4px;"></div>
          <span style="position:absolute; left:calc(4% + 4px); top:2px; font-size:12px; font-weight:600; color:{C1};">4%</span>
        </div>
      </div>
      <div style="display:flex; align-items:center; margin-bottom:4px;">
        <span style="width:180px; font-size:14px; color:{C1};">Proteins</span>
        <div style="flex:1; height:22px; background:rgba(231,111,81,0.2); border-radius:4px; position:relative;">
          <div style="width:3%; height:100%; background:{C5}; border-radius:4px;"></div>
          <span style="position:absolute; left:calc(3% + 4px); top:2px; font-size:12px; font-weight:600; color:{C1};">3%</span>
        </div>
      </div>
      <div style="display:flex; align-items:center; margin-bottom:4px;">
        <span style="width:180px; font-size:14px; color:{C1};">Bilirubin</span>
        <div style="flex:1; height:22px; background:rgba(42,157,143,0.15); border-radius:4px; position:relative;">
          <div style="width:1%; height:100%; background:{C1}; border-radius:4px;"></div>
          <span style="position:absolute; left:calc(1% + 4px); top:2px; font-size:12px; font-weight:600; color:{C1};">0.3%</span>
        </div>
      </div>
    </div>
    <p style="font-size:12px; color:#888; margin-top:4px;">Bile salts = mainly cholic &amp; chenodeoxycholic acids</p>
  </div>

  <!-- Right column: Key facts -->
  <div style="position:absolute; top:130px; right:60px; width:380px; z-index:5;">
    <p style="font-size:20px; font-weight:700; color:{C1}; margin-bottom:12px;">Key Facts</p>

    <div style="background:{WHITE}; border-left:4px solid {C2}; padding:12px 16px; margin-bottom:10px; border-radius:0 6px 6px 0;">
      <p style="font-size:14px; color:{C1}; line-height:1.5;">
        <span style="font-weight:700;">Cholesterol stones</span> form when bile becomes supersaturated with cholesterol. Decreased gallbladder motility further aids stone formation.
      </p>
    </div>

    <div style="background:{WHITE}; border-left:4px solid {C4}; padding:12px 16px; margin-bottom:10px; border-radius:0 6px 6px 0;">
      <p style="font-size:14px; color:{C1}; line-height:1.5;">
        <span style="font-weight:700;">Black pigment stones</span> consist of 70% calcium bilirubinate. More common in hemolytic diseases and cirrhosis.
      </p>
    </div>

    <div style="background:{WHITE}; border-left:4px solid {C5}; padding:12px 16px; margin-bottom:10px; border-radius:0 6px 6px 0;">
      <p style="font-size:14px; color:{C1}; line-height:1.5;">
        <span style="font-weight:700;">Brown pigment stones</span> form due to stasis &amp; infection. E. coli &amp; Klebsiella produce β-glucuronidase converting bilirubin to insoluble form.
      </p>
    </div>

    <div style="background:{WHITE}; border-left:4px solid {C3}; padding:12px 16px; border-radius:0 6px 6px 0;">
      <p style="font-size:14px; color:{C1}; line-height:1.5;">
        <span style="font-weight:700;">Ascaris lumbricoides</span> has been implicated in brown pigment stone formation.
      </p>
    </div>
  </div>

  {page_badge(3)}
</div>
</body>
</html>'''
write_slide(3, slide_03)


# ============================================================
# SLIDE 04 - Types of Gallstones
# ============================================================
slide_04 = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="background: {WHITE}; overflow:hidden;">
  <!-- Header bar -->
  <div style="position:absolute; top:0; left:0; right:0; height:60px; background:{C1}; z-index:2;"></div>
  <p style="position:absolute; top:14px; left:60px; font-size:22px; font-weight:700; color:{WHITE}; z-index:10;">Types of Gallstones</p>

  <!-- Three columns -->
  <!-- Column 1: Cholesterol Stones -->
  <div style="position:absolute; top:80px; left:40px; width:280px; z-index:5;">
    <svg width="280" height="60" viewBox="0 0 280 60" aria-hidden="true">
      <rect x="0" y="0" width="280" height="60" rx="8" fill="{C2}"/>
      <text x="140" y="38" text-anchor="middle" fill="{WHITE}" font-family="Times New Roman, serif" font-size="16" font-weight="700">Cholesterol Stones</text>
    </svg>
    <div style="background:{LIGHT_BG}; border-radius:0 0 8px 8px; padding:16px; margin-top:-2px;">
      <div style="display:flex; align-items:center; margin-bottom:10px;">
        <div style="width:48px; height:48px; background:{C2}; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:12px;">
          <span style="font-size:22px; font-weight:700; color:{WHITE};">80%</span>
        </div>
        <span style="font-size:14px; color:{C1}; font-weight:600;">of all GB stones</span>
      </div>
      <p style="font-size:13px; color:{C1}; line-height:1.6; margin-bottom:6px;">
        <span style="font-weight:600;">Mechanism:</span> Supersaturation of bile with cholesterol
      </p>
      <p style="font-size:13px; color:{C1}; line-height:1.6; margin-bottom:6px;">
        <span style="font-weight:600;">Contributing factor:</span> Decreased GB motility
      </p>
      <p style="font-size:13px; color:{C1}; line-height:1.6;">
        Most common type worldwide, associated with obesity and high-fat diets
      </p>
    </div>
  </div>

  <!-- Column 2: Black Pigment Stones -->
  <div style="position:absolute; top:80px; left:340px; width:280px; z-index:5;">
    <svg width="280" height="60" viewBox="0 0 280 60" aria-hidden="true">
      <rect x="0" y="0" width="280" height="60" rx="8" fill="{C1}"/>
      <text x="140" y="38" text-anchor="middle" fill="{WHITE}" font-family="Times New Roman, serif" font-size="16" font-weight="700">Black Pigment Stones</text>
    </svg>
    <div style="background:{LIGHT_BG}; border-radius:0 0 8px 8px; padding:16px; margin-top:-2px;">
      <p style="font-size:13px; color:{C1}; line-height:1.6; margin-bottom:8px;">
        <span style="font-weight:600;">Composition:</span> 70% Calcium bilirubinate
      </p>
      <p style="font-size:13px; color:{C1}; line-height:1.6; margin-bottom:10px;">
        <span style="font-weight:600;">Associated with:</span>
      </p>
      <ul style="margin:0; padding-left:18px;">
        <li style="font-size:13px; color:{C1}; margin-bottom:4px;">Sickle cell anaemia</li>
        <li style="font-size:13px; color:{C1}; margin-bottom:4px;">Hereditary spherocytosis</li>
        <li style="font-size:13px; color:{C1}; margin-bottom:4px;">Thalassaemia</li>
        <li style="font-size:13px; color:{C1};">Liver cirrhosis</li>
      </ul>
    </div>
  </div>

  <!-- Column 3: Brown Pigment Stones -->
  <div style="position:absolute; top:80px; right:40px; width:280px; z-index:5;">
    <svg width="280" height="60" viewBox="0 0 280 60" aria-hidden="true">
      <rect x="0" y="0" width="280" height="60" rx="8" fill="{C5}"/>
      <text x="140" y="38" text-anchor="middle" fill="{WHITE}" font-family="Times New Roman, serif" font-size="16" font-weight="700">Brown Pigment Stones</text>
    </svg>
    <div style="background:{LIGHT_BG}; border-radius:0 0 8px 8px; padding:16px; margin-top:-2px;">
      <p style="font-size:13px; color:{C1}; line-height:1.6; margin-bottom:8px;">
        <span style="font-weight:600;">Incidence:</span> &lt; 5% of all stones
      </p>
      <p style="font-size:13px; color:{C1}; line-height:1.6; margin-bottom:8px;">
        <span style="font-weight:600;">Location:</span> Intrahepatic &amp; extrahepatic bile ducts + GB
      </p>
      <p style="font-size:13px; color:{C1}; line-height:1.6; margin-bottom:6px;">
        <span style="font-weight:600;">Cause:</span> Stasis + infection
      </p>
      <p style="font-size:12px; color:{C4}; line-height:1.5;">
        E. coli &amp; Klebsiella → β-glucuronidase → converts conjugated bilirubin to insoluble unconjugated state
      </p>
      <p style="font-size:12px; color:#888; margin-top:6px;">
        Soft, earthy, brown stones
      </p>
    </div>
  </div>

  {page_badge(4)}
</div>
</body>
</html>'''
write_slide(4, slide_04)


# ============================================================
# SLIDE 05 - Risk Factors
# ============================================================
risk_factors_left = [
    ("01", "Age > 40 years"),
    ("02", "Female sex (2× risk than men)"),
    ("03", "Oral contraception"),
    ("04", "High fat, low fiber diet"),
    ("05", "Obesity"),
    ("06", "Pregnancy (increased in multipara)"),
]
risk_factors_right = [
    ("07", "Hyperlipidaemia / Anti-hyperlipidaemic drugs (clofibrate)"),
    ("08", "Bile salt loss (ileal disease or resection)"),
    ("09", "Cystic fibrosis"),
    ("10", "Gall bladder dysmotility"),
    ("11", "Prolonged fasting / TPN"),
    ("12", "Liver cirrhosis"),
    ("13", "Biliary sludge"),
]

rf_left_html = ""
for num, text in risk_factors_left:
    rf_left_html += f'''
    <div style="display:flex; align-items:flex-start; margin-bottom:10px;">
      <div style="min-width:32px; height:32px; background:{C2}; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:10px; margin-top:1px;">
        <span style="font-size:13px; font-weight:700; color:{WHITE};">{num}</span>
      </div>
      <span style="font-size:14px; color:{C1}; line-height:1.5;">{text}</span>
    </div>'''

rf_right_html = ""
for num, text in risk_factors_right:
    rf_right_html += f'''
    <div style="display:flex; align-items:flex-start; margin-bottom:10px;">
      <div style="min-width:32px; height:32px; background:{C4}; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:10px; margin-top:1px;">
        <span style="font-size:13px; font-weight:700; color:{WHITE};">{num}</span>
      </div>
      <span style="font-size:14px; color:{C1}; line-height:1.5;">{text}</span>
    </div>'''

slide_05 = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="background: {LIGHT_BG}; overflow:hidden;">
  <!-- Header bar -->
  <div style="position:absolute; top:0; left:0; right:0; height:60px; background:{C1}; z-index:2;"></div>
  <p style="position:absolute; top:14px; left:60px; font-size:22px; font-weight:700; color:{WHITE}; z-index:10;">Risk Factors for Cholesterol Gallstones</p>

  <!-- Banner -->
  <div style="position:absolute; top:74px; left:60px; background:{C3}; padding:6px 20px; border-radius:4px; z-index:5;">
    <span style="font-size:15px; font-weight:700; color:{C1};">13 Known Risk Factors</span>
  </div>

  <!-- Left column -->
  <div style="position:absolute; top:110px; left:60px; width:400px; z-index:5;">
    {rf_left_html}
  </div>

  <!-- Right column -->
  <div style="position:absolute; top:110px; right:60px; width:440px; z-index:5;">
    {rf_right_html}
  </div>

  <!-- Center divider -->
  <div style="position:absolute; top:110px; left:478px; width:2px; height:400px; background:{C2}; opacity:0.2; z-index:1;"></div>

  {page_badge(5)}
</div>
</body>
</html>'''
write_slide(5, slide_05)


# ============================================================
# SLIDE 06 - Clinical Presentations
# ============================================================
presentations = [
    ("1", "Asymptomatic", "Discovered incidentally", C2),
    ("2", "Chronic Calcular Cholecystitis", "Biliary colic episodes", C2),
    ("3", "Acute Cholecystitis", "Chemical + bacterial infection", C3),
    ("4", "Cholestasis", "Bile flow obstruction", C4),
    ("5", "Acute Cholangitis", "Charcot's triad", C5),
    ("6", "Acute Pancreatitis", "CBD stone obstruction", C4),
    ("7", "Gall Stone Ileus", "Bowel obstruction", C5),
    ("8", "GB Adenocarcinoma", "Malignant transformation", C1),
]

pres_html = ""
for i, (num, title, desc, color) in enumerate(presentations):
    col = i % 4
    row = i // 4
    x = 40 + col * 225
    y = 90 + row * 210
    pres_html += f'''
  <div style="position:absolute; top:{y}px; left:{x}px; width:205px; z-index:5;">
    <svg width="205" height="50" viewBox="0 0 205 50" aria-hidden="true">
      <rect x="0" y="0" width="205" height="50" rx="6" fill="{color}"/>
      <text x="18" y="32" fill="{WHITE}" font-family="Times New Roman, serif" font-size="24" font-weight="700">{num}</text>
      <text x="45" y="32" fill="{WHITE}" font-family="Times New Roman, serif" font-size="15" font-weight="600">{title}</text>
    </svg>
    <p style="font-size:13px; color:#555; margin-top:6px; padding-left:4px;">{desc}</p>
  </div>'''

slide_06 = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="background: {WHITE}; overflow:hidden;">
  <!-- Header bar -->
  <div style="position:absolute; top:0; left:0; right:0; height:60px; background:{C1}; z-index:2;"></div>
  <p style="position:absolute; top:14px; left:60px; font-size:22px; font-weight:700; color:{WHITE}; z-index:10;">Clinical Presentations</p>

  {pres_html}

  <!-- Note -->
  <div style="position:absolute; bottom:50px; left:60px; right:60px; z-index:5;">
    <div style="background:{LIGHT_BG}; padding:10px 16px; border-radius:6px; border-left:4px solid {C3};">
      <p style="font-size:13px; color:{C1};">
        <span style="font-weight:700;">Important:</span> 2/3 of gallstones are asymptomatic (discovered incidentally). Yearly risk of developing biliary pain is 14%.
      </p>
    </div>
  </div>

  {page_badge(6)}
</div>
</body>
</html>'''
write_slide(6, slide_06)


# ============================================================
# SLIDE 07 - Investigations
# ============================================================
slide_07 = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="background: {LIGHT_BG}; overflow:hidden;">
  <!-- Header bar -->
  <div style="position:absolute; top:0; left:0; right:0; height:60px; background:{C1}; z-index:2;"></div>
  <p style="position:absolute; top:14px; left:60px; font-size:22px; font-weight:700; color:{WHITE}; z-index:10;">Investigations of GB Stones</p>

  <!-- Investigation cards -->
  <!-- Row 1 -->
  <div style="position:absolute; top:76px; left:40px; width:270px; background:{WHITE}; border-radius:8px; padding:14px; border-top:4px solid {C2}; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:6px;">Ultrasonography</p>
    <p style="font-size:12px; color:{C2}; font-weight:600; margin-bottom:6px;">DEFINITIVE INVESTIGATION</p>
    <p style="font-size:12px; color:#555; line-height:1.5;">
      Visualizes radio-lucent &amp; radio-opaque stones, intrahepatic biliary dilatation, hepatic &amp; extrahepatic lesions
    </p>
    <div style="margin-top:8px; padding:4px 10px; background:{C2}; border-radius:4px; display:inline-block;">
      <span style="font-size:11px; color:{WHITE}; font-weight:600;">95% sensitivity &amp; specificity</span>
    </div>
  </div>

  <div style="position:absolute; top:76px; left:330px; width:270px; background:{WHITE}; border-radius:8px; padding:14px; border-top:4px solid {C3}; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:6px;">Oral Cholecystogram</p>
    <p style="font-size:12px; color:#555; line-height:1.5;">
      Visualizes both radio-lucent and radio-opaque stones as multiple filling defects in contrast media
    </p>
  </div>

  <div style="position:absolute; top:76px; right:40px; width:270px; background:{WHITE}; border-radius:8px; padding:14px; border-top:4px solid {C4}; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:6px;">Plain X-ray</p>
    <p style="font-size:12px; color:#555; line-height:1.5;">
      Only 10% of gallstones are radio-opaque. Limited diagnostic value.
    </p>
  </div>

  <!-- Row 2 -->
  <div style="position:absolute; top:250px; left:40px; width:270px; background:{WHITE}; border-radius:8px; padding:14px; border-top:4px solid {C5}; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:6px;">MRCP</p>
    <p style="font-size:12px; color:#555; line-height:1.5;">
      Imaging of biliary tree with <span style="font-weight:700;">90% sensitivity &amp; specificity</span> compared to ERCP
    </p>
  </div>

  <div style="position:absolute; top:250px; left:330px; width:270px; background:{WHITE}; border-radius:8px; padding:14px; border-top:4px solid {C1}; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:6px;">ERCP</p>
    <p style="font-size:12px; color:#555; line-height:1.5;">
      Diagnosis of stones &amp; obstructive lesions in CBD and pancreatic duct. Also therapeutic.
    </p>
  </div>

  <div style="position:absolute; top:250px; right:40px; width:270px; background:{WHITE}; border-radius:8px; padding:14px; border-top:4px solid {C2}; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:6px;">Multislice CT Abdomen</p>
    <p style="font-size:12px; color:#555; line-height:1.5;">
      Cross-sectional imaging for comprehensive evaluation of biliary system and complications
    </p>
  </div>

  {page_badge(7)}
</div>
</body>
</html>'''
write_slide(7, slide_07)


# ============================================================
# SLIDE 08 - Management
# ============================================================
slide_08 = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="background: {WHITE}; overflow:hidden;">
  <!-- Header bar -->
  <div style="position:absolute; top:0; left:0; right:0; height:60px; background:{C1}; z-index:2;"></div>
  <p style="position:absolute; top:14px; left:60px; font-size:22px; font-weight:700; color:{WHITE}; z-index:10;">Management of Gallstone Disease</p>

  <!-- Left: Asymptomatic -->
  <div style="position:absolute; top:80px; left:40px; width:430px; z-index:5;">
    <svg width="430" height="48" viewBox="0 0 430 48" aria-hidden="true">
      <rect x="0" y="0" width="430" height="48" rx="6" fill="{C2}"/>
      <text x="20" y="32" fill="{WHITE}" font-family="Times New Roman, serif" font-size="17" font-weight="700">Asymptomatic Gallstones</text>
    </svg>
    <div style="background:{LIGHT_BG}; padding:16px; border-radius:0 0 8px 8px; margin-top:-1px;">
      <div style="display:flex; align-items:flex-start; margin-bottom:10px;">
        <div style="width:8px; height:8px; background:{C2}; border-radius:50%; margin-top:6px; margin-right:10px; flex-shrink:0;"></div>
        <p style="font-size:13px; color:{C1}; line-height:1.6;">2/3 of gallstones are asymptomatic (discovered incidentally by ultrasonography)</p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:10px;">
        <div style="width:8px; height:8px; background:{C3}; border-radius:50%; margin-top:6px; margin-right:10px; flex-shrink:0;"></div>
        <p style="font-size:13px; color:{C1}; line-height:1.6;">Yearly risk of developing biliary pain is <span style="font-weight:700;">14%</span></p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:10px;">
        <div style="width:8px; height:8px; background:{C4}; border-radius:50%; margin-top:6px; margin-right:10px; flex-shrink:0;"></div>
        <p style="font-size:13px; color:{C1}; line-height:1.6;">Patients seldom develop complications</p>
      </div>
      <div style="display:flex; align-items:flex-start;">
        <div style="width:8px; height:8px; background:{C5}; border-radius:50%; margin-top:6px; margin-right:10px; flex-shrink:0;"></div>
        <p style="font-size:13px; color:{C1}; line-height:1.6;">GB cancer risk &lt; 0.01% — less than cholecystectomy mortality</p>
      </div>
    </div>
  </div>

  <!-- Right: Symptomatic -->
  <div style="position:absolute; top:80px; right:40px; width:430px; z-index:5;">
    <svg width="430" height="48" viewBox="0 0 430 48" aria-hidden="true">
      <rect x="0" y="0" width="430" height="48" rx="6" fill="{C5}"/>
      <text x="20" y="32" fill="{WHITE}" font-family="Times New Roman, serif" font-size="17" font-weight="700">Symptomatic Gallstones</text>
    </svg>
    <div style="background:{LIGHT_BG}; padding:16px; border-radius:0 0 8px 8px; margin-top:-1px;">
      <div style="display:flex; align-items:flex-start; margin-bottom:10px;">
        <div style="width:8px; height:8px; background:{C5}; border-radius:50%; margin-top:6px; margin-right:10px; flex-shrink:0;"></div>
        <p style="font-size:13px; color:{C1}; line-height:1.6;">Annual complication rate: <span style="font-weight:700;">12%</span></p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:10px;">
        <div style="width:8px; height:8px; background:{C5}; border-radius:50%; margin-top:6px; margin-right:10px; flex-shrink:0;"></div>
        <p style="font-size:13px; color:{C1}; line-height:1.6;">50% chance of further biliary colic episode</p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:10px;">
        <div style="width:8px; height:8px; background:{C4}; border-radius:50%; margin-top:6px; margin-right:10px; flex-shrink:0;"></div>
        <p style="font-size:13px; color:{C1}; line-height:1.6;"><span style="font-weight:700;">Treatment should be offered</span></p>
      </div>
      <div style="display:flex; align-items:flex-start;">
        <div style="width:8px; height:8px; background:{C3}; border-radius:50%; margin-top:6px; margin-right:10px; flex-shrink:0;"></div>
        <p style="font-size:13px; color:{C1}; line-height:1.6;"><span style="font-weight:700;">Cholecystectomy</span> = optimal management (removes stones + GB)</p>
      </div>
    </div>
  </div>

  <!-- Bottom highlight -->
  <div style="position:absolute; bottom:40px; left:40px; right:40px; z-index:5;">
    <div style="background:{C1}; padding:12px 20px; border-radius:8px;">
      <p style="font-size:15px; color:{WHITE}; text-align:center; font-weight:600;">
        Cholecystectomy = optimal management — removes both gallstones and gallbladder, preventing recurrent disease
      </p>
    </div>
  </div>

  {page_badge(8)}
</div>
</body>
</html>'''
write_slide(8, slide_08)


# ============================================================
# SLIDE 09 - Chronic Calcular Cholecystitis
# ============================================================
slide_09 = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="background: {WHITE}; overflow:hidden;">
  <!-- Header bar -->
  <div style="position:absolute; top:0; left:0; right:0; height:60px; background:{C1}; z-index:2;"></div>
  <p style="position:absolute; top:14px; left:60px; font-size:22px; font-weight:700; color:{WHITE}; z-index:10;">Chronic Calcular Cholecystitis</p>

  <!-- Left: Clinical Picture -->
  <div style="position:absolute; top:80px; left:40px; width:430px; z-index:5;">
    <p style="font-size:18px; font-weight:700; color:{C1}; margin-bottom:12px;">Clinical Picture</p>

    <div style="background:{LIGHT_BG}; border-left:4px solid {C2}; padding:10px 14px; margin-bottom:8px; border-radius:0 6px 6px 0;">
      <p style="font-size:14px; font-weight:600; color:{C2};">1. Biliary Colic</p>
      <p style="font-size:12px; color:{C1}; line-height:1.5;">
        Starts in epigastrium or RUQ, radiates to interscapular region. Persists 15 min – 24 hours. Caused by GB distension from obstruction or stone passage through cystic duct.
      </p>
    </div>

    <div style="background:{LIGHT_BG}; border-left:4px solid {C3}; padding:10px 14px; margin-bottom:8px; border-radius:0 6px 6px 0;">
      <p style="font-size:14px; font-weight:600; color:{C3};">2. Local Tenderness</p>
      <p style="font-size:12px; color:{C1}; line-height:1.5;">
        <span style="font-weight:700;">Positive Murphy's sign</span> — tenderness on palpation of RUQ during inspiration
      </p>
    </div>

    <div style="background:{LIGHT_BG}; border-left:4px solid {C4}; padding:10px 14px; margin-bottom:8px; border-radius:0 6px 6px 0;">
      <p style="font-size:14px; font-weight:600; color:{C4};">3. Nausea or Vomiting</p>
    </div>

    <div style="background:{LIGHT_BG}; border-left:4px solid {C5}; padding:10px 14px; border-radius:0 6px 6px 0;">
      <p style="font-size:14px; font-weight:600; color:{C5};">4. Early Satiety &amp; Fat Intolerance</p>
    </div>
  </div>

  <!-- Right: Investigation & Treatment -->
  <div style="position:absolute; top:80px; right:40px; width:430px; z-index:5;">
    <p style="font-size:18px; font-weight:700; color:{C1}; margin-bottom:12px;">Investigation</p>

    <div style="background:{C2}; padding:12px 16px; border-radius:8px; margin-bottom:20px;">
      <p style="font-size:14px; color:{WHITE}; font-weight:600;">
        Ultrasonography = definitive investigation
      </p>
      <p style="font-size:13px; color:rgba(255,255,255,0.85);">
        95% sensitivity and specificity
      </p>
    </div>

    <p style="font-size:18px; font-weight:700; color:{C1}; margin-bottom:12px;">Treatment</p>

    <div style="display:flex; align-items:flex-start; margin-bottom:8px;">
      <div style="min-width:28px; height:28px; background:{C3}; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:10px;">
        <span style="font-size:12px; font-weight:700; color:{WHITE};">A</span>
      </div>
      <p style="font-size:13px; color:{C1}; line-height:1.6;">
        Most episodes managed at home with <span style="font-weight:700;">analgesics &amp; antiemetics</span>
      </p>
    </div>

    <div style="display:flex; align-items:flex-start; margin-bottom:8px;">
      <div style="min-width:28px; height:28px; background:{C4}; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:10px;">
        <span style="font-size:12px; font-weight:700; color:{WHITE};">B</span>
      </div>
      <p style="font-size:13px; color:{C1}; line-height:1.6;">
        Pain &gt; 24 hrs or fever → suggests acute cholecystitis → <span style="font-weight:700;">hospital admission</span>
      </p>
    </div>

    <div style="display:flex; align-items:flex-start;">
      <div style="min-width:28px; height:28px; background:{C5}; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:10px;">
        <span style="font-size:12px; font-weight:700; color:{WHITE};">C</span>
      </div>
      <p style="font-size:13px; color:{C1}; line-height:1.6;">
        <span style="font-weight:700;">Cholecystectomy</span> — definitive treatment
      </p>
    </div>
  </div>

  {page_badge(9)}
</div>
</body>
</html>'''
write_slide(9, slide_09)


# ============================================================
# SLIDE 10 - Acute Cholecystitis
# ============================================================
slide_10 = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="background: {LIGHT_BG}; overflow:hidden;">
  <!-- Header bar -->
  <div style="position:absolute; top:0; left:0; right:0; height:60px; background:{C5}; z-index:2;"></div>
  <p style="position:absolute; top:14px; left:60px; font-size:22px; font-weight:700; color:{WHITE}; z-index:10;">Acute Cholecystitis</p>

  <!-- Mechanism banner -->
  <div style="position:absolute; top:72px; left:60px; right:60px; background:{WHITE}; padding:10px 20px; border-radius:8px; border-left:4px solid {C5}; z-index:5;">
    <p style="font-size:14px; color:{C1}; line-height:1.5;">
      Initially a <span style="font-weight:700; color:{C5};">chemical inflammation</span> followed by <span style="font-weight:700; color:{C5};">secondary bacterial infection</span>. Occurs when obstruction of the cystic duct persists.
    </p>
  </div>

  <!-- Left: Clinical + Investigations -->
  <div style="position:absolute; top:120px; left:40px; width:430px; z-index:5;">
    <p style="font-size:18px; font-weight:700; color:{C1}; margin-bottom:10px;">Clinical Picture</p>

    <div style="background:{WHITE}; padding:12px 14px; border-radius:8px; margin-bottom:10px;">
      <div style="display:flex; align-items:center; margin-bottom:6px;">
        <div style="width:8px; height:8px; background:{C4}; border-radius:50%; margin-right:10px;"></div>
        <p style="font-size:13px; color:{C1};">Mild fever, nausea, vomiting</p>
      </div>
      <div style="display:flex; align-items:center; margin-bottom:6px;">
        <div style="width:8px; height:8px; background:{C5}; border-radius:50%; margin-right:10px;"></div>
        <p style="font-size:13px; color:{C1};">Acute RUQ pain → radiates to <span style="font-weight:700;">right shoulder</span></p>
      </div>
      <div style="display:flex; align-items:center;">
        <div style="width:8px; height:8px; background:{C2}; border-radius:50%; margin-right:10px;"></div>
        <p style="font-size:13px; color:{C1};">Localized tenderness in RUQ</p>
      </div>
    </div>

    <p style="font-size:18px; font-weight:700; color:{C1}; margin-bottom:10px;">Investigations</p>
    <div style="background:{WHITE}; padding:12px 14px; border-radius:8px;">
      <p style="font-size:13px; color:{C1}; margin-bottom:4px;">
        <span style="font-weight:600;">USG:</span> Tender, thick-walled, edematous GB with adjacent fluid
      </p>
      <p style="font-size:13px; color:{C1}; margin-bottom:4px;">
        <span style="font-weight:600;">LFTs:</span> Often mildly abnormal
      </p>
      <p style="font-size:13px; color:{C1};">
        <span style="font-weight:600;">CBC:</span> Leucocytosis
      </p>
    </div>
  </div>

  <!-- Right: Complications + Management -->
  <div style="position:absolute; top:120px; right:40px; width:430px; z-index:5;">
    <p style="font-size:18px; font-weight:700; color:{C5}; margin-bottom:10px;">Complications</p>

    <div style="display:flex; gap:8px; margin-bottom:16px;">
      <div style="flex:1; background:{C5}; padding:10px; border-radius:8px; text-align:center;">
        <p style="font-size:13px; color:{WHITE}; font-weight:600;">Empyema</p>
        <p style="font-size:11px; color:rgba(255,255,255,0.8);">Mucocele</p>
      </div>
      <div style="flex:1; background:{C4}; padding:10px; border-radius:8px; text-align:center;">
        <p style="font-size:13px; color:{WHITE}; font-weight:600;">Gangrene</p>
      </div>
      <div style="flex:1; background:{C1}; padding:10px; border-radius:8px; text-align:center;">
        <p style="font-size:13px; color:{WHITE}; font-weight:600;">Fistula</p>
      </div>
      <div style="flex:1; background:{C5}; padding:10px; border-radius:8px; text-align:center;">
        <p style="font-size:13px; color:{WHITE}; font-weight:600;">Perforation</p>
      </div>
    </div>

    <p style="font-size:18px; font-weight:700; color:{C1}; margin-bottom:10px;">Management</p>

    <div style="background:{WHITE}; padding:12px 14px; border-radius:8px; margin-bottom:8px;">
      <div style="display:flex; align-items:center; margin-bottom:6px;">
        <div style="min-width:24px; height:24px; background:{C2}; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:10px;">
          <span style="font-size:11px; color:{WHITE}; font-weight:700;">1</span>
        </div>
        <p style="font-size:13px; color:{C1};">NSAID or opioid analgesic</p>
      </div>
      <div style="display:flex; align-items:center; margin-bottom:6px;">
        <div style="min-width:24px; height:24px; background:{C2}; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:10px;">
          <span style="font-size:11px; color:{WHITE}; font-weight:700;">2</span>
        </div>
        <p style="font-size:13px; color:{C1};">Broad spectrum parenteral antibiotic</p>
      </div>
      <div style="display:flex; align-items:center; margin-bottom:6px;">
        <div style="min-width:24px; height:24px; background:{C2}; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:10px;">
          <span style="font-size:11px; color:{WHITE}; font-weight:700;">3</span>
        </div>
        <p style="font-size:13px; color:{C1};">Monitor: tachycardia, fever, tenderness</p>
      </div>
      <div style="display:flex; align-items:center;">
        <div style="min-width:24px; height:24px; background:{C5}; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:10px;">
          <span style="font-size:11px; color:{WHITE}; font-weight:700;">4</span>
        </div>
        <p style="font-size:13px; color:{C1}; font-weight:600;">Cholecystectomy during same admission</p>
      </div>
    </div>
  </div>

  {page_badge(10)}
</div>
</body>
</html>'''
write_slide(10, slide_10)


# ============================================================
# SLIDE 11 - Acute Cholangitis
# ============================================================
slide_11 = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="background: {WHITE}; overflow:hidden;">
  <!-- Header bar -->
  <div style="position:absolute; top:0; left:0; right:0; height:60px; background:{C5}; z-index:2;"></div>
  <p style="position:absolute; top:14px; left:60px; font-size:22px; font-weight:700; color:{WHITE}; z-index:10;">Acute Cholangitis</p>

  <!-- Definition -->
  <div style="position:absolute; top:72px; left:60px; right:60px; background:{LIGHT_BG}; padding:10px 16px; border-radius:8px; z-index:5;">
    <p style="font-size:14px; color:{C1}; line-height:1.5;">
      When an <span style="font-weight:700;">obstructed CBD becomes contaminated with bacteria</span>, usually from the duodenum. This is a medical emergency.
    </p>
  </div>

  <!-- Charcot's Triad -->
  <div style="position:absolute; top:124px; left:40px; width:440px; z-index:5;">
    <p style="font-size:20px; font-weight:700; color:{C5}; margin-bottom:14px;">Charcot's Triad (Severe Cholangitis)</p>

    <!-- Three cards for triad -->
    <div style="display:flex; gap:10px; margin-bottom:14px;">
      <div style="flex:1; background:{C5}; padding:14px; border-radius:8px; text-align:center;">
        <div style="width:48px; height:48px; background:rgba(255,255,255,0.2); border-radius:50%; margin:0 auto 8px; display:flex; align-items:center; justify-content:center;">
          <span style="font-size:24px;">1</span>
        </div>
        <p style="font-size:15px; font-weight:700; color:{WHITE};">Pain</p>
        <p style="font-size:12px; color:rgba(255,255,255,0.85);">Right upper quadrant</p>
      </div>
      <div style="flex:1; background:{C4}; padding:14px; border-radius:8px; text-align:center;">
        <div style="width:48px; height:48px; background:rgba(255,255,255,0.2); border-radius:50%; margin:0 auto 8px; display:flex; align-items:center; justify-content:center;">
          <span style="font-size:24px;">2</span>
        </div>
        <p style="font-size:15px; font-weight:700; color:{WHITE};">Jaundice</p>
        <p style="font-size:12px; color:rgba(255,255,255,0.85);">Obstructive</p>
      </div>
      <div style="flex:1; background:{C3}; padding:14px; border-radius:8px; text-align:center;">
        <div style="width:48px; height:48px; background:rgba(0,0,0,0.15); border-radius:50%; margin:0 auto 8px; display:flex; align-items:center; justify-content:center;">
          <span style="font-size:24px;">3</span>
        </div>
        <p style="font-size:15px; font-weight:700; color:{C1};">Fever</p>
        <p style="font-size:12px; color:{C1};">High swinging with rigors &amp; chills</p>
      </div>
    </div>
  </div>

  <!-- Right: Treatment -->
  <div style="position:absolute; top:124px; right:40px; width:400px; z-index:5;">
    <p style="font-size:20px; font-weight:700; color:{C5}; margin-bottom:14px;">Urgent Treatment Required</p>

    <div style="background:{LIGHT_BG}; border-radius:8px; padding:14px; margin-bottom:10px;">
      <p style="font-size:13px; color:{C1}; margin-bottom:8px;">
        <span style="font-weight:700;">1. Broad spectrum antibiotics</span>
      </p>
      <p style="font-size:13px; color:{C1}; margin-bottom:8px;">
        <span style="font-weight:700;">2. Early decompression:</span>
      </p>
      <div style="padding-left:16px;">
        <p style="font-size:12px; color:{C1}; margin-bottom:4px;">• Endoscopic (ERCP)</p>
        <p style="font-size:12px; color:{C1}; margin-bottom:4px;">• Radiological stenting (PTC)</p>
        <p style="font-size:12px; color:{C1};">• Surgical drainage if stenting not available</p>
      </div>
    </div>

    <div style="background:{C5}; border-radius:8px; padding:12px 16px; margin-bottom:10px;">
      <p style="font-size:13px; color:{WHITE}; font-weight:600;">
        ⚠ Delay may result in septicemia or liver abscesses → HIGH MORTALITY
      </p>
    </div>

    <div style="background:{LIGHT_BG}; border-radius:8px; padding:10px 16px; border-left:4px solid {C4};">
      <p style="font-size:12px; color:{C1}; line-height:1.5;">
        <span style="font-weight:600;">Chronic complications:</span> Secondary sclerosing cholangitis &amp; secondary biliary cirrhosis
      </p>
    </div>
  </div>

  {page_badge(11)}
</div>
</body>
</html>'''
write_slide(11, slide_11)


# ============================================================
# SLIDE 12 - PTC
# ============================================================
slide_12 = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="background: {LIGHT_BG}; overflow:hidden;">
  <!-- Header bar -->
  <div style="position:absolute; top:0; left:0; right:0; height:60px; background:{C1}; z-index:2;"></div>
  <p style="position:absolute; top:14px; left:60px; font-size:22px; font-weight:700; color:{WHITE}; z-index:10;">Percutaneous Transhepatic Cholangiography (PTC)</p>

  <!-- Left: Diagnostic -->
  <div style="position:absolute; top:80px; left:40px; width:430px; z-index:5;">
    <svg width="430" height="44" viewBox="0 0 430 44" aria-hidden="true">
      <rect x="0" y="0" width="430" height="44" rx="6" fill="{C2}"/>
      <text x="20" y="30" fill="{WHITE}" font-family="Times New Roman, serif" font-size="16" font-weight="700">Diagnostic PTC</text>
    </svg>
    <div style="background:{WHITE}; padding:14px; border-radius:0 0 8px 8px; margin-top:-1px;">
      <p style="font-size:13px; color:{C1}; line-height:1.6; margin-bottom:8px;">
        Visualizes anatomy of biliary tract in patients with <span style="font-weight:700;">biliary duct dilation on USG</span>
      </p>
      <p style="font-size:13px; color:{C1}; line-height:1.6; margin-bottom:8px;">
        Used when:
      </p>
      <ul style="margin:0; padding-left:18px;">
        <li style="font-size:12px; color:{C1}; margin-bottom:3px;">Not candidates for ERCP (e.g. gastrojejunostomy)</li>
        <li style="font-size:12px; color:{C1}; margin-bottom:3px;">ERCP unsuccessful</li>
        <li style="font-size:12px; color:{C1}; margin-bottom:3px;">Evaluation of ERCP complications</li>
        <li style="font-size:12px; color:{C1};">Delineating bile leaks</li>
      </ul>
    </div>
  </div>

  <!-- Right: Therapeutic -->
  <div style="position:absolute; top:80px; right:40px; width:430px; z-index:5;">
    <svg width="430" height="44" viewBox="0 0 430 44" aria-hidden="true">
      <rect x="0" y="0" width="430" height="44" rx="6" fill="{C4}"/>
      <text x="20" y="30" fill="{WHITE}" font-family="Times New Roman, serif" font-size="16" font-weight="700">Therapeutic PTC</text>
    </svg>
    <div style="background:{WHITE}; padding:14px; border-radius:0 0 8px 8px; margin-top:-1px;">
      <p style="font-size:13px; color:{C1}; line-height:1.6; margin-bottom:8px;">
        Also permits:
      </p>
      <ul style="margin:0; padding-left:18px;">
        <li style="font-size:12px; color:{C1}; margin-bottom:4px;">Drainage of infected bile in cholangitis</li>
        <li style="font-size:12px; color:{C1}; margin-bottom:4px;">Dilation of benign biliary strictures</li>
        <li style="font-size:12px; color:{C1};">Placement of stent across malignant stricture</li>
      </ul>
    </div>
  </div>

  <!-- Bottom: Drainage types + Contraindications -->
  <div style="position:absolute; bottom:40px; left:40px; width:460px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:10px;">Types of Drainage</p>
    <div style="display:flex; gap:8px;">
      <div style="flex:1; background:{WHITE}; padding:10px; border-radius:8px; border-top:3px solid {C2}; text-align:center;">
        <p style="font-size:12px; font-weight:600; color:{C1};">External</p>
        <p style="font-size:11px; color:#666;">Big tail (3 weeks)</p>
      </div>
      <div style="flex:1; background:{WHITE}; padding:10px; border-radius:8px; border-top:3px solid {C3}; text-align:center;">
        <p style="font-size:12px; font-weight:600; color:{C1};">Internal-External</p>
        <p style="font-size:11px; color:#666;">BP &lt;15 mmHg</p>
      </div>
      <div style="flex:1; background:{WHITE}; padding:10px; border-radius:8px; border-top:3px solid {C4}; text-align:center;">
        <p style="font-size:12px; font-weight:600; color:{C1};">GB to Outside</p>
        <p style="font-size:11px; color:#666;">Direct drainage</p>
      </div>
    </div>
  </div>

  <div style="position:absolute; bottom:40px; right:40px; width:420px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C5}; margin-bottom:10px;">Contraindications</p>
    <div style="background:{WHITE}; padding:10px 16px; border-radius:8px; border-left:4px solid {C5};">
      <p style="font-size:13px; color:{C1}; margin-bottom:4px;">• <span style="font-weight:600;">Bleeding diathesis</span></p>
      <p style="font-size:13px; color:{C1};">• <span style="font-weight:600;">Gross ascites</span></p>
    </div>
  </div>

  {page_badge(12)}
</div>
</body>
</html>'''
write_slide(12, slide_12)


# ============================================================
# SLIDE 13 - Summary / Key Takeaways
# ============================================================
slide_13 = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="background: {C1}; overflow:hidden;">
  <!-- Decorative SVGs -->
  <svg style="position:absolute; top:0; left:0; width:960px; height:540px; z-index:0;" viewBox="0 0 960 540" aria-hidden="true">
    <circle cx="800" cy="-100" r="300" fill="{C2}" opacity="0.08"/>
    <circle cx="100" cy="550" r="200" fill="{C3}" opacity="0.06"/>
  </svg>

  <!-- Title -->
  <p style="position:absolute; top:30px; left:60px; font-size:36px; font-weight:700; color:{WHITE}; z-index:10;">Key Takeaways</p>
  <div style="position:absolute; top:78px; left:60px; width:120px; height:3px; background:{C3}; border-radius:1.5px; z-index:1;"></div>

  <!-- Takeaway cards -->
  <div style="position:absolute; top:100px; left:40px; width:430px; z-index:5;">
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:12px 16px; margin-bottom:8px; border-left:4px solid {C2};">
      <p style="font-size:14px; color:{WHITE}; line-height:1.5;">
        <span style="font-weight:700;">Gallstones</span> are the most common abdominal reason for hospital admission
      </p>
    </div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:12px 16px; margin-bottom:8px; border-left:4px solid {C3};">
      <p style="font-size:14px; color:{WHITE}; line-height:1.5;">
        <span style="font-weight:700;">3 types:</span> Cholesterol (80%), Black pigment, Brown pigment (&lt;5%)
      </p>
    </div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:12px 16px; margin-bottom:8px; border-left:4px solid {C4};">
      <p style="font-size:14px; color:{WHITE}; line-height:1.5;">
        <span style="font-weight:700;">USG</span> is the definitive investigation (95% sensitivity &amp; specificity)
      </p>
    </div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:12px 16px; border-left:4px solid {C5};">
      <p style="font-size:14px; color:{WHITE}; line-height:1.5;">
        <span style="font-weight:700;">Cholecystectomy</span> = optimal management for symptomatic gallstones
      </p>
    </div>
  </div>

  <div style="position:absolute; top:100px; right:40px; width:430px; z-index:5;">
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:12px 16px; margin-bottom:8px; border-left:4px solid {C2};">
      <p style="font-size:14px; color:{WHITE}; line-height:1.5;">
        <span style="font-weight:700;">Acute cholangitis</span> = Charcot's triad (pain + jaundice + fever) → urgent treatment
      </p>
    </div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:12px 16px; margin-bottom:8px; border-left:4px solid {C3};">
      <p style="font-size:14px; color:{WHITE}; line-height:1.5;">
        <span style="font-weight:700;">Decompression</span> via ERCP, PTC, or surgical drainage is life-saving
      </p>
    </div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:12px 16px; margin-bottom:8px; border-left:4px solid {C4};">
      <p style="font-size:14px; color:{WHITE}; line-height:1.5;">
        <span style="font-weight:700;">PTC:</span> Diagnostic &amp; therapeutic for biliary drainage
      </p>
    </div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:12px 16px; border-left:4px solid {C5};">
      <p style="font-size:14px; color:{WHITE}; line-height:1.5;">
        <span style="font-weight:700;">Delay in cholangitis</span> → septicemia, liver abscesses, high mortality
      </p>
    </div>
  </div>

  <!-- Bottom bar -->
  <div style="position:absolute; bottom:0; left:0; right:0; height:50px; background:rgba(0,0,0,0.25); z-index:5;"></div>
  <p style="position:absolute; bottom:14px; left:60px; font-size:14px; color:{C3}; z-index:10; font-style:italic;">
    Biliary System — Gallstones: Summary
  </p>

  {page_badge(13)}
</div>
</body>
</html>'''
write_slide(13, slide_13)


print("\n✅ All 13 slides generated successfully!")
print(f"Output directory: {SLIDES_DIR}")
