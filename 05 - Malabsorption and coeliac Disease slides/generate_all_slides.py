#!/usr/bin/env python3
"""
Generate all 15 HTML slides for: 05 - Malabsorption and Coeliac Disease
Palette 10: #264653 #2a9d8f #e9c46a #f4a261 #e76f51
Font: Times New Roman | Dimensions: 960x540
"""

import os

# Palette colors
C1 = "#264653"
C2 = "#2a9d8f"
C3 = "#e9c46a"
C4 = "#f4a261"
C5 = "#e76f51"
WHITE = "#ffffff"
LIGHT_BG = "#f0f7f7"

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SLIDES_DIR = os.path.join(OUT_DIR, "slides")
NUM_SLIDES = 15

APPENDIX_A = """<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
html, body { margin:0; padding:0; width:100%; height:100%; overflow:hidden; display:flex; justify-content:center; align-items:center; background:#000; }
.slide-content { width:960px; height:540px; position:relative; transform-origin:center center; }
</style>
<script>
function scaleSlide(){const s=document.querySelector('.slide-content');if(!s)return;const sx=window.innerWidth/960;const sy=window.innerHeight/540;const sc=Math.min(sx,sy);s.style.width='960px';s.style.height='540px';s.style.transform=`scale(${sc})`;s.style.transformOrigin='center center';s.style.flexShrink='0';}
window.addEventListener('load',scaleSlide);window.addEventListener('resize',scaleSlide);
</script>"""


def page_badge(num):
    return f'''<svg style="position:absolute; right:32px; bottom:24px; z-index:50;" width="48" height="28" viewBox="0 0 48 28" aria-hidden="true">
  <rect x="0" y="0" width="48" height="28" rx="14" fill="{C1}" opacity="0.85"/>
  <text x="24" y="19" text-anchor="middle" fill="{WHITE}" font-family="Times New Roman, serif" font-size="14" font-weight="600">{num}</text>
</svg>'''


def write_slide(num, content):
    path = os.path.join(SLIDES_DIR, f"slide-{num:02d}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Written: slide-{num:02d}.html")


def header_bar(title, bg=C1):
    return f'''<div style="position:absolute; top:0; left:0; right:0; height:56px; background:{bg}; z-index:2;"></div>
  <p style="position:absolute; top:12px; left:50px; font-size:21px; font-weight:700; color:{WHITE}; z-index:10;">{title}</p>'''


# ============================================================
# SLIDE 01 - COVER
# ============================================================
slide_01 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{C1}; overflow:hidden;">
  <svg style="position:absolute; top:0; left:0; width:960px; height:540px; z-index:0;" viewBox="0 0 960 540" aria-hidden="true">
    <circle cx="800" cy="-80" r="320" fill="{C2}" opacity="0.12"/>
    <circle cx="850" cy="120" r="140" fill="{C3}" opacity="0.10"/>
    <rect x="-50" y="380" width="1100" height="220" fill="{C2}" opacity="0.08" transform="rotate(-8 480 490)"/>
    <rect x="0" y="0" width="8" height="540" fill="{C2}"/>
  </svg>
  <div style="position:absolute; top:130px; left:70px; width:80px; height:5px; background:{C3}; border-radius:2px; z-index:5;"></div>
  <p style="position:absolute; top:148px; left:70px; font-size:48px; font-weight:700; color:{WHITE}; z-index:10; line-height:1.15;">Malabsorption</p>
  <p style="position:absolute; top:212px; left:70px; font-size:42px; font-weight:700; color:{C3}; z-index:10; line-height:1.15;">Syndrome</p>
  <p style="position:absolute; top:280px; left:70px; font-size:24px; font-weight:600; color:{WHITE}; opacity:0.85; z-index:10;">&amp;</p>
  <p style="position:absolute; top:310px; left:70px; font-size:36px; font-weight:700; color:{C3}; z-index:10;">Coeliac Disease</p>
  <p style="position:absolute; top:365px; left:70px; font-size:18px; color:{WHITE}; opacity:0.75; z-index:10; max-width:500px; line-height:1.5;">
    Definition, Causes, Clinical Features, Investigations,<br>Diagnosis, Complications &amp; Treatment
  </p>
  <div style="position:absolute; bottom:0; left:0; right:0; height:52px; background:rgba(0,0,0,0.25); z-index:5;"></div>
  <p style="position:absolute; bottom:14px; left:70px; font-size:14px; color:{C3}; z-index:10; font-style:italic;">Gastro-enterology &amp; Internal Medicine</p>
  <svg style="position:absolute; right:60px; top:80px; z-index:2;" width="220" height="300" viewBox="0 0 220 300" aria-hidden="true">
    <ellipse cx="110" cy="120" rx="90" ry="60" fill="{C2}" opacity="0.2"/>
    <path d="M 60 120 Q 60 80 110 70 Q 160 80 160 120 Q 160 160 110 170 Q 60 160 60 120 Z" fill="{C2}" opacity="0.15"/>
    <path d="M 80 140 Q 80 180 90 220" stroke="{C3}" stroke-width="3" fill="none" opacity="0.4"/>
    <path d="M 110 140 Q 110 190 115 240" stroke="{C3}" stroke-width="3" fill="none" opacity="0.4"/>
    <path d="M 140 140 Q 140 180 135 220" stroke="{C3}" stroke-width="3" fill="none" opacity="0.4"/>
    <circle cx="90" cy="220" r="4" fill="{C5}" opacity="0.5"/>
    <circle cx="115" cy="240" r="3" fill="{C5}" opacity="0.4"/>
    <circle cx="135" cy="220" r="4" fill="{C5}" opacity="0.5"/>
  </svg>
</div></body></html>'''
write_slide(1, slide_01)


# ============================================================
# SLIDE 02 - TABLE OF CONTENTS
# ============================================================
toc_items = [
    ("01", "Malabsorption Syndrome", "Definition, causes & clinical picture"),
    ("02", "Causes of Malabsorption", "Small intestinal, pancreatic, mixed"),
    ("03", "Nutritional Manifestations", "Anemia, osteomalacia, vitamin deficiencies"),
    ("04", "Investigations", "Lab, anatomy, absorption tests"),
    ("05", "Coeliac Disease", "Definition & pathophysiology"),
    ("06", "Coeliac — Clinical Subtypes", "Typical, atypical, silent, latent"),
    ("07", "Coeliac — Diagnosis", "Antibodies, HLA, biopsy"),
    ("08", "Coeliac — Complications & Treatment", "Lymphoma, dermatitis, GFD"),
    ("09", "Coeliac — New Treatments", "Immunotherapy & research"),
    ("10", "Short Bowel & Radiation Enteritis", "Resection complications"),
    ("11", "Other Causes", "Parasitic, protein-losing, rare conditions"),
    ("12", "Small Intestine Tumors", "Adenocarcinoma, lymphoma, carcinoid"),
    ("13", "Summary", "Key takeaways"),
]

toc_html = ""
for i, (num, title, desc) in enumerate(toc_items):
    y = 72 + i * 35
    toc_html += f'''
  <div style="position:absolute; top:{y}px; left:70px; z-index:5;">
    <span style="display:inline-block; width:32px; font-size:14px; font-weight:700; color:{C2};">{num}</span>
    <span style="font-size:13px; font-weight:600; color:{C1};">{title}</span>
    <span style="font-size:11px; color:#666; margin-left:8px;">{desc}</span>
  </div>'''
    if i < len(toc_items) - 1:
        toc_html += f'\n  <div style="position:absolute; top:{y+26}px; left:102px; width:780px; height:1px; background:{C2}; opacity:0.15; z-index:1;"></div>'

slide_02 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{WHITE}; overflow:hidden;">
  <div style="position:absolute; top:0; left:0; width:50px; height:540px; background:{C1}; z-index:2;"></div>
  <div style="position:absolute; top:0; left:50px; width:4px; height:540px; background:{C2}; z-index:2;"></div>
  <p style="position:absolute; top:30px; left:72px; font-size:28px; font-weight:700; color:{C1}; z-index:10;">Table of Contents</p>
  <div style="position:absolute; top:64px; left:72px; width:90px; height:3px; background:{C2}; border-radius:1.5px; z-index:1;"></div>
  {toc_html}
  {page_badge(2)}
</div></body></html>'''
write_slide(2, slide_02)


