#!/usr/bin/env python3
"""Generate 14 HTML slides for: 07 - IBD - Crohns Disease"""
import os
C1="#264653";C2="#2a9d8f";C3="#e9c46a";C4="#f4a261";C5="#e76f51";W="#ffffff";LB="#f0f7f7"
OUT=os.path.dirname(os.path.abspath(__file__));SD=os.path.join(OUT,"slides")
A='<meta name="viewport" content="width=device-width,initial-scale=1.0"><style>html,body{margin:0;padding:0;width:100%;height:100%;overflow:hidden;display:flex;justify-content:center;align-items:center;background:#000;}.slide-content{width:960px;height:540px;position:relative;transform-origin:center center;}</style><script>function scaleSlide(){const s=document.querySelector(".slide-content");if(!s)return;const sx=window.innerWidth/960,sy=window.innerHeight/540,sc=Math.min(sx,sy);s.style.width="960px";s.style.height="540px";s.style.transform="scale("+sc+")";s.style.transformOrigin="center center";s.style.flexShrink="0";}window.addEventListener("load",scaleSlide);window.addEventListener("resize",scaleSlide);</script>'
def b(n):return f'<svg style="position:absolute;right:28px;bottom:20px;z-index:50;" width="44" height="26" viewBox="0 0 44 26"><rect x="0" y="0" width="44" height="26" rx="13" fill="{C1}" opacity=".85"/><text x="22" y="18" text-anchor="middle" fill="{W}" font-family="Times New Roman,serif" font-size="13" font-weight="600">{n}</text></svg>'
def h(t,c=C1):return f'<div style="position:absolute;top:0;left:0;right:0;height:52px;background:{c};z-index:2;"></div><p style="position:absolute;top:10px;left:50px;font-size:20px;font-weight:700;color:{W};z-index:10;">{t}</p>'
def w(n,c):open(os.path.join(SD,f"slide-{n:02d}.html"),"w").write(c);print(f"  slide-{n:02d}.html OK")

