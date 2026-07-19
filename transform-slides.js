#!/usr/bin/env node
/**
 * Surgery Slide → TROPICAL THEME (single-pass, in-place)
 * 
 * Transforms all 7 surgery presentations by modifying the existing HTML
 * in-place: new backgrounds, tropical colors, header bar, slide numbers.
 * Preserves 100% of content by keeping the proven absolute-positioned layout.
 * 
 * Usage: node transform-slides.js
 */

const fs = require('fs');
const path = require('path');

const ROOT = '/media/mohamed/projects4/git/raw material/GIT Presentation';

const PRES = [
  { dir: 'surgery_esophagus', count: 27, name: 'Esophagus' },
  { dir: 'surgery_stomach', count: 27, name: 'Stomach' },
  { dir: 'surgery_liver', count: 17, name: 'Liver' },
  { dir: 'surgery_intestine_peritoneum', count: 19, name: 'Intestine & Peritoneum' },
  { dir: 'surgery_oral_anal', count: 18, name: 'Oral Cavity & Anal Canal' },
  { dir: 'surgery_pancreas_appendix', count: 17, name: 'Pancreas & Appendix' },
  { dir: 'surgery_diverticula_hernias', count: 19, name: 'Diverticula & Hernias' },
];

const CSS = '<link rel="stylesheet" href="../../css/surgery-design-system.css">';
const JS  = '<script src="../../js/surgery-slide.js"></script>';
const HD_STYLE = '<style>html,body{margin:0;padding:0;width:100%;height:100%;overflow:hidden;display:flex;justify-content:center;align-items:center;background:#000;}.slide-content{width:960px;height:540px;position:relative;transform-origin:center center;}</style>';

const HDR = ['#264653','#2a9d8f','#f4a261','#e76f51'];
function hc(n){return HDR[(n-1)%HDR.length];}
function pad2(n){return String(n).padStart(2,'0');}
function pname(d){const p=PRES.find(x=>x.dir===d);return p?p.name:d;}

// ═══════════════════════════════════════════════════════════════
//  HEADER SVG (colored bar + teal underline)
// ═══════════════════════════════════════════════════════════════

function headerSVG(color) {
  return `<svg style="position:absolute;top:0;left:0;width:960px;height:540px;z-index:0;" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<rect x="0" y="0" width="960" height="540" fill="#fff"/>
<rect x="0" y="0" width="960" height="65" fill="${color}"/>
<rect x="0" y="65" width="960" height="3" fill="#2a9d8f"/>
</svg>`;
}

// ═══════════════════════════════════════════════════════════════
//  SLIDE NUMBER SVG
// ═══════════════════════════════════════════════════════════════

function slideNumSVG(n) {
  return `<svg style="position:absolute;right:32px;bottom:24px;width:40px;height:24px;z-index:100;" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="40" height="24" rx="4" fill="#2a9d8f" opacity="0.9"/>
<text x="20" y="17" text-anchor="middle" font-family="Times New Roman,serif" font-size="14" fill="#fff" font-weight="700">${pad2(n)}</text>
</svg>`;
}

// ═══════════════════════════════════════════════════════════════
//  COVER SLIDE — complete tropical redesign
// ═══════════════════════════════════════════════════════════════

