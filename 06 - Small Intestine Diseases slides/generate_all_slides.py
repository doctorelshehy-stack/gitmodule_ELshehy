#!/usr/bin/env python3
"""
Generate 14 HTML slides for: 06 - Small Intestine Diseases
Palette 10: #264653 #2a9d8f #e9c46a #f4a261 #e76f51
Font: Times New Roman | 960x540
"""
import os

C1 = "#264653"; C2 = "#2a9d8f"; C3 = "#e9c46a"; C4 = "#f4a261"; C5 = "#e76f51"
WHITE = "#ffffff"; LIGHT_BG = "#f0f7f7"

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SLIDES_DIR = os.path.join(OUT_DIR, "slides")

A = """<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>html,body{margin:0;padding:0;width:100%;height:100%;overflow:hidden;display:flex;justify-content:center;align-items:center;background:#000;}.slide-content{width:960px;height:540px;position:relative;transform-origin:center center;}</style>
<script>
function scaleSlide(){const s=document.querySelector('.slide-content');if(!s)return;const sx=window.innerWidth/960,sy=window.innerHeight/540,sc=Math.min(sx,sy);s.style.width='960px';s.style.height='540px';s.style.transform='scale('+sc+')';s.style.transformOrigin='center center';s.style.flexShrink='0';}
window.addEventListener('load',scaleSlide);window.addEventListener('resize',scaleSlide);
</script>"""

def badge(n):
    return f'<svg style="position:absolute;right:28px;bottom:20px;z-index:50;" width="44" height="26" viewBox="0 0 44 26" aria-hidden="true"><rect x="0" y="0" width="44" height="26" rx="13" fill="{C1}" opacity="0.85"/><text x="22" y="18" text-anchor="middle" fill="{WHITE}" font-family="Times New Roman, serif" font-size="13" font-weight="600">{n}</text></svg>'

def hbar(title, bg=C1):
    return f'<div style="position:absolute;top:0;left:0;right:0;height:52px;background:{bg};z-index:2;"></div><p style="position:absolute;top:10px;left:50px;font-size:20px;font-weight:700;color:{WHITE};z-index:10;">{title}</p>'

def w(n, c):
    path = os.path.join(SLIDES_DIR, f"slide-{n:02d}.html")
    with open(path, "w") as f: f.write(c)
    print(f"  slide-{n:02d}.html OK")

# =========== SLIDE 01 - COVER ===========
s01 = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{C1};overflow:hidden;">
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;z-index:0;" viewBox="0 0 960 540" aria-hidden="true">
<circle cx="800" cy="-80" r="320" fill="{C2}" opacity="0.12"/><circle cx="850" cy="120" r="140" fill="{C3}" opacity="0.10"/>
<rect x="-50" y="380" width="1100" height="220" fill="{C2}" opacity="0.08" transform="rotate(-8 480 490)"/>
<rect x="0" y="0" width="8" height="540" fill="{C2}"/></svg>
<div style="position:absolute;top:130px;left:70px;width:80px;height:5px;background:{C3};border-radius:2px;z-index:5;"></div>
<p style="position:absolute;top:148px;left:70px;font-size:46px;font-weight:700;color:{WHITE};z-index:10;line-height:1.15;">Small Intestine</p>
<p style="position:absolute;top:210px;left:70px;font-size:48px;font-weight:700;color:{C3};z-index:10;line-height:1.15;">Diseases</p>
<p style="position:absolute;top:280px;left:70px;font-size:18px;color:{WHITE};opacity:0.75;z-index:10;max-width:500px;line-height:1.5;">
Short Bowel Syndrome · Radiation Enteritis · Parasitic Infestation<br>
Tumors · Carcinoid · Peutz-Jeghers &amp; More</p>
<div style="position:absolute;bottom:0;left:0;right:0;height:48px;background:rgba(0,0,0,0.25);z-index:5;"></div>
<p style="position:absolute;bottom:13px;left:70px;font-size:13px;color:{C3};z-index:10;font-style:italic;">Gastro-enterology &amp; Internal Medicine</p>
<svg style="position:absolute;right:60px;top:90px;z-index:2;" width="200" height="280" viewBox="0 0 200 280" aria-hidden="true">
<path d="M 60 140 Q 60 100 100 90 Q 140 100 140 140 Q 140 180 100 190 Q 60 180 60 140 Z" fill="{C2}" opacity="0.15"/>
<circle cx="100" cy="140" r="55" fill="none" stroke="{C3}" stroke-width="2" opacity="0.3"/>
<path d="M 60 140 Q 40 180 50 220" stroke="{C3}" stroke-width="2" fill="none" opacity="0.3"/>
<path d="M 140 140 Q 160 180 150 220" stroke="{C3}" stroke-width="2" fill="none" opacity="0.3"/>
<circle cx="50" cy="220" r="5" fill="{C5}" opacity="0.4"/>
<circle cx="150" cy="220" r="5" fill="{C5}" opacity="0.4"/>
<circle cx="100" cy="50" r="6" fill="{C3}" opacity="0.5"/>
</svg>
</div></body></html>'''
w(1, s01)

# =========== SLIDE 02 - TOC ===========
toc = [
    ("01","Short Bowel Syndrome","Resection & metabolic consequences"),
    ("02","Radiation Enteritis","Acute & chronic radiation damage"),
    ("03","Parasitic Infestation","Giardia, Cryptosporidiosis"),
    ("04","Protein-losing Enteropathy","Hypoalbuminemia & edema"),
    ("05","Amyloidosis & Rheumatic Disorders","Systemic involvement"),
    ("06","Eosinophilic Gastroenteritis","Eosinophilic infiltration"),
    ("07","Intestinal Lymphangiectasia","Lymphatic dilation"),
    ("08","Abetalipoproteinaemia","Rare genetic disorder"),
    ("09","Small Intestine Tumors","Adenocarcinoma & Lymphoma"),
    ("10","Carcinoid Tumours","Neuroendocrine tumors"),
    ("11","Peutz-Jeghers Syndrome","Polyposis & pigmentation"),
]
toc_html = ""
for i,(n,t,d) in enumerate(toc):
    y=62+i*39
    toc_html += f'<div style="position:absolute;top:{y}px;left:70px;z-index:5;"><span style="display:inline-block;width:30px;font-size:13px;font-weight:700;color:{C2};">{n}</span><span style="font-size:13px;font-weight:600;color:{C1};">{t}</span><span style="font-size:11px;color:#666;margin-left:6px;">{d}</span></div>'
    if i<len(toc)-1: toc_html += f'<div style="position:absolute;top:{y+28}px;left:100px;width:790px;height:1px;background:{C2};opacity:0.12;z-index:1;"></div>'

s02 = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{WHITE};overflow:hidden;">
<div style="position:absolute;top:0;left:0;width:48px;height:540px;background:{C1};z-index:2;"></div>
<div style="position:absolute;top:0;left:48px;width:4px;height:540px;background:{C2};z-index:2;"></div>
<p style="position:absolute;top:26px;left:72px;font-size:26px;font-weight:700;color:{C1};z-index:10;">Table of Contents</p>
<div style="position:absolute;top:58px;left:72px;width:80px;height:3px;background:{C2};border-radius:1.5px;z-index:1;"></div>
{toc_html}{badge(2)}
</div></body></html>'''
w(2, s02)