# === S01 - COVER ===
s01=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{C1};overflow:hidden;">
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;z-index:0;" viewBox="0 0 960 540"><circle cx="800" cy="-80" r="320" fill="{C2}" opacity=".12"/><circle cx="850" cy="120" r="140" fill="{C3}" opacity=".10"/><rect x="-50" y="380" width="1100" height="220" fill="{C2}" opacity=".08" transform="rotate(-8 480 490)"/><rect x="0" y="0" width="8" height="540" fill="{C2}"/></svg>
<div style="position:absolute;top:120px;left:70px;width:80px;height:5px;background:{C3};border-radius:2px;z-index:5;"></div>
<p style="position:absolute;top:120px;left:70px;font-size:32px;font-weight:700;color:{W};z-index:10;line-height:1.15;">Inflammatory Bowel Disease</p>
<p style="position:absolute;top:168px;left:70px;font-size:52px;font-weight:700;color:{C3};z-index:10;line-height:1.15;">Crohn's Disease</p>
<p style="position:absolute;top:240px;left:70px;font-size:18px;color:{W};opacity:.75;z-index:10;max-width:520px;line-height:1.5;">
Pathophysiology · Genetics · Clinical Features<br>Diagnosis · Medical &amp; Surgical Management</p>
<div style="position:absolute;bottom:0;left:0;right:0;height:48px;background:rgba(0,0,0,.25);z-index:5;"></div>
<p style="position:absolute;bottom:13px;left:70px;font-size:13px;color:{C3};z-index:10;font-style:italic;">Gastro-enterology &amp; Internal Medicine</p>
<svg style="position:absolute;right:50px;top:100px;z-index:2;" width="180" height="260" viewBox="0 0 180 260"><path d="M 90 30 Q 160 50 170 130 Q 160 210 90 230 Q 20 210 10 130 Q 20 50 90 30 Z" fill="{C2}" opacity=".12"/><path d="M 90 50 Q 140 65 148 130 Q 140 195 90 210 Q 40 195 32 130 Q 40 65 90 50 Z" fill="none" stroke="{C3}" stroke-width="2" opacity=".3"/><path d="M 50 130 Q 50 160 70 190" stroke="{C4}" stroke-width="2" fill="none" opacity=".4"/><path d="M 130 130 Q 130 160 110 190" stroke="{C4}" stroke-width="2" fill="none" opacity=".4"/><circle cx="58" cy="145" r="4" fill="{C5}" opacity=".5"/><circle cx="122" cy="145" r="4" fill="{C5}" opacity=".5"/><circle cx="75" cy="175" r="3" fill="{C5}" opacity=".4"/><circle cx="105" cy="175" r="3" fill="{C5}" opacity=".4"/></svg>
</div></body></html>'''
w(1,s01)

# === S02 - TOC ===
toc=[("01","IBD Overview","Definition & etiopathogenesis"),("02","Genetics","CARD15/NOD2 & gene loci"),("03","Crohn's Epidemiology","Incidence & risk factors"),("04","Pathology","Transmural inflammation patterns"),("05","Clinical Features","Symptoms, fistulae, perianal disease"),("06","Investigations","Endoscopy, imaging, labs"),("07","Lifestyle & 5-ASA","Diet, smoking cessation, 5-ASA"),("08","Antibiotics & Steroids","Metronidazole, prednisone"),("09","Immunosuppressives","Azathioprine, 6-MP, MTX"),("10","Biologics","Anti-TNF, IL-12/23, integrin"),("11","Surgical Treatment","Resection & recurrence rates"),("12","Ileal Resection","Complications & management"),("13","Prognosis & Complications","Outcomes & surveillance"),]
th=""
for i,(n,t,d) in enumerate(toc):
    y=68+i*36
    th+=f'<div style="position:absolute;top:{y}px;left:70px;z-index:5;"><span style="display:inline-block;width:30px;font-size:13px;font-weight:700;color:{C2};">{n}</span><span style="font-size:13px;font-weight:600;color:{C1};">{t}</span><span style="font-size:11px;color:#666;margin-left:6px;">{d}</span></div>'
    if i<len(toc)-1:th+=f'<div style="position:absolute;top:{y+26}px;left:100px;width:790px;height:1px;background:{C2};opacity:.12;z-index:1;"></div>'
s02=f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body><div class="slide-content" style="background:{W};overflow:hidden;"><div style="position:absolute;top:0;left:0;width:48px;height:540px;background:{C1};z-index:2;"></div><div style="position:absolute;top:0;left:48px;width:4px;height:540px;background:{C2};z-index:2;"></div><p style="position:absolute;top:20px;left:72px;font-size:26px;font-weight:700;color:{C1};z-index:10;">Table of Contents</p><div style="position:absolute;top:60px;left:72px;width:80px;height:3px;background:{C2};border-radius:1.5px;z-index:1;"></div>{th}{b(2)}</div></body></html>'
w(2,s02)

# === S03 - IBD Overview & Genetics ===
s03=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{LB};overflow:hidden;">
{h("IBD — Definition & Genetics")}
<div style="position:absolute;top:62px;left:40px;width:440px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C1};margin-bottom:8px;">Definition</p>
<div style="background:{W};padding:10px 14px;border-radius:8px;margin-bottom:10px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Complex, <span style="font-weight:700;">multifactorial etiology</span></li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Sustained immune response to enteric flora</li>
<li style="font-size:12px;color:{C1};">Lack of down-regulation after infection in genetically predisposed individual</li>
</ul>
</div>
<p style="font-size:15px;font-weight:700;color:{C1};margin-bottom:8px;">Genetics</p>
<div style="background:{W};padding:10px 14px;border-radius:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C2};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Increased risk in relatives of IBD patients — especially siblings</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Familial risk greater if proband has <span style="font-weight:700;">CD rather than UC</span></p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">200+</span> associated gene loci — polygenomic pattern</p></div>
</div>
</div>
<div style="position:absolute;top:62px;right:40px;width:420px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">CARD15/NOD2 Gene</p>
<div style="background:{W};padding:10px 14px;border-radius:8px;margin-bottom:10px;">
<div style="display:flex;align-items:flex-start;margin-bottom:6px;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Associated with <span style="font-weight:700;">Crohn's Disease</span></p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:6px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Relative risk: heterozygote <span style="font-weight:700;">3</span>, homozygote <span style="font-weight:700;">40</span></p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:6px;">
<div style="min-width:8px;height:8px;background:{C3};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">More common in <span style="font-weight:700;">Ashkenazi Jews</span></p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:6px;">
<div style="min-width:8px;height:8px;background:{C2};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Associated with <span style="font-weight:700;">early onset, ileal, fistulizing, stricturing</span> disease</p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C1};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Modulates <span style="font-weight:700;">NFκβ</span> — required for innate immune response to microbes</p></div>
</div>
</div>
{b(3)}
</div></body></html>'''
w(3,s03)

