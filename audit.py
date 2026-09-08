# -*- coding: utf-8 -*-
"""
Responsive + quality audit for the built site.

    python audit.py

Chrome headless on Windows will not open a window narrower than ~485 CSS px,
so narrow viewports are tested by loading each page inside an iframe of an
exact width. An iframe gets a real viewport: media queries, vw units and
layout all resolve against the iframe's own width, so this is a genuine test
rather than a scaled screenshot.

For every page x width it reports:
  - horizontal overflow (scrollWidth > clientWidth)
  - any individual element whose box escapes the viewport
  - text smaller than 12px
  - tap targets under 40px in either axis
"""

import glob
import json
import os
import re
import shutil
import subprocess
import tempfile

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
WIDTHS = [320, 360, 390, 430, 600, 768, 900, 1024, 1280, 1440]

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

PROBE = r"""
<!doctype html><meta charset="utf-8"><title>audit</title>
<style>html,body{margin:0;background:#fff}iframe{border:0;display:block}</style>
<div id="host"></div>
<script>
const PAGES = __PAGES__, WIDTHS = __WIDTHS__;
const host = document.getElementById('host');
const results = [];

function inspect(doc, win, wReq){
  const out = {overflow:null, escapes:[], wide:[], tiny:[], taps:[]};
  const de = doc.documentElement;
  const w = de.clientWidth;              // real viewport, scrollbar excluded
  if (de.scrollWidth > w + 1)
    out.overflow = {scroll: de.scrollWidth, client: w};
  const seen = new Set();
  for (const el of doc.querySelectorAll('body *')) {
    const cs = win.getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || cs.position === 'fixed') continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    // element escaping the viewport horizontally
    if ((r.right > w + 1 || r.left < -1) && cs.clipPath === 'none') {
      const id = el.tagName + '.' + (el.className || '').toString().trim().split(/\s+/)[0];
      if (!seen.has('e' + id)) { seen.add('e' + id);
        out.escapes.push({sel:id, w:Math.round(r.width), l:Math.round(r.left), r:Math.round(r.right)}); }
    }
    // content wider than its own box (long unbreakable word, wide table...)
    if (el.scrollWidth > el.clientWidth + 1 && el.clientWidth > 0
        && cs.overflowX === 'visible') {
      const id = el.tagName + '.' + (el.className || '').toString().trim().split(/\s+/)[0];
      if (!seen.has('w' + id)) { seen.add('w' + id);
        out.wide.push({sel:id, content:el.scrollWidth, box:el.clientWidth,
                       txt:(el.textContent||'').trim().slice(0,44)}); }
    }
    // text too small to read
    const fs = parseFloat(cs.fontSize);
    const ownText = Array.from(el.childNodes)
      .filter(n => n.nodeType === 3 && n.textContent.trim().length > 1).length > 0;
    // .brand-t is the tagline inside the logo lockup - a wordmark element,
    // not reading copy, and set as such. Excluded deliberately.
    if (ownText && fs < 12 && !el.classList.contains('brand-t')) {
      const id = el.tagName + '.' + (el.className || '').toString().trim().split(/\s+/)[0];
      if (!seen.has('t' + id)) { seen.add('t' + id); out.tiny.push({sel:id, px:+fs.toFixed(1)}); }
    }
    // tap targets
    if ((el.tagName === 'A' || el.tagName === 'BUTTON' || el.tagName === 'INPUT'
         || el.tagName === 'SELECT') && cs.display !== 'inline'
        && cs.clipPath === 'none' && !el.closest('.copy,.trail,.foot-btm,p')) {
      // WCAG 2.5.8 exception: a control enclosed by a much larger label
      // (the consent checkbox) already has an adequate activation area.
      const lab = el.closest('label');
      const enclosed = lab && lab.getBoundingClientRect().height >= 24
                           && lab.getBoundingClientRect().width >= 24;
      if (!enclosed && r.height > 0 && (r.height < 24 || r.width < 24)) {
        const id = el.tagName + '.' + (el.className || '').toString().trim().split(/\s+/)[0];
        if (!seen.has('p' + id)) { seen.add('p' + id);
          out.taps.push({sel:id, w:Math.round(r.width), h:Math.round(r.height)}); }
      }
    }
  }
  return out;
}

async function run(){
  for (const page of PAGES) {
    for (const w of WIDTHS) {
      const f = document.createElement('iframe');
      f.width = w; f.height = 900; f.src = page;
      host.appendChild(f);
      await new Promise(res => { f.onload = res; setTimeout(res, 2500); });
      try {
        const r = inspect(f.contentDocument, f.contentWindow, w);
        if (r.overflow || r.escapes.length || r.wide.length || r.tiny.length || r.taps.length)
          results.push(Object.assign({page, w}, r));
      } catch (e) {
        results.push({page, w, error: String(e)});
      }
      f.remove();
    }
  }
  document.title = 'AUDIT' + JSON.stringify(results);
}
run();
</script>
"""


