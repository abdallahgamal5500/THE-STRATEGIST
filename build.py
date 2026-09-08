# -*- coding: utf-8 -*-
"""
THE STRATEGIST - static site generator.

    python build.py

Reads content.py, renders every page into dist/ as plain HTML with a shared
layout, and copies assets/ alongside. No dependencies, no toolchain - the
output is ordinary static files that can be hosted anywhere or opened
directly from disk.

Presentation follows the "instrument" concept documented at the top of
assets/css/site.css: a measure rail, ruled indices instead of cards, and one
bold moment (the six-stage lifecycle drawn as a graduated scale).
"""

import os
import shutil
import datetime
from content import (
    SITE, WHO_WE_ARE, VISION, MISSION, PHILOSOPHY, METHODOLOGY,
    APPROACH, APPROACH_INTRO, PILLARS, FAMILIES, INDUSTRIES,
    CASE_STUDIES, INSIGHTS, INSIGHT_CATEGORIES, LEADERSHIP,
    PARTNERS, PARTNER_CATEGORIES, CLIENTS, TESTIMONIALS, WHY_US,
    CHALLENGES_HOME,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")

# Beta banner. Set to None before any real launch.
BETA = ("<b>Beta preview</b> &mdash; structure and draft copy for review. "
        "Anything tagged <b>Draft</b> or <b>Placeholder</b> still needs client "
        "content or approval.")

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Archivo:wdth,wght@100,600;100,700;112,600;112,700"
         "&family=Instrument+Sans:wght@400;500;600"
         "&display=swap")


# ------------------------------------------------------------------ helpers

def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def pillar_by_slug(slug):
    return next(p for p in PILLARS if p["slug"] == slug)


def families_of(slug):
    return [f for f in FAMILIES if f["pillar"] == slug]


def family_by_slug(slug):
    return next((f for f in FAMILIES if f["slug"] == slug), None)


def fmt_date(iso):
    return datetime.date.fromisoformat(iso).strftime("%d %B %Y")


def tag(label="Draft"):
    """Beta-only marker so the client can see what still needs their input."""
    return '<span class="tag">%s</span>' % esc(label)


def wa_svg():
    return ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 '
            '4.95L2 22l5.25-1.38a9.9 9.9 0 0 0 4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91S17.5 2 12.04 2zm5.8 14.16c-.25.69-1.44 '
            '1.32-1.98 1.37-.53.05-1.02.24-3.45-.72-2.9-1.14-4.75-4.09-4.9-4.28-.14-.19-1.17-1.56-1.17-2.97s.74-2.11 '
            '1-2.4c.26-.29.57-.36.76-.36l.55.01c.17.01.41-.07.64.49.25.6.84 2.07.91 2.22.07.15.12.32.02.51-.1.19-.15.31-.29.48l-.44.51c-.14.14-.29.3-.13.59.17.29.74 '
            '1.22 1.59 1.98 1.09.97 2.01 1.27 2.3 1.42.29.14.46.12.63-.07.17-.19.73-.85.92-1.15.19-.29.39-.24.65-.14.26.09 '
            '1.66.78 1.94.93.29.14.48.22.55.34.07.12.07.7-.18 1.39z"/></svg>')


# --------------------------------------------------------------- components

def layout_block(rail_title, field_html, rail_note=None):
    """Section with the measure rail on the left and content in the field."""
    note = "<small>%s</small>" % esc(rail_note) if rail_note else ""
    return ('<div class="layout"><div class="rail">%s%s</div>'
            '<div class="field">%s</div></div>'
            % (esc(rail_title), note, field_html))


def band(inner, cls="band", wrap="wrap"):
    return '<section class="%s"><div class="%s">%s</div></section>' % (cls, wrap, inner)


def portfolio_index(show_sub=True):
    """All ten service families as a ruled three-column index - names only.
    The columns are too narrow to carry a value proposition without cutting it
    mid-sentence, and a directory reads better as a directory."""
    cols = []
    for p in PILLARS:
        rows = "".join(
            '<a class="index-row" href="%s.html"><span class="n">%s</span></a>'
            % (f["slug"], esc(f["name"])) for f in families_of(p["slug"]))
        sub = '<div class="index-sub">%s</div>' % esc(p["blurb"]) if show_sub else ""
        cols.append('<div class="index-col"><div class="index-head">%s</div>%s%s</div>'
                    % (esc(p["name"]), sub, rows))
    return '<div class="index">%s</div>' % "".join(cols)


def ruled_rows(pairs, flat=False):
    cls = "rows rows-flat" if flat else "rows"
    out = []
    for item in pairs:
        if flat:
            out.append('<div class="row"><div class="row-v">%s</div></div>' % esc(item))
        else:
            k, v = item
            out.append('<div class="row"><div class="row-k">%s</div>'
                       '<div class="row-v">%s</div></div>' % (esc(k), esc(v)))
    return '<div class="%s">%s</div>' % (cls, "".join(out))


def lifecycle_scale(mini=False):
    """The six-stage lifecycle as a graduated scale. A genuine sequence,
    which is the only content on the site that carries numbers."""
    stages = []
    for i, (name, desc) in enumerate(APPROACH, 1):
        stages.append('<div class="stage"><span class="stage-n">%02d</span>'
                      '<div class="stage-t">%s</div>'
                      '<div class="stage-d">%s</div></div>' % (i, esc(name), esc(desc)))
    cls = "scale-mini" if mini else "scale-track"
    return '<div class="%s">%s</div>' % (cls, "".join(stages))


def case_entry(c):
    return ('<div class="entry">'
            '<div class="entry-side"><b>%s</b><span>%s</span></div>'
            '<div><h3><a href="case-%s.html">%s</a></h3><p>%s</p></div>'
            '<div class="entry-side"><b>%s</b><span>%s</span></div>'
            '</div>'
            % (esc(c["sector"]), esc(c["client"]) + (" (anonymized)" if c["anonymized"] else ""),
               c["slug"], esc(c["title"]), esc(c["excerpt"]),
               esc(c["service"]), esc(pillar_by_slug(family_by_slug(c["service_slug"])["pillar"])["name"])
               if family_by_slug(c["service_slug"]) else ""))


def insight_entry(a):
    return ('<div class="entry">'
            '<div class="entry-side"><b>%s</b><span>%s</span></div>'
            '<div><h3><a href="insight-%s.html">%s</a></h3><p>%s</p></div>'
            '<div class="entry-side"><span>%s</span></div>'
            '</div>'
            % (esc(a["category"]), esc(fmt_date(a["date"])),
               a["slug"], esc(a["title"]), esc(a["excerpt"]), esc(a["read"])))