# === S04 - Crohn's Definition & Epidemiology ===
s04=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{W};overflow:hidden;">
{h("Crohn's Disease — Definition & Epidemiology",C5)}
<div style="position:absolute;top:62px;left:50px;right:50px;z-index:5;">
<div style="background:{LB};padding:10px 16px;border-radius:8px;border-left:4px solid {C5};">
<p style="font-size:13px;color:{C1};line-height:1.5;"><span style="font-weight:700;">Definition:</span> Chronic <span style="font-weight:700;">transmural</span> inflammatory disorder potentially affecting the entire gut from mouth to perianal region — "gum to bum".</p></div>
</div>
<div style="position:absolute;top:118px;left:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Epidemiology</p>
<div style="background:{LB};padding:10px 14px;border-radius:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Worldwide incidence: <span style="font-weight:700;">3-15 to 10-20/100,000</span></p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">135,000 Canadians living with CD</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C3};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Bimodal</span> onset: &lt;30 yrs, second peak at 60 yrs</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C2};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">M = F, increasing in young females</p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C1};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">More in White people, <span style="font-weight:700;">Ashkenazi Jews</span></p></div>
</div>
</div>
<div style="position:absolute;top:118px;right:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C4};margin-bottom:8px;">Risk Factors</p>
<div style="background:{LB};padding:10px 14px;border-radius:8px;margin-bottom:10px;">
<div style="display:flex;align-items:flex-start;margin-bottom:8px;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Smoking:</span> Higher incidence in CD patients than general population</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:8px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Migration:</span> Risk in Asians increases with move to Western countries</p></div>
</div>
<div style="background:{C5};padding:10px 14px;border-radius:8px;">
<p style="font-size:12px;color:{W};line-height:1.4;"><span style="font-weight:600;">Key Point:</span> CD incidence is increasing relative to UC globally</p></div>
</div>
{b(4)}
</div></body></html>'''
w(4,s04)

# === S05 - Pathology ===
s05=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{LB};overflow:hidden;">
{h("Crohn's Disease — Pathology",C5)}
<div style="position:absolute;top:62px;left:40px;width:440px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C1};margin-bottom:8px;">Location & Appearance</p>
<div style="background:{W};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:6px;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Most common:</span> Ileum + right colon</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:6px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Linear ulcers</span> → mucosal islands → "cobblestone" appearance</p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C2};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Granulomas:</span> 50% of surgical specimens, 15% of mucosal biopsies</p></div>
</div>
</div>
<div style="position:absolute;top:62px;right:40px;width:420px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Key Pathologic Features</p>
<div style="display:flex;gap:8px;margin-bottom:10px;">
<div style="flex:1;background:{C5};padding:12px 8px;border-radius:8px;text-align:center;">
<p style="font-size:13px;font-weight:700;color:{W};">Transmural</p>
<p style="font-size:10px;color:rgba(255,255,255,.85);">Involves all layers</p></div>
<div style="flex:1;background:{C4};padding:12px 8px;border-radius:8px;text-align:center;">
<p style="font-size:13px;font-weight:700;color:{W};">Skip Lesions</p>
<p style="font-size:10px;color:rgba(255,255,255,.85);">Normal segments between</p></div>
<div style="flex:1;background:{C1};padding:12px 8px;border-radius:8px;text-align:center;">
<p style="font-size:13px;font-weight:700;color:{W};">Fissures</p>
<p style="font-size:10px;color:rgba(255,255,255,.85);">Deep → fistula risk</p></div>
</div>
<div style="background:{W};padding:10px 14px;border-radius:8px;">
<p style="font-size:13px;font-weight:700;color:{C5};margin-bottom:4px;">Crohn's vs UC — Key Differences</p>
<p style="font-size:11px;color:{C1};line-height:1.4;">CD: transmural, skip lesions, granulomas, fistulae, strictures</p>
<p style="font-size:11px;color:{C1};line-height:1.4;">UC: mucosal only, continuous, crypt abscesses, no fistulae</p>
</div>
</div>
{b(5)}
</div></body></html>'''
w(5,s05)

