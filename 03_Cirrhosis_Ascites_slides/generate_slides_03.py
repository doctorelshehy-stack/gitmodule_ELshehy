#!/usr/bin/env python3
"""Generate comprehensive HTML slides for Cirrhosis & Ascites (File 03)."""

import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

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

def scale_snippet():
    return '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<style>\nhtml, body { margin:0; padding:0; width:100%; height:100%; overflow:hidden; display:flex; justify-content:center; align-items:center; background:#000; }\n.slide-content { width:960px; height:540px; position:relative; transform-origin:center center; }\n</style>\n<script>\nfunction scaleSlide(){const s=document.querySelector(\'.slide-content\');if(!s)return;const sx=window.innerWidth/960;const sy=window.innerHeight/540;const sc=Math.min(sx,sy);s.style.width=\'960px\';s.style.height=\'540px\';s.style.transform=\'scale(\'+sc+\')\';s.style.transformOrigin=\'center center\';s.style.flexShrink=\'0\';}\nwindow.addEventListener(\'load\',scaleSlide);window.addEventListener(\'resize\',scaleSlide);\n</script>'

def html_head(title):
    h = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>' + title + '</title>\n'
    h += scale_snippet() + '\n</head>\n<body>\n'
    h += '<div class="slide-content" style="width:960px;height:540px;position:relative;background:' + C_BG + ';font-family:\'Times New Roman\',Times,serif;color:' + C_TEXT + ';overflow:hidden;">\n'
    h += '<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:' + C_WHITE + ';z-index:0;"></div>\n'
    h += '<svg aria-hidden="true" style="position:absolute;top:0;left:0;z-index:1;" width="960" height="540" viewBox="0 0 960 540"><rect x="0" y="0" width="960" height="6" fill="' + C_DARK + '"/></svg>\n'
    return h

def html_foot():
    return '</div>\n</body>\n</html>'

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

def bullet(text):
    return '<tr><td style="width:16px;vertical-align:top;padding:2px 4px 2px 0;"><span style="color:' + C_CORAL + ';font-size:16px;">▸</span></td>' \
           '<td style="vertical-align:top;padding:2px 0;font-size:14px;color:' + C_TEXT + ';line-height:1.5;">' + text + '</td></tr>'

def check(text):
    return '<tr><td style="width:16px;vertical-align:top;padding:2px 4px 2px 0;"><span style="color:' + C_TEAL + ';font-size:16px;">✔</span></td>' \
           '<td style="vertical-align:top;padding:2px 0;font-size:14px;color:' + C_TEXT + ';line-height:1.5;">' + text + '</td></tr>'


# ════════════════════════════════════════════════
# SLIDE 01 — COVER
# ════════════════════════════════════════════════
def slide_01():
    h = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>Cover — Cirrhosis & Ascites</title>\n'
    h += scale_snippet() + '\n</head>\n<body>\n'
    h += '<div class="slide-content" style="width:960px;height:540px;position:relative;background:' + C_BG + ';font-family:\'Times New Roman\',Times,serif;color:' + C_TEXT + ';overflow:hidden;">\n'
    h += '<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:' + C_DARK + ';z-index:0;"></div>\n'
    h += '<div style="position:absolute;top:0;left:0;width:960px;height:540px;z-index:1;background:radial-gradient(ellipse at 70% 50%, rgba(42,157,143,0.3) 0%, transparent 70%);"></div>\n'
    h += '<svg aria-hidden="true" style="position:absolute;top:0;left:0;z-index:2;" width="960" height="540" viewBox="0 0 960 540">\n'
    h += '  <rect x="0" y="0" width="12" height="540" fill="' + C_GOLD + '"/>\n'
    h += '  <circle cx="820" cy="80" r="120" fill="none" stroke="' + C_TEAL + '" stroke-width="1" opacity="0.3"/>\n'
    h += '  <circle cx="820" cy="80" r="180" fill="none" stroke="' + C_TEAL + '" stroke-width="0.5" opacity="0.15"/>\n'
    h += '  <rect x="70" y="130" width="80" height="5" rx="2.5" fill="' + C_GOLD + '"/>\n'
    h += '  <line x1="70" y1="400" x2="400" y2="400" stroke="' + C_TEAL + '" stroke-width="0.5" opacity="0.3"/>\n'
    h += '</svg>\n'
    h += '<p style="position:absolute;top:100px;left:70px;z-index:5;font-family:\'Times New Roman\',Times,serif;font-size:28px;color:' + C_GOLD + ';font-weight:400;letter-spacing:2px;opacity:0.9;">TROPICAL SUPPORT 41</p>\n'
    h += '<p style="position:absolute;top:150px;left:70px;z-index:5;font-family:\'Times New Roman\',Times,serif;font-size:48px;color:' + C_WHITE + ';font-weight:700;line-height:1.1;">Cirrhosis &amp;<br><span style="color:' + C_GOLD + ';">Ascites</span></p>\n'
    h += '<p style="position:absolute;top:280px;left:70px;z-index:5;font-family:\'Times New Roman\',Times,serif;font-size:18px;color:' + C_TEAL + ';font-weight:400;">Gastroenterology Module — Tropical Medicine</p>\n'
    h += '<p style="position:absolute;top:320px;left:70px;z-index:5;font-family:\'Times New Roman\',Times,serif;font-size:14px;color:rgba(255,255,255,0.6);">Comprehensive Review with Clinical Management Guidelines</p>\n'
    h += '<svg aria-hidden="true" style="position:absolute;bottom:40px;right:50px;z-index:5;" width="60" height="60" viewBox="0 0 60 60">\n'
    h += '  <circle cx="30" cy="30" r="28" fill="none" stroke="' + C_GOLD + '" stroke-width="1.5" opacity="0.5"/>\n'
    h += '  <text x="30" y="35" text-anchor="middle" fill="' + C_GOLD + '" font-size="14" font-weight="700" font-family:\'Times New Roman\',Times,serif;" opacity="0.8">03</text>\n'
    h += '</svg>\n'
    h += html_foot()
    return h