def person(p, bio=True):
    b = '<div class="bio">%s</div>' % esc(p["bio"]) if bio and p.get("bio") else ""
    e = '<div class="exp">%s</div>' % esc(p["expertise"]) if p.get("expertise") else ""
    return ('<div class="person"><div class="person-ph">PHOTO</div>'
            '<h4>%s%s</h4><div class="role">%s</div>%s%s</div>'
            % (esc(p["name"]), tag("Placeholder"), esc(p["title"]), b, e))


def figs(items):
    return '<div class="figs">%s</div>' % "".join(
        '<div class="fig"><b>%s</b><span>%s</span></div>' % (esc(v), esc(k)) for v, k in items)


def filters(labels, first="All"):
    return ('<div class="filters"><span class="on">%s</span>%s</div>'
            % (esc(first), "".join('<span>%s</span>' % esc(l) for l in labels)))


def closing(title="Discuss your challenge",
            text="Tell us what you are trying to change, and we will tell you how we would approach it."):
    return ('<section class="close-band band"><div class="wrap"><div class="close-in">'
            '<div><h2>%s</h2><p>%s</p></div>'
            '<div class="close-acts">'
            '<a href="contact.html" class="btn btn-invert">Request a consultation</a>'
            '<a href="approach.html" class="btn btn-line-invert">See how we work</a>'
            '</div></div></div></section>' % (esc(title), esc(text)))


# ------------------------------------------------------------------- chrome

NAV = [("About", "about.html"), ("Industries", "industries.html"),
       ("Our Approach", "approach.html"), ("Case Studies", "case-studies.html"),
       ("Insights", "insights.html")]


def header(current):
    menu = ['<button id="panelBtn" aria-expanded="false" aria-controls="panel">'
            'Services <i class="chev"></i></button>']
    for label, href in NAV:
        menu.append('<a href="%s"%s>%s</a>'
                    % (href, ' class="here"' if href == current else "", esc(label)))
    menu.append('<a href="contact.html" class="head-cta">Request a consultation</a>')

    panel = ('<div class="panel" id="panel"><div class="wrap">%s'
             '<div class="panel-foot"><a href="services.html" class="tlink">'
             'The full portfolio: three pillars, ten service families</a></div>'
             '</div></div>'
             % portfolio_index(show_sub=False).replace('class="index"', 'class="index panel-in"'))

    drawer_services = "".join(
        '<div class="grp">%s</div>%s' % (
            esc(p["name"]),
            "".join('<a class="sub" href="%s.html">%s</a>' % (f["slug"], esc(f["name"]))
                    for f in families_of(p["slug"])))
        for p in PILLARS)

    drawer = ('<nav class="drawer" id="drawer"><div class="wrap">'
              '<a href="services.html">All services</a>' + drawer_services
              + '<div class="grp">Firm</div>'
              + "".join('<a href="%s">%s</a>' % (h, esc(t)) for t, h in NAV)
              + '<a href="leadership.html">Leadership and experts</a>'
                '<a href="partners.html">Partners</a>'
                '<a href="clients.html">Clients</a>'
                '<a href="testimonials.html">Testimonials</a>'
                '<a href="contact.html" class="btn btn-invert">Request a consultation</a>'
                '</div></nav>')

    return ('<header class="head"><div class="wrap"><div class="head-in">'
            '<a class="brand" href="index.html">'
            '<img src="assets/img/mark-light.svg" alt="">'
            '<span class="brand-x"><span class="brand-n">%s</span>'
            '<span class="brand-t">%s</span></span></a>'
            '<nav class="menu">%s</nav>'
            '<button class="burger" id="burger" aria-expanded="false" aria-controls="drawer" '
            'aria-label="Menu"><span></span><span></span><span></span></button>'
            '</div></div>%s%s</header>'
            % (esc(SITE["name"]).upper(), esc(SITE["tagline"]), "".join(menu), panel, drawer))


def footer():
    def col(title, links):
        return ('<div class="foot-col"><h4>%s</h4>%s</div>'
                % (esc(title), "".join('<a href="%s">%s</a>' % (h, esc(t)) for t, h in links)))

    strat = [(f["name"], f["slug"] + ".html") for f in families_of("strategy")]
    perf = [(f["name"], f["slug"] + ".html") for f in families_of("performance")]
    trans = [(f["name"], f["slug"] + ".html") for f in families_of("transformation")]

    return ('<footer class="foot"><div class="wrap"><div class="foot-top">'
            '<div class="foot-brand">'
            '<a class="brand" href="index.html"><img src="assets/img/mark-light.svg" alt="">'
            '<span><span class="brand-n">%(up)s</span>'
            '<span class="brand-t">%(tag)s</span></span></a>'
            '<p>%(vp)s</p>'
            '<p><a href="mailto:%(email)s">%(email)s</a><br>'
            '<a href="tel:%(tel)s">%(phone)s</a><br>%(city)s</p></div>'
            '%(c1)s%(c2)s%(c3)s%(c4)s</div>'
            '<div class="foot-btm"><div>&copy; %(year)s %(name)s. All rights reserved.</div>'
            '<div><a href="privacy.html">Privacy notice</a> &nbsp; '
            '<a href="%(li)s">LinkedIn</a></div></div></div></footer>'
            % {"up": esc(SITE["name"]).upper(), "tag": esc(SITE["tagline"]),
               "vp": esc(SITE["valueprop"]), "email": esc(SITE["email"]),
               "tel": SITE["phone"].replace(" ", ""), "phone": esc(SITE["phone"]),
               "city": esc(SITE["city"]), "li": SITE["linkedin"],
               "name": esc(SITE["name"]), "year": datetime.date.today().year,
               "c1": col("Strategy", strat), "c2": col("Performance", perf),
               "c3": col("Transformation", trans),
               "c4": col("Firm", [("About", "about.html"), ("Our Approach", "approach.html"),
                                  ("Industries", "industries.html"),
                                  ("Leadership", "leadership.html"),
                                  ("Partners", "partners.html"), ("Clients", "clients.html"),
                                  ("Case Studies", "case-studies.html"),
                                  ("Insights", "insights.html"), ("Contact", "contact.html")])})