# === S06 - Clinical Features ===
s06=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{W};overflow:hidden;">
{h("Crohn's Disease — Clinical Features",C5)}
<div style="position:absolute;top:62px;left:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C1};margin-bottom:8px;">Presenting Symptoms</p>
<div style="background:{LB};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:4px;"><span style="font-weight:700;">Recurrent episodes</span> of abdominal cramps, non-bloody diarrhea, weight loss</li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Ileitis: post-prandial pain, vomiting, RLQ mass — mimics acute appendicitis</li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;">Natural history <span style="font-weight:700;">unpredictable</span></li>
<li style="font-size:12px;color:{C1};">Perianal disease: fistulae, fissures, abscesses</li>
</ul>
</div>
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Fistulae</p>
<div style="background:{LB};padding:8px 12px;border-radius:8px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:3px;">Enteric fistulae: skin, bladder, vagina, other bowel</li>
<li style="font-size:12px;color:{C1};">Deep fissures → perforation into contiguous viscera</li>
</ul>
</div>
</div>
<div style="position:absolute;top:62px;right:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C4};margin-bottom:8px;">Poor Prognosis Factors</p>
<div style="display:flex;gap:6px;margin-bottom:10px;">
<div style="flex:1;background:{C5};padding:10px;border-radius:8px;text-align:center;">
<p style="font-size:13px;font-weight:700;color:{W};">Young Age</p></div>
<div style="flex:1;background:{C4};padding:10px;border-radius:8px;text-align:center;">
<p style="font-size:13px;font-weight:700;color:{W};">Perianal Disease</p></div>
<div style="flex:1;background:{C1};padding:10px;border-radius:8px;text-align:center;">
<p style="font-size:13px;font-weight:700;color:{W};">Corticosteroid Need</p></div>
</div>
<p style="font-size:15px;font-weight:700;color:{C2};margin-bottom:8px;">Extra-intestinal Manifestations</p>
<div style="background:{LB};padding:8px 12px;border-radius:8px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:3px;">More common with colonic involvement</li>
<li style="font-size:12px;color:{C1};">Joints, skin, eyes, liver (see EIM table)</li>
</ul>
</div>
</div>
{b(6)}
</div></body></html>'''
w(6,s06)

# === S07 - Investigations ===
s07=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{LB};overflow:hidden;">
{h("Crohn's Disease — Investigations",C5)}
<div style="position:absolute;top:68px;left:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C2};margin-bottom:8px;">Endoscopy & Imaging</p>
<div style="background:{W};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C2};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Colonoscopy + biopsy</span> — visualize mucosa, take biopsies</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">CT/MR enterography</span> — visualize small bowel</p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Gastroscopy</span> — less often but may show upper GI involvement</p></div>
</div>
</div>
<div style="position:absolute;top:68px;right:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Laboratory Tests</p>
<div style="background:{W};padding:10px 14px;border-radius:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">CRP</span> — elevated in most new cases, useful to monitor treatment response</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Bacterial cultures, O&amp;P</span> — exclude other causes</p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C3};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">C. difficile toxin</span> — rule out superimposed infection</p></div>
</div>
</div>
{b(7)}
</div></body></html>'''
w(7,s07)