# ============================================================
# SLIDE 03 - Malabsorption Definition & Causes
# ============================================================
slide_03 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{LIGHT_BG}; overflow:hidden;">
  {header_bar("Malabsorption Syndrome — Definition")}
  <div style="position:absolute; top:68px; left:50px; right:50px; background:{WHITE}; padding:12px 18px; border-radius:8px; border-left:4px solid {C2}; z-index:5;">
    <p style="font-size:14px; color:{C1}; line-height:1.6;">
      <span style="font-weight:700;">Definition:</span> The inability to absorb fat, protein, carbohydrates, vitamins, minerals or bile acids from the intestinal lumen into the bloodstream or lymphatics.
    </p>
  </div>
  <div style="position:absolute; top:130px; left:50px; width:420px; z-index:5;">
    <p style="font-size:17px; font-weight:700; color:{C1}; margin-bottom:10px;">Types of Malabsorption</p>
    <div style="display:flex; gap:8px; margin-bottom:12px;">
      <div style="flex:1; background:{C2}; padding:10px; border-radius:8px; text-align:center;">
        <p style="font-size:14px; font-weight:700; color:{WHITE};">Simple</p>
        <p style="font-size:11px; color:rgba(255,255,255,0.85);">Single component</p>
      </div>
      <div style="flex:1; background:{C4}; padding:10px; border-radius:8px; text-align:center;">
        <p style="font-size:14px; font-weight:700; color:{WHITE};">Complex</p>
        <p style="font-size:11px; color:rgba(255,255,255,0.85);">Multiple components</p>
      </div>
    </div>
    <p style="font-size:13px; color:{C1}; font-weight:600; margin-bottom:6px;">Simple may involve:</p>
    <ul style="margin:0; padding-left:18px; margin-bottom:10px;">
      <li style="font-size:12px; color:{C1}; margin-bottom:2px;">Carbohydrates, Fat, Protein</li>
      <li style="font-size:12px; color:{C1}; margin-bottom:2px;">Lactose, Xylose</li>
    </ul>
    <p style="font-size:13px; color:{C1}; font-weight:600; margin-bottom:6px;">Clinical Picture — Symptoms:</p>
    <ul style="margin:0; padding-left:18px;">
      <li style="font-size:12px; color:{C1}; margin-bottom:2px;">Diarrhea or steatorrhea</li>
      <li style="font-size:12px; color:{C1}; margin-bottom:2px;">Weight loss and edema</li>
      <li style="font-size:12px; color:{C1}; margin-bottom:2px;">Abdominal pain, distension</li>
      <li style="font-size:12px; color:{C1};">Symptoms of nutritional deficiencies</li>
    </ul>
  </div>
  <div style="position:absolute; top:130px; right:50px; width:400px; z-index:5;">
    <p style="font-size:17px; font-weight:700; color:{C1}; margin-bottom:10px;">Signs</p>
    <div style="background:{WHITE}; padding:12px 14px; border-radius:8px; margin-bottom:14px;">
      <ul style="margin:0; padding-left:18px;">
        <li style="font-size:12px; color:{C1}; margin-bottom:3px;">Distension or masses may be present</li>
        <li style="font-size:12px; color:{C1}; margin-bottom:3px;">Edema may be present</li>
        <li style="font-size:12px; color:{C1}; margin-bottom:3px;">Signs of nutritional deficiencies</li>
        <li style="font-size:12px; color:{C1};">Abdominal discomfort</li>
      </ul>
    </div>
    <p style="font-size:17px; font-weight:700; color:{C1}; margin-bottom:10px;">Key Investigations Overview</p>
    <div style="display:flex; gap:6px;">
      <div style="flex:1; background:{C2}; padding:8px; border-radius:6px; text-align:center;">
        <p style="font-size:11px; font-weight:600; color:{WHITE};">Lab Tests</p>
      </div>
      <div style="flex:1; background:{C3}; padding:8px; border-radius:6px; text-align:center;">
        <p style="font-size:11px; font-weight:600; color:{C1};">Anatomy</p>
      </div>
      <div style="flex:1; background:{C4}; padding:8px; border-radius:6px; text-align:center;">
        <p style="font-size:11px; font-weight:600; color:{WHITE};">Absorption</p>
      </div>
    </div>
  </div>
  {page_badge(3)}