# =========== SLIDE 03 - Short Bowel Syndrome ===========
s03 = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{LIGHT_BG};overflow:hidden;">
{hbar("Short Bowel Syndrome (Intestinal Resection)")}
<div style="position:absolute;top:62px;left:50px;right:50px;z-index:5;">
<div style="background:{WHITE};padding:10px 16px;border-radius:8px;border-left:4px solid {C5};">
<p style="font-size:13px;color:{C1};line-height:1.5;">Massive resection leaving <span style="font-weight:700;color:{C5};">&lt;1m of small bowel</span> in continuity → Short Bowel Syndrome. Jejunal resection tolerated better than ileal resection.</p>
</div></div>
<div style="position:absolute;top:120px;left:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">After Ileal Resection</p>
<div style="background:{WHITE};border-left:4px solid {C5};padding:8px 12px;margin-bottom:5px;border-radius:0 6px 6px 0;">
<p style="font-size:12px;font-weight:600;color:{C5};margin-bottom:2px;">1. Bile-Salt Diarrhea</p>
<p style="font-size:11px;color:{C1};line-height:1.4;">Bile salts + fatty acids enter colon → water/electrolyte malabsorption</p></div>
<div style="background:{WHITE};border-left:4px solid {C4};padding:8px 12px;margin-bottom:5px;border-radius:0 6px 6px 0;">
<p style="font-size:12px;font-weight:600;color:{C4};margin-bottom:2px;">2. Steatorrhea &amp; Gallstones</p>
<p style="font-size:11px;color:{C1};line-height:1.4;">Loss >⅓ bile salts → ↓micelle formation → steatorrhea + lithogenic bile</p></div>
<div style="background:{WHITE};border-left:4px solid {C2};padding:8px 12px;margin-bottom:5px;border-radius:0 6px 6px 0;">
<p style="font-size:12px;font-weight:600;color:{C2};margin-bottom:2px;">3. Oxaluria &amp; Oxalate Stones</p>
<p style="font-size:11px;color:{C1};line-height:1.4;">Bile salts in colon → ↑oxalate absorption → urinary stones</p></div>
<div style="background:{WHITE};border-left:4px solid {C1};padding:8px 12px;border-radius:0 6px 6px 0;">
<p style="font-size:12px;font-weight:600;color:{C1};margin-bottom:2px;">4. Vitamin B12 Deficiency</p>
<p style="font-size:11px;color:{C1};line-height:1.4;">Ileum is the site of B12 absorption</p></div>
</div>
<div style="position:absolute;top:120px;right:40px;width:420px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C1};margin-bottom:8px;">Additional Features</p>
<div style="background:{WHITE};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<p style="font-size:13px;font-weight:600;color:{C2};margin-bottom:4px;">Jejunal Resection</p>
<p style="font-size:12px;color:{C1};line-height:1.4;">May lead to gastric hypersecretion with high gastrin levels</p></div>
<div style="background:{WHITE};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<p style="font-size:13px;font-weight:600;color:{C4};margin-bottom:4px;">Ileocaecal Valve Removal</p>
<p style="font-size:12px;color:{C1};line-height:1.4;">Increases incidence of diarrhea</p></div>
<div style="background:{C2};padding:10px 14px;border-radius:8px;">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:600;">Adaptation:</span> Structural and functional intestinal adaptation occurs over ~1 year</p></div>
</div>
{badge(3)}
</div></body></html>'''
w(3, s03)

# =========== SLIDE 04 - Radiation Enteritis ===========
s04 = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{WHITE};overflow:hidden;">
{hbar("Radiation Enteritis")}
<div style="position:absolute;top:62px;left:50px;right:50px;z-index:5;">
<div style="background:{LIGHT_BG};padding:10px 16px;border-radius:8px;border-left:4px solid {C4};">
<p style="font-size:13px;color:{C1};line-height:1.5;">Radiation <span style="font-weight:700;color:{C5};">&gt;40 Gy</span> damages intestine. Ileum &amp; rectum most involved (pelvic RT for gynecological/urological cancers).</p>
</div></div>
<div style="position:absolute;top:120px;left:40px;width:440px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C1};margin-bottom:8px;">Acute Radiation Enteritis</p>
<div style="background:{LIGHT_BG};padding:10px 14px;border-radius:8px;margin-bottom:12px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:3px;">Nausea, vomiting, diarrhea, abdominal pain</li>
<li style="font-size:12px;color:{C1};margin-bottom:3px;">Improves within <span style="font-weight:700;">6 weeks</span> of therapy completion</li>
</ul></div>
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Chronic Radiation Enteritis</p>
<div style="background:{LIGHT_BG};padding:10px 14px;border-radius:8px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:3px;">Diagnosed if symptoms persist <span style="font-weight:700;">≥3 months</span></li>
<li style="font-size:12px;color:{C1};margin-bottom:3px;">Prevalence <span style="font-weight:700;">&gt;15%</span></li>
<li style="font-size:12px;color:{C1};margin-bottom:3px;">Abdominal pain due to obstruction = main symptom</li>
<li style="font-size:12px;color:{C1};margin-bottom:3px;">Malabsorption from bacterial overgrowth + mucosal damage</li>
<li style="font-size:12px;color:{C1};">Treatment symptomatic — often unsuccessful</li>
</ul></div>
</div>
<div style="position:absolute;top:120px;right:40px;width:420px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Chronic Effects</p>
<div style="display:flex;gap:8px;margin-bottom:12px;">
<div style="flex:1;background:{C5};padding:10px;border-radius:8px;text-align:center;">
<p style="font-size:12px;font-weight:600;color:{WHITE};">Muscle Fiber Atrophy</p>
</div>
<div style="flex:1;background:{C4};padding:10px;border-radius:8px;text-align:center;">
<p style="font-size:12px;font-weight:600;color:{WHITE};">Ischemic Ulceration</p>
</div>
<div style="flex:1;background:{C1};padding:10px;border-radius:8px;text-align:center;">
<p style="font-size:12px;font-weight:600;color:{WHITE};">Fibrotic Strictures</p>
</div>
</div>
<div style="background:{LIGHT_BG};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<p style="font-size:13px;font-weight:600;color:{C5};margin-bottom:4px;">Treatment Approach</p>
<p style="font-size:12px;color:{C1};line-height:1.4;">Symptomatic management. <span style="font-weight:700;color:{C5};">Surgery avoided</span> unless for obstruction or perforation.</p></div>
<div style="background:{C4};padding:10px 14px;border-radius:8px;">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:600;">Radiation Proctitis:</span> Diarrhea, tenesmus, ± blood. Local steroids may help initially.</p></div>
</div>
{badge(4)}
</div></body></html>'''
w(4, s04)