# ════════════════════════════════════════════════
# SLIDE 02 — TABLE OF CONTENTS
# ════════════════════════════════════════════════
def slide_02():
    items = [
        ("01", "Definition &amp; Causes of Ascites"),
        ("02", "Pathogenesis of Cirrhotic Ascites"),
        ("03", "Clinical Manifestations &amp; Grades"),
        ("04", "Investigations — Lab, Imaging &amp; Paracentesis"),
        ("05", "Diagnostic Paracentesis — SAAG &amp; Analysis"),
        ("06", "Treatment of Cirrhotic Ascites"),
        ("07", "Refractory Ascites &amp; Treatment Strategy"),
        ("08", "Differential Diagnosis of Ascites"),
        ("09", "Spontaneous Bacterial Peritonitis (SBP)"),
        ("10", "SBP — Pathogenesis, Diagnosis &amp; Treatment"),
    ]
    rows = ""
    for i, (num, title) in enumerate(items):
        rows += '<tr>\n'
        rows += '  <td style="width:40px;vertical-align:middle;text-align:center;"><span style="display:inline-block;width:28px;height:28px;line-height:28px;border-radius:50%;background:' + C_TEAL + ';color:' + C_WHITE + ';font-size:12px;font-weight:700;text-align:center;">' + num + '</span></td>\n'
        rows += '  <td style="vertical-align:middle;padding-left:10px;font-size:16px;color:' + C_DARK + ';font-weight:600;">' + title + '</td>\n'
        rows += '</tr>\n'
        if i < len(items) - 1:
            rows += '<tr><td colspan="2"><div style="height:1px;background:' + C_GOLD + ';opacity:0.3;margin:2px 0;"></div></td></tr>\n'

    return html_head("Table of Contents") + '\n' \
        + section_label("NAVIGATION") + '\n' \
        + slide_title("Table of Contents") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:100px;left:70px;right:70px;z-index:5;">\n' \
        + '  <table style="width:100%;border-collapse:collapse;">\n' + rows + '  </table>\n' \
        + '</div>\n' + page_badge(2) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 03 — DEFINITION & CAUSES
# ════════════════════════════════════════════════
def slide_03():
    return html_head("Definition & Causes of Ascites") + '\n' \
        + section_label("SECTION 01 — ASCITES BASICS") + '\n' \
        + slide_title("Definition &amp; Causes of Ascites") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="background:' + C_CARD + ';border-radius:8px;padding:12px 16px;margin-bottom:12px;border-left:4px solid ' + C_CORAL + ';">\n' \
        + '    <p style="font-size:14px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">❖ Definition</p>\n' \
        + '    <p style="font-size:13px;color:' + C_TEXT + ';margin:0;line-height:1.5;">Pathological accumulation of fluid within the peritoneal cavity results in ascites (&gt;100 cc). It is the <span style="font-weight:700;color:' + C_CORAL + ';">commonest complication</span> in patients with liver cirrhosis, develops because of severe impairment of liver function and portal hypertension, and is associated with poor prognosis.</p>\n' \
        + '  </div>\n' \
        + '  <p style="font-size:15px;font-weight:700;color:' + C_DARK + ';margin:0 0 8px 0;">❖ Causes of Ascites</p>\n' \
        + '  <p style="font-size:13px;color:#555;margin:0 0 8px 0;">The most common cause of ascites in Egypt is <span style="font-weight:700;color:' + C_DARK + ';">cirrhosis</span>, accounting for approximately 80% of cases.</p>\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-top:3px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">Portal Hypertension</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Prehepatic: PV thrombosis, splenic vein thrombosis, extrinsic compression, splanchnic AV fistula") + '\n' \
        + bullet("Hepatic: Cirrhosis, schistosomiasis, infiltrative disease, ALF, PBC, PSC, SOS") + '\n' \
        + bullet("Posthepatic: Heart failure, constrictive pericarditis, Budd-Chiari, IVC obstruction") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-top:3px solid ' + C_ORANGE + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">Non-Portal Hypertension</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Protein-poor: Nephrotic syndrome, malnutrition, protein-losing enteropathy") + '\n' \
        + bullet("Protein-rich: Malignancy, pancreatitis, TB, hemoperitoneum, chylous ascites, myxedema, perforated viscus") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(3) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 04 — PATHOGENESIS
# ════════════════════════════════════════════════
def slide_04():
    return html_head("Pathogenesis of Cirrhotic Ascites") + '\n' \
        + section_label("SECTION 01 — ASCITES BASICS") + '\n' \
        + slide_title("Pathogenesis of Cirrhotic Ascites") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:8px;padding:12px 14px;border-top:4px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:14px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">❖ Key Factors</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + check("Increased total body sodium and water") + '\n' \
        + check("Splanchnic arterial vasodilatation due to clinically significant portal hypertension (HVPG &gt; 12 mmHg)") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:8px;padding:12px 14px;border-top:4px solid ' + C_ORANGE + ';">\n' \
        + '      <p style="font-size:14px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">❖ In Cirrhosis</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + check("Hepatic dysfunction &amp; increased sinusoidal portal pressure signal the kidney to retain excess sodium and fluid") + '\n' \
        + check("Portal hypertension localizes excess fluid to the peritoneal cavity rather than the periphery") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '  <div style="margin-top:12px;background:' + C_WHITE + ';border-radius:8px;padding:12px 14px;border:1px solid #e0e0e0;border-left:4px solid ' + C_GOLD + ';">\n' \
        + '    <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">Pathophysiology Pathway</p>\n' \
        + '    <p style="font-size:12px;color:#555;margin:0;line-height:1.6;">Cirrhosis → Portal hypertension → Reduced albumin → ↓ Oncotic pressure → Reduced aldosterone metabolism → ↑ Aldosterone → Activation of RAAS → Underfilling of circulation → Reduced renal blood flow → Splanchnic vasodilatation → Lymph formation exceeds lymph return → Salt and water retention → <span style="font-weight:700;color:' + C_CORAL + ';">Ascites</span></p>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(4) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 05 — CLINICAL MANIFESTATIONS & GRADES