# === S08 - Lifestyle & 5-ASA ===
s08=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{W};overflow:hidden;">
{h("Management — Lifestyle, Antidiarrheals & 5-ASA")}
<div style="position:absolute;top:62px;left:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C2};margin-bottom:8px;">Lifestyle & Diet</p>
<div style="background:{LB};padding:8px 12px;border-radius:8px;margin-bottom:10px;">
<div style="display:flex;align-items:flex-start;margin-bottom:4px;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};font-weight:700;">Smoking cessation</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:4px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Fluids only during acute exacerbation</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:4px;">
<div style="min-width:8px;height:8px;background:{C3};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Enteral diets → remission for Crohn's ileitis only</p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C2};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Vitamin/mineral supplements if extensive involvement</p></div>
</div>
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Antidiarrheal Agents</p>
<div style="background:{LB};padding:8px 12px;border-radius:8px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:3px;"><span style="font-weight:700;">Loperamide</span> &gt; Diphenoxylate &gt; Codeine</li>
<li style="font-size:12px;color:{C1};margin-bottom:3px;">↓ Small bowel motility</li>
<li style="font-size:12px;color:{C5};font-weight:700;">CAUTION: avoid during flare-ups — risk of toxic megacolon</li>
</ul>
</div>
</div>
<div style="position:absolute;top:62px;right:40px;width:420px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C4};margin-bottom:8px;">5-ASA Preparations</p>
<div style="background:{LB};padding:8px 12px;border-radius:8px;margin-bottom:8px;">
<p style="font-size:13px;font-weight:600;color:{C4};margin-bottom:4px;">Sulfasalazine (Salazopyrin)</p>
<p style="font-size:11px;color:{C1};line-height:1.4;">5-ASA bound to sulfapyridine. Hydrolysis by bacteria releases active 5-ASA.</p>
</div>
<div style="background:{LB};padding:8px 12px;border-radius:8px;margin-bottom:8px;">
<p style="font-size:13px;font-weight:600;color:{C2};margin-bottom:4px;">Mesalamine (Pentasa)</p>
<p style="font-size:11px;color:{C1};line-height:1.4;">Coated 5-ASA — releases in ileum &amp; colon. Used for mild ileitis.</p>
</div>
<div style="background:{C3};padding:8px 12px;border-radius:8px;">
<p style="font-size:12px;color:{C1};line-height:1.4;"><span style="font-weight:600;">Note:</span> 5-ASA efficacy in CD is controversial. Initial trial for mild ileitis warranted.</p>
</div>
</div>
{b(8)}
</div></body></html>'''
w(8,s08)

# === S09 - Antibiotics & Steroids ===
s09=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{LB};overflow:hidden;">
{h("Management — Antibiotics & Corticosteroids")}
<div style="position:absolute;top:62px;left:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C2};margin-bottom:8px;">Antibiotics</p>
<div style="background:{W};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C2};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Metronidazole</span> 20 mg/kg/d BID/TID</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Ciprofloxacin</span></p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Best described for <span style="font-weight:700;">perianal CD</span> — relapse when discontinued</p></div>
</div>
</div>
<div style="position:absolute;top:62px;right:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Corticosteroids</p>
<div style="background:{W};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Prednisone</span> 40 mg OD for acute exacerbations</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">IV methylprednisolone</span> if severe</p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C3};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">No proven role in maintaining remission</p></div>
</div>
<div style="background:{C5};padding:10px 14px;border-radius:8px;">
<p style="font-size:12px;color:{W};line-height:1.4;"><span style="font-weight:600;">Warning:</span> Steroids mask intra-abdominal sepsis. Do not use for maintenance.</p></div>
</div>
{b(9)}
</div></body></html>'''
w(9,s09)