# =========== SLIDE 05 - Parasitic & Protein-losing ===========
s05 = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{LIGHT_BG};overflow:hidden;">
{hbar("Parasitic Infestation & Protein-losing Enteropathy")}
<div style="position:absolute;top:62px;left:40px;width:440px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C2};margin-bottom:8px;">Parasitic Infestation</p>
<div style="background:{WHITE};padding:10px 14px;border-radius:8px;margin-bottom:6px;">
<p style="font-size:13px;font-weight:600;color:{C2};margin-bottom:2px;">Giardia intestinalis</p>
<p style="font-size:11px;color:{C1};line-height:1.4;">Produces diarrhea + malabsorption with steatorrhea. Organism found in jejunal fluid/mucosa.</p></div>
<div style="background:{WHITE};padding:10px 14px;border-radius:8px;">
<p style="font-size:13px;font-weight:600;color:{C5};margin-bottom:2px;">Cryptosporidiosis</p>
<p style="font-size:11px;color:{C1};line-height:1.4;">Can also produce malabsorption. HIV patients particularly prone to parasitic infestation.</p></div>
</div>
<div style="position:absolute;top:62px;right:40px;width:420px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C4};margin-bottom:8px;">Protein-losing Enteropathy</p>
<div style="background:{WHITE};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Intestinal protein loss → <span style="font-weight:700;">hypoalbuminemia</span></li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Usually a minor part of a generalized disorder</li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Hepatic synthesis may not compensate → <span style="font-weight:700;">peripheral edema</span></li>
<li style="font-size:12px;color:{C1};">Treatment = treat the underlying cause</li>
</ul></div>
<p style="font-size:14px;font-weight:700;color:#888;margin-bottom:6px;">Other Conditions (referenced)</p>
<div style="background:{WHITE};padding:8px 12px;border-radius:8px;">
<p style="font-size:12px;color:{C1};line-height:1.5;"><span style="font-weight:600;">Meckel's Diverticulum</span> — see later</p>
<p style="font-size:12px;color:{C1};line-height:1.5;margin-top:2px;"><span style="font-weight:600;">Intestinal Ischaemia</span> — see later</p>
</div>
</div>
{badge(5)}
</div></body></html>'''
w(5, s05)

# =========== SLIDE 06 - Amyloidosis & Rheumatic ===========
s06 = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{WHITE};overflow:hidden;">
{hbar("Amyloidosis & Rheumatic Autoimmune Disorders")}
<div style="position:absolute;top:62px;left:40px;width:440px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C1};margin-bottom:8px;">Amyloidosis</p>
<div style="background:{LIGHT_BG};padding:10px 14px;border-radius:8px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Diffuse GI involvement in systemic amyloidosis</li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Occasionally polypoid deposits</li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Symptoms depend on site</li>
<li style="font-size:12px;color:{C1};">Small intestine involvement → <span style="font-weight:700;">diarrhea</span></li>
</ul></div>
</div>
<div style="position:absolute;top:62px;right:40px;width:420px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C4};margin-bottom:8px;">Rheumatic Autoimmune Disorders</p>
<div style="background:{LIGHT_BG};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<p style="font-size:13px;font-weight:600;color:{C5};margin-bottom:4px;">Systemic Sclerosis</p>
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:3px;">Most commonly affects esophagus</li>
<li style="font-size:12px;color:{C1};margin-bottom:3px;">Small bowel &amp; colon may be involved</li>
<li style="font-size:12px;color:{C1};margin-bottom:3px;">Diarrhea &amp; steatorrhea from <span style="font-weight:700;">bacterial overgrowth</span></li>
<li style="font-size:12px;color:{C1};">Due to ↓ motility, dilatation &amp; diverticula</li>
</ul></div>
<div style="background:{LIGHT_BG};padding:8px 12px;border-radius:8px;">
<p style="font-size:12px;color:{C1};"><span style="font-weight:600;">RA &amp; SLE:</span> GI symptoms may occur but rarely predominate</p>
</div>
</div>
{badge(6)}
</div></body></html>'''
w(6, s06)