</div></body></html>'''
write_slide(3, slide_03)


# ============================================================
# SLIDE 04 - Causes of Malabsorption (3 categories)
# ============================================================
slide_04 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{WHITE}; overflow:hidden;">
  {header_bar("Causes of Malabsorption")}
  <!-- Column A: Small Intestinal -->
  <div style="position:absolute; top:66px; left:30px; width:290px; z-index:5;">
    <svg width="290" height="36" viewBox="0 0 290 36" aria-hidden="true"><rect x="0" y="0" width="290" height="36" rx="6" fill="{C2}"/><text x="145" y="24" text-anchor="middle" fill="{WHITE}" font-family="Times New Roman, serif" font-size="13" font-weight="700">A) Small Intestinal Causes</text></svg>
    <div style="background:{LIGHT_BG}; padding:8px 10px; border-radius:0 0 6px 6px; margin-top:-1px;">
      <ul style="margin:0; padding-left:14px;">
        <li style="font-size:11px; color:{C1}; margin-bottom:2px;">Coeliac disease</li>
        <li style="font-size:11px; color:{C1}; margin-bottom:2px;">Tropical sprue</li>
        <li style="font-size:11px; color:{C1}; margin-bottom:2px;">Bacterial overgrowth</li>
        <li style="font-size:11px; color:{C1}; margin-bottom:2px;">Intestinal resection</li>
        <li style="font-size:11px; color:{C1}; margin-bottom:2px;">Intestinal lymphoma</li>
        <li style="font-size:11px; color:{C1}; margin-bottom:2px;">Lymphangiectasia</li>
        <li style="font-size:11px; color:{C1}; margin-bottom:2px;">Whipple's disease</li>
        <li style="font-size:11px; color:{C1}; margin-bottom:2px;">Radiation enteritis</li>
        <li style="font-size:11px; color:{C1}; margin-bottom:2px;">Parasitic infestation</li>
        <li style="font-size:11px; color:{C1}; margin-bottom:2px;">Intestinal ischemia</li>
        <li style="font-size:11px; color:{C1}; margin-bottom:2px;">Crohn's disease</li>
        <li style="font-size:11px; color:{C1}; margin-bottom:2px;">Ulcerative colitis</li>
        <li style="font-size:11px; color:{C1};">1° lactase deficiency</li>
      </ul>
    </div>
  </div>
  <!-- Column B: Pancreatic -->
  <div style="position:absolute; top:66px; left:340px; width:270px; z-index:5;">
    <svg width="270" height="36" viewBox="0 0 270 36" aria-hidden="true"><rect x="0" y="0" width="270" height="36" rx="6" fill="{C4}"/><text x="135" y="24" text-anchor="middle" fill="{WHITE}" font-family="Times New Roman, serif" font-size="13" font-weight="700">B) Pancreatic Causes</text></svg>
    <div style="background:{LIGHT_BG}; padding:8px 10px; border-radius:0 0 6px 6px; margin-top:-1px;">
      <ul style="margin:0; padding-left:14px;">
        <li style="font-size:11px; color:{C1}; margin-bottom:3px;">Chronic pancreatitis</li>
        <li style="font-size:11px; color:{C1}; margin-bottom:3px;">Pancreatic carcinoma</li>
        <li style="font-size:11px; color:{C1};">Glucagonoma, Gastrinoma, VIPoma</li>
      </ul>
    </div>
    <p style="font-size:12px; color:#888; margin-top:8px; padding:0 4px;">Pancreatic insufficiency leads to impaired fat digestion → steatorrhea</p>
  </div>
  <!-- Column C: Mixed -->
  <div style="position:absolute; top:66px; right:30px; width:290px; z-index:5;">
    <svg width="290" height="36" viewBox="0 0 290 36" aria-hidden="true"><rect x="0" y="0" width="290" height="36" rx="6" fill="{C5}"/><text x="145" y="24" text-anchor="middle" fill="{WHITE}" font-family="Times New Roman, serif" font-size="13" font-weight="700">C) Mixed Defects</text></svg>
    <div style="background:{LIGHT_BG}; padding:8px 10px; border-radius:0 0 6px 6px; margin-top:-1px;">
      <ul style="margin:0; padding-left:14px;">
        <li style="font-size:11px; color:{C1}; margin-bottom:3px;">Zollinger-Ellison syndrome</li>
        <li style="font-size:11px; color:{C1};">Post gastrectomy syndrome</li>
      </ul>
    </div>
  </div>
  {page_badge(4)}
</div></body></html>'''
write_slide(4, slide_04)


# ============================================================
# SLIDE 05 - Nutritional Manifestations
# ============================================================
slide_05 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{LIGHT_BG}; overflow:hidden;">
  {header_bar("Nutritional Manifestations of Malabsorption")}
  <div style="position:absolute; top:68px; left:40px; width:430px; z-index:5;">
    <div style="background:{WHITE}; border-left:4px solid {C5}; padding:10px 14px; margin-bottom:8px; border-radius:0 6px 6px 0;">
      <p style="font-size:13px; font-weight:700; color:{C5};">Anemia</p>
      <p style="font-size:12px; color:{C1}; line-height:1.5;">Due to blood loss or malabsorption of iron, B12 or folic acid</p>
    </div>
    <div style="background:{WHITE}; border-left:4px solid {C2}; padding:10px 14px; margin-bottom:8px; border-radius:0 6px 6px 0;">
      <p style="font-size:13px; font-weight:700; color:{C2};">Edema</p>
      <p style="font-size:12px; color:{C1}; line-height:1.5;">Due to hypoproteinemia from protein malabsorption or protein-losing enteropathy</p>
    </div>
    <div style="background:{WHITE}; border-left:4px solid {C3}; padding:10px 14px; margin-bottom:8px; border-radius:0 6px 6px 0;">
      <p style="font-size:13px; font-weight:700; color:{C1};">Cholesterol GB Stones</p>
      <p style="font-size:12px; color:{C1}; line-height:1.5;">Malabsorption of bile acids from terminal ileum → cholesterol supersaturated bile → stones</p>
    </div>
    <div style="background:{WHITE}; border-left:4px solid {C4}; padding:10px 14px; margin-bottom:8px; border-radius:0 6px 6px 0;">
      <p style="font-size:13px; font-weight:700; color:{C4};">Osteomalacia</p>
      <p style="font-size:12px; color:{C1}; line-height:1.5;">Due to malabsorption of Calcium and Vitamin D</p>
    </div>
    <div style="background:{WHITE}; border-left:4px solid {C1}; padding:10px 14px; border-radius:0 6px 6px 0;">
      <p style="font-size:13px; font-weight:700; color:{C1};">Vitamin A Deficiency</p>
      <p style="font-size:12px; color:{C1}; line-height:1.5;">Leads to night blindness</p>
    </div>
  </div>
  <div style="position:absolute; top:68px; right:40px; width:420px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:10px;">Extra-Intestinal Manifestations (IBD)</p>
    <div style="background:{WHITE}; padding:12px 14px; border-radius:8px; margin-bottom:10px;">
      <p style="font-size:13px; font-weight:600; color:{C2}; margin-bottom:4px;">Joint Complications (~20% of IBD patients)</p>
      <ul style="margin:0; padding-left:16px;">
        <li style="font-size:12px; color:{C1}; margin-bottom:2px;">Axial (central) arthritis</li>
        <li style="font-size:12px; color:{C1};">Peripheral arthritis</li>
      </ul>
    </div>
    <div style="background:{WHITE}; padding:12px 14px; border-radius:8px;">
      <p style="font-size:13px; font-weight:600; color:{C4}; margin-bottom:4px;">Ophthalmologic (3-4% of IBD)</p>
      <ul style="margin:0; padding-left:16px;">
        <li style="font-size:12px; color:{C1}; margin-bottom:2px;">Episcleritis — burning eyes, scleral injection</li>
        <li style="font-size:12px; color:{C1}; margin-bottom:2px;">Parallels disease course</li>
        <li style="font-size:12px; color:{C1};">Resolves with IBD treatment + topical steroids</li>
      </ul>
    </div>
  </div>
  {page_badge(5)}