# === S10 - Immunosuppressives ===
s10=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{W};overflow:hidden;">
{h("Management — Immunosuppressives")}
<div style="position:absolute;top:62px;left:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C1};margin-bottom:8px;">Agents</p>
<div style="background:{LB};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C2};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">6-Mercaptopurine (6-MP)</span></p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Azathioprine (Imuran)</span></p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Methotrexate (MTX)</span> — used less often</p></div>
</div>
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Key Uses</p>
<div style="background:{LB};padding:10px 14px;border-radius:8px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:3px;">Maintain remission — NOT acute inflammation</li>
<li style="font-size:12px;color:{C1};margin-bottom:3px;"><span style="font-weight:700;">Steroid-sparing</span> — reduces risk of relapse as steroids withdrawn</li>
<li style="font-size:12px;color:{C1};margin-bottom:3px;">May heal fistulae, decrease disease activity</li>
<li style="font-size:12px;color:{C1};margin-bottom:3px;">May require &gt;3 months for effect — continued for years</li>
<li style="font-size:12px;color:{C1};">Given with biologics — increases efficacy, lowers tolerance</li>
</ul>
</div>
</div>
<div style="position:absolute;top:62px;right:40px;width:420px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Side Effects</p>
<div style="display:flex;gap:6px;margin-bottom:10px;flex-wrap:wrap;">
<div style="background:{C5};padding:8px 12px;border-radius:6px;"><span style="font-size:11px;font-weight:600;color:{W};">Vomiting</span></div>
<div style="background:{C4};padding:8px 12px;border-radius:6px;"><span style="font-size:11px;font-weight:600;color:{W};">Pancreatitis</span></div>
<div style="background:{C1};padding:8px 12px;border-radius:6px;"><span style="font-size:11px;font-weight:600;color:{W};">Bone Marrow Suppression</span></div>
<div style="background:{C5};padding:8px 12px;border-radius:6px;"><span style="font-size:11px;font-weight:600;color:{W};">Lymphoma Risk</span></div>
</div>
<div style="background:{C2};padding:10px 14px;border-radius:8px;">
<p style="font-size:13px;color:{W};font-weight:600;margin-bottom:4px;">Top-Down Strategy</p>
<p style="font-size:12px;color:rgba(255,255,255,.9);line-height:1.4;">Immunosuppressants + immunomodulators increasingly used as first-line therapy.</p></div>
</div>
{b(10)}
</div></body></html>'''
w(10,s10)

# === S11 - Biologics ===
s11=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{LB};overflow:hidden;">
{h("Management — Biologics")}
<div style="position:absolute;top:62px;left:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Anti-TNF Agents</p>
<div style="background:{W};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:6px;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Infliximab (Remicade)</span> — IV antibody to TNF-α</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:6px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Adalimumab (Humira)</span> — SC antibody to TNF-α</p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C3};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};">Proven effective for <span style="font-weight:700;">fistulae</span> and <span style="font-weight:700;">medically refractory CD</span></p></div>
</div>
<div style="background:{C2};padding:8px 12px;border-radius:8px;margin-bottom:8px;">
<p style="font-size:12px;color:{W};line-height:1.4;"><span style="font-weight:700;">Dual Therapy:</span> Infliximab + azathioprine more effective than either alone</p></div>
</div>
<div style="position:absolute;top:62px;right:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C2};margin-bottom:8px;">Newer Biologics</p>
<div style="background:{W};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:6px;">
<div style="min-width:8px;height:8px;background:{C2};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<div><p style="font-size:12px;font-weight:600;color:{C2};margin-bottom:2px;">Ustekinumab</p>
<p style="font-size:11px;color:{C1};">Monoclonal antibody against P40 subunit of IL-12 and IL-23</p></div></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<div><p style="font-size:12px;font-weight:600;color:{C4};margin-bottom:2px;">Vedolizumab</p>
<p style="font-size:11px;color:{C1};">Anti-integrin α4β7 → reduces lymphocyte traffic to gut. Indicated for UC &amp; CD.</p></div></div>
</div>
<div style="background:{C5};padding:8px 12px;border-radius:8px;">
<p style="font-size:12px;color:{W};line-height:1.4;"><span style="font-weight:600;">Key:</span> Biologics have revolutionized CD management, especially for fistulizing disease.</p></div>
</div>
{b(11)}
</div></body></html>'''
w(11,s11)