JS = """
(function(){
  var b=document.getElementById('burger'), d=document.getElementById('drawer');
  if(b&&d){b.addEventListener('click',function(){
    var o=b.getAttribute('aria-expanded')==='true';
    b.setAttribute('aria-expanded',String(!o)); d.classList.toggle('open',!o);
  });}
  var pb=document.getElementById('panelBtn'), p=document.getElementById('panel');
  if(pb&&p){
    var shut=function(){pb.setAttribute('aria-expanded','false');p.classList.remove('open');};
    pb.addEventListener('click',function(e){
      e.stopPropagation();
      var o=pb.getAttribute('aria-expanded')==='true';
      pb.setAttribute('aria-expanded',String(!o)); p.classList.toggle('open',!o);
    });
    document.addEventListener('click',function(e){
      if(!p.contains(e.target)&&e.target!==pb) shut();
    });
    document.addEventListener('keydown',function(e){
      if(e.key==='Escape'&&p.classList.contains('open')){ shut(); pb.focus(); }
    });
  }
  var f=document.getElementById('leadForm');
  if(f){f.addEventListener('submit',function(e){
    e.preventDefault();
    if(f.querySelector('[name=website]').value) return;   /* honeypot */
    window.location.href='thank-you.html';
  });}
})();
"""


def page(title, desc, body, current=""):
    beta = '<div class="beta"><div class="wrap">%s</div></div>' % BETA if BETA else ""
    return ("""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="website">
<link rel="icon" href="assets/img/favicon.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/favicon-512.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="%(fonts)s">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
%(beta)s
%(head)s
<main id="main">
%(body)s
</main>
%(foot)s
<a class="wa" href="https://wa.me/%(wa)s" aria-label="Message us on WhatsApp" target="_blank" rel="noopener">%(wasvg)s</a>
<script>%(js)s</script>
</body>
</html>
""" % {"title": esc(title), "desc": esc(desc), "fonts": FONTS, "beta": beta,
       "head": header(current), "body": body, "foot": footer(),
       "wa": SITE["whatsapp"], "wasvg": wa_svg(), "js": JS})


def phead(title, lede, trail=None, tg=None):
    t = ""
    if trail:
        parts = ['<a href="%s">%s</a>' % (h, esc(l)) for l, h in trail[:-1]]
        parts.append(esc(trail[-1][0]))
        t = '<div class="trail">%s</div>' % "<i>/</i>".join(parts)
    return ('<section class="phead"><div class="wrap"><div class="phead-in">%s'
            '<h1>%s%s</h1><p class="lede">%s</p></div></div></section>'
            % (t, esc(title), tag(tg) if tg else "", esc(lede)))


# -------------------------------------------------------------------- pages

def p_home():
    hero = ('<section class="hero"><div class="wrap"><div class="hero-in">'
            '<h1>%s</h1>'
            '<p class="hero-lede">%s is a management consulting firm working with executive '
            'teams across %s, from setting direction through to the governance that sustains it.</p>'
            '<div class="hero-acts">'
            '<a href="contact.html" class="btn btn-solid">Request a consultation</a>'
            '<a href="services.html" class="btn btn-line">See the portfolio</a></div>'
            '<div class="hero-meta">'
            '<div><b>Egypt, the GCC and the Middle East</b>Working with government entities, '
            'family groups and large enterprises.</div>'
            '<div><b>Ten service families</b>Across strategy, corporate performance and '
            'business transformation.</div>'
            '<div><b>A six-stage delivery lifecycle</b>Diagnose through to sustain, applied to '
            'every engagement.</div>'
            '</div></div></div></section>'
            % (esc(SITE["valueprop"]), esc(SITE["name"]), esc(SITE["markets"])))

    who = band(layout_block(
        "Who we are",
        '<h2 class="measure-tight">An executive-grade partner across the full journey '
        'from direction to execution.</h2>'
        '<p class="lede">%s</p><p class="dim">%s</p>'
        '<p><a href="about.html" class="tlink">More about the firm</a></p>'
        % (esc(WHO_WE_ARE[0]), esc(WHO_WE_ARE[1])),
        "The firm"))

    portfolio = band(layout_block(
        "The portfolio",
        '<h2 class="measure-tight">Three pillars. Ten service families.</h2>'
        '<p class="lede">Every family is a distinct commercial offer with its own '
        'capabilities, deliverables and expected business value.</p>'
        + portfolio_index(),
        "Three pillars, ten families, more than fifty defined components"),
        cls="band on-paper")

    challenges = band(layout_block(
        "What brings clients to us",
        '<h2 class="measure-tight">The problems executive teams arrive with</h2>'
        + ruled_rows(CHALLENGES_HOME),
        "Recurring patterns across sectors"))

    method = ('<section class="band on-navy"><div class="wrap">%s'
              '<div class="scale">%s</div></div></section>'
              % (layout_block("How we create value",
                              '<h2 class="measure-tight">A six-stage consulting lifecycle</h2>'
                              '<p class="lede">%s</p>' % esc(APPROACH_INTRO),
                              "Diagnose to sustain"),
                 lifecycle_scale()))

    cases = band(layout_block(
        "Selected experience",
        '<h2 class="measure-tight">Engagements and measurable outcomes%s</h2>'
        '<div class="entries">%s</div>'
        '<p><a href="case-studies.html" class="tlink">All case studies</a></p>'
        % (tag("Draft"), "".join(case_entry(c) for c in CASE_STUDIES)),
        "Anonymized where confidentiality applies"), cls="band on-paper")

    ins = band(layout_block(
        "Insights",
        '<h2 class="measure-tight">Latest thinking%s</h2>'
        '<div class="entries">%s</div>'
        '<p><a href="insights.html" class="tlink">All insights</a></p>'
        % (tag("Draft"), "".join(insight_entry(a) for a in INSIGHTS[:3])),
        "Articles and executive perspectives"))

    why = band(layout_block(
        "Why work with us",
        '<h2 class="measure-tight">What makes the difference in delivery</h2>'
        + ruled_rows(WHY_US),
        "Six differentiators"), cls="band on-paper")

    return page("%s | Strategy, Performance, Transformation" % SITE["name"],
                SITE["valueprop"] + " Management consulting across Egypt, the GCC and the Middle East.",
                hero + who + portfolio + challenges + method + cases + ins + why + closing(),
                "index.html")