</div></body></html>'''
write_slide(5, slide_05)


# ============================================================
# SLIDE 06 - Investigations - Laboratory
# ============================================================
slide_06 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{WHITE}; overflow:hidden;">
  {header_bar("Investigations — Laboratory")}
  <div style="position:absolute; top:68px; left:40px; width:440px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:8px;">CBC for Anemia Type</p>
    <div style="background:{LIGHT_BG}; padding:10px 14px; border-radius:8px; margin-bottom:10px;">
      <p style="font-size:12px; color:{C1}; margin-bottom:4px;"><span style="font-weight:700; color:{C5};">Low MCV:</span> Measure serum ferritin &amp; soluble transferrin receptor → differentiate iron deficiency from chronic disorder</p>
      <p style="font-size:12px; color:{C1}; margin-bottom:4px;"><span style="font-weight:700; color:{C4};">High MCV:</span> Measure serum B12, serum &amp; red cell folate</p>
      <p style="font-size:12px; color:{C1};"><span style="font-weight:700; color:{C2};">Normal MCV:</span> May indicate mixed deficiencies</p>
    </div>
    <div style="background:{WHITE}; border-left:3px solid {C2}; padding:8px 12px; margin-bottom:6px;">
      <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Red cell folate:</span> Good indicator of small bowel disease. Frequently low in coeliac &amp; Crohn's</p>
    </div>
    <div style="background:{WHITE}; border-left:3px solid {C3}; padding:8px 12px; margin-bottom:6px;">
      <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Howell-Jolly bodies:</span> May indicate splenic atrophy (associated with coeliac disease)</p>
    </div>
    <div style="background:{WHITE}; border-left:3px solid {C4}; padding:8px 12px;">
      <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Serum minerals &amp; vitamins</span> + immunological tests (anti-gliadin, endomysial Ab)</p>
    </div>
  </div>
  <div style="position:absolute; top:68px; right:40px; width:420px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:8px;">Key Serum Markers</p>
    <div style="background:{LIGHT_BG}; padding:10px 14px; border-radius:8px;">
      <div style="display:flex; align-items:flex-start; margin-bottom:8px;">
        <div style="min-width:8px; height:8px; background:{C2}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1}; line-height:1.5;"><span style="font-weight:600;">Serum albumin:</span> Indicates nutritional status &amp; intestinal protein loss</p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:8px;">
        <div style="min-width:8px; height:8px; background:{C4}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1}; line-height:1.5;"><span style="font-weight:600;">Low Ca²⁺ + raised ALP:</span> Suggests osteomalacia (Vit D deficiency)</p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:8px;">
        <div style="min-width:8px; height:8px; background:{C3}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1}; line-height:1.5;"><span style="font-weight:600;">HLA testing:</span> Useful in coeliac disease (DQ2/DQ8)</p>
      </div>
      <div style="display:flex; align-items:flex-start;">
        <div style="min-width:8px; height:8px; background:{C5}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1}; line-height:1.5;"><span style="font-weight:600;">Anti-gliadin &amp; endomysial Ab:</span> Specific for coeliac disease</p>
      </div>
    </div>
  </div>
  {page_badge(6)}
</div></body></html>'''
write_slide(6, slide_06)


# ============================================================
# SLIDE 07 - Investigations - Anatomy & Absorption Tests
# ============================================================
slide_07 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{LIGHT_BG}; overflow:hidden;">
  {header_bar("Investigations — Anatomy & Absorption Tests")}
  <div style="position:absolute; top:68px; left:40px; width:440px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:8px;">B) Small Bowel Anatomy</p>
    <div style="background:{WHITE}; padding:10px 14px; border-radius:8px; margin-bottom:8px;">
      <div style="display:flex; align-items:flex-start; margin-bottom:6px;">
        <div style="min-width:8px; height:8px; background:{C2}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Barium meal + follow-through:</span> Detects diverticula, strictures, Crohn's, gross dilatation</p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:6px;">
        <div style="min-width:8px; height:8px; background:{C3}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Capsule endoscopy &amp; enteroscopy</span></p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:6px;">
        <div style="min-width:8px; height:8px; background:{C4}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Enteroscopy + biopsy:</span> Assess microanatomy. Smear jejunal juice for Giardia</p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:6px;">
        <div style="min-width:8px; height:8px; background:{C5}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">CT scan:</span> Wall thickening, diverticula, abscesses</p>
      </div>
      <div style="display:flex; align-items:flex-start;">
        <div style="min-width:8px; height:8px; background:{C1}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">MRI enteroclysis:</span> No radiation, monitors small bowel changes</p>
      </div>
    </div>
  </div>
  <div style="position:absolute; top:68px; right:40px; width:420px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:8px;">C) Absorption Tests</p>
    <div style="background:{WHITE}; padding:10px 14px; border-radius:8px;">
      <div style="display:flex; align-items:flex-start; margin-bottom:6px;">
        <div style="min-width:8px; height:8px; background:{C2}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Stool fat (3 days):</span> Diet ~100g fat/day. Normal &lt;6g/day</p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:6px;">
        <div style="min-width:8px; height:8px; background:{C3}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">D-xylose test:</span> Absorbed from proximal intestine. Blood &amp; urine levels reflect absorption</p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:6px;">
        <div style="min-width:8px; height:8px; background:{C4}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Lactose tolerance:</span> 50g lactose → measure blood glucose → diagnose lactase deficiency</p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:6px;">
        <div style="min-width:8px; height:8px; background:{C5}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Protein-losing:</span> IV radiolabelled albumin → detect in stool</p>
      </div>
      <div style="display:flex; align-items:flex-start;">
        <div style="min-width:8px; height:8px; background:{C1}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">H₂ breath test:</span> Oral lactose/glucose → early bacterial metabolism → increased breath H₂</p>
      </div>
    </div>
  </div>
  {page_badge(7)}
</div></body></html>'''
write_slide(7, slide_07)


# ============================================================
# SLIDE 08 - Coeliac Disease Definition & Pathophysiology
# ============================================================
slide_08 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{WHITE}; overflow:hidden;">
  {header_bar("Coeliac Disease — Definition & Pathophysiology", C5)}
  <div style="position:absolute; top:68px; left:50px; right:50px; background:{LIGHT_BG}; padding:12px 18px; border-radius:8px; border-left:4px solid {C5}; z-index:5;">
    <p style="font-size:14px; color:{C1}; line-height:1.6;">
      <span style="font-weight:700;">Definition:</span> Inflammation of the mucosa of the upper small bowel that improves when gluten is withdrawn from the diet and relapses when gluten is reintroduced. Up to <span style="font-weight:700; color:{C5};">1%</span> of populations are affected, though most have clinically silent disease.
    </p>
  </div>
  <div style="position:absolute; top:130px; left:50px; width:430px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:10px;">Pathophysiology</p>
    <div style="background:{WHITE}; border:1px solid #e0e0e0; padding:10px 14px; border-radius:8px; margin-bottom:8px;">
      <p style="font-size:12px; color:{C1}; line-height:1.6;">
        <span style="font-weight:600;">1. Gliadin peptides</span> pass through enhanced paracellular permeability (compromised tight junctions)
      </p>
    </div>
    <svg width="30" height="20" viewBox="0 0 30 20" aria-hidden="true" style="display:block; margin:0 auto;"><line x1="15" y1="0" x2="15" y2="16" stroke="{C2}" stroke-width="2"/><polygon points="8,14 15,22 22,14" fill="{C2}"/></svg>
    <div style="background:{WHITE}; border:1px solid #e0e0e0; padding:10px 14px; border-radius:8px; margin-bottom:8px;">
      <p style="font-size:12px; color:{C1}; line-height:1.6;">
        <span style="font-weight:600;">2. Tissue transglutaminase</span> deamidates gliadin → increases immunogenicity → binds to APC → activates CD4+ T cells via HLA-DQ2/DQ8
      </p>
    </div>
    <svg width="30" height="20" viewBox="0 0 30 20" aria-hidden="true" style="display:block; margin:0 auto;"><line x1="15" y1="0" x2="15" y2="16" stroke="{C2}" stroke-width="2"/><polygon points="8,14 15,22 22,14" fill="{C2}"/></svg>
    <div style="background:{WHITE}; border:1px solid #e0e0e0; padding:10px 14px; border-radius:8px;">
      <p style="font-size:12px; color:{C1}; line-height:1.6;">
        <span style="font-weight:600;">3. T cells produce</span> IFN-γ + interact with B cells → endomysial &amp; tTG antibodies
      </p>
    </div>
  </div>
  <div style="position:absolute; top:130px; right:50px; width:390px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:10px;">Inflammatory Cascade</p>
    <div style="background:{LIGHT_BG}; padding:12px 14px; border-radius:8px;">
      <div style="display:flex; align-items:flex-start; margin-bottom:8px;">
        <div style="min-width:28px; height:28px; background:{C5}; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:10px;">
          <span style="font-size:11px; color:{WHITE}; font-weight:700;">4</span>
        </div>
        <p style="font-size:12px; color:{C1}; line-height:1.5;">Gliadin peptides → release <span style="font-weight:700;">IL-15</span> from enterocytes</p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:8px;">
        <div style="min-width:28px; height:28px; background:{C4}; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:10px;">
          <span style="font-size:11px; color:{WHITE}; font-weight:700;">5</span>
        </div>
        <p style="font-size:12px; color:{C1}; line-height:1.5;">Activates <span style="font-weight:700;">intraepithelial lymphocytes</span> (NK cell marker)</p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:8px;">
        <div style="min-width:28px; height:28px; background:{C3}; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:10px;">
          <span style="font-size:11px; color:{C1}; font-weight:700;">6</span>
        </div>
        <p style="font-size:12px; color:{C1}; line-height:1.5;">Releases <span style="font-weight:700;">metalloproteinases</span> &amp; other mediators</p>
      </div>
      <div style="display:flex; align-items:flex-start;">
        <div style="min-width:28px; height:28px; background:{C2}; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:10px;">
          <span style="font-size:11px; color:{WHITE}; font-weight:700;">7</span>
        </div>
        <p style="font-size:12px; color:{C1}; line-height:1.5;">→ Villous atrophy, crypt hyperplasia → <span style="font-weight:700; color:{C5};">Coeliac Disease</span></p>
      </div>
    </div>
    <div style="background:{C2}; padding:10px 14px; border-radius:8px; margin-top:10px;">
      <p style="font-size:12px; color:{WHITE}; font-weight:600; text-align:center;">Key: Resolves completely on gluten-free diet</p>
    </div>
  </div>
  {page_badge(8)}
</div></body></html>'''
write_slide(8, slide_08)


