#!/usr/bin/env python3
"""يبني موقع هوجاس ستوديو في site/dist: الصفحات + الدليل + ملف التحميل من نفس المستودع.
   python3 site/build.py            (من جذر المستودع، بعد commit)
   Netlify: build command = python3 site/build.py · publish = site/dist"""
import os, re, shutil, subprocess, sys, zipfile, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site"); OUT = os.path.join(SITE, "dist")
VER = open(os.path.join(ROOT, "VERSION")).read().strip()
VER_SHORT = re.sub(r"\.0$", "", VER)

PAGES = {
    "index": ("هوجاس ستوديو: منتج مقطعك مع Claude", "هوجاس ستوديو أداة مونتاج لمقاطع الكلام للكاميرا: كابشن عربي، كروت شرح، تايم لاين في المتصفح، إشعارات على جوالك، ونشر على تيك توك بموافقتك. تعمل مع Claude Code على جهازك.", "/"),
    "features": ("الميزات: هوجاس ستوديو", "كل ميزات هوجاس ستوديو مرتبة حسب الغرض: القص والتفريغ، الكابشن، كروت الشرح، الصور والمقاطع، المؤثرات، الصوت، التايم لاين، التصدير والنشر.", "/features"),
    "news": ("أخبار الذكاء الاصطناعي: هوجاس ستوديو", "أهم أخبار الذكاء الاصطناعي بالعربي، كل خبر بمصدره ونسبة وثوقه، والأخبار اللي نزلت في حساباتنا معلّمة.", "/news"),
    "updates": ("التحديثات: هوجاس ستوديو", "سجل كل إصدار من هوجاس ستوديو: وش انضاف، ومتى. الأحدث فوق.", "/updates"),
}
NAV = [("/", "الرئيسية"), ("/features", "الميزات"), ("/guide", "دليل الاستخدام"), ("/news", "أخبار الذكاء"), ("/updates", "التحديثات")]

def nav(cur, cls_nav="nav", cls_btn="btn btn-primary"):
    links = "\n".join("<a %shref='%s'>%s</a>" % ("aria-current='page' " if u == cur else "", u, t) for u, t in NAV)
    return '<nav class="%s" id="nav" aria-label="التنقل الرئيسي">\n%s\n<a class="%s" href="/#download">حمّل الأداة</a>\n</nav>' % (cls_nav, links, cls_btn)

def page(name, body, size):
    title, desc, cur = PAGES[name]
    return f'''<!doctype html>
<html lang="ar" dir="rtl" data-ver="{VER_SHORT}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="مونتاج مقاطع الكلام للكاميرا مع Claude، وتعدّل لمساتك على التايم لاين.">
<meta property="og:type" content="website">
<meta property="og:locale" content="ar_SA">
<meta name="theme-color" content="#141413">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">تخطّى إلى المحتوى</a>

<header class="site-header">
<div class="wrap bar">
<a aria-label='هوجاس ستوديو، الصفحة الرئيسية' class='brand' href='/'>
<span class="mark" aria-hidden="true"></span>
<span class="brand-name">هوجاس ستوديو</span>
<span class="brand-latin">Hojas Studio</span>
</a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav">القائمة</button>
{nav(cur)}
</div>
</header>

<main id="main">
{body.replace("{VER}", VER_SHORT).replace("{SIZE}", size)}
</main>

<footer class="site-footer">
<div class="wrap foot">
<a class='brand' href='/'>
<span class="mark" aria-hidden="true"></span>
<span class="brand-name">هوجاس ستوديو</span>
</a>
<ul class="foot-links">
<li><a href='/features'>الميزات</a></li>
<li><a href='/guide'>دليل الاستخدام</a></li>
<li><a href='/news'>أخبار الذكاء</a></li>
<li><a href='/updates'>التحديثات</a></li>
<li><a href="downloads/hojas-studio.zip" download>تحميل الأداة</a></li>
<li><a href="downloads/hojas-studio-guide.pdf" download>دليل PDF</a></li>
<li><a href="https://github.com/rakaga66/hojas-studio" target="_blank" rel="noopener">GitHub</a></li>
</ul>
<p class="foot-note">هوجاس ستوديو · الإصدار {VER_SHORT} · مجاني للاستخدام الشخصي وغير التجاري. Claude و Claude Code علامتان تجاريتان لشركة Anthropic، وهذا الموقع مستقل ولا يتبع لها.</p>
</div>
</footer>

<script src="assets/site.js" defer></script>
</body>
</html>
'''