def p_about():
    hero = phead("About the firm",
                 "A management consulting firm built to close the distance between strategic "
                 "ambition and operational reality.",
                 [("Home", "index.html"), ("About", "")])

    who = band(layout_block(
        "Who we are",
        '<h2 class="measure-tight">Integrated across strategy, performance and transformation</h2>'
        '<p class="lede">%s</p><p class="dim">%s</p>' % (esc(WHO_WE_ARE[0]), esc(WHO_WE_ARE[1])),
        "The firm"))

    vm = band(layout_block(
        "Vision and mission",
        '<div class="rows"><div class="row"><div class="row-k">Vision</div>'
        '<div class="row-v">%s</div></div>'
        '<div class="row"><div class="row-k">Mission</div>'
        '<div class="row-v">%s</div></div></div>' % (esc(VISION), esc(MISSION)),
        "In the firm's words"), cls="band on-navy")

    phil = band(layout_block(
        "Our philosophy",
        '<h2 class="measure-tight">%s</h2><p class="lede">%s</p>%s'
        % (esc(PHILOSOPHY["name"]), esc(PHILOSOPHY["intro"]),
           ruled_rows(PHILOSOPHY["items"])),
        "People, process, product, profit"), cls="band on-paper")

    meth = band(layout_block(
        "Our methodology",
        '<h2 class="measure-tight">%s</h2><p class="lede">%s</p>'
        '<p><a href="approach.html" class="tlink">The six-stage lifecycle</a></p>'
        % (esc(METHODOLOGY["name"]), esc(METHODOLOGY["intro"])),
        "Cross-functional by design"))

    pos = band(layout_block(
        "Positioning",
        '<h2 class="measure-tight">Strategy. Performance. Transformation.</h2>'
        '<p class="lede">Three integrated pillars, ten service families, one accountable team.</p>'
        + portfolio_index(),
        "The full portfolio"), cls="band on-paper")

    why = band(layout_block(
        "Why clients choose us",
        '<h2 class="measure-tight">What clients get that they do not get elsewhere</h2>'
        + ruled_rows(WHY_US),
        "Six differentiators"))

    cover = band(layout_block(
        "Coverage",
        '<h2 class="measure-tight">Where we work%s</h2>'
        '<p class="lede">We support organizations across %s, working with government entities, '
        'family groups, and medium and large enterprises.</p>%s'
        % (tag("Draft"), esc(SITE["markets"]),
           figs([("3", "Integrated consulting pillars"), ("10", "Service families"),
                 ("50+", "Defined service components"), ("6", "Stage delivery lifecycle")])),
        "Egypt, GCC, Middle East"), cls="band on-paper")

    lead = band(layout_block(
        "Leadership",
        '<h2 class="measure-tight">Governance, executive capability and specialist expertise</h2>'
        '<p class="lede">Board and advisory governance, an executive team, and an expert network '
        'across strategy, performance, transformation and industry.</p>'
        '<p><a href="leadership.html" class="btn btn-solid">Meet the team</a></p>',
        "Board, executives, experts"))

    return page("About | %s" % SITE["name"],
                "The Strategist integrates strategy, corporate performance, organization "
                "development and business transformation.",
                hero + who + vm + phil + meth + pos + why + cover + lead + closing(),
                "about.html")


def p_services():
    hero = phead("Services",
                 "Three integrated pillars and ten service families covering the full journey "
                 "from strategic direction through execution to sustained performance.",
                 [("Home", "index.html"), ("Services", "")])

    idx = band(layout_block(
        "The portfolio",
        '<h2 class="measure-tight">Ten service families, one delivery standard</h2>'
        '<p class="lede">Every family page follows the same structure: the client challenges it '
        'addresses, what we do, the components within it, our methodology, the deliverables you '
        'receive and the business value you should expect.</p>' + portfolio_index(),
        "More than fifty defined components"))

    blocks = []
    for i, p in enumerate(PILLARS):
        fams = families_of(p["slug"])
        rows = [(f["name"], f["valueprop"]) for f in fams]
        blocks.append(band(layout_block(
            p["name"],
            '<h2 class="measure-tight">%s</h2><p class="lede">%s</p>%s'
            '<p><a href="%s.html" class="tlink">The %s pillar in full</a></p>'
            % (esc(p["blurb"]), esc(p["lede"]), ruled_rows(rows), p["slug"], esc(p["name"].lower())),
            "%d service families" % len(fams)),
            cls="band on-paper" if i % 2 == 0 else "band"))

    return page("Services | %s" % SITE["name"],
                "Strategy, Performance and Transformation consulting across ten service families "
                "and more than fifty defined components.",
                hero + idx + "".join(blocks) + closing(), "services.html")


def p_pillar(p):
    fams = families_of(p["slug"])
    hero = phead(p["name"], p["lede"],
                 [("Home", "index.html"), ("Services", "services.html"), (p["name"], "")])

    fam = band(layout_block(
        "Service families",
        '<h2 class="measure-tight">%d families within %s</h2>%s'
        % (len(fams), esc(p["name"]),
           '<div class="index"><div class="index-col" style="border-top-width:2px">%s</div></div>'
           % "".join('<a class="index-row" href="%s.html"><span class="n">%s</span>'
                     '<span class="d">%s</span></a>' % (f["slug"], esc(f["name"]), esc(f["valueprop"]))
                     for f in fams)),
        p["blurb"]))

    caps = band(layout_block(
        "Components",
        '<h2 class="measure-tight">What sits inside this pillar</h2>%s'
        % ruled_rows([(f["name"], " / ".join(c[0] for c in f["capabilities"])) for f in fams]),
        "%d defined components" % sum(len(f["capabilities"]) for f in fams)),
        cls="band on-paper")

    appr = ('<section class="band on-navy"><div class="wrap">%s%s</div></section>'
            % (layout_block("Our approach",
                            '<h2 class="measure-tight">How %s engagements run</h2>'
                            '<p class="lede">%s</p>' % (esc(p["name"].lower()), esc(APPROACH_INTRO)),
                            "Six stages"),
               '<div class="scale">%s</div>' % lifecycle_scale(mini=True)))

    rel = [c for c in CASE_STUDIES
           if family_by_slug(c["service_slug"]) and
           family_by_slug(c["service_slug"])["pillar"] == p["slug"]]
    cases = band(layout_block(
        "Related experience",
        '<h2 class="measure-tight">Selected engagements%s</h2><div class="entries">%s</div>'
        % (tag("Draft"), "".join(case_entry(c) for c in rel)),
        "Anonymized")) if rel else ""

    return page("%s Consulting | %s" % (p["name"], SITE["name"]), p["blurb"],
                hero + fam + caps + appr + cases
                + closing("Discuss a %s challenge" % p["name"].lower()), "services.html")