# =========== SLIDE 07 - Eosinophilic Gastroenteritis ===========
s07 = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{LIGHT_BG};overflow:hidden;">
{hbar("Eosinophilic Gastroenteritis")}
<div style="position:absolute;top:62px;left:50px;right:50px;z-index:5;">
<div style="background:{WHITE};padding:10px 16px;border-radius:8px;border-left:4px solid {C5};">
<p style="font-size:13px;color:{C1};line-height:1.5;">Aetiology unknown. Eosinophilic infiltration &amp; edema of GI mucosa. Gastric antrum &amp; proximal small intestine usually involved.</p></div>
</div>
<div style="position:absolute;top:120px;left:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Key Features</p>
<div style="background:{WHITE};padding:10px 14px;border-radius:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:6px;">
<div style="min-width:8px;height:8px;background:{C2};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Associated with <span style="font-weight:700;">asthma, eczema &amp; urticaria</span></p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:6px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Abdominal pain, nausea, vomiting, <span style="font-weight:700;">upper GI bleeding</span></p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Peripheral eosinophilia + high IgE in <span style="font-weight:700;">only 20%</span></p></div>
</div>
</div>
<div style="position:absolute;top:120px;right:40px;width:420px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C2};margin-bottom:8px;">Diagnosis &amp; Treatment</p>
<div style="background:{WHITE};padding:10px 14px;border-radius:8px;margin-bottom:10px;">
<p style="font-size:12px;font-weight:600;color:{C2};margin-bottom:4px;">Diagnosis</p>
<p style="font-size:12px;color:{C1};line-height:1.4;"><span style="font-weight:700;">Endoscopic biopsy</span> is the key — shows eosinophilic infiltration histologically</p></div>
<div style="background:{C2};padding:10px 14px;border-radius:8px;">
<p style="font-size:12px;font-weight:600;color:{WHITE};margin-bottom:4px;">Treatment</p>
<p style="font-size:12px;color:rgba(255,255,255,0.9);line-height:1.4;"><span style="font-weight:700;">Steroids</span> — for widespread infiltration, especially if peripheral eosinophilia present</p></div>
</div>
{badge(7)}
</div></body></html>'''
w(7, s07)

# =========== SLIDE 08 - Intestinal Lymphangiectasia ===========
s08 = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{WHITE};overflow:hidden;">
{hbar("Intestinal Lymphangiectasia")}
<div style="position:absolute;top:62px;left:50px;right:50px;z-index:5;">
<div style="background:{LIGHT_BG};padding:10px 16px;border-radius:8px;border-left:4px solid {C2};">
<p style="font-size:13px;color:{C1};line-height:1.5;">Dilatation of lymphatics — may be <span style="font-weight:700;">primary</span> or <span style="font-weight:700;">secondary</span> to lymphatic obstruction (malignancy, constrictive pericarditis).</p></div>
</div>
<div style="position:absolute;top:120px;left:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C1};margin-bottom:8px;">Clinical Features</p>
<div style="background:{LIGHT_BG};padding:10px 14px;border-radius:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:8px;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:10px;"></div>
<div><p style="font-size:12px;font-weight:600;color:{C5};margin-bottom:2px;">Hypoproteinaemia</p>
<p style="font-size:11px;color:{C1};">Low serum proteins lead to ankle edema — main presenting feature</p></div></div>
<div style="display:flex;align-items:flex-start;margin-bottom:8px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:10px;"></div>
<div><p style="font-size:12px;font-weight:600;color:{C4};margin-bottom:2px;">Immune Abnormalities</p>
<p style="font-size:11px;color:{C1};">Reduced serum immunoglobulins + low circulating lymphocytes</p></div></div>
</div>
</div>
<div style="position:absolute;top:120px;right:40px;width:420px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C2};margin-bottom:8px;">Treatment</p>
<div style="background:{LIGHT_BG};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:8px;">
<div style="min-width:28px;height:28px;background:{C2};border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:10px;">
<span style="font-size:11px;color:{WHITE};font-weight:700;">1</span></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Low-fat diet</span> + fat-soluble vitamin supplements</p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:28px;height:28px;background:{C4};border-radius:50%;display:flex;align-items:center;justify-content:center;margin-right:10px;">
<span style="font-size:11px;color:{WHITE};font-weight:700;">2</span></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Octreotide</span> — dramatic effect in some primary cases</p></div>
</div>
<div style="background:{C1};padding:10px 14px;border-radius:8px;">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:600;">Key:</span> Differentiate primary vs secondary (treat underlying cause for secondary)</p></div>
</div>
{badge(8)}
</div></body></html>'''
w(8, s08)