# ════════════════════════════════════════════════
def slide_05():
    return html_head("Clinical Manifestations & Grades of Ascites") + '\n' \
        + section_label("SECTION 02 — CLINICAL PRESENTATION") + '\n' \
        + slide_title("Clinical Manifestations &amp; Grades of Ascites") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:8px;padding:10px 12px;border-top:4px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">❖ Symptoms</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Progressive abdominal distension") + '\n' \
        + bullet("Abdominal discomfort, shortness of breath") + '\n' \
        + bullet("Weight gain") + '\n' \
        + bullet("Cirrhosis: confusion, GI bleeding (decompensation)") + '\n' \
        + bullet("Malignant: weight loss") + '\n' \
        + bullet("Heart failure: dyspnea, orthopnea, peripheral edema") + '\n' \
        + bullet("Chylous: diarrhea, steatorrhea, malnutrition, nausea, fever, night sweats") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:8px;padding:10px 12px;border-top:4px solid ' + C_ORANGE + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">❖ Signs</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Flank dullness, shifting dullness") + '\n' \
        + bullet("Stigmata of liver cell failure: spider angioma, palmar erythema, abdominal wall collaterals, jaundice, muscle wasting, gynecomastia, leukonychia, parotid enlargement") + '\n' \
        + bullet("Heart failure: JVD, pulmonary congestion, peripheral edema") + '\n' \
        + bullet("Chylous: LE edema, lymphadenopathy, cachexia, abdominal masses") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '  <div style="margin-top:10px;background:#fff3e0;border-radius:8px;padding:10px 14px;border:1px solid ' + C_GOLD + ';">\n' \
        + '    <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">❖ Grades of Ascites (International Ascites Club)</p>\n' \
        + '    <table style="border-collapse:collapse;font-size:13px;">\n' \
        + '      <tr><td style="padding:2px 8px;font-weight:700;color:' + C_CORAL + ';">Grade 1</td><td style="padding:2px 0;">Mild — detectable only by ultrasound</td></tr>\n' \
        + '      <tr><td style="padding:2px 8px;font-weight:700;color:' + C_ORANGE + ';">Grade 2</td><td style="padding:2px 0;">Moderate — moderate symmetrical abdominal distension</td></tr>\n' \
        + '      <tr><td style="padding:2px 8px;font-weight:700;color:' + C_CORAL + ';">Grade 3</td><td style="padding:2px 0;">Large / gross — marked abdominal distension</td></tr>\n' \
        + '    </table>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(5) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 06 — INVESTIGATIONS: LAB & IMAGING
# ════════════════════════════════════════════════
def slide_06():
    return html_head("Investigations — Laboratory & Imaging") + '\n' \
        + section_label("SECTION 03 — INVESTIGATIONS") + '\n' \
        + slide_title("Investigations — Laboratory &amp; Imaging") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:8px;padding:12px 14px;border-top:4px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:14px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">1) Laboratory Tests</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Abnormalities related to underlying cause") + '\n' \
        + bullet("Cirrhosis / Heart failure: abnormal LFTs, renal failure") + '\n' \
        + bullet("Cirrhosis: elevated INR, hypoalbuminemia, thrombocytopenia, anemia, leukopenia") + '\n' \
        + bullet("Chylous ascites: hypoalbuminemia, decreased gamma globulin, lymphopenia") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:8px;padding:12px 14px;border-top:4px solid ' + C_ORANGE + ';">\n' \
        + '      <p style="font-size:14px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">2) Imaging Studies</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Ultrasound: most cost-effective modality") + '\n' \
        + bullet("Cirrhosis: nodular liver on US, CT, or MRI") + '\n' \
        + bullet("Portal hypertension: PV dilation ≥13 mm, splenomegaly &gt;12 cm") + '\n' \
        + bullet("HCC screening: US → CT/MRI for further evaluation") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '  <div style="margin-top:10px;background:#fff3e0;border-radius:8px;padding:10px 14px;border:1px solid ' + C_GOLD + ';">\n' \
        + '    <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">Key Point</p>\n' \
        + '    <p style="font-size:12px;color:#555;margin:0;line-height:1.4;">Abdominal paracentesis is central to determining the cause of ascites and is indicated for ALL patients with new onset ascites.</p>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(6) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 07 — DIAGNOSTIC PARACENTESIS: APPEARANCE
# ════════════════════════════════════════════════
def slide_07():
    return html_head("Diagnostic Paracentesis — Appearance & Routine Tests") + '\n' \
        + section_label("SECTION 03 — INVESTIGATIONS") + '\n' \
        + slide_title("Diagnostic Paracentesis — Appearance &amp; Routine Tests") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:8px;padding:10px 12px;border-top:4px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">(a) Appearance of Ascitic Fluid</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("<span style='font-weight:600;'>Clear</span> — Uncomplicated cirrhotic ascites") + '\n' \
        + bullet("<span style='font-weight:600;'>Turbid / Cloudy</span> — Spontaneously infected fluid") + '\n' \
        + bullet("<span style='font-weight:600;'>Milky</span> — Chylous ascites (high triglycerides)") + '\n' \
        + bullet("<span style='font-weight:600;'>Pink / Bloody</span> — Ruptured HCC") + '\n' \
        + bullet("<span style='font-weight:600;'>Brown</span> — Deep jaundice (bilirubin ~40% of serum)") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:8px;padding:10px 12px;border-top:4px solid ' + C_ORANGE + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">Routine Ascitic Fluid Analysis</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Albumin") + '\n' \
        + bullet("Protein") + '\n' \
        + bullet("PMN cell count") + '\n' \
        + bullet("Cultures") + '\n' \
        + bullet("Optional: Glucose, LDH, Amylase, RBC count, TB smear/culture, Cytology, Triglycerides") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(7) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 08 — SAAG, CELL COUNT, PROTEIN