def p_family(f):
    p = pillar_by_slug(f["pillar"])
    hero = phead(f["name"], f["valueprop"],
                 [("Home", "index.html"), ("Services", "services.html"),
                  (p["name"], "%s.html" % p["slug"]), (f["name"], "")])

    ch = band(layout_block(
        "Client challenges",
        '<h2 class="measure-tight">The business problems this addresses</h2>'
        + ruled_rows(f["challenges"]),
        "Why clients engage us here"))

    wwd = band(layout_block(
        "What we do",
        '<h2 class="measure-tight">Our role in %s</h2><p class="lede">%s</p>'
        % (esc(f["name"]), esc(f["whatwedo"])),
        "Scope of the work"), cls="band on-paper")

    caps = band(layout_block(
        "Components",
        '<h2 class="measure-tight">Service components</h2>' + ruled_rows(f["capabilities"]),
        "%d within this family" % len(f["capabilities"])))

    appr = ('<section class="band on-navy"><div class="wrap">%s%s</div></section>'
            % (layout_block("Methodology",
                            '<h2 class="measure-tight">How the work runs</h2>'
                            '<p class="lede">%s</p>' % esc(APPROACH_INTRO), "Six stages"),
               '<div class="scale">%s</div>' % lifecycle_scale(mini=True)))

    dl = band(layout_block(
        "Deliverables",
        '<h2 class="measure-tight">What you receive</h2>' + ruled_rows(f["deliverables"], flat=True),
        "Tangible outputs"), cls="band on-paper")

    val = band(layout_block(
        "Business value",
        '<h2 class="measure-tight">Outcomes leadership can expect</h2>'
        + ruled_rows(f["outcomes"], flat=True),
        "What changes"))

    rel_case = next((c for c in CASE_STUDIES if c["service_slug"] == f["slug"]), None)
    rc = band(layout_block(
        "Related experience",
        '<h2 class="measure-tight">A comparable engagement%s</h2><div class="entries">%s</div>'
        % (tag("Draft"), case_entry(rel_case)), "Case study"),
        cls="band on-paper") if rel_case else ""

    rel_ins = [a for a in INSIGHTS if a.get("service_slug") == f["slug"]]
    ri = band(layout_block(
        "Related insights",
        '<h2 class="measure-tight">Further reading%s</h2><div class="entries">%s</div>'
        % (tag("Draft"), "".join(insight_entry(a) for a in rel_ins)), "Articles")) if rel_ins else ""

    sib = [x for x in families_of(f["pillar"]) if x["slug"] != f["slug"]]
    other = band(layout_block(
        "Also in %s" % p["name"],
        '<h2 class="measure-tight">Related service families</h2>'
        '<div class="index"><div class="index-col">%s</div></div>'
        % "".join('<a class="index-row" href="%s.html"><span class="n">%s</span>'
                  '<span class="d">%s</span></a>' % (x["slug"], esc(x["name"]), esc(x["valueprop"]))
                  for x in sib),
        p["name"]), cls="band on-paper" if not rel_ins else "band") if sib else ""

    return page("%s | %s" % (f["name"], SITE["name"]), f["valueprop"],
                hero + ch + wwd + caps + appr + dl + val + rc + ri + other
                + closing("Discuss your %s challenge" % f["name"].lower()), "services.html")


def p_approach():
    hero = phead("Our Approach", APPROACH_INTRO, [("Home", "index.html"), ("Our Approach", "")])

    cycle = ('<section class="band on-navy"><div class="wrap">%s'
             '<div class="scale">%s</div></div></section>'
             % (layout_block("The lifecycle",
                             '<h2 class="measure-tight">Six stages from diagnosis to '
                             'sustained performance</h2>', "Diagnose to sustain"),
                lifecycle_scale()))

    detail = band(layout_block(
        "Stage by stage",
        '<h2 class="measure-tight">What happens at each stage</h2>' + ruled_rows(APPROACH),
        "In sequence"))

    phil = band(layout_block(
        "The lens",
        '<h2 class="measure-tight">%s</h2><p class="lede">%s</p>%s'
        % (esc(PHILOSOPHY["name"]), esc(PHILOSOPHY["intro"]), ruled_rows(PHILOSOPHY["items"])),
        "How we assess organizational health"), cls="band on-paper")

    meth = band(layout_block(
        "The method",
        '<h2 class="measure-tight">%s</h2><p class="lede">%s</p>'
        % (esc(METHODOLOGY["name"]), esc(METHODOLOGY["intro"])),
        "Cross-functional teams"))

    return page("Our Approach | %s" % SITE["name"],
                "A six-stage consulting lifecycle: Diagnose, Define, Design, Execute, "
                "Measure, Sustain.",
                hero + cycle + detail + phil + meth + closing(), "approach.html")


def p_industries():
    hero = phead("Industries",
                 "Sector experience across government, financial services, industrial, "
                 "healthcare, real estate, consumer, technology and family groups.",
                 [("Home", "index.html"), ("Industries", "")], "Draft")
    grid = band(layout_block(
        "Sectors",
        '<h2 class="measure-tight">Where we work%s</h2>'
        '<p class="lede">The sector list is drafted for review. The client should confirm the '
        'final list, and flag any sector the firm does not wish to claim.</p>%s'
        % (tag("Draft"), ruled_rows(INDUSTRIES)),
        "Eight sectors"))
    note = band(layout_block(
        "Cross-sector",
        '<h2 class="measure-tight">The same disciplines, applied to sector reality</h2>'
        '<p class="lede">Strategy, performance and transformation problems recur across sectors. '
        'What changes is the regulatory context, the economics, and the pace at which decisions '
        'can be taken, which is why each engagement pairs our practice leads with '
        'industry-specific expertise from the expert network.</p>'
        '<p><a href="leadership.html" class="tlink">Our expert network</a></p>',
        "How sector expertise enters"), cls="band on-paper")
    return page("Industries | %s" % SITE["name"],
                "Industry experience across government, financial services, energy, healthcare, "
                "real estate, consumer, technology and family businesses.",
                hero + grid + note + closing(), "industries.html")


def p_cases():
    hero = phead("Case Studies",
                 "Selected engagements: the challenge, what we did, and the measurable outcome. "
                 "Anonymized where client confidentiality applies.",
                 [("Home", "index.html"), ("Case Studies", "")], "Draft")
    grid = band(layout_block(
        "Selected experience",
        '<h2 class="measure-tight">Engagements and impact%s</h2>%s<div class="entries">%s</div>'
        % (tag("Draft"), filters([p["name"] for p in PILLARS]),
           "".join(case_entry(c) for c in CASE_STUDIES)),
        "Three published"))
    note = band(layout_block(
        "Disclosure",
        '<p class="lede">Where a client has given permission, engagements are published with the '
        'client named. Where confidentiality applies, the case study is published in anonymized '
        'form describing the sector, the challenge and the outcome without identifying the '
        'organization.</p>', "Client permission"), cls="band-tight on-paper")
    return page("Case Studies | %s" % SITE["name"],
                "Selected consulting engagements across strategy, performance and transformation.",
                hero + grid + note + closing(), "case-studies.html")