# =========== SLIDE 09 - Abetalipoproteinaemia ===========
s09 = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{LIGHT_BG};overflow:hidden;">
{hbar("Abetalipoproteinaemia")}
<div style="position:absolute;top:62px;left:50px;right:50px;z-index:5;">
<div style="background:{WHITE};padding:10px 16px;border-radius:8px;border-left:4px solid {C5};">
<p style="font-size:13px;color:{C1};line-height:1.5;"><span style="font-weight:700;">Rare genetic disorder.</span> Failure of apo B-100 (liver) and apo B-48 (intestine) synthesis → no chylomicron formation → fat accumulates in intestinal cells.</p></div>
</div>
<div style="position:absolute;top:118px;left:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Clinical Features</p>
<div style="background:{WHITE};padding:10px 14px;border-radius:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:8px;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:10px;"></div>
<div><p style="font-size:12px;font-weight:600;color:{C5};margin-bottom:2px;">Acanthocytosis</p>
<p style="font-size:11px;color:{C1};">Spiky red blood cells due to membrane abnormalities</p></div></div>
<div style="display:flex;align-items:flex-start;margin-bottom:8px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:10px;"></div>
<div><p style="font-size:12px;font-weight:600;color:{C4};margin-bottom:2px;">Retinitis Pigmentosa</p>
<p style="font-size:11px;color:{C1};">Progressive vision loss</p></div></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C1};border-radius:50%;margin-top:5px;margin-right:10px;"></div>
<div><p style="font-size:12px;font-weight:600;color:{C1};margin-bottom:2px;">Neurologic Abnormalities</p>
<p style="font-size:11px;color:{C1};">Mental &amp; neurological deficits — <span style="font-weight:700;">preventable by vitamin E injections</span></p></div></div>
</div>
</div>
<div style="position:absolute;top:118px;right:40px;width:420px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C2};margin-bottom:8px;">Pathophysiology</p>
<div style="background:{WHITE};padding:10px 14px;border-radius:8px;margin-bottom:12px;">
<p style="font-size:12px;color:{C1};line-height:1.5;">
<span style="font-weight:700;">Apo B-100</span> in liver + <span style="font-weight:700;">Apo B-48</span> in intestinal cells are both defective → chylomicrons cannot form → fat retained in enterocytes → characteristic histology on jejunal biopsy
</p></div>
<div style="background:{C5};padding:10px 14px;border-radius:8px;">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:600;">Key Intervention:</span> Vitamin E injections can prevent neurologic deterioration</p></div>
</div>
{badge(9)}
</div></body></html>'''
w(9, s09)

# =========== SLIDE 10 - Small Intestine Tumors Overview ===========
s10 = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{WHITE};overflow:hidden;">
{hbar("Small Intestine Tumors — Overview")}
<div style="position:absolute;top:62px;left:50px;right:50px;z-index:5;">
<div style="background:{LIGHT_BG};padding:10px 16px;border-radius:8px;border-left:4px solid {C5};">
<p style="font-size:13px;color:{C1};line-height:1.5;">Small intestine is relatively resistant to neoplasia — only <span style="font-weight:700;">3–6%</span> of all GI tumors, &lt;1% of all malignancies.</p></div>
</div>
<div style="position:absolute;top:118px;left:40px;width:430px;z-index:5;">
<p style="font-size:14px;font-weight:700;color:{C2};margin-bottom:8px;">Why So Protected?</p>
<div style="background:{LIGHT_BG};padding:10px 14px;border-radius:8px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Fluidity of small bowel contents</li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Relative sterility</li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Rapid transit time</li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;">High lymphoid tissue + IgA secretion</li>
<li style="font-size:12px;color:{C1};">→ Reduced exposure to carcinogens</li>
</ul></div>
</div>
<div style="position:absolute;top:118px;right:40px;width:420px;z-index:5;">
<p style="font-size:14px;font-weight:700;color:{C1};margin-bottom:8px;">Risk Factors</p>
<div style="background:{LIGHT_BG};padding:10px 14px;border-radius:8px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Coeliac disease (↑lymphoma &amp; adenocarcinoma)</li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Crohn's disease</li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Peutz-Jeghers syndrome</li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;">FAP (Familial Adenomatous Polyposis)</li>
<li style="font-size:12px;color:{C1};">Neurofibromatosis</li>
</ul></div>
</div>
{badge(10)}
</div></body></html>'''
w(10, s10)