# ============================================================
# SLIDE 09 - Coeliac - 4 Clinical Subtypes
# ============================================================
subtypes = [
    ("Typical CD", C5, [
        "Presents 6-24 months (start eating)",
        "Impaired growth, abnormal stools",
        "Abdominal distension",
        "Muscle wasting, hypotonia",
        "Poor appetite, unhappy behavior",
    ]),
    ("Atypical CD", C4, [
        "Older children &amp; adults",
        "No overt malabsorption",
        "Recurrent abdominal pain",
        "Dental enamel defects",
        "Aphthous stomatitis",
    ]),
    ("Silent CD", C2, [
        "Family history / autoimmune disorders",
        "Irritability, impaired school performance",
        "Chronic fatigue, poor fitness",
        "Iron deficiency anemia",
        "Reduced bone mineral density",
    ]),
    ("Latent/Potential CD", C3, [
        "Normal intestinal mucosa",
        "Positive anti-tTG &amp; AGA",
        "Subepithelial tTG IgA deposits",
        "Associated: Down, Turner syndrome",
        "Type 1 DM prevalence ~4.5%",
    ]),
]

sub_html = ""
for i, (title, color, items) in enumerate(subtypes):
    col = i % 2
    row = i // 2
    x = 40 + col * 450
    y = 68 + row * 230
    items_html = ""
    for item in items:
        items_html += f'<li style="font-size:11px; color:{C1}; margin-bottom:2px;">{item}</li>'
    sub_html += f'''
  <div style="position:absolute; top:{y}px; left:{x}px; width:430px; z-index:5;">
    <svg width="430" height="32" viewBox="0 0 430 32" aria-hidden="true"><rect x="0" y="0" width="430" height="32" rx="6" fill="{color}"/><text x="14" y="22" fill="{WHITE}" font-family="Times New Roman, serif" font-size="13" font-weight="700">{title}</text></svg>
    <div style="background:{LIGHT_BG}; padding:8px 12px; border-radius:0 0 6px 6px; margin-top:-1px;">
      <ul style="margin:0; padding-left:16px;">{items_html}</ul>
    </div>
  </div>'''

slide_09 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{WHITE}; overflow:hidden;">
  {header_bar("Coeliac Disease — 4 Clinical Subtypes", C5)}
  {sub_html}
  {page_badge(9)}
</div></body></html>'''
write_slide(9, slide_09)


# ============================================================
# SLIDE 10 - Coeliac Diagnosis
# ============================================================
slide_10 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{LIGHT_BG}; overflow:hidden;">
  {header_bar("Coeliac Disease — Diagnosis", C5)}
  <div style="position:absolute; top:68px; left:40px; width:430px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:8px;">Specific Antibodies</p>
    <div style="background:{WHITE}; padding:10px 14px; border-radius:8px; margin-bottom:10px;">
      <div style="display:flex; align-items:center; margin-bottom:6px;">
        <div style="min-width:8px; height:8px; background:{C5}; border-radius:50%; margin-right:8px;"></div>
        <p style="font-size:13px; color:{C1};"><span style="font-weight:700;">Tissue Transglutaminase IgA (tTG)</span></p>
      </div>
      <div style="display:flex; align-items:center; margin-bottom:6px;">
        <div style="min-width:8px; height:8px; background:{C4}; border-radius:50%; margin-right:8px;"></div>
        <p style="font-size:13px; color:{C1};"><span style="font-weight:700;">Endomysial IgA (EMA)</span></p>
      </div>
      <div style="display:flex; align-items:center;">
        <div style="min-width:8px; height:8px; background:{C3}; border-radius:50%; margin-right:8px;"></div>
        <p style="font-size:13px; color:{C1};"><span style="font-weight:700;">Anti-gliadin IgA (AGA)</span></p>
      </div>
    </div>
    <div style="background:{C5}; padding:10px 14px; border-radius:8px; margin-bottom:10px;">
      <p style="font-size:12px; color:{WHITE}; line-height:1.5;">
        In <span style="font-weight:700;">IgA deficiency</span> → investigate for <span style="font-weight:700;">tTG IgG</span>
      </p>
    </div>
    <div style="background:{WHITE}; border-left:3px solid {C4}; padding:8px 12px; margin-bottom:8px;">
      <p style="font-size:12px; color:{C1}; line-height:1.5;">
        Persistent elevated EMA/tTG after 12 months GFD → <span style="font-weight:700;">poor compliance</span>
      </p>
    </div>
    <div style="background:{WHITE}; border-left:3px solid {C2}; padding:8px 12px;">
      <p style="font-size:12px; color:{C1}; line-height:1.5;">
        Seronegative CD in <span style="font-weight:700;">6-9%</span> (elderly &amp; immunocompromised)
      </p>
    </div>
  </div>
  <div style="position:absolute; top:68px; right:40px; width:420px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:8px;">Genetic &amp; Endoscopic</p>
    <div style="background:{WHITE}; padding:12px 14px; border-radius:8px; margin-bottom:10px;">
      <p style="font-size:14px; font-weight:700; color:{C5}; margin-bottom:6px;">HLA Genetic Study</p>
      <p style="font-size:12px; color:{C1}; line-height:1.5;">
        HLA-DQ2 and HLA-DQ8 testing — highly sensitive for ruling out coeliac disease
      </p>
    </div>
    <div style="background:{WHITE}; padding:12px 14px; border-radius:8px; margin-bottom:10px;">
      <p style="font-size:14px; font-weight:700; color:{C5}; margin-bottom:6px;">Upper Endoscopy + Biopsy</p>
      <p style="font-size:12px; color:{C1}; line-height:1.5;">
        At least <span style="font-weight:700;">6 duodenal biopsies</span>. Shows <span style="font-weight:700;">villous atrophy</span> — more proximal than distal
      </p>
    </div>
    <div style="background:{C1}; padding:10px 14px; border-radius:8px;">
      <p style="font-size:13px; color:{WHITE}; font-weight:600;">Associated Conditions</p>
      <ul style="margin:4px 0 0 16px;">
        <li style="font-size:11px; color:rgba(255,255,255,0.85); margin-bottom:2px;">Autoimmune diseases (Type 1 DM, thyroid)</li>
        <li style="font-size:11px; color:rgba(255,255,255,0.85); margin-bottom:2px;">IgA deficiency</li>
        <li style="font-size:11px; color:rgba(255,255,255,0.85);">Down, Turner, Williams syndrome</li>
      </ul>
    </div>
  </div>
  {page_badge(10)}
</div></body></html>'''
write_slide(10, slide_10)