GUIDE_CSS = '''
/* site bar: same header as the other pages */
.site-header{position:relative;z-index:10;background:var(--paper);border-bottom:1px solid var(--line);font-size:16px;line-height:1.8}
.site-bar{width:min(1120px,100% - 32px);margin-inline:auto;min-height:64px;display:flex;align-items:center;justify-content:space-between;gap:16px}
.site-brand{display:inline-flex;align-items:center;gap:12px;color:var(--ink);text-decoration:none}
.site-mark{width:22px;height:22px;flex:none;background:currentColor;-webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 260 260'%3E%3Crect width='150.5' height='46.8'/%3E%3Crect x='62.5' y='106.6' width='197.5' height='46.8'/%3E%3Crect y='213.2' width='103.7' height='46.8'/%3E%3C/svg%3E") center / contain no-repeat; mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 260 260'%3E%3Crect width='150.5' height='46.8'/%3E%3Crect x='62.5' y='106.6' width='197.5' height='46.8'/%3E%3Crect y='213.2' width='103.7' height='46.8'/%3E%3C/svg%3E") center / contain no-repeat;}
.site-name{font-size:17px;font-weight:700}
.site-latin{font-size:14px;font-weight:500;color:var(--mute)}
.nav-toggle{min-height:44px;padding:0 16px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink);font:600 15px var(--sans);cursor:pointer}
.site-nav{display:none}
.site-nav.is-open{display:grid;position:absolute;inset-inline:0;top:100%;padding:8px 16px 16px;border-bottom:1px solid var(--line);background:var(--paper)}
.site-nav a{padding:12px 0;border-bottom:1px solid var(--line);color:var(--ink);font-weight:500;text-decoration:none}
.site-nav a:last-child{border-bottom:0}
.site-nav a[aria-current="page"]{color:var(--clay-ink)}
.site-nav .site-btn{display:inline-flex;align-items:center;justify-content:center;min-height:44px;margin-top:12px;padding:10px 20px;border-radius:8px;background:var(--clay);color:#141413;font-weight:600;line-height:1.2}
.site-nav .site-btn:hover{background:#E38B6E}
.site-header :focus-visible{outline:2px solid var(--clay);outline-offset:3px}
@media (min-width:768px){ .site-bar{width:min(1120px,100% - 64px)} }
@media (min-width:860px){
.nav-toggle{display:none}
.site-nav,.site-nav.is-open{display:flex;align-items:center;gap:28px;position:static;padding:0;border:0;background:none}
.site-nav a{padding:8px 0;border:0}
.site-nav a[aria-current="page"]{color:var(--ink);text-decoration:underline;text-decoration-color:var(--clay);text-decoration-thickness:2px;text-underline-offset:8px}
.site-nav .site-btn{margin-top:0;padding:10px 20px}
}
@media print{ .site-header{display:none} }
'''

def guide():
    s = open(os.path.join(ROOT, "GUIDE.html"), encoding="utf-8").read()
    s = s.replace("<title>دليل Hojas Studio</title>", '<title>دليل الاستخدام: هوجاس ستوديو</title>\n<meta name="description" content="دليل هوجاس ستوديو: التثبيت خطوة بخطوة، أول مقطع، صفحة الأسئلة، وكل أداة داخل الاستوديو.">\n<meta property="og:title" content="دليل الاستخدام: هوجاس ستوديو">\n<meta property="og:type" content="website">\n<meta property="og:locale" content="ar_SA">\n<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">', 1)
    i = s.index("</style>"); s = s[:i] + GUIDE_CSS + s[i:]
    links = "\n".join("<a %shref='%s'>%s</a>" % ("aria-current='page' " if u == "/guide" else "", u, t) for u, t in NAV)
    hdr = '''<header class="site-header">
<div class="site-bar">
<a aria-label='هوجاس ستوديو، الصفحة الرئيسية' class='site-brand' href='/'>
<span class="site-mark" aria-hidden="true"></span>
<span class="site-name">هوجاس ستوديو</span>
<span class="site-latin">Hojas Studio</span>
</a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav">القائمة</button>
<nav class="site-nav" id="nav" aria-label="التنقل الرئيسي">
%s
<a class="site-btn" href="/#download">حمّل الأداة</a>
</nav>
</div>
</header>
''' % links
    s = re.sub(r"<body([^>]*)>", lambda m: m.group(0) + "\n" + hdr, s, count=1)
    s = s.replace("نزّل الملف المضغوط من الموقع،", 'نزّل <a href="downloads/hojas-studio.zip" download>الملف المضغوط</a>،', 1)
    s = s.replace("<span>يعمل مع Claude Code وOpenCode</span></footer>", '<span><a href="downloads/hojas-studio-guide.pdf" download>نزّل الدليل PDF</a> · يعمل مع Claude Code وOpenCode</span></footer>', 1)
    s = s.replace("</body>", '<script src="assets/site.js" defer></script>\n</body>', 1)
    return s


NEWS_SHOWN = 20
NOBREAK_HYPHEN = re.compile(r"(?<=\w)-(?=\w)")
MONTHS = ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"]