# ════════════════════════════════════════════════
def slide_08():
    return html_head("Diagnostic Paracentesis — SAAG, Cell Count & Protein") + '\n' \
        + section_label("SECTION 03 — INVESTIGATIONS") + '\n' \
        + slide_title("SAAG, Cell Count &amp; Total Protein") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;">\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:8px;padding:10px 12px;border:1px solid #e0e0e0;border-top:4px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">(b) SAAG</p>\n' \
        + '      <p style="font-size:11px;color:#555;margin:0 0 4px 0;">Serum-to-Ascites Albumin Gradient</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + check("Calculated: serum albumin − ascitic fluid albumin (same day)") + '\n' \
        + check("≥1.1 g/dL → portal hypertension (97% accuracy)") + '\n' \
        + check("&lt;1.1 g/dL → no portal hypertension") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:8px;padding:10px 12px;border:1px solid #e0e0e0;border-top:4px solid ' + C_ORANGE + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">(c) Cell Count &amp; Differential</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Order on EVERY specimen including therapeutic paracentesis") + '\n' \
        + bullet("Neutrophil count &gt;250 cells/mm³ → SBP") + '\n' \
        + bullet("Evaluates for infection") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:8px;padding:10px 12px;border:1px solid #e0e0e0;border-top:4px solid ' + C_CORAL + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">(d) Total Protein</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Exudate: ≥2.5–3 g/dL") + '\n' \
        + bullet("Transudate: &lt;2.5–3 g/dL") + '\n' \
        + '      </table>\n' \
        + '      <p style="font-size:11px;color:#555;margin:4px 0 0 0;">Helps differentiate causes of ascites</p>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '  <div style="margin-top:10px;background:#fff3e0;border-radius:8px;padding:8px 12px;border:1px solid ' + C_GOLD + ';">\n' \
        + '    <p style="font-size:12px;color:' + C_DARK + ';margin:0;line-height:1.4;"><span style="font-weight:700;">SAAG Key:</span> High gradient (≥1.1) = portal hypertension. Low gradient (&lt;1.1) = other causes (malignancy, TB, pancreatitis, nephrotic syndrome).</p>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(8) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 09 — TB TESTS & CYTOLOGY
# ════════════════════════════════════════════════
def slide_09():
    return html_head("Paracentesis — TB Tests & Cytology") + '\n' \
        + section_label("SECTION 03 — INVESTIGATIONS") + '\n' \
        + slide_title("TB Peritonitis Tests &amp; Cytology") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:8px;padding:12px 14px;border-top:4px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:14px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">(e) Tests for Tuberculous Peritonitis</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("1) Direct smear and Mycobacterial culture") + '\n' \
        + bullet("2) Peritoneoscopy with biopsy culture → sensitivity ~100% (Gold standard). Fluid &amp; tissue can be sent for TB PCR") + '\n' \
        + bullet("3) Adenosine deaminase (ADA) &gt;39 U/L") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:8px;padding:12px 14px;border-top:4px solid ' + C_ORANGE + ';">\n' \
        + '      <p style="font-size:14px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">(f) Cytology</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Almost 100% of patients with peritoneal carcinomatosis have positive ascitic fluid cytology") + '\n' \
        + bullet("Due to viable malignant cells exfoliating into the ascitic fluid") + '\n' \
        + '      </table>\n' \
        + '      <p style="font-size:12px;color:#555;margin:6px 0 0 0;line-height:1.4;">Cytology is 60–90% accurate in malignant ascites. Immuno-cytochemical techniques with monoclonal/polyclonal antibodies against tumor markers may help differentiate malignant cells from atypical mesothelial cells.</p>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(9) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 10 — TREATMENT OF CIRRHOTIC ASCITES
# ════════════════════════════════════════════════
def slide_10():
    return html_head("Treatment of Cirrhotic Ascites") + '\n' \
        + section_label("SECTION 04 — TREATMENT") + '\n' \
        + slide_title("Treatment of Cirrhotic Ascites") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:8px;padding:10px 12px;border-top:4px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">❖ Goals</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + check("Minimize ascitic volume and peripheral edema") + '\n' \
        + check("Avoid intravascular volume depletion") + '\n' \
        + '      </table>\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:8px 0 4px 0;">❖ Benefits</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + check("Patient comfort") + '\n' \
        + check("Reduced risk of hernia formation") + '\n' \
        + check("Possible reduction in SBP (increased opsonins)") + '\n' \
        + check("Improved nutrition") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:8px;padding:10px 12px;border-top:4px solid ' + C_ORANGE + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">❖ Treatment Measures</p>\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_CORAL + ';margin:0 0 4px 0;">1) Bed Rest &amp; Sodium Restriction</p>\n' \
        + '      <p style="font-size:12px;color:#555;margin:0 0 8px 4px;">Sodium intake restricted to 5–6 g/day</p>\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_CORAL + ';margin:0 0 4px 0;">2) Diuretic Therapy</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Start with <span style=\'font-weight:600;\'>potassium-sparing diuretics</span> (spironolactone 100 mg → up to 400 mg/day)") + '\n' \
        + bullet("Then combination with <span style=\'font-weight:600;\'>loop diuretics</span> (frusemide 40 mg → up to 160 mg/day)") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(10) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 11 — TREATMENT STRATEGY GRADE 2 & 3