# ============================================================
# SLIDE 11 - Coeliac Complications & Treatment
# ============================================================
slide_11 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{WHITE}; overflow:hidden;">
  {header_bar("Coeliac Disease — Complications & Treatment", C5)}
  <div style="position:absolute; top:68px; left:40px; width:440px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C5}; margin-bottom:8px;">Complications</p>
    <div style="background:{LIGHT_BG}; padding:10px 14px; border-radius:8px;">
      <div style="display:flex; align-items:flex-start; margin-bottom:6px;">
        <div style="min-width:8px; height:8px; background:{C5}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Enteropathy-associated T-cell lymphoma (EATCL)</span></p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:6px;">
        <div style="min-width:8px; height:8px; background:{C4}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Ulcerative jejunitis:</span> fever, pain, perforation, bleeding</p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:6px;">
        <div style="min-width:8px; height:8px; background:{C3}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Small bowel adenocarcinoma</span> — incidence increased in CD</p>
      </div>
      <div style="display:flex; align-items:flex-start; margin-bottom:6px;">
        <div style="min-width:8px; height:8px; background:{C2}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Dermatitis herpetiformis:</span> blistering skin eruption, responds to dapsone + GFD</p>
      </div>
      <div style="display:flex; align-items:flex-start;">
        <div style="min-width:8px; height:8px; background:{C1}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
        <p style="font-size:12px; color:{C1};">Malignancy unrelated to disease duration but <span style="font-weight:700;">reduced by GFD</span></p>
      </div>
    </div>
  </div>
  <div style="position:absolute; top:68px; right:40px; width:420px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C2}; margin-bottom:8px;">Treatment — Gluten-Free Diet</p>
    <div style="background:{LIGHT_BG}; padding:10px 14px; border-radius:8px; margin-bottom:10px;">
      <p style="font-size:12px; font-weight:600; color:{C5}; margin-bottom:4px;">AVOID (contain gluten):</p>
      <p style="font-size:12px; color:{C1}; line-height:1.5;">Wheat, rye, barley, couscous, kamut</p>
    </div>
    <div style="background:{LIGHT_BG}; padding:10px 14px; border-radius:8px; margin-bottom:10px;">
      <p style="font-size:12px; font-weight:600; color:{C2}; margin-bottom:4px;">SAFE (gluten-free):</p>
      <p style="font-size:12px; color:{C1}; line-height:1.5;">Rice, maize, buckwheat, potato, chestnut, tapioca, sorghum, millet, quinoa, amaranth</p>
    </div>
    <div style="background:{LIGHT_BG}; padding:10px 14px; border-radius:8px; margin-bottom:10px;">
      <p style="font-size:12px; color:{C1}; line-height:1.5;">
        <span style="font-weight:600;">Oats:</span> Now considered safe (uncontaminated) — improves diet quality
      </p>
    </div>
    <div style="background:{LIGHT_BG}; padding:10px 14px; border-radius:8px;">
      <p style="font-size:12px; color:{C1}; line-height:1.5;">
        <span style="font-weight:600;">Other foods:</span> Vegetables, fruits, nuts, meat, fish, eggs, milk — no limitations
      </p>
      <p style="font-size:12px; color:{C1}; line-height:1.5; margin-top:4px;">
        <span style="font-weight:600;">Supplements:</span> Iron, calcium, vitamin deficiencies
      </p>
    </div>
  </div>
  {page_badge(11)}
</div></body></html>'''
write_slide(11, slide_11)


# ============================================================
# SLIDE 12 - Coeliac New Treatments
# ============================================================
slide_12 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{LIGHT_BG}; overflow:hidden;">
  {header_bar("Coeliac Disease — New Treatment Modalities", C5)}
  <div style="position:absolute; top:68px; left:50px; right:50px; z-index:5;">
    <p style="font-size:14px; color:{C1}; margin-bottom:12px; font-style:italic;">Based on current insights into disease pathogenesis:</p>
    <div style="display:flex; gap:10px; margin-bottom:10px;">
      <div style="flex:1; background:{WHITE}; padding:10px 12px; border-radius:8px; border-top:3px solid {C5};">
        <p style="font-size:12px; font-weight:700; color:{C5}; margin-bottom:4px;">Fontolizumab</p>
        <p style="font-size:11px; color:{C1}; line-height:1.4;">Humanised anti-IFN-γ antibody. Safety &amp; activity in moderate-severe Crohn's</p>
      </div>
      <div style="flex:1; background:{WHITE}; padding:10px 12px; border-radius:8px; border-top:3px solid {C4};">
        <p style="font-size:12px; font-weight:700; color:{C4}; margin-bottom:4px;">Infliximab</p>
        <p style="font-size:11px; color:{C1}; line-height:1.4;">Long-term for life-threatening type I refractory coeliac disease</p>
      </div>
      <div style="flex:1; background:{WHITE}; padding:10px 12px; border-radius:8px; border-top:3px solid {C2};">
        <p style="font-size:12px; font-weight:700; color:{C2}; margin-bottom:4px;">Alemtuzumab</p>
        <p style="font-size:11px; color:{C1}; line-height:1.4;">For refractory CD at risk for EATCL</p>
      </div>
      <div style="flex:1; background:{WHITE}; padding:10px 12px; border-radius:8px; border-top:3px solid {C3};">
        <p style="font-size:12px; font-weight:700; color:{C1}; margin-bottom:4px;">IL-10</p>
        <p style="font-size:11px; color:{C1}; line-height:1.4;">Recombinant human IL-10 suppresses gliadin-dependent T cell activation</p>
      </div>
    </div>
    <p style="font-size:15px; font-weight:700; color:{C1}; margin-bottom:10px;">Research Focus Areas</p>
    <div style="display:flex; gap:8px;">
      <div style="flex:1; background:{C1}; padding:10px; border-radius:8px;">
        <p style="font-size:11px; font-weight:600; color:{WHITE}; text-align:center;">Engineering gluten-free grains</p>
      </div>
      <div style="flex:1; background:{C2}; padding:10px; border-radius:8px;">
        <p style="font-size:11px; font-weight:600; color:{WHITE}; text-align:center;">Exogenous endopeptidases to degrade gliadin</p>
      </div>
      <div style="flex:1; background:{C4}; padding:10px; border-radius:8px;">
        <p style="font-size:11px; font-weight:600; color:{WHITE}; text-align:center;">Zonulin receptor blockage</p>
      </div>
      <div style="flex:1; background:{C5}; padding:10px; border-radius:8px;">
        <p style="font-size:11px; font-weight:600; color:{WHITE}; text-align:center;">tTG2 inhibitors</p>
      </div>
    </div>
    <div style="display:flex; gap:8px; margin-top:8px;">
      <div style="flex:1; background:{C3}; padding:10px; border-radius:8px;">
        <p style="font-size:11px; font-weight:600; color:{C1}; text-align:center;">HLA-DQ2 antagonists</p>
      </div>
      <div style="flex:1; background:{C1}; padding:10px; border-radius:8px;">
        <p style="font-size:11px; font-weight:600; color:{WHITE}; text-align:center;">Cytokine modulation</p>
      </div>
      <div style="flex:1; background:{C2}; padding:10px; border-radius:8px;">
        <p style="font-size:11px; font-weight:600; color:{WHITE}; text-align:center;">Oral tolerance induction to gluten</p>
      </div>
    </div>
  </div>
  {page_badge(12)}
</div></body></html>'''
write_slide(12, slide_12)