# === S12 - Surgical Treatment ===
s12=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{W};overflow:hidden;">
{h("Management — Surgical Treatment")}
<div style="position:absolute;top:62px;left:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Indications for Surgery</p>
<div style="background:{LB};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:4px;"><span style="font-weight:700;">Fistulae</span></li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;"><span style="font-weight:700;">Obstruction</span></li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;"><span style="font-weight:700;">Abscess</span></li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;"><span style="font-weight:700;">Perforation</span></li>
<li style="font-size:12px;color:{C1};margin-bottom:4px;"><span style="font-weight:700;">Bleeding</span></li>
<li style="font-size:12px;color:{C1};"><span style="font-weight:700;">Medically refractory disease</span></li>
</ul>
</div>
<p style="font-size:14px;font-weight:700;color:{C5};margin-bottom:6px;">Short Bowel Risk</p>
<div style="background:{LB};padding:8px 12px;border-radius:8px;">
<p style="font-size:12px;color:{C1};line-height:1.5;">If &lt;50% or &lt;200 cm of functional small intestine remains → <span style="font-weight:700;">short bowel syndrome</span></p></div>
</div>
<div style="position:absolute;top:62px;right:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C4};margin-bottom:8px;">Recurrence After Surgery</p>
<div style="background:{LB};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C5};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Clinical:</span> 50% within 5 yrs, 85% within 15 yrs</p></div>
<div style="display:flex;align-items:flex-start;margin-bottom:5px;">
<div style="min-width:8px;height:8px;background:{C4};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">Endoscopic:</span> Even higher recurrence rate</p></div>
<div style="display:flex;align-items:flex-start;">
<div style="min-width:8px;height:8px;background:{C3};border-radius:50%;margin-top:5px;margin-right:8px;"></div>
<p style="font-size:12px;color:{C1};"><span style="font-weight:700;">2nd resection:</span> 40% likelihood</p></div>
</div>
<div style="background:{C5};padding:10px 14px;border-radius:8px;">
<p style="font-size:12px;color:{W};line-height:1.4;"><span style="font-weight:600;">3rd resection:</span> 30% likelihood</p></div>
</div>
{b(12)}
</div></body></html>'''
w(12,s12)

# === S13 - Ileal Resection Complications ===
s13=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{LB};overflow:hidden;">
{h("Management — Ileal Resection Complications")}
<div style="position:absolute;top:62px;left:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">&lt;100 cm Resected</p>
<div style="background:{W};padding:10px 14px;border-radius:8px;margin-bottom:10px;">
<p style="font-size:13px;font-weight:600;color:{C5};margin-bottom:4px;">Watery Diarrhea / Cholorrhea</p>
<p style="font-size:12px;color:{C1};line-height:1.4;">Impaired bile salt absorption → excess bile salts in colon → draw water → diarrhea</p>
</div>
<p style="font-size:14px;font-weight:600;color:{C2};margin-bottom:6px;">Treatment:</p>
<div style="display:flex;gap:6px;flex-wrap:wrap;">
<div style="background:{C2};padding:8px 16px;border-radius:6px;"><span style="font-size:11px;font-weight:600;color:{W};">Cholestyramine</span></div>
<div style="background:{C4};padding:8px 16px;border-radius:6px;"><span style="font-size:11px;font-weight:600;color:{W};">Loperamide</span></div>
</div>
</div>
<div style="position:absolute;top:62px;right:40px;width:430px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C4};margin-bottom:8px;">&gt;100 cm Resected</p>
<div style="background:{W};padding:10px 14px;border-radius:8px;margin-bottom:10px;">
<p style="font-size:13px;font-weight:600;color:{C4};margin-bottom:4px;">Steatorrhea</p>
<p style="font-size:12px;color:{C1};line-height:1.4;">Reduced mucosal surface area + bile salt deficiency → fat malabsorption</p>
</div>
<p style="font-size:14px;font-weight:600;color:{C4};margin-bottom:6px;">Treatment:</p>
<div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:10px;">
<div style="background:{C5};padding:8px 16px;border-radius:6px;"><span style="font-size:11px;font-weight:600;color:{W};">Fat Restriction</span></div>
<div style="background:{C1};padding:8px 16px;border-radius:6px;"><span style="font-size:11px;font-weight:600;color:{W};">MCT Supplements</span></div>
</div>
<div style="background:{C3};padding:8px 12px;border-radius:8px;">
<p style="font-size:12px;color:{C1};line-height:1.4;"><span style="font-weight:600;">Note:</span> Cholestyramine for &lt;100 cm; but non-specific antidiarrheals often more convenient</p></div>
</div>
{b(13)}
</div></body></html>'''
w(13,s13)