# ════════════════════════════════════════════════
def slide_11():
    return html_head("Treatment Strategy — Grade 2 & 3 Ascites") + '\n' \
        + section_label("SECTION 04 — TREATMENT") + '\n' \
        + slide_title("Treatment Strategy for Grade 2 &amp; 3 Ascites") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <table style="width:100%;border-collapse:collapse;font-size:13px;font-family:\'Times New Roman\',Times,serif;">\n' \
        + '    <thead>\n' \
        + '      <tr>\n' \
        + '        <th style="width:50%;padding:8px 12px;text-align:center;background:' + C_TEAL + ';color:' + C_WHITE + ';border:1px solid ' + C_TEAL + ';">Grade 2 Ascites (Moderate)</th>\n' \
        + '        <th style="width:50%;padding:8px 12px;text-align:center;background:' + C_CORAL + ';color:' + C_WHITE + ';border:1px solid ' + C_CORAL + ';">Grade 3 Ascites (Large)</th>\n' \
        + '      </tr>\n' \
        + '    </thead>\n' \
        + '    <tbody>\n' \
        + '      <tr style="background:' + C_WHITE + ';">\n' \
        + '        <td style="padding:8px 12px;border:1px solid #ccc;vertical-align:top;">\n' \
        + '          <p style="margin:0 0 4px 0;font-weight:600;color:' + C_DARK + ';">Salt Restriction + Diuretics</p>\n' \
        + '          <p style="margin:0 0 2px 0;font-size:12px;">Spironolactone 50–100 mg/day</p>\n' \
        + '          <p style="margin:0 0 2px 0;font-size:12px;">Torasemide 20 mg or Frusemide 40 mg</p>\n' \
        + '          <p style="margin:0;font-size:12px;">Increase dose as needed until disappearance of ascites</p>\n' \
        + '        </td>\n' \
        + '        <td style="padding:8px 12px;border:1px solid #ccc;vertical-align:top;">\n' \
        + '          <p style="margin:0 0 4px 0;font-weight:600;color:' + C_DARK + ';">Large Volume Paracentesis</p>\n' \
        + '          <p style="margin:0 0 2px 0;font-size:12px;">&lt;5 L → Albumin or synthetic plasma expanders</p>\n' \
        + '          <p style="margin:0 0 2px 0;font-size:12px;">&gt;5 L → Albumin</p>\n' \
        + '          <p style="margin:0;font-size:12px;">Then salt restriction + diuretic therapy as tolerated</p>\n' \
        + '        </td>\n' \
        + '      </tr>\n' \
        + '      <tr style="background:' + C_CARD + ';">\n' \
        + '        <td colspan="2" style="padding:8px 12px;border:1px solid #ccc;text-align:center;">\n' \
        + '          <span style="font-weight:700;color:' + C_DARK + ';">Maintenance Therapy:</span> Continue salt restriction. Reduce diuretics as needed.\n' \
        + '        </td>\n' \
        + '      </tr>\n' \
        + '    </tbody>\n' \
        + '  </table>\n' \
        + '  <div style="margin-top:10px;background:#fff3e0;border-radius:8px;padding:8px 12px;border:1px solid ' + C_GOLD + ';">\n' \
        + '    <p style="font-size:12px;color:' + C_DARK + ';margin:0;line-height:1.4;"><span style="font-weight:700;">Key Principle:</span> Grade 2 → medical therapy. Grade 3 → large volume paracentesis first, then medical therapy. Always monitor for complications including HRS and SBP.</p>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(11) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 12 — REFRACTORY ASCITES
# ════════════════════════════════════════════════
def slide_12():
    return html_head("Treatment of Refractory Ascites") + '\n' \
        + section_label("SECTION 04 — TREATMENT") + '\n' \
        + slide_title("Treatment of Refractory Ascites") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="background:' + C_CARD + ';border-radius:8px;padding:10px 14px;margin-bottom:12px;border-left:4px solid ' + C_CORAL + ';">\n' \
        + '    <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">❖ Definition of Refractory Ascites</p>\n' \
        + '    <p style="font-size:12px;color:#555;margin:0;line-height:1.4;">Ascites not responding to intensive diuretic therapy (spironolactone 400 mg/day + furosemide 160 mg/day) for at least 1 week <span style="font-weight:700;">AND</span> on a salt-restricted diet of less than 90 mmol/day.</p>\n' \
        + '  </div>\n' \
        + '  <p style="font-size:14px;font-weight:700;color:' + C_DARK + ';margin:0 0 8px 0;">❖ Therapeutic Options</p>\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:10px 12px;border:1px solid #e0e0e0;border-left:4px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">1) Repeated Therapeutic Paracentesis</p>\n' \
        + '      <p style="font-size:12px;color:#555;margin:0;line-height:1.4;">Large volume paracentesis with volume expansion using albumin 1 g/kg/day</p>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:10px 12px;border:1px solid #e0e0e0;border-left:4px solid ' + C_ORANGE + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">2) TIPS</p>\n' \
        + '      <p style="font-size:12px;color:#555;margin:0;line-height:1.4;">Transjugular Intrahepatic Portosystemic Shunt — reduces portal pressure</p>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:10px 12px;border:1px solid #e0e0e0;border-left:4px solid ' + C_GOLD + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">3) Peritoneo-venous (Le Veen) Shunt</p>\n' \
        + '      <p style="font-size:12px;color:#555;margin:0;line-height:1.4;">Shunts ascitic fluid from peritoneum to venous system. Risk of infection (~20%).</p>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:10px 12px;border:1px solid #e0e0e0;border-left:4px solid ' + C_CORAL + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">4) Liver Transplantation</p>\n' \
        + '      <p style="font-size:12px;color:#555;margin:0;line-height:1.4;">Definitive treatment for end-stage liver disease with refractory ascites</p>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(12) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 13 — DIFFERENTIAL DIAGNOSIS: MALIGNANT