# =========== SLIDE 11 - Tumor Types ===========
s11 = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{LIGHT_BG};overflow:hidden;">
{hbar("Small Intestine Tumor Types")}
<div style="position:absolute;top:68px;left:30px;width:290px;z-index:5;">
<svg width="290" height="36" viewBox="0 0 290 36" aria-hidden="true"><rect x="0" y="0" width="290" height="36" rx="6" fill="{C5}"/><text x="145" y="24" text-anchor="middle" fill="{WHITE}" font-family="Times New Roman, serif" font-size="13" font-weight="700">Adenocarcinoma</text></svg>
<div style="background:{WHITE};padding:8px 10px;border-radius:0 0 6px 6px;margin-top:-1px;">
<ul style="margin:0;padding-left:14px;">
<li style="font-size:11px;color:{C1};margin-bottom:2px;"><span style="font-weight:600;">Most common</span> SI malignancy</li>
<li style="font-size:11px;color:{C1};margin-bottom:2px;">Found in <span style="font-weight:700;">duodenum</span> (periampullary) &amp; jejunum</li>
<li style="font-size:11px;color:{C1};margin-bottom:2px;">Increased in coeliac disease</li>
</ul>
</div>
</div>
<div style="position:absolute;top:68px;left:340px;width:290px;z-index:5;">
<svg width="290" height="36" viewBox="0 0 290 36" aria-hidden="true"><rect x="0" y="0" width="290" height="36" rx="6" fill="{C2}"/><text x="145" y="24" text-anchor="middle" fill="{WHITE}" font-family="Times New Roman, serif" font-size="13" font-weight="700">Lymphoma</text></svg>
<div style="background:{WHITE};padding:8px 10px;border-radius:0 0 6px 6px;margin-top:-1px;">
<ul style="margin:0;padding-left:14px;">
<li style="font-size:11px;color:{C1};margin-bottom:2px;">Most frequent in <span style="font-weight:700;">ileum</span></li>
<li style="font-size:11px;color:{C1};margin-bottom:2px;">B-cell type = MALT (common in developed)</li>
<li style="font-size:11px;color:{C1};margin-bottom:2px;">T-cell = ulcerated plaques/strictures in proximal bowel</li>
<li style="font-size:11px;color:{C1};">Burkitt-like in N. Africa/Middle East (terminal ileum)</li>
</ul>
</div>
</div>
<div style="position:absolute;top:68px;right:30px;width:290px;z-index:5;">
<svg width="290" height="36" viewBox="0 0 290 36" aria-hidden="true"><rect x="0" y="0" width="290" height="36" rx="6" fill="{C4}"/><text x="145" y="24" text-anchor="middle" fill="{WHITE}" font-family="Times New Roman, serif" font-size="13" font-weight="700">Other Tumors</text></svg>
<div style="background:{WHITE};padding:8px 10px;border-radius:0 0 6px 6px;margin-top:-1px;">
<ul style="margin:0;padding-left:14px;">
<li style="font-size:11px;color:{C1};margin-bottom:2px;"><span style="font-weight:600;">Lipomas</span></li>
<li style="font-size:11px;color:{C1};margin-bottom:2px;"><span style="font-weight:600;">Stromal tumors</span></li>
<li style="font-size:11px;color:{C1};margin-bottom:2px;"><span style="font-weight:600;">Adenomas</span></li>
<li style="font-size:11px;color:{C1};margin-bottom:2px;"><span style="font-weight:600;">FAP</span> → may progress to adenocarcinoma</li>
</ul>
</div>
</div>
{badge(11)}
</div></body></html>'''
w(11, s11)

# =========== SLIDE 12 - Carcinoid Tumours ===========
s12 = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{WHITE};overflow:hidden;">
{hbar("Carcinoid Tumours")}
<div style="position:absolute;top:62px;left:40px;width:430px;z-index:5;">
<p style="font-size:14px;font-weight:700;color:{C5};margin-bottom:6px;">Key Facts</p>
<div style="background:{LIGHT_BG};padding:10px 12px;border-radius:8px;margin-bottom:6px;">
<div style="display:flex;align-items:flex-start;margin-bottom:4px;">
<div style="min-width:8px;height:8px;background:{C2};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:11px;color:{C1};"><span style="font-weight:600;">10%</span> of all small bowel neoplasms</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:4px;">
<div style="min-width:8px;height:8px;background:{C3};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:11px;color:{C1};">Common sites: <span style="font-weight:700;">appendix, terminal ileum, rectum</span></p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:4px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:11px;color:{C1};">10% of appendix carcinoids → acute appendicitis</p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:11px;color:{C1};">Carcinoid syndrome in <span style="font-weight:700;">only 5%</span> (with liver mets)</p></div>
</div>
<p style="font-size:14px;font-weight:700;color:{C1};margin-bottom:6px;">Carcinoid Syndrome Features</p>
<div style="background:{LIGHT_BG};padding:10px 12px;border-radius:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:4px;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:11px;color:{C1};"><span style="font-weight:600;">Flushing</span> — bluish-red, face &amp; neck → permanent telangiectases</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:4px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:11px;color:{C1};"><span style="font-weight:600;">Diarrhea</span> — abdominal pain + watery diarrhea</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:4px;">
<div style="min-width:8px;height:8px;background:{C3};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:11px;color:{C1};"><span style="font-weight:600;">Cardiac</span> — pulmonary stenosis, tricuspid incompetence (50%)</p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C1};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:11px;color:{C1};"><span style="font-weight:600;">Hepatomegaly</span> — liver metastases</p></div>
</div>
</div>
<div style="position:absolute;top:62px;right:40px;width:430px;z-index:5;">
<p style="font-size:14px;font-weight:700;color:{C2};margin-bottom:6px;">Mediators Secreted</p>
<div style="background:{LIGHT_BG};padding:8px 12px;border-radius:8px;margin-bottom:10px;">
<p style="font-size:11px;color:{C1};line-height:1.5;">Serotonin (5-HT), bradykinin, histamine, tachykinins, prostaglandins. Diarrhea &amp; cardiac = 5-HT. Flushing = kinins (bradykinin).</p>
</div>
<p style="font-size:14px;font-weight:700;color:{C2};margin-bottom:6px;">Diagnosis</p>
<div style="background:{LIGHT_BG};padding:8px 12px;border-radius:8px;margin-bottom:10px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:11px;color:{C1};margin-bottom:3px;">Ultrasound → liver metastases</li>
<li style="font-size:11px;color:{C1};">Urine <span style="font-weight:700;">5-HIAA</span> (5-hydroxyindoleacetic acid) — high levels</li>
</ul>
</div>
<p style="font-size:14px;font-weight:700;color:{C2};margin-bottom:6px;">Treatment</p>
<div style="background:{C2};padding:10px 12px;border-radius:8px;">
<p style="font-size:12px;color:{WHITE};line-height:1.5;">
<span style="font-weight:700;">Octreotide</span> 200 μg SC TDS → depot 30 mg/4wk<br>
<span style="font-weight:700;">Lanreotide</span> 30 mg/7-10d or gel 60 mg/28d<br>
Survival: <span style="font-weight:700;">5-10 years</span> after diagnosis
</p>
</div>
</div>
{badge(12)}
</div></body></html>'''
w(12, s12)