def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def news_body():
    """صفحة الأخبار من site/data/news.json (يتحقق منها news.py ويحسب الوثوق)."""
    sys.path.insert(0, SITE)
    import news as N
    items = N.load()
    for i, it in enumerate(items):
        N.validate(it, i)
    items.sort(key=lambda x: (x["date"], x["key"]), reverse=True)
    shown = items[:NEWS_SHOWN]
    rows = []
    for it in shown:
        y, m, d = it["date"].split("-")
        when = "%d %s" % (int(d), MONTHS[int(m) - 1])
        t = it["trust"]; lvl = "hi" if t >= 90 else "mid" if t >= 60 else "lo"
        posted = [n for k, n in (("tiktok", "تيك توك"), ("instagram", "إنستقرام")) if it.get("posted", {}).get(k)]
        badge = '<span class="posted">نزل في %s</span>' % " و".join(posted) if posted else ""
        srcs = " · ".join('<a href="%s" target="_blank" rel="noopener">%s</a>' % (esc(s["url"]), esc(s["name"])) for s in it["sources"])
        note = '<p class="news-note">%s</p>' % esc(it["note"]) if it.get("note") else ""
        title = NOBREAK_HYPHEN.sub("\u2011", esc(it["title"]))  # model names like Decision-1 stay on one line
        rows.append(f'''<li class="news-item" id="{it["key"]}">
<div class="news-meta"><time datetime="{it["date"]}">{when}</time><span>{esc(it["company"])}</span><span>{esc(it["category"])}</span>{badge}</div>
<h2>{title}</h2>
<p>{esc(it["summary"])}</p>
{note}
<div class="news-foot"><span class="trust trust-{lvl}" title="{N.label(t)}"><b>{t}%</b> {N.label(t)}</span><span class="news-src">المصدر: {srcs}</span></div>
</li>''')
    posted_n = sum(1 for it in shown if any(it.get("posted", {}).values()))
    last = ""
    if shown:
        y, m, d = shown[0]["date"].split("-"); last = "%d %s %s" % (int(d), MONTHS[int(m) - 1], y)
    return f'''<section class="page-head">
<div class="wrap">
<h1>أخبار الذكاء الاصطناعي</h1>
<p>آخر {len(shown)} خبر، كل واحد برابط مصدره ونسبة وثوق محسوبة من نوع المصدر. آخر تحديث {last}{" · %d منها نزلت في حساباتنا" % posted_n if posted_n else ""}.</p>
</div>
</section>
<div class="wrap news-wrap">
<ol class="news-list">
{"".join(rows)}
</ol>
<aside class="trust-key" aria-labelledby="tk">
<h2 id="tk">كيف نحسب نسبة الوثوق</h2>
<ul>
<li><b>95%</b> إعلان رسمي من الشركة نفسها.</li>
<li><b>85%</b> مصدرين إخباريين معروفين.</li>
<li><b>70%</b> مصدر إخباري واحد.</li>
<li><b>45%</b> منشورات تواصل اجتماعي فقط.</li>
<li><b>35%</b> حد أعلى للتسريبات والإشاعات.</li>
</ul>
<p>الأرقام اللي تقولها الشركة عن نفسها (سرعة، دقة) نكتب جنبها إنها من الشركة.</p>
</aside>
</div>
'''

def tool_zip(path):
    """ملف التحميل = آخر commit بدون docs ولا site (git archive يطبّق .gitattributes، فـ install.bat بنهايات ويندوز)."""
    raw = subprocess.run(["git", "-C", ROOT, "archive", "--format=zip", "--prefix=hojas-studio/", "HEAD"], capture_output=True, check=True).stdout
    src = zipfile.ZipFile(io.BytesIO(raw)); dst = zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED)
    for it in src.infolist():
        rel = it.filename[len("hojas-studio/"):]
        if rel.startswith(("docs/", "site/")) or rel in (".gitignore", ".gitattributes"): continue
        dst.writestr(it, src.read(it.filename))
    dst.close()

def main():
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "downloads"))
    shutil.copytree(os.path.join(SITE, "assets"), os.path.join(OUT, "assets"))
    shutil.copy(os.path.join(SITE, "favicon.ico"), OUT)
    z = os.path.join(OUT, "downloads", "hojas-studio.zip"); tool_zip(z)
    size = "%.1f" % (os.path.getsize(z) / 1048576)
    shutil.copy(os.path.join(ROOT, "GUIDE.pdf"), os.path.join(OUT, "downloads", "hojas-studio-guide.pdf"))
    for name in PAGES:
        body = news_body() if name == "news" else open(os.path.join(SITE, "pages", name + ".html"), encoding="utf-8").read()
        open(os.path.join(OUT, name + ".html"), "w", encoding="utf-8").write(page(name, body, size))
    open(os.path.join(OUT, "guide.html"), "w", encoding="utf-8").write(guide())
    shutil.copy(os.path.join(SITE, "data", "news.json"), os.path.join(OUT, "news.json"))
    print("الموقع جاهز:", OUT, "· الإصدار", VER, "· التحميل", size, "ميقا")

if __name__ == "__main__": main()