# ════════════════════════════════════════════════
def slide_13():
    return html_head("Differential Diagnosis — Malignant Ascites & Post-sinusoidal") + '\n' \
        + section_label("SECTION 05 — DIFFERENTIAL DIAGNOSIS") + '\n' \
        + slide_title("Differential Diagnosis of Ascites") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:8px;padding:10px 12px;border:1px solid #e0e0e0;border-top:4px solid ' + C_CORAL + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">1) Malignant Ascites</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Macroscopically bloody in only 10% of patients") + '\n' \
        + bullet("Total protein &gt;3 g/dL") + '\n' \
        + bullet("SAAG &lt;1.1 (low gradient)") + '\n' \
        + bullet("High LDH and cholesterol") + '\n' \
        + bullet("Cytology: 60–90% accurate") + '\n' \
        + bullet("Immuno-cytochemical techniques help differentiate malignant vs mesothelial cells") + '\n' \
        + bullet("Laparoscopic biopsy may be needed if cytology negative") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:8px;padding:10px 12px;border:1px solid #e0e0e0;border-top:4px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">2) Post-sinusoidal Portal Hypertension</p>\n' \
        + '      <p style="font-size:11px;color:#555;margin:0 0 4px 0;">Causes: CHF, constrictive pericarditis, IVC obstruction, Budd-Chiari syndrome</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("SAAG &lt;1.1 (low gradient)") + '\n' \
        + bullet("LDH and cholesterol not increased") + '\n' \
        + bullet("Heart failure / Budd-Chiari: usually easy clinical diagnosis") + '\n' \
        + bullet("Constrictive pericarditis: often lacks CHF symptoms") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(13) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 14 — DIFFERENTIAL: CHYLOUS, BILIARY, HYDROTHORAX
# ════════════════════════════════════════════════
def slide_14():
    return html_head("Differential Diagnosis — Chylous, Biliary, Pancreatic & Hydrothorax") + '\n' \
        + section_label("SECTION 05 — DIFFERENTIAL DIAGNOSIS") + '\n' \
        + slide_title("Other Types of Ascites") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-top:3px solid ' + C_GOLD + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">3) Chylous Ascites</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Macroscopically turbid / milky (high triglycerides)") + '\n' \
        + bullet("Causes: lymphangiectasia, lymphoma, cirrhosis (infrequent)") + '\n' \
        + bullet("Other: retroperitoneal surgery, pancreatitis, sarcoidosis, TB, abdominal trauma") + '\n' \
        + bullet("Mechanism: hydrostatic hypertension → spontaneous lymphatic rupture") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-top:3px solid ' + C_CORAL + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">4) Biliary &amp; Pancreatic Ascites</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Green ascitic fluid (bilirubin &gt;plasma)") + '\n' \
        + bullet("Suspected after liver biopsy or biliary surgery") + '\n' \
        + bullet("Exudate (protein &gt;3 g/dL)") + '\n' \
        + bullet("High pancreatic enzymes → chronic pancreatitis") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-top:3px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">5) Cirrhotic Hydrothorax</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("5% of cirrhosis patients") + '\n' \
        + bullet("Pleural effusion (usually right-sided) without pulmonary/pleural disease") + '\n' \
        + bullet("Mechanism: ascites passes through diaphragmatic defects into pleural space") + '\n' \
        + bullet("Risk of spontaneous bacterial empyema") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:#fff3e0;border-radius:6px;padding:8px 10px;border:1px solid ' + C_GOLD + ';">\n' \
        + '      <p style="font-size:11px;color:' + C_DARK + ';margin:0;line-height:1.4;"><span style="font-weight:700;">Key:</span> SAAG ≥1.1 = portal hypertension. SAAG &lt;1.1 = malignancy, TB, pancreatitis, nephrotic syndrome. Total protein helps classify exudate vs transudate.</p>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(14) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 15 — SBP: DEFINITION & EPIDEMIOLOGY
# ════════════════════════════════════════════════
def slide_15():
    return html_head("Spontaneous Bacterial Peritonitis — Definition & Pathogenesis") + '\n' \
        + section_label("SECTION 06 — SPONTANEOUS BACTERIAL PERITONITIS") + '\n' \
        + slide_title("SBP — Definition &amp; Pathogenesis") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="background:' + C_CARD + ';border-radius:8px;padding:10px 14px;margin-bottom:10px;border-left:4px solid ' + C_CORAL + ';">\n' \
        + '    <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">❖ Definition</p>\n' \
        + '    <p style="font-size:12px;color:#555;margin:0;line-height:1.5;">New onset of fever, abdominal pain, confusion, or other signs/symptoms of infection in a cirrhotic patient should prompt evaluation of ascitic fluid for SBP. Develops in <span style="font-weight:700;color:' + C_CORAL + ';">8%</span> of cirrhotic patients with ascites. Usually <span style="font-weight:700;">mono-microbial</span> and <span style="font-weight:700;">Gram-negative</span>. Patients are at particular risk of renal complications (HRS).</p>\n' \
        + '  </div>\n' \
        + '  <p style="font-size:14px;font-weight:700;color:' + C_DARK + ';margin:0 0 8px 0;">❖ Pathogenesis</p>\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-top:3px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">Bacterial Translocation</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Enteric bacteria cross the GI mucosa → colonize mesenteric lymph nodes → bloodstream via intestinal lymphatics") + '\n' \
        + bullet("Most common: Gram-negative aerobes, E. coli (~80%)") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-top:3px solid ' + C_ORANGE + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">Depression of RES</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Hepatic reticulo-endothelial system depression allows free passage of microorganisms from intestinal lumen → systemic circulation → bacteremia") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-top:3px solid ' + C_GOLD + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">Decreased Opsonic Activity</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Inverse correlation between ascitic fluid opsonic activity &amp; SBP risk") + '\n' \
        + bullet("Protein &lt;10 g/L → higher SBP frequency") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-top:3px solid ' + C_CORAL + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">Iatrogenic Factors</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Diagnostic/therapeutic maneuvers alter natural defense barriers") + '\n' \
        + bullet("Sclerotherapy → bacteremia 5–30%") + '\n' \
        + bullet("Le Veen shunt → infection ~20%") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '  <div style="margin-top:8px;background:#fff3e0;border-radius:8px;padding:8px 12px;border:1px solid ' + C_GOLD + ';">\n' \
        + '    <p style="font-size:11px;color:' + C_DARK + ';margin:0;line-height:1.4;"><span style="font-weight:700;">Pathway:</span> Cirrhosis → ↓ Immunity → Bacterial Translocation → Transient Bacteremia → ↓ C3/C4 → Prolonged Bacteremia → Ascites Colonization → <span style="font-weight:700;color:' + C_CORAL + ';">SBP</span></p>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(15) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 16 — SBP: DIAGNOSIS