def p_case(c):
    fam = family_by_slug(c["service_slug"])
    hero = phead(c["title"], c["excerpt"],
                 [("Home", "index.html"), ("Case Studies", "case-studies.html"),
                  (c["client"], "")], "Draft")

    facts = band('<div class="layout"><div class="rail">At a glance</div>'
                 '<div class="field">%s</div></div>' % figs(c["metrics"]), cls="band-tight")

    meta = band(layout_block(
        "Engagement",
        ruled_rows([("Client", c["client"] + (" (anonymized)" if c["anonymized"] else "")),
                    ("Sector", c["sector"]),
                    ("Service family", c["service"]),
                    ("Pillar", pillar_by_slug(fam["pillar"])["name"] if fam else "")]),
        "Details"), cls="band-tight on-paper")

    nar = band(layout_block(
        "The engagement",
        '<h2 class="measure-tight">Business challenge</h2>'
        '<div class="copy"><p>%s</p>'
        '<h2>Scope of work</h2><p>%s</p>'
        '<h2>Approach</h2><ol>%s</ol>'
        '<h2>Key deliverables</h2><ul>%s</ul>'
        '<h2>Outcome and impact</h2><p>%s</p></div>'
        % (esc(c["challenge"]), esc(c["scope"]),
           "".join('<li>%s</li>' % esc(x) for x in c["approach"]),
           "".join('<li>%s</li>' % esc(x) for x in c["deliverables"]),
           esc(c["outcome"])),
        "Challenge to outcome"))

    rel = band(layout_block(
        "Related service",
        '<h2 class="measure-tight">The family behind this work</h2>'
        '<div class="index"><div class="index-col">'
        '<a class="index-row" href="%s.html"><span class="n">%s</span>'
        '<span class="d">%s</span></a></div></div>'
        % (fam["slug"], esc(fam["name"]), esc(fam["valueprop"])),
        pillar_by_slug(fam["pillar"])["name"]), cls="band on-paper") if fam else ""

    others = [x for x in CASE_STUDIES if x["slug"] != c["slug"]]
    more = band(layout_block(
        "More case studies",
        '<div class="entries">%s</div>' % "".join(case_entry(x) for x in others),
        "Other engagements")) if others else ""

    return page("%s | Case Study | %s" % (c["title"], SITE["name"]), c["excerpt"],
                hero + facts + meta + nar + rel + more + closing(), "case-studies.html")


def p_insights():
    hero = phead("Insights",
                 "Articles, executive insights and publications on strategy, corporate "
                 "performance and transformation.",
                 [("Home", "index.html"), ("Insights", "")], "Draft")
    grid = band(layout_block(
        "Latest thinking",
        '<h2 class="measure-tight">Insights and publications%s</h2>%s<div class="entries">%s</div>'
        % (tag("Draft"), filters(INSIGHT_CATEGORIES),
           "".join(insight_entry(a) for a in INSIGHTS)),
        "%d published" % len(INSIGHTS)))
    return page("Insights | %s" % SITE["name"],
                "Executive insights on strategy execution, corporate performance management "
                "and business transformation.",
                hero + grid + closing(), "insights.html")


def p_insight(a):
    out = []
    for kind, val in a["body"]:
        if kind == "p":
            out.append("<p>%s</p>" % esc(val))
        elif kind in ("h2", "h3"):
            out.append("<%s>%s</%s>" % (kind, esc(val), kind))
        elif kind == "blockquote":
            out.append("<blockquote>%s</blockquote>" % esc(val))
        elif kind == "ul":
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % esc(x) for x in val))

    hero = ('<section class="phead"><div class="wrap"><div class="phead-in">'
            '<div class="trail"><a href="index.html">Home</a><i>/</i>'
            '<a href="insights.html">Insights</a><i>/</i>%s</div>'
            '<h1>%s%s</h1><p class="lede">%s</p></div></div></section>'
            % (esc(a["category"]), esc(a["title"]), tag("Draft"), esc(a["excerpt"])))

    art = band('<div class="layout">'
               '<div class="rail">%s<small>%s<br>%s<br>%s</small></div>'
               '<div class="field"><div class="copy">%s</div>'
               '<p class="small dim" style="margin-top:40px;padding-top:20px;'
               'border-top:1px solid var(--rule)">Share this article: '
               '<a href="#" class="tlink">LinkedIn</a> &nbsp; '
               '<a href="#" class="tlink">Email</a></p></div></div>'
               % (esc(a["category"]), esc(fmt_date(a["date"])), esc(a["author"]),
                  esc(a["read"]), "".join(out)))

    fam = family_by_slug(a["service_slug"]) if a.get("service_slug") else None
    rel = band(layout_block(
        "Related service",
        '<h2 class="measure-tight">Where this shows up in our work</h2>'
        '<div class="index"><div class="index-col">'
        '<a class="index-row" href="%s.html"><span class="n">%s</span>'
        '<span class="d">%s</span></a></div></div>'
        % (fam["slug"], esc(fam["name"]), esc(fam["valueprop"])),
        pillar_by_slug(fam["pillar"])["name"]), cls="band on-paper") if fam else ""

    others = [x for x in INSIGHTS if x["slug"] != a["slug"]][:3]
    more = band(layout_block(
        "More insights",
        '<div class="entries">%s</div>' % "".join(insight_entry(x) for x in others),
        "Further reading")) if others else ""

    return page("%s | %s" % (a["title"], SITE["name"]), a["excerpt"],
                hero + art + rel + more + closing(), "insights.html")