# === S14 - Prognosis, Complications & Summary ===
s14=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">{A}</head><body>
<div class="slide-content" style="background:{W};overflow:hidden;">
{h("Prognosis, Complications & Summary")}
<div style="position:absolute;top:62px;left:40px;width:420px;z-index:5;">
<p style="font-size:15px;font-weight:700;color:{C1};margin-bottom:8px;">Prognosis</p>
<div style="background:{LB};padding:10px 14px;border-radius:8px;margin-bottom:8px;">
<ul style="margin:0;padding-left:16px;">
<li style="font-size:12px;color:{C1};margin-bottom:3px;">Highly variable course</li>
<li style="font-size:12px;color:{C1};margin-bottom:3px;">10% disabled, spontaneous remission described</li>
<li style="font-size:12px;color:{C1};">Increased mortality — most in first 4-5 yrs</li>
</ul>
</div>
<p style="font-size:15px;font-weight:700;color:{C5};margin-bottom:8px;">Complications</p>
<div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px;">
<div style="background:{C5};padding:6px 14px;border-radius:6px;"><span style="font-size:11px;font-weight:600;color:{W};">Obstruction</span></div>
<div style="background:{C4};padding:6px 14px;border-radius:6px;"><span style="font-size:11px;font-weight:600;color:{W};">Perforation</span></div>
<div style="background:{C1};padding:6px 14px;border-radius:6px;"><span style="font-size:11px;font-weight:600;color:{W};">Fistula</span></div>
<div style="background:{C5};padding:6px 14px;border-radius:6px;"><span style="font-size:11px;font-weight:600;color:{W};">Malignancy</span></div>
</div>
<div style="background:{C3};padding:8px 12px;border-radius:8px;">
<p style="font-size:12px;color:{C1};"><span style="font-weight:600;">Malignancy:</span> Lower risk than UC. Same surveillance colonoscopy if &gt;⅓ colon involved.</p></div>
</div>
<div style="position:absolute;top:62px;right:40px;width:440px;z-index:5;">
<p style="font-size:16px;font-weight:700;color:{C2};margin-bottom:8px;">Key Takeaways</p>
<div style="background:rgba(42,157,143,0.1);border-radius:8px;padding:8px 14px;margin-bottom:5px;border-left:4px solid {C2};">
<p style="font-size:12px;color:{C1};line-height:1.4;"><span style="font-weight:700;">Crohn's</span> is a chronic transmural disease affecting the entire GI tract — "gum to bum"</p></div>
<div style="background:rgba(233,196,106,0.1);border-radius:8px;padding:8px 14px;margin-bottom:5px;border-left:4px solid {C3};">
<p style="font-size:12px;color:{C1};line-height:1.4;"><span style="font-weight:700;">CARD15/NOD2</span> gene mutation → 40× risk in homozygotes</p></div>
<div style="background:rgba(244,162,97,0.1);border-radius:8px;padding:8px 14px;margin-bottom:5px;border-left:4px solid {C4};">
<p style="font-size:12px;color:{C1};line-height:1.4;"><span style="font-weight:700;">Smoking</span> increases risk. <span style="font-weight:700;">Smoking cessation</span> is first-line intervention</p></div>
<div style="background:rgba(231,111,81,0.1);border-radius:8px;padding:8px 14px;margin-bottom:5px;border-left:4px solid {C5};">
<p style="font-size:12px;color:{C1};line-height:1.4;"><span style="font-weight:700;">Biologics</span> (anti-TNF, IL-12/23, integrin) revolutionized therapy</p></div>
<div style="background:rgba(38,70,83,0.1);border-radius:8px;padding:8px 14px;border-left:4px solid {C1};">
<p style="font-size:12px;color:{C1};line-height:1.4;"><span style="font-weight:700;">Surgery</span> reserved for complications. 50% clinical recurrence in 5 yrs</p></div>
</div>
{b(14)}
</div></body></html>'''
w(14,s14)

print("\n✅ All 14 slides generated!")