# ════════════════════════════════════════════════
def slide_16():
    return html_head("SBP — Diagnosis") + '\n' \
        + section_label("SECTION 06 — SPONTANEOUS BACTERIAL PERITONITIS") + '\n' \
        + slide_title("SBP — Diagnosis") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="background:' + C_CARD + ';border-radius:8px;padding:10px 14px;margin-bottom:10px;border-left:4px solid ' + C_TEAL + ';">\n' \
        + '    <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">Ascitic Fluid Analysis</p>\n' \
        + '    <p style="font-size:12px;color:#555;margin:0;line-height:1.4;">Diagnosis through cell count/differential and fluid culture.</p>\n' \
        + '  </div>\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-top:3px solid ' + C_CORAL + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">SBP</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Neutrophil count &gt;250 cells/mm³") + '\n' \
        + bullet("Positive mono-microbial ascitic culture") + '\n' \
        + bullet("Mostly Gram-negative (E. coli ~80%)") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-top:3px solid ' + C_ORANGE + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">NNBA</p>\n' \
        + '      <p style="font-size:11px;color:#555;margin:0 0 4px 0;">Non-Neutrocytic Bacterascites</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Cell count &lt;250 cells/mm³") + '\n' \
        + bullet("Positive ascitic culture") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-top:3px solid ' + C_GOLD + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">CNNA</p>\n' \
        + '      <p style="font-size:11px;color:#555;margin:0 0 4px 0;">Culture-Negative Neutrocytic Ascites</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Neutrophil count &gt;250 cells/mm³") + '\n' \
        + bullet("Negative ascitic culture") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-top:3px solid ' + C_CORAL + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">Secondary Peritonitis</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Neutrophil count &gt;250 cells/mm³") + '\n' \
        + bullet("Positive POLY-microbial ascitic culture") + '\n' \
        + bullet("Suggests bowel perforation") + '\n' \
        + bullet("Check LDH, glucose, total protein to differentiate") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '  <div style="margin-top:8px;background:#fff3e0;border-radius:8px;padding:8px 12px;border:1px solid ' + C_GOLD + ';">\n' \
        + '    <p style="font-size:11px;color:' + C_DARK + ';margin:0;line-height:1.4;"><span style="font-weight:700;">Key:</span> Always measure LDH, glucose, and total protein in ascitic fluid to differentiate SBP from secondary peritonitis. TIPS is NOT associated with significant bacterial infection.</p>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(16) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 17 — SBP: TREATMENT
# ════════════════════════════════════════════════
def slide_17():
    return html_head("SBP — Treatment") + '\n' \
        + section_label("SECTION 06 — SPONTANEOUS BACTERIAL PERITONITIS") + '\n' \
        + slide_title("SBP — Treatment") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:8px;padding:12px 14px;border-top:4px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:14px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">❖ Antibiotic Therapy</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Five days of parenteral <span style=\'font-weight:600;\'>third-generation cephalosporin</span>") + '\n' \
        + bullet("Cefotaxime 1–2 g / 12 h × 5 days — usually effective") + '\n' \
        + bullet("IV Ciprofloxacin followed by oral treatment is also effective") + '\n' \
        + bullet("Review choice empirically once culture &amp; sensitivity results known") + '\n' \
        + bullet("Repeat paracentesis NOT needed unless clinical indication of failing treatment") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:8px;padding:12px 14px;border-top:4px solid ' + C_CORAL + ';">\n' \
        + '      <p style="font-size:14px;font-weight:700;color:' + C_DARK + ';margin:0 0 6px 0;">❖ IV Albumin</p>\n' \
        + '      <table style="border-collapse:collapse;">\n' \
        + bullet("Given the risks of renal dysfunction (HRS) due to altered effective circulating volume") + '\n' \
        + bullet("IV albumin maintains oncotic tone and renal perfusion") + '\n' \
        + bullet("<span style=\'font-weight:600;\'>Dose:</span> 1.5 g/kg on day 1 + 1 g/kg on day 3") + '\n' \
        + bullet("Yields renal protection and improved mortality") + '\n' \
        + '      </table>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(17) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 18 — SBP: PROPHYLAXIS