# ============================================================
# SLIDE 13 - Short Bowel & Radiation Enteritis
# ============================================================
slide_13 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{WHITE}; overflow:hidden;">
  {header_bar("Short Bowel Syndrome & Radiation Enteritis")}
  <div style="position:absolute; top:68px; left:40px; width:440px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:8px;">Short Bowel Syndrome (Intestinal Resection)</p>
    <div style="background:{LIGHT_BG}; padding:10px 14px; border-radius:8px; margin-bottom:8px;">
      <p style="font-size:12px; color:{C1}; line-height:1.5;">
        Massive resection leaving <span style="font-weight:700;">&lt;1m small bowel</span> in continuity
      </p>
      <p style="font-size:12px; color:{C1}; line-height:1.5; margin-top:4px;">
        Jejunal resection better tolerated than ileal (bile salt &amp; B12 absorption site)
      </p>
    </div>
    <p style="font-size:13px; font-weight:600; color:{C1}; margin-bottom:6px;">After Ileal Resection:</p>
    <div style="display:flex; align-items:flex-start; margin-bottom:4px;">
      <div style="min-width:8px; height:8px; background:{C5}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
      <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Bile-salt diarrhea:</span> Bile salts → colon → water/electrolyte malabsorption</p>
    </div>
    <div style="display:flex; align-items:flex-start; margin-bottom:4px;">
      <div style="min-width:8px; height:8px; background:{C4}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
      <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Steatorrhea &amp; gallstones:</span> ↓ micelle formation, lithogenic bile</p>
    </div>
    <div style="display:flex; align-items:flex-start; margin-bottom:4px;">
      <div style="min-width:8px; height:8px; background:{C3}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
      <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">Oxaluria &amp; oxalate stones:</span> ↑ oxalate absorption in colon</p>
    </div>
    <div style="display:flex; align-items:flex-start;">
      <div style="min-width:8px; height:8px; background:{C2}; border-radius:50%; margin-top:5px; margin-right:8px;"></div>
      <p style="font-size:12px; color:{C1};"><span style="font-weight:600;">B12 deficiency</span> + gastric hypersecretion</p>
    </div>
  </div>
  <div style="position:absolute; top:68px; right:40px; width:420px; z-index:5;">
    <p style="font-size:16px; font-weight:700; color:{C1}; margin-bottom:8px;">Radiation Enteritis</p>
    <div style="background:{LIGHT_BG}; padding:10px 14px; border-radius:8px; margin-bottom:8px;">
      <p style="font-size:12px; color:{C1}; line-height:1.5;">
        Radiation <span style="font-weight:700;">&gt;40 Gy</span> damages intestine. Ileum &amp; rectum most often involved (pelvic irradiation)
      </p>
    </div>
    <div style="display:flex; gap:6px; margin-bottom:8px;">
      <div style="flex:1; background:{C2}; padding:8px; border-radius:6px;">
        <p style="font-size:11px; font-weight:600; color:{WHITE}; text-align:center;">Acute</p>
        <p style="font-size:10px; color:rgba(255,255,255,0.85); text-align:center;">Nausea, vomiting, diarrhea — improves within 6 weeks</p>
      </div>
      <div style="flex:1; background:{C5}; padding:8px; border-radius:6px;">
        <p style="font-size:11px; font-weight:600; color:{WHITE}; text-align:center;">Chronic (&gt;3 months)</p>
        <p style="font-size:10px; color:rgba(255,255,255,0.85); text-align:center;">Prevalence &gt;15%. Obstruction main symptom</p>
      </div>
    </div>
    <div style="background:{WHITE}; border-left:3px solid {C4}; padding:8px 12px;">
      <p style="font-size:12px; color:{C1}; line-height:1.5;">
        Chronic effects: muscle atrophy, ulcerative changes (ischemia), fibrotic strictures. Treatment symptomatic. Surgery avoided unless obstruction/perforation.
      </p>
    </div>
  </div>
  {page_badge(13)}