def p_leadership():
    hero = phead("Leadership and Expert Network",
                 "Governance, executive capability and access to specialist expertise across "
                 "strategy, performance, transformation and industry.",
                 [("Home", "index.html"), ("Leadership", "")], "Placeholder")

    board = band(layout_block(
        "Board and advisory board",
        '<h2 class="measure-tight">Governance and advisory oversight%s</h2>'
        '<p class="lede">Advisory and governance roles, presented separately from executive '
        'management.</p><div class="people">%s</div>'
        % (tag("Placeholder"), "".join(person(x) for x in LEADERSHIP["board"])),
        "Three profiles"))

    execs = band(layout_block(
        "Executive team",
        '<h2 class="measure-tight">Management and delivery leadership%s</h2>'
        '<div class="people">%s</div>'
        % (tag("Placeholder"), "".join(person(x) for x in LEADERSHIP["executives"])),
        "Three profiles"), cls="band on-paper")

    experts = band(layout_block(
        "Experts and associate experts",
        '<h2 class="measure-tight">Specialist expertise across disciplines and industries%s</h2>'
        '<p class="lede">Presented as associate experts and advisors, which does not imply an '
        'employment relationship.</p>%s<div class="people">%s</div>'
        % (tag("Placeholder"), filters([p["name"] for p in PILLARS]),
           "".join(person(x, bio=False) for x in LEADERSHIP["experts"])),
        "Filterable by expertise"))

    return page("Leadership and Experts | %s" % SITE["name"],
                "Board, advisory board, executive team and expert network at The Strategist.",
                hero + board + execs + experts + closing(), "leadership.html")


def p_partners():
    hero = phead("Strategic Partners",
                 "Consulting alliances, technology providers, training and research partners "
                 "that extend what we can deliver for clients.",
                 [("Home", "index.html"), ("Partners", "")], "Placeholder")
    grid = band(layout_block(
        "Partner ecosystem",
        '<h2 class="measure-tight">Approved strategic relationships%s</h2>'
        '<p class="lede">Only formally approved partnerships are displayed. Wording does not '
        'imply certification, exclusivity or endorsement.</p>%s'
        '<div class="marks">%s</div>%s'
        % (tag("Placeholder"), filters(PARTNER_CATEGORIES),
           "".join('<div>PARTNER LOGO<em>%s</em></div>' % esc(cat) for _, cat, _ in PARTNERS),
           ruled_rows([(n + " — " + cat, d) for n, cat, d in PARTNERS])),
        "Four categories"))
    return page("Strategic Partners | %s" % SITE["name"],
                "The Strategist's partner ecosystem: consulting alliances, technology, training "
                "and research partners.",
                hero + grid + closing(), "partners.html")


def p_clients():
    hero = phead("Our Clients",
                 "Selected client experience across the sectors we serve, published where "
                 "permission has been given and anonymized where it has not.",
                 [("Home", "index.html"), ("Clients", "")], "Placeholder")
    wall = band(layout_block(
        "Selected clients",
        '<h2 class="measure-tight">Organizations we work with%s</h2>%s<div class="marks">%s</div>'
        % (tag("Placeholder"), filters([n for n, _ in INDUSTRIES[:4]], "All industries"),
           "".join('<div>CLIENT LOGO<em>%s</em></div>' % esc(sec) for _, sec in CLIENTS)),
        "Eight logos"))
    note = band(layout_block(
        "Permission",
        '<p class="lede">Client logos and names are published only where we hold permission or '
        'an appropriate legal basis. For confidential engagements we publish anonymized '
        'experience describing the sector, challenge and outcome instead.</p>'
        '<p><a href="case-studies.html" class="tlink">Anonymized case studies</a></p>',
        "Confidentiality"), cls="band on-paper")
    return page("Our Clients | %s" % SITE["name"],
                "Selected client experience across government, financial services, industrial, "
                "healthcare and consumer sectors.",
                hero + wall + note + closing(), "clients.html")


def p_testimonials():
    hero = phead("Client Testimonials",
                 "What clients say about the engagement experience, delivery quality and "
                 "measurable impact.",
                 [("Home", "index.html"), ("Testimonials", "")], "Placeholder")
    body = "".join(
        '<div class="quote" style="margin-top:%s"><p>%s</p>'
        '<footer>%s%s<br>%s, %s<br>%s</footer></div>'
        % ("0" if i == 0 else "52px", esc(t["quote"]), esc(t["name"]), tag("Placeholder"),
           esc(t["title"]), esc(t["org"]), esc(t["service"]))
        for i, t in enumerate(TESTIMONIALS))
    grid = band(layout_block(
        "In their words",
        '<h2 class="measure-tight">Approved client feedback%s</h2>'
        '<p class="lede">Testimonials are published only once approved by the client, and are '
        'not materially edited.</p>%s' % (tag("Placeholder"), body),
        "Four published"))
    return page("Client Testimonials | %s" % SITE["name"],
                "Approved client testimonials on engagement quality and measurable impact.",
                hero + grid + closing(), "testimonials.html")


def p_contact():
    opts = ['<option value="">Select a service</option>']
    for p in PILLARS:
        opts.append('<optgroup label="%s">' % esc(p["name"]))
        for f in families_of(p["slug"]):
            opts.append('<option>%s</option>' % esc(f["name"]))
        opts.append("</optgroup>")
    opts.append('<option>Not sure yet</option>')

    form = (
        '<form class="form" id="leadForm" method="post" action="#"><div class="f-grid">'
        '<div class="f"><label for="name">Name <em>required</em></label>'
        '<input type="text" id="name" name="name" required autocomplete="name"></div>'
        '<div class="f"><label for="company">Company <em>required</em></label>'
        '<input type="text" id="company" name="company" required autocomplete="organization"></div>'
        '<div class="f"><label for="jobtitle">Job title</label>'
        '<input type="text" id="jobtitle" name="jobtitle" autocomplete="organization-title"></div>'
        '<div class="f"><label for="email">Email <em>required</em></label>'
        '<input type="email" id="email" name="email" required autocomplete="email"></div>'
        '<div class="f"><label for="phone">Phone</label>'
        '<input type="tel" id="phone" name="phone" autocomplete="tel"></div>'
        '<div class="f"><label for="country">Country</label>'
        '<input type="text" id="country" name="country" autocomplete="country-name"></div>'
        '<div class="f wide"><label for="service">Service of interest</label>'
        '<select id="service" name="service">%s</select></div>'
        '<div class="f wide"><label for="enquiry">What can we help with</label>'
        '<select id="enquiry" name="enquiry"><option>Request a consultation</option>'
        '<option>General inquiry</option></select></div>'
        '<div class="f wide"><label for="message">Message <em>required</em></label>'
        '<textarea id="message" name="message" required '
        'placeholder="Tell us about the challenge you are trying to solve."></textarea></div>'
        '<div class="f wide"><label class="f-consent">'
        '<input type="checkbox" name="consent" required>'
        '<span>I agree that %s may store and use these details to respond to my enquiry, '
        'as described in the <a href="privacy.html">privacy notice</a>.</span></label></div>'
        '<div class="hp"><label>Website<input type="text" name="website" tabindex="-1" '
        'autocomplete="off"></label></div>'
        '<div class="f wide act"><button type="submit" class="btn btn-solid">Send enquiry</button>'
        '<p class="small dim" style="margin-top:14px">Not connected in this beta. On launch it '
        'emails %s and shows a confirmation.%s</p></div>'
        '</div></form>' % ("".join(opts), esc(SITE["name"]), esc(SITE["email"]), tag("Beta")))

    hero = phead("Contact",
                 "Tell us what you are trying to change, and we will come back with how we "
                 "would approach it.",
                 [("Home", "index.html"), ("Contact", "")])

    body = band('<div class="layout">'
                '<div class="rail">Get in touch'
                '<small><a href="mailto:%s">%s</a><br><a href="tel:%s">%s</a><br>%s</small>'
                '<small><a href="https://wa.me/%s" class="tlink">WhatsApp</a></small>'
                '<small><a href="%s" class="tlink">LinkedIn</a></small>'
                '<small>Contact details are placeholders pending client confirmation.</small>'
                '</div>'
                '<div class="field"><h2 class="measure-tight">Request a consultation</h2>'
                '<p class="lede">Complete the form and we will respond within two business days.</p>'
                '%s</div></div>'
                % (esc(SITE["email"]), esc(SITE["email"]), SITE["phone"].replace(" ", ""),
                   esc(SITE["phone"]), esc(SITE["city"]), SITE["whatsapp"], SITE["linkedin"], form))

    return page("Contact | %s" % SITE["name"],
                "Request a consultation with The Strategist. Management consulting across Egypt, "
                "the GCC and the wider Middle East.",
                hero + body, "contact.html")