# ════════════════════════════════════════════════
def slide_18():
    return html_head("SBP — Antibiotic Prophylaxis") + '\n' \
        + section_label("SECTION 06 — SPONTANEOUS BACTERIAL PERITONITIS") + '\n' \
        + slide_title("SBP — Antibiotic Prophylaxis") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <p style="font-size:14px;font-weight:700;color:' + C_CORAL + ';margin:0 0 8px 0;">❖ Indications of Antibiotic Prophylaxis for SBP</p>\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-left:4px solid ' + C_CORAL + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">A. Prior History of SBP</p>\n' \
        + '      <p style="font-size:11px;color:#555;margin:0;">Secondary prophylaxis after an episode of SBP</p>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_WHITE + ';border-radius:6px;padding:8px 10px;border:1px solid #e0e0e0;border-left:4px solid ' + C_CORAL + ';">\n' \
        + '      <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">B. Acute GI Bleeding</p>\n' \
        + '      <p style="font-size:11px;color:#555;margin:0;">Prophylaxis during acute variceal bleeding episodes</p>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '  <div style="margin-top:8px;background:#fff3e0;border-radius:8px;padding:10px 14px;border:1px solid ' + C_GOLD + ';">\n' \
        + '    <p style="font-size:12px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">C. Non-SBP Patients at High Risk</p>\n' \
        + '    <p style="font-size:11px;color:#555;margin:0 0 4px 0;">If ascitic fluid total protein &lt;1.5 g/dL + ≥2 of the following:</p>\n' \
        + '    <table style="border-collapse:collapse;font-size:12px;">\n' \
        + '      <tr><td style="padding:1px 12px;">▸ Serum creatinine ≥1.2 mg/dL</td><td style="padding:1px 12px;">▸ BUN ≥25 mg/dL</td></tr>\n' \
        + '      <tr><td style="padding:1px 12px;">▸ Serum sodium ≤130 mEq/L</td><td style="padding:1px 12px;">▸ Child\'s ≥9 (bilirubin ≥3 mg/dL)</td></tr>\n' \
        + '    </table>\n' \
        + '  </div>\n' \
        + '  <div style="margin-top:8px;background:' + C_CARD + ';border-radius:8px;padding:10px 14px;border-top:4px solid ' + C_TEAL + ';">\n' \
        + '    <p style="font-size:13px;font-weight:700;color:' + C_DARK + ';margin:0 0 4px 0;">Recommended Regimens for 1° &amp; 2° SBP Prophylaxis (Oral)</p>\n' \
        + '    <table style="border-collapse:collapse;">\n' \
        + '      <tr><td style="padding:2px 8px;">a)</td><td style="padding:2px 0;">Norfloxacin 400 mg/day</td></tr>\n' \
        + '      <tr><td style="padding:2px 8px;">b)</td><td style="padding:2px 0;">Ciprofloxacin 500 mg daily</td></tr>\n' \
        + '      <tr><td style="padding:2px 8px;">c)</td><td style="padding:2px 0;">Co-trimoxazole one DS tablet daily</td></tr>\n' \
        + '    </table>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(18) + '\n' + html_foot()


# ════════════════════════════════════════════════
# SLIDE 19 — SUMMARY
# ════════════════════════════════════════════════
def slide_19():
    return html_head("Summary — Key Takeaways") + '\n' \
        + section_label("SECTION 07 — SUMMARY") + '\n' \
        + slide_title("Summary — Key Takeaways") + '\n' \
        + gold_sep() + '\n' \
        + '<div style="position:absolute;top:106px;left:60px;right:60px;z-index:5;bottom:60px;overflow-y:auto;">\n' \
        + '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:6px;padding:8px 12px;border-left:4px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:11px;font-weight:700;color:' + C_DARK + ';margin:0 0 2px 0;">Ascites Definition</p>\n' \
        + '      <p style="font-size:10px;color:#555;margin:0;line-height:1.4;">Fluid &gt;100 cc in peritoneal cavity. Commonest complication of cirrhosis (80% of cases in Egypt).</p>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:6px;padding:8px 12px;border-left:4px solid ' + C_ORANGE + ';">\n' \
        + '      <p style="font-size:11px;font-weight:700;color:' + C_DARK + ';margin:0 0 2px 0;">Pathogenesis</p>\n' \
        + '      <p style="font-size:10px;color:#555;margin:0;line-height:1.4;">Portal hypertension + splanchnic vasodilatation → RAAS activation → Na/H₂O retention → ascites.</p>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:6px;padding:8px 12px;border-left:4px solid ' + C_CORAL + ';">\n' \
        + '      <p style="font-size:11px;font-weight:700;color:' + C_DARK + ';margin:0 0 2px 0;">SAAG</p>\n' \
        + '      <p style="font-size:10px;color:#555;margin:0;line-height:1.4;">≥1.1 = portal hypertension (97% accuracy). &lt;1.1 = other causes (malignancy, TB, pancreatitis).</p>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:6px;padding:8px 12px;border-left:4px solid ' + C_GOLD + ';">\n' \
        + '      <p style="font-size:11px;font-weight:700;color:' + C_DARK + ';margin:0 0 2px 0;">Treatment</p>\n' \
        + '      <p style="font-size:10px;color:#555;margin:0;line-height:1.4;">Grade 1–2: Salt restriction + spironolactone → frusemide. Grade 3: LVP + albumin. Refractory: TIPS, shunt, transplant.</p>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:6px;padding:8px 12px;border-left:4px solid ' + C_TEAL + ';">\n' \
        + '      <p style="font-size:11px;font-weight:700;color:' + C_DARK + ';margin:0 0 2px 0;">SBP Diagnosis</p>\n' \
        + '      <p style="font-size:10px;color:#555;margin:0;line-height:1.4;">PMN &gt;250/mm³ + mono-microbial culture (Gram-negative). NNBA and CNNA variants exist.</p>\n' \
        + '    </div>\n' \
        + '    <div style="background:' + C_CARD + ';border-radius:6px;padding:8px 12px;border-left:4px solid ' + C_CORAL + ';">\n' \
        + '      <p style="font-size:11px;font-weight:700;color:' + C_DARK + ';margin:0 0 2px 0;">SBP Treatment</p>\n' \
        + '      <p style="font-size:10px;color:#555;margin:0;line-height:1.4;">Cefotaxime 1–2 g/12h × 5d + IV albumin (1.5 → 1 g/kg). Prophylaxis: norfloxacin or ciprofloxacin.</p>\n' \
        + '    </div>\n' \
        + '  </div>\n' \
        + '  <div style="margin-top:8px;background:' + C_DARK + ';border-radius:8px;padding:10px 16px;text-align:center;">\n' \
        + '    <p style="font-size:14px;color:' + C_GOLD + ';font-weight:700;margin:0;">Cirrhosis &amp; Ascites — Complete Review</p>\n' \
        + '  </div>\n' \
        + '</div>\n' + page_badge(19) + '\n' + html_foot()


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
    ("slide-19.html", slide_19),
]

for fname, func in slides:
    path = os.path.join(OUT_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(func())
    print("OK " + fname)

print("\nAll " + str(len(slides)) + " slides generated in " + OUT_DIR)