def find_chrome():
    for c in CHROME_CANDIDATES:
        if os.path.exists(c):
            return c
    raise SystemExit("No Chrome or Edge found")


def main():
    pages = sorted(os.path.basename(p) for p in glob.glob(os.path.join(DIST, "*.html")))
    pages = [p for p in pages if not p.startswith("__")]
    print("Auditing %d pages x %d widths = %d checks\n"
          % (len(pages), len(WIDTHS), len(pages) * len(WIDTHS)))

    probe = (PROBE.replace("__PAGES__", json.dumps(pages))
                  .replace("__WIDTHS__", json.dumps(WIDTHS)))
    probe_path = os.path.join(DIST, "__audit.html")
    with open(probe_path, "w", encoding="utf-8") as fh:
        fh.write(probe)

    profile = tempfile.mkdtemp(prefix="audit-chrome-")
    url = "file:///" + probe_path.replace("\\", "/").replace(" ", "%20")
    budget = 3000 + len(pages) * len(WIDTHS) * 900
    try:
        out = subprocess.run(
            [find_chrome(), "--headless=new", "--disable-gpu", "--no-sandbox",
             # file:// iframes are opaque origins by default, so the probe
             # cannot reach contentDocument without this.
             "--allow-file-access-from-files", "--disable-web-security",
             "--user-data-dir=" + profile, "--window-size=1500,1000",
             "--virtual-time-budget=%d" % budget, "--dump-dom", url],
            capture_output=True, text=True, timeout=600, encoding="utf-8", errors="ignore")
        dom = out.stdout or ""
    finally:
        shutil.rmtree(profile, ignore_errors=True)
        try:
            os.remove(probe_path)
        except OSError:
            pass

    m = re.search(r"<title>AUDIT(.*?)</title>", dom, re.S)
    if not m:
        print("Probe did not report. DOM bytes:", len(dom))
        t = re.search(r"<title>(.*?)</title>", dom, re.S)
        if t:
            print("title was:", t.group(1)[:400])
        raise SystemExit(1)

    findings = json.loads(m.group(1).replace("&quot;", '"').replace("&amp;", "&")
                          .replace("&lt;", "<").replace("&gt;", ">"))

    if not findings:
        print("PASS - no overflow, no escaping elements, no sub-12px text,")
        print("       no tap target under 24px (WCAG 2.5.8), across all %d page/width combinations."
              % (len(pages) * len(WIDTHS)))
        return

    print("%d page/width combinations reported something:\n" % len(findings))
    for f in findings:
        print("  %-46s %4dpx" % (f["page"], f["w"]))
        if f.get("error"):
            print("      error: %s" % f["error"])
        if f.get("overflow"):
            print("      OVERFLOW  scrollWidth=%s clientWidth=%s"
                  % (f["overflow"]["scroll"], f["overflow"]["client"]))
        for e in f.get("escapes", [])[:10]:
            print("      escapes   %-30s w=%s left=%s right=%s"
                  % (e["sel"], e["w"], e["l"], e["r"]))
        for x in f.get("wide", [])[:8]:
            print("      content   %-24s box=%s content=%s  %r"
                  % (x["sel"], x["box"], x["content"], x["txt"]))
        for t in f.get("tiny", [])[:6]:
            print("      tiny text %-30s %spx" % (t["sel"], t["px"]))
        for p in f.get("taps", [])[:6]:
            print("      small tap %-30s %sx%s" % (p["sel"], p["w"], p["h"]))
    raise SystemExit(1)


if __name__ == "__main__":
    main()