def p_thanks():
    hero = phead("Thank you",
                 "Your enquiry has been received. A member of the team will respond within two "
                 "business days.",
                 [("Home", "index.html"), ("Contact", "contact.html"), ("Thank you", "")])
    body = band(layout_block(
        "Next steps",
        '<h2 class="measure-tight">What happens now</h2>'
        + ruled_rows([
            "We review your enquiry and identify the right practice lead.",
            "We come back within two business days to arrange an initial conversation.",
            "That conversation is a discussion of your challenge, not a sales pitch.",
        ], flat=True)
        + '<p style="margin-top:34px"><a href="insights.html" class="btn btn-solid">Read our '
          'insights</a> <a href="index.html" class="btn btn-line">Back to home</a></p>',
        "After you send"))
    return page("Thank you | %s" % SITE["name"], "Your enquiry has been received.",
                hero + body, "contact.html")


def p_privacy():
    hero = phead("Privacy Notice", "How we handle the information you submit through this website.",
                 [("Home", "index.html"), ("Privacy", "")], "Draft")
    body = band(layout_block(
        "Privacy",
        '<div class="copy">'
        '<p><strong>Placeholder text for the beta.</strong> The final notice must be reviewed and '
        'approved by the client, and should reflect the jurisdictions in which the firm operates.</p>'
        '<h2>What we collect</h2><p>When you submit the contact form we collect your name, '
        'company, job title, email address, telephone number, country, the service you are '
        'interested in and the content of your message.</p>'
        '<h2>Why we collect it</h2><p>Solely to respond to your enquiry and, where relevant, to '
        'discuss a potential engagement. We do not sell this information or share it with third '
        'parties for marketing.</p>'
        '<h2>How long we keep it</h2><p>Enquiry records are retained for as long as necessary to '
        'manage the business relationship, after which they are deleted.</p>'
        '<h2>Your rights</h2><p>You may request access to, correction of, or deletion of the '
        'information you submitted by contacting <a href="mailto:%s">%s</a>.</p>'
        '<h2>Cookies</h2><p>This website uses only the cookies necessary for it to function. No '
        'advertising or third-party tracking cookies are set.</p></div>'
        % (esc(SITE["email"]), esc(SITE["email"])),
        "Draft for approval"))
    return page("Privacy Notice | %s" % SITE["name"], "Privacy notice for The Strategist website.",
                hero + body, "")


# --------------------------------------------------------------------- build

def _clean(path):
    """Empty dist/ in place. Removing the directory itself fails on Windows
    whenever anything holds a handle on it (Explorer, a browser previewing
    the output); clearing the contents works in every case."""
    if not os.path.isdir(path):
        os.makedirs(path)
        return
    for entry in os.listdir(path):
        target = os.path.join(path, entry)
        try:
            if os.path.isdir(target) and not os.path.islink(target):
                shutil.rmtree(target)
            else:
                os.remove(target)
        except PermissionError:
            print("  warning: %s is in use, left in place" % entry)


def _copy_assets(src, dst):
    for root, _dirs, files in os.walk(src):
        rel = os.path.relpath(root, src)
        out = os.path.join(dst, rel) if rel != "." else dst
        os.makedirs(out, exist_ok=True)
        for name in files:
            shutil.copy2(os.path.join(root, name), os.path.join(out, name))


def build():
    _clean(DIST)
    _copy_assets(os.path.join(ROOT, "assets"), os.path.join(DIST, "assets"))

    pages = [("index.html", p_home()), ("about.html", p_about()),
             ("services.html", p_services())]
    pages += [("%s.html" % p["slug"], p_pillar(p)) for p in PILLARS]
    pages += [("%s.html" % f["slug"], p_family(f)) for f in FAMILIES]
    pages += [("approach.html", p_approach()), ("industries.html", p_industries()),
              ("case-studies.html", p_cases())]
    pages += [("case-%s.html" % c["slug"], p_case(c)) for c in CASE_STUDIES]
    pages += [("insights.html", p_insights())]
    pages += [("insight-%s.html" % a["slug"], p_insight(a)) for a in INSIGHTS]
    pages += [("leadership.html", p_leadership()), ("partners.html", p_partners()),
              ("clients.html", p_clients()), ("testimonials.html", p_testimonials()),
              ("contact.html", p_contact()), ("thank-you.html", p_thanks()),
              ("privacy.html", p_privacy())]

    for name, html in pages:
        with open(os.path.join(DIST, name), "w", encoding="utf-8") as fh:
            fh.write(html)

    with open(os.path.join(DIST, "sitemap.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(sorted(n for n, _ in pages)))

    print("Built %d pages into %s" % (len(pages), DIST))


if __name__ == "__main__":
    build()