function makeCover(html, dir) {
  const name = pname(dir);
  let t1='Surgery', t2='', sub='', foot='Surgery · Gastroenterology · 2026';
  const m1=html.match(/top:1[0-9]{2}px[^>]*>([^<]+)</); if(m1) t1=m1[1].trim();
  const m2=html.match(/color:#FFC107[^>]*>([^<]+)</); if(m2) t2=m2[1].trim();
  const m3=html.match(/color:#42A5F5[^>]*>([^<]+(?:<br>[^<]*)?)</);
  if(m3) sub=m3[1].replace(/<br>/g,' ');
  const m4=html.match(/color:rgba\(255,255,255,0\.6\)[^>]*>([^<]+)</); if(m4) foot=m4[1].trim();
  return `<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">${CSS}${HD_STYLE}${JS}<title>${name} — Cover</title></head><body>
<div class="slide-content cover">
<svg class="cover-svg" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<rect class="cover-svg-bg" x="0" y="0" width="960" height="540"/>
<circle class="cover-circle-1" cx="850" cy="-50" r="300"/>
<circle class="cover-circle-2" cx="700" cy="400" r="250"/>
<circle class="cover-circle-3" cx="150" cy="500" r="200"/>
<rect x="80" y="300" width="4" height="100" fill="#e9c46a" rx="2"/>
<rect x="80" y="420" width="60" height="4" fill="#e9c46a" rx="2"/>
</svg>
<div style="position:absolute;top:0;left:0;width:960px;height:540px;z-index:2;">
<p style="position:absolute;top:170px;left:110px;font-size:20px;color:#e9c46a;font-weight:400;letter-spacing:2px;opacity:0.9;">SURGERY</p>
<p style="position:absolute;top:210px;left:110px;font-size:48px;color:#fff;font-weight:700;line-height:1.2;">${t1}<br><span style="color:#e9c46a;">${t2||name}</span></p>
<p style="position:absolute;top:330px;left:110px;font-size:16px;color:rgba(255,255,255,0.7);line-height:1.6;">${sub.replace(/&/g,'&')}</p>
<div style="position:absolute;top:440px;left:110px;width:80px;height:3px;background:#f4a261;"></div>
<p style="position:absolute;top:465px;left:110px;font-size:13px;color:rgba(255,255,255,0.5);">${foot}</p>
</div></div></body></html>`;
}

// ═══════════════════════════════════════════════════════════════
//  EXTRACT CONTENT FROM 840PX AREA — handles nested divs properly
// ═══════════════════════════════════════════════════════════════

function extract840Content(html) {
  const startMarker = 'style="position:absolute;top:120px;left:60px;width:840px';
  const idx = html.indexOf(startMarker);
  if (idx === -1) return '';
  
  // Find the '>' that closes the opening tag
  const openEnd = html.indexOf('>', idx);
  if (openEnd === -1) return '';
  
  let depth = 1;
  let pos = openEnd + 1;
  let contentStart = pos;
  
  // Walk through the HTML, tracking div nesting
  while (pos < html.length && depth > 0) {
    const nextDiv = html.indexOf('<div', pos);
    const nextClose = html.indexOf('</div>', pos);
    
    // Find which comes first
    if (nextDiv !== -1 && (nextDiv < nextClose || nextClose === -1)) {
      // Check if it's an opening div (not self-closing, not closing)
      const afterDiv = html.indexOf('>', nextDiv);
      const tagContent = html.slice(nextDiv, afterDiv + 1);
      if (!tagContent.includes('/>') && !tagContent.includes('</div')) {
        depth++;
      }
      pos = afterDiv + 1;
    } else if (nextClose !== -1) {
      depth--;
      if (depth === 0) {
        // Found the matching closing div
        return html.slice(contentStart, nextClose);
      }
      pos = nextClose + 6; // '</div>'.length
    } else {
      break;
    }
  }
  return '';
}

// ═══════════════════════════════════════════════════════════════
//  SUMMARY SLIDE — tropical dark template
// ═══════════════════════════════════════════════════════════════

function makeSummary(html, dir, num) {
  const name = pname(dir);
  
  // Extract body content using div nesting tracker
  let body = extract840Content(html);
  
  // Fallback: simpler regex if extraction fails
  if (!body) {
    const m = html.match(/<div[^>]*style="position:absolute;top:1[0-9]{2}px[^>]*>([\s\S]*?)<\/div>\s*<\/div>\s*<\/body>/);
    if (m) body = m[1];
  }

  // Recolor for dark background
  body = body
    .replace(/color:#fff(?!["';\s}])/g, 'color:rgba(255,255,255,0.85)')
    .replace(/color:#fff;/g, 'color:rgba(255,255,255,0.85);')
    .replace(/color:#fff\s*}/g, 'color:rgba(255,255,255,0.85);}')
    .replace(/color:#FFC107/g, 'color:#e9c46a')
    .replace(/color:#42A5F5/g, 'color:#2a9d8f')
    .replace(/color:#FF9800/g, 'color:#f4a261')
    .replace(/color:#E53935/g, 'color:#e76f51')
    .replace(/color:rgba\(255,255,255,0\.6\)/g, 'color:rgba(255,255,255,0.4)');

  return `<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">${CSS}${HD_STYLE}${JS}<title>Summary — ${name}</title></head><body>
<div class="slide-content cover">
<svg class="cover-svg" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<rect class="cover-svg-bg" x="0" y="0" width="960" height="540"/>
<circle class="cover-circle-1" cx="800" cy="-80" r="300"/>
<circle class="cover-circle-2" cx="100" cy="600" r="250"/>
<rect x="70" y="320" width="4" height="80" fill="#e9c46a" rx="2"/>
</svg>
<div style="position:absolute;top:0;left:0;width:960px;height:540px;z-index:2;">
<p style="position:absolute;top:60px;left:70px;font-size:28px;color:#fff;font-weight:700;margin:0;">Summary — ${name}</p>
<div style="position:absolute;top:105px;left:70px;width:60px;height:3px;background:#e9c46a;"></div>
<div style="position:absolute;top:130px;left:70px;width:820px;z-index:2;line-height:1.8;">
${body}
</div>
<p style="position:absolute;top:490px;left:70px;font-size:11px;color:rgba(255,255,255,0.35);">All Details Preserved</p>
</div>${slideNumSVG(num)}</div></body></html>`;
}

// ═══════════════════════════════════════════════════════════════
//  CONTENT SLIDE — modify in-place
// ═══════════════════════════════════════════════════════════════

function modifyContent(html, dir, num) {
  const name = pname(dir);
  const col = hc(num);

  // 1. Replace head: add CSS + JS
  html = html.replace(/<link[^>]*surgery-design-system\.css[^>]*>\s*/g, '');
  html = html.replace(/<script[^>]*surgery-slide\.js[^>]*><\/script>\s*/g, '');
  html = html.replace(/<style>[\s\S]*?<\/style>/, HD_STYLE);
  html = html.replace(/<script>\s*function scaleSlide[\s\S]*?<\/script>/, '');
  html = html.replace(/(<meta name="viewport"[^>]*>)/, '$1\n' + CSS);
  html = html.replace(/(<\/head>)/, JS + '\n$1');

  // 2. Replace slide-content background: remove the dark gradient, use white
  html = html.replace(
    /<div class="slide-content" style="width:960px;height:540px;background:linear-gradient\([^)]+\);overflow:hidden;position:relative;">/,
    '<div class="slide-content content" style="background:#fff;overflow:hidden;font-family:\'Times New Roman\',serif;">'
  );

  // 3. Remove old background SVGs (decorative bars/circles)
  html = html.replace(
    /(?:<!--[^>]*-->)?\s*<svg[^>]*style="position:absolute;top:0;left:0;width:960px;height:540px;z-index:\d;"[^>]*>[\s\S]*?<rect[^>]*fill="transparent"[^>]*\/>[\s\S]*?<\/svg>/g,
    ''
  );
  // Also remove SVGs that have circles (cover decorations in non-cover slides)
  html = html.replace(
    /(?:<!--[^>]*-->)?\s*<svg[^>]*>[\s\S]*?<rect[^>]*fill="transparent"[^>]*\/>[\s\S]*?(?:<circle[^>]*>){2,}[\s\S]*?<\/svg>/g,
    ''
  );

  // 4. Remove old bottom-bar divs
  html = html.replace(/<div class="bottom-bar"><\/div>\s*/g, '');

  // 5. Add header bar SVG just inside slide-content (after opening tag)
  if (html.indexOf('fill="#fff"/><rect x="0" y="0" width="960" height="65"') === -1) {
    html = html.replace(
      /<div class="slide-content content"[^>]*>/,
      function(m) { return m + '\n' + headerSVG(col); }
    );
  }

  // 6. Remove old decorative SVGs (cover-style decorations that might remain)
  html = html.replace(/<!-- Decorative[^>]*-->[\s\S]*?<svg[^>]*>[\s\S]*?<\/svg>/g, '');

  // 7. Recolor from dark theme → tropical palette
  html = recolor(html);

  // 8. Add presentation name header (positioned over the colored bar) - AFTER recolor to protect color:#fff
  if (html.indexOf('top:14px;left:40px;z-index:2') === -1) {
    html = html.replace(
      /(<div class="slide-content content"[^>]*>[\s\S]*?)\n/,
      function(match) {
        return match + `<div style="position:absolute;top:14px;left:40px;z-index:2;"><p style="font-size:20px;font-weight:700;color:#fff;margin:0;">${name}</p></div>\n`;
      }
    );
  }

  // 9. Add slide number (if not present)
  if (html.indexOf('bottom:24px;width:40px;height:24px') === -1) {
    html = html.replace('</div>\n</body>', slideNumSVG(num) + '\n</div>\n</body>');
  }

  return html;
}

// ═══════════════════════════════════════════════════════════════
//  COLOR REMAPPING (dark theme → tropical)
// ═══════════════════════════════════════════════════════════════

function recolor(html) {
  let s = html;

  // Text colors
  s = s.replace(/color:#FFC107/g, 'color:#2a9d8f');
  s = s.replace(/color:#42A5F5/g, 'color:#264653');
  s = s.replace(/color:#FF9800/g, 'color:#f4a261');
  s = s.replace(/color:#E53935/g, 'color:#e76f51');
  s = s.replace(/color:#4CAF50/g, 'color:#2a9d8f');

  // White text on dark bg → dark text on white bg
  s = s.replace(/color:#fff(?!["';\s}])/g, 'color:#444');
  s = s.replace(/color:#fff;/g, 'color:#444;');
  s = s.replace(/color:#fff\s*}/g, 'color:#444;}');

  // Muted white text → gray
  s = s.replace(/color:rgba\(255,255,255,0\.6\)/g, 'color:#888');

  // Background semi-transparents → solid tropical tints
  s = s.replace(/background:rgba\(66,165,245,0\.1\)/g, 'background:#f0f7f6');
  s = s.replace(/background:rgba\(66,165,245,0\.2\)/g, 'background:#d4ece8');
  s = s.replace(/background:rgba\(255,152,0,0\.1\)/g, 'background:#fdf6f0');
  s = s.replace(/background:rgba\(229,57,53,0\.1\)/g, 'background:#fef0f0');
  s = s.replace(/background:rgba\(76,175,80,0\.1\)/g, 'background:#f0f7f6');
  s = s.replace(/background:rgba\(255,193,7,0\.15\)/g, 'background:#fff8f0');
  s = s.replace(/background:rgba\(0,0,0,0\.[34]\)/g, 'background:#f8f9fa');

  // Solid background colors (for bars, etc.)
  s = s.replace(/background:#42A5F5/g, 'background:#2a9d8f');

  // Border colors
  s = s.replace(/rgba\(66,165,245,0\.3\)/g, 'rgba(42,157,143,0.3)');
  s = s.replace(/rgba\(255,255,255,0\.1[5)]/g, 'rgba(0,0,0,0.06)');
  s = s.replace(/rgba\(255,255,255,0\.08\)/g, 'rgba(0,0,0,0.04)');

  // Border-left gold accent
  s = s.replace(/border-left:4px solid #FFC107/g, 'border-left:4px solid #2a9d8f');

  // Border-top colored accents
  s = s.replace(/border-top:3px solid #42A5F5/g, 'border-top:3px solid #2a9d8f');
  s = s.replace(/border-top:3px solid #FF9800/g, 'border-top:3px solid #f4a261');
  s = s.replace(/border-top:3px solid #E53935/g, 'border-top:3px solid #e76f51');

  // SVG fills (for old decoration SVGs)
  s = s.replace(/fill="#42A5F5"/g, 'fill="#2a9d8f"');
  s = s.replace(/stroke="#42A5F5"/g, 'stroke="#2a9d8f"');

  return s;
}

// ═══════════════════════════════════════════════════════════════
//  MAIN
// ═══════════════════════════════════════════════════════════════

console.log('=== Surgery → TROPICAL theme ===\n');
for (const p of PRES) {
  const d = path.join(ROOT, p.dir, 'slides');
  for (let i = 1; i <= p.count; i++) {
    const fp = path.join(d, `slide-${pad2(i)}.html`);
    if (!fs.existsSync(fp)) continue;
    let html = fs.readFileSync(fp, 'utf-8');
    if (i === 1) {
      html = makeCover(html, p.dir);
    } else if (i === p.count) {
      html = makeSummary(html, p.dir, i);
    } else {
      html = modifyContent(html, p.dir, i);
    }
    fs.writeFileSync(fp, html, 'utf-8');
  }
  console.log(`  ✓ ${p.dir} (${p.count})`);
}
console.log('\n✅ Done — 144 slides in tropical theme.');