</div></body></html>'''
write_slide(13, slide_13)


# ============================================================
# SLIDE 14 - Other Causes & Small Intestine Tumors
# ============================================================
slide_14 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{LIGHT_BG}; overflow:hidden;">
  {header_bar("Other Causes & Small Intestine Tumors")}
  <div style="position:absolute; top:68px; left:40px; width:440px; z-index:5;">
    <p style="font-size:15px; font-weight:700; color:{C1}; margin-bottom:8px;">Other Causes of Malabsorption</p>
    <div style="background:{WHITE}; padding:8px 12px; border-radius:8px; margin-bottom:6px;">
      <p style="font-size:12px; color:{C1};"><span style="font-weight:600; color:{C2};">Parasitic:</span> Giardia intestinalis → diarrhea + steatorrhea. Cryptosporidiosis in HIV</p>
    </div>
    <div style="background:{WHITE}; padding:8px 12px; border-radius:8px; margin-bottom:6px;">
      <p style="font-size:12px; color:{C1};"><span style="font-weight:600; color:{C4};">Protein-losing enteropathy:</span> Hypoalbuminemia, peripheral edema</p>
    </div>
    <div style="background:{WHITE}; padding:8px 12px; border-radius:8px; margin-bottom:6px;">
      <p style="font-size:12px; color:{C1};"><span style="font-weight:600; color:{C3};">Eosinophilic gastroenteritis:</span> Associated with asthma, eczema. Steroid treatment</p>
    </div>
    <div style="background:{WHITE}; padding:8px 12px; border-radius:8px; margin-bottom:6px;">
      <p style="font-size:12px; color:{C1};"><span style="font-weight:600; color:{C5};">Intestinal lymphangiectasia:</span> Hypoproteinaemia, ankle edema. Low-fat diet</p>
    </div>
    <div style="background:{WHITE}; padding:8px 12px; border-radius:8px;">
      <p style="font-size:12px; color:{C1};"><span style="font-weight:600; color:{C1};">Abetalipoproteinaemia:</span> Rare. Acanthocytosis, retinitis pigmentosa. Vit E injections</p>
    </div>
  </div>
  <div style="position:absolute; top:68px; right:40px; width:420px; z-index:5;">
    <p style="font-size:15px; font-weight:700; color:{C1}; margin-bottom:8px;">Small Intestine Tumors</p>
    <div style="background:{WHITE}; padding:8px 12px; border-radius:8px; margin-bottom:6px;">
      <p style="font-size:12px; color:{C1};">
        Only <span style="font-weight:700;">3-6%</span> of GI tumors, &lt;1% malignancies. Fluidity, sterility, rapid transit = protection
      </p>
    </div>
    <div style="display:flex; gap:6px; margin-bottom:8px;">
      <div style="flex:1; background:{C5}; padding:8px; border-radius:6px;">
        <p style="font-size:11px; font-weight:600; color:{WHITE}; text-align:center;">Adenocarcinoma</p>
        <p style="font-size:10px; color:rgba(255,255,255,0.85); text-align:center;">Most common. Duodenum/jejunum</p>
      </div>
      <div style="flex:1; background:{C2}; padding:8px; border-radius:6px;">
        <p style="font-size:11px; font-weight:600; color:{WHITE}; text-align:center;">Lymphoma</p>
        <p style="font-size:10px; color:rgba(255,255,255,0.85); text-align:center;">Ileum. B-cell (MALT) or T-cell</p>
      </div>
      <div style="flex:1; background:{C4}; padding:8px; border-radius:6px;">
        <p style="font-size:11px; font-weight:600; color:{WHITE}; text-align:center;">Carcinoid</p>
        <p style="font-size:10px; color:rgba(255,255,255,0.85); text-align:center;">10% of SI neoplasms</p>
      </div>
    </div>
    <div style="background:{C1}; padding:10px 12px; border-radius:8px;">
      <p style="font-size:13px; font-weight:700; color:{C3}; margin-bottom:4px;">Carcinoid Syndrome (5% with liver mets)</p>
      <ul style="margin:0; padding-left:14px;">
        <li style="font-size:11px; color:rgba(255,255,255,0.85); margin-bottom:2px;">Flushing, diarrhea, abdominal pain</li>
        <li style="font-size:11px; color:rgba(255,255,255,0.85); margin-bottom:2px;">Cardiac: pulmonary stenosis, tricuspid incompetence (50%)</li>
        <li style="font-size:11px; color:rgba(255,255,255,0.85); margin-bottom:2px;">Urine 5-HIAA elevated</li>
        <li style="font-size:11px; color:rgba(255,255,255,0.85);">Treatment: Octreotide, Lanreotide</li>
      </ul>
    </div>
  </div>
  {page_badge(14)}
</div></body></html>'''
write_slide(14, slide_14)


# ============================================================
# SLIDE 15 - SUMMARY
# ============================================================
slide_15 = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">{APPENDIX_A}</head><body>
<div class="slide-content" style="background:{C1}; overflow:hidden;">
  <svg style="position:absolute; top:0; left:0; width:960px; height:540px; z-index:0;" viewBox="0 0 960 540" aria-hidden="true">
    <circle cx="800" cy="-100" r="300" fill="{C2}" opacity="0.08"/>
    <circle cx="100" cy="550" r="200" fill="{C3}" opacity="0.06"/>
  </svg>
  <p style="position:absolute; top:28px; left:50px; font-size:34px; font-weight:700; color:{WHITE}; z-index:10;">Key Takeaways</p>
  <div style="position:absolute; top:72px; left:50px; width:110px; height:3px; background:{C3}; border-radius:1.5px; z-index:1;"></div>
  <div style="position:absolute; top:90px; left:40px; width:430px; z-index:5;">
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:10px 14px; margin-bottom:7px; border-left:4px solid {C2};">
      <p style="font-size:13px; color:{WHITE}; line-height:1.5;"><span style="font-weight:700;">Malabsorption:</span> Inability to absorb nutrients from intestinal lumen</p>
    </div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:10px 14px; margin-bottom:7px; border-left:4px solid {C3};">
      <p style="font-size:13px; color:{WHITE}; line-height:1.5;"><span style="font-weight:700;">3 cause categories:</span> Small intestinal, Pancreatic, Mixed</p>
    </div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:10px 14px; margin-bottom:7px; border-left:4px solid {C4};">
      <p style="font-size:13px; color:{WHITE}; line-height:1.5;"><span style="font-weight:700;">Nutritional manifestations:</span> Anemia, osteomalacia, edema, GB stones, night blindness</p>
    </div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:10px 14px; border-left:4px solid {C5};">
      <p style="font-size:13px; color:{WHITE}; line-height:1.5;"><span style="font-weight:700;">Coeliac:</span> 1% prevalence, 4 subtypes, tTG/EMA Ab + biopsy = diagnosis</p>
    </div>
  </div>
  <div style="position:absolute; top:90px; right:40px; width:430px; z-index:5;">
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:10px 14px; margin-bottom:7px; border-left:4px solid {C2};">
      <p style="font-size:13px; color:{WHITE}; line-height:1.5;"><span style="font-weight:700;">Pathophysiology:</span> Gliadin → tTG → CD4+ T cells → IFN-γ → villous atrophy</p>
    </div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:10px 14px; margin-bottom:7px; border-left:4px solid {C3};">
      <p style="font-size:13px; color:{WHITE}; line-height:1.5;"><span style="font-weight:700;">Treatment:</span> Gluten-free diet — wheat, rye, barley avoided. Rice, maize safe</p>
    </div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:10px 14px; margin-bottom:7px; border-left:4px solid {C4};">
      <p style="font-size:13px; color:{WHITE}; line-height:1.5;"><span style="font-weight:700;">Complications:</span> EATCL, ulcerative jejunitis, dermatitis herpetiformis</p>
    </div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:10px 14px; border-left:4px solid {C5};">
      <p style="font-size:13px; color:{WHITE}; line-height:1.5;"><span style="font-weight:700;">New treatments:</span> Fontolizumab, Infliximab, IL-10, zonulin blockers, tTG2 inhibitors</p>
    </div>
  </div>
  <div style="position:absolute; bottom:0; left:0; right:0; height:48px; background:rgba(0,0,0,0.25); z-index:5;"></div>
  <p style="position:absolute; bottom:12px; left:50px; font-size:13px; color:{C3}; z-index:10; font-style:italic;">Malabsorption &amp; Coeliac Disease — Summary</p>
  {page_badge(15)}
</div></body></html>'''
write_slide(15, slide_15)


print(f"\n✅ All {NUM_SLIDES} slides generated successfully!")
print(f"Output: {SLIDES_DIR}")