# =========== SLIDE 13 - Peutz-Jeghers Syndrome ===========
s13 = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{LIGHT_BG};overflow:hidden;">
{hbar("Peutz-Jeghers Syndrome")}
<div style="position:absolute;top:62px;left:50px;right:50px;z-index:5;">
<div style="background:{WHITE};padding:10px 16px;border-radius:8px;border-left:4px solid {C5};">
<p style="font-size:13px;color:{C1};line-height:1.5;">Mucocutaneous pigmentation + GI polyps. <span style="font-weight:700;">Autosomal dominant</span> inheritance.</p></div>
</div>
<div style="position:absolute;top:118px;left:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Clinical Features</p>
<div style="background:{WHITE};padding:10px 14px;border-radius:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:8px;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:10px;"></div>
<div><p style="font-size:12px;font-weight:600;color:{C5};margin-bottom:2px;">Pigmentation</p>
<p style="font-size:11px;color:{C1};">Circumoral <span style="font-weight:700;">(95%)</span>, hands (70%), feet (60%). Brown buccal pigment is characteristic.</p></div></div>
<div style="display:flex;align-items:flex-start;margin-bottom:8px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:10px;"></div>
<div><p style="font-size:12px;font-weight:600;color:{C4};margin-bottom:2px;">GI Polyps</p>
<p style="font-size:11px;color:{C1};">Hamartomas — anywhere in GI tract, most frequent in <span style="font-weight:700;">small bowel</span>. May bleed.</p></div></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C1};border-radius:50%;margin-top:5px;margin-right:10px;"></div>
<div><p style="font-size:12px;font-weight:600;color:{C1};margin-bottom:2px;">Intussusception</p>
<p style="font-size:11px;color:{C1};">Occurs in <span style="font-weight:700;">50%</span> of patients → bowel obstruction</p></div></div>
</div>
</div>
<div style="position:absolute;top:118px;right:40px;width:420px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C2};margin-bottom:8px;">Treatment</p>
<div style="background:{WHITE};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:4px;"><span style="font-weight:700;">Endoscopic polypectomy</span> — first line</li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Bowel resection avoided — only for gangrenous intussusception</li>
<li style="font-size:12px;color:{C1};">Yearly <span style="font-weight:700;">pan-endoscopy</span> — high malignancy risk</li>
</ul></div>
<div style="background:{C5};padding:10px 14px;border-radius:8px;">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:600;">Malignancy Risk:</span> Adenocarcinoma can develop. Regular surveillance is essential.</p></div>
</div>
{badge(13)}
</div></body></html>'''
w(13, s13)

# =========== SLIDE 14 - SUMMARY ===========
s14 = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{C1};overflow:hidden;">
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;z-index:0;" viewBox="0 0 960 540" aria-hidden="true">
<circle cx="800" cy="-100" r="300" fill="{C2}" opacity="0.08"/>
<circle cx="100" cy="550" r="200" fill="{C3}" opacity="0.06"/></svg>
<p style="position:absolute;top:24px;left:50px;font-size:30px;font-weight:700;color:{WHITE};z-index:10;">Key Takeaways</p>
<div style="position:absolute;top:66px;left:50px;width:100px;height:3px;background:{C3};border-radius:1.5px;z-index:1;"></div>
<div style="position:absolute;top:84px;left:40px;width:430px;z-index:5;">
<div style="background:rgba(255,255,255,0.1);border-radius:8px;padding:8px 12px;margin-bottom:6px;border-left:4px solid {C2};">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:700;">Short Bowel:</span> &lt;1m resection → bile-salt diarrhea, steatorrhea, oxalate stones, B12 deficiency</p>
</div>
<div style="background:rgba(255,255,255,0.1);border-radius:8px;padding:8px 12px;margin-bottom:6px;border-left:4px solid {C3};">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:700;">Radiation Enteritis:</span> &gt;40 Gy → acute (improves 6wk) or chronic (&gt;15%, obstruction)</p>
</div>
<div style="background:rgba(255,255,255,0.1);border-radius:8px;padding:8px 12px;margin-bottom:6px;border-left:4px solid {C4};">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:700;">Parasitic:</span> Giardia → steatorrhea. Cryptosporidiosis → HIV patients</p>
</div>
<div style="background:rgba(255,255,255,0.1);border-radius:8px;padding:8px 12px;margin-bottom:6px;border-left:4px solid {C5};">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:700;">Lymphangiectasia:</span> Dilated lymphatics → hypoalbuminemia + edema → low-fat diet + octreotide</p>
</div>
<div style="background:rgba(255,255,255,0.1);border-radius:8px;padding:8px 12px;border-left:4px solid {C3};">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:700;">Abetalipoproteinaemia:</span> Rare. Acanthocytosis, retinitis pigmentosa. Vit E prevents neuro damage</p>
</div>
</div>
<div style="position:absolute;top:84px;right:40px;width:430px;z-index:5;">
<div style="background:rgba(255,255,255,0.1);border-radius:8px;padding:8px 12px;margin-bottom:6px;border-left:4px solid {C2};">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:700;">SI Tumors:</span> 3-6% of GI tumors. Adenocarcinoma (most common), Lymphoma (ileum)</p>
</div>
<div style="background:rgba(255,255,255,0.1);border-radius:8px;padding:8px 12px;margin-bottom:6px;border-left:4px solid {C4};">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:700;">Carcinoid:</span> APUD cells, 10% of SI neoplasms. Carcinoid syndrome (5%) → flushing, diarrhea, cardiac</p>
</div>
<div style="background:rgba(255,255,255,0.1);border-radius:8px;padding:8px 12px;margin-bottom:6px;border-left:4px solid {C5};">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:700;">Carcinoid Treatment:</span> Octreotide, lanreotide. Urine 5-HIAA for diagnosis</p>
</div>
<div style="background:rgba(255,255,255,0.1);border-radius:8px;padding:8px 12px;margin-bottom:6px;border-left:4px solid {C3};">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:700;">Peutz-Jeghers:</span> AD inheritance. Pigmentation + hamartomatous polyps → endoscopic polypectomy + yearly surveillance</p>
</div>
<div style="background:rgba(255,255,255,0.1);border-radius:8px;padding:8px 12px;border-left:4px solid {C2};">
<p style="font-size:12px;color:{WHITE};line-height:1.4;"><span style="font-weight:700;">Eosinophilic GE:</span> Unknown etiology. Steroids for treatment. Biopsy for diagnosis</p>
</div>
</div>
<div style="position:absolute;bottom:0;left:0;right:0;height:44px;background:rgba(0,0,0,0.25);z-index:5;"></div>
<p style="position:absolute;bottom:11px;left:50px;font-size:12px;color:{C3};z-index:10;font-style:italic;">Small Intestine Diseases — Summary</p>
{badge(14)}
</div></body></html>'''
w(14, s14)

print(f"\n✅ All 14 slides generated!")
