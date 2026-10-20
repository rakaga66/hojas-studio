#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hojas Studio 4.36 — استوديو مونتاج بمحرّكه (مجلد engine بجنب هذا الملف، بدون أي مكتبة خارجية).

  python hs.py open   <work> [--engine <مجلد المحرّك>] [--port 8800] [--no-browser]
        يشغّل الخادم بالخلفية ويفتح المتصفح. شغّله أول ما تبدأ المونتاج، حتى قبل ما يجهز أي ملف.
  python hs.py serve  <work> [--engine …] [--port 8800]          الخادم بالواجهة (للتجربة)
  python hs.py say    <work> "وش قاعد أسوي" [--kind step|info|done|ask]   سطر يظهر للمستخدم بالبث الحي
  python hs.py status <work>                                       المراحل + آخر النشاط

  python hs.py brief  <work> ask [--hooks "…" "…"] [--topics "…" "…"] [--note "…"] [--file q.json]
        يفتح للمستخدم صفحة أسئلة قبل المونتاج (بعد التفريغ). ثم:  brief <work> wait   ثم:  brief <work> apply
  python hs.py media  <work> search "query" [--n 8] | add <رقم> --at <ثانية> [--dur 3] [--fit card|cover]     صور برخص حرّة
  python hs.py gen    <work> request image|video "وصف" [--at t] [--fit card|cover] | list | import <رقم> <ملف|رابط> [--at t] | rm <رقم> | moments [4]
        بلا مفاتيح API: الطلب ينحفظ، يتولّد من حساب المستخدم (ChatGPT للصور · Gemini للمقاطع)، ثم import يدخّله التايم لاين.
  python hs.py platform [tiktok instagram x linkedin]     وش تحتاج كل منصة (مقاس · مدة · مناطق آمنة · أسلوب)
  python hs.py auto   <work> zooms | transitions [type=curve dir=right] | beats | clear zooms|transitions|beats
  python hs.py caps   <work> regroup [wpl=5 lines=2] | names | clean [--dry]     الكابشن 5 كلمات بالسطر على الأنفاس · الأسماء بالإنجليزي · شيل جمل whisper المخترعة
  python hs.py look   <work> list | apply <اسم> | off           طابع جاهز (ملف سري · كينوت · سينما صامتة · مشربية …)
  python hs.py sound  providers [set elevenlabs higgsfield | off]   خدمات الأصوات المربوطة بحسابه (يسألك عنها بصفحة الأسئلة)
  python hs.py dub    <work> script <ar|en|es…> | import <json> | add <رقم> <ملف> | track <ملف> | build | off | status   الدبلجة بسكتات المقطع
  python hs.py quality <work> off | light | strong | preview <ث>   تحسين الجودة: ينظّف ويحدّد ويرفع لـ1080 (قبل الكابشن)
  python hs.py media  <work> [fresh]                            القص الفوري: هل الفيديو على آخر قص؟ و fresh يبنيه الحين
  python hs.py mode   <work> [claude | manual]                    وضع الاستوديو: Claude يمنتج، أو مونتاج يدوي (و«اسأل Claude» لو احتجته)
  python hs.py beat   <work> [ملف | my2] [--at ث]                 يقيس إيقاع الموسيقى (للقص على الضربة)

  python hs.py text   <work> [show | <رقم الجملة> "النص الجديد"]
  python hs.py tr     <work> export | import <file.json>
  python hs.py set    <work> cap.font=Tajawal cap.size=70 en.on=true mix.voice=1.2 …
  python hs.py layer  <work> list | add type=text text="…" s=1 e=4 … | set <id> k=v … | rm <id>
  python hs.py kf     <work> <id> list | add <ث> [dx= dy= s= r= o= e=smooth|linear|back|hold] | rm <ث|all> | preset across|grow|rise|spin|pulse|sway   حركة بالمفاتيح
  python hs.py hook   <work> set "صيغة 1" "صيغة 2" … | active <رقم> | off
  python hs.py check  <work>                         فحص الاحتفاظ + الحشو + الجمل المعادة
  python hs.py remove <work> [--cards 3 7] [--ranges 4.2-5.1 …] [--fillers] [--force]    يقص من الفيديو والصوت (يرفض الكلام المهم وآخر المقطع بدون --force)
  python hs.py logo   <work> plan | auto | add <الاسم> <ملف|رابط>     شعار الشركة لما ينذكر اسمها، و«X أفضل من Y»
  python hs.py takes  <work> scan | list [--all] | use <رقم> [--why …] | drop | keep | note | fit <ث> | preview | apply   اختيار الجمل (إعادات وتلعثم)
  python hs.py plan   <work> show | check | wait | approve      خطة المقطع قبل البناء (plan.json)
  python hs.py voice  <work> list | mute <من> <إلى> | set <من> <إلى> <مستوى> | rm <رقم|all>   مستوى صوتك لأجزاء من المقطع
  python hs.py rmbg   <work> <صورة> [auto|flat|person]          يشيل خلفية صورة مضافة (على الجهاز)
  python hs.py undo   <work>  ·  redo <work>                      ترجع خطوة أو تعيدها (السجل محفوظ بالمشروع، حتى تعديلات Claude والقص)
  python hs.py steps  <work> · facts <work> · cuts <work> [fix] · gloss list|add|rm     الخطوات · أرقام تتأكد منها · قطعات على صوت · قاموسك
  python hs.py fonts  list | install <zip|مجلد> | apply <work>         خطوطه الخاصة (تبقى على جهازه، ما تنرفع)
  python hs.py export <work> [--clean] [--hooks] [--frame 9:16|4:5|1:1|16:9]     التصدير النهائي (نفس زر الاستوديو)
  python hs.py pack   <work>                         حزمة النشر (فيديو + SRT عربي/إنجليزي + نص البوست)
  python hs.py notes  <work> [list | done <id> "وش سويت" | reopen <id>]
  python hs.py brand  <work> list | save <اسم> | apply <اسم>
  python hs.py identity list | new "الاسم" [--text …] [--file …] | show | set | check | default | apply <work>   هويته (identity.md) لكل مونتاج وموشن وبودكاست (4.37)
  python hs.py patch  <work>          يركّب إضافة المحرّك على compose.html (آمن تكراره)
  python hs.py face   <work>                         يحدد مكان الوجه (يشتغل لحاله، هذا للإعادة)
  python hs.py mask   <work> <ث-ث> …                 يجهّز قص الشخص لمدى معيّن (يشتغل لحاله مع type=bg|behind)
  python hs.py sfx    <work> list | add <id> <ث> … | import <ملف أو مجلد> [--name "…"] [--note "…"]   مكتبة الأصوات + أصوات المستخدم
  python hs.py bleep  <work> list | word <كلمة> … | at <ث> | add <من> <إلى> | rm <رقم|all> | mode beep|mute | cap stars|hide|keep | tone <هيرتز>   كتم كلمة (4.6)
  python hs.py notify setup | test | off | status | send "نص" [--file ملف]    إشعارات وملفات لجوالك (ntfy، بلا حساب)
  python hs.py style  show | snap <work> | learn <work> | apply <work> | reset   يتعلّم أسلوب المستخدم من تعديلاته
  python hs.py publish <work> list | <tiktok> [--at "وقت"] | done <المنصة> <الرابط>   يجهّز النشر من متصفح المستخدم
  python hs.py update                                يحدّث السكل (لو مثبّت بـ git)
  python hs.py kinetic <work> auto [--from ث --to ث] [--deco flowers|badges|both|none] | clear | set mark=… avatar=…   أسلوب «ورق متحرك»
  python hs.py dahih  <work> on [--title …] [--tag …] [--avatar …] [--layout window|full] | bg <mode> --at ث | off      أسلوب «الدحيح»
  python hs.py hub   [--root <مجلد المشاريع>] [--tailscale] [--no-browser] [--autostart [off]]   المكتبة: كل مقاطعك + أوامرك لـClaude + حالة جهازك (جوال وكمبيوتر)
  python hs.py clips scan <حلقة.mp4> <مجلد> | make <مجلد> --from 12:30 --to 13:45 --title "…" --credit "…" | list <مجلد>   مقاطع مترجمة من حلقة طويلة
  python hs.py tools                                 وش الأدوات اللي يحتاجها السكل وليش (اعرضها على المستخدم قبل أي تثبيت)
  python hs.py doctor [--engine …]
  python hs.py selftest [<work>]      فحص ذاتي: صياغة الملفات · النصوص العربية سليمة · كل مفاتيح الواجهة موجودة · الخادم يرد
"""
import sys, os, json, time, re, shutil, subprocess, threading, secrets, base64, array, glob, zipfile, difflib, hashlib, tempfile, math
import importlib.util, urllib.parse, urllib.request, urllib.error, socket, html

# ويندوز: الخادم يشتغل بلا نافذة، فأي برنامج يشغّله (ffmpeg · node · bash) كان يفتح نافذة تيرمنال تومض.
# نخلّي كل تشغيل مخفي افتراضياً إلا لو الأمر حدد أعلامه بنفسه.
if os.name == "nt":
    _Popen0 = subprocess.Popen
    class _QuietPopen(_Popen0):
        def __init__(self, *a, **k):
            if not k.get("creationflags"): k["creationflags"] = 0x08000000      # CREATE_NO_WINDOW
            super().__init__(*a, **k)
    subprocess.Popen = _QuietPopen

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace"); sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
os.environ.setdefault("PYTHONUTF8", "1"); os.environ.setdefault("PYTHONIOENCODING", "utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
VERSION = "4.38"
HOME_CFG = os.path.join(os.path.expanduser("~"), ".hojas-studio")
SNAP_FILES = ("caps.json", "theme.json", "studio.json", "sfx.json", "cut.json", "takes.json")
TAG = '<script src="hs-ext.js"></script>'
PY = sys.executable
FILLERS = ["يعني", "اه", "آه", "أه", "اهه", "امم", "اممم", "ام", "إم", "ممم", "ايه", "إيه", "طيب", "يعنى", "هاه", "ااه", "اا"]
STAGES = [("src", "استلام الفيديو", "Source video"), ("cut", "قص السكتات", "Silence cut"), ("stt", "تفريغ الكلام", "Transcribe"),
          ("caps", "الكابشن", "Captions"), ("video", "القص والزوم", "Cut and zoom"), ("scenes", "المشاهد والموشن", "Scenes"),
          ("render", "الرسم", "Render"), ("final", "الملف النهائي", "Final file")]

# ───────────────────────── أدوات عامة ─────────────────────────
def rj(path, default=None):
    if not os.path.exists(path): return default
    try:
        with open(path, encoding="utf-8") as f: return json.load(f)
    except Exception: return default
_WJ_LOCK = threading.Lock()
def wj(path, obj):
    """4.33: ملف مؤقت باسم خاص لكل كتابة، ولو ويندوز رفض الاستبدال (الملف مفتوح للقراءة، OneDrive، مضاد الفيروسات) نعيد المحاولة ثم نكتب مباشرة.
    قبل: كتابتين بنفس اللحظة على job.json.tmp تطلع «Access is denied [WinError 5]» وتوقف الشغل."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True); tmp = "%s.%d.%d.tmp" % (path, os.getpid(), threading.get_ident())
    with open(tmp, "w", encoding="utf-8") as f: json.dump(obj, f, ensure_ascii=False, indent=1)
    for k in range(12):
        try: os.replace(tmp, path); return
        except PermissionError: time.sleep(0.05 * (k + 1))
    try:
        with open(path, "w", encoding="utf-8") as f: json.dump(obj, f, ensure_ascii=False, indent=1)
    finally:
        try: os.remove(tmp)
        except OSError: pass
def card_key(c): return " ".join(w["t"] for w in c["w"])
def hs_of(st): return st.setdefault("hs", {})
def J(work, *a): return os.path.join(work, *a)
def load_studio(work): return rj(J(work, "studio.json"), {}) or {}
def new_id(layers): return "L%d" % (max([int(re.sub(r"\D", "", str(l.get("id", "0"))) or 0) for l in layers] or [0]) + 1)

def find_engine(explicit=None):
    """المحرّك جزء من السكل: مجلد engine بجنب hs.py. --engine و HS_ENGINE للتجارب فقط."""
    for c in (explicit, os.environ.get("HS_ENGINE"), os.path.join(HERE, "engine")):
        if c and os.path.isfile(os.path.join(c, "studio", "studio.py")) and os.path.isdir(os.path.join(c, "scripts")):
            return os.path.abspath(c)
    return None
def remember_engine(eng):
    try: os.makedirs(HOME_CFG, exist_ok=True); cfg = rj(os.path.join(HOME_CFG, "config.json"), {}) or {}; cfg["engine"] = eng; wj(os.path.join(HOME_CFG, "config.json"), cfg)
    except Exception: pass

def fix_windows_path():
    """على ويندوز: bash لازم يكون قِت-باش مو WSL، وإلا سكربتات المحرّك تفشل."""
    if os.name != "nt": return
    for d in (r"C:\Program Files\Git\bin", r"C:\Program Files (x86)\Git\bin",
              os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs", "Git", "bin")):
        if os.path.isfile(os.path.join(d, "bash.exe")):
            os.environ["PATH"] = d + os.pathsep + os.environ.get("PATH", ""); return

# ───────────────────────── 4.9: خطوط هويتك (ثمانية) ─────────────────────────
# ترخيص خط ثمانية يمنع رفعه أو توزيعه مع أي برنامج، فملفاته ما تنرفق بالنسخة العامة (.gitignore):
# تنحط مرة على جهاز المستخدم (hs fonts install <zip>) وتنسخ لمجلد كل مشروع عشان الرسم والتصدير يشوفونها.
BRAND_FONTS = {"Thmanyah Sans": "thmanyahsans", "Thmanyah Serif Display": "thmanyahserifdisplay", "Thmanyah Serif Text": "thmanyahseriftext"}
CAP_BRAND, TITLE_BRAND = "Thmanyah Sans", "Thmanyah Serif Display"     # الكابشن · العنوان الثابت فوق (ما يستخدمه غيره)
FONT_W = {"thin": 100, "extralight": 200, "light": 300, "regular": 400, "book": 400, "medium": 500, "semibold": 600, "bold": 700, "extrabold": 800, "heavy": 900, "black": 900}
def font_dirs():
    return [os.path.join(HOME_CFG, "fonts"), os.path.join(HERE, "fonts"), os.path.join(os.path.expanduser("~"), "Documents", "hojas-studio", "fonts")]
def brand_fonts():
    """{العائلة: [(الوزن، المسار)…]} للخطوط المركّبة على هالجهاز (woff2 أول، وإلا otf/ttf)."""
    out = {}
    for fam, pre in BRAND_FONTS.items():
        got = {}
        for d in font_dirs():
            if not os.path.isdir(d): continue
            for f in os.listdir(d):
                m = re.match(re.escape(pre) + r"-([A-Za-z]+)\.(woff2|otf|ttf)$", f, re.I)
                if not m or m.group(1).lower() not in FONT_W: continue
                w = FONT_W[m.group(1).lower()]; rank = {"woff2": 0, "otf": 1, "ttf": 2}[m.group(2).lower()]
                if w not in got or rank < got[w][0]: got[w] = (rank, os.path.join(d, f))
        if got: out[fam] = sorted((w, p) for w, (r, p) in got.items())
    return out
def brand_fonts_install(src):
    """من ملف zip أو مجلد: ينسخ ملفات الخط (woff2 و otf) لمجلد الخطوط الخاص بالجهاز ~/.hojas-studio/fonts."""
    dst = os.path.join(HOME_CFG, "fonts"); os.makedirs(dst, exist_ok=True); n = 0; pat = re.compile(r"(%s)-[A-Za-z]+\.(woff2|otf|ttf)$" % "|".join(BRAND_FONTS.values()), re.I)
    if os.path.isfile(src) and src.lower().endswith(".zip"):
        with zipfile.ZipFile(src) as z:
            for nm in z.namelist():
                b = os.path.basename(nm)
                if "__MACOSX" in nm or not pat.search(b): continue
                open(os.path.join(dst, b), "wb").write(z.read(nm)); n += 1
    elif os.path.isdir(src):
        for root, _, fs in os.walk(src):
            for b in fs:
                if pat.search(b) and "__MACOSX" not in root: shutil.copy2(os.path.join(root, b), os.path.join(dst, b)); n += 1
    else: raise RuntimeError("أعطني ملف zip أو مجلد الخط")
    return n, dst
def brand_fonts_project(work, fams=(CAP_BRAND, TITLE_BRAND)):
    """ينسخ خطوط الهوية لمجلد المشروع ويسجّلها بـ studio.json (hs.fonts) بأوزانها. يرجّع True لو غيّر شي."""
    bf = brand_fonts(); fams = [f for f in fams if f in bf]
    if not fams: return False
    os.makedirs(J(work, "fonts"), exist_ok=True); sp = J(work, "studio.json"); st = load_studio(work); hs = hs_of(st)
    have = {(x.get("name"), x.get("file")) for x in hs.get("fonts") or []}; add = []
    for fam in fams:
        for w, p in bf[fam]:
            b = os.path.basename(p); d = J(work, "fonts", b)
            if not os.path.isfile(d) or os.path.getsize(d) != os.path.getsize(p): shutil.copy2(p, d)
            if (fam, b) not in have: add.append({"name": fam, "file": b, "weight": w})
    if add: hs["fonts"] = (hs.get("fonts") or []) + add; wj(sp, st)
    return bool(add)
def brand_fonts_defaults(hs):
    """الافتراضي لو خط الهوية مركّب: الكابشن ثمانية سانس، والعنوان الثابت فوق ثمانية سيرف ديسبلاي."""
    bf = brand_fonts(); ch = []
    if CAP_BRAND in bf:
        cap = hs.setdefault("cap", {}); ws = [w for w, _ in bf[CAP_BRAND]]
        cap["font"] = CAP_BRAND; cap["weight"] = min(ws, key=lambda w: abs(w - int(cap.get("weight") or 700))); ch.append("الكابشن: " + CAP_BRAND)
    if TITLE_BRAND in bf:
        hk = hs.setdefault("hooks", {}); hk["font"] = TITLE_BRAND; ch.append("العنوان فوق: " + TITLE_BRAND)
    return ch
def cmd_fonts(args):
    sub = args[0] if args else "list"
    if sub == "install":
        if len(args) < 2: sys.exit("fonts install <ملف zip أو مجلد الخط>")
        n, d = brand_fonts_install(os.path.abspath(args[1])); print("انحطت %d ملف خط في %s (على جهازك بس، ما تنرفع مع السكل)" % (n, d))
    elif sub == "apply":
        if len(args) < 2: sys.exit("fonts apply <work>")
        w = os.path.abspath(args[1]); st = load_studio(w); ch = brand_fonts_defaults(hs_of(st)); wj(J(w, "studio.json"), st); brand_fonts_project(w)
        print("\n".join(ch) if ch else "خط الهوية مو مركّب. ركّبه: hs fonts install <zip>")
    else:
        bf = brand_fonts()
        print("\n".join("%s: %s" % (k, " · ".join(str(w) for w, _ in v)) for k, v in bf.items()) if bf else "ما فيه خطوط هوية مركّبة. ركّبها: hs fonts install <zip>")
def patch(work, quiet=False):
    """ينسخ الإضافة لمجلد الشغل ويضيف سطرها آخر compose.html. يرجّع True لو غيّر شي، None لو compose ما وُجد بعد."""
    comp = J(work, "compose.html")
    if not os.path.exists(comp):
        if quiet: return None
        sys.exit("ما فيه compose.html بمجلد الشغل: " + work)
    src_ext = os.path.join(HERE, "ext.js"); dst = J(work, "hs-ext.js")
    if not os.path.exists(dst) or open(src_ext, "rb").read() != open(dst, "rb").read(): shutil.copyfile(src_ext, dst)
    try: brand_fonts_project(work)   # 4.9: خطوط الهوية المركّبة على الجهاز تنسخ للمشروع
    except Exception: pass
    src = open(comp, encoding="utf-8").read()
    old = "T('والملف كامل يوصلك على الخاص',540,1370"   # 3.9: السطر الصغير بكرت الختام صار يتعدّل من الاستوديو
    if old in src: src = src.replace(old, "T(OUTRO_T.sub==null?'والملف كامل يوصلك على الخاص':OUTRO_T.sub,540,1370"); open(comp, "w", encoding="utf-8").write(src)
    of_old = "function outro(t){ const s=VEND;"   # 4.1: خط كرت الختام يتغيّر من الاستوديو
    if of_old in src and "function outroF(" not in src:
        src = src.replace(of_old, "function outro(t){ return outroF(t,OUTRO_T.font?'\"'+OUTRO_T.font+'\"':FONT); }\nfunction outroF(t,FONT){ const s=VEND;"); open(comp, "w", encoding="utf-8").write(src)
    if TAG in src: return False
    i = src.rfind("</body>")
    src = (src[:i] + TAG + "\n" + src[i:]) if i >= 0 else (src + "\n" + TAG + "\n")
    open(comp, "w", encoding="utf-8").write(src); return True

# ───────────────────────── البث الحي: نشاط + مراحل ─────────────────────────
def act_path(work): return J(work, ".hs", "activity.jsonl")
def say(work, text, kind="info"):
    os.makedirs(J(work, ".hs"), exist_ok=True); p = act_path(work)
    n = sum(1 for _ in open(p, encoding="utf-8")) if os.path.exists(p) else 0
    with open(p, "a", encoding="utf-8") as f:
        f.write(json.dumps({"id": n + 1, "t": int(time.time()), "kind": kind, "text": str(text)[:1200]}, ensure_ascii=False) + "\n")
_ACT = {}
def activity(work, since=0, limit=80):
    p = act_path(work)
    try: st = os.stat(p)
    except OSError: return []
    c = _ACT.get(p)
    if c and c[0] == (st.st_mtime, st.st_size) and since >= c[1]: return []   # 4.4.1: ما تغيّر شي، لا نقرأ الملف كامل
    out = []
    for line in open(p, encoding="utf-8"):
        try: e = json.loads(line)
        except Exception: continue
        if e.get("id", 0) > since: out.append(e)
        last = e.get("id", 0)
    try: _ACT[p] = ((st.st_mtime, st.st_size), last)
    except NameError: pass
    return out[-limit:]
_STG = {}
def stages(work):
    """4.4.1: نفس النتيجة بدون ما نعدّ آلاف الفريمات مع كل نبضة: نعيد الحساب بس لو شي تغيّر."""
    def mt_(*a):
        try: return os.path.getmtime(J(work, *a))
        except OSError: return 0
    k = (signature(work), mt_("vfr"), mt_("out"), mt_("ad-master.mp4"), mt_("ad-final.mp4"), mt_("src.mov"), mt_("a.json"))
    c = _STG.get(work)
    if c and c[0] == k: return c[1]
    r = _stages(work); _STG[work] = (k, r); return r
def _stages(work):
    E = lambda *a: os.path.exists(J(work, *a))
    nvf = len(os.listdir(J(work, "vfr"))) if os.path.isdir(J(work, "vfr")) else 0
    nout = len(os.listdir(J(work, "out"))) if os.path.isdir(J(work, "out")) else 0
    caps = rj(J(work, "caps.json"), None); st = load_studio(work); sfx = rj(J(work, "sfx.json"), {}) or {}
    total = round(((caps or {}).get("total", 0) + sfx.get("outro", 0)) * 30) if caps else 0
    comp = open(J(work, "compose.html"), encoding="utf-8").read() if E("compose.html") else ""
    has_sc = bool([s for s in (st.get("scenes") or []) if s.get("m") not in (None, "R_FULL")]) or "SCENE_LIST.push" in comp.split("SCENE_LIST=[]")[-1][-6000:] or bool((st.get("hs") or {}).get("layers"))
    done = {"src": E("src.mov") or E("cutz.mp4"), "cut": E("cut.json"), "stt": E("a.json") or bool(caps), "caps": bool(caps and caps.get("cards")),
            "video": E("cutz.mp4") and nvf > 0, "scenes": has_sc, "render": total > 0 and nout >= total - 1, "final": E("ad-master.mp4") or E("ad-final.mp4")}
    out = []
    for k, ar, en in STAGES:
        d = {"key": k, "ar": ar, "en": en, "done": bool(done[k])}
        if k == "render" and total and 0 < nout < total - 1: d["pct"] = round(100 * nout / total)
        out.append(d)
    return out
# 4.18: وضع الاستوديو لكل مشروع: claude (Claude يمنتج: المعاينة والخطة وتقدّمه) · manual (المحرّر كامل، وClaude لما تطلبه)
STUDIO_MODES = ("claude", "manual")
def studio_mode(work): return (load_studio(work).get("hs") or {}).get("mode")
def studio_mode_set(work, mode, only_if_unset=False):
    if mode not in STUDIO_MODES: return None
    st = load_studio(work); hs = hs_of(st)
    if only_if_unset and hs.get("mode") in STUDIO_MODES: return hs["mode"]
    hs["mode"] = mode; wj(J(work, "studio.json"), st); return mode
def cmd_mode(work, args):
    if not args: print(studio_mode(work) or "manual (الافتراضي)"); return
    if args[0] not in STUDIO_MODES: sys.exit("mode لازم: claude | manual")
    studio_mode_set(work, args[0]); print("الاستوديو صار على: " + ("Claude يمنتج" if args[0] == "claude" else "مونتاج يدوي"))
def ready(work): return os.path.exists(J(work, "compose.html")) and bool((rj(J(work, "caps.json"), {}) or {}).get("cards")) and os.path.isdir(J(work, "vfr")) and os.path.exists(J(work, "cutz.mp4"))
def signature(work):
    h = hashlib.md5()
    for f in ("caps.json", "theme.json", "studio.json", "sfx.json", "cut.json", "compose.html", "cutz.mp4", "notes.json", "review.json", "post.txt", "brief.json", "gen.json"):
        p = J(work, f); h.update(("%s:%s;" % (f, int(os.path.getmtime(p) * 10) if os.path.exists(p) else 0)).encode())
    return h.hexdigest()[:12]

# ───────────────────────── تعديل نص جملة ─────────────────────────
def set_card_text(caps, idx, text):
    """يعدّل نص جملة. لو التعديل حذف كلمات فقط، الكلمات الباقية تحتفظ بتوقيتها الحقيقي."""
    c = caps["cards"][idx]; old = c["w"]; words = text.split()
    if not words: raise ValueError("النص فاضي — للحذف استخدم حذف الجملة")
    if len(words) == len(old):
        for w, t in zip(old, words): w["t"] = t
        return
    if len(words) < len(old):                       # حذف فقط؟ طابق الباقي بالترتيب
        j = 0; keep = []
        for w in old:
            if j < len(words) and w["t"] == words[j]: keep.append(w); j += 1
        if j == len(words): c["w"] = keep; return
    s0, e1 = old[0]["s"], old[-1]["e"]; span = max(0.12 * len(words), e1 - s0)
    tot = sum(len(w) + 1 for w in words); acc = 0.0; out = []
    hot = {w["t"]: w for w in old if w.get("hot") or w.get("fx")}
    for w in words:
        d = span * (len(w) + 1) / tot
        n = {"t": w, "s": round(s0 + acc, 3), "e": round(s0 + acc + d, 3), "hot": False}
        if w in hot:
            n["hot"] = bool(hot[w].get("hot"))
            if hot[w].get("fx"): n["fx"] = hot[w]["fx"]
        out.append(n); acc += d
    c["w"] = out

def apply_text(work, i, text):
    cp = J(work, "caps.json"); sp = J(work, "studio.json")
    caps = rj(cp); old = card_key(caps["cards"][i]); new = " ".join(str(text).split())
    set_card_text(caps, i, new); wj(cp, caps)
    st = load_studio(work); hs = hs_of(st); ed = hs.setdefault("edits", {})
    src = next((k for k, v in ed.items() if v == old), old); ed[src] = new
    mp = (hs.get("en") or {}).get("map") or {}
    if old in mp and new != old: mp[new] = mp.pop(old)
    ov = hs.get("capOv") or {}
    if old in ov and new != old: ov[new] = ov.pop(old)
    wj(sp, st); return caps, hs

# ───────────────────────── الفحص: احتفاظ + حشو + إعادات ─────────────────────────
def _norm(w):
    w = re.sub(r"[\u064B-\u0652\u0640]", "", w)
    w = w.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ة", "ه").replace("ى", "ي")
    return re.sub(r"[^\w]", "", w)
_STOP = {"في", "من", "علي", "الي", "عن", "مع", "هذا", "هذي", "هذه", "ذلك", "اللي", "الي", "و", "او", "ثم", "بس", "يا", "ان", "ما", "لا", "كل", "كان", "صار", "هو", "هي"}
def _sim(a, b):
    wa, wb = [w for w in a if w not in _STOP], [w for w in b if w not in _STOP]
    if not wa or not wb: return 0.0
    shared = len(set(wa) & set(wb)) / min(len(wa), len(wb))
    return max(shared, difflib.SequenceMatcher(None, " ".join(a), " ".join(b)).ratio())
_PV = {"busy": False}
def pv_build(work):
    """يبني فريمات المعاينة المصغّرة بالخلفية مرة وحدة (ويعيدها لو تغيّر القص)."""
    if _PV["busy"] or not shutil.which("ffmpeg"): return
    _PV["busy"] = True
    def go():
        try:
            out = J(work, ".hs", "pv"); os.makedirs(out, exist_ok=True)
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-start_number", "1", "-i", J(work, "vfr", "%05d.jpg"), "-vf", "scale=540:-2", "-q:v", "5", "-start_number", "1", os.path.join(out, "%05d.jpg")], capture_output=True)
            n = len(glob.glob(J(work, "vfr", "*.jpg")))
            for f in glob.glob(os.path.join(out, "*.jpg")):
                if int(re.sub(r"\D", "", os.path.basename(f)) or 0) > n: os.remove(f)
        finally: _PV["busy"] = False
    threading.Thread(target=go, daemon=True).start()
def vsig(work):
    try: return "%x" % int(os.path.getmtime(J(work, "cutz.mp4")) * 10) + "-" + str(int((rj(J(work, ".hs", "enhance.json"), {}) or {}).get("at") or 0) % 100000)
    except OSError: return "0"
def keep_seams(work):
    keep = (rj(J(work, "cut.json"), {}) or {}).get("keep") or []; acc = 0.0; out = []
    for a, b in keep[:-1]: acc += b - a; out.append(round(acc, 3))
    return out
def open_check(first, ev, hs, total):
    """أول 3 ثواني (نسبة التخطي بانستقرام = اللي يسحب قبل الثانية 3). يرجع قائمة النواقص: voice · change · text."""
    if total < 6: return {"miss": [], "first": first, "changes": 0}
    ch = [x for x in ev if 0.3 < x <= 3.0]; hk = hs.get("hooks") or {}
    txt = bool(hk.get("on") and hk.get("items")) or any(not L.get("off") and L.get("type") in ("text", "cover", "lt") and float(L.get("s", 0)) <= 1.0 for L in hs.get("layers") or [])
    miss = (["voice"] if (first is not None and 0.7 < first <= 1.0) else []) + ([] if ch else ["change"]) + ([] if txt else ["text"])
    return {"miss": miss, "first": first, "changes": len(ch)}
def len_check(total, plats):
    """مدة المقطع مقابل كل منصة مختارة: over = يتعدى الحد · long/short = برا المدى الأنسب."""
    out = []
    for n in plats or []:
        P_ = PLATFORMS.get(n)
        if not P_ or not total: continue
        lo, hi = P_["bestS"]
        k = "over" if total > P_["maxS"] else "long" if total > hi * 1.5 else "short" if total < lo * 0.6 else None
        if k: out.append({"p": n, "k": k, "max": P_["maxS"], "lo": lo, "hi": hi})
    return out
def check(work):
    caps = rj(J(work, "caps.json"), {"cards": [], "total": 0}); cards = caps["cards"]; total = caps.get("total", 0)
    st = load_studio(work); hs = st.get("hs") or {}; cfg = hs.get("check") or {}
    gap = float(cfg.get("gap", 2.5)); maxw = int(cfg.get("maxWords", 10)); extra = [_norm(x) for x in (cfg.get("fillers") or [])]
    fl = set(_norm(x) for x in FILLERS) | set(extra)
    fillers = [{"card": i, "idx": j, "t": w["t"], "s": w["s"], "e": w["e"]} for i, c in enumerate(cards) for j, w in enumerate(c["w"]) if _norm(w["t"]) in fl and len(c["w"]) > 1]
    dupes = []   # 4.5: كل مجموعة إعادات نخلي فيها الأحسن (مو دايم الأخيرة)
    for g in takes(work):
        for i in g["cards"]:
            if i != g["keep"]: dupes.append({"a": i, "b": g["keep"], "r": round(_sim([_norm(w["t"]) for w in cards[i]["w"]], [_norm(w["t"]) for w in cards[g["keep"]]["w"]]), 2), "why": g["why"], "group": g["cards"]})
    ev = [0.0] + keep_seams(work)                                   # كل لحمة قص = تغيّر زوم
    for s in st.get("scenes") or []: ev += [s.get("s", 0)]
    for k in ("brollClips", "stickers"):
        for b in st.get(k) or []: ev += [b.get("s", 0), b.get("e", 0)]
    for L in hs.get("layers") or []:
        if L.get("off"): continue
        ev += [L.get("s", 0)] + ([] if L.get("type") == "fx" else [L.get("e", 0)])
    hk = hs.get("hooks") or {}
    if hk.get("on") and hk.get("items"): ev += [0.0, hk.get("dur", 2.6)]
    if cfg.get("caps"): ev += [c["s"] for c in cards]
    ev = sorted(set(round(x, 2) for x in ev if 0 <= x < total)) + [total]
    gaps = [{"s": a, "e": b, "d": round(b - a, 2)} for a, b in zip(ev, ev[1:]) if b - a > gap]
    long_caps = [{"card": i, "n": len(c["w"])} for i, c in enumerate(cards) if len(c["w"]) > maxw]
    first = cards[0]["w"][0]["s"] if cards else None
    issues = len(gaps) + len(long_caps) + (1 if (first is not None and first > 1.0) else 0)
    score = max(0, 100 - 6 * len(gaps) - 4 * len(long_caps) - (15 if (first is not None and first > 1.0) else 0) - int(sum(g["d"] - gap for g in gaps) * 2))
    try: tips = flow_tips(work, ev, total, hs)
    except Exception: tips = []
    try: xs = {"unsure": sum(1 for c in cards for w in c["w"] if w.get("lo")), "speechGaps": caps_gaps(work)[:12], "cutSound": len(cut_on_sound(work)[0]), "facts": facts(work)[:12]}   # 4.10
    except Exception: xs = {"unsure": 0, "speechGaps": [], "cutSound": 0, "facts": []}
    return {"gap": gap, "words": maxw, "fillers": fillers, "dupes": dupes, "gaps": gaps, "longCaps": long_caps, "firstCap": first, "issues": issues, "score": score, "total": total, "tips": tips,
            "open": open_check(first, ev, hs, total), "len": len_check(total, hs.get("platforms")), **xs}

# ───────────────────────── قص مقاطع من الفيديو (حشو · إعادات · بليد) ─────────────────────────
def snapshot(work, name):
    vid = time.strftime("%Y%m%d-%H%M%S"); vd = J(work, ".hs", "versions", vid); n = 1
    while os.path.exists(vd): vd = J(work, ".hs", "versions", vid + "-%d" % n); n += 1
    os.makedirs(vd)
    for f in SNAP_FILES:
        if os.path.exists(J(work, f)): shutil.copy(J(work, f), os.path.join(vd, f))
    wj(os.path.join(vd, "meta.json"), {"name": (name or "نسخة")[:60], "at": time.strftime("%Y-%m-%d %H:%M")}); return os.path.basename(vd)

# ───────────────────────── 4.14: سجل التراجع على القرص ─────────────────────────
# كل تغيير (منك بالاستوديو، أو من Claude، أو قص) ينحفظ خطوة بـ .hs/hist، فالتراجع يشتغل حتى بعد ما تقفل الاستوديو أو تحدّث الصفحة.
# الخطوة = نسخة الملفات اللي تغيّرت قبل التغيير. التراجع يرجّعها ويحط الحالية بالإعادة، ولو تغيّر القص يعيد بناء الفيديو.
HIST_FILES = SNAP_FILES
HIST_MAX = 300
HSTL = threading.Lock()
def _hdir(work, sub=""):
    d = J(work, ".hs", "hist", sub) if sub else J(work, ".hs", "hist"); os.makedirs(d, exist_ok=True); return d
def hist_state(work):
    out = {}
    for f in HIST_FILES:
        try: out[f] = open(J(work, f), encoding="utf-8").read() if os.path.isfile(J(work, f)) else None
        except Exception: out[f] = None
    return out
def _hsame(a, b):
    if a == b: return True
    if a is None or b is None: return False
    try: return json.loads(a) == json.loads(b)
    except Exception: return False
def _hlist(work, sub): return sorted(x for x in os.listdir(_hdir(work, sub)) if x.endswith(".json"))
def _hwrite(path, obj):
    tmp = path + ".tmp"; open(tmp, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False)); os.replace(tmp, path)
def _hpush(work, sub, entry):
    names = _hlist(work, sub); n = int(names[-1][:-5]) + 1 if names else 1
    _hwrite(os.path.join(_hdir(work, sub), "%07d.json" % n), entry)
    for old in names[:max(0, len(names) + 1 - HIST_MAX)]:
        try: os.remove(os.path.join(_hdir(work, sub), old))
        except OSError: pass
def _hpop(work, sub):
    names = _hlist(work, sub)
    if not names: return None
    p = os.path.join(_hdir(work, sub), names[-1]); e = rj(p, None)
    try: os.remove(p)
    except OSError: pass
    return e
def hist_checkpoint(work, why="تعديل"):
    """يقارن الملفات بآخر حالة انحفظت بالسجل. لو فيه فرق، الحالة القديمة تصير خطوة تقدر ترجع لها."""
    with HSTL:
        cur_p = os.path.join(_hdir(work), "cur.json"); now = hist_state(work); last = rj(cur_p, None)
        if not isinstance(last, dict): _hwrite(cur_p, now); return False
        ch = {f: last.get(f) for f in HIST_FILES if not _hsame(last.get(f), now.get(f))}
        if not ch: return False
        _hpush(work, "undo", {"files": ch, "why": why, "at": time.strftime("%H:%M:%S")})
        for x in _hlist(work, "redo"):
            try: os.remove(os.path.join(_hdir(work, "redo"), x))
            except OSError: pass
        _hwrite(cur_p, now); return True
def hist_step(work, back=True):
    """تراجع (back) أو إعادة. يرجّع (تم؟، القص تغيّر؟، وش كانت الخطوة)."""
    hist_checkpoint(work, "تعديل من Claude")
    with HSTL:
        src, dst = ("undo", "redo") if back else ("redo", "undo")
        e = _hpop(work, src)
        if not e or not isinstance(e.get("files"), dict): return False, False, ""
        media_pin(work); old_keep = (rj(J(work, "cut.json"), {}) or {}).get("keep"); now = hist_state(work)
        _hpush(work, dst, {"files": {f: now.get(f) for f in e["files"]}, "why": e.get("why"), "at": e.get("at")})
        for f, txt in e["files"].items():
            if f not in HIST_FILES: continue
            p = J(work, f)
            if txt is None:
                if os.path.isfile(p): os.remove(p)
            else:
                tmp = p + ".tmp"; open(tmp, "w", encoding="utf-8").write(txt); os.replace(tmp, p)
        _hwrite(os.path.join(_hdir(work), "cur.json"), hist_state(work))
        changed = (rj(J(work, "cut.json"), {}) or {}).get("keep") != old_keep
        return True, changed and not media_map(work)[0], e.get("why") or ""   # 4.23: يعيد البناء بس لو الفيديو الحالي ما يغطي القص
def hist_counts(work): return len(_hlist(work, "undo")), len(_hlist(work, "redo"))
HIST_WHY = {"/api/save": "تعديل", "/hs/remove": "قص", "/hs/move_shot": "نقل لقطة", "/hs/takes_apply": "اختيار الجمل", "/hs/cuts_fix": "تصليح القص", "/hs/ver_restore": "استرجاع نسخة",
            "/hs/takes_set": "اختيار الجمل", "/hs/plan_set": "الخطة", "/hs/plan_build": "بناء الخطة", "/hs/unsure": "الكلمات المشكوك فيها", "/hs/rmbg": "شيل الخلفية", "/hs/sv": "صوت استوديو"}
def cmd_undo(work, back=True):
    ok, rb, why = hist_step(work, back)
    if not ok: print("ما فيه خطوة " + ("ترجع لها." if back else "تعيدها.")); return
    if rb:
        eng = find_engine(None) or sys.exit("ما لقيت مجلد engine")
        rebuild_video(work, os.path.join(eng, "scripts"), lambda m: None)
    u, r = hist_counts(work); print(("رجعت: " if back else "أعدت: ") + (why or "تعديل") + ("، وأعدت بناء الفيديو" if rb else "") + ". (باقي %d للتراجع، %d للإعادة)" % (u, r))

def run(cmd, log, cwd=None, check=True, env=None):
    log("$ " + " ".join(os.path.basename(str(c)) if os.sep in str(c) else str(c) for c in cmd)[:220])
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd, env=env, encoding="utf-8", errors="replace")
    out = ((r.stdout or "") + (r.stderr or "")).strip()
    if out: log(out[-700:])
    if check and r.returncode: raise RuntimeError(os.path.basename(str(cmd[1] if len(cmd) > 1 else cmd[0])) + " فشل: " + out[-300:])
    return r

# ── 4.23: القص الفوري: القص يغيّر الكابشن والطبقات والتايم لاين على طول، والمعاينة تعرض من الفيديو الحالي وتتخطّى المقصوص.
#    الفيديو ينبني من جديد بس وقت التصدير (أو لو رجّعت جزء مو موجود بالفيديو الحالي). .hs/media.json = القص اللي انبنى منه cutz.mp4 (برّا التراجع والنسخ).
def _segs(keep): return [(float(a), float(b)) for a, b in (keep or [])]
def media_path(work): return J(work, ".hs", "media.json")
def media_pin(work):
    """لو ما ندري الفيديو انبنى من أي قص: هو القص الحالي (قبل ما يتغيّر)."""
    if os.path.isfile(media_path(work)): return
    k = (rj(J(work, "cut.json"), {}) or {}).get("keep")
    if k: os.makedirs(J(work, ".hs"), exist_ok=True); wj(media_path(work), {"keep": k})
def media_map(work):
    """(الفيديو الحالي يغطي القص؟، خريطة [بداية جديدة، نهاية جديدة، بداية بالفيديو] أو None لو مطابق)."""
    keep = _segs((rj(J(work, "cut.json"), {}) or {}).get("keep")); med = _segs((rj(media_path(work), {}) or {}).get("keep")) or keep
    if not keep: return True, None
    if len(keep) == len(med) and all(abs(a - c) < 1e-3 and abs(b - d) < 1e-3 for (a, b), (c, d) in zip(keep, med)): return True, None
    mo, acc = [], 0.0
    for a, b in med: mo.append(acc); acc += b - a
    out, nacc = [], 0.0
    for a, b in keep:
        x = a
        while x < b - 1e-4:
            j = next((i for i, (ma, mb) in enumerate(med) if ma - 0.06 <= x < mb - 1e-4), None)   # القص يلقط الحدود على الفريمات: فرق أقل من فريمين عادي
            if j is None: return False, None
            ma, mb = med[j]; y = b if b - mb <= 0.06 else mb; o = mo[j] + min(max(0.0, x - ma), mb - ma)
            if out and abs(out[-1][1] - nacc) < 1e-4 and abs(out[-1][2] + (out[-1][1] - out[-1][0]) - o) < 2e-3: out[-1][1] = round(nacc + (y - x), 4)
            else: out.append([round(nacc, 4), round(nacc + (y - x), 4), round(o, 4)])
            nacc += y - x; x = y
    return True, out
def ensure_media(work, S, log):
    """قبل التصدير: لو الفيديو مبني من قص قديم يتبني من جديد. يرجّع True لو بناه."""
    ok, vm = media_map(work)
    if ok and vm is None: return False
    log("أركّب الفيديو على آخر قص (القص كان فوري بالاستوديو)…"); rebuild_video(work, S, log); return True
# ── 4.23: تنقل لقطة لمكان ثاني: الترتيب يتغيّر بالقص نفسه، والكابشن والطبقات والمؤثرات تمشي معها، والمعاينة فورية ──
def move_shot(work, s, e, to):
    cut_init(work); cm = cutmap_mod(); cut = rj(J(work, "cut.json")); keep = [list(map(float, x)) for x in cut["keep"]]; off, total = cm.offsets(keep)
    s, e, to = max(0.0, float(s)), min(total, float(e)), min(max(0.0, float(to)), total)
    if e - s < 0.1: raise ValueError("اللقطة قصيرة")
    if s - 0.01 <= to <= e + 0.01: raise ValueError("نفس مكانها")
    def split_at(k, t):
        o_, _ = cm.offsets(k)
        for i, ((a, b), o) in enumerate(zip(k, o_)):
            if o + 1e-4 < t < o + (b - a) - 1e-4: x = round(a + (t - o), 6); return k[:i] + [[a, x], [x, b]] + k[i + 1:]
        return k
    for t in (s, e, to): keep = split_at(keep, t)
    off, _ = cm.offsets(keep); segs = [(o, o + (b - a), [a, b]) for (a, b), o in zip(keep, off)]
    mid = [g for g in segs if g[0] >= s - 1e-4 and g[1] <= e + 1e-4]; rest = [g for g in segs if g not in mid]
    if not mid: raise ValueError("ما لقيت اللقطة")
    idx = next((i for i, g in enumerate(rest) if g[0] >= to - 1e-4), len(rest)); order = rest[:idx] + mid + rest[idx:]
    ns, acc = {}, 0.0
    for g in order: ns[g[0]] = acc; acc += g[1] - g[0]
    def remap(t, mode=None):
        for g in segs:
            if g[0] - 1e-6 <= t < g[1] - 1e-6 or (g is segs[-1] and t <= g[1] + 1e-6): return round(ns[g[0]] + (t - g[0]), 3)
        return t
    media_pin(work); snapshot(work, "قبل نقل اللقطة (تلقائي)")
    bounds = sorted({round(x, 4) for x in (s, e, to)})
    caps = rj(J(work, "caps.json")); cards = []
    for c in caps.get("cards") or []:   # الجملة اللي يمر فيها حد اللقطة تنقسم عنده
        grp = []
        for w in c.get("w") or []:
            if grp and any(grp[-1]["e"] <= b + 1e-3 and (w["s"] + w["e"]) / 2 > b for b in bounds): cards.append({**c, "w": grp}); grp = []
            grp.append(w)
        if grp: cards.append({**c, "w": grp})
    out = []
    for c in cards:
        ws = c["w"]; lead = min(0.3, max(0.0, ws[0]["s"] - c.get("s", ws[0]["s"]))) if len(ws) == len(c["w"]) else 0.05; tail = min(0.5, max(0.0, c.get("e", ws[-1]["e"]) - ws[-1]["e"]))
        nw = [{**w, "s": remap(w["s"]), "e": round(remap(w["s"]) + (w["e"] - w["s"]), 3)} for w in ws]
        out.append({**c, "s": round(max(0.0, nw[0]["s"] - lead), 3), "e": round(nw[-1]["e"] + tail, 3), "w": nw})
    out.sort(key=lambda c: c["s"])
    for i in range(len(out) - 1):
        if out[i]["e"] > out[i + 1]["s"] - 0.02: out[i]["e"] = round(max(out[i]["w"][-1]["e"], out[i + 1]["s"] - 0.02), 3)
    wj(J(work, "caps.json"), {**caps, "cards": out})
    cut["keep"] = [g[2] for g in order]; cut["edited"] = True; wj(J(work, "cut.json"), cut)
    # الطبقات والمؤثرات وغيرها: بدايتها تمشي مع اللقطة ومدتها نفسها (الثابتة بثانيتها ما تتحرك)
    st = load_studio(work); hs = hs_of(st); pin_all = hs.get("pinLayers", True) is not False
    def mvd(x):
        s0 = float(x.get("s", 0)); d = float(x.get("e", 0)) - s0; s1 = remap(s0); return {**x, "s": round(s1, 3), "e": round(min(total, s1 + d), 3)}
    hs["layers"] = [mvd(x) if (x.get("pin") if x.get("pin") is not None else pin_all) else x for x in hs.get("layers") or []]
    for k in ("blank",): hs[k] = sorted([mvd(x) for x in hs.get(k) or []], key=lambda x: x["s"]) if hs.get(k) else hs.get(k)
    if (hs.get("mix") or {}).get("vr"): hs["mix"]["vr"] = sorted([mvd(x) for x in hs["mix"]["vr"]], key=lambda x: x["s"])
    if (hs.get("bleep") or {}).get("items"): hs["bleep"]["items"] = sorted([mvd(x) for x in hs["bleep"]["items"]], key=lambda x: x["s"])
    for k in ("stickers", "brollClips"):
        if st.get(k): st[k] = sorted([mvd(x) for x in st[k]], key=lambda x: x["s"])
    if hs.get("marks"): hs["marks"] = []
    wj(J(work, "studio.json"), st)
    sfx = rj(J(work, "sfx.json"), None)
    if sfx is not None:
        for k, v in list(sfx.items()):
            if isinstance(v, list): sfx[k] = sorted([([remap(t[0])] + list(t[1:])) if isinstance(t, list) else remap(t) for t in v], key=lambda t: t[0] if isinstance(t, list) else t)
        wj(J(work, "sfx.json"), sfx)
    return {"to": remap(s), "n": len(mid)}
# ── 4.26: الدبلجة: سكربت بتوقيت كل جملة وسكتتها، صوت لكل جملة (ElevenLabs من حسابه أو ملف يجيبه)، ويتركّب بنفس السكتات والصوت الأصلي ينشال ──
DUB_LANGS = {"ar": "العربية", "en": "الإنجليزية", "es": "الإسبانية", "fr": "الفرنسية", "de": "الألمانية", "tr": "التركية", "ur": "الأوردو", "hi": "الهندية", "id": "الإندونيسية", "pt": "البرتغالية", "it": "الإيطالية", "ru": "الروسية", "zh": "الصينية", "ja": "اليابانية", "ko": "الكورية"}
DUB_WPS = {"ar": 2.3, "en": 2.6, "es": 2.8, "fr": 2.7, "de": 2.3}
def dub_path(work): return J(work, "dub.json")
def dub_get(work): return rj(dub_path(work), None)
def dub_script(work, lang):
    """يكتب dub.json وdub-script.txt: كل جملة بوقتها ومدتها والسكتة اللي بعدها، وكم كلمة تقريباً تتسع."""
    if lang not in DUB_LANGS: raise ValueError("اللغة لازم وحدة من: " + " · ".join(DUB_LANGS))
    cards = (rj(J(work, "caps.json"), {}) or {}).get("cards") or []
    if not cards: raise ValueError("ما فيه كابشن بالمشروع")
    old = {x.get("key"): x for x in ((dub_get(work) or {}).get("segs") or [])}
    segs = []
    for i, c in enumerate(cards):
        k = card_key(c); s0, e0 = float(c["w"][0]["s"]), float(c["w"][-1]["e"]); nxt = float(cards[i + 1]["w"][0]["s"]) if i + 1 < len(cards) else e0 + 1.0
        o = old.get(k) or {}
        segs.append({"i": i, "key": k, "s": round(s0, 3), "e": round(e0, 3), "pause": round(max(0.0, nxt - e0), 2), "words": max(1, round((e0 - s0) * DUB_WPS.get(lang, 2.5))), "tr": o.get("tr", ""), "file": o.get("file")})
    D = {"lang": lang, "segs": segs, "at": int(time.time())}; wj(dub_path(work), D); dub_txt(work, D); return D
def dub_txt(work, D=None):
    D = D or dub_get(work) or {}; L = ["سكربت الدبلجة (%s): كل جملة بوقتها. خلّ الترجمة بنفس الطول تقريباً، والسكتة بعدها نفسها." % DUB_LANGS.get(D.get("lang"), D.get("lang")), ""]
    for x in D.get("segs") or []:
        L.append("#%d  %d:%04.1f ← %d:%04.1f  (%.1f ث، تقريباً %d كلمة)  ثم سكتة %.1f ث" % (x["i"] + 1, x["s"] // 60, x["s"] % 60, x["e"] // 60, x["e"] % 60, x["e"] - x["s"], x["words"], x["pause"]))
        L.append("    الأصل: " + x["key"]); L.append("    الدبلجة: " + (x.get("tr") or "…")); L.append("")
    open(J(work, "dub-script.txt"), "w", encoding="utf-8").write("\n".join(L)); return J(work, "dub-script.txt")
def dub_import(work, items):
    D = dub_get(work) or {}; S = {x["i"]: x for x in D.get("segs") or []}; n = 0
    for it in items or []:
        x = S.get(int(it.get("i", -1)))
        if x is not None and isinstance(it.get("tr"), str): x["tr"] = it["tr"].strip(); n += 1
    wj(dub_path(work), D); dub_txt(work, D)
    st = load_studio(work); en = hs_of(st).setdefault("en", {}); mp = en.setdefault("map", {})
    for x in D.get("segs") or []:
        if x.get("tr"): mp[x["key"]] = x["tr"]
    en["on"] = True; wj(J(work, "studio.json"), st); return n
def dub_add(work, i, src):
    D = dub_get(work) or {}; x = next((y for y in D.get("segs") or [] if y["i"] == int(i)), None)
    if x is None: raise ValueError("ما فيه جملة رقم %s" % i)
    os.makedirs(J(work, "dub"), exist_ok=True); dst = J(work, "dub", "%03d%s" % (int(i), os.path.splitext(src)[1].lower() or ".mp3"))
    if os.path.abspath(src) != os.path.abspath(dst): shutil.copy(src, dst)
    x["file"] = os.path.relpath(dst, work).replace("\\", "/"); wj(dub_path(work), D); return dst
def dub_track(work, src):
    """ملف دبلجة كامل جاهز (من ElevenLabs Dubbing أو سجّله هو) على نفس توقيت المقطع."""
    D = dub_get(work) or {"lang": "", "segs": []}; os.makedirs(J(work, "dub"), exist_ok=True); dst = J(work, "dub", "track" + (os.path.splitext(src)[1].lower() or ".mp3"))
    if os.path.abspath(src) != os.path.abspath(dst): shutil.copy(src, dst)
    D["track"] = os.path.relpath(dst, work).replace("\\", "/"); wj(dub_path(work), D); return dst
def dub_build(work, log=print):
    """يركّب dub.wav على توقيت الفيديو الحالي: كل جملة عند بدايتها، ولو أطول من مكانها (مدتها + سكتتها) تتسرّع لين ×1.3."""
    D = dub_get(work)
    if not D: raise ValueError("ما فيه دبلجة. ابدأ بـ: hs dub <work> script <اللغة>")
    caps = rj(J(work, "caps.json"), {}) or {}; cards = caps.get("cards") or []; total = float(caps.get("total") or 0)
    ok_, vm_ = media_map(work); med = lambda t: next((m0 + max(0.0, t - s0) for s0, e0, m0 in vm_ if t < e0), t) if vm_ else t
    mtot = med(total) if vm_ else total; out = J(work, "dub.wav")
    if D.get("track") and os.path.isfile(J(work, D["track"])):
        run(["ffmpeg", "-v", "error", "-y", "-i", J(work, D["track"]), "-ac", "2", "-ar", "48000", "-af", "apad", "-t", "%.3f" % mtot, out], log); D["built"] = int(time.time()); wj(dub_path(work), D); return out, 0
    pos = {card_key(c): (float(c["w"][0]["s"]), float(c["w"][-1]["e"]), (float(cards[i + 1]["w"][0]["s"]) if i + 1 < len(cards) else total)) for i, c in enumerate(cards)}
    ins, fl, n, miss = [], [], 0, 0
    for x in D.get("segs") or []:
        f = J(work, x["file"]) if x.get("file") else None
        if not f or not os.path.isfile(f) or x["key"] not in pos: miss += 1; continue
        s0, e0, nx = pos[x["key"]]; room = max(0.3, nx - s0 - 0.05); d = ffdur(f) or room; sp = min(1.3, max(1.0, d / room))
        ins += ["-i", f]; fl.append("[%d:a]aresample=48000,aformat=channel_layouts=stereo%s,adelay=%d|%d[d%d]" % (n, (",atempo=%.3f" % sp) if sp > 1.001 else "", int(med(s0) * 1000), int(med(s0) * 1000), n)); n += 1
        if sp >= 1.299: log("تنبيه: الجملة #%d أطول من مكانها حتى بعد التسريع. قصّر ترجمتها." % (x["i"] + 1))
    if not n: raise ValueError("ما فيه ولا ملف صوت للجمل. أضفها بـ: hs dub <work> add <رقم> <ملف>")
    fc = ";".join(fl) + ";" + "".join("[d%d]" % i for i in range(n)) + "amix=inputs=%d:duration=longest:normalize=0,apad,atrim=0:%.3f[o]" % (n, mtot)
    run(["ffmpeg", "-v", "error", "-y"] + ins + ["-filter_complex", fc, "-map", "[o]", "-ac", "2", "-ar", "48000", out], log)
    D["built"] = int(time.time()); wj(dub_path(work), D); return out, miss
def dub_on(work): return bool((hs_of(load_studio(work)).get("mix") or {}).get("dub")) and os.path.isfile(J(work, "dub.wav"))
# ── 4.25: تحسين الجودة: ينظّف التشويش ويحدّد التفاصيل ويرفع الدقة لـ1080 على فيديوك قبل الكابشن والعناصر (فالنص يبقى نظيف) ──
ENH_LEVELS = ("off", "light", "strong")
def enh_level(work):
    l = (hs_of(load_studio(work)).get("enhance") or {}).get("level"); return l if l in ENH_LEVELS else "off"
def vid_size(path):
    try: w, h = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0:s=x", path], capture_output=True, text=True, timeout=30).stdout.strip().split("x")[:2]; return int(w), int(h)
    except Exception: return 0, 0
def enh_filter(level, src_w=0, src_h=0):
    """سلسلة فلاتر ffmpeg (تشتغل بويندوز وماك: كلها فلاتر داخلية، ولو فلتر ناقص ينحط بديله)."""
    if level not in ("light", "strong"): return ""
    f = []
    if src_w and src_h and (src_w < 1080 or src_h < 1920): f.append("scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920")
    if ff_has("hqdn3d"): f.append("hqdn3d=1.5:1.5:6:6" if level == "light" else "hqdn3d=3:2.5:8:8")
    if level == "strong" and ff_has("deband"): f.append("deband")
    f.append(("cas=%.2f" % (0.5 if level == "light" else 0.85)) if ff_has("cas") else ("unsharp=5:5:%.1f:5:5:0" % (0.8 if level == "light" else 1.3)))
    if level == "strong": f.append("unsharp=7:7:0.35:7:7:0")
    f.append("eq=saturation=%.2f:contrast=%.2f" % ((1.05, 1.03) if level == "light" else (1.08, 1.05)))
    return ",".join(f)
def vfr_extract(work, log, level=None):
    """يطلّع فريمات المعاينة والتصدير من cutz.mp4 (بالتحسين لو مشغّل). تنكتب بمجلد مؤقت وتتبدّل مرة وحدة."""
    level = level or enh_level(work); src = J(work, "cutz.mp4"); w, h = vid_size(src); ch = enh_filter(level, w, h)
    new, old = J(work, ".hs", "vfr.new"), J(work, ".hs", "vfr.old")
    shutil.rmtree(new, ignore_errors=True); shutil.rmtree(old, ignore_errors=True); os.makedirs(new)
    if ch: log("أحسّن الجودة (%s)…" % {"light": "خفيف", "strong": "قوي"}[level])
    run(["ffmpeg", "-v", "error", "-i", src, "-vf", "fps=30" + ("," + ch if ch else ""), "-q:v", "2", "-y", os.path.join(new, "%05d.jpg")], log, cwd=work)
    if os.path.isdir(J(work, "vfr")): os.replace(J(work, "vfr"), old)
    os.replace(new, J(work, "vfr")); shutil.rmtree(old, ignore_errors=True)
    os.makedirs(J(work, ".hs"), exist_ok=True); wj(J(work, ".hs", "enhance.json"), {"level": level, "at": int(time.time())})
def quality_preview(work, t, level):
    """قبل وبعد لنفس اللقطة (تفاصيل بالحجم الحقيقي من نص الصورة)."""
    ok, vm = media_map(work); o = float(t)
    if vm:
        for s0, e0, m0 in vm:
            if o < e0: o = m0 + max(0.0, o - s0); break
    src = J(work, "cutz.mp4"); w, h = vid_size(src); ch = enh_filter(level if level in ("light", "strong") else "light", w, h)
    base = "scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920"
    vf = "[0:v]%s,split[o][x];[x]%s[e];[o]crop=540:760:270:520[oc];[e]crop=540:760:270:520[ec];[oc][ec]hstack" % (base, ch or "null")
    out = J(work, ".hs", "qprev.jpg")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "%.3f" % max(0.0, o), "-i", src, "-frames:v", "1", "-filter_complex", vf, "-q:v", "2", out], check=True, timeout=60)
    return out
# ── 4.27: مكان الفيديو بالكادر: تشوف الصورة الأصلية كاملة وتحرك المربع وتكبّر، والفيديو يتقص من الأصل من جديد ──
def vpos_info(work):
    cut_ = rj(J(work, "cut.json"), {}) or {}; src = J(work, "src.mov")
    can = os.path.isfile(src) and cut_.get("src") != "cutz" and bool(cut_.get("keep"))
    sw, sh = vid_size(src) if can else (1080, 1920)
    ks = ((rj(J(work, "reframe.json"), {}) or {}).get("keys") or [])
    return {"ok": True, "can": can, "sw": sw, "sh": sh, "wide": sw / max(1, sh) > 0.75, "vpos": hs_of(load_studio(work)).get("vpos") or {}, "auto": [round(float(k[1]), 3) for k in ks][:12]}
def vpos_thumb(work, t):
    """صورة من الأصل (قبل القص العمودي) عند نفس اللحظة بالتايم لاين."""
    keep = _segs((rj(J(work, "cut.json"), {}) or {}).get("keep")); o = float(t); acc = 0.0; srcT = keep[0][0] if keep else 0.0
    for a, b in keep:
        if o < acc + (b - a): srcT = a + (o - acc); break
        acc += b - a; srcT = b - 0.05
    out = J(work, ".hs", "vthumb.jpg"); os.makedirs(J(work, ".hs"), exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "%.3f" % max(0.0, srcT), "-i", J(work, "src.mov"), "-frames:v", "1", "-vf", "scale=640:-2", "-q:v", "4", out], check=True, timeout=60)
    return out
def vpos_set(work, fr):
    st = load_studio(work); h = hs_of(st)
    if fr is None: h.pop("vpos", None)
    else:
        f = {}
        if fr.get("x") is not None: f["x"] = round(min(1.0, max(0.0, float(fr["x"]))), 4)
        if fr.get("y") is not None: f["y"] = round(min(1.0, max(0.0, float(fr["y"]))), 4)
        f["z"] = round(min(3.0, max(1.0, float(fr.get("z") or 1))), 3)
        if fr.get("still"): f["still"] = True
        h["vpos"] = f
    wj(J(work, "studio.json"), st)
# ── 4.25: مشروع بدون cut.json (مبني بطريقة ثانية، مثل مقاطع الموشن): الفيديو الحالي هو الأصل، والقص والتصدير يشتغلون عليه ──
def cut_init(work):
    if os.path.isfile(J(work, "cut.json")): return False
    cz = J(work, "cutz.mp4"); base = J(work, "src-cutz.mp4")
    if not os.path.isfile(cz) and not os.path.isfile(base): raise ValueError("ما لقيت فيديو المشروع (cutz.mp4)")
    if not os.path.isfile(base): shutil.copy2(cz, base)   # نسخة مو رابط: لو أي أداة كتبت فوق cutz.mp4 الأصل ما يتأثر
    d = round(probe_dur(base) or float((rj(J(work, "caps.json"), {}) or {}).get("total") or 0), 3)
    if d <= 0: raise ValueError("ما قدرت أقرأ مدة الفيديو")
    keep = [[0.0, d]]; wj(J(work, "cut.json"), {"keep": keep, "total": d, "src": "cutz"}); os.makedirs(J(work, ".hs"), exist_ok=True); wj(media_path(work), {"keep": keep}); return True
def _concat_cutz(work, keep, log):
    """يركّب cutz.mp4 من قطع src-cutz.mp4 بالترتيب (بدل 03_cut_zoom اللي يحتاج src.mov)."""
    base = J(work, "src-cutz.mp4"); has_a = "audio" in subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type", "-of", "csv=p=0", base], capture_output=True, text=True).stdout
    fc, ins = [], ""
    for i, (a, b) in enumerate(keep):
        fc.append("[0:v]trim=start=%.4f:end=%.4f,setpts=PTS-STARTPTS[v%d]" % (a, b, i)); ins += "[v%d]" % i
        if has_a: fc.append("[0:a]atrim=start=%.4f:end=%.4f,asetpts=PTS-STARTPTS[a%d]" % (a, b, i)); ins += "[a%d]" % i
    fc.append("%sconcat=n=%d:v=1:a=%d[v]%s" % (ins, len(keep), 1 if has_a else 0, "[a]" if has_a else ""))
    tmp = J(work, ".hs", "cutz.tmp.mp4"); os.makedirs(J(work, ".hs"), exist_ok=True)
    run(["ffmpeg", "-v", "error", "-y", "-i", base, "-filter_complex", ";".join(fc), "-map", "[v]"] + (["-map", "[a]", "-c:a", "aac", "-b:a", "192k"] if has_a else []) + ["-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p", "-r", "30", "-movflags", "+faststart", tmp], log)
    os.replace(tmp, J(work, "cutz.mp4")); wj(media_path(work), {"keep": [list(map(float, x)) for x in keep]})
    log("✅ cutz.mp4 من %d قطعة" % len(keep))
def rebuild_video(work, S, log):
    cut_ = rj(J(work, "cut.json"), {}) or {}
    if cut_.get("src") == "cutz" and os.path.isfile(J(work, "src-cutz.mp4")): log("أركّب الفيديو من القطع…"); _concat_cutz(work, cut_["keep"], log)
    else: log("أقص وأركّب الفيديو من جديد…"); run([PY, os.path.join(S, "03_cut_zoom.py"), work], log, cwd=work)
    log("أطلّع الفريمات…"); vfr_extract(work, log)
    for f in ("behind.json", "sfx.wav"):
        try: os.remove(J(work, f))
        except FileNotFoundError: pass
    shutil.rmtree(J(work, "bt"), ignore_errors=True); shutil.rmtree(J(work, "out"), ignore_errors=True); vision_reset(work)

_CM = None
def cutmap_mod():
    """engine/scripts/cutmap.py (خريطة القص المشتركة مع 10_script_edit)."""
    global _CM
    if _CM is None:
        eng = find_engine(None) or sys.exit("ما لقيت مجلد engine")
        spec = importlib.util.spec_from_file_location("hs_cutmap", os.path.join(eng, "scripts", "cutmap.py")); _CM = importlib.util.module_from_spec(spec); spec.loader.exec_module(_CM)
    return _CM
def retime_project(work, remap, total, new_total):
    """بعد أي تغيير بالقص: المؤثرات والمشاهد والطبقات والكلمات المكتومة تمشي لوقتها الجديد. remap(t, mode) = الوقت الجديد أو None لو انشال."""
    shift = lambda t: (lambda v: round(v, 3) if v is not None else round(remap(t, "prev"), 3))(remap(t))
    inside = lambda t: remap(t) is None
    sfx = rj(J(work, "sfx.json"), None)
    if sfx is not None:
        for k, v in list(sfx.items()):
            if isinstance(v, list): sfx[k] = [([shift(t[0])] + list(t[1:])) if isinstance(t, list) else shift(t) for t in v if not inside(t[0] if isinstance(t, list) else t)]
        wj(J(work, "sfx.json"), sfx)
    st = load_studio(work); hs = hs_of(st)
    def mv(arr):
        o = []
        for x in arr or []:
            s0, e0 = remap(x.get("s", 0), "next"), remap(x.get("e", 0), "prev")
            if s0 is not None and e0 is not None and e0 - s0 > 0.15: o.append({**x, "s": round(s0, 3), "e": round(e0, 3)})
        return o
    if st.get("scenes"):
        sc = mv(st["scenes"])
        if sc: sc[0]["s"] = 0
        if sc and st["scenes"][-1].get("e", 0) >= total - 0.05: sc[-1]["e"] = new_total + 5
        st["scenes"] = sc
    for k in ("stickers", "brollClips"):
        if st.get(k): st[k] = mv(st[k])
    if hs.get("layers"):   # 4.20: المربوطة باللقطة تمشي معها، والثابتة تبقى بثانيتها
        pin_all = hs.get("pinLayers", True) is not False; out = []
        for x in hs["layers"]:
            if (x.get("pin") if x.get("pin") is not None else pin_all): out += mv([x])
            elif float(x.get("s", 0)) < new_total - 0.1: out.append({**x, "e": round(min(float(x.get("e", 0)), new_total), 3)})
        hs["layers"] = out
    if (hs.get("bleep") or {}).get("items"):   # 4.6: الكلمات المكتومة تزحف مع القص
        hs["bleep"]["items"] = [{**x, "s": shift(float(x["s"])), "e": shift(float(x["e"]))} for x in hs["bleep"]["items"] if shift(float(x["e"])) - shift(float(x["s"])) >= 0.04]
    if (hs.get("mix") or {}).get("vr"):   # 4.11: مستوى صوت الأجزاء يزحف مع القص
        hs["mix"]["vr"] = [{**x, "s": shift(float(x["s"])), "e": shift(float(x["e"]))} for x in hs["mix"]["vr"] if shift(float(x["e"])) - shift(float(x["s"])) >= 0.04]
    if hs.get("blank"):   # 4.14: أجزاء «الصورة بس انحذفت» تزحف مع القص
        hs["blank"] = [{**x, "s": shift(float(x["s"])), "e": shift(float(x["e"]))} for x in hs["blank"] if shift(float(x["e"])) - shift(float(x["s"])) >= 0.04]
    if hs.get("marks"): hs["marks"] = []   # علامات القص اليدوية تنمسح بعد أي قص (مكانها تغيّر)
    st["behindOff"] = []; wj(J(work, "studio.json"), st)
def remove_ranges(work, S, log, ranges=(), cards=(), words=(), rebuild=True):
    """يشيل مقاطع (بزمن الإخراج) من الفيديو والصوت، ويزحّف كل شي بعدها: الكابشن · المؤثرات · المشاهد · الطبقات."""
    caps = rj(J(work, "caps.json")); cs = caps["cards"]; total = caps["total"]; iv = []
    for a, b in ranges: iv.append([max(0.0, float(a)), min(total, float(b))])
    drop_cards = set(int(i) for i in cards); drop_words = set((int(i), int(j)) for i, j in words)
    for i in sorted(drop_cards):
        c = cs[i]; a = max(0.0, c["w"][0]["s"] - 0.08); b = min(total, c["w"][-1]["e"] + 0.12)
        if i + 1 < len(cs): b = min(b, cs[i + 1]["w"][0]["s"] - 0.02)
        if i > 0: a = max(a, cs[i - 1]["w"][-1]["e"] + 0.02)
        if b > a: iv.append([a, b])
    for i, j in sorted(drop_words):
        if i in drop_cards: continue
        ws = cs[i]["w"]; w = ws[j]
        a = ws[j - 1]["e"] if j > 0 else max(0.0, w["s"] - 0.04)
        b = ws[j + 1]["s"] if j + 1 < len(ws) else min(total, w["e"] + 0.04)
        a = min(a, w["s"]); b = max(b, w["e"]); a = max(a, w["s"] - 0.25); b = min(b, w["e"] + 0.25)
        if b > a: iv.append([a, b])
    iv = sorted(x for x in iv if x[1] - x[0] > 0.03)
    if not iv: raise ValueError("ما فيه شي ينشال")
    # 4.9: الحذف يمر من خريطة القص: كل وقت ينحسب من مكانه بالأصل، وحدود القص على أهدأ نقطة، فالكابشن ما يتأخر ولا يبقى كابشن لكلام انشال
    cut_init(work); media_pin(work); cm = cutmap_mod(); cut = rj(J(work, "cut.json")); keep = [list(x) for x in cut["keep"]]
    guards = [(w["s"], w["e"]) for i, c in enumerate(cs) if i not in drop_cards for j, w in enumerate(c["w"]) if (i, j) not in drop_words and not any(a <= (w["s"] + w["e"]) / 2 <= b for a, b in iv)]
    new_keep, remap, gone = cm.remove(work, keep, iv, guards)
    new_total = round(sum(b - a for a, b in new_keep), 3)
    if new_total < 1.0: raise ValueError("بيبقى أقل من ثانية — ما أقدر أشيل كل هذا")
    snapshot(work, "قبل القص (تلقائي)")
    shift = lambda t: (lambda v: round(v, 3) if v is not None else round(remap(t, "prev"), 3))(remap(t))
    inside = lambda t: remap(t) is None
    cut["keep"] = new_keep; cut["total"] = new_total; cut["edited"] = True; wj(J(work, "cut.json"), cut)
    kept = {"total": total, "cards": [{**c, "w": [w for j, w in enumerate(c["w"]) if (i, j) not in drop_words]} for i, c in enumerate(cs) if i not in drop_cards]}
    kept["cards"] = [c for c in kept["cards"] if c["w"]]
    wj(J(work, "caps.json"), cm.remap_caps(kept, remap, new_total))
    retime_project(work, remap, total, new_total)
    log("انشال %.2f ثانية: المدة %.2f ← %.2f" % (gone, total, new_total))
    if rebuild: rebuild_video(work, S, log)
    return {"gone": round(gone, 2), "total": new_total}

# ───────────────────────── 4.10: اختيار الجمل (الإعادات والتلعثم من التسجيل الخام) ─────────────────────────
_TK = None
def takes_mod():
    """engine/scripts/takes.py"""
    global _TK
    if _TK is None:
        eng = find_engine(None) or sys.exit("ما لقيت مجلد engine")
        spec = importlib.util.spec_from_file_location("hs_takes", os.path.join(eng, "scripts", "takes.py")); _TK = importlib.util.module_from_spec(spec); spec.loader.exec_module(_TK)
    return _TK
def _src_dur(work):
    cut = rj(J(work, "cut.json"), {}) or {}
    if cut.get("src_dur"): return float(cut["src_dur"])
    a = rj(J(work, "a.json"), {}) or {}; ws = [w for s in a.get("segments") or [] for w in s.get("words") or []]
    return float(ws[-1]["end"]) if ws else 0.0
def tk_base(work):
    """قص السكتات قبل اختيار الجمل (ينحفظ أول مرة)."""
    b = rj(J(work, "cut.base.json"), None)
    if b and b.get("keep"): return [list(x) for x in b["keep"]]
    cut = rj(J(work, "cut.json"), None)
    if cut and cut.get("keep"): wj(J(work, "cut.base.json"), {"keep": cut["keep"], "total": cut.get("total"), "src_dur": cut.get("src_dur")}); return [list(x) for x in cut["keep"]]
    d = _src_dur(work); return [[0.0, d]] if d else []
def tk_scan(work):
    T = takes_mod(); cm = cutmap_mod()
    a = rj(J(work, "a.json"), None) or sys.exit("ما فيه a.json (التفريغ). فرّغ أول")
    data = T.scan(T.words_of(a, rj(J(work, "fixes.json"), None)), cm.env(work))
    tk_base(work); data.update(raw=round(_src_dur(work), 2), at=int(time.time()), by="auto", note="")
    old = rj(J(work, "takes.json"), None)
    if old and old.get("applied"): data["applied"] = old["applied"]
    tk_farrep(data); data["summary"] = T.summary(data); wj(J(work, "takes.json"), data); return data
def tk_load(work):
    d = rj(J(work, "takes.json"), None)
    return d if d and d.get("items") is not None else None
def tk_find(data, iid):
    for it in data["items"]:
        if it["id"] == str(iid): return it, None
        for t in it.get("trims") or []:
            if t["id"] == str(iid): return it, t
    return None, None
def tk_set(work, iid, action, why="", by="user"):
    """use = خلّ هذي المختارة من مجموعتها · drop = احذفها · keep = أرجعها."""
    data = tk_load(work) or sys.exit("ما فيه takes.json. شغّل: hs takes <work> scan")
    it, tr = tk_find(data, iid)
    if not it: raise ValueError("ما لقيت الجملة %s" % iid)
    if tr is not None: tr["drop"] = action == "drop"
    elif action == "use" and it.get("group"):
        g = next(x for x in data["groups"] if x["id"] == it["group"])
        for x in data["items"]:
            if x.get("group") == g["id"]: x["drop"] = x["id"] != it["id"]; x["chosen"] = x["id"] == it["id"]
        g.update(pick=it["id"], by=by, why=why or g.get("why", ""))
        if why: it["why"] = why
    else:
        it["drop"] = action == "drop"
        if why: it["why"] = why
    if by == "claude": data["by"] = "claude"
    data["summary"] = takes_mod().summary(data); wj(J(work, "takes.json"), data); return it
def tk_plan(work, data=None):
    """القص الجديد بدون ما يطبّقه: (القص الحالي، الجديد، فترات الحذف، اللي انشال بره اختيار الجمل)."""
    T = takes_mod(); cm = cutmap_mod(); data = data or tk_load(work)
    base = tk_base(work); cut = rj(J(work, "cut.json"), {}) or {}; old = [list(x) for x in cut.get("keep") or base]
    manual = T.missing(T.subtract(base, data.get("applied") or [], 0.0), old)   # حذفها بالاستوديو أو بالأوامر: تبقى محذوفة
    dr = T.drops(data, cm.env(work), cm.quiet_point)
    F = cm.fps_of(work, cut); new = [[cm.snap(a, F), cm.snap(b, F)] for a, b in T.subtract(base, dr + manual)]
    return old, [x for x in new if x[1] - x[0] >= 0.12], dr, manual
def _same_keep(a, b, tol=0.05):
    """نفس القص تقريباً (فرق التقريب للفريمات ما يحسب تغيير)."""
    if abs(sum(y - x for x, y in a) - sum(y - x for x, y in b)) > tol: return False
    ia = [x for x in a if x[1] - x[0] > tol]; ib = [x for x in b if x[1] - x[0] > tol]
    return len(ia) == len(ib) and all(abs(p[0] - q[0]) <= tol and abs(p[1] - q[1]) <= tol for p, q in zip(ia, ib))
def apply_keep(work, old, new, S=None, log=print, rebuild=True, snap="قبل اختيار الجمل"):
    """يطبّق قص جديد (بوقت التسجيل الأصلي): الكابشن بتصحيحاتك يمشي عليه، واللي رجع ينضاف من التفريغ، والطبقات والمؤثرات تتبعه، والفيديو ينبني."""
    T = takes_mod(); cm = cutmap_mod(); cg = capgroup_mod()
    snapshot(work, snap)
    o_off, o_tot = cm.offsets(old); n_off, n_tot = cm.offsets(new)
    cut = rj(J(work, "cut.json"), {}) or {}; cut.update(keep=new, total=round(n_tot, 3)); wj(J(work, "cut.json"), cut)
    caps = rj(J(work, "caps.json"), None)
    if caps and caps.get("cards"):
        ws = []
        for c in caps["cards"]:
            for w in c["w"]:
                ws.append({**w, "ss": cm.out_to_src(old, o_off, w["s"]), "se": cm.out_to_src(old, o_off, w["e"])})
        back = T.missing(new, old)
        if back:
            fx = rj(J(work, "fixes.json"), None); allw = T.refine(T.words_of(rj(J(work, "a.json"), {}), fx), T.Energy(cm.env(work)))   # نفس ضبط التوقيت على الصوت
            have = [(w["ss"], w["se"]) for w in ws]
            raw = cg.english_names([{"t": w["t"], "s": w["s"], "e": w["e"]} for w in allw if any(a <= (w["s"] + w["e"]) / 2 <= b for a, b in back) and not any(x <= (w["s"] + w["e"]) / 2 <= y for x, y in have)])
            ws += [{"t": gloss_word(w["t"]), "ss": w["s"], "se": w["e"], **({"en": w["en"]} if w.get("en") else {})} for w in raw]
        out = []
        for w in sorted(ws, key=lambda x: x["ss"]):
            m = cm.src_to_out(new, n_off, (w["ss"] + w["se"]) / 2)
            if m is None: continue
            s = cm.src_to_out(new, n_off, w["ss"], "next"); e = cm.src_to_out(new, n_off, w["se"], "prev")
            s = m if s is None or s > m else s; e = m if e is None or e < m else e
            x = {k: v for k, v in w.items() if k not in ("ss", "se")}; x.update(s=round(s, 3), e=round(max(e, s + 0.08), 3)); out.append(x)
        wpl = int((hs_of(load_studio(work)).get("cap") or {}).get("wpl") or 5)
        wj(J(work, "caps.json"), {**caps, "total": round(n_tot, 3), "cards": cg.cards_of(cg.pack(out, wpl=wpl or 5), total=round(n_tot, 3)) if out else []})
    remap = lambda t, mode=None: cm.src_to_out(new, n_off, cm.out_to_src(old, o_off, t), mode)
    retime_project(work, remap, o_tot, round(n_tot, 3))
    log("المدة %.1f ← %.1f ث" % (o_tot, n_tot))
    if rebuild and S and os.path.isfile(J(work, "cutz.mp4")): rebuild_video(work, S, log)
    return {"changed": True, "total": round(n_tot, 3), "was": round(o_tot, 3)}
def tk_apply(work, S=None, log=print, rebuild=True):
    data = tk_load(work) or sys.exit("ما فيه takes.json")
    old, new, dr, manual = tk_plan(work, data)
    if not new: raise ValueError("ما يبقى شي من الفيديو")
    data["applied"] = dr
    if _same_keep(old, new):
        wj(J(work, "takes.json"), data); log("ما تغيّر شي بالقص."); return {"changed": False, "total": round(sum(b - a for a, b in new), 3)}
    r = apply_keep(work, old, new, S, log, rebuild)
    wj(J(work, "takes.json"), data); cut = rj(J(work, "cut.json"), {}); cut["takes"] = True; wj(J(work, "cut.json"), cut)
    return r
def tk_view(work):
    """للاستوديو: الجمل بوسومها + مدة الخام وبعد القص + شريط المحذوف والباقي."""
    data = tk_load(work)
    if not data: return {"ok": False, "has": os.path.isfile(J(work, "a.json"))}
    T = takes_mod(); raw = data.get("raw") or _src_dur(work)
    try: old, new, dr, manual = tk_plan(work, data)
    except Exception: old, new, dr, manual = [], [], [], []
    cut = rj(J(work, "cut.json"), {}) or {}; cur = cut.get("keep") or []; o_off, _ = cutmap_mod().offsets(cur) if cur else ([], 0)
    cm = cutmap_mod()
    for it in data["items"]:
        it["out"] = round(cm.src_to_out(cur, o_off, (it["s"] + it["e"]) / 2), 2) if cur and cm.src_to_out(cur, o_off, (it["s"] + it["e"]) / 2) is not None else None
    pending = not _same_keep(cur, new)
    return {"ok": True, **data, "raw": round(raw, 2), "kept": round(sum(b - a for a, b in new), 2), "now": round(sum(b - a for a, b in cur), 2), "keep": new, "pending": pending,
            "gone": round(sum(b - a for a, b in dr), 1), "labels": T.TAGS}
def raw_audio(work, s, e, out):
    """مقطع من الصوت الأصلي (حتى المحذوف) عشان تسمع اللقطة قبل ما تقرر."""
    src = J(work, "a.wav") if os.path.isfile(J(work, "a.wav")) else J(work, "src.mov")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "%.3f" % max(0.0, s), "-t", "%.3f" % max(0.1, e - s), "-i", src, "-vn", "-ac", "1", "-c:a", "aac", "-b:a", "96k", out], capture_output=True)
    return out if os.path.isfile(out) and os.path.getsize(out) > 200 else None
def tk_preview(work, out):
    """تسمع النتيجة قبل القص: الصوت الأصلي بالقص الجديد."""
    _, new, _, _ = tk_plan(work); src = J(work, "a.wav") if os.path.isfile(J(work, "a.wav")) else J(work, "src.mov")
    if not new: return None
    expr = "+".join("between(t,%.3f,%.3f)" % (a, b) for a, b in new)
    fl = J(work, ".hs", "tkprev.txt"); os.makedirs(J(work, ".hs"), exist_ok=True); open(fl, "w").write("aselect='%s',asetpts=N/SR/TB" % expr)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vn", "-ac", "1", "-filter_script:a", fl, "-c:a", "aac", "-b:a", "96k", out], capture_output=True)
    return out if os.path.isfile(out) and os.path.getsize(out) > 200 else None
def cmd_takes(work, args):
    sub = args[0] if args else "list"; T = takes_mod()
    def show(data, every=False):
        lab = T.TAGS; gpick = {g["id"]: g for g in data.get("groups") or []}
        for it in data["items"]:
            if not every and not (it["tags"] or it.get("group") or it.get("trims")): continue
            st = "✗" if it.get("drop") else ("✓" if it.get("chosen") else "·")
            tg = "، ".join(lab[t] for t in it["tags"]); g = ("[%s]" % it["group"]) if it.get("group") else ""
            print(" %s %5s  %5.1fث  %-6s %s %s%s" % (st, it["id"], it["s"], g, it["text"][:80], ("  (" + tg + ")") if tg else "", ("  ← " + it["why"]) if it.get("why") and not it.get("drop") else ""))
            for t in it.get("trims") or []: print("   %s %6s  %s «%s»" % ("✗" if t.get("drop") else "·", t["id"], lab[t["kind"]], t["text"]))
        print("\n" + data.get("summary", "")); v = tk_view(work)
        if v.get("ok"): print("الخام %.1f ث · بعد اختيار الجمل %.1f ث%s" % (v["raw"], v["kept"], " (ما تطبّق للحين: hs takes <work> apply)" if v.get("pending") else ""))
    if sub == "scan":
        data = tk_scan(work); show(data); print("\n✓ باقية · ✗ محذوفة · [g] نفس الجملة أكثر من مرة. راجع كل مجموعة واختار الأفضل بالمعنى: hs takes <work> use <رقم> --why \"ليش\"")
    elif sub == "list": show(tk_load(work) or sys.exit("شغّل scan أول"), "--all" in args)
    elif sub in ("use", "drop", "keep"):
        ids = [x for x in args[1:] if not x.startswith("--")]; why = ""; by = "claude" if "--claude" in args or os.environ.get("CLAUDECODE") else "user"
        if "--why" in args: i = args.index("--why"); why = args[i + 1] if i + 1 < len(args) else ""; ids = [x for x in ids if x != why]
        for x in ids: it = tk_set(work, x, sub, why, by); print("%s %s: %s" % ({"use": "اخترت", "drop": "حذفت", "keep": "رجّعت"}[sub], x, it["text"][:70]))
    elif sub == "note":
        data = tk_load(work); data["note"] = " ".join(args[1:]).strip(); data["by"] = "claude"; wj(J(work, "takes.json"), data); print("انحفظ الملخص.")
    elif sub == "apply":
        r = tk_apply(work, find_engine(None) and os.path.join(find_engine(None), "scripts"), print, rebuild="--no-rebuild" not in args)
        print("المدة صارت %.1f ث" % r["total"] if r.get("changed") else "ما تغيّر شي.")
    elif sub == "preview":
        out = tk_preview(work, J(work, "takes-preview.m4a")); print(out or "ما قدرت أطلع المعاينة")
    elif sub == "fit":
        tgt = float(args[1]) if len(args) > 1 else 60.0; out, tot = tk_fit(work, tgt)
        print(("اقتراح حذف %d جملة عشان يوصل %.0f ث (يصير %.1f ث):\n" % (len(out), tgt, tot) + "\n".join("  ✗ %s  %5.1fث  %s" % (x["id"], x["s"], x["text"][:70]) for x in out) + "\nراجعها (keep <رقم> للي تبيه) وبعدها apply") if out else "المقطع %.1f ث، ما يحتاج تقصير." % tot)
    else: sys.exit("takes: scan | list [--all] | use <رقم> [--why …] | drop <أرقام> | keep <أرقام> | note \"ملخص\" | fit <ثواني> | preview | apply [--no-rebuild]")

# ───────────────────────── 4.11: شيل الخلفية من الصور ─────────────────────────
def _img_rgba(src):
    p = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0:s=x", src], capture_output=True, text=True).stdout.strip().split("\n")[0]
    w, h_ = [int(x) for x in p.split("x")[:2]]
    sc = min(1.0, 2000.0 / max(w, h_)); W_, H_ = max(2, int(w * sc)) // 2 * 2, max(2, int(h_ * sc)) // 2 * 2
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-vf", "scale=%d:%d" % (W_, H_), "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "rgba", "-"], capture_output=True).stdout
    return W_, H_, raw
def _save_rgba(arr, out):
    H_, W_ = arr.shape[:2]
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", "%dx%d" % (W_, H_), "-i", "-", "-frames:v", "1", out], input=arr.tobytes(), capture_output=True)
    return os.path.isfile(out) and os.path.getsize(out) > 100
def rmbg_flat(src, out, tol=30.0):
    """خلفية سادة (أبيض، لون واحد، لقطة شاشة): نعبّي من حواف الصورة على اللون اللي يشبه الحافة ونخليه شفاف بحافة ناعمة. بلا نت وبلا موديل."""
    import numpy as np
    W_, H_, raw = _img_rgba(src)
    if len(raw) < W_ * H_ * 4: return {"ok": False, "msg": "ما قدرت أقرأ الصورة"}
    a = np.frombuffer(raw[:W_ * H_ * 4], dtype=np.uint8).reshape(H_, W_, 4).copy(); rgb = a[:, :, :3].astype(np.float32)
    edge = np.concatenate([rgb[0], rgb[-1], rgb[:, 0], rgb[:, -1]]); bg = np.median(edge, axis=0)
    de = np.sqrt(((edge - bg) ** 2).sum(1)); flat = float((de < tol).mean())
    if flat < 0.6: return {"ok": False, "flat": round(flat, 2), "msg": "الخلفية مو سادة"}
    dist = np.sqrt(((rgb - bg) ** 2).sum(2)); cand = dist < tol
    reg = np.zeros_like(cand); reg[0, :] = cand[0, :]; reg[-1, :] = cand[-1, :]; reg[:, 0] = cand[:, 0]; reg[:, -1] = cand[:, -1]
    for _ in range(max(W_, H_) * 2):
        g = reg.copy(); g[1:] |= reg[:-1]; g[:-1] |= reg[1:]; g[:, 1:] |= reg[:, :-1]; g[:, :-1] |= reg[:, 1:]; g &= cand
        if (g == reg).all(): break
        reg = g
    alpha = np.where(reg, 0.0, 1.0)
    near = np.zeros_like(reg); near[1:] |= reg[:-1]; near[:-1] |= reg[1:]; near[:, 1:] |= reg[:, :-1]; near[:, :-1] |= reg[:, 1:]; near &= ~reg   # حافة ناعمة
    soft = np.clip((dist - tol * 0.5) / (tol * 1.5), 0, 1); alpha = np.where(near, np.minimum(alpha, soft + 0.15), alpha)
    a[:, :, 3] = (np.clip(alpha, 0, 1) * a[:, :, 3]).astype(np.uint8)
    if not _save_rgba(a, out): return {"ok": False, "msg": "ما قدرت أحفظ الصورة"}
    return {"ok": True, "out": out, "removed": round(float(reg.mean()), 3), "mode": "flat"}
def rmbg_person(src, out):
    """صورة فيها شخص: موديل فصل الشخص اللي بالسكل (MediaPipe، على جهازك)."""
    eng = find_engine(None); js = os.path.join(eng, "scripts", "23_rmbg.js")
    r = subprocess.run(["node", js, os.path.abspath(src), os.path.abspath(out)], capture_output=True, text=True, timeout=180)
    if r.returncode != 0 or not os.path.isfile(out): return {"ok": False, "msg": (r.stderr or r.stdout or "ما اشتغل فصل الشخص").strip()[-200:]}
    try: return {"ok": True, "out": out, "mode": "person", **json.loads((r.stdout or "{}").strip().splitlines()[-1])}
    except Exception: return {"ok": True, "out": out, "mode": "person"}
def rmbg(work, src, mode="auto"):
    """يشيل الخلفية ويحفظ نسخة PNG جنب الأصل بـ assets. auto: سادة أول، وإلا شخص."""
    p = src if os.path.isabs(src) else J(work, src.lstrip("/"))
    if not os.path.isfile(p): return {"ok": False, "msg": "ما لقيت الصورة: " + src}
    os.makedirs(J(work, "assets"), exist_ok=True); base = re.sub(r"(-nobg)+$", "", os.path.splitext(os.path.basename(p))[0])
    out = J(work, "assets", "%s-nobg-%s.png" % (re.sub(r"-nobg-\d+$", "", base), time.strftime("%H%M%S"))); r = {"ok": False}
    if mode in ("auto", "flat"):
        try: r = rmbg_flat(p, out)
        except ImportError: r = {"ok": False, "msg": "يحتاج numpy"}
    if not r.get("ok") and mode in ("auto", "person"): r = rmbg_person(p, out)
    if r.get("ok"): r["src"] = os.path.relpath(out, work).replace("\\", "/")
    return r
def cmd_rmbg(work, args):
    if not args: sys.exit("rmbg <work> <صورة بمجلد المشروع> [auto|flat|person]")
    r = rmbg(work, args[0], args[1] if len(args) > 1 else "auto")
    print(("شلت الخلفية (%s): %s" % ({"flat": "خلفية سادة", "person": "فصل الشخص"}.get(r.get("mode"), ""), r["src"])) if r.get("ok") else ("ما قدرت: %s. للصور المعقدة استخدم أداة شيل الخلفية من حسابه (Higgsfield أو Canva) وبعدها gen import." % r.get("msg", "")))
    if not r.get("ok"): sys.exit(5)
def cmd_voice(work, args):
    """4.11: مستوى صوتك لأجزاء: mute <من> <إلى> · set <من> <إلى> <مستوى> · list · rm <رقم|all>"""
    if args and args[0] == "studio": return cmd_studio_voice(work, args[1:])
    st = load_studio(work); hs = hs_of(st); vr = hs.setdefault("mix", {}).setdefault("vr", []); sub = args[0] if args else "list"
    if sub in ("mute", "set") and len(args) >= 3:
        s, e = sorted([float(args[1]), float(args[2])]); g = 0.0 if sub == "mute" else float(args[3]) if len(args) > 3 else 0.5
        vr[:] = [r for r in vr if r["e"] <= s or r["s"] >= e] + [{"s": round(s, 3), "e": round(e, 3), "g": round(g, 3)}]; vr.sort(key=lambda r: r["s"])
    elif sub == "rm" and len(args) >= 2: vr[:] = [] if args[1] == "all" else [r for i, r in enumerate(vr) if i != int(args[1]) - 1]
    elif sub != "list": sys.exit("voice: list | mute <من> <إلى> | set <من> <إلى> <مستوى 0-3> | rm <رقم|all>")
    wj(J(work, "studio.json"), st)
    print("\n".join("%d  %s ← %s  %s" % (i + 1, fmt_t(r["s"]), fmt_t(r["e"]), "مكتوم" if r["g"] == 0 else "×%.2f" % r["g"]) for i, r in enumerate(vr)) or "صوتك بنفس المستوى بكل المقطع.")

# ───────────────────────── 4.12: صوت استوديو (على جهازك، بلا رفع ولا اشتراك) ─────────────────────────
# الخطوات: يصلّح القص (clipping) لو فيه ← يشيل الهمهمة ← يشيل الضجيج بنموذج RNNoise (يعرف الكلام من غيره)
# ← يخفّض الفراغ بين الكلام (صدى الغرفة والنفس) ← يوزن مستوى كل جملة على مستوى جملك الوسط ← ضغط خفيف.
# ما يلمس cutz.mp4: يطلع ملف صوت جنبه بزمن المقطع، والتصدير والمعاينة ياخذون منه. فما يتراكم التنظيف أبداً.
SV_VER = 1
SV_DIP = -12.0
SVL = threading.Lock()
_FFL = {}
def ff_has(name):
    """هل ffmpeg اللي بالجهاز فيه هالفلتر؟ (النسخ القديمة ما فيها arnndn)"""
    if "t" not in _FFL:
        try: _FFL["t"] = subprocess.run(["ffmpeg", "-hide_banner", "-filters"], capture_output=True, text=True, errors="replace").stdout or ""
        except Exception: _FFL["t"] = ""
    return re.search(r"\s%s\s" % re.escape(name), _FFL["t"]) is not None
def sv_model():
    eng = find_engine(None); p = os.path.join(eng, "audio", "sh.rnnn") if eng else ""
    return p if p and os.path.isfile(p) else None
def sv_mode(mix):
    v = (mix or {}).get("studio")
    return "ext" if v == "ext" else "local" if v else ""
def _keep_key(work):
    keep = (rj(J(work, "cut.json"), {}) or {}).get("keep") or []
    return hashlib.md5(json.dumps([[round(a, 2), round(b, 2)] for a, b in keep]).encode()).hexdigest()[:10]
def _cards_key(work):
    cards = (rj(J(work, "caps.json"), {}) or {}).get("cards") or []
    return hashlib.md5(json.dumps([[round(c["s"], 2), round(c["e"], 2)] for c in cards]).encode()).hexdigest()[:8]
def sv_sig(work):
    """يتغير لو تغيّر القص أو توقيت الجمل، فما يطلع صوت قديم."""
    return "%s-%s-%d" % (vsig(work), _cards_key(work), SV_VER)
def _db10(path):
    """شدة الصوت كل 10ms بالديسيبل (numpy لو موجود، وإلا بايثون عادي)."""
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vn", "-ac", "1", "-ar", "8000", "-f", "s16le", "-"], capture_output=True).stdout
    try:
        import numpy as np
        a = np.frombuffer(raw[:len(raw) // 160 * 160], dtype="<i2").astype(np.float64).reshape(-1, 80)
        return [float(x) for x in 10 * np.log10((a * a).mean(1) / 1073741824.0 + 1e-12)]
    except ImportError: pass
    import math
    a = array.array("h"); a.frombytes(raw[:len(raw) // 2 * 2])
    if sys.byteorder == "big": a.byteswap()
    out = []; lg = math.log10
    for i in range(0, len(a) - 79, 80):
        s = 0
        for x in a[i:i + 80]: s += x * x
        out.append(10 * lg(s / 80 / 1073741824.0 + 1e-12))
    return out
def sv_speech(db, merge=15, pre=4, hold=12):
    """وين الكلام؟ (كل 10ms) + الكلام مع هامش قبل الكلمة وبعدها، والفراغ أقصر من 150ms بين الكلمات ينحسب كلام."""
    n = len(db); srt = sorted(db) or [0.0]; floor, top = srt[int(n * .1)], srt[min(n - 1, int(n * .95))]
    thr = floor + max(6.0, (top - floor) * .3); v = [x > thr for x in db]; runs = []; i = 0
    while i < n:
        if not v[i]: i += 1; continue
        j = i
        while j < n and v[j]: j += 1
        if runs and i - runs[-1][1] < merge: runs[-1][1] = j
        else: runs.append([i, j])
        i = j
    m = [False] * n
    for a, b in runs:
        if b - a < 3: continue
        for k in range(max(0, a - pre), min(n, b + hold)): m[k] = True
    return v, m
def sv_levels(db, v, cards):
    """مستوى كل جملة (بس لحظات الكلام فيها)."""
    import math
    out = []
    for c in cards:
        p = [10 ** (db[k] / 10) for k in range(int(c["s"] * 100), min(len(db), int(c["e"] * 100) + 1)) if v[k]]
        out.append(10 * math.log10(sum(p) / len(p)) if len(p) >= 15 else None)
    return out
def _spread(L):
    x = sorted(y for y in L if y is not None)
    return round(x[int(len(x) * .9)] - x[int(len(x) * .1)], 1) if len(x) >= 4 else 0.0
def sv_plan(db, cards, dip=SV_DIP, amount=0.85, cap=6.0):
    """الكسب لكل 10ms: (1) الفراغ بين الكلام ينزل dip ديسيبل على مهل  (2) كل جملة تتوزن على الجملة الوسط (لحد cap)."""
    n = len(db)
    if n < 50: return [1.0] * n, {}
    v, m = sv_speech(db); lo = 10 ** (dip / 20.0); g = [1.0 if x else lo for x in m]
    dn, up = (1 - lo) / 8.0, (1 - lo) / 3.0
    for k in range(1, n): g[k] = max(g[k], g[k - 1] - dn)
    for k in range(n - 2, -1, -1): g[k] = max(g[k], g[k + 1] - up)
    L = sv_levels(db, v, cards); have = sorted(x for x in L if x is not None); lev = [0.0] * n
    if len(have) >= 2:
        tgt = have[len(have) // 2]
        gd = [0.0 if x is None else max(-cap, min(cap, amount * (tgt - x))) for x in L]; gd = [0.0 if abs(x) < 1 else x for x in gd]
        S = [c["s"] * 100 for c in cards]; E = [c["e"] * 100 for c in cards]
        for i in range(len(cards) - 1):          # بين جملتين ملتصقتين: انتقال 100ms بالنص
            if S[i + 1] - E[i] < 10:
                mid = (E[i] + S[i + 1]) / 2; E[i] = max(S[i], mid - 5); S[i + 1] = min(E[i + 1], mid + 5)
        pts = sorted(p for i in range(len(cards)) for p in ((S[i], gd[i]), (E[i], gd[i])))
        j = 0
        for k in range(n):
            while j + 1 < len(pts) and pts[j + 1][0] <= k: j += 1
            if k <= pts[0][0]: lev[k] = pts[0][1]
            elif j + 1 >= len(pts): lev[k] = pts[-1][1]
            else:
                (x0, y0), (x1, y1) = pts[j], pts[j + 1]; lev[k] = y0 if x1 <= x0 else y0 + (y1 - y0) * (k - x0) / (x1 - x0)
    return [g[k] * 10 ** (lev[k] / 20.0) for k in range(n)], {"mask": m, "voiced": v}
def _ebur(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-vn", "-af", "ebur128=peak=sample", "-f", "null", "-"], capture_output=True, text=True, errors="replace").stderr or ""
    I = re.findall(r"I:\s*(-?[\d.]+) LUFS", r); pk = re.findall(r"Peak:\s*(-?[\d.]+) dBFS", r)
    return (float(I[-1]) if I else None), (float(pk[-1]) if pk else None)
def sv_stats(work, out, info=None):
    """قبل وبعد: كم صوتك أعلى من الضجيج، وكم الفرق بين أعلى جملة وأوطاها."""
    cards = (rj(J(work, "caps.json"), {}) or {}).get("cards") or []
    a, b = _db10(J(work, "cutz.mp4")), _db10(out); n = min(len(a), len(b)); a, b = a[:n], b[:n]
    v, m = (info or {}).get("voiced") or sv_speech(a)[0], (info or {}).get("mask") or sv_speech(a)[1]
    def med(x): x = sorted(x); return x[len(x) // 2] if x else 0.0
    def snr(d): return round(med([d[k] for k in range(n) if v[k]]) - med([d[k] for k in range(n) if not m[k]]), 1) if any(v[:n]) and not all(m[:n]) else None
    return {"snrBefore": snr(a), "snrAfter": snr(b), "spreadBefore": _spread(sv_levels(a, v, cards)), "spreadAfter": _spread(sv_levels(b, v, cards))}
def sv_cur(work):
    """ملف الصوت المعالج الحالي لو موجود وصالح (بدون ما يعالج)."""
    f = J(work, ".hs", "sv-%s.wav" % sv_sig(work)); return f if os.path.isfile(f) else None
def studio_voice(work, log=print, force=False):
    """4.12: يعالج صوت المقطع على الجهاز ويرجع (ملف wav بزمن المقطع، الأرقام). ما يعيد الشغل لو القص والجمل ما تغيّرت."""
    src = J(work, "cutz.mp4")
    if not os.path.isfile(src): return None, {"ok": False, "msg": "ما فيه مقطع مقصوص"}
    d = J(work, ".hs"); os.makedirs(d, exist_ok=True); sig = sv_sig(work); out = os.path.join(d, "sv-%s.wav" % sig); meta = os.path.join(d, "sv.json")
    with SVL:
        if os.path.isfile(out) and not force:
            m = rj(meta, {}) or {}; return out, (m if m.get("sig") == sig else {"ok": True, "sig": sig})
        t0 = time.time(); a1, env, a2, tmp = (os.path.join(d, x) for x in ("sv-a.wav", "sv-env.f32", "sv-b.wav", "sv-part.wav"))
        vd = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", src, "-vn", "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True, errors="replace").stderr or ""
        mx = re.search(r"max_volume:\s*(-?[\d.]+)", vd); h0 = re.search(r"histogram_0db:\s*(\d+)", vd)
        clip = bool(mx and float(mx.group(1)) > -0.1 and h0 and int(h0.group(1)) > 40 and ff_has("adeclip"))
        model = sv_model() if ff_has("arnndn") else None
        af = ("adeclip," if clip else "") + "highpass=f=75," + ("arnndn=m=sh.rnnn:mix=0.95," if model else "afftdn=nr=14:nf=-40,") + ("deesser=i=0.35," if ff_has("deesser") else "") + "aformat=sample_fmts=s16:channel_layouts=mono"
        log("صوت استوديو: أشيل الضجيج…")
        run(["ffmpeg", "-v", "error", "-y", "-i", os.path.abspath(src), "-vn", "-af", af, "-ar", "48000", "-c:a", "pcm_s16le", os.path.abspath(a1)], log, cwd=os.path.dirname(model) if model else None)
        log("صوت استوديو: أوزن مستوى الجمل وأخفف صدى الغرفة بين الكلام…")
        cards = (rj(J(work, "caps.json"), {}) or {}).get("cards") or []; db = _db10(a1); gains, info = sv_plan(db, cards)
        e = array.array("f")
        for k in range(len(gains)):
            x0 = gains[k]; x1 = gains[k + 1] if k + 1 < len(gains) else x0
            e.extend(x0 + (x1 - x0) * j / 10.0 for j in range(10))
        e.extend([gains[-1] if gains else 1.0] * 2000)     # ذيل احتياط عشان آخر الصوت ما ينقص
        if sys.byteorder == "big": e.byteswap()
        with open(env, "wb") as f: e.tofile(f)
        fc = ("[1:a]aresample=48000,aformat=sample_fmts=flt:channel_layouts=mono[e];[0:a]aformat=sample_fmts=flt:channel_layouts=mono[v];"
              "[v]acompressor=threshold=-20dB:ratio=2:attack=12:release=200:makeup=1[c];[c][e]amultiply[o]")      # الضغط قبل، عشان ما يرفع الضجيج اللي خفّضناه
        run(["ffmpeg", "-v", "error", "-y", "-i", a1, "-f", "f32le", "-ar", "1000", "-i", env, "-filter_complex", fc, "-map", "[o]", "-c:a", "pcm_f32le", a2], log)
        I0, _ = _ebur(src); I1, pk = _ebur(a2)
        gdb = min((I0 if I0 is not None else -16.0) - I1, -1.0 - pk) if I1 is not None and pk is not None else 0.0
        run(["ffmpeg", "-v", "error", "-y", "-i", a2, "-t", "%.3f" % ffdur(src), "-af", "volume=%.2fdB" % gdb, "-c:a", "pcm_s16le", tmp], log)
        for old in glob.glob(os.path.join(d, "sv-*.wav")) + glob.glob(os.path.join(d, "au-sv-*.m4a")):
            if os.path.basename(old) not in (os.path.basename(tmp), os.path.basename(out)):
                try: os.remove(old)
                except OSError: pass
        os.replace(tmp, out)
        for x in (a1, env, a2):
            try: os.remove(x)
            except OSError: pass
        st = {"ok": True, "sig": sig, "denoise": "rnnoise" if model else "fft", "declip": clip, "sec": round(time.time() - t0, 1)}
        try: st.update(sv_stats(work, out, info))
        except Exception as ex: log("تنبيه: ما قدرت أحسب أرقام قبل وبعد (%s)" % str(ex)[:80])
        wj(meta, st); return out, st
def sv_ext_file(work):
    """صوت معالج من برا (Auphonic أو Adobe Podcast من حسابك): يشتغل بس لو القص ما تغيّر بعد ما صدّرته."""
    f, m = J(work, ".hs", "sv-ext.wav"), rj(J(work, ".hs", "sv-ext.json"), {}) or {}
    return f if os.path.isfile(f) and m.get("keep") == _keep_key(work) else None
def voice_track(work, mix, log=print):
    """الصوت اللي يدخل التصدير: (مسار أو None للأصلي، الطريقة)."""
    if mix.get("dub") and dub_get(work):   # 4.26: الدبلجة بدل الصوت الأصلي كامل
        try: f, _ = dub_build(work, log); return f, "dub"
        except Exception as ex: log("تنبيه: الدبلجة ما تركّبت (%s). أكمل بالصوت الأصلي." % str(ex)[:160])
    mode = sv_mode(mix)
    if mode == "ext":
        f = sv_ext_file(work)
        if f: return f, "ext"
        log("تنبيه: الصوت اللي جبته من برا كان على قص قديم. أستخدم صوت الاستوديو اللي على جهازك بداله.")
    if mode:
        try:
            f, _ = studio_voice(work, log); return (f, "local") if f else (None, "")
        except Exception as ex: log("تنبيه: صوت الاستوديو ما اشتغل (%s). أكمل بالصوت الأصلي." % str(ex)[:160])
    return None, ""
def ffdur(path):
    try: return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip())
    except Exception: return 0.0
def sv_export(work):
    """صوت القص الحالي كـ wav، ترفعه على Auphonic أو Adobe Podcast من حسابك."""
    out = J(work, "voice-for-studio.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", J(work, "cutz.mp4"), "-vn", "-ac", "1", "-ar", "48000", "-c:a", "pcm_s16le", out], capture_output=True)
    if not os.path.isfile(out): raise RuntimeError("ما قدرت أطلّع الصوت")
    os.makedirs(J(work, ".hs"), exist_ok=True); wj(J(work, ".hs", "sv-ext.json"), {"keep": _keep_key(work), "dur": round(ffdur(out), 3), "pending": True})
    return out
def sv_import(work, path):
    """يرجّع الصوت المعالج من برا. لازم يكون نفس طول القص (فرق أقل من 0.15 ثانية)."""
    p = path if os.path.isabs(path) else J(work, path)
    if not os.path.isfile(p): raise RuntimeError("ما لقيت الملف: " + path)
    want, got = ffdur(J(work, "cutz.mp4")), ffdur(p)
    if not got: raise RuntimeError("الملف مو صوت")
    if abs(want - got) > 0.15: raise RuntimeError("طول الملف %.2f ث والقص الحالي %.2f ث. صدّر الصوت من جديد (voice studio export) وعالجه مرة ثانية." % (got, want))
    out = J(work, ".hs", "sv-ext.wav"); os.makedirs(J(work, ".hs"), exist_ok=True)
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", p, "-vn", "-ac", "1", "-ar", "48000", "-t", "%.3f" % want, "-af", "apad", "-c:a", "pcm_s16le", out], capture_output=True, text=True)
    if r.returncode or not os.path.isfile(out): raise RuntimeError("ما قدرت أقرأ الملف: " + (r.stderr or "")[-160:])
    wj(J(work, ".hs", "sv-ext.json"), {"keep": _keep_key(work), "dur": round(want, 3), "from": os.path.basename(p)})
    st = load_studio(work); hs_of(st).setdefault("mix", {})["studio"] = "ext"; wj(J(work, "studio.json"), st)
    return out
def sv_line(st):
    if not st.get("ok"): return st.get("msg") or "ما اشتغل"
    out = ["صوت الاستوديو جاهز."]
    if st.get("snrBefore") is not None and st.get("snrAfter") is not None:
        d = round(st["snrAfter"] - st["snrBefore"])
        out.append("الضجيج بين كلامك نزل %d ديسيبل." % d if d >= 2 else "تسجيلك نظيف أصلاً، فالفرق بالضجيج بسيط.")
    if st.get("spreadBefore"): out.append("الفرق بين أعلى جملة وأوطاها صار %s ديسيبل بدل %s." % (st["spreadAfter"], st["spreadBefore"]))
    if st.get("declip"): out.append("وصلّحت التشويش اللي من ارتفاع الصوت.")
    if st.get("denoise") == "fft": out.append("ffmpeg اللي عندك قديم وما فيه RNNoise، فاستخدمت تنظيف أبسط. حدّثه لنتيجة أحسن.")
    return " ".join(out)
def sv_info(work):
    """للاستوديو: هل فيه صوت معالج جاهز، وأرقامه."""
    m = rj(J(work, ".hs", "sv.json"), {}) or {}; cur = m.get("sig") == sv_sig(work) and bool(sv_cur(work))
    return {"ready": cur, "line": sv_line(m) if cur else "", "ext": bool(sv_ext_file(work)), "rnn": bool(sv_model()) and ff_has("arnndn")}
def music_file(work):
    """موسيقى الخلفية بمجلد المشروع (نفس ترتيب 06b_master)."""
    for n in ("bg-audio", "bg", "sound", "music"):
        for e in ("mp3", "m4a", "wav", "aac"):
            if os.path.isfile(J(work, n + "." + e)): return J(work, n + "." + e)
    return None
def cmd_studio_voice(work, args):
    sub = args[0] if args else "status"; st = load_studio(work); mix = hs_of(st).setdefault("mix", {})
    if sub in ("on", "off"):
        mix["studio"] = sub == "on"; wj(J(work, "studio.json"), st)
        if sub == "off": print("رجعت لصوتك الأصلي."); return
        sub = "make"
    if sub in ("make", "redo"):
        try: f, s = studio_voice(work, log=lambda m: None, force=sub == "redo")
        except RuntimeError as e: sys.exit(str(e))
        print(sv_line(s)); return
    if sub == "export":
        f = sv_export(work); print("طلّعت صوت القص الحالي: %s\nارفعه على Auphonic أو Adobe Podcast من حسابك، نزّل النتيجة، وبعدها: voice %s studio import <الملف>" % (os.path.basename(f), os.path.basename(work.rstrip("/\\")))); return
    if sub == "import":
        if len(args) < 2: sys.exit("voice <work> studio import <ملف الصوت المعالج>")
        try: sv_import(work, args[1])
        except RuntimeError as e: sys.exit(str(e))
        print("تمام. التصدير يستخدم الصوت اللي عالجته من برا. لو غيّرت القص بعدين، يرجع لصوت الاستوديو اللي على جهازك."); return
    if sub == "status":
        mode = sv_mode(mix); m = rj(J(work, ".hs", "sv.json"), {}) or {}
        print({"": "مطفي (صوتك الأصلي).", "local": "شغّال على جهازك.", "ext": "يستخدم صوت من برا" + ("" if sv_ext_file(work) else " (قديم، القص تغيّر)")}[mode])
        if mode == "local" and m.get("sig") == sv_sig(work): print(sv_line(m))
        return
    sys.exit("voice <work> studio on | off | redo | status | export | import <ملف>")

# ───────────────────────── 4.10: عشر حلول لمشاكل متعبة ─────────────────────────
def fmt_t(x): x = max(0.0, float(x or 0)); return "%d:%04.1f" % (int(x // 60), x % 60)
# (1) كلمات ما تأكد منها التفريغ: تحتها خط منقط، وClaude يراجعها بالمعنى
def caps_unsure(work, annotate=True, thr=0.5):
    caps = rj(J(work, "caps.json"), None); a = rj(J(work, "a.json"), None)
    if not caps or not caps.get("cards"): return []
    if a and annotate:
        cm = cutmap_mod(); keep = (rj(J(work, "cut.json"), {}) or {}).get("keep") or []; off, _ = cm.offsets(keep) if keep else ([], 0)
        aw = sorted(((float(w["start"]), float(w["end"]), float(w.get("probability", 1) or 1)) for s in a.get("segments") or [] for w in s.get("words") or []))
        starts = [x[0] for x in aw]; import bisect
        for c in caps["cards"]:
            for w in c["w"]:
                if w.get("en"): w.pop("lo", None); continue
                m = (w["s"] + w["e"]) / 2; sm = cm.out_to_src(keep, off, m) if keep else m; k = bisect.bisect_right(starts, sm) - 1; p = None
                for j in (k, k + 1, k - 1):
                    if 0 <= j < len(aw) and aw[j][0] - 0.12 <= sm <= aw[j][1] + 0.12: p = aw[j][2]; break
                if p is not None and p < thr: w["lo"] = True
                else: w.pop("lo", None)
        wj(J(work, "caps.json"), caps)
    out = []
    for i, c in enumerate(caps["cards"]):
        for j, w in enumerate(c["w"]):
            if w.get("lo"): out.append({"card": i, "word": j, "t": w["t"], "s": w["s"], "ctx": " ".join(x["t"] for x in c["w"])})
    return out
# (2) قاموسك: التصحيحات اللي تسويها تنحفظ وتنطبق على مقاطعك الجاية
_GL = {"m": None, "d": {}}
def gloss_path(): return os.path.join(HOME_CFG, "glossary.json")
def gloss_load():
    p = gloss_path(); m = os.path.getmtime(p) if os.path.isfile(p) else 0
    if _GL["m"] != m: _GL["m"] = m; _GL["d"] = rj(p, {}) or {}
    return _GL["d"]
def gloss_save(d): os.makedirs(HOME_CFG, exist_ok=True); wj(gloss_path(), d); _GL["m"] = None
def _gkey(txt): return " ".join(_norm(x) for x in str(txt).split() if _norm(x))
def gloss_word(t):
    G = gloss_load(); k = _gkey(t)
    if not G or not k: return t
    tail = re.search(r"[؟?!.،,]+$", str(t)); tail = tail.group(0) if tail else ""
    if k in G: return G[k] + tail
    if len(k) > 3 and k[0] == "و" and k[1:] in G: return "و" + G[k[1:]] + tail
    return t
def gloss_apply_words(words):
    """يبدّل الكلمات (والعبارات لين 3 كلمات) حسب قاموسك. يرجّع (الكلمات، عدد التبديلات)."""
    G = gloss_load()
    if not G: return words, 0
    out, i, n, ch = [], 0, len(words), 0
    while i < n:
        hit = None
        for L in (3, 2, 1):
            if i + L > n: continue
            k = " ".join(_norm(w["t"]) for w in words[i:i + L])
            if k in G: hit = (L, G[k]); break
            if len(k) > 3 and k[0] == "و" and k[1:] in G: r_ = G[k[1:]]; hit = (L, ("و " if re.search(r"[A-Za-z]", r_) else "و") + r_); break   # «وشات جي بي تي» ← «و ChatGPT»
        if hit:
            L, rep = hit; w0, w1 = words[i], words[i + L - 1]; tail = re.search(r"[؟?!.،,]+$", str(w1["t"]))
            out.append({**w0, "t": rep + (tail.group(0) if tail else ""), "e": w1["e"], "lo": False}); out[-1].pop("lo"); i += L; ch += 1
        else: out.append(words[i]); i += 1
    return out, ch
def gloss_learn(old_caps, new_caps):
    """يقارن الكابشن قبل وبعد تعديلك: الكلمة اللي صححتها (اسم، أو كتابة قريبة من الغلط، أو كلمة ما تأكد منها التفريغ) تنحفظ بالقاموس."""
    try:
        A = [w for c in (old_caps or {}).get("cards") or [] for w in c.get("w") or []]; B = [w for c in (new_caps or {}).get("cards") or [] for w in c.get("w") or []]
        if not A or not B or abs(len(A) - len(B)) > 40: return 0
        na = [_norm(w["t"]) for w in A]; nb = [_norm(w["t"]) for w in B]; G = dict(gloss_load()); n = 0
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, na, nb, autojunk=False).get_opcodes():
            if op != "replace" or i2 - i1 > 3 or j2 - j1 > 3: continue
            ok_ = " ".join(na[i1:i2]); new = " ".join(re.sub(r"[؟?!.،,]+$", "", B[j]["t"]) for j in range(j1, j2)).strip()
            if len(ok_.replace(" ", "")) < 3 or re.search(r"\d", ok_ + new) or not new: continue
            latin = bool(re.search(r"[A-Za-z]", new)); close = difflib.SequenceMatcher(None, ok_, " ".join(nb[j1:j2])).ratio() >= 0.6; lo = any(A[i].get("lo") for i in range(i1, i2))
            if latin or close or lo: G[ok_] = new; n += 1
        if n:
            if len(G) > 600: G = dict(list(G.items())[-600:])
            gloss_save(G)
        return n
    except Exception: return 0
def cmd_gloss(args):
    sub = args[0] if args else "list"; G = dict(gloss_load())
    if sub == "list": print("\n".join("%s ← %s" % (v, k) for k, v in G.items()) or "القاموس فاضي. يتعلّم من تصحيحاتك بالاستوديو، أو: hs gloss add \"الغلط\" \"الصح\"")
    elif sub == "add" and len(args) >= 3: G[_gkey(args[1])] = args[2]; gloss_save(G); print("انحفظ: %s ← %s" % (args[2], args[1]))
    elif sub == "rm" and len(args) >= 2: G.pop(_gkey(args[1]), None); gloss_save(G); print("انشال.")
    else: sys.exit("gloss: list | add \"الغلط\" \"الصح\" | rm \"الغلط\"")
def caps_gloss(work):
    caps = rj(J(work, "caps.json")); ch = 0
    for c in caps["cards"]: c["w"], n = gloss_apply_words(c["w"]); ch += n
    if ch: snapshot(work, "قبل تطبيق القاموس"); wj(J(work, "caps.json"), caps)
    return ch
# (3) القص ما ينزل على صوت: نقطة القص على كلام يقطع آخر حرف أو أول حرف
def cut_on_sound(work):
    cm = cutmap_mod(); T = takes_mod(); db = cm.env(work); keep = (rj(J(work, "cut.json"), {}) or {}).get("keep") or []
    if not db or len(keep) < 2: return [], keep, keep
    E = T.Energy(db); n = len(db); bad = []; new = [list(x) for x in keep]
    loud = lambda i: 0 <= i < n and db[i] > E.thr + 3
    for k, (a, b) in enumerate(keep):
        for edge, tt in (("s", a), ("e", b)):
            if (edge == "s" and k == 0) or (edge == "e" and k == len(keep) - 1): continue
            if (edge == "s" and abs(a - keep[k - 1][1]) < 0.02) or (edge == "e" and abs(keep[k + 1][0] - b) < 0.02): continue   # جزئين متلاصقين: الصوت ما انقطع أصلاً
            i = int(round(tt * 100))
            if not (loud(i - 1) and loud(i)): continue
            lim_lo = keep[k - 1][1] if edge == "s" else a; lim_hi = b if edge == "s" else keep[k + 1][0]
            step = -1 if edge == "s" else 1; j = i; moved = None
            for _ in range(14):
                j += step
                if not (lim_lo * 100 < j < lim_hi * 100): break
                if db[j] <= E.thr: moved = j / 100.0; break
            bad.append({"seg": k, "edge": edge, "t": round(tt, 3), "to": moved})
            if moved is not None: new[k][0 if edge == "s" else 1] = moved
    F = cm.fps_of(work); new = [[cm.snap(x, F), cm.snap(y, F)] for x, y in new]
    return bad, keep, new
# (7) كلام بدون كابشن: صوت كلام واضح ما له ولا كلمة بالكابشن (whisper نسيه)
def caps_gaps(work, min_len=0.6):
    cm = cutmap_mod(); T = takes_mod(); db = cm.env(work); keep = (rj(J(work, "cut.json"), {}) or {}).get("keep") or []; caps = rj(J(work, "caps.json"), None)
    if not db or not keep or not caps: return []
    E = T.Energy(db); off, _ = cm.offsets(keep); words = sorted((w["s"], w["e"]) for c in caps["cards"] for w in c["w"]); out = []
    for (a, b), o in zip(keep, off):
        runs = []
        for i in range(int(a * 100), int(b * 100)):
            if 0 <= i < len(db) and db[i] > E.thr + 2:
                if runs and i - runs[-1][1] <= 15: runs[-1][1] = i
                else: runs.append([i, i])
        for r0, r1 in runs:
            if (r1 - r0) / 100.0 < min_len: continue
            s, e = o + r0 / 100.0 - a, o + r1 / 100.0 - a
            cov = sum(max(0.0, min(e, y + 0.15) - max(s, x - 0.15)) for x, y in words if y > s - 0.2 and x < e + 0.2)
            if cov < 0.35 * (e - s): out.append({"s": round(s, 2), "e": round(e, 2), "src": round(r0 / 100.0, 2)})
    return out
# (8) أرقام وأسماء تتأكد منها قبل النشر
def facts(work):
    caps = rj(J(work, "caps.json"), {"cards": []}) or {"cards": []}; out = []
    for sn in _sentences(caps.get("cards") or [], gap=0.6, maxw=26):
        txt = sn["text"]; why = []
        if "رقم أو سعر" in cutmap_mod().important(txt): why.append("رقم أو سعر")
        if re.search(r"[A-Za-z]{2,}\s?\d|\d+(\.\d+)", txt): why.append("نسخة أو موديل")
        if re.search(r"(أفضل|اقوى|أقوى|أسرع|اسرع|أرخص|ارخص|الوحيد|أول|اول) ", txt) and re.search(r"[A-Za-z]{2,}", txt): why.append("مقارنة بين منتجات")
        if why: out.append({"s": round(sn["s"], 2), "text": txt, "why": why})
    return out
# (4) و(5) و(9) بالجمل: الفكرة المكررة بمكان بعيد، التقصير لمدة، التحية بالبداية
def tk_farrep(data):
    T = takes_mod(); items = [it for it in data["items"] if not it.get("drop")]; n = 0
    for i, b in enumerate(items):
        tb = [T.key(T.norm(x)) for x in b["text"].split()]; cb = [x for x in tb if x not in T.STOP and len(x) >= 2]
        if len(cb) < 5: continue
        for a in items[:i]:
            if b["s"] - a["e"] < 15: continue
            ta = [T.key(T.norm(x)) for x in a["text"].split()]
            if T.sim(ta, tb) >= 0.75 and "farrep" not in b["tags"]: b["tags"].append("farrep"); b["why"] = "قلتها قبل عند %d:%02d" % (int(a["s"] // 60), int(a["s"] % 60)); b["rep"] = a["id"]; n += 1; break
    return n
def tk_fit(work, target):
    """يقترح جمل تنحذف عشان المقطع يوصل لمدة معينة: يبدأ بالأضعف (تحية، فكرة مكررة، جملة متروكة، بلا معلومة) ويخلي الهوك والختام."""
    data = tk_load(work) or tk_scan(work); cm = cutmap_mod()
    for it in data["items"]:
        if "fit" in it["tags"]: it["tags"].remove("fit"); it["drop"] = False if not any(t in it["tags"] for t in ("retake", "stumble", "nospeech", "noise", "filler")) else it["drop"]
    _, new, _, _ = tk_plan(work, data); total = sum(b - a for a, b in new)
    kept = [it for it in data["items"] if not it.get("drop")]
    if total <= target: wj(J(work, "takes.json"), data); return [], total
    cand = []; head = kept[0]["s"] + 8.0 if kept else 0   # أول 8 ثواني (الهوك) وآخر جملتين ما نلمسها
    for k, it in enumerate(kept):
        if it["s"] < head or k >= len(kept) - 2: continue
        why = cm.important(it["text"]); sc = 1.0 + 1.5 * ("رقم أو سعر" in why) + 1.2 * ("نصيحة أو مقارنة" in why) + 0.4 * ("اسم" in why)
        sc -= 2.0 * ("farrep" in it["tags"]) + 1.6 * ("greet" in it["tags"]) + 1.2 * ("cutoff" in it["tags"])
        cand.append((sc / max(0.6, it["e"] - it["s"]) ** 0.3, it))
    cand.sort(key=lambda x: x[0]); out = []
    for sc, it in cand:
        if total <= target: break
        it["drop"] = True; it["tags"].append("fit"); it["why"] = "عشان المقطع يوصل %d ث" % target; total -= (it["e"] - it["s"]) + 0.2; out.append(it)
    data["summary"] = takes_mod().summary(data); wj(J(work, "takes.json"), data); return out, total
# (6) الخطة قبل البناء: Claude يكتب وش يطلع بكل جزء، وتوافق أو تعدّل قبل ما يصرف وقت وتوليد
PLAN_KINDS = {"web": "من النت", "archive": "أرشيف حقيقي", "gen": "صورة مولّدة", "draw": "رسمة بالكود", "overlay": "عنصر فوق الفيديو", "screen": "لقطة شاشة أو موقع", "text": "نص أو موشن", "none": "وجهك بس"}
def plan_load(work): return rj(J(work, "plan.json"), None)
def plan_view(work):
    p = plan_load(work)
    if not p: return {"ok": False}
    st = load_studio(work); Ls = [L for L in hs_of(st).get("layers") or [] if not L.get("off") and L.get("type") != "fx"]   # التقريب والمؤثرات ما تحسب بناء
    for it in p.get("items") or []:
        it["built"] = bool(it.get("status") == "done" or any(L["s"] < float(it.get("e", 0)) and L["e"] > float(it.get("s", 0)) for L in Ls))
        it["kindAr"] = PLAN_KINDS.get(it.get("kind"), it.get("kind", ""))
    return {"ok": True, **p}
# ───────────────────────── 4.16: القصة البصرية: يتابع الكلام، مثال قريب لكل فكرة، وموشن مربوط بالكلمات ─────────────────────────
PLAN_FX = ("focus", "zoomblur", "whip", "stretch")
def plan_beats(work, maxlen=5.0, minlen=1.8, pause=0.45):
    """يقسم الكلام لمقاطع (كل مقطع فكرة وحدة تقريباً): ينقطع عند نهاية الجملة أو سكتة أو لو طال."""
    cards = (rj(J(work, "caps.json"), {}) or {}).get("cards") or []; beats = []; cur = None
    for c in cards:
        txt = " ".join(w["t"] for w in c.get("w") or []).strip()
        if not txt: continue
        if cur and (c["s"] - cur["e"] >= pause or cur["e"] - cur["s"] >= maxlen or re.search(r"[.!؟?]$", cur["speech"])): beats.append(cur); cur = None
        if cur: cur["e"] = c["e"]; cur["speech"] += " " + txt
        else: cur = {"s": round(c["s"], 2), "e": round(c["e"], 2), "speech": txt}
    if cur: beats.append(cur)
    out = []
    for b in beats:   # القصيرة تنضم للي قبلها
        if out and b["e"] - b["s"] < minlen and b["e"] - out[-1]["s"] <= maxlen + 1.5: out[-1]["e"] = b["e"]; out[-1]["speech"] += " " + b["speech"]
        else: out.append(dict(b))
    return [{**b, "e": round(b["e"], 2)} for b in out]
def plan_draft(work, force=False):
    if plan_load(work) and not force: return None
    items = [{"id": i + 1, "s": b["s"], "e": b["e"], "speech": b["speech"], "title": "", "idea": "", "example": "", "show": "", "kind": "gen", "prompt": "", "move": {}, "anno": [], "glow": None}
             for i, b in enumerate(plan_beats(work))]
    p = {"approved": False, "feedback": "", "style": "", "look": "cinema", "items": items, "callback": None}
    wj(J(work, "plan.json"), p); return p
def cue_times(work, cues, s, e):
    """كلمات (أو جزء منها) ← وقت كل وحدة بالترتيب داخل [s,e]. يرجّع أوقات مطلقة."""
    words = [w for c in (rj(J(work, "caps.json"), {}) or {}).get("cards") or [] for w in c.get("w") or []]
    out = []; t0 = s - 0.25
    for q in ([cues] if isinstance(cues, str) else cues or []):
        if isinstance(q, (int, float)): out.append(float(q)); t0 = float(q); continue
        k = _norm(str(q)); hit = None
        for w in words:
            if w["s"] < t0 or w["s"] > e + 0.3: continue
            nw = _norm(w["t"])
            if k and (nw == k or k in nw or (len(nw) > 2 and nw in k)): hit = w["s"]; break
        if hit is None: continue
        out.append(round(hit, 3)); t0 = hit + 0.05
    return out
def plan_build(work):
    """يبني من الخطة: صورة ملء الشاشة بحركة، وتعليقات على الصورة تطلع مع الكلمات، وكلمة متوهجة، والربط بالنهاية. يعيد البناء بدون تكرار."""
    p = plan_load(work) or {}; st = load_studio(work); hs = hs_of(st); Ls = [L for L in hs.get("layers") or [] if L.get("auto") != "plan"]; n = 0; miss = []
    for i, it in enumerate(p.get("items") or []):
        src = it.get("src") or it.get("img"); s0, e0 = float(it.get("s", 0)), float(it.get("e", 0)); pid = it.get("id", i + 1)
        if it.get("kind") == "none" or e0 - s0 < 0.4: continue
        n += plan_mg(work, it, Ls, s0, e0, pid, bool(src))   # موشن جرافيك وشعارات وكلمة متوهجة: تشتغل بدون صورة
        g = it.get("glow")
        if g:
            g = {"text": g} if isinstance(g, str) else dict(g); tt = cue_times(work, g.get("cue") or g["text"].split()[0], s0, e0); gs = tt[0] if tt else s0 + 0.2
            Ls.append({"id": new_id(Ls), "type": "text", "text": g["text"], "anim": "glow", "size": g.get("size", 165), "y": g.get("y", 0.16), "color": g.get("color", "#FFE7B3"), "s": round(gs, 3), "e": round(float(g.get("e", e0)), 3), "track": 2, "auto": "plan", "pid": pid}); n += 1
        if not src:
            if it.get("kind") in ("gen", "web", "archive", "screen", "draw"): miss.append(pid)
            continue
        mv = it.get("move") if isinstance(it.get("move"), dict) else {}
        L = {"id": new_id(Ls), "type": "image", "src": src, "fit": "cover", "s": round(s0, 3), "e": round(e0, 3), "track": 0, "anim": "fade", "auto": "plan", "pid": pid,
             "move": mv.get("type", "push"), "hand": mv.get("hand", True), "inFx": mv.get("in", PLAN_FX[i % len(PLAN_FX)])}
        for k_ in ("fx", "fy", "amount", "outFx"):
            if mv.get(k_) is not None: L[k_] = mv[k_]
        if mv.get("shake"): L["shake"] = [round(t - s0, 3) for t in cue_times(work, mv["shake"], s0, e0)] or None
        Ls.append(L); n += 1
        for a in it.get("anno") or []:
            A = {k_: v for k_, v in a.items() if k_ not in ("cue",)}; A.update({"type": "anno", "track": 1, "anim": "none", "auto": "plan", "pid": pid})
            A.setdefault("kind", "ring"); A["s"] = round(float(a.get("s", s0 + 0.12)), 3); A["e"] = round(float(a.get("e", e0)), 3)
            if a.get("cue"): A["at"] = [round(max(0.0, t - A["s"]), 3) for t in cue_times(work, a["cue"], s0, e0)] or None
            A["id"] = new_id(Ls); Ls.append(A); n += 1
    cb = p.get("callback") or {}
    if cb.get("items"):   # الربط: أشياء القصة ترجع جنب وجهه بالنهاية
        cs, ce = float(cb.get("s", 0)), float(cb.get("e", 0))
        for j, src in enumerate(cb["items"][:4]):
            left = j % 2 == 0; row = j // 2
            if isinstance(src, dict): src = src.get("src") or (logo_to_project(work, src["logo"]) if src.get("logo") else None)
            if not src: continue
            Ls.append({"id": new_id(Ls), "type": "image", "src": src, "fit": "free", "w": cb.get("w", 0.15), "x": 0.12 if left else 0.88, "y": 0.27 + row * 0.12, "s": round(cs + 0.12 * j, 3), "e": round(ce, 3), "track": 1, "anim": "pop", "move": "float", "auto": "plan", "pid": "callback"}); n += 1
    hs["layers"] = Ls
    if p.get("look") and not hs.get("look") and p["look"] in looks_all(): wj(J(work, "studio.json"), st); look_apply(work, p["look"]); st = load_studio(work); hs_of(st)["layers"] = Ls
    wj(J(work, "studio.json"), st); return n, miss
PLAN_MG_AT = ("stat", "slam", "ring", "callout", "logo", "quote")   # هذي تطلع لحظة ما يقول الكلمة، والقوائم كل سطر مع كلمته
def plan_mg(work, it, Ls, s0, e0, pid, over):
    n = 0; ms = it.get("mg"); ms = [ms] if isinstance(ms, dict) else list(ms or [])
    lg = it.get("logo"); lg = [lg] if isinstance(lg, (str, dict)) else list(lg or [])
    if lg:   # الشعارات: كل شعار يطلع لما يقول اسمه، ويبقى لين اللي بعده
        ents = [({"name": x} if isinstance(x, str) else dict(x)) for x in lg]; tt = []
        for x in ents: c = cue_times(work, x.get("cue") or x["name"], s0, e0); tt.append(c[0] if c else None)
        for j, x in enumerate(ents):
            if tt[j] is None: tt[j] = (tt[j - 1] + 0.9) if j and tt[j - 1] is not None else s0 + 0.15 + j * max(0.8, (e0 - s0) / max(1, len(ents)))
        for j, x in enumerate(ents):
            a = max(s0, tt[j] - 0.1); b = min(e0, max(a + 0.8, (tt[j + 1] - 0.1) if j + 1 < len(ents) else e0))
            ms.append({"kind": "logo", "name": x["name"], "s": a, "e": b, **{k_: x[k_] for k_ in ("y", "src", "size") if x.get(k_) is not None}})
    for m in ms:
        k = m.get("kind")
        if k not in MG_KINDS: continue
        M = {k_: v for k_, v in m.items() if k_ != "cue"}; M.update({"type": "mg", "auto": "plan", "pid": pid}); M.setdefault("track", 2 if over else 1)
        cs = cue_times(work, m["cue"], s0, e0) if m.get("cue") else []
        M["s"] = round(float(m["s"]) if m.get("s") is not None else (max(s0, cs[0] - 0.12) if cs and k in PLAN_MG_AT else s0 + 0.1), 3)
        M["e"] = round(float(m["e"]) if m.get("e") is not None else e0, 3)
        if cs and k not in PLAN_MG_AT: M["at"] = [round(max(0.0, t - M["s"]), 3) for t in cs]
        if k == "logo" and not M.get("src"): M["src"] = logo_to_project(work, M.get("name", ""))
        if k == "logo" and M.get("name2") and not M.get("src2"): M["src2"] = logo_to_project(work, M["name2"])
        if M["e"] - M["s"] < 0.5: continue
        for t_ in ("text", "title"):
            if isinstance(M.get(t_), list): M[t_] = "\n".join(M[t_])
        M["id"] = new_id(Ls); Ls.append(M); n += 1
    return n
def plan_check(work):
    p = plan_load(work); total = (rj(J(work, "caps.json"), {}) or {}).get("total") or 0; bad = []
    if not p: return ["ما فيه plan.json"]
    for i, it in enumerate(p.get("items") or []):
        if it.get("kind") not in PLAN_KINDS: bad.append("البند %d: النوع لازم واحد من %s" % (i + 1, ", ".join(PLAN_KINDS)))
        if not (0 <= float(it.get("s", -1)) < float(it.get("e", 0)) <= total + 0.5): bad.append("البند %d: الوقت برا المقطع" % (i + 1))
        if not it.get("show"): bad.append("البند %d: ناقص «وش يطلع»" % (i + 1))
        if it.get("kind") in ("gen", "web", "archive") and not (it.get("example") or "").strip(): bad.append("البند %d: ناقص «المثال» (وش الشي اللي يشوفه الناس ويفهمون منه الفكرة)" % (i + 1))
        ms = it.get("mg"); ms = [ms] if isinstance(ms, dict) else list(ms or [])
        for m in ms:
            if m.get("kind") not in MG_KINDS: bad.append("البند %d: نوع الموشن لازم واحد من %s" % (i + 1, ", ".join(MG_KINDS)))
        lg = it.get("logo"); lg = [lg] if isinstance(lg, (str, dict)) else list(lg or [])
        for a in (it.get("anno") or []) + ms + [x for x in lg if isinstance(x, dict)]:
            if a.get("cue") and not cue_times(work, a["cue"], float(it.get("s", 0)), float(it.get("e", 0))): bad.append("البند %d: ما لقيت الكلمة %s بكلامه بهالجزء" % (i + 1, json.dumps(a["cue"], ensure_ascii=False)))
        if it.get("kind") == "text" and not (ms or lg or it.get("glow")): bad.append("البند %d: نوعه نص أو موشن بس ما فيه mg ولا logo ولا glow" % (i + 1))
    return bad
def cmd_plan(work, args):
    sub = args[0] if args else "show"
    if sub == "show":
        v = plan_view(work)
        if not v.get("ok"): sys.exit("ما فيه خطة. اكتب <work>/plan.json (شوف SKILL.md قسم الخطة)")
        print("الخطة %s" % ("(موافق عليها)" if v.get("approved") else "(تنتظر موافقته)"))
        for i, it in enumerate(v.get("items") or []): print("%2d %6.1f-%-6.1f %-16s %s%s" % (i + 1, float(it["s"]), float(it["e"]), it["kindAr"], it.get("show", "")[:70], "  ✓" if it["built"] else ""))
        if v.get("feedback"): print("\nملاحظته: " + v["feedback"])
    elif sub == "check":
        bad = plan_check(work); print("\n".join(bad) if bad else "الخطة سليمة."); sys.exit(4 if bad else 0)
    elif sub == "wait":
        tmo = 540; t0 = time.time(); p0 = plan_load(work) or sys.exit("ما فيه خطة"); f0 = p0.get("feedback", "")
        while True:
            p = plan_load(work) or {}
            if p.get("approved"): print("وافق على الخطة. ابدأ البناء."); return
            if p.get("feedback", "") != f0: print("عدّل على الخطة:\n" + p["feedback"] + "\nعدّل plan.json على كلامه وأعد: hs plan <work> wait"); return
            if time.time() - t0 > tmo: print("لسه ما وافق. أعد نفس الأمر وانتظره."); sys.exit(3)
            time.sleep(2)
    elif sub in ("approve", "unapprove"):
        p = plan_load(work) or sys.exit("ما فيه خطة"); p["approved"] = sub == "approve"; wj(J(work, "plan.json"), p); print("تم.")
    elif sub == "draft":   # 4.16: المقاطع من كلامه، وأنت تعبّي الفكرة والمثال والصورة والموشن
        p = plan_draft(work, force="--force" in args)
        if p is None: sys.exit("فيه خطة. --force يكتب فوقها.")
        for it in p["items"]: print("%2d %6.1f-%-6.1f %s" % (it["id"], it["s"], it["e"], it["speech"]))
        print("\nعبّ لكل بند: idea و example و show و prompt و move و anno (cue = الكلمة) و glow. القواعد: engine/references/visual-story.md")
    elif sub == "build":
        n, miss = plan_build(work); print("بنيت %d طبقة من الخطة." % n + ("" if not miss else " ناقصها صورة: " + ", ".join(str(x) for x in miss)))
    elif sub == "cues" and len(args) >= 4:
        print(cue_times(work, args[3:], float(args[1]), float(args[2])))
    else: sys.exit("plan: show | check | wait | approve | unapprove | draft [--force] | build | cues <من> <إلى> <كلمة>…")
# (10) خطوات المشروع: وين وصل ووش الباقي
def steps(work):
    tk = tk_load(work); caps = rj(J(work, "caps.json"), None); p = plan_load(work); st = load_studio(work); Ls = [L for L in hs_of(st).get("layers") or [] if not L.get("off")]
    ex = bool(glob.glob(J(work, "ad-*.mp4")) or glob.glob(J(work, "out", "*.mp4")))
    try: tk_pending = bool(tk) and tk_view(work).get("pending")
    except Exception: tk_pending = False
    unsure = sum(1 for c in (caps or {}).get("cards") or [] for w in c["w"] if w.get("lo"))
    S_ = [("takes", "الجمل", "done" if tk and not tk_pending else ("now" if os.path.isfile(J(work, "a.json")) else "todo")),
          ("caps", "الكابشن", "done" if caps and not unsure else ("now" if caps else "todo")),
          ("plan", "الخطة", "done" if p and p.get("approved") else ("now" if caps else "todo")),
          ("build", "البناء", "done" if Ls and (not p or all(x.get("built") for x in plan_view(work).get("items") or [])) else ("now" if p and p.get("approved") else "todo")),
          ("export", "التصدير", "done" if ex else ("now" if Ls else "todo"))]
    cur = next((i for i, x in enumerate(S_) if x[2] != "done"), len(S_))
    return [{"k": k, "label": l, "state": "done" if s == "done" else ("now" if i == cur else "todo"), "n": i + 1, "unsure": unsure if k == "caps" else 0} for i, (k, l, s) in enumerate(S_)]

# ───────────────────────── المنصات والمقاسات (3.1) ─────────────────────────
# safe = نسبة من كل حافة تغطيها واجهة المنصة [فوق، تحت، يسار، يمين]. أرقام تيك توك وانستقرام من أدلة المقاسات المنشورة، وإكس ولينكدإن تقدير محافظ.
PLATFORMS = {
    "tiktok": {"ar": "تيك توك", "frames": ["9:16"], "safe": [8, 22, 6, 13], "max": "10 دقايق من التطبيق · 60 دقيقة رفع", "best": "20-45 ثانية", "maxS": 600, "bestS": [20, 45],
               "tips": ["الهوك في أول ثانية ونص: جملة أو حركة توقف الإصبع، بلا مقدمة ولا شعار", "تغيير بصري كل 2-3 ثواني (قطع · زوم · صورة · نص)",
                        "الكابشن على الشاشة أساسي وكلمات البحث تنقال وتنكتب (تيك توك محرك بحث)", "الختام يرجّع لأول المقطع أو يطلب تعليق، لأن الإعادة والإكمال أهم إشارتين",
                        "لا تحط نص تحت 78% من الارتفاع ولا بآخر 13% يمين (أزرار الإعجاب والوصف)"]},
    "instagram": {"ar": "انستقرام", "frames": ["9:16", "4:5"], "safe": [12, 32, 6, 11], "max": "الريلز لين 3 دقايق عشان ينقترح لناس جدد", "best": "15-45 ثانية", "maxS": 180, "bestS": [15, 45],
                  "tips": ["أهم إشارة المشاركة بالخاص: اصنع لحظة تستاهل تنرسل لصديق", "العنوان والوجه في وسط الكادر، لأن شبكة الحساب تقص المقطع 3:4",
                           "الكابشن أعلى من تيك توك: لا تنزل تحت 68% من الارتفاع (الوصف والصوت يغطون آخر 32%)", "بلا علامة مائية من أي تطبيق ثاني، وجودة نظيفة", "أول 3 ثواني تحدد «نسبة التخطي» اللي تطلع بالإحصائيات: صوت ونص وحركة من البداية",
                           "غلاف واضح بعنوان مقروء لأنه يظهر في الشبكة"]},
    "x": {"ar": "إكس", "frames": ["16:9", "1:1", "9:16"], "safe": [6, 10, 5, 5], "max": "140 ثانية للحساب العادي · أطول للمشترك", "best": "15-45 ثانية", "maxS": 140, "bestS": [15, 45],
          "tips": ["المقطع يشتغل صامت بالتايم لاين: الفكرة لازم تنفهم من النص على الشاشة من أول فريم", "رأي واضح أو معلومة محددة من أول جملة، بلا تمهيد",
                   "العرضي 16:9 والمربع 1:1 يطلعون أكبر في التايم لاين على الكمبيوتر، والعمودي أحسن بالجوال", "لا تتعدى 140 ثانية لو الحساب مو مشترك، وإلا ما ينرفع",
                   "نص التغريدة يشيل نص السياق والمقطع يشيل الإثبات"]},
    "linkedin": {"ar": "لينكدإن", "frames": ["4:5", "1:1", "9:16"], "safe": [6, 12, 5, 5], "max": "15 دقيقة للمنشور العادي", "best": "30-90 ثانية", "maxS": 900, "bestS": [30, 90],
                 "tips": ["نبرة مهنية وفائدة مباشرة: درس · رقم · تجربة شغل، بلا ترندات ولا موسيقى صاخبة", "أول جملة تقول وش بيستفيد المشاهد، والإيقاع أهدأ من تيك توك",
                          "4:5 أو 1:1 ياخذ مساحة أكبر بالفيد من العرضي", "الكابشن المحروق أساسي لأن أغلبهم يشوف بلا صوت بالدوام",
                          "الختام سؤال يفتح نقاش بالتعليقات، مو «تابعني»"]},
}
FRAMES = {"9:16": (1080, 1920), "4:5": (1080, 1350), "1:1": (1080, 1080), "16:9": (1920, 1080)}
def frame_of(hs): f = (hs.get("frame") or {}); ar = f.get("ar") if f.get("ar") in FRAMES else "9:16"; return ar, float(f.get("cy", 0.47))
def crop_y0(ar, cy): h = FRAMES[ar][1]; return int(max(0, min(1920 - h, round(cy * 1920 - h / 2)))) // 2 * 2
def safe_of(plats, ar="9:16", cy=0.47):
    """أشد حدود آمنة للمنصات المختارة + حدود القص لو المقاس مو 9:16. ترجع نسب من الكادر العمودي الكامل."""
    z = [6, 10, 5, 5]
    for n in plats or []:
        if n in PLATFORMS: z = [max(a, b) for a, b in zip(z, PLATFORMS[n]["safe"])]
    crop = None
    if ar in ("4:5", "1:1"):
        y0 = crop_y0(ar, cy); h = FRAMES[ar][1]; crop = [round(y0 / 19.2, 2), round((y0 + h) / 19.2, 2)]
        z = [6, 10, 5, 5]                                   # بعد القص حدود المنصة تنحسب من الكادر المقصوص
    lo = (crop[0] if crop else 0) + z[0] * ((crop[1] - crop[0]) / 100 if crop else 1)
    hi = (crop[1] if crop else 100) - z[1] * ((crop[1] - crop[0]) / 100 if crop else 1)
    return {"zone": z, "crop": crop, "capMin": round(lo + 6, 1), "capMax": round(hi - 1, 1), "ar": ar, "platforms": [n for n in plats or [] if n in PLATFORMS]}
def platform_text(names=None):
    L = []
    for n in (names or list(PLATFORMS)):
        P_ = PLATFORMS.get(n)
        if not P_: continue
        L.append("◆ %s: المقاس %s · المدة المسموحة %s · الأنسب %s · مناطق مغطاة (فوق %d%% · تحت %d%% · يسار %d%% · يمين %d%%)" % (P_["ar"], " أو ".join(P_["frames"]), P_["max"], P_["best"], *P_["safe"]))
        L += ["    - " + x for x in P_["tips"]]
    return "\n".join(L)
def reframe(work, src, ar, cy, log=print):
    """يطلّع نسخة بمقاس ثاني من الماستر العمودي. 4:5 و1:1 قص · 16:9 المقطع بالنص وخلفية مغبّشة منه."""
    if ar == "9:16" or ar not in FRAMES: return None
    out = J(work, "ad-%s.mp4" % ar.replace(":", "x")); w, h = FRAMES[ar]
    if ar == "16:9": fc = "[0:v]split[a][b];[a]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,boxblur=28:3,eq=brightness=-0.14[bg];[b]scale=-2:1080[fg];[bg][fg]overlay=(W-w)/2:0,format=yuv420p[v]"
    else: fc = "[0:v]crop=%d:%d:0:%d,format=yuv420p[v]" % (w, h, crop_y0(ar, cy))
    log("نسخة بمقاس %s…" % ar)
    run(["ffmpeg", "-v", "error", "-nostats", "-i", src, "-filter_complex", fc, "-map", "[v]", "-map", "0:a?", "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-profile:v", "high", "-pix_fmt", "yuv420p",
         "-color_range", "tv", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-r", "30", "-c:a", "copy", "-movflags", "+faststart", "-y", out], log)
    return os.path.basename(out)

# ───────────────────────── التصدير ─────────────────────────
CLEAN_AF = "highpass=f=80,afftdn=nf=-28:nt=w,acompressor=threshold=-18dB:ratio=3:attack=8:release=120,"
def render_frames(work, S, log, rng=None):
    try: vision_ensure(work, log)
    except Exception as e: log("تنبيه: ما قدرت أجهّز قص الشخص أو مكان الوجه (%s). التصدير يكمل بدونها." % str(e)[:120])
    cmd = ["node", os.path.join(S, "04_render_frames.js"), work] + (["range", str(rng[0]), str(rng[1])] if rng else ["all", "--force"])
    log("$ 04_render_frames.js " + " ".join(cmd[3:]))
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace"); ok = False
    for line in p.stdout:
        if "Failed to load resource" in line: continue
        log(line.rstrip())
        if "فريم مرسوم من" in line: ok = True; time.sleep(1.5); p.kill(); break
    p.wait()
    if not ok: raise RuntimeError("الرسم ما اكتمل — شوف السجل")
# ───────────────────────── 3.8: العين (مكان الوجه + قناع الشخص) ─────────────────────────
# كله محلي: engine/scripts/21_vision.js يشغّل كروم بلا واجهة على فريمات المشروع، بموديلات داخل engine/vision. ما يطلع شي من الجهاز.
def vision_run(work, args, log=print):
    eng = find_engine(None)
    if not eng: raise RuntimeError("ما لقيت مجلد engine")
    return run(["node", os.path.join(eng, "scripts", "21_vision.js"), work] + [str(x) for x in args], log, check=False).returncode == 0
def _nvf(work):
    try: return len([f for f in os.listdir(J(work, "vfr")) if f.endswith(".jpg")])
    except OSError: return 0
def mask_ranges(work):
    try: return json.loads(open(J(work, "hs-mask.js"), encoding="utf-8").read().split("=", 1)[1].rstrip().rstrip(";")).get("ranges") or []
    except Exception: return []
def mask_need(work):
    """المدى (بالثواني) لكل طبقة خلفية أو نص خلف الشخص ما له قناع كامل."""
    n = _nvf(work); have = mask_ranges(work); need = []
    if not n: return need
    for L in ((load_studio(work).get("hs") or {}).get("layers") or []):
        if L.get("type") not in ("bg", "behind") or L.get("off"): continue
        try: a, b = float(L["s"]), float(L["e"])
        except Exception: continue
        f0 = max(1, int(a * 30) + 1); f1 = min(n, int(b * 30 + 0.999) + 1)
        if f1 >= f0 and not any(r[0] <= f0 and r[1] >= f1 for r in have): need.append("%.2f-%.2f" % (a, b))
    for a, b in dahih_cut_ranges(work, n / 30.0):   # 4.2: مكتب الدحيح يحتاج قص الشخص بكل مدى خلفيته مو «original»
        f0 = max(1, int(a * 30) + 1); f1 = min(n, int(b * 30 + 0.999) + 1)
        if f1 >= f0 and not any(r[0] <= f0 and r[1] >= f1 for r in have): need.append("%.2f-%.2f" % (a, b))
    return need
def dahih_cut_ranges(work, total):
    D = (load_studio(work).get("hs") or {}).get("dahih") or {}
    if not D.get("on"): return []
    pts = [(0.0, D.get("bg") or "paper")] + sorted(((float(b["s"]), b["mode"]) for b in (D.get("bgs") or []) if b.get("mode")), key=lambda x: x[0])
    out = []
    for i, (a, m) in enumerate(pts):
        b = pts[i + 1][0] if i + 1 < len(pts) else total
        if m != "original" and b > a: out.append((max(0.0, a - 0.5), min(total, b + 0.1)))
    return out
def face_stale(work):
    fj = J(work, "face.json"); src = J(work, "cutz.mp4")
    if not _nvf(work): return False
    try: return (not os.path.exists(fj)) or (os.path.exists(src) and os.path.getmtime(fj) < os.path.getmtime(src))
    except OSError: return True
def vision_ensure(work, log=print):
    """يجهّز الناقص فقط: مكان الوجه + أقنعة الطبقات اللي تحتاجها. يرجّع قائمة اللي سواه."""
    did = []
    if face_stale(work):
        log("أحدد مكان الوجه عشان الكروت ما تقص وجهه…"); did.append("face" if vision_run(work, ["face"], log) else "face!")
    need = mask_need(work)
    if need:
        log("أقص الشخص عن الخلفية للمدى: " + " · ".join(need)); did.append("mask" if vision_run(work, ["mask"] + need, log) else "mask!")
    return did
def vision_reset(work):
    shutil.rmtree(J(work, "mk"), ignore_errors=True)
    for f in ("hs-mask.js", "face.json", "hs-face.js"):
        try: os.remove(J(work, f))
        except OSError: pass

# ───────────────────────── 3.8: أصوات المستخدم ─────────────────────────
# يحط ملفاته في ~/.hojas-studio/my-sounds (أو يرفعها من الاستوديو). تتحول wav وتاخذ رقماً يبدأ بـ my، وتنستخدم مثل أصوات المكتبة.
AUD_EXT = (".wav", ".mp3", ".m4a", ".aac", ".ogg", ".flac", ".opus", ".wma", ".aif", ".aiff")
def my_dir(): d = os.path.join(HOME_CFG, "my-sounds"); os.makedirs(d, exist_ok=True); return d
def my_meta_path(): return os.path.join(HOME_CFG, "my-sounds.json")
def my_list(sync=True):
    meta = [m for m in (rj(my_meta_path(), []) or []) if isinstance(m, dict) and m.get("id")]; ch = False
    if sync:
        files = sorted(f for f in os.listdir(my_dir()) if f.lower().endswith(AUD_EXT)); known = {m.get("file") for m in meta}
        keep = [m for m in meta if m.get("file") in files and sfx_have(m["id"])]
        if len(keep) != len(meta):
            for m in meta:
                if m not in keep:
                    try: os.remove(sfx_path(m["id"]))
                    except OSError: pass
            meta = keep; ch = True
        for f in files:
            if f in known: continue
            nid = "my%d" % (max([int(re.sub(r"\D", "", m["id"]) or 0) for m in meta] or [0]) + 1); src = os.path.join(my_dir(), f)
            try:
                r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vn", "-ac", "2", "-ar", "48000", sfx_path(nid)], capture_output=True)
                if r.returncode or not sfx_have(nid): continue
                pr = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", sfx_path(nid)], capture_output=True, text=True)
                d = round(float((pr.stdout or "0").strip() or 0), 1)
            except Exception: continue
            meta.append({"id": nid, "name": os.path.splitext(f)[0][:60], "file": f, "dur": d, "note": ""}); ch = True
        if ch: wj(my_meta_path(), meta)
    return meta
# 4.19: أصوات من حسابه بخدمة أصوات مربوطة بـ Claude (موصّل، بدون مفاتيح API). Claude يسجّل وش المربوط، وصفحة الأسئلة تسأله منين الأصوات
SOUND_KNOWN = {"elevenlabs": {"name": "ElevenLabs", "can": ["sfx", "music", "voice"]}, "higgsfield": {"name": "Higgsfield", "can": ["sfx", "music"]}}
def sound_cfg_path(): return os.path.join(HOME_CFG, "sound.json")
def sound_providers(): return [p for p in ((rj(sound_cfg_path(), {}) or {}).get("providers") or []) if isinstance(p, dict) and p.get("id")]
def sound_set(ids, names=None):
    out = []
    for i, x in enumerate(ids):
        k = re.sub(r"[^a-z0-9_-]+", "", str(x).lower())
        if not k: continue
        kn = SOUND_KNOWN.get(k) or {}; out.append({"id": k, "name": ((names or [None] * len(ids))[i] if names and i < len(names) else None) or kn.get("name") or x, "can": kn.get("can") or ["sfx", "music"]})
    os.makedirs(HOME_CFG, exist_ok=True); wj(sound_cfg_path(), {"providers": out, "at": int(time.time())}); return out
def sound_name(pid): return next((p["name"] for p in sound_providers() if p["id"] == pid), (SOUND_KNOWN.get(pid) or {}).get("name") or pid)
def cmd_sound(args):
    sub = args[0] if args else "providers"
    if sub != "providers": sys.exit("sound providers [set <elevenlabs|higgsfield|…> [--name \"…\"] | off]")
    rest = list(args[1:])
    if rest[:1] == ["off"]: sound_set([]); print("انشالت خدمات الأصوات. الأصوات من المكتبة المجانية بس."); return
    if rest[:1] == ["set"]:
        names = []
        if "--name" in rest: i = rest.index("--name"); names = [rest[i + 1]]; del rest[i:i + 2]
        P = sound_set(rest[1:], names); print("الخدمات المربوطة: " + (" · ".join(p["name"] for p in P) or "ولا وحدة")); return
    P = sound_providers(); print(chr(10).join("%-12s %s  (%s)" % (p["id"], p["name"], "، ".join(p["can"])) for p in P) or "ما فيه خدمة أصوات مربوطة. الأصوات من المكتبة المجانية (CC0).")
def my_import(src, name=None, note="", gen=None, prompt=None):
    if not os.path.isfile(src) or not src.lower().endswith(AUD_EXT): raise ValueError("مو ملف صوت: " + src)
    base = re.sub(r"[^\w.\- ]+", "_", os.path.basename(src)); dst = os.path.join(my_dir(), base)
    if os.path.abspath(src) != os.path.abspath(dst): shutil.copy(src, dst)
    meta = my_list(); m = next((x for x in meta if x.get("file") == base), None)
    if not m: raise RuntimeError("ما قدرت أقرأ الصوت: " + base)
    if name: m["name"] = name[:60]
    if note: m["note"] = note[:200]
    if gen: m["gen"] = re.sub(r"[^a-z0-9_-]+", "", str(gen).lower())[:30]; m["at"] = int(time.time())   # 4.19: مولّد من حسابه
    if prompt: m["prompt"] = str(prompt)[:300]
    wj(my_meta_path(), meta); return m
def my_edit(i, name=None, note=None, delete=False):
    meta = my_list(False); m = next((x for x in meta if x["id"] == i), None)
    if not m: return meta
    if delete:
        for f in (sfx_path(i), os.path.join(my_dir(), m.get("file") or "-")):
            try: os.remove(f)
            except OSError: pass
        meta = [x for x in meta if x["id"] != i]
    else:
        if name is not None: m["name"] = str(name)[:60] or m["name"]
        if note is not None: m["note"] = str(note)[:200]
    wj(my_meta_path(), meta); return meta
def sfx_all():
    """مكتبة السكل + أصوات المستخدم بشكل واحد."""
    out = [dict(x, have=sfx_have(x["id"]), long=float(x.get("sec") or 0) > 8) for x in sfx_lib()]
    for m in my_list(): out.append({"id": m["id"], "ar": m["name"], "en": m["name"], "dur": "%ss" % m.get("dur", 0), "have": True, "mine": True, "note": m.get("note", ""), "long": float(m.get("dur") or 0) > 8})
    return out

# ───────────────────────── 3.8: وش يتثبّت وليش (شفافية) ─────────────────────────
TOOLS = [
    ("ffmpeg", "يقص الفيديو ويركّب الصوت والصورة ويطلّع الملف النهائي", "برنامج مفتوح المصدر معروف (ffmpeg.org) · 90 ميقا تقريباً", lambda: bool(shutil.which("ffmpeg"))),
    ("Python + whisper", "يفرّغ كلامك لنص بتوقيت كل كلمة عشان الكابشن", "مكتبة OpenAI المفتوحة (openai-whisper) وموديلها ينزل مرة وحدة 1.4 قيقا · يشتغل على جهازك وصوتك ما ينرفع لأي مكان", lambda: importlib.util.find_spec("whisper") is not None),
    ("Node.js + puppeteer-core", "يشغّل متصفح كروم بدون نافذة عشان يرسم الكابشن والكروت فريم فريم", "Node من nodejs.org و puppeteer-core من قوقل (مكتبة تحكم بالمتصفح) · ما يفتح مواقع ولا يدخل حساباتك", lambda: bool(shutil.which("node")) and deps_ok()),
    ("Google Chrome أو Edge", "نفس المتصفح اللي عندك، يُستخدم كمحرّك رسم فقط", "ما يتثبّت شي جديد لو عندك واحد منهم", lambda: True),
    ("Git for Windows", "على ويندوز فقط: يشغّل سكربتات التجميع (bash)", "من git-scm.com", lambda: os.name != "nt" or bool(shutil.which("bash"))),
]
NET_USE = [
    "خطوط Google: ينزّل ملف الخط اللي تختاره (fonts.googleapis.com). بلا نت يشتغل بخط مرفوع.",
    "مكتبة الأصوات: أول مرة تستخدم صوتاً ينزل من مصدره (Mixkit، أو مكتبة CC0 على GitHub) وينحفظ على جهازك.",
    "بحث الصور والمقاطع: يسأل ويكيميديا كومنز بكلمات البحث فقط وينزّل اللي تختاره.",
    "لقطة موقع: يفتح الرابط اللي تكتبه أنت فقط.",
    "غير هذا ما فيه أي اتصال: الفيديو والصوت والنص والوجه كلها تتعالج على جهازك.",
    "إشعارات الجوال (لو فعّلتها بنفسك): الإشعار والمقطع المرفق يمرّون على خادم ntfy.sh ساعات قليلة، واسم القناة هو كلمة السر.",
    "النشر (لو طلبته): من متصفحك وبحسابك بأداة Claude in Chrome، وClaude يوقف قبل زر النشر لين توافق."
]
def tools_text():
    L = ["الأدوات اللي يحتاجها Hojas Studio (كلها مجانية ومفتوحة المصدر، وما يتثبّت شي إلا بموافقتك):", ""]
    for name, why, src, ok in TOOLS:
        try: good = ok()
        except Exception: good = False
        L += ["%s %s" % ("✓" if good else "□", name), "   ليش: " + why, "   وش هو: " + src, ""]
    L += ["وش يتصل بالنت:"] + ["  · " + x for x in NET_USE]
    L += ["", "الخادم محلي على جهازك (127.0.0.1). رابط الجوال يشتغل على شبكة البيت فقط وبرمز دخول، ورابط العميل برمز ثاني بصلاحية تعليق فقط.",
          "فصل الشخص وتحديد الوجه بموديلات محفوظة داخل السكل (engine/vision، من MediaPipe المفتوح): ما ترفع صورتك لأي خدمة."]
    return "\n".join(L)
# ───────────────────────── مكتبة المؤثرات الصوتية (3.6) ─────────────────────────
# 30 صوت من Mixkit. رخصتها تسمح باستخدامها داخل الفيديو، وما تسمح بإعادة توزيع الملفات نفسها،
# فالسكل ما يحملها معه: كل جهاز ينزّلها من المصدر مرة وحدة وتنحفظ في ~/.hojas-studio/sfx
# 4.7: + 128 صوت وموسيقى CC0 (أرقامها cc-…) من agent-video-editor، مثبّتة على نسخة محددة من المستودع
# عشان ما تتغير. الموسيقى mp3 فتتحول لـ wav أول ما تنزل.
def sfx_lib():
    return rj(os.path.join(HERE, "sfxlib.json"), []) or []
SFX_CAT = {"mixkit": "الأساسية (Mixkit)", "transition": "انتقال", "click": "نقر", "appear": "ظهور", "notification": "تنبيه", "success": "نجاح",
           "error": "خطأ", "typing": "كتابة", "impact": "ضربة", "stinger": "فاصل موسيقي", "office": "فلوس وورق", "ambience": "أجواء", "music": "موسيقى"}
def sfx_dir():
    d = os.path.join(HOME_CFG, "sfx"); os.makedirs(d, exist_ok=True); return d
def sfx_path(i): return os.path.join(sfx_dir(), os.path.basename(str(i)) + ".wav")
def sfx_have(i):
    try: return os.path.getsize(sfx_path(i)) > 2000
    except OSError: return False
def sfx_fetch(ids=None, log=None):
    """ينزّل الناقص. يرجّع (كم نزل، قائمة اللي فشل)."""
    lib = {x["id"]: x for x in sfx_lib()}; ids = [i for i in (ids or list(lib)) if i in lib]; ok = 0; bad = []
    for i in ids:
        if sfx_have(i): continue
        try:
            b = None; err = None
            for u in [x for x in (lib[i].get("url"), lib[i].get("url2")) if x]:
                try:
                    rq = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (Hojas Studio)"})
                    b = urllib.request.urlopen(rq, timeout=60).read(); break
                except Exception as e: err = e
            if b is None: raise err or ValueError("ما فيه رابط")
            mp3 = b[:3] == b"ID3" or (len(b) > 1 and b[0] == 0xFF and (b[1] & 0xE0) == 0xE0)
            if len(b) < 2000 or not (b[:4] == b"RIFF" or mp3): raise ValueError("الملف مو صوت")
            tmp = sfx_path(i) + ".part"; open(tmp, "wb").write(b)
            if mp3:
                src = tmp + ".mp3"; os.replace(tmp, src)
                r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-ar", "48000", "-ac", "2", "-f", "wav", tmp], capture_output=True)
                try: os.remove(src)
                except OSError: pass
                if r.returncode != 0 or not os.path.isfile(tmp): raise ValueError("ffmpeg ما حوّل الموسيقى")
            os.replace(tmp, sfx_path(i)); ok += 1
            if log: log("نزل: %s (%s)" % (lib[i]["ar"], i))
        except Exception as e:
            bad.append(i)
            if log: log("فشل: %s (%s) ← %s" % (lib[i]["ar"], i, str(e)[:90]))
    return ok, bad
def cmd_sfx(work, args):
    sub = args[0] if args else "list"; lib = sfx_lib(); mine = my_list(); ids = {x["id"] for x in lib} | {m["id"] for m in mine}
    if sub == "list":
        want = args[1] if len(args) > 1 else ""; cats = []
        for x in lib:
            c = x.get("cat") or "mixkit"
            if c not in cats: cats.append(c)
        if want and want not in cats: sys.exit("الأقسام: " + " · ".join("%s (%s)" % (c, SFX_CAT.get(c, c)) for c in cats))
        for c in ([want] if want else cats):
            print("\n── %s ──" % SFX_CAT.get(c, c))
            for x in [x for x in lib if (x.get("cat") or "mixkit") == c]:
                print("%-30s %-6s %s  %s%s" % (x["id"], x["dur"], "✓" if sfx_have(x["id"]) else "—", x["ar"], ("  ← " + x["use"]) if x.get("use") else ""))
        print("\n✓ = منزّل على هذا الجهاز. نزّل الباقي: hs sfx <work> fetch · قسم واحد: hs sfx <work> list music")
        print("cc-… كلها CC0 (حرة للاستخدام التجاري بدون ذكر المصدر). القواعد: references/editing-rules.md")
        print("\nأصوات المستخدم (ملفاته هو، قدّمها على المكتبة لما تناسب اللحظة):" if mine else "\nما عنده أصوات خاصة بعد. مجلدها: " + my_dir())
        for m in mine: print("%-7s %-6s %s%s%s%s" % (m["id"], "%ss" % m.get("dur", 0), m["name"], "  ← " + m["note"] if m.get("note") else "", "  [مولّد من %s]" % sound_name(m["gen"]) if m.get("gen") else "", "  (طويل: يصلح خلفية أو موسيقى، حدد المدة [ث, قوة, مدة])" if float(m.get("dur") or 0) > 8 else ""))
        return
    if sub == "import":
        rest = list(args[1:]); fl = {}
        for flag_ in ("--name", "--note", "--gen", "--prompt"):
            if flag_ in rest: i = rest.index(flag_); fl[flag_] = rest[i + 1]; del rest[i:i + 2]
        nm, nt = fl.get("--name"), fl.get("--note")
        if not rest: sys.exit("sfx import <ملف صوت أو مجلد> [--name \"…\"] [--note \"متى ينستخدم\"] [--gen elevenlabs --prompt \"…\"]")
        src = os.path.abspath(rest[0]); files = [os.path.join(src, f) for f in sorted(os.listdir(src)) if f.lower().endswith(AUD_EXT)] if os.path.isdir(src) else [src]
        for f in files:
            try: m = my_import(f, nm if len(files) == 1 else None, nt or "", fl.get("--gen"), fl.get("--prompt")); print("انضاف: %s ← %s (%ss)%s" % (m["id"], m["name"], m.get("dur"), ("  مولّد من " + sound_name(m["gen"])) if m.get("gen") else ""))
            except Exception as e: print("فشل: %s ← %s" % (os.path.basename(f), str(e)[:100]))
        return
    if sub == "fetch":
        ok, bad = sfx_fetch(args[1:] or None, print); print("نزل %d · فشل %d%s" % (ok, len(bad), (" (يحتاج نت)" if bad else ""))); return
    if sub in ("add", "rm"):
        if len(args) < 3: sys.exit("sfx %s <id> <ثانية> [ثانية …]   (الأصوات المبنية: tap · thud · whoosh_up · whoosh_down)" % sub)
        k = args[1]
        if k not in ids and k not in ("tap", "thud", "whoosh_up", "whoosh_down"): sys.exit("ما فيه صوت بهذا الرقم. شوف: hs sfx <work> list")
        if k in {x["id"] for x in lib} and sub == "add" and not sfx_have(k):
            _, bad = sfx_fetch([k], print)
            if bad: sys.exit("ما قدرت أنزّل الصوت (يحتاج نت).")
        sp = J(work, "sfx.json"); s = rj(sp, {"outro": 0}) or {"outro": 0}; ts = [round(float(x), 3) for x in args[2:]]; cur = s.get(k) or []
        if sub == "add": cur = sorted(cur + ts, key=lambda q: q[0] if isinstance(q, list) else q)
        else: cur = [q for q in cur if not any(abs((q[0] if isinstance(q, list) else q) - t) < 0.06 for t in ts)]
        if cur: s[k] = cur
        else: s.pop(k, None)
        wj(sp, s); print("تم: %s ← %s" % (k, cur)); return
    sys.exit("sfx: list | fetch [id …] | add <id> <ث> … | rm <id> <ث> … | import <ملف أو مجلد>")
def build_sfx(work, S, log, gains):
    sfx = rj(J(work, "sfx.json"), {"outro": 0}) or {"outro": 0}
    types = [k for k, v in sfx.items() if isinstance(v, list) and v]
    if not types or all(abs(float(gains.get(k, 1)) - 1) < 0.01 for k in types):
        run([PY, os.path.join(S, "05_sfx.py"), work], log, cwd=work, check=False); return
    tmp = J(work, ".hs", "sfxtmp"); shutil.rmtree(tmp, ignore_errors=True); ins = []; flt = []
    for n, k in enumerate(types):
        d = os.path.join(tmp, k); os.makedirs(d); shutil.copy(J(work, "caps.json"), os.path.join(d, "caps.json"))
        wj(os.path.join(d, "sfx.json"), {"outro": sfx.get("outro", 0), k: sfx[k]})
        run([PY, os.path.join(S, "05_sfx.py"), d], log, check=False)
        if os.path.exists(os.path.join(d, "sfx.wav")): ins += ["-i", os.path.join(d, "sfx.wav")]; flt.append("[%d:a]volume=%.3f[s%d]" % (len(flt), float(gains.get(k, 1)), len(flt)))
    if not flt: return
    fc = ";".join(flt) + ";" + "".join("[s%d]" % i for i in range(len(flt))) + "amix=inputs=%d:duration=longest:normalize=0[o]" % len(flt)
    run(["ffmpeg", "-v", "error"] + ins + ["-filter_complex", fc, "-map", "[o]", "-ac", "2", "-ar", "48000", "-y", J(work, "sfx.wav")], log)
def bg_fades(mix):
    """تلاشي الصوت بالخلفية بالثواني (بداية، نهاية). الافتراضي 1.0 و1.4، والحد 0 إلى 6."""
    def f(k, d):
        try: v = float(mix.get(k, d))
        except (TypeError, ValueError): v = d
        return str(round(min(max(v, 0.0), 6.0), 2))
    return f("bgIn", 1.0), f("bgOut", 1.4)
# ── 4.6: كتم الكلمات (بيب). studio.json ← hs.bleep = {mode: beep|mute, cap: stars|hide|keep, tone: هيرتز, items: [{s, e, t}]} بزمن الإخراج ──
BLEEP_MODES = ("beep", "mute"); BLEEP_CAPS = ("stars", "hide", "keep")
BLEEP_PRE = ("وال", "بال", "فال", "كال", "لل", "ال", "و", "ف", "ب", "ل", "ك")
def bleep_of(hs):
    b = (hs or {}).get("bleep") or {}; out = []
    for x in b.get("items") or []:
        try: s0, e0 = float(x["s"]), float(x["e"])
        except (KeyError, TypeError, ValueError): continue
        if e0 - s0 >= 0.04: out.append({**x, "s": round(max(0.0, s0), 3), "e": round(e0, 3)})
    out.sort(key=lambda x: x["s"])
    try: tone = int(min(max(float(b.get("tone", 1000)), 300), 3000))
    except (TypeError, ValueError): tone = 1000
    return {"items": out, "mode": b.get("mode") if b.get("mode") in BLEEP_MODES else "beep",
            "cap": b.get("cap") if b.get("cap") in BLEEP_CAPS else "stars", "tone": tone}
def bleep_filters(B):
    """(قطعة تنحط بسلسلة صوت الكلام وتكتمه، فلتر صوت البيب أو None). بلا كلمات = ("", None) والصوت نفسه بالضبط."""
    if not B["items"]: return "", None
    ex = "+".join("between(t,%.3f,%.3f)" % (x["s"], x["e"]) for x in B["items"])
    mute = "volume=0:enable='%s'," % ex
    if B["mode"] != "beep": return mute, None
    end = round(B["items"][-1]["e"] + 0.5, 3)
    return mute, "sine=frequency=%d:sample_rate=48000:duration=%.3f,volume=1.5,volume=0:enable='not(%s)',aformat=sample_rates=48000:channel_layouts=stereo" % (B["tone"], end, ex)
def _bnorm(w): return re.sub(r"[^\w]", "", norm_txt(w))
def bleep_hit(w, items):
    m = (float(w["s"]) + float(w["e"])) / 2
    return any(x["s"] - 1e-6 <= m <= x["e"] + 1e-6 for x in items)
def bleep_star(t):
    a = list(str(t)); return "*" if len(a) < 2 else a[0] + "*" * min(5, len(a) - 1)
def bleep_card_text(c, B):
    """نص الجملة للترجمة والنص المكتوب: الكلمة المكتومة نجوم (إلا لو اختار «كما هي»)."""
    if not B["items"] or B["cap"] == "keep": return card_key(c)
    return " ".join(bleep_star(w["t"]) if bleep_hit(w, B["items"]) else w["t"] for w in c["w"])
def bleep_match(word, targets):
    n = _bnorm(word)
    if not n: return False
    if n in targets: return True
    return any(n.startswith(p) and n[len(p):] in targets and len(n) - len(p) >= 2 for p in BLEEP_PRE)
def bleep_find(caps, words):
    """كل مرة انقالت فيها الكلمة (بدون همزات وتاء مربوطة، ومع و ب ل ال قبلها). يرجّع [{s, e, t}]."""
    targets = {_bnorm(w) for w in words if _bnorm(w)}; out = []
    if not targets: return out
    for c in (caps or {}).get("cards") or []:
        for w in c.get("w") or []:
            if bleep_match(w["t"], targets): out.append({"s": round(max(0.0, w["s"] - 0.03), 3), "e": round(w["e"] + 0.03, 3), "t": w["t"]})
    return out
def bleep_add(hs, new):
    """يضيف بدون تكرار (نفس الكلمة بنفس الوقت). يرجّع كم انضاف."""
    b = hs.setdefault("bleep", {}); items = b.setdefault("items", []); n = 0
    for x in new:
        if any(abs(float(y.get("s", 0)) - x["s"]) < 0.08 and abs(float(y.get("e", 0)) - x["e"]) < 0.08 for y in items): continue
        items.append(x); n += 1
    items.sort(key=lambda x: float(x.get("s", 0))); return n
def cmd_bleep(work, args):
    sub = args[0] if args else "list"; st = load_studio(work); hs = hs_of(st); caps = rj(J(work, "caps.json"), {}) or {}
    if sub == "list":
        B = bleep_of(hs); print("الصوت: %s · الكابشن: %s · النغمة %d هيرتز" % ({"beep": "بيب", "mute": "صمت"}[B["mode"]], {"stars": "نجوم", "hide": "مربع", "keep": "كما هي"}[B["cap"]], B["tone"]))
        if not B["items"]: print("ما فيه كلمات مكتومة. مثال: hs bleep <work> word فلان"); return
        for i, x in enumerate(B["items"]): print("%2d) %6.2f-%6.2f  %s" % (i + 1, x["s"], x["e"], x.get("t", "")))
        return
    if sub == "word":
        if len(args) < 2: sys.exit("bleep <work> word <كلمة> [كلمة …]")
        hits = bleep_find(caps, args[1:]); n = bleep_add(hs, hits); wj(J(work, "studio.json"), st)
        print("لقيتها %d مرة، وانكتم %d جديد." % (len(hits), n) if hits else "ما لقيت الكلمة بالكلام. شوف النص: hs text <work>"); return
    if sub == "at":
        if len(args) < 2: sys.exit("bleep <work> at <ثانية>")
        t0 = float(args[1]); hit = None
        for c in caps.get("cards") or []:
            for w in c["w"]:
                if w["s"] - 0.05 <= t0 <= w["e"] + 0.05: hit = w
        if not hit: sys.exit("ما فيه كلمة عند %s" % args[1])
        n = bleep_add(hs, [{"s": round(max(0.0, hit["s"] - 0.03), 3), "e": round(hit["e"] + 0.03, 3), "t": hit["t"]}]); wj(J(work, "studio.json"), st); print("انكتمت: %s" % hit["t"] if n else "مكتومة من قبل"); return
    if sub == "add":
        if len(args) < 3: sys.exit("bleep <work> add <من> <إلى>")
        a, b = float(args[1]), float(args[2])
        if b - a < 0.04: sys.exit("المدة قصيرة")
        bleep_add(hs, [{"s": round(a, 3), "e": round(b, 3), "t": ""}]); wj(J(work, "studio.json"), st); print("تم"); return
    if sub == "rm":
        if len(args) < 2: sys.exit("bleep <work> rm <رقم|all>")
        b = hs.setdefault("bleep", {}); items = sorted(b.get("items") or [], key=lambda x: float(x.get("s", 0)))
        if args[1] == "all": items = []
        else:
            k = int(args[1]) - 1
            if not 0 <= k < len(items): sys.exit("ما فيه رقم %s" % args[1])
            items.pop(k)
        b["items"] = items; wj(J(work, "studio.json"), st); print("باقي %d" % len(items)); return
    if sub in ("mode", "cap", "tone"):
        if len(args) < 2: sys.exit("bleep <work> mode beep|mute · cap stars|hide|keep · tone <هيرتز>")
        v = args[1]; ok = {"mode": BLEEP_MODES, "cap": BLEEP_CAPS}.get(sub)
        if ok and v not in ok: sys.exit("القيم: " + " | ".join(ok))
        hs.setdefault("bleep", {})[sub] = int(float(v)) if sub == "tone" else v; wj(J(work, "studio.json"), st); print("تم"); return
    sys.exit("bleep: list | word <كلمة> … | at <ث> | add <من> <إلى> | rm <رقم|all> | mode beep|mute | cap stars|hide|keep | tone <هيرتز>")
def vr_filters(mix):
    """4.11: مستوى صوت لأجزاء من كلامك (كتم أو خفض أو رفع) بزمن المقطع."""
    out = ""
    for r in mix.get("vr") or []:
        try: s, e, g = float(r["s"]), float(r["e"]), max(0.0, min(3.0, float(r.get("g", 1))))
        except Exception: continue
        if e - s >= 0.02 and abs(g - 1) > 1e-3: out += "volume=%.3f:enable='between(t,%.3f,%.3f)'," % (g, s, e)
    return out
# 4.21: حارس الصوت: المؤثرات ما تعلو على صوتك، والموسيقى تبقى تحته بوضوح (يقيس صوتك بالمقطع نفسه)
def _rms_windows(path, sr=8000, win=0.4, limit=None):
    try: raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr)] + (["-t", str(limit)] if limit else []) + ["-f", "s16le", "-"], capture_output=True, timeout=120).stdout
    except Exception: return []
    a = array.array("h"); a.frombytes(raw[: len(raw) // 2 * 2]); n = int(sr * win); out = []
    for i in range(0, len(a) - n + 1, n):
        seg = a[i:i + n]; ss = sum(x * x for x in seg) / n
        out.append((i / sr, 10 * math.log10(ss / 1073741824.0 + 1e-12)))
    return out
def voice_guard(work, mix, log, voice_src, sfx_margin=3.0, bg_margin=12.0):
    """يرجّع (معامل المؤثرات، مستوى الموسيقى). صوتك = وسط مستوى الكلام، والمؤثر الأعلى ما يتعدى صوتك ناقص 3 dB، والموسيقى صوتك ناقص 12 dB."""
    bg = float(mix.get("bg", 0.28) or 0)
    if mix.get("guard") is False: return 1.0, bg
    words = sorted((w["s"], w["e"]) for c in (rj(J(work, "caps.json"), {}) or {}).get("cards", []) for w in c.get("w", []))
    V = _rms_windows(voice_src)
    if not V or not words: return 1.0, bg
    sp, j = [], 0
    for t0, db in V:
        tc = t0 + 0.2
        while j < len(words) and words[j][1] < tc: j += 1
        if j < len(words) and words[j][0] <= tc <= words[j][1] and db > -60: sp.append(db)
    if len(sp) < 5: return 1.0, bg
    sp.sort(); vlev = sp[len(sp) // 2] + 20 * math.log10(max(float(mix.get("voice", 1) or 1), 1e-3)); g = 1.0
    if os.path.exists(J(work, "sfx.wav")):
        Sx = [db for _, db in _rms_windows(J(work, "sfx.wav"))]
        if Sx and max(Sx) > vlev - sfx_margin:
            g = 10 ** ((vlev - sfx_margin - max(Sx)) / 20); log("حارس الصوت: خفّضت المؤثرات %.1f dB عشان ما تعلو على صوتك" % (20 * math.log10(g)))
    mf = music_file(work)
    if mf and bg > 0:
        M = sorted(db for _, db in _rms_windows(mf, limit=90) if db > -60)
        if M:
            eff = M[int(len(M) * 0.75)] + 20 * math.log10(bg)
            if eff > vlev - bg_margin:
                nb = bg * 10 ** ((vlev - bg_margin - eff) / 20); log("حارس الصوت: الموسيقى %.2f ← %.2f عشان تبقى تحت صوتك" % (bg, nb)); bg = nb
    return g, round(bg, 4)
def encode(work, S, log, out_final, out_master, mix):
    caps = rj(J(work, "caps.json")); sfx = rj(J(work, "sfx.json"), {"outro": 0}) or {}
    dur = round(caps["total"] + sfx.get("outro", 0), 3); fade = round(dur - 0.6, 3)
    svf, svm = voice_track(work, mix, log)      # 4.12: صوت استوديو (يغني عن التنظيف العادي)
    voice = float(mix.get("voice", 1)); chain = (CLEAN_AF if mix.get("clean") and not svf else "") + VOICE_FX.get(mix.get("voiceFx") or "", "") + "volume=%.3f," % voice + vr_filters(mix)
    has_sfx = os.path.exists(J(work, "sfx.wav")); ins = ["-framerate", "30", "-i", J(work, "out", "%05d.jpg"), "-i", J(work, "cutz.mp4")] + (["-i", J(work, "sfx.wav")] if has_sfx else []) + (["-i", svf] if svf else [])
    bm, bp = bleep_filters(bleep_of(hs_of(load_studio(work)))); a0 = "a0"; ain = "[%d:a]" % (3 if has_sfx else 2) if svf else "[1:a]"
    g_sfx, bg_lv = voice_guard(work, mix, log, svf or J(work, "cutz.mp4"))
    if svf: log("الصوت: " + {"ext": "اللي عالجته من برا", "dub": "الدبلجة", "local": "صوت استوديو"}.get(svm, "صوت استوديو"))
    fc = "[0:v]scale=in_range=pc:out_range=tv:out_color_matrix=bt709,format=yuv420p[vo];%s%s%sapad=pad_dur=8[a0];" % (ain, chain, bm)
    if bp: fc += "%s[bp];[a0][bp]amix=inputs=2:duration=first:normalize=0[a0b];" % bp; a0 = "a0b"
    fc += ("[2:a]volume=%.4f[sx];[%s][sx]amix=inputs=2:duration=first:normalize=0[am];" % (g_sfx, a0) if has_sfx else "[%s]anull[am];" % a0)
    fc += "[am]atrim=0:%s,asetpts=PTS-STARTPTS,afade=t=out:st=%s:d=0.6[ao]" % (dur, fade)
    for f in (out_final, out_master):
        try: os.remove(f)
        except FileNotFoundError: pass
    log("تجميع…")
    run(["ffmpeg", "-v", "error", "-nostats"] + ins + ["-filter_complex", fc, "-map", "[vo]", "-map", "[ao]", "-c:v", "libx264", "-preset", "slow", "-crf", "18",
         "-maxrate", "10M", "-bufsize", "20M", "-profile:v", "high", "-level", "4.0", "-pix_fmt", "yuv420p", "-color_range", "tv", "-colorspace", "bt709",
         "-color_primaries", "bt709", "-color_trc", "bt709", "-r", "30", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", "-y", out_final], log)
    log("معايرة الصوت…"); env = dict(os.environ); env["BG_GAIN"] = str(bg_lv); env["BG_FADE_IN"], env["BG_FADE_OUT"] = bg_fades(mix)
    try: master_audio(work, out_final, out_master, log, float(env["BG_GAIN"]), env["BG_FADE_IN"], env["BG_FADE_OUT"])   # 4.35: بدون bash
    except Exception as e: log("المعايرة ما اشتغلت (%s) — أسلّم الملف بلا معايرة" % str(e)[:160])
    if not os.path.exists(out_master): shutil.copy(out_final, out_master)
def master_audio(work, src, out, log=print, gain=0.28, fade_in=1.0, fade_out=1.4, lufs=-14.0):
    """4.35: معايرة الصوت لـ -14 LUFS + الصوت بالخلفية (bg-audio.*) ينخفض وقت الكلام. نفس 06b_master.sh بس بايثون وffmpeg مباشرة،
    لأن ويندوز يشغّل bash حق WSL بدل Git Bash (يدوّر System32 قبل PATH) فكانت المعايرة تفشل والمقطع يطلع بدونها."""
    dur = ffdur(src) or 0.0
    if dur <= 0: raise RuntimeError("ما قدرت أقرا مدة " + src)
    bg = next((J(work, n + "." + e) for n in ("bg-audio", "bg", "sound", "music") for e in ("mp3", "m4a", "wav", "aac") if os.path.isfile(J(work, n + "." + e))), None)
    fi = round(min(max(float(fade_in or 0), 0.01), max(0.01, dur / 2)), 3); fo_d = round(min(max(float(fade_out or 0), 0.01), max(0.01, dur)), 3); fo = max(0.0, round(dur - fo_d, 3))
    mix = J(work, ".master-mix.wav"); nrm = J(work, ".master-norm.wav")
    try:
        if bg:
            log("الخلفية الصوتية: %s (تنخفض وقت الكلام)" % os.path.basename(bg))
            fc = ("[0:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,asplit=2[v0][sc];"
                  "[1:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,volume=%s,atrim=0:%s,asetpts=N/SR/TB,afade=t=in:st=0:d=%s,afade=t=out:st=%s:d=%s[m];"
                  "[m][sc]sidechaincompress=threshold=0.035:ratio=9:attack=8:release=320[md];[v0][md]amix=inputs=2:duration=first:normalize=0[a]") % (gain, dur, fi, fo, fo_d)
            subprocess.run(["ffmpeg", "-v", "error", "-nostats", "-i", src, "-stream_loop", "-1", "-i", bg, "-filter_complex", fc, "-map", "[a]", "-ac", "2", "-ar", "48000", "-y", mix], check=True)
        else: subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-vn", "-ac", "2", "-ar", "48000", "-y", mix], check=True)
        r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", mix, "-af", "loudnorm=I=%s:TP=-1.5:LRA=11:print_format=json" % lufs, "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8", errors="replace")
        ms = re.findall(r"\{[^{}]*input_i[^{}]*\}", r.stderr, re.S); M = json.loads(ms[-1]) if ms else None
        ii = float(M["input_i"]) if M and M.get("input_i") not in (None, "-inf", "inf") else None
        if M and ii is not None and ii > -70:
            log("الصوت قبل %.1f LUFS، بعد %s LUFS" % (ii, lufs))
            af = "loudnorm=I=%s:TP=-1.5:LRA=11:measured_I=%s:measured_TP=%s:measured_LRA=%s:measured_thresh=%s:linear=true" % (lufs, M["input_i"], M["input_tp"], M["input_lra"], M["input_thresh"])
            subprocess.run(["ffmpeg", "-v", "error", "-nostats", "-i", mix, "-af", af, "-ar", "48000", "-y", nrm], check=True)
        elif M is None: subprocess.run(["ffmpeg", "-v", "error", "-nostats", "-i", mix, "-af", "loudnorm=I=%s:TP=-1.5:LRA=11" % lufs, "-ar", "48000", "-y", nrm], check=True)
        else: log("الصوت صامت، تخطّيت المعايرة"); shutil.copy(mix, nrm)
        subprocess.run(["ffmpeg", "-v", "error", "-nostats", "-i", src, "-i", nrm, "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", "-y", out], check=True)
    finally:
        for f in (mix, nrm):
            try: os.remove(f)
            except OSError: pass
    return out
def export(work, S, log, kind="final", hooks=False, frame=None):
    """kind: final | clean (بلا كابشن). hooks=True يطلّع نسخة لكل صيغة هوك."""
    ensure_media(work, S, log)   # 4.23: القص الفوري يتركّب هنا
    st = load_studio(work); hs = hs_of(st); mix = hs.get("mix") or {}; outs = []
    if kind == "clean": hs["nocap"] = True; wj(J(work, "studio.json"), st)
    try:
        patch(work, quiet=True); render_frames(work, S, log); os.environ["HS_DUCK"] = str(mix.get("duck", 0.45)); build_sfx(work, S, log, mix.get("sfx") or {})
        name = "ad-clean" if kind == "clean" else "ad"
        fin, mas = (J(work, "ad-clean-raw.mp4"), J(work, "ad-clean.mp4")) if kind == "clean" else (J(work, "ad-final.mp4"), J(work, "ad-master.mp4"))
        encode(work, S, log, fin, mas, mix); outs.append(os.path.basename(mas))
        ar, cy = frame_of(hs); ar = frame if frame in FRAMES else ar
        if kind == "final":
            for old in glob.glob(J(work, "ad-[0-9]*x[0-9]*.mp4")): os.remove(old)
            r = reframe(work, mas, ar, cy, log)
            if r: outs.append(r)
        hk = hs.get("hooks") or {}
        if hooks and kind == "final" and hk.get("on") and len(hk.get("items") or []) > 1:
            act = int(hk.get("active", 0)); d = float(hk.get("dur", 2.6)) + 0.5
            for i in range(len(hk["items"])):
                if i == act: continue
                st2 = load_studio(work); hs_of(st2)["hooks"]["active"] = i; wj(J(work, "studio.json"), st2)
                log("نسخة الهوك %d…" % (i + 1)); render_frames(work, S, log, (0, d))
                encode(work, S, log, J(work, "ad-hook-%d-raw.mp4" % (i + 1)), J(work, "ad-hook-%d.mp4" % (i + 1)), mix); outs.append("ad-hook-%d.mp4" % (i + 1))
                try: os.remove(J(work, "ad-hook-%d-raw.mp4" % (i + 1)))
                except OSError: pass
            st2 = load_studio(work); hs_of(st2)["hooks"]["active"] = act; wj(J(work, "studio.json"), st2); render_frames(work, S, log, (0, d))
    finally:
        if kind == "clean":
            st3 = load_studio(work); hs_of(st3).pop("nocap", None); wj(J(work, "studio.json"), st3)
            try: os.remove(J(work, "ad-clean-raw.mp4"))
            except OSError: pass
    if kind == "final":
        ed = J(work, ".hs", "exports"); os.makedirs(ed, exist_ok=True); shutil.copy(J(work, "ad-master.mp4"), os.path.join(ed, time.strftime("%Y%m%d-%H%M%S") + ".mp4"))
        for old in sorted(os.listdir(ed))[:-6]: os.remove(os.path.join(ed, old))
        try: style_learn(work)
        except Exception as e: log("ما قدرت أتعلّم من تعديلاتك: %s" % e)
        main_out = J(work, outs[1] if len(outs) > 1 and not outs[1].startswith("ad-hook") else outs[0])
        notify_quiet("المقطع جاهز: %s" % os.path.basename(work.rstrip("/\\")), title="Hojas Studio: خلص المونتاج", file=main_out, tags="white_check_mark")
    return outs

def srt_ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = int(t % 60); ms = int(round((t - int(t)) * 1000))
    if ms == 1000: s += 1; ms = 0
    return "%02d:%02d:%02d,%03d" % (h, m, s, ms)
def make_srt(work, lang):
    caps = rj(J(work, "caps.json")); cs = caps["cards"]; hs0 = load_studio(work).get("hs") or {}; mp = (hs0.get("en") or {}).get("map") or {}; out = []; n = 0; B = bleep_of(hs0)
    for i, c in enumerate(cs):
        txt = bleep_card_text(c, B) if lang == "ar" else mp.get(card_key(c), "")
        if not txt: continue
        end = min(c["e"], cs[i + 1]["s"] - 0.02) if i + 1 < len(cs) else c["e"]
        if end <= c["s"]: end = c["s"] + 0.4
        n += 1; out.append("%d\n%s --> %s\n%s\n" % (n, srt_ts(c["s"]), srt_ts(end), txt))
    return "\n".join(out), n
def pack(work):
    """حزمة النشر: الفيديو النهائي + SRT عربي/إنجليزي + نص الكلام + نص البوست، في ملف zip واحد."""
    files = []; pk = J(work, "publish"); os.makedirs(pk, exist_ok=True)
    for f in ("ad-master.mp4", "ad-clean.mp4") + tuple(sorted(x for x in os.listdir(work) if re.match(r"ad-(hook-\d+|\d+x\d+)\.mp4$", x))):
        if os.path.exists(J(work, f)): files.append(J(work, f))
    for lang in ("ar", "en"):
        s, n = make_srt(work, lang)
        if n: p = os.path.join(pk, "captions.%s.srt" % lang); open(p, "w", encoding="utf-8").write(s); files.append(p)
    caps = rj(J(work, "caps.json")); B = bleep_of(load_studio(work).get("hs") or {}); p = os.path.join(pk, "transcript.txt"); open(p, "w", encoding="utf-8").write("\n".join(bleep_card_text(c, B) for c in caps["cards"]) + "\n"); files.append(p)
    if os.path.exists(J(work, "post.txt")): files.append(J(work, "post.txt"))
    cr = rj(J(work, "assets", "credits.json"), []) or []; used = set(l.get("src", "").split("/")[-1] for l in (load_studio(work).get("hs") or {}).get("layers") or [])
    cr = [c for c in cr if c["file"] in used]
    if cr:
        p = os.path.join(pk, "credits.txt"); open(p, "w", encoding="utf-8").write("\n".join("%s — %s — %s — %s" % (c.get("title"), c.get("author") or "?", c.get("license"), c.get("source")) for c in cr) + "\n"); files.append(p)
    z = J(work, ".hs", "pack.zip"); os.makedirs(J(work, ".hs"), exist_ok=True)
    with zipfile.ZipFile(z, "w", zipfile.ZIP_STORED) as zf:
        for f in files: zf.write(f, os.path.basename(f))
    return [os.path.basename(f) for f in files]

# ───────────────────────── الأسئلة قبل المونتاج (brief) ─────────────────────────
def brief_paths(work): return J(work, ".hs", "brief_ask.json"), J(work, "brief.json")
def brief_state(work):
    ap, bp = brief_paths(work); ask = rj(ap); ans = rj(bp)
    if not ask: return None
    return "saved" if (ans and ans.get("savedAt", 0) >= ask.get("askedAt", 0)) else "pending"
def brief_ask(work, hooks=(), topics=(), note="", extra=None):
    ap, bp = brief_paths(work); os.makedirs(J(work, ".hs"), exist_ok=True)
    if os.path.exists(bp): shutil.copy(bp, J(work, ".hs", "brief.prev.json"))
    wj(ap, {"askedAt": int(time.time()), "hooks": list(hooks), "topics": list(topics), "note": note, "extra": extra or []})
    say(work, "جهّزت لك أسئلة قبل ما أبدأ المونتاج. جاوب عليها واضغط حفظ.", "ask")
    notify_quiet("جهّزت لك صفحة الأسئلة. افتح الاستوديو وجاوب عشان أبدأ المونتاج.", title="Hojas Studio: أنتظرك", tags="question")
def brief_text(work):
    a = rj(brief_paths(work)[1]) or {}; caps = rj(J(work, "caps.json"), {"cards": []}); L = []
    def row(k, v):
        if v not in (None, "", [], {}): L.append("- %s: %s" % (k, v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)))
    row("نوع المقطع", a.get("goalText") if a.get("goal") == "other" else a.get("goal")); row("المنصات", a.get("platform")); row("المقاس", a.get("frame")); row("ألوان الحساب", a.get("theme")); row("المدة", a.get("length")); row("الإيقاع", a.get("pace"))
    row("الكابشن", a.get("cap")); row("ترجمة إنجليزية", "نعم" if a.get("en") else "لا"); row("الهوك", a.get("hook"))
    row("الشخصية", a.get("char")); row("الصور والمقاطع", a.get("media")); row("كروت الشرح", a.get("cards")); row("المؤثرات", a.get("fx"))
    c = a.get("cut") or {}; drop = [i for i in (c.get("drop") or []) if i < len(caps["cards"])]
    row("القص", {"fillers": c.get("fillers"), "dupes": c.get("dupes")})
    for i in drop: L.append("  · يبي تنشال الجملة %d: %s" % (i + 1, card_key(caps["cards"][i])))
    row("الهوية", a.get("brand")); row("الختام", a.get("outro")); row("إجابات إضافية", a.get("extra")); row("رابط مرجعي", a.get("ref")); row("ملاحظاته", a.get("notes"))
    return "\n".join(L) or "ما فيه إجابات."
def brief_apply(work):
    """يطبّق الإجابات اللي لها إعداد مباشر، ويطبع الباقي كمهام لـ Claude."""
    a = rj(brief_paths(work)[1]) or sys.exit("ما فيه إجابات محفوظة بعد."); sp = J(work, "studio.json"); st = load_studio(work); hs = hs_of(st); todo = []; done = []
    if a.get("brand"):
        b = rj(os.path.join(brand_dir(), a["brand"] + ".json"))
        if b: hs["cap"] = {**(hs.get("cap") or {}), **(b.get("cap") or {})}; hs["en"] = {**(hs.get("en") or {}), **(b.get("en") or {})}; done.append("الهوية: " + a["brand"])
    if a.get("cap"): hs["cap"] = {**{k: v for k, v in (hs.get("cap") or {}).items() if k not in CAP_STYLE_KEYS}, **a["cap"], "on": True}; done.append("إعدادات الكابشن")
    try: done += brand_fonts_defaults(hs)   # 4.9: خط الهوية هو الافتراضي (الكابشن والعنوان فوق)
    except Exception: pass
    plats = [x for x in (a.get("platform") or []) if x in PLATFORMS]; ar = a.get("frame") if a.get("frame") in FRAMES else "9:16"
    hs["frame"] = {**(hs.get("frame") or {}), "ar": ar}; hs["platforms"] = plats; done.append("المقاس " + ar)
    sz = safe_of(plats, ar, frame_of(hs)[1]); cy_ = float((hs.get("cap") or {}).get("y", 76))
    if a.get("cap") and not (sz["capMin"] <= cy_ <= sz["capMax"]):
        ny = min(sz["capMax"], max(sz["capMin"], cy_)); hs["cap"]["y"] = ny; done.append("رفعت/نزّلت الكابشن إلى %s%% عشان يطلع داخل المنطقة الآمنة لمنصاته" % ny)
    th_a = a.get("theme") or {}; tp0 = J(work, "theme.json"); th0 = rj(tp0, {}) or {}
    def _dark(hx, k=0.72):
        try: r, g, b = (int(hx[i:i + 2], 16) for i in (1, 3, 5)); return "#%02X%02X%02X" % (int(r * k), int(g * k), int(b * k))
        except Exception: return hx
    if th_a.get("mode") == "mono": th0.update({"bg": "#0E0E10", "ink": "#FFFFFF", "acc": "#FFE14D", "clay": "#C9A800", "mut": "#9A9AA5"}); done.append("الألوان: أبيض وأسود")
    elif th_a.get("mode") == "identity": pass   # 4.37: تنطبق آخر شي (ident_apply)
    elif th_a.get("mode") == "custom": th0.update({"bg": th_a.get("bg") or "#101014", "ink": th_a.get("ink") or "#FFFFFF", "acc": th_a.get("acc") or "#F2B33D", "clay": _dark(th_a.get("acc") or "#F2B33D"), "mut": "#9A9AA5"}); done.append("الألوان: ألوانه (%s · %s)" % (th0["bg"], th0["acc"]))
    else: todo.append("الألوان: قال «اختر لي من المقطع». اقرأ لقطة من الفيديو واختر خلفية غامقة قريبة من لون ملابسه أو خلفيته ولون تمييز يبان عليها، واكتبها في theme.json (bg · ink · acc · clay · mut) بدون ما تسأله")
    if th_a.get("handle"): th0["handle"] = th_a["handle"]
    if (a.get("cap") or {}).get("font"): th0["font"] = a["cap"]["font"]
    th0.setdefault("grade", False); th0.setdefault("badgeUntil", 0); wj(tp0, th0)
    todo.append('حركات الأرقام: أي نسبة أو مقارنة أو مسافة بكلامه لها حركة جاهزة (layer add type=viz kind=pctdots|people|fill|bars|route …). شوف جدول «الحركات» في SKILL.md. موقع يذكره؟ hs shot <work> <الرابط> --at <ث>. موضوع تاريخي أو مكان؟ hs media <work> search "…" --video')
    cd = a.get("cards") or "some"; tot_ = float((rj(J(work, "caps.json"), {}) or {}).get("total") or 30)
    if cd == "none": todo.append("كروت الشرح: ما يبيها. لا تضف أي كرت شاشة مقسومة")
    else:
        n_ = cards_hint(tot_, cd)
        todo.append("كروت الشرح (%s): حط تقريباً %d كرت بهذا المقطع، ونوّع أشكالها ولا تكرر نفس الشكل مرتين ورا بعض. لكل فكرة اختر الشكل اللي يشرحها: خطوات ← style=steps · مراحل تتحول ← flow · مقارنة ← versus · رقم ← stat · صح وغلط ← check · تواريخ ← timeline · تناقص ← funnel · جملة قوية ← quote · علاقة أو فكرة مركّبة ← style=draw ترسمها أنت بعناصر (دوائر، صناديق، أسهم، أيقونات، أرقام تعد). الأمر: python hs.py layer <work> add type=split style=<الشكل> title=\"…\" \"text=سطر\\nسطر\" s=<بداية الجملة> e=<نهايتها>. التفاصيل والأمثلة في SKILL.md قسم «كروت الشرح». لا تحطها على الهوك، ومدة الكرت = مدة الكلام عنه" % ({"few": "قليل", "some": "متوسط", "many": "كثير"}.get(cd, cd), n_))
    hs.setdefault("en", {})["on"] = bool(a.get("en"))
    if a.get("en"): todo.append("اكتب الترجمة الإنجليزية: tr export ثم tr import")
    hk = a.get("hook") or {}
    if hk.get("use"):
        items = [{"text": x} for x in ([hk.get("text")] if hk.get("text") else []) + [v for v in (hk.get("variants") or []) if v and v != hk.get("text")]][:3]
        if items: hs["hooks"] = {**{"dur": 2.6, "style": "box"}, **(hs.get("hooks") or {}), "on": True, "active": 0, "items": items}; done.append("الهوك (%d صيغة)" % len(items))
        else: todo.append("اكتب 3 صيغ هوك من أقوى سطر: hook set")
    elif "hooks" in hs: hs["hooks"]["on"] = False
    ch = a.get("char") or {}; Ls = [l for l in hs.get("layers") or [] if l.get("auto") != "char"]
    if ch.get("use") and ch["use"] != "none":
        total = (rj(J(work, "caps.json"), {}) or {}).get("total", 30); right = ch.get("side") == "right"
        L = {"id": new_id(Ls), "type": "char", "auto": "char", "s": 0, "e": total, "track": 0, "x": 0.8 if right else 0.2, "y": 0.62, "size": 0.26, "anim": "pop", "react": True, "flip": right}
        if ch.get("src"): L["src"] = ch["src"]
        else: L["char"] = ch["use"]; L["color"] = ch.get("color") or "#8F73F5"
        Ls.append(L); done.append("الشخصية: " + str(ch.get("src") or ch["use"]))
    hs["layers"] = Ls
    fx = a.get("fx") or {}; mix = hs.setdefault("mix", {}); stl_ = a.get("style") or "normal"
    if fx.get("sfx") == "none":
        spx = J(work, "sfx.json"); sx = rj(spx, {"outro": 0}) or {"outro": 0}; wj(spx, {"outro": sx.get("outro", 0)}); done.append("بلا مؤثرات صوتية")
    elif fx.get("sfx") == "light": todo.append("مؤثرات صوتية خفيفة: 6 أحداث بالدقيقة بالكثير، من مكتبة الأصوات (hs sfx <work> list ثم hs sfx <work> add <id> <ثانية>)")
    elif fx.get("sfx") == "rich": todo.append("مؤثرات صوتية أكثر: لين 15 حدث بالدقيقة عند اللحظات اللي لها معنى، من مكتبة الأصوات (hs sfx <work> list ثم hs sfx <work> add <id> <ثانية>)")
    wj(sp, st)
    if a.get("pace"):
        tp = J(work, "theme.json"); th = rj(tp, {}) or {}
        if a["pace"] == "calm": th["pace"] = "calm"
        else: th.pop("pace", None)
        wj(tp, th); todo.append({"calm": "إيقاع هادي: مشاهد أقل وزوم أخف", "normal": "إيقاع عادي: تغيير بصري كل 2-3 ثواني", "fast": "إيقاع سريع: تغيير بصري كل 1.5-2 ثانية"}.get(a["pace"], ""))
    if fx.get("zoom") and stl_ not in ("dahih", "podcast"):
        nz = auto_layers(work, "zooms", True) if (rj(J(work, "caps.json"), {}) or {}).get("cards") else 0
        if nz: done.append("زووم عند الكلمات المميّزة (%d)" % nz)
        else: todo.append("بعد ما يجهز الفيديو: python hs.py auto <work> zooms")
    if fx.get("transitions") and stl_ not in ("dahih", "podcast"): todo.append("بعد القص: python hs.py auto <work> transitions")
    src_ = fx.get("src") if fx.get("src") in {p["id"] for p in sound_providers()} else None
    if src_ and fx.get("sfx") != "none":   # 4.19: اختار يجيب الأصوات من حسابه
        todo.append("الأصوات من %s من حسابه (وافق إنها تصرف من رصيده): المكتبة وأصواته أول، وولّد بس اللحظات اللي ما لها صوت مناسب. احفظ كل صوت بـ <work>/assets/sfx/ ثم hs sfx <work> import <الملف> --name \"…\" --note \"متى ينستخدم\" --gen %s --prompt \"الوصف\" وبعدها hs sfx <work> add <id> <ثانية>. قل له كم صوت بتولّد قبل ما تبدأ" % (sound_name(src_), src_))
    if fx.get("bg"): todo.append("يبي صوت بالخلفية: اطلب منه ملف bg-audio.mp3 أو اسأله من وين" + ((" أو ولّدها من %s لو وافق (موسيقى بدون كلام، بطول المقطع)" % sound_name(src_)) if src_ and "music" in next((p["can"] for p in sound_providers() if p["id"] == src_), []) else ""))
    c = a.get("cut") or {}; cmd = []
    if c.get("drop"):
        cmd += ["--cards"] + [str(i + 1) for i in c["drop"]]; cc_ = (rj(J(work, "caps.json"), {"cards": []}) or {"cards": []})["cards"]
        bk = brief_marks(work); bk["drop"] = [card_key(cc_[i]) for i in c["drop"] if 0 <= i < len(cc_)]; wj(brief_marks_path(work), bk)
    if c.get("fillers"): cmd += ["--fillers"]
    if cmd: todo.append("القص المطلوب (نفّذه قبل تصميم المشاهد وبعد ما يجهز cutz.mp4): python hs.py remove <work> " + " ".join(cmd))
    if c.get("dupes"): todo.append("شيل الجمل المعادة: python hs.py check <work> ثم remove --cards للأولى من كل زوج")
    ln = a.get("length")
    if ln and ln != "keep": todo.append({"tight": "شدّ المقطع: شيل أي جملة ما تخدم الفكرة", "max30": "المدة 30 ثانية بالكثير: اختر أقوى الجمل واعرضها عليه قبل القص", "max60": "المدة 60 ثانية بالكثير"}.get(ln, ln))
    m = a.get("media") or {}
    if m.get("mode") and m["mode"] != "none":
        t = "، ".join(m.get("topics") or []) or "استخرجها من الكلام"; n = {"few": "2-3", "some": "4-6", "many": "7-10"}.get(m.get("amount"), "4-6")
        if m["mode"] in ("search", "mix"): todo.append("صور حقيقية (%s صور) عن: %s ← python hs.py media <work> search \"…\" ثم media add <رقم> --at <وقت الجملة>" % (n, t))
        if m["mode"] in ("ai", "mix"): todo.append("صور مولّدة (%s) عن: %s ← لكل وحدة: python hs.py gen <work> request image \"وصف بالإنجليزي\" --at <وقت>%s. التوليد من حسابه الشخصي بلا مفاتيح API: افتح ChatGPT (صور) أو Gemini (مقاطع) بمتصفحه، ولّد ونزّل، ثم gen import <رقم> <ملف>. لو ما عندك متصفحه استخدم موصل التوليد المربوط بحسابه، وإلا خلّ الطلبات تنتظره بالاستوديو وقل له" % (n, t, " · ومقاطع: gen request video" if m.get("video") else ""))
        if m["mode"] == "mine": todo.append("هو بيرفع صوره ومقاطعه من «الملفات»: لا تضف صوراً من عندك")
    o = a.get("outro") or {}
    if o.get("use"):
        st = load_studio(work); ot = st.setdefault("outro", {}); txt = (o.get("text") or "").strip(); ws = txt.split()
        if len(ws) >= 2: ot["cta"], ot["word"] = " ".join(ws[:-1]), ws[-1]
        elif txt: ot["cta"] = txt
        wj(J(work, "studio.json"), st)
        if o.get("handle"):
            tpx = J(work, "theme.json"); thx = rj(tpx, {}) or {}; thx["handle"] = o["handle"]; wj(tpx, thx)
        spx = J(work, "sfx.json"); sx = rj(spx, {"outro": 0}) or {"outro": 0}
        if not sx.get("outro"): sx["outro"] = 3.5; wj(spx, sx)
        done.append("كرت الختام" + ((": " + txt) if txt else "") + ((" · " + o["handle"]) if o.get("handle") else ""))
        if not txt: todo.append("كرت الختام: ما كتب دعوة. اكتب وحدة تناسب المقطع: hs set <work> outro.cta=\"…\" outro.word=\"…\"")
    else:
        spx = J(work, "sfx.json"); sx = rj(spx, {"outro": 0}) or {"outro": 0}
        if sx.get("outro"): sx["outro"] = 0; wj(spx, sx); done.append("بلا كرت ختام")
    goal = (a.get("goalText") or "").strip() if a.get("goal") == "other" else a.get("goal")
    if goal: todo.append("نوع المقطع: " + str(goal) + ((" (كتبه بنفسه: افهم منه الأسلوب المطلوب وامش عليه)") if a.get("goal") == "other" else ""))
    if ar != "9:16":
        todo.append({"4:5": "المقاس 4:5: التصدير يقص الكادر العمودي إلى 1080×1350. خل الوجه والنصوص والصور داخل الحزام بين %s%% و%s%% من الارتفاع (زر «مناطق الأمان» يوريه)" % tuple(sz["crop"] or (0, 100)),
                     "1:1": "المقاس مربع: التصدير يقص إلى 1080×1080. كل شي مهم داخل الحزام بين %s%% و%s%% من الارتفاع، والمشاهد اللي تملأ الشاشة طولياً بتنقص" % tuple(sz["crop"] or (0, 100)),
                     "16:9": "المقاس عرضي 16:9: المحرّك يركّب عمودي، فالتصدير يحط المقطع بالنص وخلفية مغبّشة منه. قل له هذا بوضوح، ولو يبي عرضي حقيقي يملأ الشاشة يحتاج مونتاج عرضي من المصدر"}[ar])
    for k, v in (a.get("extra") or {}).items(): todo.append("إجابة «%s»: %s" % (k, v))
    stl = a.get("style") or "normal"
    if stl == "paper": todo.append("الأسلوب: ورق متحرك. اقرأ <engine>/references/styles.md (القسم 1) ثم: hs kinetic <work> auto --deco both، وراجع كل شاشة بنفسك")
    elif stl == "podcast":
        st2 = load_studio(work); h2 = hs_of(st2); P = h2.setdefault("pod", {})
        if not P.get("on"):
            P.update({"on": True, "title": P.get("title") or ((a.get("hook") or {}).get("text") or "").strip()[:60], "lang": P.get("lang") or "ar", "orig": True})
            h2["cap"] = {**(h2.get("cap") or {}), **POD_CAP}; h2["hooks"] = {**(h2.get("hooks") or {}), "on": False}; wj(J(work, "studio.json"), st2)
        done.append("أسلوب البودكاست المترجم")
        todo.append("بودكاست مترجم: اقرأ <engine>/references/clips.md. العنوان فوق (pod.title) والمصدر (pod.credit)، والترجمة لكل جملة: hs tr <work> export ثم import. لا موشن ولا مؤثرات ولا زووم، وكروت الشرح بس لو اختارها")
    elif stl == "dahih" and not (hs_of(load_studio(work)).get("dahih") or {}).get("on"):
        ttl = ((a.get("hook") or {}).get("text") or "").strip()[:40]
        try: cmd_dahih(work, ["on"] + (["--title", ttl] if ttl else [])); done.append("أسلوب الدحيح شغّال")
        except SystemExit: pass
        todo.append("الأسلوب: الدحيح شغّال. اقرأ <engine>/references/styles.md (القسم 2)، عدّل العنوان والهاشتاق، وحط كروت المكتب على كلامه وبدّل الخلفيات مع تغيّر الفكرة")
    elif stl == "dahih": todo.append("الأسلوب: الدحيح. اقرأ <engine>/references/styles.md (القسم 2) ثم: hs dahih <work> on --title \"…\" --tag \"…\"، وحط كروت المكتب على كلامه")
    elif stl == "motion":   # 4.37: الموشن جرافيك أساسي
        st3 = load_studio(work); hs_of(st3)["wantStyle"] = "motion"; wj(J(work, "studio.json"), st3); done.append("أسلوب موشن جرافيك")
        todo.append("الأسلوب: موشن جرافيك (أساسي، مو زينة). اقرأ <engine>/references/motion-graphics.md كامل، اختر القالب من جدول التوجيه (قسم 3، ومقاطع حسابه MG-05 متكلم + إدخالات)، عبّ متغيراته من هويته وكلامه، وابنِ بالطبقات حسب «البناء بـ hs». افحص بقائمة قسم 6، وبعدها: hs brief <work> ok mg \"MG-xx: وش بنيت\"")
    if a.get("ref"): todo.append("مرجع يبي مثله: " + a["ref"])
    if a.get("notes"): todo.append("ملاحظاته الحرّة: " + a["notes"])
    if th_a.get("mode") == "identity":   # 4.37: الهوية آخر شي عشان ما يغطيها شكل الكابشن أو البودكاست
        try: done += ident_apply(work, th_a.get("identity")); t_ = ident_task(ident_get(th_a.get("identity")))
        except Exception as e: done.append("الهوية ما انطبقت: " + str(e)[:80]); t_ = ""
        if t_: todo.insert(0, t_)
        todo.append("هويته: اقرأ %s قبل ما تصمم أي شي (الألوان والخطوط والموشن والدعوة منها)" % (ident_get(th_a.get("identity")) or {}).get("md", "identity.md"))
    nw = style_apply(work)
    if nw: done.append("تصحيحات كلمات تعلّمتها منه: %d" % nw)
    print("انطبق تلقائياً: " + ("، ".join(done) or "لا شي")); print("\nمهامك من إجاباته:")
    for x in todo:
        if x: print("  □ " + x)
    if plats:
        print("\nوش تحتاج منصاته (التزم فيها بالمونتاج، ولو تعارضت منصتين امش على الأشد):"); print(platform_text(plats))
        if len(plats) > 1: print("  ← الكابشن والنصوص لازم تكون بين %s%% و%s%% من الارتفاع عشان تسلم في كل المنصات المختارة." % (sz["capMin"], sz["capMax"]))
        short = [n for n in plats if n == "x"]; tot = (rj(J(work, "caps.json"), {}) or {}).get("total", 0)
        if short and tot > 140: print("  ← تنبيه: المقطع %d ثانية وإكس يقبل 140 للحساب العادي. اسأله: حسابه مشترك؟ وإلا اقترح نسخة أقصر." % tot)
    if style_prof().get("n"): print("\nأسلوبه من تعديلاته السابقة (إجاباته الحين تتقدّم عليه لو تعارضت):"); print(style_text())
    print("\nقائمة التحقق من إجاباته (ما تسلّم لين تطلع كلها ✓):"); brief_print(work)
    print("\nبعد ما تخلص كل شي: python hs.py brief <work> check  ← لازم يطلع «كل إجاباته مطبّقة». البنود اللي ما تنفحص لحالها: brief <work> ok <رمز> \"وش سويت\"")
    say(work, "قرأت إجاباتك وبدأت المونتاج عليها.", "step")

def brief_marks_path(work): return J(work, ".hs", "brief_marks.json")
def brief_marks(work): return rj(brief_marks_path(work), {}) or {}
def brief_reqs(work):
    """كل إجابة بصفحة الأسئلة تصير بند: ok=True/False يتفحص من ملفات المشروع، وman=True لو يحتاج Claude يأكّد وش سوّى."""
    a = rj(brief_paths(work)[1])
    if not a: return []
    st = load_studio(work); hs = hs_of(st); caps = rj(J(work, "caps.json"), {"cards": [], "total": 0}) or {"cards": [], "total": 0}; cards = caps.get("cards") or []
    total = float(caps.get("total") or 0); th = rj(J(work, "theme.json"), {}) or {}; sx = rj(J(work, "sfx.json"), {"outro": 0}) or {"outro": 0}
    Ls = [L for L in hs.get("layers") or [] if not L.get("off")]; mk = brief_marks(work); man_ok = mk.get("ok") or {}; R = []
    def req(k, label, ok=None, why="", man=False):
        if man: ok = k in man_ok; why = man_ok.get(k) or why
        R.append({"k": k, "label": label, "ok": bool(ok), "man": man, "why": why})
    ar = a.get("frame") if a.get("frame") in FRAMES else "9:16"; req("frame", "المقاس " + ar, frame_of(hs)[0] == ar)
    if a.get("cap"):
        cp = hs.get("cap") or {}; ign_ = ("y", "font", "active") if ident_get(hs.get("identity")) else ("y",)   # 4.37: الهوية تغيّر الخط ولون الكلمة
        if cp.get("font") == CAP_BRAND: ign_ += ("font", "weight")   # خط الهوية الخاص (ثمانية) يضبط الوزن على أوزانه
        diff = [k for k, v in a["cap"].items() if k not in ign_ and cp.get(k) != v]
        req("cap", "الكابشن بالإعدادات اللي اختارها", cp.get("on", True) and not diff, ("تغيّر: " + "، ".join(diff)) if diff else "")
    plats = [x for x in (a.get("platform") or []) if x in PLATFORMS]
    if plats:
        sz = safe_of(plats, ar, frame_of(hs)[1]); cy = float((hs.get("cap") or {}).get("y", 76))
        req("safe", "الكابشن داخل منطقة الأمان لـ " + "، ".join(plats), sz["capMin"] <= cy <= sz["capMax"], "الكابشن على %s%% والمسموح %s-%s" % (cy, sz["capMin"], sz["capMax"]))
    ta = a.get("theme") or {}
    if ta.get("mode") in ("mono", "custom"): req("colors", "الألوان اللي اختارها", (ta.get("mode") == "mono" and th.get("bg") == "#0E0E10") or (ta.get("mode") == "custom" and th.get("acc") == (ta.get("acc") or "#F2B33D")))
    elif ta.get("mode") == "identity":   # 4.37
        I_ = ident_get(ta.get("identity")); req("colors", "ألوان هويته «%s»" % ((I_ or {}).get("name") or ta.get("identity")), bool(I_) and th.get("acc") == I_["colors"]["acc"] and hs.get("identity") == I_["slug"], "" if I_ else "الهوية انحذفت")
        req("idmd", "ملف الهوية كامل (identity.md)", bool(I_) and not I_.get("draft"), "لسه مسودة: اكتبه ثم hs identity check " + str(ta.get("identity")))
    else: req("colors", "ألوان مختارة من المقطع (قال اختر لي)", man=True, why="اقرأ لقطة واكتب الألوان في theme.json")
    if ta.get("handle") or (a.get("outro") or {}).get("handle"):
        hd = (a.get("outro") or {}).get("handle") or ta.get("handle"); req("handle", "الحساب " + hd, th.get("handle") == hd)
    cd = a.get("cards") or "some"; want = cards_hint(total, cd)
    have = sum(1 for L in Ls if L.get("type") in ("split", "pip") or (L.get("type") == "viz" and L.get("kind") in ("card", "draw")) or L.get("type") in ("desk", "kinetic"))
    if cd == "none": req("cards", "بلا كروت شرح", not any(L.get("type") in ("split", "pip") for L in Ls))
    elif cards: req("cards", "كروت الشرح: تقريباً %d" % want, max(1, want // 2) <= have <= max(want * 2, want + 2), "الحين %d" % have)
    if a.get("en"):
        mp = (hs.get("en") or {}).get("map") or {}; miss = sum(1 for c in cards if not mp.get(card_key(c)))
        req("en", "ترجمة إنجليزية لكل الجمل", (hs.get("en") or {}).get("on") and not miss, "ناقص %d جملة" % miss if miss else "")
    hk = a.get("hook") or {}
    if hk.get("use"): req("hook", "هوك بأول المقطع", (hs.get("hooks") or {}).get("on") and (hs.get("hooks") or {}).get("items"))
    ch = a.get("char") or {}
    if ch.get("use") and ch["use"] != "none": req("char", "الشخصية الكرتونية", any(L.get("type") == "char" for L in Ls))
    fx = a.get("fx") or {}; ev = sum(len(v) for k, v in sx.items() if isinstance(v, list)); per_min = ev / max(total / 60.0, 0.25)
    if fx.get("sfx") == "none": req("sfx", "بلا مؤثرات صوتية", ev == 0, "فيه %d مؤثر" % ev)
    elif fx.get("sfx") == "light": req("sfx", "مؤثرات صوتية خفيفة (6 بالدقيقة بالكثير)", 1 <= ev and per_min <= 6.5, "الحين %d (%.0f بالدقيقة)" % (ev, per_min))
    elif fx.get("sfx") == "rich": req("sfx", "مؤثرات صوتية أكثر", per_min > 6, "الحين %d (%.0f بالدقيقة)" % (ev, per_min))
    stl = a.get("style") or "normal"
    if fx.get("zoom") and stl not in ("dahih", "podcast"): req("zoom", "زووم عند الكلمات المهمة", any(L.get("type") == "fx" and L.get("fx") == "punch" for L in Ls))
    if fx.get("transitions") and stl not in ("dahih", "podcast"): req("tr", "انتقالات عند تغيّر الفكرة", any(L.get("type") == "fx" and L.get("fx") not in ("punch", "shake", "flash") for L in Ls))
    if fx.get("bg"): req("bgm", "صوت بالخلفية", any(os.path.exists(J(work, f)) for f in ("bg-audio.mp3", "bg-audio.m4a", "bg-audio.wav")) or bool((hs.get("mix") or {}).get("bg")), man=False)
    c = a.get("cut") or {}
    if c.get("fillers") or c.get("dupes"):
        ck = check(work) if cards else {"fillers": [], "dupes": []}
        if c.get("fillers"): req("fillers", "شيل الحشو (اممم، يعني…)", not ck["fillers"], "باقي %d" % len(ck["fillers"]))
        if c.get("dupes"): req("dupes", "شيل الجمل المعادة", not ck["dupes"], "باقي %d زوج" % len(ck["dupes"]))
    if c.get("drop"):
        left = [k for k in (mk.get("drop") or []) if k in set(card_key(x) for x in cards)]
        req("drop", "شيل الجمل اللي حددها (%d)" % len(c["drop"]), not left, ("باقي: " + " · ".join(x[:24] for x in left)) if left else "")
    ln = a.get("length")
    if ln in ("max30", "max60"): lim = 30 if ln == "max30" else 60; req("length", "المدة %d ثانية بالكثير" % lim, total <= lim + 1.5, "الحين %.0f ث" % total)
    elif ln == "tight": req("length", "شدّ المقطع (شيل اللي ما يخدم الفكرة)", man=True)
    m = a.get("media") or {}
    if m.get("mode") and m["mode"] != "none":
        if m["mode"] == "mine": req("media", "صوره هو بس (لا تضف من عندك)", man=True)
        else:
            lo = {"few": 2, "some": 4, "many": 7}.get(m.get("amount"), 4); nimg = sum(1 for L in Ls if L.get("type") in ("image", "bg", "behind") and L.get("src") not in (None, "", "video", "clock"))
            req("media", "صور (%d على الأقل)" % lo, nimg >= lo, "الحين %d" % nimg)
    o = a.get("outro") or {}
    if o.get("use"):
        ot = st.get("outro") or {}; txt = (o.get("text") or "").strip(); have_t = (" ".join([ot.get("cta") or "", ot.get("word") or ""])).strip()
        req("outro", "كرت الختام" + ((": " + txt) if txt else ""), float(sx.get("outro") or 0) > 0 and (not txt or _norm(txt) == _norm(have_t) or _norm(txt) in _norm(have_t)), "" if float(sx.get("outro") or 0) > 0 else "مدة كرت الختام صفر")
    else: req("outro", "بلا كرت ختام", not float(sx.get("outro") or 0))
    if stl == "podcast":
        P = hs.get("pod") or {}; mp = (hs.get("en") or {}).get("map") or {}; miss = sum(1 for c in cards if not mp.get(card_key(c)))
        req("style", "بودكاست مترجم: عنوان وترجمة لكل جملة", P.get("on") and P.get("title") and not miss, ("ناقص ترجمة %d جملة" % miss) if miss else ("" if P.get("title") else "ما فيه عنوان"))
    elif stl == "paper": req("style", "أسلوب الورق المتحرك", any(L.get("type") == "kinetic" for L in Ls))
    elif stl == "motion":   # 4.37
        nmg = sum(1 for L in Ls if L.get("type") in ("mg", "viz", "split", "kinetic", "behind", "cover", "anno", "collage", "draw", "desk", "mark", "cursor")); want_ = max(2, int(total // 8))
        req("mgn", "موشن جرافيك: %d عناصر موشن على الأقل" % want_, nmg >= want_, "الحين %d" % nmg)
        req("mg", "قالب الموشن من motion-graphics.md", man=True, why='hs brief <work> ok mg "MG-xx: …"')
    elif stl == "dahih": req("style", "أسلوب الدحيح مع كروت مكتب", (hs.get("dahih") or {}).get("on") and any(L.get("type") == "desk" for L in Ls), "" if (hs.get("dahih") or {}).get("on") else "الأسلوب مو شغّال")
    goal = (a.get("goalText") or "").strip() if a.get("goal") == "other" else a.get("goal")
    if goal: req("goal", "نوع المقطع: " + str(goal), man=True)
    if a.get("ref"): req("ref", "على نفس المرجع: " + a["ref"][:60], man=True)
    if a.get("notes"): req("notes", "ملاحظاته: " + a["notes"][:80], man=True)
    for i, (k, v) in enumerate((a.get("extra") or {}).items()): req("x%d" % (i + 1), "«%s»: %s" % (str(k)[:40], str(v)[:60]), man=True)
    return R
def brief_print(work):
    R = brief_reqs(work)
    for r in R: print("  %s %-8s %s%s" % ("✓" if r["ok"] else "□", r["k"], r["label"], ("  ← " + r["why"]) if r["why"] and (not r["ok"] or r["man"]) else ""))
    return R
# ───────────────────────── صور حقيقية برخص حرّة (ويكيميديا كومنز) ─────────────────────────
CAP_STYLE_KEYS = ("bg", "bgColor", "bgOpacity", "stroke", "strokeColor", "shadow", "shadowColor", "hl", "chunk", "actScale", "fill", "mode", "enter", "exit", "lines")
MEDIA_UA = {"User-Agent": "hojas-studio/%s (image search for video b-roll)" % VERSION}
LIC_OK = ("Public domain", "CC0", "CC BY 2.0", "CC BY 2.5", "CC BY 3.0", "CC BY 4.0", "CC BY-SA", "PDM", "No restrictions")
def http_json(url, data=None, headers=None, timeout=60, method=None):
    req = urllib.request.Request(url, data=(json.dumps(data).encode() if data is not None else None), headers={**({"Content-Type": "application/json"} if data is not None else {}), **(headers or {})}, method=method)
    with urllib.request.urlopen(req, timeout=timeout) as r: return json.loads(r.read().decode("utf-8", "replace"))
def video_search(work, q, n=10):
    """مقاطع حقيقية برخص حرّة من ويكيميديا كومنز (أرشيف تاريخي، أخبار، أماكن، علوم). بلا مفتاح."""
    base = os.environ.get("HS_COMMONS_API", "https://commons.wikimedia.org/w/api.php")
    p = {"action": "query", "format": "json", "generator": "search", "gsrsearch": q + " filetype:video", "gsrnamespace": 6, "gsrlimit": max(n * 3, 20), "prop": "videoinfo", "viprop": "url|size|mime|extmetadata|derivatives", "viurlwidth": 480}
    d = http_json(base + "?" + urllib.parse.urlencode(p), headers=MEDIA_UA); res = []
    if not any(pg.get("videoinfo") for pg in (d.get("query", {}).get("pages") or {}).values()):      # خادم ما يدعم videoinfo ← نفس البيانات من imageinfo
        p2 = {**{k: x for k, x in p.items() if not k.startswith("vi")}, "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata", "iiurlwidth": 480}
        d = http_json(base + "?" + urllib.parse.urlencode(p2), headers=MEDIA_UA)
    for pg in sorted((d.get("query", {}).get("pages") or {}).values(), key=lambda x: x.get("index", 0)):
        vi = (pg.get("videoinfo") or pg.get("imageinfo") or [{}])[0]; em = vi.get("extmetadata") or {}; lic = (em.get("LicenseShortName") or {}).get("value", ""); dur = float(vi.get("duration") or 0)
        if not str(vi.get("mime", "")).startswith("video/") or dur < 2 or vi.get("width", 0) < 320: continue
        if not any(lic.startswith(k) for k in LIC_OK): continue
        ders = [x for x in (vi.get("derivatives") or []) if str(x.get("type", "")).startswith("video/") and x.get("src") and x.get("height")]
        good = sorted([x for x in ders if 360 <= int(x["height"]) <= 1080], key=lambda x: abs(int(x["height"]) - 720))
        url = (good[0]["src"] if good else vi.get("url"))
        res.append({"kind": "video", "title": re.sub(r"^File:|\.\w+$", "", pg.get("title", "")), "thumb": vi.get("thumburl") or "", "url": url, "page": vi.get("descriptionurl", ""), "w": vi.get("width"), "h": vi.get("height"), "dur": round(dur, 1),
                    "lic": lic, "author": re.sub(r"<[^>]+>", "", (em.get("Artist") or {}).get("value", ""))[:80]})
        if len(res) >= n: break
    wj(J(work, ".hs", "media_last.json"), {"q": q, "items": res}); return res
def video_add(work, item, at=None, dur=4.0, start=None, fit=None, log=None):
    """ينزّل المقطع، يقص منه المدة المطلوبة، ويحوّله لقطة بي-رول عمودية على التايم لاين."""
    log = log or (lambda *_: None); os.makedirs(J(work, "broll_src"), exist_ok=True); os.makedirs(J(work, "broll"), exist_ok=True)
    key = "v" + time.strftime("%H%M%S") + secrets.token_hex(2); ext = os.path.splitext(urllib.parse.urlparse(item["url"]).path)[1].lower() or ".webm"; src = J(work, "broll_src", key + ext)
    with urllib.request.urlopen(urllib.request.Request(item["url"], headers=MEDIA_UA), timeout=180) as r, open(src, "wb") as f: shutil.copyfileobj(r, f)
    if os.path.getsize(src) < 20000: raise RuntimeError("المقطع ما نزل")
    total = float(item.get("dur") or 0); dur = max(1.0, min(float(dur or 4), 8.0)); st = float(start) if start not in (None, "") else (max(0.0, min(total * 0.25, total - dur)) if total else 0.0)
    wide = (item.get("w") or 16) > (item.get("h") or 9) * 1.05; mode = fit or ("fit" if wide else "crop")
    vf = ("fps=30,split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=28:4,eq=brightness=-0.18[bg];[b]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2" if mode == "fit"
          else "fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920")
    run(["ffmpeg", "-v", "error", "-ss", "%.2f" % st, "-t", "%.2f" % dur, "-i", src] + (["-filter_complex", vf] if mode == "fit" else ["-vf", vf]) + ["-q:v", "3", "-y", J(work, "broll", key + "_%04d.jpg")], log)
    n = len([f for f in os.listdir(J(work, "broll")) if f.startswith(key + "_")])
    if not n: raise RuntimeError("ما قدرت أقرأ المقطع")
    stu = load_studio(work); stu.setdefault("brNeed", {})[key] = [1, n]; wj(J(work, "studio.json"), stu); add_broll_clip(work, key, at, n / 30.0)
    cp = J(work, "assets", "credits.json"); os.makedirs(J(work, "assets"), exist_ok=True); cr = rj(cp, []) or []; cr.append({"file": "broll_src/" + key + ext, "title": item.get("title"), "author": item.get("author"), "license": item.get("lic"), "source": item.get("page")}); wj(cp, cr)
    return key, n
def shot_add(work, url, at=None, dur=4.0, full=True, w=0.84, log=None):
    """لقطة لصفحة موقع ← صورة بإطار متصفح على التايم لاين (تتحرك لتحت لو الصفحة طويلة)."""
    log = log or print; eng = find_engine(None) or sys.exit("ما لقيت مجلد engine"); os.makedirs(J(work, "assets"), exist_ok=True)
    if not re.match(r"^https?://", url): url = "https://" + url
    name = "shot-%s.png" % time.strftime("%H%M%S"); out = J(work, "assets", name)
    run(["node", os.path.join(eng, "scripts", "20_shot.js"), url, out] + (["--full"] if full else []), log)
    if not os.path.exists(out): raise RuntimeError("اللقطة ما انحفظت")
    lid = add_image_layer(work, "assets/" + name, at, dur, "free", {"frame": "browser", "url": urllib.parse.urlparse(url).netloc + urllib.parse.urlparse(url).path.rstrip("/"), "w": w, "y": 0.36, "ratio": 1.25, "anim": "rise"})
    return lid, name
def media_search(work, q, n=12):
    base = os.environ.get("HS_COMMONS_API", "https://commons.wikimedia.org/w/api.php")
    p = {"action": "query", "format": "json", "generator": "search", "gsrsearch": q + " filetype:bitmap", "gsrnamespace": 6, "gsrlimit": max(n * 3, 20), "prop": "imageinfo", "iiprop": "url|size|extmetadata|mime", "iiurlwidth": 1600}
    d = http_json(base + "?" + urllib.parse.urlencode(p), headers=MEDIA_UA); res = []
    pages = sorted((d.get("query", {}).get("pages") or {}).values(), key=lambda x: x.get("index", 0))
    for pg in pages:
        ii = (pg.get("imageinfo") or [{}])[0]; mime = ii.get("mime", ""); em = ii.get("extmetadata") or {}; lic = (em.get("LicenseShortName") or {}).get("value", "")
        if not mime.startswith("image/") or mime in ("image/svg+xml", "image/gif") or ii.get("width", 0) < 700: continue
        if not any(lic.startswith(k) for k in LIC_OK): continue
        res.append({"title": re.sub(r"^File:|\.\w+$", "", pg.get("title", "")), "thumb": ii.get("thumburl") or ii.get("url"), "url": ii.get("thumburl") or ii.get("url"), "page": ii.get("descriptionurl", ""),
                    "w": ii.get("width"), "h": ii.get("height"), "lic": lic, "author": re.sub(r"<[^>]+>", "", (em.get("Artist") or {}).get("value", ""))[:80]})
        if len(res) >= n: break
    wj(J(work, ".hs", "media_last.json"), {"q": q, "items": res}); return res
def add_image_layer(work, src, at=None, dur=3.0, fit="card", extra=None):
    st = load_studio(work); hs = hs_of(st); Ls = hs.setdefault("layers", []); total = (rj(J(work, "caps.json"), {}) or {}).get("total", 0) or 600
    s = max(0.0, min(float(at or 0), max(0, total - 0.5))); L = {"id": new_id(Ls), "type": "image", "src": src, "s": round(s, 3), "e": round(min(total, s + float(dur)), 3), "track": 0, "fit": fit, "kb": True, "anim": "fade", **({"move": "push", "hand": True, "inFx": "focus"} if fit == "cover" else {}), **(extra or {})}   # 4.15: الصورة ملء الشاشة ما تكون ثابتة
    Ls.append(L); wj(J(work, "studio.json"), st); return L["id"]
def media_add(work, item, at=None, dur=3.0, fit="card"):
    os.makedirs(J(work, "assets"), exist_ok=True); slug = re.sub(r"[^\w\-]+", "-", item.get("title", "image"))[:40].strip("-") or "image"
    name = slug + ".jpg"; n = 1
    while os.path.exists(J(work, "assets", name)): n += 1; name = "%s-%d.jpg" % (slug, n)
    raw = urllib.request.urlopen(urllib.request.Request(item["url"], headers=MEDIA_UA), timeout=120).read()
    if len(raw) < 2000: raise RuntimeError("الصورة ما نزلت")
    open(J(work, "assets", name), "wb").write(raw)
    cp = J(work, "assets", "credits.json"); cr = rj(cp, []) or []; cr.append({"file": name, "title": item.get("title"), "author": item.get("author"), "license": item.get("lic"), "source": item.get("page")}); wj(cp, cr)
    return add_image_layer(work, "assets/" + name, at, dur, fit), name

# ───────────────────────── توليد بالذكاء الاصطناعي من حساب المستخدم (بلا مفاتيح API) ─────────────────────────
# الطلب ينحفظ في gen.json. يتنفّذ بأحد ثلاث طرق، كلها بحسابه الشخصي: (1) Claude يفتح ChatGPT/Gemini في متصفحه وينزّل الناتج
# (2) موصل التوليد المربوط بحسابه في Claude  (3) هو نفسه يضغط «افتح» بالاستوديو ويرفع الملف. ثم gen_import يدخّله التايم لاين.
GEN_SITES = {"image": "https://chatgpt.com/", "video": "https://gemini.google.com/app"}
IMG_EXT = (".png", ".jpg", ".jpeg", ".webp"); VID_EXT = (".mp4", ".mov", ".webm", ".m4v")
def gen_list(work): return rj(J(work, "gen.json"), []) or []
def gen_request(work, kind, prompt, at=None, fit="card", by="user"):
    if kind not in ("image", "video"): raise RuntimeError("النوع: image أو video")
    q = gen_list(work); rid = max([int(x["id"]) for x in q] or [0]) + 1
    q.append({"id": rid, "kind": kind, "prompt": prompt.strip(), "at": (round(float(at), 2) if at is not None else None), "fit": fit or "card", "status": "pending", "by": by, "ts": int(time.time())})
    wj(J(work, "gen.json"), q); return rid
def gen_prompt(r, frame="9:16"):
    """النص اللي ينلصق في ChatGPT أو Gemini."""
    if r["kind"] == "image": return "Create an image: %s. Vertical 9:16 portrait, high detail, no text or watermark in the image." % r["prompt"]
    return "Generate a video: %s. Vertical 9:16, about 8 seconds, no text or captions in the video." % r["prompt"]
def gen_import(work, rid, src, name=None, at=None, fit=None, log=print):
    q = gen_list(work); r = next((x for x in q if str(x["id"]) == str(rid)), None) if rid not in (None, "", "-", "new") else None
    name = name or os.path.basename(src); ext = os.path.splitext(name)[1].lower(); at = at if at is not None else (r or {}).get("at"); fit = fit or (r or {}).get("fit") or "card"
    if re.match(r"https?://", str(src)):   # 4.9: رابط صورة أو مقطع من موقع التوليد مباشرة
        u = str(src); ext = os.path.splitext(urllib.parse.urlparse(u).path)[1].lower() or ".png"; ext = ext if ext in IMG_EXT + VID_EXT else ".png"
        tmp = J(work, ".hs", "dl-%s%s" % (time.strftime("%H%M%S"), ext)); os.makedirs(J(work, ".hs"), exist_ok=True)
        with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=90) as rr_, open(tmp, "wb") as f_: shutil.copyfileobj(rr_, f_)
        src = tmp; name = os.path.basename(tmp); ext = os.path.splitext(name)[1].lower()
    if not os.path.isfile(src) or os.path.getsize(src) < 1500: raise RuntimeError("ما لقيت الملف أو إنه فاضي: " + src)
    tag = "gen%s-%s" % (r["id"] if r else "", time.strftime("%H%M%S"))
    if ext in IMG_EXT:
        os.makedirs(J(work, "assets"), exist_ok=True); fn = tag + ext; shutil.copy(src, J(work, "assets", fn))
        lid = add_image_layer(work, "assets/" + fn, at, 3, fit); res = {"file": "assets/" + fn, "layer": lid}
    elif ext in VID_EXT:
        os.makedirs(J(work, "broll_src"), exist_ok=True); os.makedirs(J(work, "broll"), exist_ok=True); key = tag.replace("-", ""); dst = J(work, "broll_src", key + ext); shutil.copy(src, dst)
        run(["ffmpeg", "-v", "error", "-i", dst, "-vf", "fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920", "-q:v", "3", "-y", J(work, "broll", key + "_%04d.jpg")], log)
        n = len([f for f in os.listdir(J(work, "broll")) if f.startswith(key + "_")])
        if not n: raise RuntimeError("ما قدرت أقرأ المقطع")
        st = load_studio(work); st.setdefault("brNeed", {})[key] = [1, n]; wj(J(work, "studio.json"), st); add_broll_clip(work, key, at); res = {"file": "broll_src/" + key + ext, "clip": key, "frames": n}
    else: raise RuntimeError("صيغة غير مدعومة: صور png/jpg/webp أو مقاطع mp4/mov/webm")
    if r:
        q = gen_list(work)
        for x in q:
            if x["id"] == r["id"]: x.update(status="done", file=res["file"], doneAt=int(time.time()))
        wj(J(work, "gen.json"), q)
    return res
def gen_rm(work, rid): q = [x for x in gen_list(work) if str(x["id"]) != str(rid)]; wj(J(work, "gen.json"), q); return q
def add_broll_clip(work, key, at=None, dur=None):
    st = load_studio(work); n = (st.get("brNeed") or {}).get(key, [1, 90])[1]; total = (rj(J(work, "caps.json"), {}) or {}).get("total", 0) or 600
    s = max(0.0, min(float(at or 0), max(0, total - 0.5))); st.setdefault("brollClips", []).append({"k": key, "s": round(s, 3), "e": round(min(total, s + (float(dur) if dur else min(4, n / 30))), 3), "mode": "full"}); wj(J(work, "studio.json"), st)

# ───────────────────────── إضافات تلقائية: تقريب عند الكلمات المميّزة · انتقال عند القصات ─────────────────────────
def auto_layers(work, kind, on=True, opts=None):
    opts = opts or {}
    st = load_studio(work); hs = hs_of(st); Ls = [l for l in hs.get("layers") or [] if l.get("auto") != kind]; caps = rj(J(work, "caps.json"), {"cards": [], "total": 0}); total = caps.get("total", 0); n = 0
    if on and kind == "zooms":
        last = -9
        for c in caps["cards"]:
            for w in c["w"]:
                if w.get("hot") and w["s"] - last > 2.5 and w["s"] > 0.8 and not any(l.get("auto") == "zooms" and c["s"] <= l["s"] <= c["e"] for l in Ls):
                    Ls.append({"id": new_id(Ls), "type": "fx", "fx": "punch", "auto": "zooms", "s": round(max(0, w["s"] - 0.05), 3), "e": round(min(total, w["e"] + 0.55), 3), "amount": 0.5, "track": 2}); last = w["s"]; n += 1
    if on and kind == "transitions":
        typ = opts.get("type") or (hs.get("look") and (looks_all().get(hs["look"].get("name")) or {}).get("tr")) or "curve"; dr = opts.get("dir") or hs.get("trDir") or "right"
        cards = caps["cards"]; bounds = [c["s"] for i, c in enumerate(cards) if i == 0 or re.search(r"[.!?؟…]$", str(cards[i - 1]["w"][-1]["t"]).strip()) or c["s"] - cards[i - 1]["e"] > 0.45]
        seams = [sm for sm in keep_seams(work) if 0.6 < sm < total - 0.6]; pick = [sm for sm in seams if any(abs(sm - b) < 0.4 for b in bounds)] or seams[::3]; last = -9
        for sm in pick:   # الانتقال عند تغيّر الفكرة فقط، مو عند كل قصة. والقصات الباقية قطع مباشر
            if sm - last < 4: continue
            Ls.append({"id": new_id(Ls), "type": "fx", "fx": typ, "dir": dr, "auto": "transitions", "seam": round(sm, 3), "s": round(sm - 0.3, 3), "e": round(min(total, sm + 0.35), 3), "amount": 0.6, "track": 2}); n += 1; last = sm
    if on and kind == "beats":
        b = rj(J(work, "beats.json")) or sys.exit("شغّل أول: hs beat <work> <ملف الموسيقى>")
        if not b.get("rhythmic"): print("الموسيقى هادية: ما حطيت ضربات. امش على الجمل.")
        else:
            last = -9
            for t0 in b.get("strong") or []:
                if 0.3 < t0 < total - 0.3 and t0 - last >= 1.2: Ls.append({"id": new_id(Ls), "type": "fx", "fx": "punch", "auto": "beats", "s": round(t0 - 0.02, 3), "e": round(t0 + 0.28, 3), "amount": 0.45, "track": 2}); n += 1; last = t0
    hs["layers"] = Ls; wj(J(work, "studio.json"), st); return n

def cmd_brief(work, args):
    sub = args[0] if args else "show"
    def multi(name):
        if name not in args: return []
        i = args.index(name); j = i + 1
        while j < len(args) and not args[j].startswith("--"): j += 1
        return args[i + 1:j]
    if sub == "ask":
        extra = rj(multi("--file")[0]) if multi("--file") else None
        brief_ask(work, hooks=multi("--hooks"), topics=multi("--topics"), note=" ".join(multi("--note")), extra=extra)
        u = J(work, ".hs", "url.txt"); print("الأسئلة جاهزة للمستخدم." + ((" الرابط: " + open(u).read().split("\n")[0]) if os.path.exists(u) else " شغّل: hs.py open <work>"))
        print("انتظره: python hs.py brief <work> wait")
    elif sub == "wait":
        tmo = float((multi("--timeout") or ["540"])[0]); t0 = time.time()
        if brief_state(work) is None: sys.exit("ما فيه أسئلة مرسلة. ابدأ بـ: brief <work> ask")
        while brief_state(work) != "saved":
            if time.time() - t0 > tmo: print("لسه ما حفظ إجاباته. أعد تشغيل نفس الأمر وانتظره، ولا تبدأ المونتاج قبلها."); sys.exit(3)
            time.sleep(2)
        print("حفظ إجاباته:\n" + brief_text(work)); print("\nالخطوة الجاية: python hs.py brief <work> apply")
    elif sub == "show": print(brief_text(work))
    elif sub == "apply": brief_apply(work)
    elif sub == "check":
        R = brief_print(work); miss = [r for r in R if not r["ok"]]
        if not R: print("ما فيه إجابات محفوظة."); return
        if miss: print("\nباقي %d من %d. لا تسلّم قبلها." % (len(miss), len(R))); sys.exit(4)
        print("\nكل إجاباته مطبّقة (%d)." % len(R))
    elif sub in ("ok", "undo"):
        if len(args) < 2: sys.exit('brief <work> ok <رمز> "وش سويت"  ·  undo <رمز>')
        k = args[1]; R = {r["k"]: r for r in brief_reqs(work)}
        if k not in R: sys.exit("ما فيه بند بهالرمز. الرموز: " + " ".join(R))
        if sub == "ok" and not R[k]["man"]: sys.exit("هذا البند يتفحص لحاله من المشروع، طبّقه فعلاً: " + R[k]["label"] + ((" (" + R[k]["why"] + ")") if R[k]["why"] else ""))
        bk = brief_marks(work); okm = bk.setdefault("ok", {})
        if sub == "ok":
            why = " ".join(args[2:]).strip()
            if len(why) < 4: sys.exit("اكتب وش سويت بالضبط عشان يشوفه بالاستوديو")
            okm[k] = why[:300]
        else: okm.pop(k, None)
        wj(brief_marks_path(work), bk); print("تم:", k, "✓" if sub == "ok" else "□")
    else: sys.exit("brief: ask [--hooks …] [--topics …] [--note …] [--file q.json] | wait | show | apply | check | ok <رمز> \"…\" | undo <رمز>")
def cmd_media(work, args):
    sub = args[0] if args else ""
    def opt(name, d=None):
        if name in args: i = args.index(name); v = args[i + 1]; del args[i:i + 2]; return v
        return d
    if sub == "search":
        n = int(opt("--n", 8)); vid = "--video" in args
        if vid: args.remove("--video")
        q = " ".join(args[1:])
        if vid:
            try: res = video_search(work, q, n)
            except Exception as e: sys.exit("البحث فشل (تأكد من النت): " + str(e)[:200])
            for i, r in enumerate(res): print("%d  %s  [%s · %s]  %dx%d · %s ث" % (i + 1, r["title"][:60], r["lic"], r["author"][:30] or "—", r["w"], r["h"], r["dur"]))
            print("ما لقيت مقاطع برخصة حرّة. جرّب استعلاماً إنجليزياً أبسط، أو ولّد المقطع من حسابه." if not res else "\nأضف واحد: python hs.py media <work> add <رقم> --at <ثانية> [--dur 4] [--from <ثانية البداية داخل المقطع>]"); return
        try: res = media_search(work, q, n)
        except Exception as e: sys.exit("البحث فشل (تأكد من النت): " + str(e)[:200])
        for i, r in enumerate(res): print("%d  %s  [%s · %s]  %dx%d" % (i + 1, r["title"][:60], r["lic"], r["author"][:30] or "—", r["w"], r["h"]))
        print("ما لقيت صوراً برخصة حرّة. جرّب استعلاماً إنجليزياً أبسط." if not res else "\nأضف وحدة: python hs.py media <work> add <رقم> --at <ثانية> [--dur 3] [--fit card|cover]")
    elif sub == "add":
        at = opt("--at", 0); dur = opt("--dur", None); fit = opt("--fit", None); frm = opt("--from", None); last = rj(J(work, ".hs", "media_last.json"), {}) or {}
        try: item = last["items"][int(args[1]) - 1]
        except Exception: sys.exit("رقم غير موجود. شغّل media search أول.")
        if item.get("kind") == "video":
            key, n = video_add(work, item, at, dur or 4, frm, fit if fit in ("fit", "crop") else None, print); print("انضاف المقطع %s (%.1f ث) عند %s ث (الرخصة: %s)" % (key, n / 30.0, at, item["lic"])); return
        dur = dur or 3; fit = fit or "card"
        lid, name = media_add(work, item, at, dur, fit); print("انضافت %s كطبقة %s عند %s ث (الرخصة: %s)" % (name, lid, at, item["lic"]))
    else: sys.exit("media: search \"query\" [--n 8] | add <n> --at <t> [--dur 3] [--fit card|cover]")
# ───────────────────────── 4.9: شعار الشركة لما ينذكر اسمها ─────────────────────────
# الشعارات من Simple Icons (CC0، github.com/simple-icons/simple-icons) وتنزل على الجهاز أول مرة.
# شعار مو موجود هناك (OpenAI، Canva، Microsoft…)؟ يطلع حرف أول بدائرة، أو حط ملفه الرسمي: hs logo add <الاسم> <ملف|رابط>
LOGO_SLUG = {"Claude": "claude", "Claude Code": "claude", "Anthropic": "anthropic", "Haiku": "claude", "Sonnet": "claude", "Opus": "claude", "Fable": "claude", "Mythos": "claude",
             "Gemini": "googlegemini", "Google": "google", "Google Drive": "googledrive", "Drive": "googledrive", "Gmail": "gmail", "YouTube": "youtube", "TikTok": "tiktok",
             "Instagram": "instagram", "WhatsApp": "whatsapp", "Telegram": "telegram", "Meta": "meta", "Facebook": "facebook", "Snapchat": "snapchat", "Twitter": "x", "X": "x",
             "Apple": "apple", "iPhone": "apple", "iPad": "apple", "MacBook": "apple", "Samsung": "samsung", "Netflix": "netflix", "Tesla": "tesla", "Nvidia": "nvidia",
             "Grok": "x", "xAI": "x", "DeepSeek": "deepseek", "Perplexity": "perplexity", "Mistral": "mistralai", "Notion": "notion", "Figma": "figma", "GitHub": "github",
             "Cursor": "cursor", "Vercel": "vercel", "Supabase": "supabase", "Python": "python", "JavaScript": "javascript", "React": "react", "Zapier": "zapier",
             "Spotify": "spotify", "Discord": "discord", "Reddit": "reddit", "Shopify": "shopify", "Netlify": "netlify", "Replit": "replit", "Higgsfield": "", "Kling": "",
             "ChatGPT": "", "GPT": "", "OpenAI": "", "Codex": "", "Sora": "", "Canva": "", "Microsoft": "", "Copilot": "", "Amazon": "", "CapCut": "", "Slack": "", "LinkedIn": "",
             "Midjourney": "", "Runway": "", "ElevenLabs": "", "Excel": "", "PowerPoint": "", "Photoshop": "", "Premiere": "", "After Effects": "", "Final Cut": "", "Salla": "", "Zid": ""}
def logo_dir(): d = os.path.join(HOME_CFG, "logos"); os.makedirs(d, exist_ok=True); return d
def logo_key(name): return re.sub(r"[^a-z0-9]+", "", str(name).lower()) or "logo"
def logo_get(name):
    """مسار ملف الشعار على الجهاز (svg أبيض أو صورة حطها المستخدم)، أو None."""
    k = logo_key(name)
    for ext in (".svg", ".png", ".webp", ".jpg"):
        p = os.path.join(logo_dir(), k + ext)
        if os.path.isfile(p) and os.path.getsize(p) > 60: return p
    slug = LOGO_SLUG.get(name, logo_key(name))
    if not slug: return None
    for u in ("https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/%s.svg" % slug, "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/%s.svg" % slug):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=12) as r: svg = r.read().decode("utf-8", "replace")
            if "<svg" not in svg: continue
            svg = re.sub(r"<svg ", '<svg width="128" height="128" fill="#FFFFFF" ', svg, count=1)
            p = os.path.join(logo_dir(), k + ".svg"); open(p, "w", encoding="utf-8").write(svg); return p
        except Exception: continue
    return None
def logo_to_project(work, name):
    p = logo_get(name)
    if not p: return ""
    os.makedirs(J(work, "assets", "logos"), exist_ok=True); b = logo_key(name) + os.path.splitext(p)[1]; shutil.copy2(p, J(work, "assets", "logos", b)); return "assets/logos/" + b
_CMP = r"(أفضل|افضل|أحسن|احسن|أقوى|اقوى|أسرع|اسرع|أذكى|اذكى|أرخص|ارخص|أغلى|اغلى|أدق|ادق|أضعف|اضعف|أبطأ|ابطأ|أسهل|اسهل)"
def logos_plan(work, gap_same=25.0, gap_any=4.0, per_min=5):
    """يلقى أسماء الشركات بالكابشن (بعد كتابتها بالإنجليزي) ويخطط شارات الشعار، و«X أفضل من Y» تصير شارتين متقابلتين."""
    caps = rj(J(work, "caps.json"), {}) or {}; ws = [w for c in caps.get("cards") or [] for w in c["w"]]
    st = load_studio(work); Ls = [L for L in hs_of(st).get("layers") or [] if not L.get("off") and L.get("auto") != "logos"]   # الشارات القديمة تنشال وتنعاد
    busy = lambda a, b: any(L.get("type") in ("mg", "image", "split", "viz", "kinetic", "cover", "collage", "pip") and L["s"] < b and L["e"] > a for L in Ls)
    def nm(w):
        e = w.get("en") or (str(w["t"]).strip("؟?!.،, ") if re.fullmatch(r"[A-Za-z][A-Za-z0-9 .+\-]*", str(w["t"]).strip("؟?!.،, ")) else "")
        return e if e in LOGO_SLUG else ""
    plan, last = [], {}
    # 1) المقارنات أول: «X … أفضل من Y» (X قبلها بـ 12 كلمة و 7 ث بالكثير)
    for j, w in enumerate(ws):
        if not re.fullmatch(_CMP + r"[؟?!.،,]*", str(w["t"]).strip()): continue
        n2 = next(((nm(ws[k]), ws[k]) for k in range(j + 1, min(len(ws), j + 4)) if nm(ws[k])), None)
        if not n2: continue
        n1 = next((nm(ws[k]) for k in range(j - 1, max(-1, j - 13), -1) if nm(ws[k]) and nm(ws[k]) != n2[0] and w["s"] - ws[k]["s"] <= 7.0), "")
        if not n1: continue
        rel = " ".join(str(x["t"]).strip("؟?!.،,") for x in ws[j:j + 3] if not nm(x) and x["s"] < n2[1]["s"]) or "أفضل من"
        s0 = max(0.0, w["s"] - 0.35); e0 = max(s0 + 3.0, n2[1]["e"] + 1.6)
        if busy(s0, e0) or any(p["s"] < e0 + gap_any and p["e"] > s0 - gap_any for p in plan): continue
        plan.append({"name": n1, "name2": n2[0], "rel": rel, "s": round(s0, 3), "e": round(e0, 3)}); last[n1] = last[n2[0]] = s0
    # 2) الذكر العادي: أول ذكر لكل شركة له الأولوية، وبعدها لو رجع ينذكر بعد 25 ث. بين كل شارتين 4 ث، وبالكثير 5 بأي دقيقة
    seen, cands = set(), []
    for w in ws:
        n1 = nm(w)
        if n1: cands.append((w["s"], n1, n1 not in seen)); seen.add(n1)
    for first in (True, False):
        for t, n1, f in cands:
            if f != first or any(n1 in (p["name"], p.get("name2")) and abs(p["s"] - t) < gap_same for p in plan): continue
            s0 = round(max(0.0, t - 0.1), 3); e0 = round(s0 + 2.2, 3)
            if any(p["s"] < e0 + gap_any and p["e"] > s0 - gap_any for p in plan) or busy(s0, e0): continue
            if sum(1 for p in plan if t - 60 < p["s"] <= t) >= per_min or sum(1 for p in plan if t <= p["s"] < t + 60) >= per_min: continue
            plan.append({"name": n1, "s": s0, "e": e0})
    plan.sort(key=lambda p: p["s"])
    return plan
def logos_apply(work, dry=False):
    plan = logos_plan(work)
    if dry or not plan: return plan
    st = load_studio(work); hs = hs_of(st); Ls = hs.setdefault("layers", []); Ls[:] = [L for L in Ls if L.get("auto") != "logos"]
    for p in plan:
        L = {"id": new_id(Ls), "type": "mg", "kind": "logo", "auto": "logos", "s": p["s"], "e": p["e"], "track": 1, "name": p["name"], "src": logo_to_project(work, p["name"])}
        if p.get("name2"): L.update(name2=p["name2"], src2=logo_to_project(work, p["name2"]), rel=p["rel"])
        Ls.append(L)
    wj(J(work, "studio.json"), st); return plan
def cmd_logo(work, args):
    sub = args[0] if args else "plan"
    if sub in ("plan", "auto"):
        plan = logos_apply(work, dry=(sub == "plan"))
        for p in plan: print("%6.2f  %s%s" % (p["s"], p["name"], ("  %s  %s" % (p.get("rel"), p["name2"])) if p.get("name2") else ""))
        print(("انضافت %d شارة شعار" % len(plan)) if sub == "auto" else ("%d شارة مقترحة. طبّقها: hs logo <work> auto" % len(plan)) if plan else "ما لقيت أسماء شركات بالكابشن.")
    elif sub == "add":
        if len(args) < 3: sys.exit("logo add <الاسم بالإنجليزي> <ملف أو رابط>")
        name, src = args[1], args[2]; ext = os.path.splitext(urllib.parse.urlparse(src).path if src.startswith("http") else src)[1].lower() or ".png"
        dst = os.path.join(logo_dir(), logo_key(name) + ext)
        if src.startswith("http"):
            with urllib.request.urlopen(urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as r, open(dst, "wb") as f: shutil.copyfileobj(r, f)
        else: shutil.copy2(src, dst)
        print("انحفظ شعار %s: %s" % (name, dst))
    else: sys.exit("logo: plan | auto | add <الاسم> <ملف|رابط>")
def gen_moments(work, n=4, spacing=8.0):
    """4.9: أهم الجمل اللي تستاهل صورة تخيلية (فكرة مهمة، رقم، مقارنة، قصة)، بعيدة عن الطبقات الموجودة وعن بعض."""
    caps = rj(J(work, "caps.json"), {}) or {}; cm = cutmap_mod(); st = load_studio(work); Ls = hs_of(st).get("layers") or []
    busy = lambda a, b: any(L.get("type") in ("image", "split", "viz", "kinetic", "cover", "collage", "mg") and L["s"] < b and L["e"] > a for L in Ls)
    cands = []; ws = [w for c in caps.get("cards") or [] for w in c["w"]]
    for i, g in enumerate(capgroup_mod().breaths(ws, pause=0.6, max_words=18, max_dur=7.0)):   # جمل كاملة، مو كروت
        c = {"s": g[0]["s"], "e": g[-1]["e"], "w": g}; txt = " ".join(str(w["t"]) for w in g); why = cm.important(txt); score = sum({"رقم أو سعر": 2, "نصيحة أو مقارنة": 2, "اسم": 1}.get(x, 1) for x in why) + min(2, len(c["w"]) / 5)
        if c["s"] < 2.5 or len(c["w"]) < 3: continue   # الهوك له عنوانه، والجمل القصيرة ما تحمل فكرة
        if not busy(c["s"], c["e"] + 1.5): cands.append((score, c["s"], txt, why))
    cands.sort(key=lambda x: -x[0]); out = []
    for sc, s, txt, why in cands:
        if len(out) >= n: break
        if all(abs(s - o["at"]) >= spacing for o in out): out.append({"at": round(s, 2), "text": txt, "why": why})
    return sorted(out, key=lambda o: o["at"])
def cmd_gen(work, args):
    sub = args[0] if args else "list"
    def opt(name, d=None):
        if name in args: i = args.index(name); v = args[i + 1]; del args[i:i + 2]; return v
        return d
    at = opt("--at"); fit = opt("--fit"); at = float(at) if at is not None else None
    try:
        if sub in ("request", "image", "video"):
            kind = args[1] if sub == "request" else sub; prompt = " ".join(args[2:] if sub == "request" else args[1:])
            if not prompt: sys.exit('gen: request image|video "وصف" [--at t] [--fit card|cover]')
            rid = gen_request(work, kind, prompt, at, fit or "card", by="claude"); r = gen_list(work)[-1]
            print("انحفظ طلب التوليد #%d (%s). ولّده من حساب المستخدم (%s) بهذا النص:\n  %s\nثم: python hs.py gen <work> import %d <الملف اللي نزل>" % (rid, kind, GEN_SITES[kind], gen_prompt(r), rid))
        elif sub == "list":
            q = gen_list(work)
            if not q: print("ما فيه طلبات توليد.")
            for r in q: print("#%d [%s] %s عند %s: %s%s" % (r["id"], "تمّ" if r["status"] == "done" else "ينتظر", "صورة" if r["kind"] == "image" else "مقطع", r.get("at"), r["prompt"], ("  ← " + r["file"]) if r.get("file") else ""))
            pend = [r for r in q if r["status"] != "done"]
            if pend: print("\nالنص الجاهز لكل طلب ينتظر:"); [print("  #%d → %s\n      %s" % (r["id"], GEN_SITES[r["kind"]], gen_prompt(r))) for r in pend]
        elif sub == "import":
            if len(args) < 3: sys.exit("gen: import <رقم الطلب أو -> <ملف> [--at t] [--fit card|cover]")
            print(json.dumps(gen_import(work, args[1], os.path.abspath(args[2]), at=at, fit=fit), ensure_ascii=False))
        elif sub == "rm": gen_rm(work, args[1]); print("انشال.")
        elif sub == "moments":
            for m in gen_moments(work, int(args[1]) if len(args) > 1 else 4): print("%6.2f  %s%s" % (m["at"], m["text"], ("   (" + "، ".join(m["why"]) + ")") if m["why"] else ""))
        else: sys.exit('gen: request image|video "وصف" [--at t] | list | import <رقم> <ملف> | rm <رقم>')
    except RuntimeError as e: sys.exit(str(e))
def cmd_platform(names): print(platform_text([n for n in names if n in PLATFORMS] or None)); print("\nالمقاسات: " + " · ".join("%s = %d×%d" % (k, v[0], v[1]) for k, v in FRAMES.items()))
# ───────────────────────── 4.0: الدمج (أفكار HyperFrames و lemo-opuscar و gbro و onetake، مكتوبة من الصفر) ─────────────────────────
TR_TYPES = ("curve", "push", "pull", "rack", "whip", "spin", "iris", "flash", "punch", "zoom", "blur", "glitch", "shake")
HALLU = ["اشتركوا في القناة", "اشترك في القناة", "لا تنسوا الاشتراك", "ترجمة نانسي قنقر", "نانسي قنقر", "شكرا للمشاهدة", "شكرا على المشاهدة",
         "اشتركو في القناة", "سبتايتل", "ترجمة اسعد", "شكرا لكم على المشاهدة"]
VOICE_FX = {"clarity": "equalizer=f=250:t=q:w=1:g=-2,equalizer=f=3000:t=q:w=1:g=2.5,",
            "deboom": "highpass=f=90,equalizer=f=200:t=q:w=1:g=-4,",
            "demud": "equalizer=f=250:t=q:w=1:g=-3,equalizer=f=4500:t=q:w=1:g=1.5,",
            "soft": "equalizer=f=3200:t=q:w=1:g=-3,equalizer=f=8000:t=q:w=1:g=-2,",
            "radio": "highpass=f=100,equalizer=f=180:t=q:w=1:g=2,equalizer=f=3000:t=q:w=1:g=3,acompressor=threshold=-20dB:ratio=4:attack=5:release=80,",
            "phone": "highpass=f=300,lowpass=f=3400,"}
def _ntxt(s): return " ".join(_norm(w) for w in str(s).split())
def audio_env(work, rate=50):
    """شدة الصوت كل 1/rate ثانية من cutz.mp4 (بايثون عادي، بلا مكتبات)."""
    import array
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", J(work, "cutz.mp4"), "-vn", "-ac", "1", "-ar", "8000", "-f", "s16le", "-"], capture_output=True).stdout
    a = array.array("h"); a.frombytes(raw[:len(raw) // 2 * 2]); hop = 8000 // rate
    return [sum(abs(x) for x in a[i:i + hop]) / hop for i in range(0, len(a), hop)], rate
_CG = None
def capgroup_mod():
    """engine/scripts/capgroup.py: تقسيم الكابشن والأسماء الإنجليزية (مشترك مع 02_captions)."""
    global _CG
    if _CG is None:
        eng = find_engine(None) or sys.exit("ما لقيت مجلد engine")
        spec = importlib.util.spec_from_file_location("hs_capgroup", os.path.join(eng, "scripts", "capgroup.py")); _CG = importlib.util.module_from_spec(spec); spec.loader.exec_module(_CG)
    return _CG
def caps_regroup(work, wpl=5, lines=2, pause=0.5, names=True):
    """4.9: يعيد تقسيم الكابشن: 5 كلمات بالسطر، كلمة أو كلمتين زيادة للكابشن اللي بعده، 3 أو أكثر سطر ثاني. ويكتب الأسماء المعروفة بالإنجليزي."""
    cg = capgroup_mod(); caps = rj(J(work, "caps.json")); words = [w for c in caps["cards"] for w in c["w"]]
    if not words: return 0, 0
    if names: words = cg.english_names(words)
    cards = cg.cards_of(cg.pack(words, wpl=wpl, lines=lines, pause=pause), total=caps.get("total"))
    snapshot(work, "قبل تقسيم الكابشن"); old = len(caps["cards"]); caps["cards"] = cards; wj(J(work, "caps.json"), caps)
    st = load_studio(work); hs = hs_of(st); hs.setdefault("cap", {})["wpl"] = wpl
    if names:
        for it in (hs.get("hooks") or {}).get("items") or []:
            if it.get("text"): it["text"] = cg.names_text(it["text"])
    wj(J(work, "studio.json"), st)
    return old, len(cards)
def caps_names(work):
    """يكتب الأسماء المعروفة بالإنجليزي بالكابشن الموجود (بدون ما يغيّر التقسيم)."""
    cg = capgroup_mod(); caps = rj(J(work, "caps.json")); ch = []
    for c in caps["cards"]:
        nw = cg.english_names(c["w"])
        if [w["t"] for w in nw] != [w["t"] for w in c["w"]]: ch.append(" ".join(str(w["t"]) for w in nw)); c["w"] = nw
    st = load_studio(work); hk = (hs_of(st).get("hooks") or {}).get("items") or []; hch = False   # والعنوان الثابت فوق
    for it in hk:
        if it.get("text") and cg.names_text(it["text"]) != it["text"]: ch.append(cg.names_text(it["text"])); it["text"] = cg.names_text(it["text"]); hch = True
    if ch: snapshot(work, "قبل الأسماء الإنجليزية"); wj(J(work, "caps.json"), caps)
    if hch: wj(J(work, "studio.json"), st)
    return ch
def caps_clean(work, dry=False):
    """يشيل جمل اخترعها whisper فوق السكوت (مثل «اشتركوا في القناة» أو «ترجمة نانسي قنقر»). يشيل الكابشن فقط، مو الفيديو."""
    caps = rj(J(work, "caps.json")); total = caps.get("total", 0); env, rate = audio_env(work)
    if not env: return []
    def lvl(a, b): seg = env[max(0, int(a * rate)):max(int(a * rate) + 1, int(b * rate))]; return sum(seg) / max(1, len(seg))
    sp = sorted(lvl(w["s"], w["e"]) for c in caps["cards"] for w in c["w"]); base = sp[len(sp) // 2] if sp else 1
    bad = []
    for i, c in enumerate(caps["cards"]):
        txt = _ntxt(card_key(c)); m = lvl(c["s"], c["e"]); hall = any(_ntxt(h) in txt for h in HALLU); quiet = m < 0.18 * base
        if (hall and (quiet or c["s"] > total - 2.5)) or m < 0.06 * base: bad.append(i)
    gone = [card_key(caps["cards"][i]) for i in bad]
    if bad and not dry:
        snapshot(work, "قبل تنظيف الكابشن"); caps["cards"] = [c for i, c in enumerate(caps["cards"]) if i not in bad]; wj(J(work, "caps.json"), caps)
    return gone
def cmd_caps(work, args):
    sub = args[0] if args else ""
    if sub == "regroup":
        kv = parse_kv(args[1:]); a, b = caps_regroup(work, int(kv.get("wpl", kv.get("words", 5))), int(kv.get("lines", 2)), float(kv.get("pause", 0.5)), names=str(kv.get("names", "true")).lower() != "false")
        print("الكابشن صار %s كلمات بالسطر على أنفاس الكلام: %d جملة ← %d" % (kv.get("wpl", kv.get("words", 5)), a, b))
        if (hs_of(load_studio(work)).get("en") or {}).get("map"): print("تنبيه: الترجمة كانت مربوطة بالجمل القديمة، أعد الترجمة (hs tr export/import).")
    elif sub == "clean":
        g = caps_clean(work, dry="--dry" in args)
        print(("انشالت %d جملة مخترعة:\n" % len(g) + "\n".join("  · " + x for x in g)) if g else "ما فيه جمل مخترعة.")
    elif sub == "names":
        ch = caps_names(work); print(("صارت بالإنجليزي في %d جملة:\n" % len(ch) + "\n".join("  · " + x for x in ch[:30])) if ch else "ما فيه أسماء تتبدّل.")
    elif sub == "unsure":   # 4.10
        u = caps_unsure(work); print(("%d كلمة ما تأكد منها التفريغ (تحتها خط منقط بالاستوديو):\n" % len(u) + "\n".join("  %s  «%s»  ← %s" % (fmt_t(x["s"]), x["t"], x["ctx"]) for x in u[:80])) if u else "كل الكلمات واضحة.")
    elif sub == "gloss":
        n = caps_gloss(work); print("انطبق القاموس على %d كلمة." % n if n else "ما فيه شي من قاموسك بهذا المقطع.")
    elif sub == "gaps":
        g = caps_gaps(work); print(("%d مكان فيه كلام بدون كابشن:\n" % len(g) + "\n".join("  %s ← %s (%.1f ث)" % (fmt_t(x["s"]), fmt_t(x["e"]), x["e"] - x["s"]) for x in g)) if g else "كل الكلام له كابشن.")
    else: sys.exit("caps: regroup [wpl=5 lines=2 pause=0.5 names=true] | names | clean [--dry] | unsure | gloss | gaps")

def looks_all(): return {k: v for k, v in (rj(os.path.join(HERE, "looks.json"), {}) or {}).items() if not k.startswith("_")}
def look_apply(work, name):
    st = load_studio(work); hs = hs_of(st)
    old_acc = (hs.get("cardDefault") or {}).get("accent")   # 4.17: الموشن اللي أخذ لون الطابع القديم يمشي مع الجديد
    if old_acc:
        for Ly in hs.get("layers") or []:
            if Ly.get("type") in ("mg", "anno") and Ly.get("accent") == old_acc: Ly.pop("accent", None)
    if name in ("off", "none", ""):
        hs.pop("look", None); hs.pop("grade", None); wj(J(work, "studio.json"), st); return "انشال الطابع."
    L = looks_all().get(name) or sys.exit("ما فيه طابع بهذا الاسم. شوف: hs look <work> list")
    hs["look"] = {"name": name, "overlay": L.get("overlay", "none"), "amount": L.get("amount", 0.5)}
    if L.get("grade"): hs["grade"] = {"preset": L["grade"], "amount": 0.85}
    hs.setdefault("cap", {}).update(L.get("cap") or {}); hs["cardDefault"] = dict(L.get("card") or {})
    for Ly in hs.get("layers") or []:
        if Ly.get("type") in ("split", "viz", "pip"): Ly.update({k: v for k, v in (L.get("card") or {}).items() if not (k == "deco" and Ly.get("type") == "viz")})
        if Ly.get("type") == "fx" and Ly.get("auto") in ("transitions", "trans") and L.get("tr"): Ly["fx"] = L["tr"]
    wj(J(work, "studio.json"), st); return "تطبّق الطابع: " + L.get("ar", name)
def cmd_look(work, args):
    sub = args[0] if args else "list"
    if sub == "list":
        for k, v in looks_all().items(): print("%-11s %s · طبقة %s · تلوين %s · انتقال %s" % (k, v.get("ar"), v.get("overlay"), v.get("grade"), v.get("tr")))
        print("طبّق: hs look <work> apply <الاسم> · شيله: hs look <work> off")
    elif sub == "apply" and len(args) > 1: print(look_apply(work, args[1]))
    elif sub == "off": print(look_apply(work, "off"))
    else: sys.exit("look: list | apply <name> | off")

def beat_detect(path, offset=0.0, sr=11025, hop=256):
    """يقيس إيقاع الموسيقى (بايثون عادي): الضربات، السرعة، وهل الموسيقى إيقاعية فعلاً أو هادية (لو هادية لا تقص على الضربة)."""
    import array, math
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vn", "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"], capture_output=True).stdout
    a = array.array("h"); a.frombytes(raw[:len(raw) // 2 * 2]); n = len(a) // hop
    if n < 50: return None
    e = [sum(x * x for x in a[i * hop:(i + 1) * hop]) / hop for i in range(n)]; le = [math.log10(1e-9 + x) for x in e]
    fl = [0.0] + [max(0.0, le[i] - le[i - 1]) for i in range(1, n)]; fps = sr / hop
    kk = (1, 2, 3, 2, 1); fs_ = [sum(kk[j] * fl[i + j - 2] for j in range(5) if 0 <= i + j - 2 < n) / 9.0 for i in range(n)]   # تنعيم بسيط عشان السرعة تنقاس صح
    lo, hi = int(fps * 60 / 180), int(fps * 60 / 60)
    ac = {L: sum(fs_[i] * fs_[i - L] for i in range(L, n)) for L in range(lo, hi + 1)}
    lag = max(ac, key=ac.get); mean_ac = sum(ac.values()) / len(ac); rhythmic = ac[lag] / max(1e-9, mean_ac) > 1.25 and sorted(fl)[int(n * 0.95)] > 0.15
    h = [L for L in (round(lag / 2) - 1, round(lag / 2), round(lag / 2) + 1) if L in ac]   # الضربة نص المدة؟ (خطأ الضعف المشهور)
    if h and max(ac[L] for L in h) >= 0.8 * ac[lag]: lag = max(h, key=ac.get)
    p = float(lag)
    if lag - 1 in ac and lag + 1 in ac:   # مدة بكسور (تمنع انزلاق الضربات مع الوقت)
        y0, y1, y2 = ac[lag - 1], ac[lag], ac[lag + 1]; d = (y0 - 2 * y1 + y2)
        if d < 0: p = lag + max(-0.5, min(0.5, 0.5 * (y0 - y2) / d))
    K = int((n - 1) / p)
    ph = max(range(lag), key=lambda o: sum(fl[int(round(o + k * p))] for k in range(K) if int(round(o + k * p)) < n))
    beats = [round(offset + (ph + k * p) / fps, 3) for k in range(K + 1) if ph + k * p < n]
    dn = max(range(4), key=lambda o: sum(fl[int(round(ph + (o + 4 * k) * p))] for k in range(len(beats) // 4) if int(round(ph + (o + 4 * k) * p)) < n))
    strong = beats[dn::4]
    return {"bpm": round(60 * fps / p, 1), "beats": beats, "strong": strong, "rhythmic": rhythmic, "src": os.path.basename(path), "offset": offset}
def cmd_beat(work, args):
    src = args[0] if args else ""; at = 0.0
    if "--at" in args: at = float(args[args.index("--at") + 1])
    if src.startswith(("my", "mk", "cc-")):
        sfx = rj(J(work, "sfx.json"), {}) or {}; v = (sfx.get(src) or [[0]])[0]; at = float((v if isinstance(v, list) else [v])[0]); src = os.path.join(sfx_dir(), src + ".wav")
    if not src:
        for nme in ("bg-audio", "bg", "music"):
            for ext in ("mp3", "m4a", "wav", "aac"):
                if os.path.exists(J(work, nme + "." + ext)): src = J(work, nme + "." + ext); break
            if src: break
    if not src or not os.path.exists(src): sys.exit("beat: عطني ملف الموسيقى (مسار، أو my2 من أصواته، أو bg-audio.mp3 بمجلد المشروع)")
    r = beat_detect(src, at) or sys.exit("الملف قصير أو ما انقرأ")
    wj(J(work, "beats.json"), r)
    print("السرعة %.0f ضربة/دقيقة · %d ضربة · %s" % (r["bpm"], len(r["beats"]), "إيقاعية: تقدر تقص على الضربة" if r["rhythmic"] else "هادية: لا تقص على الضربات، امش على الجمل"))

def cards_hint(total, density="some"):
    base = 7 if total < 60 else 10 if total < 180 else 15
    k = {"few": 1.5, "some": 1.0, "many": 0.7}.get(density, 1.0)
    return 0 if density == "none" else max(1, int(round(total / (base * k))))
def flow_tips(work, ev, total, hs):
    """نصايح الإيقاع والقراءة (مستوحاة من فحوص HyperFrames و onetake، مكتوبة من جديد)."""
    tips = []; iv = [b - a for a, b in zip(ev, ev[1:]) if b - a > 0.05]
    if len(iv) >= 5 and total > 12:
        m = sum(iv) / len(iv); sd = (sum((x - m) ** 2 for x in iv) / len(iv)) ** 0.5
        if m > 0 and sd / m < 0.25: tips.append({"t": 0, "k": "cadence", "msg": "التغييرات تجي على مسافات متساوية فتحس إنه عرض شرائح. نوّع: لحظة سريعة ولحظة هادية."})
        if max(iv) < 1.0: tips.append({"t": 0, "k": "rest", "msg": "ما فيه ولا لحظة هدوء ثانية كاملة. خلّ نفس قبل أهم جملة."})
    for L in hs.get("layers") or []:
        if L.get("off") or L.get("type") not in ("text", "lt", "cover"): continue
        txt = (L.get("text") or "") + (L.get("sub") or ""); n = len(re.sub(r"\s", "", txt))
        if not n: continue
        need = n / 12.0 + (0.4 if L.get("type") == "cover" else 1.0); have = float(L.get("e", 0)) - float(L.get("s", 0))
        if have < need * 0.8: tips.append({"t": L.get("s", 0), "k": "read", "msg": "«%s» يحتاج %.1f ث عشان ينقرا، وهو %.1f ث بس." % (txt.split("\n")[0][:24], need, have)})
    trs = [L for L in hs.get("layers") or [] if L.get("type") == "fx" and L.get("fx") in ("curve", "push", "pull", "rack", "whip", "spin", "iris")]
    if len(set(L.get("fx") for L in trs)) > 3: tips.append({"t": 0, "k": "trmix", "msg": "فيه أكثر من 3 أنواع انتقال. خلّها نوعين أو ثلاثة بالكثير."})
    if len(set(L.get("dir") or hs.get("trDir") or "right" for L in trs if L.get("fx") in ("curve", "whip"))) > 1: tips.append({"t": 0, "k": "trdir", "msg": "الانتقالات تمشي باتجاهات مختلفة. خلّها اتجاه واحد بكل المقطع."})
    ev_s = []   # 4.7: نفس الصوت أكثر من 3 مرات ورا بعض يتعب الأذن (قواعد المونتاج)
    for k, v in (rj(J(work, "sfx.json"), {}) or {}).items():
        if isinstance(v, list): ev_s += [(float(x[0] if isinstance(x, list) else x), k) for x in v]
    ev_s.sort(); run_k = None; run_n = 0
    for t0, k in ev_s:
        run_n = run_n + 1 if k == run_k else 1; run_k = k
        if run_n == 4: tips.append({"t": t0, "k": "sfxrep", "msg": "نفس الصوت (%s) 4 مرات ورا بعض. بدّل بينه وبين بديله، أو شيل واحد." % k}); break
    br = rj(J(work, "brief.json"), {}) or {}; want = cards_hint(total, br.get("cards", "some")) if br else 0
    have = sum(1 for L in hs.get("layers") or [] if not L.get("off") and (L.get("type") in ("split", "pip") or (L.get("type") == "viz" and L.get("kind") in ("card", "draw"))))
    if want and have < max(1, want // 2): tips.append({"t": 0, "k": "cards", "msg": "كروت الشرح %d، والمناسب لطول المقطع واختياره تقريباً %d." % (have, want)})
    return tips

def cmd_auto(work, args):
    kind = args[0] if args else "";
    if kind == "clear": kind = args[1]; print("انشالت."); auto_layers(work, kind, False); return
    if kind not in ("zooms", "transitions", "beats"): sys.exit("auto: zooms | transitions [type=curve dir=right] | beats | clear zooms|transitions|beats")
    print("انضاف %d %s" % (auto_layers(work, kind, True, parse_kv(args[1:])), {"zooms": "تقريب عند الكلمات المميّزة", "transitions": "انتقال عند تغيّر الفكرة", "beats": "ضربة على الإيقاع"}[kind]))

# ───────────────────────── الفحص الذاتي (3.1) ─────────────────────────
MOJIBAKE = ("\ufffd", "\u00d8\u00a7", "\u00d9\u201e", "\u00d8\u00b9", "\u00c3\u02dc", "\u00e2\u20ac")
def cmd_selftest(work=None, engine=None):
    """يفحص ملفات الاستوديو نفسها: الصياغة · سلامة النص العربي · اكتمال مفاتيح الواجهة باللغتين · الخط · (ومع <work>) الخادم يرد."""
    bad = []; n_ok = 0
    def chk(name, good, detail=""):
        nonlocal n_ok
        if good: n_ok += 1
        else: bad.append(name + ((": " + detail) if detail else ""))
        print(("OK   " if good else "خطأ  ") + name + ((" ← " + detail) if (detail and not good) else ""))
    files = ["hs.py", "ext.js", "app.js", "i18n.js", "qr.js", "studio.html", "hub.html", "review.html", "tele.html", "AGENT.md", "README.md", "SKILL.md"]; txt = {}
    for f in files:
        fp = os.path.join(HERE, f)
        if not os.path.isfile(fp): chk("موجود: " + f, False); continue
        try: txt[f] = open(fp, encoding="utf-8").read()
        except UnicodeDecodeError as e: chk("ترميز UTF-8: " + f, False, str(e)[:80]); continue
        hit = [m for m in MOJIBAKE if m in txt[f]] if f != "qr.js" else []
        chk("النص سليم: " + f, not hit, "فيه حروف خربانة " + repr(hit))
    if not os.path.isfile(ui_font()): print("ملاحظة: خط الواجهة الخاص مو موجود في fonts/، الواجهة تشتغل بالخط البديل")
    eng0 = find_engine(engine); chk("المحرّك engine كامل", bool(eng0) and all(os.path.exists(os.path.join(eng0, p)) for p in ("studio/studio.py", "scripts/04_render_frames.js", "scripts/21_vision.js", "vision/vision_bundle.mjs", "vision/wasm/vision_wasm_internal.wasm", "vision/selfie_segmentation.tflite", "vision/face_detection_short_range.tflite", "scripts/compose.REFERENCE.html", "scripts/03_cut_zoom.py", "scripts/05_sfx.py", "scripts/06b_master.sh", "MONTAGE.md")), "ملفات ناقصة من engine")
    try: compile(txt.get("hs.py", ""), "hs.py", "exec"); chk("صياغة hs.py", True)
    except SyntaxError as e: chk("صياغة hs.py", False, str(e))
    if shutil.which("node"):
        for f in ("ext.js", "app.js", "i18n.js"):
            r = subprocess.run(["node", "--check", os.path.join(HERE, f)], capture_output=True, text=True); chk("صياغة " + f, r.returncode == 0, (r.stderr or "").strip().split("\n")[-1][:160])
    else: print("تخطّي فحص صياغة الجافاسكربت: node مو موجود")
    i18 = txt.get("i18n.js", ""); app = txt.get("app.js", ""); html = txt.get("studio.html", "") + txt.get("review.html", "")
    ent = dict((m.group(1), (m.group(2), m.group(3))) for m in re.finditer(r"(?:^|[\s,{])([A-Za-z_]\w*):\[\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*\]", i18))
    chk("قاموس الواجهة انقرأ (%d مفتاح)" % len(ent), len(ent) > 200)
    used = set(k for k in re.findall(r"\bt\('([A-Za-z_]\w*)'", app) if not k.endswith("_")) | set(re.findall(r'data-t(?:-title|-ph)?="([A-Za-z_]\w*)"', html))
    def lst(name):
        m = re.search(name + r"\s*=\s*\[([^\]]*)\]", app); return re.findall(r"'([^']+)'", m.group(1)) if m else []
    bo = re.search(r"const B_OPTS=\{(.*?)\};", app, re.S); bvals = re.findall(r"'([^']+)'", bo.group(1)) if bo else []
    used |= set("b_" + v for v in bvals if not re.match(r"^\d", v)) | set("bf_" + v.replace(":", "x") for v in bvals if re.match(r"^\d", v))
    cp = re.search(r"const CAPPRE=\{(.*?)\} \};", app, re.S); cps = re.findall(r"(?:^|[\s,{])(\w+):\{font:", cp.group(1) + "}" if cp else "")
    chk("ستايلات الكابشن (%d)" % len(cps), len(cps) >= 12)
    try: lk = looks_all(); chk("الطوابع (%d)" % len(lk), len(lk) >= 8 and all(isinstance(v, dict) and v.get("card") for v in lk.values()))
    except Exception as e: chk("الطوابع", False, str(e)[:80])
    chk("أدوات 4.0 بالإضافة", all(x in txt.get("ext.js", "") for x in ("trDraw", "markLayer", "cursorLayer", "ltLayer", "collages", "gradeOf", "lookOverlay", "VK.line")))
    used |= set("cp_" + k for k in cps) | set("en_" + k for k in lst("const ENTERS")) | set("char_" + k for k in lst("const CHARS"))
    miss = sorted(k for k in used if k not in ent); chk("كل مفاتيح الواجهة المستخدمة موجودة بالقاموس (%d)" % len(used), not miss, "ناقص: " + "، ".join(miss[:14]))
    empty = sorted(k for k, (a, e) in ent.items() if not a.strip() or not e.strip()); chk("كل مفتاح له نص عربي وإنجليزي", not empty, "فاضي: " + "، ".join(empty[:10]))
    noar = sorted(k for k, (a, e) in ent.items() if not re.search(r"[؀-ۿ]", a) and re.search(r"[A-Za-z]{4,}", a) and a == e and k not in ("b_tiktok",))
    if noar: print("ملاحظة: مفاتيح عربيّها نفس الإنجليزي (أسماء علم غالباً): " + "، ".join(noar[:12]))
    for k, v in PLATFORMS.items(): chk("منصة %s كاملة" % k, len(v["safe"]) == 4 and v["tips"] and all(f in FRAMES for f in v["frames"]) and ("b_" + k) in ent)
    # 4.1: الأسلوب المتعلَّم · النشر · الإشعارات
    b0 = {"studio": {"hs": {"cap": {"font": "Cairo", "size": 70}, "layers": [{"id": "L1", "type": "text"}, {"id": "L2", "type": "card"}]}, "outro": {"cta": "تابعني"}}, "caps": {"cards": [{"w": [{"t": "الذكاء"}, {"t": "الاصطناعي"}, {"t": "جي بي تي"}]}]}, "theme": {"acc": "#F2B33D"}}
    c0 = {"studio": {"hs": {"cap": {"font": "Tajawal", "size": 70}, "layers": [{"id": "L1", "type": "text"}, {"id": "L3", "type": "viz"}]}, "outro": {"cta": "تابعني", "font": "Lalezar"}}, "caps": {"cards": [{"w": [{"t": "الذكاء"}, {"t": "الاصطناعي"}, {"t": "GPT"}]}]}, "theme": {"acc": "#E07A5F"}}
    d0 = style_diff(b0, c0)
    chk("الأسلوب: يلقط تعديلات المستخدم", d0["cap"] == {"font": "Tajawal"} and d0["outro"] == {"font": "Lalezar"} and d0["removed"] == {"card": 1} and d0["added"] == {"viz": 1} and d0["theme"] == {"acc": "#E07A5F"}, json.dumps(d0, ensure_ascii=False)[:200])
    chk("الأسلوب: يلقط تصحيح الكلمات", d0["words"].get("جي بي تي") == "GPT", json.dumps(d0["words"], ensure_ascii=False))
    chk("الأسلوب: الملخص يطلع", "Tajawal" in style_text({"n": 1, "updated": "x", "cap": {"font": "Tajawal"}, "words": {"a": "b"}}))
    chk("النشر: تيك توك متاح للكل", "tiktok" in publish_platforms())
    chk("الإشعارات: الرابط سليم", notify_url({"server": "https://ntfy.sh", "topic": "hojas-x"}, title="عنوان", filename="a.mp4").startswith("https://ntfy.sh/hojas-x?title=%D8"))
    # 4.2: الورق المتحرك والدحيح
    chk("الأساليب: إضافة الرسم فيها الورق المتحرك والدحيح", all(x in txt.get("ext.js", "") for x in ("function kinetics", "function deskItems", "function dkHeader", "function dkPerson", "dkNeedMask")))
    k0 = kin_compose("مونتاج ساعتين صار يخلص وأنت تشرب قهوتك".split(), 2)
    chk("الورق المتحرك: النص يتقسم لسطر وكلمة كبيرة", "\n* " in k0 or k0.startswith("* "), k0)
    sz = safe_of(["tiktok", "instagram"]); chk("حساب المنطقة الآمنة", sz["capMax"] == 67.0 and sz["capMin"] == 18.0, json.dumps(sz))
    oc = open_check(0.9, [0.0, 5.0, 9.0], {}, 20); oc2 = open_check(0.2, [0.0, 1.4, 9.0], {"hooks": {"on": True, "items": ["x"]}}, 20)
    chk("فحص أول 3 ثواني", oc["miss"] == ["voice", "change", "text"] and oc2["miss"] == [] and open_check(1.2, [0.0], {}, 4)["miss"] == [], json.dumps([oc, oc2]))
    lc = len_check(150, ["tiktok", "x", "linkedin"]); chk("فحص المدة مقابل المنصات", [(l["p"], l["k"]) for l in lc] == [("tiktok", "long"), ("x", "over"), ("linkedin", "long")] and len_check(40, ["tiktok", "instagram"]) == [] and [l["k"] for l in len_check(10, ["linkedin"])] == ["short"], json.dumps(lc))
    chk("أرقام المدة لكل منصة", all(v.get("maxS") and len(v.get("bestS") or []) == 2 for v in PLATFORMS.values()))
    chk("تلاشي الصوت بالخلفية", bg_fades({}) == ("1.0", "1.4") and bg_fades({"bgIn": 9, "bgOut": "x"}) == ("6.0", "1.4") and bg_fades({"bgOut": -2}) == ("1.0", "0.0") and "BG_FADE_OUT" in open(os.path.join(find_engine(engine) or HERE, "scripts", "06b_master.sh"), encoding="utf-8").read() if find_engine(engine) else False)
    chk("حساب القص 4:5", safe_of([], "4:5")["crop"] == [11.77, 82.08], json.dumps(safe_of([], "4:5")))
    chk("رقم الملاحظة الجديدة", next_note_id([{"id": "n1"}, {"id": 4}]) == 5)
    with tempfile.TemporaryDirectory() as tw:
        os.makedirs(os.path.join(tw, ".hs"))
        wj(os.path.join(tw, "caps.json"), {"total": 20, "cards": [{"s": 0, "e": 2, "w": [{"t": "هلا", "s": 0, "e": 1}]}]}); wj(os.path.join(tw, "studio.json"), {"hs": {"frame": {"ar": "9:16"}}})
        wj(os.path.join(tw, "sfx.json"), {"outro": 0}); wj(os.path.join(tw, "brief.json"), {"frame": "9:16", "fx": {"sfx": "none"}, "outro": {"use": True, "text": "تابعني"}, "goal": "ad"})
        r0 = {r["k"]: r["ok"] for r in brief_reqs(tw)}
        chk("قائمة التحقق من الإجابات", r0.get("frame") is True and r0.get("sfx") is True and r0.get("outro") is False and r0.get("goal") is False, json.dumps(r0))
    try:   # 4.4: ترشيح اللقطات من نص تجريبي
        td = tempfile.mkdtemp(); segs = []; t0 = 0.0
        for i in range(40):
            tx = "ليش الناس تخسر مليون ريال؟" if i % 9 == 0 else ("والله هذي الحقيقة." if i % 3 else "يعني كمّلنا بعدها")
            segs.append({"start": t0, "end": t0 + 4.2, "text": tx, "words": []}); t0 += 4.6
        wj(J(td, "long.json"), {"segments": segs}); wj(J(td, "clips.json"), {"src": "x", "dur": t0})
        C = clips_suggest(td, 3, "20-40", "الفلوس")
        chk("ترشيح اللقطات", len(C) >= 3 and all(20 <= c["to"] - c["from"] <= 41 for c in C) and C[0]["score"] >= C[-1]["score"] and "تبدأ بسؤال" in C[0]["why"], json.dumps(C[:2], ensure_ascii=False)[:200])
        shutil.rmtree(td, ignore_errors=True)
    except Exception as e: chk("ترشيح اللقطات", False, str(e))
    try:
        import sqlite3; cx = sqlite3.connect(":memory:"); cx.execute("CREATE VIRTUAL TABLE t USING fts5(a)"); f5 = True
    except Exception: f5 = False
    chk("قاعدة البيانات: توحيد الحروف وبحث سريع", norm_txt("أَلحقيقة إلى") == "الحقيقه الي" and (f5 or True), "" if f5 else "FTS5 مو متوفر، البحث بيشتغل بالطريقة العادية")
    try:
        pj = rj(os.path.join(HERE, ".claude-plugin", "plugin.json"), {}) or {}; sk = os.path.join(HERE, "skills", "hojas-studio", "SKILL.md")
        w1 = claude_why("You've hit your session limit · resets 11:40pm (Asia/Riyadh)"); w2 = claude_why("Invalid API key · Please run /login"); w3 = claude_why("weird thing", 2)
        chk("4.4.1: سبب وقوف Claude يتفهم (حد، دخول، غيره)", w1["why"] == "limit" and w1["reset"] == "11:40م" and w2["why"] == "login" and w3["why"] == "other" and "2" in w3["msg"])
        old_e = {k: os.environ.get(k) for k in ("OMP_NUM_THREADS", "HS_CPU")}; os.environ["HS_CPU"] = "light"
        try: chk("4.4.1: الوضع الخفيف يحدد الأنوية", lighten() == "light" and 1 <= int(os.environ.get("OMP_NUM_THREADS", "0")) < max(2, os.cpu_count() or 2))
        finally:
            for k, v in old_e.items():
                if v is None: os.environ.pop(k, None)
                else: os.environ[k] = v
        try:
            td = tempfile.mkdtemp(); mk = lambda s0, ws: {"s": s0, "e": s0 + len(ws) * 0.3, "w": [{"t": w, "s": s0 + i * 0.3, "e": s0 + i * 0.3 + 0.25} for i, w in enumerate(ws.split())]}
            wj(J(td, "caps.json"), {"total": 12, "cards": [mk(0.1, "اليوم بقولكم عن"), mk(1.5, "اليوم بقولكم عن أكبر غلط"), mk(3.5, "اليوم بقولكم عن أكبر غلط يسويه الناس"), mk(6, "تابعني للجزء الثاني")]})
            tk = takes(td); R = retention(td); RP = repurpose(td, True)
            chk("4.5: الإعادات تختار الأكمل · فحص قبل النشر · نصوص النشر", len(tk) == 1 and tk[0]["keep"] == 2 and R.get("ok") and 0 <= R["score"] <= 100 and len(R["curve"]) == 12 and RP.get("ok") and _unconj("وراح يوصلك") == "راح يوصلك" and _unconj("وقتها") == "وقتها")
            shutil.rmtree(td, ignore_errors=True)
        except Exception as e: chk("4.5: الإعادات وفحص قبل النشر", False, str(e)[:120])
        chk("البلقن: النسخة ونسخة السكل محدّثة", pj.get("version") == VERSION and os.path.isfile(sk) and open(sk, encoding="utf-8").read() == plugin_skill_text(), "شغّل: hs release")
    except Exception as e: chk("البلقن: النسخة ونسخة السكل محدّثة", False, str(e)[:120])
    try:
        L = sfx_lib(); cc = [x for x in L if x["id"].startswith("cc-")]; er = os.path.join(HERE, "engine", "references", "editing-rules.md")
        chk("4.7: مكتبة CC0 (128 صوت بأسماء وأقسام وروابط) وقواعد المونتاج", len(cc) == 128 and len({x["id"] for x in L}) == len(L)
            and all(x.get("ar") and x.get("use") and x.get("cat") in SFX_CAT and str(x.get("url", "")).startswith("https://raw.githubusercontent.com/kmilo93sd/agent-video-editor/8e32c0a") for x in cc)
            and os.path.isfile(er) and "cc-pop-1" in open(er, encoding="utf-8").read(), "%d صوت cc" % len(cc))
    except Exception as e: chk("4.7: مكتبة CC0 وقواعد المونتاج", False, str(e)[:120])
    try:   # 4.7.1: السكتات تنقص لحدها، القطعات على فريمات، الشريط بعد المؤثرات، بدون تغبيش على الأزرار، ووين وقف Claude
        td = tempfile.mkdtemp(prefix="hs-cut-"); eng = find_engine(None) or os.path.join(HERE, "engine")
        subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", "color=c=black:s=64x64:r=30:d=6", "-f", "lavfi", "-i",
                        "aevalsrc='0.3*sin(2*PI*440*t)*(lt(t,1)+between(t,2,3)+between(t,3.15,4.2)+between(t,5,5.6))':s=16000:d=6",
                        "-shortest", "-c:v", "libx264", "-preset", "ultrafast", "-c:a", "aac", "-y", os.path.join(td, "src.mov")], capture_output=True)
        subprocess.run([PY, os.path.join(eng, "scripts", "01_cut_plan.py"), td], capture_output=True)
        kp = (rj(os.path.join(td, "cut.json"), {}) or {}).get("keep") or []
        aligned = all(abs(round(x * 30) - x * 30) < 1e-3 for seg in kp for x in seg)
        chk("4.9: السكتة الطويلة تنقص لـ 0.16 ث والقصيرة تبقى، والقطعات على فريمات", len(kp) == 3 and aligned and 4.1 < sum(b2 - a2 for a2, b2 in kp) < 4.5, json.dumps(kp))   # كلام 3.65 + سكتة قصيرة 0.15 + سكتتين 0.22 + آخر 0.12
        shutil.rmtree(td, ignore_errors=True)
    except Exception as e: chk("4.7.1: قص السكتات", False, str(e)[:120])
    try:
        ex = txt.get("ext.js", "") or open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); sh_ = txt.get("studio.html", "") or open(os.path.join(HERE, "studio.html"), encoding="utf-8").read()
        chk("4.7.1: شريط التقدّم بعد التقريب، وما فيه تغبيش على الأزرار", "['bar',x=>{ if(_barFn" in ex and ex.index("['fx',") < ex.index("['mg',mgs]") < ex.index("['bar',x=>") and "backdrop-filter:var(--glass)" not in sh_)
        td = tempfile.mkdtemp(prefix="hs-act-"); wj(os.path.join(td, "studio.json"), {}); os.makedirs(os.path.join(td, ".hs"))
        open(os.path.join(td, ".hs", "activity.jsonl"), "w", encoding="utf-8").write(json.dumps({"id": 1, "t": int(time.time()) - 3600, "kind": "step", "text": "أفرّغ كلامك"}, ensure_ascii=False) + "\n")
        c1 = proj_card(td); say(td, "أحط الكروت"); c2 = proj_card(td); say(td, "جهز", "done"); c3 = proj_card(td); shutil.rmtree(td, ignore_errors=True)
        chk("4.7.1: المكتبة توضح وين وقف Claude", c1["stopped"] and "أفرّغ كلامك" in c1["sub"] and not c2["stopped"] and "أحط الكروت" in c2["sub"] and not c3["stopped"], "%s | %s | %s" % (c1["sub"], c2["sub"], c3["sub"]))
    except Exception as e: chk("4.7.1: الشريط والمكتبة", False, str(e)[:120])
    try:   # 4.8: الموشن الجاهز، النابض، والهوية
        ex = txt.get("ext.js", "") or open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); ap = txt.get("app.js", "") or open(os.path.join(HERE, "app.js"), encoding="utf-8").read()
        reg = re.search(r"const MGK=\{([^}]*)\}", ex); ks = [x.split(":")[0] for x in reg.group(1).split(",")] if reg else []
        chk("4.8: قوالب الموشن (ومعها شعار الشركة 4.9) بالمحرّك والاستوديو والأوامر", ks == list(MG_KINDS) and "['mg',mgs]" in ex and all(("mg:'+k" in ap or "'%s'" % k in ap) for k in MG_KINDS) and "function mgPanel" in ap, ",".join(ks))
        if shutil.which("node"):
            m = re.search(r"const SPW=\{\}; function spr\(k,z\)\{.*?\n.*?\}\n", ex, re.S)
            js = (m.group(0) if m else "") + "const a=[];for(let i=0;i<=200;i++)a.push(spr(i/200,1));const b=[];for(let i=0;i<=200;i++)b.push(spr(i/200,0.82));console.log(JSON.stringify({m1:Math.max(...a),e1:a[200],h1:a[100],m2:Math.max(...b),mono:a.every((v,i)=>!i||v>=a[i-1]-1e-9)}));"
            r = subprocess.run(["node", "-e", js], capture_output=True, text=True, timeout=20); o = json.loads(r.stdout or "{}")
            chk("4.8: النابض يستقر بالوقت بالضبط (بدون تجاوز، والخفيف يتجاوز 1 إلى 3%)", bool(o) and o["m1"] <= 1.0000001 and o["e1"] == 1 and o["h1"] > 0.85 and o["mono"] and 1.005 < o["m2"] < 1.03, json.dumps(o)[:120])
        bd = os.path.join(HERE, "brand"); import xml.etree.ElementTree as _ET
        svgs = ["hjs-symbol.svg", "hjs-wordmark.svg", "hjs-lockup.svg", "hjs-icon.svg", "favicon.svg"]; okb = all(_ET.parse(os.path.join(bd, f)).getroot().tag.endswith("svg") for f in svgs)
        hb = txt.get("hub.html", "") or open(os.path.join(HERE, "hub.html"), encoding="utf-8").read()
        chk("4.8: شعار هوجاس (الرمز + HJS) بملفات brand وشاشات التحميل", okb and "function hjsMark" in hb and "function hjsMark" in ap and "background:var(--cap);width:70%" not in hb and "hjsIn" in (txt.get("studio.html", "") or open(os.path.join(HERE, "studio.html"), encoding="utf-8").read()))
    except Exception as e: chk("4.8: الموشن الجاهز والهوية", False, str(e)[:160])
    try:   # 4.9: الكابشن، الأسماء، الكلام المهم، الكابشن اليتيم، الشعارات، الخط الخاص
        cg = capgroup_mod(); cm = cutmap_mod()
        mk = lambda ts, t0=0.0, d=0.3: [{"t": x, "s": round(t0 + i * d, 3), "e": round(t0 + i * d + 0.25, 3)} for i, x in enumerate(ts)]
        g6 = cg.pack(mk("و1 و2 و3 و4 و5 و6".split()) + mk("ب1 ب2 ب3".split(), 2.5), wpl=5, lines=2)
        g8 = cg.pack(mk("و1 و2 و3 و4 و5 و6 و7 و8".split()), wpl=5, lines=2)
        chk("4.9: الكابشن 5 كلمات، كلمة زايدة تروح للي بعده، و3 زايدة سطر ثاني", [len(g) for g in g6] == [5, 4] and g6[1][0]["t"] == "و6" and [len(g) for g in g8] == [8], "%s | %s" % ([len(g) for g in g6], [len(g) for g in g8]))
        en = cg.english_names(mk("أفضل من شات جي بي تي والسونيت بجوجل درايف".split()))
        chk("4.9: الأسماء المعروفة بالإنجليزي (ChatGPT · و Sonnet · ب Google Drive)", [w["t"] for w in en] == ["أفضل", "من", "ChatGPT", "و Sonnet", "ب Google Drive"] and en[2].get("en") == "ChatGPT", " | ".join(w["t"] for w in en))
        chk("4.9: كاشف الكلام المهم (رقم، اسم، نصيحة) بدون إنذار كاذب", cm.important("عندنا خمس نماذج") and cm.important("لازم تجرب Claude") and not cm.important("أو مع الفريق حقك") and not cm.important("الفلسفة كانت حلوة"))
        keep0 = [[0.0, 10.0]]; o0, _ = cm.offsets(keep0); new = [[0.0, 3.0], [5.0, 10.0]]; o1, t1 = cm.offsets(new)
        rm_ = lambda t, mode=None: cm.src_to_out(new, o1, cm.out_to_src(keep0, o0, t), mode)
        cc = cm.remap_caps({"cards": [{"s": 0.5, "e": 2.5, "w": mk(["أ", "ب"], 0.5)}, {"s": 3.2, "e": 4.6, "w": mk(["محذوف", "كله"], 3.4)}, {"s": 6.0, "e": 7.0, "w": mk(["باقي"], 6.0)}]}, rm_, t1)
        chk("4.9: الحذف يشيل كابشنه معه (ما يبقى كابشن يتيم) والباقي يتحرك", len(cc["cards"]) == 2 and cc["cards"][1]["w"][0]["t"] == "باقي" and abs(cc["cards"][1]["w"][0]["s"] - 4.0) < 0.01 and cc["total"] == 8.0, json.dumps([[c["s"], [w["t"] for w in c["w"]]] for c in cc["cards"]], ensure_ascii=False))
        td = tempfile.mkdtemp(prefix="hs-logo-"); ws9 = cg.english_names(mk("كلود أولاً تطبيق احترافي بالنسبة لي أفضل من شات جي بي تي".split(), 3.0, 0.4) + mk("وبعدين نستخدم كانفا للتصميم".split(), 30.0, 0.4))
        wj(os.path.join(td, "caps.json"), {"total": 40, "cards": cg.cards_of(cg.pack(ws9))}); wj(os.path.join(td, "studio.json"), {"hs": {"layers": []}}); pl = logos_plan(td); shutil.rmtree(td, ignore_errors=True)
        chk("4.9: شارة الشعار لما ينذكر الاسم، و«X أفضل من Y» شارتين", len(pl) == 2 and pl[0].get("name") == "Claude" and pl[0].get("name2") == "ChatGPT" and "أفضل" in pl[0].get("rel", "") and pl[1]["name"] == "Canva" and "mgLogo" in ex and "logo:mgLogo" in ex, json.dumps(pl, ensure_ascii=False)[:160])
        fbad = [f for f in glob.glob(os.path.join(HERE, "**", "*"), recursive=True) if re.search(r"thmanyah", os.path.basename(f), re.I) and ".git" not in f and "_backup" not in f]
        gi = open(os.path.join(HERE, ".gitignore"), encoding="utf-8").read() if os.path.isfile(os.path.join(HERE, ".gitignore")) else ""
        chk("4.9: ملفات خط ثمانية مو موجودة بمجلد السكل (رخصته تمنع النشر) والخطوط محجوبة من git", (not fbad or not os.path.isdir(os.path.join(HERE, ".git"))) and "fonts/*.woff2" in gi, ", ".join(os.path.basename(b) for b in fbad[:4]))
    except Exception as e: chk("4.9: الكابشن والأسماء والقص الآمن والشعارات", False, str(e)[:160])
    try:   # 4.10: اختيار الجمل والحلول العشر
        T = takes_mod()
        def mkw(lines):
            out = []; tt = 0.0
            for si, (gap, txt) in enumerate(lines):
                tt += gap
                for wi, x in enumerate(txt.split()):
                    if x.startswith("|"): x = x[1:]; tt += 0.3
                    out.append({"t": x, "s": round(tt, 3), "e": round(tt + 0.3, 3), "p": 0.9, "si": si, "wi": wi}); tt += 0.35
            return out
        d = T.scan(mkw([(0, "مساكم الله بالخير"), (0.8, "ترجمة نانسي قنقر"), (0.8, "كل يوم"), (0.6, "يطلع لك فيديو المحتوى"), (0.7, "كل يوم يطلع لك فيديو لصانع محتوى ناجح"),
                        (0.7, "تعطيه الفيديو آ ويعدل لك"), (0.7, "النتائج قوية قوية يعني"), (0.8, "لازم تزور مقبرة الفشل"), (0.7, "تزور مقبرة"), (0.7, "لازم تزور مقبرة الفشل قبل لا تبدا"), (0.8, "وهذا |وهذا الشي اسمه الانحياز")]))
        I = {it["text"]: it for it in d["items"]}
        ok1 = ("greet" in I["مساكم الله بالخير"]["tags"] and not I["مساكم الله بالخير"]["drop"] and I["ترجمة نانسي قنقر"]["drop"] and "stumble" in I["كل يوم"]["tags"]
               and I["يطلع لك فيديو المحتوى"]["drop"] and I["كل يوم يطلع لك فيديو لصانع محتوى ناجح"].get("chosen") and I["لازم تزور مقبرة الفشل قبل لا تبدا"].get("chosen") and I["تزور مقبرة"]["drop"]
               and [t_["kind"] for t_ in I["تعطيه الفيديو آ ويعدل لك"]["trims"]] == ["hes"] and not I["النتائج قوية قوية يعني"]["trims"] and [t_["text"] for t_ in I["وهذا وهذا الشي اسمه الانحياز"]["trims"]] == ["وهذا"])
        chk("4.10: اختيار الجمل (إعادة تختار الكاملة، بداية متعثرة، تلعثم وتردد، التأكيد يبقى، كلام مخترع، تحية اقتراح)", ok1, T.summary(d))
        # مشروع صغير بصوت حقيقي: نبضات كلام وسكوت
        td = tempfile.mkdtemp(prefix="hs-tk-"); sr = 16000; import math as _m, wave as _wv
        bursts = [(0.2, 1.2), (1.6, 2.4), (2.8, 3.8), (4.2, 5.4), (5.8, 6.8)]; n_ = int(7.2 * sr); sm = bytearray()
        for k in range(n_):
            x = k / sr; v = 0.5 * _m.sin(2 * _m.pi * 220 * x) if any(a <= x <= b for a, b in bursts) else 0.0005 * _m.sin(2 * _m.pi * 50 * x)
            sm += int(v * 32767).to_bytes(2, "little", signed=True)
        with _wv.open(os.path.join(td, "a.wav"), "wb") as wf: wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr); wf.writeframes(bytes(sm))
        segs = [("أهلا بكم اليوم", 0.2, 1.2), ("نتكلم عن", 1.6, 2.4), ("نتكلم عن الفشل", 2.8, 3.8), ("وكيف تتجاوزه بسرعة", 4.2, 5.4)]
        aj = {"segments": [{"start": a, "end": b, "text": tx, "words": [{"word": " " + x, "start": round(a + k * (b - a) / len(tx.split()), 3), "end": round(a + (k + 1) * (b - a) / len(tx.split()), 3), "probability": 0.3 if x == "بسرعة" else 0.9} for k, x in enumerate(tx.split())]} for tx, a, b in segs]}
        wj(os.path.join(td, "a.json"), aj); wj(os.path.join(td, "cut.json"), {"keep": [[0.0, 1.15], [1.5, 7.0]], "total": 6.65, "src_dur": 7.2, "fps": "30"})
        ws0 = [{"t": w["word"].strip(), "s": round(w["start"] - (0.35 if w["start"] > 1.15 else 0), 3), "e": round(w["end"] - (0.35 if w["start"] > 1.15 else 0), 3)} for s_ in aj["segments"] for w in s_["words"]]
        wj(os.path.join(td, "caps.json"), {"total": 6.65, "cards": [{"s": ws0[0]["s"], "e": ws0[-1]["e"], "w": ws0}]}); wj(os.path.join(td, "studio.json"), {"hs": {"layers": [{"id": "L1", "type": "text", "s": 3.0, "e": 4.0}]}})
        bad_, o_, n_k = cut_on_sound(td); gaps_ = caps_gaps(td); un_ = caps_unsure(td)
        chk("4.10: قطعة على صوت تنزل لأقرب سكتة · كلام بدون كابشن · كلمة مشكوك فيها", len(bad_) == 1 and bad_[0]["to"] is not None and 1.18 <= bad_[0]["to"] <= 1.3 and len(gaps_) == 1 and 5.0 < gaps_[0]["s"] < 6.6 and [u["t"] for u in un_] == ["بسرعة"], json.dumps([bad_, gaps_, [u["t"] for u in un_]], ensure_ascii=False)[:160])
        tk_scan(td); dd = tk_load(td); st_ = next(it for it in dd["items"] if it["text"] == "نتكلم عن")
        r1 = tk_apply(td, None, lambda *a: None, rebuild=False); c1 = rj(os.path.join(td, "caps.json")); t1 = [w["t"] for c in c1["cards"] for w in c["w"]]
        tk_set(td, st_["id"], "keep"); r2 = tk_apply(td, None, lambda *a: None, rebuild=False); c2 = rj(os.path.join(td, "caps.json")); t2 = [w["t"] for c in c2["cards"] for w in c["w"]]
        L1 = hs_of(load_studio(td))["layers"][0]
        chk("4.10: القص من التسجيل الأصلي (المحذوف يروح كابشنه، والمرجّع يرجع من التفريغ، والطبقات تتبع)", st_["drop"] and t1.count("نتكلم") == 1 and r1["total"] < 6.0 and t2.count("نتكلم") == 2 and r2["total"] > r1["total"] and abs(L1["s"] - 3.0) < 0.05,
            "%s | %s | %.2f %.2f" % (" ".join(t1), " ".join(t2), r1["total"], r2["total"]))
        # الخطة والخطوات والأرقام والتقصير
        wj(os.path.join(td, "plan.json"), {"approved": False, "items": [{"id": 1, "s": 0, "e": 2, "show": "صورة", "kind": "gen", "example": "مثال"}, {"id": 2, "s": 3, "e": 99, "show": "", "kind": "x"}]})
        pb = plan_check(td); sp = steps(td); wj(os.path.join(td, "caps.json"), {"total": 30, "cards": [{"s": 1, "e": 3, "w": [{"t": x, "s": 1 + k * 0.3, "e": 1.2 + k * 0.3} for k, x in enumerate("Claude Opus 5.5 أفضل من GPT بسعر 20 دولار".split())]}]})
        fc = facts(td); shutil.rmtree(td, ignore_errors=True)
        chk("4.10: الخطة تنفحص · الخطوات · أرقام وموديلات تتأكد منها", len(pb) == 3 and [x["state"] for x in sp][:2] == ["done", "now"] and fc and "رقم أو سعر" in fc[0]["why"] and "نسخة أو موديل" in fc[0]["why"], json.dumps([pb, [x["state"] for x in sp], fc], ensure_ascii=False)[:160])
        # القاموس (بمجلد مؤقت عشان ما نلمس قاموسه)
        global HOME_CFG
        old_home = HOME_CFG; HOME_CFG = tempfile.mkdtemp(prefix="hs-gl-"); _GL["m"] = None
        try:
            A_ = {"cards": [{"w": [{"t": "أفضل"}, {"t": "من"}, {"t": "شادي"}, {"t": "بيتي"}, {"t": "بكل"}, {"t": "شي"}]}]}; B_ = {"cards": [{"w": [{"t": "أفضل"}, {"t": "من"}, {"t": "ChatGPT"}, {"t": "بكل"}, {"t": "شي"}]}]}
            C_ = {"cards": [{"w": [{"t": "كبير"}]}]}; D_ = {"cards": [{"w": [{"t": "ضخم"}]}]}
            n1 = gloss_learn(A_, B_); n2 = gloss_learn(C_, D_); ww, nn = gloss_apply_words([{"t": "وشادي", "s": 0, "e": 1}, {"t": "بيتي؟", "s": 1, "e": 2}, {"t": "شادي", "s": 2, "e": 3}, {"t": "بيتي", "s": 3, "e": 4}])
            G_ = gloss_load()
        finally: shutil.rmtree(HOME_CFG, ignore_errors=True); HOME_CFG = old_home; _GL["m"] = None
        chk("4.10: قاموسك يتعلّم التصحيح (الاسم) وما يتعلّم تغيير الصياغة، وينطبق على الجاي", n1 == 1 and n2 == 0 and [w["t"] for w in ww] == ["و ChatGPT؟", "ChatGPT"], json.dumps([n1, n2, [w["t"] for w in ww], G_], ensure_ascii=False)[:160])
        ap = txt.get("app.js", "") or open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); shtml = open(os.path.join(HERE, "studio.html"), encoding="utf-8").read(); i18 = open(os.path.join(HERE, "i18n.js"), encoding="utf-8").read()
        chk("4.10: الاستوديو فيه «الجمل» و«الخطة» وشريط الخطوات والخط المنقط", all(x in ap for x in ("function takesPanel", "function planPanel", "function stepsBar", "data-tkapply", "' lo'")) and 'data-ltab="takes"' in shtml and "tkTitle:" in i18 and "planTitle:" in i18 and ".w.lo" in shtml)
    except Exception as e: chk("4.10: اختيار الجمل والحلول العشر", False, str(e)[:200])
    try:   # 4.11: تراك الصوت وشيل الخلفية
        vf = vr_filters({"vr": [{"s": 1, "e": 2, "g": 0}, {"s": 3, "e": 4, "g": 1}, {"s": 5, "e": 6.5, "g": 0.5}]})
        chk("4.11: مستوى صوتك لأجزاء (كتم وخفض) بسلسلة التصدير، والمستوى 1 ما يضيف شي", vf == "volume=0.000:enable='between(t,1.000,2.000)',volume=0.500:enable='between(t,5.000,6.500)',", vf)
        td = tempfile.mkdtemp(prefix="hs-rb-"); ok_rb = False; det = ""
        try:
            import numpy as _np
            img = _np.full((120, 160, 4), 245, dtype=_np.uint8); img[:, :, 3] = 255; img[30:90, 40:120, :3] = (200, 40, 30); img[50:70, 70:90, :3] = 245
            _save_rgba(img, os.path.join(td, "in.png")); r_ = rmbg_flat(os.path.join(td, "in.png"), os.path.join(td, "out.png"))
            W_, H_, raw_ = _img_rgba(os.path.join(td, "out.png")); o_ = _np.frombuffer(raw_[:W_ * H_ * 4], dtype=_np.uint8).reshape(H_, W_, 4)
            ok_rb = r_.get("ok") and o_[5, 5, 3] == 0 and o_[60, 50, 3] == 255 and o_[60, 80, 3] == 255; det = json.dumps(r_)[:120]
        except ImportError: ok_rb = True; det = "numpy مو موجود، تخطيت"
        finally: shutil.rmtree(td, ignore_errors=True)
        chk("4.11: شيل الخلفية السادة (الحواف شفافة، والشكل وفتحته الداخلية باقية)", ok_rb, det)
        ap = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); hb = open(os.path.join(HERE, "hub.html"), encoding="utf-8").read(); s5 = open(os.path.join(find_engine(None), "scripts", "05_sfx.py"), encoding="utf-8").read()
        chk("4.11: الاستوديو فيه تعديل الأصوات (مستوى وقص وظهور واختفاء) وأجزاء الصوت وشيل الخلفية، والمكسر يطبّقها", all(x in ap for x in ("function sxGet", "function sxPut", "function vrDraw", "data-vact", "data-rmbg")) and "off=int(" in s5 and "_tg(v)" in s5
            and "DATA.root||''):'')+'</small>" not in hb and os.path.isfile(os.path.join(find_engine(None), "scripts", "23_rmbg.js")))
    except Exception as e: chk("4.11: تراك الصوت وشيل الخلفية", False, str(e)[:200])
    try:   # 4.12: صوت استوديو والتحكم بأي صوت بضغطة
        db_ = ([-30.0] * 60 + [-70.0] * 80) * 3 + [-36.0] * 60 + [-70.0] * 40
        cards_ = [{"s": 0.0, "e": 0.6}, {"s": 1.4, "e": 2.0}, {"s": 2.8, "e": 3.4}, {"s": 4.2, "e": 4.8}]
        g_, _ = sv_plan(db_, cards_); lg = lambda x: 20 * math.log10(max(x, 1e-9))
        chk("4.12: صوت استوديو يخفّض الفراغ الطويل بين الكلام 12 ديسيبل ويرفع الجملة الواطية لمستوى البقية", abs(lg(g_[110]) + 12) < 0.5 and abs(lg(g_[30])) < 0.3 and 4.5 < lg(g_[450]) < 5.6, "%.1f %.1f %.1f" % (lg(g_[110]), lg(g_[30]), lg(g_[450])))
        td = tempfile.mkdtemp(prefix="hs-sv-"); ok_sv = False; det = ""
        try:
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "anoisesrc=d=4:c=pink:a=0.02", "-f", "lavfi", "-i", "sine=f=220:d=4", "-filter_complex", "[1:a]volume='if(lt(mod(t,1.4),0.6),0.5,0)':eval=frame[s];[0:a][s]amix=inputs=2:normalize=0", "-ar", "48000", "-ac", "1", "-c:a", "aac", os.path.join(td, "cutz.mp4")], capture_output=True)
            wj(os.path.join(td, "caps.json"), {"total": 4, "cards": cards_[:3]}); f1, st1 = studio_voice(td, log=lambda m: None); m1 = os.path.getmtime(f1); f2, _ = studio_voice(td, log=lambda m: None)
            ok_sv = bool(f1) and f1 == f2 and os.path.getmtime(f2) == m1 and abs(ffdur(f1) - ffdur(os.path.join(td, "cutz.mp4"))) < 0.06 and voice_track(td, {}, lambda m: None) == (None, "")
            try: sv_import(td, f1.replace(".wav", "-x.wav")); ok_sv = False
            except RuntimeError: pass
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f1, "-t", "2", os.path.join(td, "short.wav")], capture_output=True)
            try: sv_import(td, os.path.join(td, "short.wav")); ok_sv = False; det = "قبل ملف أقصر من القص"
            except RuntimeError: pass
            det = det or json.dumps({k: st1.get(k) for k in ("denoise", "snrBefore", "snrAfter")})
        finally: shutil.rmtree(td, ignore_errors=True)
        chk("4.12: صوت استوديو يطلع ملف بنفس طول المقطع، وما يعيد الشغل لو ما تغيّر شي، ويرفض صوت من برا على قص ثاني", ok_sv, det)
        ap = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); i18 = open(os.path.join(HERE, "i18n.js"), encoding="utf-8").read()
        chk("4.12: الاستوديو فيه زر صوت استوديو والمقارنة، وتحكم الصوت بالضغط (لقطة، جملة، موسيقى)، والنموذج موجود", all(x in ap for x in ("function svBlock", "data-svab", "function rngRow", "kind==='music'", "'#tAu .mus'")) and "svOn:" in i18 and "musTitle:" in i18
            and os.path.isfile(os.path.join(find_engine(None), "audio", "sh.rnnn")))
    except Exception as e: chk("4.12: صوت استوديو", False, str(e)[:200])
    try:   # 4.12.1: كل طبقة بسطر
        ap = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); ex = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); sh_ = open(os.path.join(HERE, "studio.html"), encoding="utf-8").read()
        chk("4.12.1: الطبقات المتداخلة كل وحدة بسطر، والسطر الأعلى ينرسم فوق", "function layerRows" in ap and "function layerToRow" in ap and 'id="tLs"' in sh_ and "var(--lo" in sh_
            and "(a.track||0)-(b.track||0)" in ex and "(b.track||0)-(a.track||0)" not in ex)
    except Exception as e: chk("4.12.1: كل طبقة بسطر", False, str(e)[:200])
    try:   # 4.13: الصوت مقاطع
        ap = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); sh_ = open(os.path.join(HERE, "studio.html"), encoding="utf-8").read()
        chk("4.13: صوتك مقاطع تنضغط وتنقص وتنقسم وتنحذف، والمؤثر ينقسم بالمقص، والتايم لاين يطول ويتسحب", all(x in ap for x in ("function auSelectAt", "function auClips", "data-auact", "kind==='sfx'){ const [k,j]=String(id).split(':'), o=sxGet(k,+j); if(x<o.t+0.05", "function tlFit"))
            and 'id="tlGrip"' in sh_ and "var(--tlh,290px)" in sh_)
    except Exception as e: chk("4.13: الصوت مقاطع", False, str(e)[:200])
    try:   # 4.14: سجل التراجع على القرص
        td = tempfile.mkdtemp(prefix="hs-hist-")
        try:
            wj(os.path.join(td, "studio.json"), {"hs": {"a": 1}}); hist_checkpoint(td)
            wj(os.path.join(td, "studio.json"), {"hs": {"a": 2}}); hist_checkpoint(td, "تجربة")
            open(os.path.join(td, "studio.json"), "w", encoding="utf-8").write('{"hs":{"a":2}}'); same = not hist_checkpoint(td)   # نفس المحتوى بتنسيق ثاني ما يصير خطوة
            ok1, rb1, why1 = hist_step(td, True); a1 = rj(os.path.join(td, "studio.json"))["hs"]["a"]
            ok2, _, _ = hist_step(td, False); a2 = rj(os.path.join(td, "studio.json"))["hs"]["a"]
            ok3, _, _ = hist_step(td, False)
            chk("4.14: التراجع والإعادة من السجل اللي بالمشروع (وتغيير التنسيق بس ما ينحسب خطوة)", same and ok1 and why1 == "تجربة" and a1 == 1 and ok2 and a2 == 2 and not ok3 and not rb1, "%s %s %s %s" % (same, a1, a2, ok3))
        finally: shutil.rmtree(td, ignore_errors=True)
        ap = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); ex = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); sh_ = open(os.path.join(HERE, "studio.html"), encoding="utf-8").read()
        chk("4.14: ربط الصوت بالصورة، حذف الصوت بس أو الصورة بس، والقص يفصل القطع (بدل الخط الأحمر)", all(x in ap for x in ("function linkToggle", "function blankAdd", "function avDel", "'/hs/undo'", "class=\"cutgap\"", "function marksSave")) and "function blankA" in ex and 'id="bLink"' in sh_ and ".cutgap{" in sh_)
    except Exception as e: chk("4.14: السجل والربط", False, str(e)[:200])
    try:   # 4.15: حركة الصور والتعليق عليها
        ex = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); ap = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); i18 = open(os.path.join(HERE, "i18n.js"), encoding="utf-8").read()
        kinds_ok = all(("k==='%s'" % k) in ex for k in ANNO_KINDS)
        chk("4.15: حركة الصور (دفع، تحريك، يد، هزّة، دخول وخروج) والتعليق عليها (8 أنواع) والكلمة المتوهجة، بالمحرك والاستوديو", "function imgMove" in ex and "function annoLayer" in ex and kinds_ok and "an==='glow'" in ex
            and all(x in ap for x in ("function annoInsp", "function imgMoveInsp", "function pickAt", "data-add=\"anno:")) and "ak_ring:" in i18 and "im_push:" in i18)
    except Exception as e: chk("4.15: حركة الصور", False, str(e)[:200])
    try:   # 4.16: القصة البصرية من الخطة
        td = tempfile.mkdtemp(prefix="hs-st-")
        try:
            W_ = [("كلود", 0.0), ("أفضل", 0.5), ("من", 0.8), ("شات", 1.0), ("جي", 1.3), ("بي", 1.5), ("تي.", 1.7), ("الكريدت", 2.6), ("مثل", 3.0), ("الرصيد", 3.3), ("اللي", 3.7), ("تستعمله", 4.0),
                  ("Low", 5.2), ("Medium", 5.8), ("High", 6.4), ("Extra", 7.0), ("Max", 7.6), ("هذا", 8.6), ("اليوم", 8.9), ("الأول", 9.3)]
            cards = [{"s": W_[i][1], "e": W_[i + 1][1] - 0.02 if i + 1 < len(W_) else 9.8, "w": [{"t": t, "s": s, "e": s + 0.25} for t, s in W_[i:i + 2]]} for i in range(0, len(W_), 2)]
            wj(os.path.join(td, "caps.json"), {"total": 10.0, "cards": cards}); wj(os.path.join(td, "studio.json"), {"hs": {"layers": [{"id": "L1", "type": "text", "s": 0, "e": 1, "text": "يدوي"}]}})
            bt = plan_beats(td); p0 = plan_draft(td); again = plan_draft(td)
            ct_ = cue_times(td, ["الرصيد", "تستعمله"], 2.5, 4.6); ct2 = cue_times(td, ["Low", "Medium", "High", "Extra", "Max"], 5.0, 8.0)
            P_ = {"approved": True, "look": "", "items": [
                {"id": 1, "s": 0.0, "e": 2.4, "kind": "text", "show": "x", "logo": [{"name": "Claude", "cue": "كلود", "src": "x.svg"}], "mg": [{"kind": "logo", "name": "Claude", "name2": "ChatGPT", "rel": "أفضل من", "cue": "أفضل", "src": "a.svg", "src2": "b.svg"}]},
                {"id": 2, "s": 2.5, "e": 5.0, "kind": "draw", "show": "x", "example": "عداد بنزين", "src": "assets/story/fuel.png", "move": {"type": "push"},
                 "anno": [{"kind": "tags", "pts": [[0.5, 0.35]], "labels": ["رصيدك"], "cue": ["الرصيد"]}, {"kind": "path", "pts": [[0.6, 0.3], [0.4, 0.3]], "cue": ["تستعمله"]}]},
                {"id": 3, "s": 5.0, "e": 8.4, "kind": "draw", "show": "x", "example": "القير", "src": "assets/story/gear.png", "anno": [{"kind": "spots", "pts": [[0.5, 0.6], [0.5, 0.5], [0.5, 0.4], [0.5, 0.3], [0.5, 0.2]], "cue": ["Low", "Medium", "High", "Extra", "Max"]}]},
                {"id": 4, "s": 5.0, "e": 8.4, "kind": "gen", "show": "x", "example": "شاحنة", "prompt": "truck", "mg": {"kind": "steps", "text": ["Low", "Max"], "cue": ["Low", "Max"]}},
                {"id": 5, "s": 8.5, "e": 9.8, "kind": "text", "show": "x", "glow": {"text": "اليوم الأول", "cue": "اليوم"}}],
                "callback": {"s": 8.5, "e": 9.8, "items": ["assets/story/gear.png", {"src": "assets/story/fuel.png"}]}}
            wj(os.path.join(td, "plan.json"), P_); bad0 = plan_check(td)
            n1, miss1 = plan_build(td); L1 = hs_of(load_studio(td))["layers"]; n2, _ = plan_build(td); L2 = hs_of(load_studio(td))["layers"]
            by = lambda k, v: [L for L in L2 if L.get(k) == v]
            sp_ = next(L for L in L2 if L.get("kind") == "spots"); gl_ = next(L for L in L2 if L.get("anim") == "glow"); lg_ = [L for L in L2 if L.get("type") == "mg" and L.get("kind") == "logo"]
            stp = next(L for L in L2 if L.get("kind") == "steps")
            P_["items"][1]["anno"][0]["cue"] = ["مو موجودة"]; P_["items"].append({"id": 6, "s": 0, "e": 1, "kind": "gen", "show": "x"}); P_["items"].append({"id": 7, "s": 0, "e": 1, "kind": "text", "show": "x"})
            P_["items"].append({"id": 8, "s": 0, "e": 1, "kind": "text", "show": "x", "mg": [{"kind": "وهمي"}]}); wj(os.path.join(td, "plan.json"), P_); bad1 = plan_check(td)
            chk("4.16: القصة البصرية: الخطة تنقسم على الكلام، وكل حركة مع كلمتها، والبناء يعيد بدون تكرار", len(bt) >= 2 and p0 and again is None and len(p0["items"]) == len(bt)
                and len(ct_) == 2 and abs(ct_[0] - 3.3) < 0.01 and abs(ct_[1] - 4.0) < 0.01 and [round(x, 1) for x in ct2] == [5.2, 5.8, 6.4, 7.0, 7.6] and not bad0
                and n1 == n2 and len(L1) == len(L2) and any(L.get("text") == "يدوي" for L in L2) and miss1 == [4]
                and [round(x + sp_["s"], 1) for x in sp_["at"]] == [5.2, 5.8, 6.4, 7.0, 7.6] and abs(gl_["s"] - 8.9) < 0.01 and len(lg_) == 2 and abs(next(L for L in lg_ if L.get("name2"))["s"] - 0.38) < 0.01
                and stp["text"] == "Low\nMax" and len(stp["at"]) == 2 and len(by("pid", "callback")) == 2 and all(L.get("auto") == "plan" for L in L2 if L.get("text") != "يدوي")
                and len(bad1) >= 4, "beats=%d n=%s/%s miss=%s bad0=%s bad1=%d" % (len(bt), n1, n2, miss1, bad0, len(bad1)))
        finally: shutil.rmtree(td, ignore_errors=True)
        ex = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); ap = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); i18 = open(os.path.join(HERE, "i18n.js"), encoding="utf-8").read()
        chk("4.16: زر «ابنِ من الخطة» والفكرة والمثال بالاستوديو، والأفياش (خطوط من نقطة وحدة) والعدّاد مع الكلمات بالمحرّك، ومرجع الطريقة",
            "data-planbuild" in ap and "'/hs/plan_build'" in ap and "planExample:" in i18 and "planBuild:" in i18 and "pts[L.hub?0:i-1]" in ex and "L.pins===false" in ex and "Array.isArray(L.at)&&L.at.length){ let n=0" in ex
            and os.path.isfile(os.path.join(HERE, "engine", "references", "visual-story.md")) and "visual-story.md" in open(os.path.join(HERE, "SKILL.md"), encoding="utf-8").read())
        sh_ = open(os.path.join(HERE, "studio.html"), encoding="utf-8").read()
        chk("4.16: صفحة الأسئلة فيها رسمة توضيحية لكل خيار يحتاج شرح (الأسلوب، المدة، الإيقاع، مكان الكابشن، الصور، الكمية، الأصوات، المؤثرات)",
            "function vtiles" in ap and all(("vtiles('%s'" % g) in ap for g in ("style", "length", "pace", "pos", "media.mode", "media.amount", "fx.sfx")) and all(k in ap for k in ("dahih:()=>", "'fx.zoom':()=>", "'hook.use':()=>"))
            and all(("bv_%s:" % k) in i18 for k in ("style_dahih", "style_paper", "length_tight", "pace_fast", "pos_mid", "media_mix", "amount_many", "sfx_rich")) and "bg_goal_explain:" in i18 and ".vts{" in sh_)
    except Exception as e: chk("4.16: القصة البصرية", False, str(e)[:240])
    try:   # 4.17: الموشن ياخذ لون الطابع
        td = tempfile.mkdtemp(prefix="hs-look-")
        try:
            wj(os.path.join(td, "studio.json"), {"hs": {"layers": [{"type": "mg", "kind": "slam", "accent": "#AAAAAA"}, {"type": "mg", "kind": "stat", "accent": "#123456"}], "cardDefault": {"accent": "#AAAAAA"}}})
            look_apply(td, "cinema"); hs1 = hs_of(load_studio(td)); look_apply(td, "off"); hs2 = hs_of(load_studio(td))
        finally: shutil.rmtree(td, ignore_errors=True)
        ex = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); ap = open(os.path.join(HERE, "app.js"), encoding="utf-8").read()
        chk("4.17: الموشن (رقم، عنوان، قائمة، مراحل، اقتباس، دائرة، مقارنة، شعار) والتعليقات والتوهج تاخذ لون الطابع، ولون الحساب لو ما فيه طابع",
            "accent" not in hs1["layers"][0] and hs1["layers"][1]["accent"] == "#123456" and hs1["cardDefault"]["accent"] == "#F4C55A" and "look" not in hs2
            and "const lookAcc=()=>(HSX.look&&HSX.cardDefault&&HSX.cardDefault.accent)" in ex and ex.count("acc=L.accent||lookAcc()") >= 8 and "col=L.color||lookAcc()" in ex
            and "function lookAccOf(h)" in ap and "{type:'mg',kind:arg,track:1,...JSON.parse(JSON.stringify(MGDEF[arg]||{}))});" in ap)
    except Exception as e: chk("4.17: الموشن ياخذ لون الطابع", False, str(e)[:240])
    try:   # 4.17: ألوان كلود بالاستوديو والمكتبة
        sh_ = open(os.path.join(HERE, "studio.html"), encoding="utf-8").read(); hb_ = open(os.path.join(HERE, "hub.html"), encoding="utf-8").read(); ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read()
        lastroot = lambda s: s[s.rindex(":root{"):].split("}")[0]
        chk("4.17: الاستوديو والمكتبة بألوان كلود (غامق دافي، كريمي، برتقالي كلود) بدون أزرق ولا تدرجات بالأزرار",
            all("--bg:#1f1e1d" in lastroot(x) and "--y:#d97757" in lastroot(x) and "4.17: ألوان كلود" in x for x in (sh_, hb_))
            and not any(b in x for b in ("#4C8DFF", "#4c8dff", "76,141,255", "#6aa2ff") for x in (sh_, hb_)) and "x.fillStyle='#8fa36f'" in ap_)
    except Exception as e: chk("4.17: ألوان كلود", False, str(e)[:240])
    try:   # 4.18: وضعين بصفحة وحدة
        td = tempfile.mkdtemp(prefix="hs-mode-")
        try:
            wj(os.path.join(td, "studio.json"), {}); m0 = studio_mode(td); m1 = studio_mode_set(td, "claude", only_if_unset=True); m2 = studio_mode_set(td, "manual", only_if_unset=True)
            m3 = studio_mode(td); studio_mode_set(td, "manual"); m4 = studio_mode(td); bad18 = studio_mode_set(td, "وهمي")
        finally: shutil.rmtree(td, ignore_errors=True)
        sh_ = open(os.path.join(HERE, "studio.html"), encoding="utf-8").read(); ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); i18_ = open(os.path.join(HERE, "i18n.js"), encoding="utf-8").read(); me_ = open(os.path.abspath(__file__), encoding="utf-8").read()
        chk("4.18: وضعين بصفحة وحدة (Claude يمنتج · مونتاج يدوي) بزر فوق، والاختيار من المكتبة، و«اسأل Claude» يعدّل على اللي حددته",
            m0 is None and m1 == "claude" and m2 == "claude" and m3 == "claude" and m4 == "manual" and bad18 is None
            and 'id="modeSw"' in sh_ and 'id="bAsk"' in sh_ and "body[data-mode=claude]:not(.m) #bin{display:none}" in sh_ and "body[data-mode=manual]:not(.asking)" in sh_
            and "function setMode(m)" in ap_ and "function askCtxHtml()" in ap_ and "refreshCheck(); applyMode();" in ap_ and "askMark(); markTabs();" in ap_
            and all(k + ":" in i18_ for k in ("modeClaude", "modeManual", "askBtn", "askOnCap", "toManualBtn")) and '"mode": studio_mode(work)' in me_
            and 'hs_of(st)["mode"] = "manual" if mode == "manual" else "claude"' in me_ and "## 6ن)" in open(os.path.join(HERE, "SKILL.md"), encoding="utf-8").read())
    except Exception as e: chk("4.18: وضعين بصفحة وحدة", False, str(e)[:240])
    try:   # 4.19: أصوات من حسابه (بدون ما نلمس إعداداته الحقيقية)
        global sound_cfg_path
        td = tempfile.mkdtemp(prefix="hs-snd-"); real_ = sound_cfg_path; sound_cfg_path = lambda: os.path.join(td, "sound.json")
        try:
            p0 = sound_providers(); P1 = sound_set(["ElevenLabs", "my-tts"], None); n1 = sound_name("elevenlabs"); sound_set([]); p2 = sound_providers()
        finally: sound_cfg_path = real_; shutil.rmtree(td, ignore_errors=True)
        ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); i18_ = open(os.path.join(HERE, "i18n.js"), encoding="utf-8").read(); me_ = open(os.path.abspath(__file__), encoding="utf-8").read()
        chk("4.19: أصوات من حسابه: Claude يسجّل الخدمات المربوطة، وصفحة الأسئلة تسأل منين الأصوات، واللي يتولّد ينحفظ بأصواتي مع مصدره",
            p0 == [] and [p["id"] for p in P1] == ["elevenlabs", "my-tts"] and P1[0]["can"] == ["sfx", "music", "voice"] and n1 == "ElevenLabs" and p2 == []
            and "function sndSrcHtml()" in ap_ and "+sndSrcHtml()+btog('fx.bg'" in ap_ and all(k + ":" in i18_ for k in ("bqSrc", "bqSrcLib", "bqSrcCost", "bqSrcHint", "bqSrcNone"))
            and '"sound": sound_providers()' in me_ and 'm["gen"] = re.sub' in me_ and "--gen" in me_ and "## 6س)" in open(os.path.join(HERE, "SKILL.md"), encoding="utf-8").read())
    except Exception as e: chk("4.19: أصوات من حسابه", False, str(e)[:240])
    try:   # 4.20: الهوك تتحكم فيه · ربط النصوص باللقطة · الأقسام تكبر وتصغر · تعديلاتك ما تنحسب «Claude عدّل»
        td = tempfile.mkdtemp(prefix="hs-pin-")
        try:
            wj(os.path.join(td, "studio.json"), {"hs": {"layers": [{"id": "L1", "type": "text", "s": 5, "e": 7}, {"id": "L2", "type": "text", "s": 5, "e": 7, "pin": False}, {"id": "L3", "type": "text", "s": 1, "e": 2}]}})
            retime_project(td, lambda t, mode=None: (t - 2 if t >= 3 else (None if t > 1.5 else t)) if mode is None else (t - 2 if t >= 3 else (1.5 if mode == "prev" else 1.5) if t > 1.5 else t), 10, 8)
            L_ = {x["id"]: x for x in hs_of(load_studio(td))["layers"]}
        finally: shutil.rmtree(td, ignore_errors=True)
        ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); ex_ = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); sh_ = open(os.path.join(HERE, "studio.html"), encoding="utf-8").read(); i18_ = open(os.path.join(HERE, "i18n.js"), encoding="utf-8").read(); me_ = open(os.path.abspath(__file__), encoding="utf-8").read()
        chk("4.20: الهوك بالتايم لاين ولوحته وسحبه، وربط النصوص باللقطة بزر ومفتاح، والأقسام تكبر وتصغر، وحفظك ما ينحسب «Claude عدّل»",
            L_["L1"]["s"] == 3 and L_["L2"]["s"] == 5 and "L3" in L_
            and "function hookInspector()" in ap_ and "hookClip(on,box)" in ap_ and "x:h.x==null?0.5:h.x" in ex_ and 'id="bPin"' in sh_ and "function layerPinned(L)" in ap_ and "(layerPinned(L)?'':' free')" in ap_
            and "mk('#bin','hs.binw'" in ap_ and "body.cw:not(.m) #mid" in sh_ and "if(pt0<=LOCALW) return;" in ap_ and "AU._rt=setTimeout(" in ap_ and "function cutBusy()" in ap_ and "if(cutBusy()){ toast(t('cutBusy')); return; }" in ap_ and 'base.JOB["kind"] == "remove":   # 4.20' in me_ and all(k + ":" in i18_ for k in ("hookTitle", "toolPin", "pinLayer", "colGrip"))
            and "## 6ع)" in open(os.path.join(HERE, "SKILL.md"), encoding="utf-8").read())
    except Exception as e: chk("4.20: الهوك والنصوص المربوطة والأقسام", False, str(e)[:240])
    try:   # 4.22: حارس الصوت + الاختصارات وكليك يمين وصفحة «الاستوديو وقف»
        td = tempfile.mkdtemp(prefix="hs-guard-")
        try:
            subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", "sine=f=220:d=4", "-af", "volume=0.1", "-y", os.path.join(td, "v.wav")], check=True)
            subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", "sine=f=1000:d=4", "-ac", "2", "-y", os.path.join(td, "sfx.wav")], check=True)
            wj(os.path.join(td, "caps.json"), {"total": 4, "cards": [{"s": 0, "e": 4, "w": [{"t": "x", "s": 0.0, "e": 3.9}]}]})
            g1, b1 = voice_guard(td, {"voice": 1, "bg": 0.28}, lambda *_: None, os.path.join(td, "v.wav")); g2, _ = voice_guard(td, {"voice": 1, "guard": False}, lambda *_: None, os.path.join(td, "v.wav"))
        finally: shutil.rmtree(td, ignore_errors=True)
        ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); sh_ = open(os.path.join(HERE, "studio.html"), encoding="utf-8").read()
        chk("4.22: حارس الصوت (المؤثرات تحت صوتك والموسيقى أوطى)، تعلّق على المسافة يسرّع، S يقص عند المؤشر، كليك يمين، والضغط ينقل المعاينة، وصفحة «الاستوديو وقف»",
            0.03 < g1 < 0.2 and b1 == 0.28 and g2 == 1.0 and "function spaceDown(e)" in ap_ and "e.code==='KeyS'){ e.preventDefault(); cutHere(); }" in ap_ and "function ctxItems()" in ap_
            and "['layer','cap','sfx','hook','broll'].includes(D.kind)) seek(D.x0)" in ap_ and 'id="ctx"' in sh_ and 'id="bCutHere"' in sh_ and "function sfxGroups(L)" in ap_ and "IC_PAUSE" in ap_
            and "الاستوديو وقف" in stopped_html("x") and "stopped_html()" in open(os.path.abspath(__file__), encoding="utf-8").read() and ".pfg input{width:100%;min-width:0" in sh_)
    except Exception as e: chk("4.22: حارس الصوت والاختصارات", False, str(e)[:240])
    try:   # 4.23: القص الفوري
        td = tempfile.mkdtemp(prefix="hs-media-")
        try:
            K0 = [[0.0, 3.49], [4.67, 11.57], [11.88, 17.4]]; wj(os.path.join(td, "cut.json"), {"keep": K0}); a0 = media_map(td)
            media_pin(td); wj(os.path.join(td, "cut.json"), {"keep": [[0.0, 3.5], [4.666667, 8.0], [10.0, 11.566667], [11.866667, 17.4]]}); ok1, vm1 = media_map(td)
            wj(os.path.join(td, "cut.json"), {"keep": [[0.0, 3.5], [3.6, 11.57]]}); ok2, _ = media_map(td)
        finally: shutil.rmtree(td, ignore_errors=True)
        ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); rf_ = open(os.path.join(find_engine(None) or os.path.join(HERE, "engine"), "scripts", "04_render_frames.js"), encoding="utf-8").read(); cz_ = open(os.path.join(find_engine(None) or os.path.join(HERE, "engine"), "scripts", "03_cut_zoom.py"), encoding="utf-8").read()
        chk("4.23: القص فوري: الكابشن والطبقات تتغيّر على طول، والمعاينة تتخطّى المقصوص من الفيديو الحالي، والتراجع فوري، والفيديو ينبني وقت التصدير",
            a0 == (True, None) and ok1 and vm1 and abs(vm1[-1][1] - 13.9333) < 0.01 and any(abs(s[0] - 6.8333) < 0.01 and abs(s[2] - 8.82) < 0.01 for s in vm1) and ok2 is False
            and "function vmInv(o)" in ap_ and "Math.round(vm(w.hsWarp?w.hsWarp(x):x)*FPS)+1" in ap_ and "if(r&&r.instant)" in ap_ and "const VMAP=" in rf_ and '".hs","media.json"' in cz_ and "ensure_media(work, S, log)   # 4.23" in open(os.path.abspath(__file__), encoding="utf-8").read())
    except Exception as e: chk("4.23: القص الفوري", False, str(e)[:240])
    try:   # 4.23: نقل لقطة + قص الطرف بالسحب مباشرة
        td = tempfile.mkdtemp(prefix="hs-move-")
        try:
            wj(os.path.join(td, "cut.json"), {"keep": [[0.0, 4.0], [10.0, 14.0], [20.0, 24.0]]}); wj(os.path.join(td, "studio.json"), {"hs": {"layers": [{"id": "L1", "type": "text", "s": 5.0, "e": 6.0}, {"id": "L2", "type": "text", "s": 1.0, "e": 2.0, "pin": False}]}})
            wj(os.path.join(td, "caps.json"), {"total": 12, "cards": [{"s": 0.8, "e": 1.6, "w": [{"t": "أ", "s": 1.0, "e": 1.5}]}, {"s": 4.8, "e": 5.6, "w": [{"t": "ب", "s": 5.0, "e": 5.5}]}, {"s": 8.8, "e": 9.6, "w": [{"t": "ج", "s": 9.0, "e": 9.5}]}]})
            r9 = move_shot(td, 4, 8, 0); K = rj(os.path.join(td, "cut.json"))["keep"]; C = [c["w"][0]["t"] for c in rj(os.path.join(td, "caps.json"))["cards"]]; L = {x["id"]: x for x in hs_of(load_studio(td))["layers"]}; okm, vmm = media_map(td)
        finally: shutil.rmtree(td, ignore_errors=True)
        ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read()
        chk("4.23: تنقل اللقطة بالسحب (الكابشن والنصوص تمشي معها والمعاينة فورية)، وتقص طرف اللقطة بالسحب مباشرة وتشوف كم بتقص",
            K == [[10.0, 14.0], [0.0, 4.0], [20.0, 24.0]] and C == ["ب", "أ", "ج"] and abs(L["L1"]["s"] - 1.0) < 1e-3 and L["L2"]["s"] == 1.0 and okm and vmm and vmm[0][2] == 4.0 and r9["to"] == 0.0
            and "function moveShot(s,e,to)" in ap_ and "function edgeNear(x,tg)" in ap_ and "D.kind==='cbmaybe'" in ap_ and "async function reloadLite()" in ap_ and "if(!confirmIt) return doRemove(body,what);" in ap_)
    except Exception as e: chk("4.23: نقل اللقطة وقص الطرف", False, str(e)[:240])
    try:   # 4.24: 15 تعليق جديد على الصور
        N24 = ("arrow", "scribble", "underline", "highlight", "cross", "check", "lens", "spotlight", "blur", "bubble", "frame", "scan", "burst", "stars", "price")
        ex_ = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); i18_ = open(os.path.join(HERE, "i18n.js"), encoding="utf-8").read()
        chk("4.24: 15 تعليق جديد على الصور (سهم، دائرة بالقلم، خط تحت، تظليل، شطب، صح، عدسة تكبير، إضاءة، إخفاء، فقاعة، قفل هدف، مسح، انفجار، نجوم، سعر)",
            all(k in ANNO_KINDS for k in N24) and len(ANNO_KINDS) == 25 and "function annoPro(" in ex_ and "else annoPro(L,lt,k,col,fs,pts,lab,D);" in ex_ and all(("k==='%s'" % k) in ex_ for k in N24)
            and all(("'%s'" % k) in ap_.split("const ANK=")[1].split("]")[0] for k in N24) and all(("ak_%s:" % k) in i18_ and ("akHint_%s:" % k) in i18_ for k in N24) and all(("%s:{" % k) in ap_.split("const ANDEF=")[1].split("};")[0] for k in N24))
    except Exception as e: chk("4.24: 15 تعليق جديد", False, str(e)[:240])
    try:   # 4.25: تحسين الجودة + القص بمشروع ما فيه cut.json
        td = tempfile.mkdtemp(prefix="hs-q-")
        try:
            subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", "testsrc2=s=540x960:d=2:r=30", "-f", "lavfi", "-i", "sine=f=300:d=2", "-shortest", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-y", os.path.join(td, "cutz.mp4")], check=True)
            wj(os.path.join(td, "caps.json"), {"total": 2, "cards": [{"s": 0, "e": 2, "w": [{"t": "x", "s": 0.1, "e": 0.5}, {"t": "y", "s": 1.4, "e": 1.8}]}]}); wj(os.path.join(td, "studio.json"), {})
            vfr_extract(td, lambda *a: None, "light"); nq = len(os.listdir(os.path.join(td, "vfr"))); wq = vid_size(os.path.join(td, "cutz.mp4"))
            import struct; jb = open(os.path.join(td, "vfr", "00001.jpg"), "rb").read(); i_ = jb.find(b"\xff\xc0"); jh, jw = struct.unpack(">HH", jb[i_ + 5:i_ + 9]) if i_ > 0 else (0, 0)
            ci = cut_init(td); r_ = remove_ranges(td, None, lambda *a: None, ranges=[[0.8, 1.2]], rebuild=False); okc, vmc = media_map(td)
            _concat_cutz(td, rj(os.path.join(td, "cut.json"))["keep"], lambda *a: None); dc = probe_dur(os.path.join(td, "cutz.mp4")); okc2, vmc2 = media_map(td)
        finally: shutil.rmtree(td, ignore_errors=True)
        fl, fs_ = enh_filter("light", 1080, 1920), enh_filter("strong", 720, 1280)
        chk("4.25: تحسين الجودة (خفيف وقوي، ويرفع لـ1080) والتصدير بجودة أعلى، والقص يشتغل بمشروع ما فيه cut.json",
            nq == 60 and (jw, jh) == (1080, 1920) and enh_filter("off") == "" and "scale=1080:1920" not in fl and fs_.startswith("scale=1080:1920") and ("cas=" in fl or "unsharp=" in fl)
            and ci is True and r_["total"] < 2 and okc and vmc and abs(dc - r_["total"]) < 0.12 and okc2 and vmc2 is None
            and '"-crf", "18"' in open(os.path.abspath(__file__), encoding="utf-8").read() and "function qualitySec(h)" in open(os.path.join(HERE, "app.js"), encoding="utf-8").read())
    except Exception as e: chk("4.25: تحسين الجودة والقص بدون cut.json", False, str(e)[:240])
    try:   # 4.26: بودكاست (النص أول من الترجمة، ضعف المرشّحات، «هات غيرها») + الدبلجة بالسكتات
        td = tempfile.mkdtemp(prefix="hs-pod-")
        try:
            vt = os.path.join(td, "a.vtt"); open(vt, "w", encoding="utf-8").write("WEBVTT\n\n00:00:01.000 --> 00:00:03.000\nhello <00:00:01.500><c> big</c><00:00:02.000><c> world.</c>\n\n00:00:05.000 --> 00:00:07.000\nsecond line here\n")
            SV = vtt_segments(vt)
            subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", "sine=f=300:d=2", "-y", os.path.join(td, "s0.mp3")], check=True); subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", "sine=f=500:d=4", "-y", os.path.join(td, "s1.mp3")], check=True)
            wj(os.path.join(td, "caps.json"), {"total": 10, "cards": [{"s": 0.9, "e": 3.1, "w": [{"t": "hello", "s": 1.0, "e": 1.4}, {"t": "world", "s": 2.0, "e": 3.0}]}, {"s": 4.9, "e": 7.1, "w": [{"t": "second", "s": 5.0, "e": 7.0}]}]}); wj(os.path.join(td, "studio.json"), {})
            D0 = dub_script(td, "ar"); ni = dub_import(td, [{"i": 0, "tr": "مرحبا"}, {"i": 1, "tr": "ثاني"}]); dub_add(td, 0, os.path.join(td, "s0.mp3")); dub_add(td, 1, os.path.join(td, "s1.mp3")); fo, miss = dub_build(td, lambda *a: None)
            dd = ffdur(fo); mp = hs_of(load_studio(td))["en"]["map"]
            pw = os.path.join(td, "ep"); pod_want(pw, {"mode": "clips", "tr": "ar", "dub": "es", "host": 0}); wp = clips_cfg(pw)["want"]
        finally: shutil.rmtree(td, ignore_errors=True)
        hb_ = open(os.path.join(HERE, "hub.html"), encoding="utf-8").read(); ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); me_ = open(os.path.abspath(__file__), encoding="utf-8").read()
        chk("4.26: بودكاست beta (النص من ترجمة يوتيوب بدون تحميل، ضعف المرشّحات بنصها، «هات غيرها»، تنزيل اللي تختاره بس، مقدّم ثابت) والدبلجة بسكتات المقطع",
            len(SV) == 2 and [w["word"] for w in SV[0]["words"]] == ["hello", "big", "world."] and abs(SV[0]["words"][1]["start"] - 1.5) < 0.02 and len(SV[1]["words"]) == 3
            and len(D0["segs"]) == 2 and D0["segs"][0]["pause"] > 1.5 and ni == 2 and mp.get("hello world") == "مرحبا" and miss == 0 and abs(dd - 10) < 0.2
            and wp.get("tr") == "ar" and wp.get("dub") == "es" and wp.get("host") is False and "--download-sections" in me_ and "count=int(n or 5) * 2" in me_ and "fresh=True" in me_
            and "data-ntr" in hb_ and "#epMore" in hb_.replace("'epMore'", "#epMore") and "youtube-nocookie.com/embed" in hb_ and "function dubSec()" in ap_ and "## 6ص)" in open(os.path.join(HERE, "SKILL.md"), encoding="utf-8").read())
    except Exception as e: chk("4.26: بودكاست والدبلجة", False, str(e)[:240])
    try:   # 4.27: شكل البودكاست الافتراضي + قوالب الاسم + مكان الفيديو
        cz_ = open(os.path.join(find_engine(None) or "", "scripts", "03_cut_zoom.py"), encoding="utf-8").read(); ex_ = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read()
        hb_ = open(os.path.join(HERE, "hub.html"), encoding="utf-8").read()
        hot_ = pod_hot([{"words": [{"word": w} for w in "طيب اذا انت في الوظائف السيفي حقك كل شوي طالع".split()]}])
        chk("4.27: البودكاست بالشكل الجديد (الاسم من العنوان، الكلمة الذهبية، كادر ثابت) وقوالب الاسم ومكان الفيديو",
            pod_speaker("كيف تنجح العلاقات مع ياسر الحزيمي | بودكاست فنجان") == "ياسر الحزيمي" and pod_speaker("حلقة عن المال") == "" and hot_[:1] == ["الوظائف"] and POD_CAP["active"] != POD_CAP["color"]
            and '.get("vpos")' in cz_ and "FZ=" in cz_ and "hotLine" in ex_ and "function tplApply" in ap_ and "function vposSec" in ap_ and "/hs/vpos" in ap_ and "u.focus({preventScroll:true})" in hb_ and "host:false}" in hb_)
    except Exception as e: chk("4.27: شكل البودكاست وقوالب الاسم ومكان الفيديو", False, str(e)[:240])
    try:   # 4.28: المؤثرات الجديدة (ext.js والاستوديو والتصدير)
        ex_ = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); hb_ = open(os.path.join(HERE, "hub.html"), encoding="utf-8").read()
        rf_ = open(os.path.join(find_engine(None) or "", "scripts", "04_render_frames.js"), encoding="utf-8").read(); i18_ = open(os.path.join(HERE, "i18n.js"), encoding="utf-8").read()
        K_ = ["stretch", "rec", "notif", "search", "apps", "articles", "mosaic", "rewind", "ba"]
        chk("4.28: تسع مؤثرات (تمطيط، تصوير، إشعارات، خانة تكتب، برامج تنشطب، مقالات، صور كثيرة، ترجيع، قبل وبعد) وداخل جوال",
            all(k + ":mg" in ex_.replace(" ", "") or k + ":()=>" in ex_ for k in K_) and "window.hsWarp" in ex_ and "hsWarp" in rf_ and "w.hsWarp" in ap_ and "b.mode==='phone'" in ex_
            and all("mg_" + k + ":" in i18_ for k in K_) and all("'" + k + "'" in ap_ for k in K_) and "['phone',t('brPhone')]" in ap_ and "overflow:hidden}" in hb_ and "function kashida" in ex_ and "## 6ق)" in open(os.path.join(HERE, "SKILL.md"), encoding="utf-8").read())
    except Exception as e: chk("4.28: المؤثرات الجديدة", False, str(e)[:240])
    try:   # 4.30
        td = tempfile.mkdtemp(prefix="hs-n29-")
        try:
            wj(os.path.join(td, "caps.json"), {"total": 6, "cards": [{"s": 0, "e": 2, "w": [{"t": "كلمة", "s": 0, "e": 1}, {"t": "مو", "s": 1, "e": 1.5, "lo": True}]}, {"s": 2, "e": 2.4, "w": [{"t": "هذا كلام طويل جداً ما يلحق ينقرا", "s": 2, "e": 2.4}]}]}); wj(os.path.join(td, "studio.json"), {"hs": {"layers": []}})
            n1 = notes_auto(td); n2 = notes_auto(td); NN = rj(os.path.join(td, "notes.json"), [])
        finally: shutil.rmtree(td, ignore_errors=True)
        ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); ex_ = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); st_ = open(os.path.join(HERE, "studio.html"), encoding="utf-8").read()
        chk("4.30: ملاحظات «لازم تعدّلها» (ما تتكرر)، شريط التقدّم بإعداداته، الكابشن يتقصّر بحرية، قوالب الاسم تبان، ملء الشاشة بمقاسه",
            n1 == 2 and n2 == 0 and all(x["kind"] == "fix" and x["status"] == "ask" for x in NN) and "data-fixgo" in ap_ and "function barSec" in ap_ and "B.full?0:60" in ex_
            and "if(D.kind==='cap') en=Math.max" not in ap_ and "#wrap:fullscreen #frame" in st_ and "tile tplt" in ap_)
    except Exception as e: chk("4.30", False, str(e)[:240])
    try:   # 4.31
        ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); ex_ = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); st_ = open(os.path.join(HERE, "studio.html"), encoding="utf-8").read()
        rf_ = open(os.path.join(find_engine(None) or "", "scripts", "04_render_frames.js"), encoding="utf-8").read()
        chk("4.31: التصدير يلقى مكتبة كروم برّا البلقن، الاستوديو بالشاشات الأصغر، الفيديو يتحرك بيدك، كابشن البودكاست بدون &gt;&gt; واسم المتكلم الصح",
            "'.hojas-studio','node_modules','puppeteer-core'" in rf_ and callable(deps_keep) and "grid-template-columns:minmax(0,1fr)" in st_ and "function vxfPanel" in ap_ and "HSX.vxf" in ex_
            and pod_speaker("مركزية العلاقة مع الله | ياسر الحزيمي") == "ياسر الحزيمي" and cap_clean("&gt;&gt;") == "" and cap_clean("&gt;&gt;الليل") == "الليل")
    except Exception as e: chk("4.31", False, str(e)[:240])
    try:   # 4.32
        S_ = [{"start": 0, "end": 3, "text": "قال لي واحد عن"}, {"start": 3.2, "end": 6, "text": "الخياط اللي ما يعرف"}, {"start": 7, "end": 11, "text": "وبعدين صار يحسب"}, {"start": 13, "end": 16, "text": "سؤال ثاني تماما"}]
        T_ = thoughts(S_); ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); ex_ = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read()
        chk("4.32: المقطع فكرة كاملة (ما ينقص بنص الكلام)، الفلتر بالتشغيل، العناصر بأقسام، «Claude يمنتج» ما يعلق",
            T_ == [(0, 2), (3, 3)] and "X.__st?X.__st.call(X,1,0,0,1,0,0)" in ex_ and "function secTabs" in ap_ and "ELGROUPS" in ap_ and title_clean("&gt;&gt; سو") == "سو"
            and 'if edit in ("me", "claude"):' in open(os.path.abspath(__file__), encoding="utf-8").read())
    except Exception as e: chk("4.32", False, str(e)[:240])
    try:   # 4.33: الحفظ ما يتعارض بويندوز
        td = tempfile.mkdtemp(prefix="hs-wj-"); er_ = []
        try:
            def w_(i):
                try:
                    for k in range(40): job_set(td, stage="s%d" % i, k=k)
                except Exception as e: er_.append(e)
            def r_():
                for k in range(120): job_get(td)
            TT = [threading.Thread(target=w_, args=(i,)) for i in range(3)] + [threading.Thread(target=r_) for _ in range(2)]
            [x.start() for x in TT]; [x.join() for x in TT]
            left = [f for f in os.listdir(os.path.join(td, ".hs")) if f.endswith(".tmp")]
        finally: shutil.rmtree(td, ignore_errors=True)
        chk("4.33: حفظ الملفات ما يطلع «Access is denied» لو كتابتين وقراءات بنفس اللحظة", not er_ and not left)
    except Exception as e: chk("4.33", False, str(e)[:240])
    try:   # 4.34
        me_ = open(os.path.abspath(__file__), encoding="utf-8").read(); rf_ = open(os.path.join(find_engine(None) or "", "scripts", "04_render_frames.js"), encoding="utf-8").read()
        chk("4.34: فحص الأدوات يكتشف مكتبة التصدير، و«hs deps» يثبّتها بـ ~/.hojas-studio", callable(cmd_deps) and 'chk("مكتبة التصدير (puppeteer-core)"' in me_ and "hs deps" in rf_ and "hs deps" in open(os.path.join(HERE, "SKILL.md"), encoding="utf-8").read())
    except Exception as e: chk("4.34", False, str(e)[:240])
    try:   # 4.35
        td = tempfile.mkdtemp(prefix="hs-35-")
        try:
            v = os.path.join(td, "in.mp4"); subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", "color=c=black:s=64x64:d=2", "-f", "lavfi", "-i", "sine=f=440:d=2", "-shortest", "-c:v", "libx264", "-c:a", "aac", "-y", v], check=True)
            o = master_audio(td, v, os.path.join(td, "out.mp4"), lambda *a: None); okm = os.path.isfile(o) and ffdur(o) > 1.5
            r_ = os.path.join(td, "root"); w_ = os.path.join(r_, "clip-x"); os.makedirs(w_); wj(os.path.join(w_, "studio.json"), {}); wj(os.path.join(w_, "caps.json"), {"cards": []})
            old_h = HOME_CFG
            try: globals()["HOME_CFG"] = td; dst = project_trash(w_, r_)
            finally: globals()["HOME_CFG"] = old_h
            okt = os.path.isdir(dst) and not os.path.exists(w_) and os.path.basename(os.path.dirname(dst)) == ".trash"
        finally: shutil.rmtree(td, ignore_errors=True)
        ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); hb_ = open(os.path.join(HERE, "hub.html"), encoding="utf-8").read(); me_ = open(os.path.abspath(__file__), encoding="utf-8").read()
        chk("4.35: معايرة الصوت بدون bash، حذف المقطع لسلة، «ما عجبتني بدّلها»",
            okm and okt and "try: master_audio(work, out_final, out_master" in me_ and "function swapNote" in ap_ and "data-trash" in hb_ and "isn't for this environment" in open(os.path.join(HERE, "GUIDE.html"), encoding="utf-8").read())
    except Exception as e: chk("4.35", False, str(e)[:240])
    try:   # 4.36: تجميد اللقطة
        td = tempfile.mkdtemp(prefix="hs-frz-")
        try:
            wj(os.path.join(td, "studio.json"), {"hs": {"layers": []}}); er_ = None
            import contextlib, io
            with contextlib.redirect_stdout(io.StringIO()):
                cmd_layer(td, ["add", "type=mg", "kind=freeze", "style=photo", "label=قبل سنتين", "s=2"]); cmd_layer(td, ["add", "type=mg", "kind=rewind", "s=5"])
                try: cmd_layer(td, ["add", "type=mg", "kind=freeze", "style=xx"])
                except SystemExit as e: er_ = str(e)
            LL = hs_of(load_studio(td))["layers"]
        finally: shutil.rmtree(td, ignore_errors=True)
        ex_ = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); i18_ = open(os.path.join(HERE, "i18n.js"), encoding="utf-8").read()
        chk("4.36: تجميد اللقطة (فلاش، صورة، كوميكس، فيلم): الفريم يوقف وصوتك والكابشن يكملون، بالمحرّك والاستوديو والطرفية وكليك يمين",
            len(LL) == 2 and LL[0]["kind"] == "freeze" and LL[0]["style"] == "photo" and abs(LL[0]["e"] - 4.2) < 1e-6 and LL[1]["kind"] == "rewind" and er_ and "flash" in er_
            and "L.kind==='freeze'" in ex_ and "w.kind==='freeze'" in ex_ and all("st==='%s'" % k in ex_ for k in ("flash", "photo", "comic")) and "function frzDraw" in ex_
            and "'freeze'" in ap_ and "function freezeHere" in ap_ and "ctxFreeze" in ap_ and all(k in i18_ for k in ("mg_freeze:", "frz_film:", "ctxFreeze:")) and "kind=freeze" in open(os.path.join(HERE, "SKILL.md"), encoding="utf-8").read())
    except Exception as e: chk("4.36: تجميد اللقطة", False, str(e)[:240])
    try:   # 4.37: Motion Graphics أساسي، والهوية المحفوظة
        td = tempfile.mkdtemp(prefix="hs-37-"); old_h = HOME_CFG
        try:
            globals()["HOME_CFG"] = td
            I = ident_new("اختبار", "الخلفية #101010 والمميز #E8202A وخط Cairo، حسابي @abc والدعوة «ستوديو»")
            w_ = os.path.join(td, "w"); os.makedirs(w_); wj(os.path.join(w_, "studio.json"), {}); ident_apply(w_)
            th_ = rj(os.path.join(w_, "theme.json"), {}) or {}; st_ = load_studio(w_)
            oki = (I["colors"]["acc"] == "#E8202A" and I["colors"]["bg"] == "#101010" and th_.get("acc") == "#E8202A" and th_.get("handle") == "@abc" and hs_of(st_).get("identity") == I["slug"]
                   and (hs_of(st_).get("cap") or {}).get("active") == "#E8202A" and (st_.get("outro") or {}).get("word") == "ستوديو" and I.get("draft") and not ident_check("اختبار")[0] and ident_default() == I["slug"])
            md_ = open(I["md"], encoding="utf-8").read(); open(I["md"], "w", encoding="utf-8").write("\n".join(l for l in md_.split("\n") if not l.startswith("> مسودة")))
            okc = ident_check("اختبار")[0] and not ident_get("اختبار").get("draft") and ident_pick(w_, "none") is None
        finally: globals()["HOME_CFG"] = old_h; shutil.rmtree(td, ignore_errors=True)
        mg = open(os.path.join(HERE, "engine", "references", "motion-graphics.md"), encoding="utf-8").read(); tpl = mg.split("## 4) القوالب")[1].split("## 5)")[0]
        cat = re.findall(r"^\| (T\d\d) \|", mg, re.M); blocks = tpl.split("### MG-")[1:]
        flds = ("**متى:**", "**من وين:**", "**الأصول", "**المتغيرات:**", "**الشكل:**", "**الضربات", "**حركة كل عنصر:**", "**الانتقالات", "**الصوت والكابشن:**", "**المدة والمقاس:**", "**البناء بـ hs:**", "**البرومبت الجاهز:**", "**لو ناقص شي:**")
        okm = (all(("| %02d_" % i) in mg for i in range(1, 17)) and len(blocks) == 10 and all(all(f in b for f in flds) for b in blocks) and len(cat) >= 90 and set(cat) <= set(re.findall(r"T\d\d", tpl))
               and "## 5) البرومبت الرئيسي" in mg and "## 6) الصفحة الفاضية" in mg and "## 7) فحص الموشن" in mg and os.path.isfile(os.path.join(HERE, "engine", "references", "identity.md")))
        ex37 = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); okm = okm and "if(rt<0.18&&an!=='none')" in ex37 and "if(V.lay==='bare'){ const cb0=L.bgColor" in ex37   # 4.37: الصفحة الفاضية (قطع نظيف، والكتابة بلونها)
        sk_ = open(os.path.join(HERE, "SKILL.md"), encoding="utf-8").read(); ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); hb_ = open(os.path.join(HERE, "hub.html"), encoding="utf-8").read()
        dsc_ = re.search(r'^description: "(.*)"$', sk_, re.M)   # claude.ai يرفض السكل لو الوصف فوق 1024 حرف
        oku = (bool(dsc_) and len(dsc_.group(1)) <= 1024 and "## 2ب) Motion Graphics" in sk_ and "## 2ج) الهوية المحفوظة" in sk_ and "references/motion-graphics.md" in sk_ and "'normal','motion','podcast','paper','dahih'" in ap_ and "function idSecHtml" in ap_
               and "/hs/identity_file" in ap_ and "data-nid" in hb_ and "['motion',IC.spark" in hb_ and 'stl == "motion"' in open(os.path.abspath(__file__), encoding="utf-8").read())
        chk("4.37: Motion Graphics أساسي (16 مجلد، %d تقنية، 10 قوالب كاملة) والهوية المحفوظة تنطبق على المونتاج والموشن والبودكاست" % len(cat), oki and okc and okm and oku, "هوية=%s فحص=%s مرجع=%s واجهة=%s" % (oki, okc, okm, oku))
    except Exception as e: chk("4.37", False, str(e)[:240])
    try:   # 4.26: حارس: ولا متغيّر داخل السيرفر يغطّي D (مجلد الكاش) أو P أو S، كان يخلّي الفريمات والصور المصغّرة ما تطلع
        me_ = open(os.path.abspath(__file__), encoding="utf-8").read(); hb_ = open(os.path.join(HERE, "hub.html"), encoding="utf-8").read()
        bad_ = [l.strip()[:60] for l in me_.split(chr(10)) if re.match(r"^ {16,}(D|P|S|base|work) = ", l)]
        chk("4.26: السيرفر ما يغطّي متغيّراته (الفريمات تطلع)، ونافذة المشروع ما ترجّعك فوق، وقسم «بودكاست» بالمكتبة",
            not bad_ and "الاختيار ما يرجّعك فوق" in hb_ and "#hostName{background:var(--s1)" in hb_ and "'all','wait','work','ready','pod'" in hb_ and '"pod": bool((hs.get("pod") or {}).get("on"))' in me_, "; ".join(bad_))
    except Exception as e: chk("4.26: حارس متغيّرات السيرفر", False, str(e)[:240])
    try:   # 4.21: خروج الكابشن (cap.exit)، والافتراضي يطلع نفس القديم
        ex_ = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); i18_ = open(os.path.join(HERE, "i18n.js"), encoding="utf-8").read()
        exl = re.search(r"const EXITS=\[([^\]]*)\]", ap_); exl = re.findall(r"'([^']+)'", exl.group(1)) if exl else []
        chk("4.21: خروج الكابشن (عادي، تلاشي، يطير، ينزل، ينكمش، ينفجر، غباش، ينسحب، مسح، كلمة كلمة، قطع) بآخر كل جملة أو دفعة، والعادي نفس القديم",
            exl[:1] == ["auto"] and len(exl) == 11 and "CAP.exit==='zoom'?'punch'" in ex_ and "CAP.exitDur" in ex_ and all(("ex_" + k + ":") in i18_ for k in exl) and "exitLbl:" in i18_ and "exitHint:" in i18_
            and "if(EX_==='auto'&&rt<0.13){ const k=rt/0.13; a=k; dy=-(1-k)*10; }" in ex_ and "(CAP.exit||'auto'), EXD=" in ex_
            and all(("EX_==='" + k + "'") in ex_ for k in exl if k not in ("auto", "fade", "none")) and "X.filter='blur('" in ex_ and "segE=Math.min(c.e,nx[0].items[0].s)" in ex_
            and 'data-k="cap.exit"' in ap_ and "exit" in CAP_STYLE_KEYS and "`cap.exit`" in open(os.path.join(HERE, "SKILL.md"), encoding="utf-8").read())
    except Exception as e: chk("4.21: خروج الكابشن", False, str(e)[:240])
    try:   # 4.29: حركة بالمفاتيح: نفس الحساب بالمحرّك (ext.js) والطرفية، وبدون مفاتيح الرسم ما يتغيّر
        ex_ = open(os.path.join(HERE, "ext.js"), encoding="utf-8").read(); ap_ = open(os.path.join(HERE, "app.js"), encoding="utf-8").read(); i18_ = open(os.path.join(HERE, "i18n.js"), encoding="utf-8").read()
        sh_ = open(os.path.join(HERE, "studio.html"), encoding="utf-8").read(); sk_ = open(os.path.join(HERE, "SKILL.md"), encoding="utf-8").read()
        K0 = [{"t": 0, "dx": 0, "s": 1, "e": "linear"}, {"t": 1, "dx": 100, "dy": -50, "s": 1.5, "r": 30, "e": "back"}, {"t": 2, "dx": -40, "o": 0.2, "e": "hold"}, {"t": 3, "dx": 300, "s": 0.5}]
        U = [-1, 0, 0.25, 0.5, 1, 1.3, 1.9, 2, 2.5, 2.999, 3, 9]
        jsv = None; m_ = re.search(r"/\*KF\{\*/(.*?)/\*\}KF\*/", ex_, re.S)
        if m_ and shutil.which("node"):
            r_ = subprocess.run(["node", "-e", m_.group(1) + "\nconst K=" + json.dumps(K0) + ";console.log(JSON.stringify(" + json.dumps(U) + ".map(u=>kfVal(K,u))));const L={type:'text',s:2,e:6,kf:K};console.log(JSON.stringify([kfAt(L,3.25),kfAt({type:'image',fit:'cover',s:0,e:3,kf:K},1),kfAt({type:'text',s:0,e:3},1),kfPivot({type:'char'})]))"], capture_output=True, text=True, timeout=30)
            if r_.returncode == 0: jsv = [json.loads(l) for l in r_.stdout.strip().split("\n")]
        pyv = [kf_val(K0, u) for u in U]
        same = jsv is not None and all(abs(a_[f] - b_[f]) < 1e-6 for a_, b_ in zip(jsv[0], pyv) for f in KF_DEF)
        L_ = {"id": "L1", "type": "text", "s": 2.0, "e": 6.0}; kf_set(L_, 2.0, {}); kf_set(L_, 4.0, {"dx": -200, "s": 1.3, "e": "back"}); kf_set(L_, 4.004, {"dy": 90}); n1 = len(L_["kf"]); dy1 = L_["kf"][1]["dy"]
        kf_preset(L_, "pulse"); n2 = len(L_["kf"]); bad_ok = False
        try: kf_set(L_, 3, {"zz": 1})
        except ValueError: bad_ok = True
        chk("4.29: حركة بالمفاتيح (مكان، حجم، دوران، شفافية، و4 انتقالات) بالمحرّك والاستوديو والطرفية، وبدون مفاتيح نفس الرسم القديم",
            same and jsv[1][0] and abs(jsv[1][0]["dx"] - kf_val(K0, 1.25)["dx"]) < 1e-6 and jsv[1][1] is None and jsv[1][2] is None and jsv[1][3] == [216, 1190.4]
            and pyv[0]["dx"] == 0 and pyv[-1]["dx"] == 300 and abs(pyv[2]["dx"] - 25) < 1e-9 and pyv[8]["dx"] == -40 and pyv[6]["s"] < 1.0   # ثابت · ارتداد يعدّي هدفه · قفزة
            and n1 == 2 and dy1 == 90 and n2 == 9 and bad_ok and not kf_ok({"type": "image", "fit": "cover"}) and kf_ok({"type": "lt"})
            and "const Q=L.kf?kfAt(L,t):null;" in ex_ and "function kfSec(L)" in ap_ and "kfDots(L)" in ap_ and "data-kfa" in ap_ and "n.kf=L.kf.map" in ap_ and "D.kf0" in ap_ and ".clip .kfd{" in sh_
            and all(("%s:" % k) in i18_ for k in ("kfTitle", "kfAdd", "kfHint", "kfHint2", "kfe_hold", "kfp_sway", "kfPresetDone")) and "hs kf" in sk_, "js=%s" % ("بدون node" if jsv is None else "مختلف" if not same else "ok"))
    except Exception as e: chk("4.29: حركة بالمفاتيح", False, str(e)[:240])
    chk("الرسم الحر بالمحرّك والاستوديو", "function drawLayer" in txt.get("ext.js", "") and "function drawStart" in txt.get("app.js", ""))
    try:   # 4.6: كتم الكلمات
        m0, p0 = bleep_filters(bleep_of({})); ct = {"cards": [{"s": 0, "e": 2, "w": [{"t": "شركة", "s": 0.1, "e": 0.4}, {"t": "والشركه", "s": 0.5, "e": 0.9}, {"t": "شركات", "s": 1.0, "e": 1.3}]}]}
        hits = bleep_find(ct, ["شركة"]); B1 = bleep_of({"bleep": {"items": hits}}); m1, p1 = bleep_filters(B1); _, p2 = bleep_filters(bleep_of({"bleep": {"items": hits, "mode": "mute"}}))
        tx = bleep_card_text(ct["cards"][0], B1); hh = {}; n1 = bleep_add(hh, hits); n2 = bleep_add(hh, hits)
        chk("4.6: كتم الكلمات (يلقى الكلمة، يكتم الصوت، نجوم بالنص، وبدونها ما يتغيّر شي)", m0 == "" and p0 is None and len(hits) == 2 and "between(t,0.070,0.430)" in m1 and p1 and "sine=frequency=1000" in p1 and p2 is None
            and tx.split()[0] == "ش***" and tx.split()[2] == "شركات" and n1 == 2 and n2 == 0 and "function blMask" in txt.get("ext.js", "") and "function bleepPreview" in txt.get("app.js", "") and "blTitle:" in open(os.path.join(HERE, "i18n.js"), encoding="utf-8").read())
    except Exception as e: chk("4.6: كتم الكلمات", False, str(e)[:120])
    if work and os.path.isdir(work):
        eng = find_engine(engine)
        if not eng: chk("المحرّك موجود لفحص الخادم", False)
        else:
            port = 8700 + secrets.randbelow(80); pr = subprocess.Popen([PY, os.path.abspath(__file__), "serve", work, "--port", str(port), "--engine", eng], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            try:
                up = False
                for _ in range(40):
                    time.sleep(0.25)
                    try: urllib.request.urlopen("http://127.0.0.1:%d/hs/info" % port, timeout=2).read(); up = True; break
                    except Exception: pass
                chk("الخادم اشتغل", up)
                for path, need in (("/", b"app.js"), ("/hs/app.js", b"CAPPRE"), ("/hs/i18n.js", b"I18N"), ("/hs/info", b'"safe"'), ("/hs/brief", b'"cards"'), ("/hs/pulse", b'"sig"'), ("/review", b"<")) + ((("/hs/ui-font.otf", b"OTTO"),) if os.path.isfile(ui_font()) else ()):
                    try: body = urllib.request.urlopen("http://127.0.0.1:%d%s" % (port, path), timeout=8).read(); chk("يرد " + path, need in body, "الرد ما فيه المتوقع")
                    except Exception as e: chk("يرد " + path, False, str(e)[:100])
            finally: pr.kill()
    print("\n%s: %d فحص سليم%s" % ("كل شي سليم" if not bad else "فيه مشاكل", n_ok, ("، %d خطأ" % len(bad)) if bad else ""))
    return not bad

# ───────────────────────── أوامر الطرفية (يستخدمها Claude) ─────────────────────────
def parse_kv(args):
    o = {}
    for a in args:
        k, _, v = a.partition("=")
        try: o[k] = json.loads(v)
        except Exception: o[k] = v.replace("\\n", "\n")
    return o
def cmd_text(work, args):
    caps = rj(J(work, "caps.json"))
    if not args or args[0] == "show":
        for i, c in enumerate(caps["cards"]): print("%2d  %6.2f-%6.2f  %s" % (i + 1, c["s"], c["e"], card_key(c)))
        return
    i = int(args[0]) - 1
    if not (0 <= i < len(caps["cards"])): sys.exit("رقم الجملة برّا المدى (1-%d)" % len(caps["cards"]))
    before = rj(J(work, "caps.json")); apply_text(work, i, " ".join(a_ for a_ in args[1:] if a_ != "--no-learn"))
    if "--no-learn" not in args: gloss_learn(before, rj(J(work, "caps.json")))   # التصحيح ينحفظ بالقاموس (اسم، كتابة قريبة من الغلط، أو كلمة ما تأكد منها التفريغ)
    print("تم: الجملة %d ← %s" % (i + 1, " ".join(a_ for a_ in args[1:] if a_ != "--no-learn")))
def next_note_id(notes):
    return max([int(re.sub(r"\D", "", str(x.get("id"))) or 0) for x in notes] or [0]) + 1
def notes_auto(work):
    """4.29: ملاحظات «لازم تعدّلها» من Claude: كلمة ما وضحت بالصوت، كابشن أسرع من إنه ينقرا، نص صغير أو يمر بسرعة. ما تتكرر."""
    path = J(work, "notes.json"); notes = rj(path, []) or []; caps = rj(J(work, "caps.json"), {"cards": []}) or {"cards": []}; have = {n.get("auto") for n in notes if n.get("auto")}; add = []
    def put(key, tt, txt, card=None, word=None):
        if key in have: return
        have.add(key); add.append({"t": round(float(tt), 2), "card": card, "word": word, "text": txt, "auto": key})
    for i, c in enumerate(caps.get("cards") or []):
        ws = c.get("w") or []; lo = [j for j, w in enumerate(ws) if w.get("lo")]
        if lo:
            j = lo[0]; ctx = " ".join(w["t"] for w in ws)
            put("lo:%s:%s" % (i, ws[j]["t"]), ws[j]["s"], "ما وضحت لي %s بالصوت: «%s» بجملة «%s». اسمعها وصحّحها لو غلط." % ("كلمة" if len(lo) == 1 else "%d كلمات" % len(lo), "، ".join(ws[k]["t"] for k in lo[:4]), ctx[:90]), i, j)
        d = float(c.get("e", 0)) - float(c.get("s", 0)); ch = len(" ".join(w["t"] for w in ws))
        if d > 0.05 and ch >= 12 and ch / d > 24:
            put("fast:%s" % i, c["s"], "الكابشن هنا يمر بسرعة وصعب ينقرا (%d حرف بـ %.1f ث). طوّل وقته أو قسّمه سطرين." % (ch, d), i, None)
    for L in hs_of(load_studio(work)).get("layers") or []:
        if L.get("type") != "text" or L.get("off") or L.get("auto"): continue
        tx = str(L.get("text") or "").strip(); d = float(L.get("e", 0)) - float(L.get("s", 0))
        if not tx: continue
        if float(L.get("size") or 96) < 34: put("small:%s" % L.get("id"), L["s"], "النص «%s» صغير وصعب ينقرا بالجوال. كبّره شوي." % tx[:40])
        if d > 0 and len(tx) / d > 22: put("tfast:%s" % L.get("id"), L["s"], "النص «%s» يمر بسرعة (%.1f ث) وصعب يلحق ينقرا. طوّل وقته." % (tx[:40], d))
    for a in add:
        nid = next_note_id(notes); notes.append({"id": nid, "t": a["t"], "card": a["card"], "word": a["word"], "text": a["text"], "pin": None, "by": "claude", "kind": "fix", "who": "Claude",
                                                "status": "ask", "auto": a["auto"], "at": time.strftime("%Y-%m-%d %H:%M")})
    if add: wj(path, notes)
    return len(add)
def cmd_notes(work, args):
    path = J(work, "notes.json"); notes = rj(path, []) or []; caps = rj(J(work, "caps.json"), {"cards": []}); sub = args[0] if args else "list"
    if sub == "add":
        rest = list(args[1:]); kind = "suggest"; pin = None
        def o(nm):
            if nm in rest: i = rest.index(nm); v = rest[i + 1]; del rest[i:i + 2]; return v
        kind = o("--kind") or "suggest"; px, py = o("--x"), o("--y")
        if kind not in ("suggest", "question", "info", "fix"): sys.exit("--kind لازم: suggest | question | info | fix")
        if len(rest) < 2: sys.exit('notes <work> add <ثانية> "النص" [--kind suggest|question|info] [--x 0-1 --y 0-1]')
        tt = round(float(rest[0]), 2); txt = " ".join(rest[1:]).strip()[:1000]
        ci = next((i for i, c in enumerate(caps["cards"]) if c["s"] - 0.05 <= tt <= c["e"] + 0.05), None)
        if px is not None and py is not None: pin = {"x": float(px), "y": float(py)}
        nid = next_note_id(notes)
        notes.append({"id": nid, "t": tt, "card": ci, "text": txt, "pin": pin, "by": "claude", "kind": kind, "who": "Claude",
                      "status": "done" if kind == "info" else "ask", "at": time.strftime("%Y-%m-%d %H:%M")})
        wj(path, notes); print("انضافت ملاحظتك #%d عند %.2f ث (%s). تطلع له بالاستوديو بتبويب الملاحظات%s." % (nid, tt, kind, "" if kind == "info" else "، وينتظر رده: موافق أو لا أو رد مكتوب"))
        try: say(work, "تركت لك ملاحظة عند %.1f ث: %s" % (tt, txt[:120]), "info")
        except Exception: pass
        return
    if sub == "auto":   # 4.29
        n_ = notes_auto(work); print("انضافت %d ملاحظة «لازم تعدّلها»" % n_ if n_ else "ما لقيت شي صعب ينقرا أو ما وضح"); return
    if sub == "list":
        todo = [n for n in notes if n.get("status") not in ("done", "ask")]; wait = [n for n in notes if n.get("status") == "ask"]
        if wait: print("اقتراحاتك اللي ما رد عليها بعد (لا تنفّذها قبل رده): " + " · ".join("#%s عند %.1f ث" % (n["id"], n["t"]) for n in wait) + "\n")
        if not todo: print("ما فيه ملاحظات مفتوحة."); return
        for n in todo:
            if n.get("by") == "claude":
                print("#%s  عند %.2f ث  (اقتراحك)\n   اقترحت: %s\n   رده: %s" % (n["id"], n["t"], n["text"], n.get("answer") or "—")); continue
            ci = n.get("card"); ctx = card_key(caps["cards"][ci]) if isinstance(ci, int) and 0 <= ci < len(caps["cards"]) else ""
            pin = n.get("pin"); pin_s = (" · المؤشر على الشاشة: x=%d y=%d (من 1080×1920)" % (pin["x"] * 1080, pin["y"] * 1920)) if pin else ""
            print("#%s  عند %.2f ث%s\n   الملاحظة: %s\n   الجملة: %s%s" % (n["id"], n["t"], pin_s, n["text"], ctx or "—", ("\n   لقطة: " + J(work, n["img"])) if n.get("img") else ""))
        print("\nبعد كل ملاحظة تنفّذها: python hs.py notes <work> done <id> \"وش سويت\"")
    elif sub in ("done", "reopen"):
        for n in notes:
            if str(n["id"]) == str(args[1]):
                n["status"] = "done" if sub == "done" else "open"
                if sub == "done": n["reply"] = " ".join(args[2:]); n["doneAt"] = time.strftime("%Y-%m-%d %H:%M")
                wj(path, notes); print("تم:", args[1], n["status"]); return
        sys.exit("ما لقيت ملاحظة برقم " + str(args[1]))
    else: sys.exit("notes: list | add <ثانية> \"…\" [--kind suggest|question|info] | done <id> \"…\" | reopen <id>")
def cmd_tr(work, args):
    sp = J(work, "studio.json"); st = load_studio(work); hs = hs_of(st); en = hs.setdefault("en", {}); mp = en.setdefault("map", {})
    caps = rj(J(work, "caps.json")); sub = args[0] if args else "export"
    if sub == "export":
        pod = hs.get("pod") or {}
        if pod.get("on") and pod.get("lang", "en") != "ar":
            out = [{"i": i, "src": card_key(c), "tr": mp.get(card_key(c), "")} for i, c in enumerate(caps["cards"])]
            print("# بودكاست مترجم: اكتب بخانة tr الترجمة العربية لكل جملة، فصحى سهلة وقصيرة تنقرا بنظرة، بنفس المعنى بدون زيادة.", file=sys.stderr)
        else: out = [{"i": i, "ar": card_key(c), "en": mp.get(card_key(c), "")} for i, c in enumerate(caps["cards"])]
        print(json.dumps(out, ensure_ascii=False, indent=1)); print("\n# ناقص ترجمة: %d من %d" % (sum(1 for o in out if not (o.get("en") or o.get("tr"))), len(out)), file=sys.stderr)
    elif sub == "import":
        data = rj(args[1]); n = 0
        items = data.items() if isinstance(data, dict) else [((o.get("src") or o.get("ar") or card_key(caps["cards"][o["i"]])), o.get("tr") or o.get("en", "")) for o in data]
        for ar, e in items:
            if e and e.strip(): mp[ar] = e.strip(); n += 1
        en["on"] = True; hs.setdefault("cap", {})["on"] = True; wj(sp, st); print("انحفظت %d ترجمة · الترجمة شغّالة" % n)
    else: sys.exit("tr: export | import <file.json>")
def cmd_set(work, args):
    sp = J(work, "studio.json"); st = load_studio(work); hs = hs_of(st)
    for k, val in parse_kv(args).items():
        if k.startswith("outro."): st.setdefault("outro", {})[k[6:]] = val; continue
        cur = hs; parts = k.split(".")
        for p in parts[:-1]: cur = cur.setdefault(p, {})
        cur[parts[-1]] = val
    wj(sp, st); print(json.dumps({k: v for k, v in hs.items() if k in ("cap", "en", "mix", "hooks", "check")}, ensure_ascii=False)[:900])
MG_KINDS = ("stat", "slam", "check", "steps", "callout", "quote", "ring", "compare", "sting", "logo")
MG_ALL = MG_KINDS + ("stretch", "rec", "notif", "search", "apps", "articles", "mosaic", "rewind", "ba", "freeze")   # 4.36: الطرفية تقبل موشن 4.28 والتجميد بعد
FREEZE_STYLES = ("flash", "photo", "comic", "film")
ANNO_KINDS = ("ring", "spots", "route", "path", "wave", "tap", "boxes", "tags", "screen", "spinner", "arrow", "scribble", "underline", "highlight", "cross", "check", "lens", "spotlight", "blur", "bubble", "frame", "scan", "burst", "stars", "price")
# ── 4.29: حركة بالمفاتيح (keyframes): نفس حساب ext.js والاستوديو، عشان Claude يقدر يحطها من الطرفية ──
KF_TYPES = ("text", "image", "char", "lt", "mark", "draw")
KF_EASES = ("smooth", "linear", "back", "hold")
KF_PRESETS = ("across", "grow", "rise", "spin", "pulse", "sway")
KF_DEF = {"dx": 0.0, "dy": 0.0, "s": 1.0, "r": 0.0, "o": 1.0}
def kf_ok(L): return isinstance(L, dict) and L.get("type") in KF_TYPES and not (L.get("type") == "image" and L.get("fit") == "cover")
def kf_ease(e, k):
    k = max(0.0, min(1.0, k))
    if e == "linear": return k
    if e == "hold": return 1.0 if k >= 1 else 0.0
    if e == "back": c1 = 1.70158; c3 = c1 + 1; return 1 + c3 * (k - 1) ** 3 + c1 * (k - 1) ** 2
    return 4 * k ** 3 if k < 0.5 else 1 - (-2 * k + 2) ** 3 / 2
def kf_val(K, u):
    """القيم عند ثانية u من بداية الطبقة (نفس kfVal بـ ext.js)."""
    K = sorted(K or [], key=lambda k: float(k["t"])); one = lambda k: {f: (float(k[f]) if k.get(f) is not None else d) for f, d in KF_DEF.items()}
    if not K: return dict(KF_DEF)
    if u <= float(K[0]["t"]): return one(K[0])
    if u >= float(K[-1]["t"]): return one(K[-1])
    i = 0
    while i < len(K) - 2 and u >= float(K[i + 1]["t"]): i += 1
    a, b = K[i], K[i + 1]; k = kf_ease(a.get("e") or "smooth", (u - float(a["t"])) / max(1e-6, float(b["t"]) - float(a["t"])))
    A, B = one(a), one(b); o = {f: A[f] + (B[f] - A[f]) * k for f in A}; o["o"] = max(0.0, min(1.0, o["o"])); o["s"] = max(0.02, o["s"]); return o
def kf_pivot(L):
    T, x, y = L.get("type"), L.get("x"), L.get("y"); X = lambda v, d: (d if v is None else float(v))
    if T == "char": return X(x, 0.2) * 1080, X(y, 0.62) * 1920
    if T == "image": return X(x, 0.5) * 1080, X(y, 0.28 if L.get("fit") == "card" else 0.36 if L.get("frame") in ("browser", "post") else 0.35) * 1920
    if T == "lt": return (0.72 if (L.get("side") or "right") == "right" else 0.28) * 1080, X(y, 0.7) * 1920
    if T == "mark": return X(x, 0.5) * 1080, X(y, 0.4) * 1920
    if T == "draw": return X(x, 0.5) * 1080, X(y, 0.5) * 1920
    return X(x, 0.5) * 1080, X(y, 0.3) * 1920
def kf_preset(L, name):
    D = max(0.3, round(float(L["e"]) - float(L["s"]), 3)); m = round(min(0.6, D / 2), 3); px, _ = kf_pivot(L)
    K = {"across": [{"t": 0, "dx": round(1080 - px + 360), "e": "linear"}, {"t": D, "dx": round(-px - 360)}],
         "grow": [{"t": 0, "s": 1}, {"t": D, "s": 1.25}],
         "rise": [{"t": 0, "dy": 180, "o": 0}, {"t": m, "dy": 0, "o": 1, "e": "linear"}, {"t": D, "dy": -60}],
         "spin": [{"t": 0, "r": -180, "s": 0.3, "e": "back"}, {"t": m, "r": 0, "s": 1}],
         "pulse": [{"t": round(min(D, i * 0.5), 3), "s": 1.12 if i % 2 else 1} for i in range(max(2, int(D / 0.5) + 1))],
         "sway": [{"t": round(min(D, i * 0.8), 3), "r": 6 if i % 2 else -6, "dy": -14 if i % 2 else 0} for i in range(max(2, int(D / 0.8) + 1))]}.get(name)
    if K is None: raise ValueError("الحركة الجاهزة لازم: " + " | ".join(KF_PRESETS))
    L["kf"] = [{**{"dx": 0, "dy": 0, "s": 1, "r": 0, "o": 1, "e": "smooth"}, **k} for k in K]; return L["kf"]
def kf_set(L, at, kv):
    """مفتاح عند ثانية at بالتايم لاين (مو من بداية الطبقة). لو فيه مفتاح بنفس الفريم يتعدّل."""
    u = round(max(0.0, min(float(L["e"]) - float(L["s"]), float(at) - float(L["s"]))), 3); K = sorted(L.get("kf") or [], key=lambda k: float(k["t"]))
    hit = next((k for k in K if abs(float(k["t"]) - u) <= 1 / 60 + 1e-6), None)
    if not hit:
        v = kf_val(K, u); hit = {"t": u, "dx": round(v["dx"]), "dy": round(v["dy"]), "s": round(v["s"], 3), "r": round(v["r"], 1), "o": round(v["o"], 3), "e": "smooth"}; K.append(hit)
    for f, x in kv.items():
        if f == "e":
            if x not in KF_EASES: raise ValueError("e لازم: " + " | ".join(KF_EASES))
            hit["e"] = x
        elif f in KF_DEF: hit[f] = round(float(x), 3)
        else: raise ValueError("المفتاح يقبل: dx dy s r o e")
    L["kf"] = sorted(K, key=lambda k: float(k["t"])); return hit
def cmd_kf(work, args):
    """hs kf <work> <id> list | add <ث> [dx=… dy=… s=… r=… o=… e=smooth|linear|back|hold] | rm <ث|all> | preset across|grow|rise|spin|pulse|sway"""
    st = load_studio(work); Ls = hs_of(st).setdefault("layers", [])
    if not args: sys.exit(cmd_kf.__doc__)
    L = next((x for x in Ls if x.get("id") == args[0]), None) or sys.exit("ما لقيت الطبقة " + args[0])
    if not kf_ok(L): sys.exit("الحركة بالمفاتيح للطبقات: " + " · ".join(KF_TYPES) + " (والصورة ملء الشاشة لا)")
    sub = args[1] if len(args) > 1 else "list"
    try:
        if sub == "list":
            K = sorted(L.get("kf") or [], key=lambda k: float(k["t"]))
            for k in K: print("%6.2f ث  dx=%-5g dy=%-5g s=%-5g r=%-5g o=%-4g %s" % (float(L["s"]) + float(k["t"]), k.get("dx", 0), k.get("dy", 0), k.get("s", 1), k.get("r", 0), k.get("o", 1), k.get("e", "smooth")))
            if not K: print("ما فيه مفاتيح على %s." % L["id"])
            return
        if sub == "add" and len(args) > 2: k = kf_set(L, float(args[2]), parse_kv(args[3:])); msg = "مفتاح عند %.2f ث" % (float(L["s"]) + k["t"])
        elif sub == "rm" and len(args) > 2:
            if args[2] == "all": L.pop("kf", None); msg = "انمسحت المفاتيح"
            else:
                u = float(args[2]) - float(L["s"]); K = [k for k in (L.get("kf") or []) if abs(float(k["t"]) - u) > 1 / 60 + 1e-6]
                if len(K) == len(L.get("kf") or []): sys.exit("ما فيه مفتاح عند هالثانية")
                if K: L["kf"] = K
                else: L.pop("kf", None)
                msg = "انحذف المفتاح"
        elif sub == "preset" and len(args) > 2: kf_preset(L, args[2]); msg = "حركة %s على مدة الطبقة (%d مفتاح)" % (args[2], len(L["kf"]))
        else: sys.exit(cmd_kf.__doc__)
    except ValueError as e: sys.exit(str(e))
    wj(J(work, "studio.json"), st); print("تم %s: %s" % (L["id"], msg))
def cmd_layer(work, args):
    sp = J(work, "studio.json"); st = load_studio(work); hs = hs_of(st); Ls = hs.setdefault("layers", []); sub = args[0] if args else "list"
    if sub == "list":
        for L in Ls: print("%-4s %-5s %6.2f-%6.2f  %s" % (L["id"], L["type"], L["s"], L["e"], json.dumps({k: v for k, v in L.items() if k not in ("id", "type", "s", "e")}, ensure_ascii=False)[:150]))
        if not Ls: print("ما فيه طبقات.")
        return
    if sub == "add":
        o = parse_kv(args[1:])
        if o.get("type") not in ("text", "image", "char", "fx", "split", "viz", "cover", "bg", "behind", "pip", "mark", "cursor", "lt", "collage", "kinetic", "desk", "draw", "mg", "anno"): sys.exit("type لازم: anno | mg | text | image | char | fx | split | viz | cover | bg | behind | pip | mark | cursor | lt | kinetic | desk | collage | draw")
        if o["type"] == "mg" and o.get("kind") not in MG_ALL: sys.exit("kind لازم: " + " | ".join(MG_ALL))
        if o["type"] == "mg" and o.get("kind") == "freeze":   # 4.36: تجميد اللقطة
            if o.setdefault("style", "flash") not in FREEZE_STYLES: sys.exit("style لازم: " + " | ".join(FREEZE_STYLES))
            o.setdefault("track", 1); o.setdefault("label", "")
            if "e" not in o: o["e"] = round(float(o.get("s", 0)) + 2.2, 3)
        if o["type"] == "anno":   # 4.15: تعليق على الصورة
            if o.get("kind", "ring") not in ANNO_KINDS: sys.exit("kind لازم: " + " | ".join(ANNO_KINDS))
            o.setdefault("kind", "ring"); o.setdefault("anim", "none"); o.setdefault("track", 1)
        if o["type"] in ("split", "viz", "pip"):
            for k2, v2 in (hs.get("cardDefault") or {}).items(): o.setdefault(k2, v2) if not (k2 == "deco" and o["type"] == "viz") else None
        for k in ("text", "title"):
            if isinstance(o.get(k), str): o[k] = o[k].replace("\\n", "\n")
        o.setdefault("s", 0); o.setdefault("e", float(o["s"]) + ({"split": 5, "viz": 5, "cover": 0.9, "pip": 5, "collage": 4, "mark": 2.5, "lt": 4, "kinetic": 3, "desk": 4, "mg": 3.5}.get(o["type"], 3))); o["id"] = new_id(Ls); o.setdefault("track", {"fx": 2, "text": 1, "split": 2, "viz": 2, "cover": 2, "behind": 1, "mark": 1, "cursor": 1, "lt": 1, "collage": 2, "pip": 2, "kinetic": 2, "desk": 1}.get(o["type"], 0)); Ls.append(o); wj(sp, st); print(o["id"])
        if o["type"] in ("bg", "behind", "split", "pip") or (o["type"] == "viz"):
            try: vision_ensure(work)
            except Exception as e: print("تنبيه: " + str(e)[:160])
        return
    L = next((x for x in Ls if x["id"] == (args[1] if len(args) > 1 else "")), None) or sys.exit("ما لقيت الطبقة")
    if sub == "set":
        kv = parse_kv(args[2:])
        for k in ("text", "title"):
            if isinstance(kv.get(k), str): kv[k] = kv[k].replace("\\n", "\n")
        L.update(kv); wj(sp, st); print("تم:", L["id"])
        if L.get("type") in ("bg", "behind"):
            try: vision_ensure(work)
            except Exception as e: print("تنبيه: " + str(e)[:160])
    elif sub == "rm": Ls.remove(L); wj(sp, st); print("انحذفت:", L["id"])
    else: sys.exit("layer: list | add k=v … | set <id> k=v … | rm <id>")
def cmd_hook(work, args):
    sp = J(work, "studio.json"); st = load_studio(work); hk = hs_of(st).setdefault("hooks", {"dur": 2.6, "style": "box", "active": 0, "items": []}); sub = args[0] if args else ""
    if sub == "set": hk["items"] = [{"text": t.replace("\\n", "\n")} for t in args[1:]]; hk["on"] = True; hk["active"] = 0
    elif sub == "active": hk["active"] = int(args[1]) - 1
    elif sub == "off": hk["on"] = False
    else: sys.exit("hook: set \"…\" \"…\" | active <n> | off")
    wj(sp, st); print(json.dumps(hk, ensure_ascii=False))
def cmd_check(work):
    c = check(work); caps = rj(J(work, "caps.json"))
    print("درجة الفحص: %d/100 · المدة %.1f ث" % (c["score"], c["total"]))
    if c["firstCap"] is not None and c["firstCap"] > 1.0: print("⚠ أول كلمة تبدأ عند %.2f ث (المفروض قبل الثانية 1)" % c["firstCap"])
    for g in c["gaps"]: print("⚠ %.1f ث بلا تغيير بصري: %.2f ← %.2f" % (g["d"], g["s"], g["e"]))
    for l in c["longCaps"]: print("⚠ الجملة %d طويلة (%d كلمة)" % (l["card"] + 1, l["n"]))
    for f in c["fillers"]: print("حشو: «%s» بالجملة %d عند %.2f" % (f["t"], f["card"] + 1, f["s"]))
    for d in c["dupes"]: print("إعادة: الجملة %d تشبه %d (%d٪)\n   %s\n   %s" % (d["a"] + 1, d["b"] + 1, d["r"] * 100, card_key(caps["cards"][d["a"]]), card_key(caps["cards"][d["b"]])))
    for tp in c.get("tips") or []: print("نصيحة: " + tp["msg"])
    OM = {"voice": "الكلام يبدأ متأخر، قرّبه لأول نص ثانية", "change": "ما فيه تغيير بصري (قطع · زوم · صورة)", "text": "ما فيه عنوان على الشاشة بأول ثانية (هوك أو نص)"}
    for m in c["open"]["miss"]: print("أول 3 ثواني: " + OM[m])
    for l in c["len"]:
        nm = PLATFORMS[l["p"]]["ar"]
        print("المدة: " + ({"over": "%s ما يقبل أكثر من %d ث، ومقطعك %.0f ث" % (nm, l["max"], c["total"]), "long": "%s الأنسب له %d-%d ث، ومقطعك %.0f ث" % (nm, l["lo"], l["hi"], c["total"]),
                            "short": "%s الأنسب له %d-%d ث، ومقطعك %.0f ث بس" % (nm, l["lo"], l["hi"], c["total"])}[l["k"]]))
    if not (c["gaps"] or c["longCaps"] or c["fillers"] or c["dupes"] or c.get("tips") or c["open"]["miss"] or c["len"]): print("ما فيه ملاحظات.")
def brand_dir(): d = os.path.join(HOME_CFG, "brands"); os.makedirs(d, exist_ok=True); return d
def brand_pack(work):
    hs = load_studio(work).get("hs") or {}; th = rj(J(work, "theme.json"), {}) or {}
    return {"cap": hs.get("cap") or {}, "en": {k: v for k, v in (hs.get("en") or {}).items() if k != "map"}, "fonts": hs.get("fonts") or [],
            "theme": {k: th[k] for k in ("bg", "ink", "acc", "clay", "mut", "font", "handle") if k in th}}
def brand_apply(work, b):
    sp = J(work, "studio.json"); st = load_studio(work); hs = hs_of(st)
    hs["cap"] = {**(hs.get("cap") or {}), **(b.get("cap") or {})}; hs["en"] = {**(hs.get("en") or {}), **(b.get("en") or {})}; wj(sp, st)
    tp = J(work, "theme.json"); th = rj(tp, {}) or {}; th.update(b.get("theme") or {}); wj(tp, th)
# ── 4.37: هوية الشخص (identity.md): Claude يكتبها مرة من ملف يرفعه أو وصف يكتبه، وتنطبق لحالها على كل مونتاج وموشن وبودكاست ──
IDENT_HEADS = ("## الألوان", "## الخطوط", "## الشعار", "## الكابشن", "## Motion Graphics", "## البودكاست", "## المونتاج العادي", "## الدعوة والنبرة", "## ممنوعات")
IDENT_FONTS = ("IBM Plex Sans Arabic", "Noto Naskh Arabic", "Noto Kufi Arabic", "Readex Pro", "El Messiri", "Reem Kufi", "Aref Ruqaa", "Cairo", "Tajawal", "Almarai", "Lalezar", "Changa", "Amiri", "Rubik", "Inter", "Montserrat", "Poppins")
IDENT_EXT = (".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".pdf", ".md", ".txt", ".ttf", ".otf", ".woff", ".woff2", ".json")
_HEX = r"#(?:[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})(?![0-9A-Fa-f])"
def _hexdark(hx, k=0.72):
    try: r, g, b = (int(hx[i:i + 2], 16) for i in (1, 3, 5)); return "#%02X%02X%02X" % (int(r * k), int(g * k), int(b * k))
    except Exception: return hx
def ident_root(): d = os.path.join(HOME_CFG, "identity"); os.makedirs(d, exist_ok=True); return d
def ident_slug(name): return re.sub(r"[^\w\-]+", "-", str(name or "").strip()).strip("-_")[:40] or "me"
def ident_dir(name): return os.path.join(ident_root(), ident_slug(name))
def ident_default(v=None):
    """الهوية الافتراضية: تنطبق على أي مشروع جديد ما اختار له هوية."""
    p = os.path.join(ident_root(), "default.txt")
    if v is not None:
        s = ident_slug(v) if v else ""; open(p, "w", encoding="utf-8").write(s); return s
    try: s = open(p, encoding="utf-8").read().strip()
    except OSError: s = ""
    return s if s and os.path.isfile(os.path.join(ident_root(), s, "identity.json")) else ""
def ident_get(name):
    if not name or name == "none": return None
    d = ident_dir(name); I = rj(os.path.join(d, "identity.json"))
    if not isinstance(I, dict): return None
    C = {"bg": "#101014", "ink": "#FFFFFF", "acc": "#F2B33D", "acc2": "", "mut": "#9A9AA5", **{k: v for k, v in (I.get("colors") or {}).items() if v}}
    if not (I.get("colors") or {}).get("ink"):   # الكتابة تعاكس الخلفية لو ما حددها
        try: C["ink"] = "#141414" if sum(int(C["bg"][i:i + 2], 16) * w for i, w in ((1, 0.2126), (3, 0.7152), (5, 0.0722))) / 255 > 0.55 else "#FFFFFF"
        except Exception: pass
    F = {"head": "", "body": "", "script": "", **(I.get("fonts") or {})}
    return {**I, "slug": os.path.basename(d), "dir": d, "md": os.path.join(d, "identity.md"), "colors": C, "fonts": F}
def ident_files(I): fd = os.path.join(I["dir"], "files"); return sorted(os.listdir(fd)) if os.path.isdir(fd) else []
def ident_list():
    dflt = ident_default(); out = []
    for s in sorted(os.listdir(ident_root())):
        I = ident_get(s) if os.path.isdir(os.path.join(ident_root(), s)) else None
        if I: out.append({"slug": I["slug"], "name": I.get("name") or I["slug"], "draft": bool(I.get("draft")), "default": I["slug"] == dflt, "colors": I["colors"], "fonts": I["fonts"], "handle": I.get("handle") or "", "cta": I.get("cta") or "", "mg": I.get("mg") or "", "files": len(ident_files(I)), "md": os.path.isfile(I["md"])})
    return out
def ident_parse(text):
    """أول قراءة للوصف بدون Claude (الألوان، الحساب، الخط، كلمة الدعوة). Claude يكمّل الباقي بـ identity.md."""
    t = str(text or ""); o = {"colors": {}, "fonts": {}, "handle": "", "cta": ""}
    def hx(h): h = h.upper(); return ("#" + "".join(c * 2 for c in h[1:])) if len(h) == 4 else h
    for key, words in (("bg", "خلفية|background|bg"), ("ink", "كتابة|نص|ink|text"), ("acc", "مميز|تمييز|accent|primary|أساسي|رئيسي")):
        m = re.search(r"(?:%s)[^#\n]{0,24}(%s)" % (words, _HEX), t, re.I)
        if m: o["colors"][key] = hx(m.group(1))
    rest = [hx(h) for h in re.findall(_HEX, t)]; rest = [h for i, h in enumerate(rest) if h not in o["colors"].values() and h not in rest[:i]]
    def lum(h): r, g, b_ = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)); return 0.2126 * r + 0.7152 * g + 0.0722 * b_
    def sat(h): v = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]; return (max(v) - min(v)) / (max(v) or 1)
    if "bg" not in o["colors"] and rest:   # بدون كلمة: الأغمق خلفية لو غامق فعلاً، والأشبع مميز
        dk = min(rest, key=lum)
        if lum(dk) < 0.2: o["colors"]["bg"] = dk; rest.remove(dk)
    if "acc" not in o["colors"] and rest: ac = max(rest, key=sat); o["colors"]["acc"] = ac; rest.remove(ac)
    if "bg" not in o["colors"] and rest: o["colors"]["bg"] = rest.pop(0)
    if rest: o["colors"]["acc2"] = rest.pop(0)
    m = re.search(r"@[A-Za-z0-9_.]{2,30}", t); o["handle"] = m.group(0).rstrip(".") if m else ""
    found = []
    for f in IDENT_FONTS:
        if re.search(r"(?<![A-Za-z])" + re.escape(f) + r"(?![A-Za-z])", t, re.I) and not any(f in g for g in found): found.append(f)
    found.sort(key=lambda f: t.lower().find(f.lower()))
    if found: o["fonts"]["head"] = found[0]; o["fonts"]["body"] = found[1] if len(found) > 1 else found[0]
    m = re.search(r"(?:الدعوة|دعوة|CTA|كلمة)[^«\"\n]{0,16}[«\"]([^»\"\n]{1,24})[»\"]", t, re.I); o["cta"] = m.group(1).strip() if m else ""
    return o
def ident_md_draft(I, text=""):
    C, F = I["colors"], I["fonts"]; fs = ident_files(I)
    L = ["# هوية %s" % (I.get("name") or I["slug"]), "", "> مسودة: انكتبت من وصفه بدون Claude. Claude يكمّلها أول مرة يشتغل على مقطع له (الدليل: engine/references/identity.md)، وبعدها: hs identity check %s" % I["slug"], "",
         "سطر الهوية: (مين هو ووش يقدّم، بجملة وحدة)", "",
         "## الألوان", "", "| الدور | اللون | وين |", "|---|---|---|",
         "| الخلفية | %s | خلفية الكروت والموشن (تقريباً 60%%) |" % C["bg"], "| الكتابة | %s | النصوص (30%%) |" % C["ink"], "| المميز | %s | كلمة وحدة بالسطر، الأزرار، الدعوة (10%%) |" % C["acc"]]
    if C.get("acc2"): L.append("| مميز ثاني | %s | للرسوم بس، مو للنص |" % C["acc2"])
    L += ["", "## الخطوط", "", "- العنوان: " + (F.get("head") or "Cairo 800"), "- الكابشن والنص: " + (F.get("body") or "Tajawal 700"), "- كلمة بخط اليد: " + (F.get("script") or "Aref Ruqaa"), "",
          "## الشعار", "", "- الملف: " + (I.get("logo") or "ما فيه بعد"), "- مكانه: ختم بالنهاية (`mg sting brand=logo`) وعلامة صغيرة لو طلبها", "",
          "## الكابشن", "", "- الكلمة المنطوقة والمهمة بلون المميز " + C["acc"], "- الشكل الباقي من صفحة الأسئلة", "",
          "## Motion Graphics", "", "- القالب المفضل: " + (I.get("mg") or "MG-05 متكلم + إدخالات موشن (engine/references/motion-graphics.md)"), "- لون مميز واحد، 2 إلى 3 أنماط حركة", "",
          "## البودكاست", "", "- صندوق اسم المتكلم: " + ((I.get("pod") or {}).get("nameBg") or C["bg"]), "- الكلمة المهمة بالكابشن: " + C["acc"], "",
          "## المونتاج العادي", "", "- الهوك وكروت الشرح بنفس الألوان والخطوط", "",
          "## الدعوة والنبرة", "", "- كلمة الدعوة: " + (I.get("cta") or "(كلمة وحدة ثابتة، نفس الإملاء بكل مكان)"), "- الحساب: " + (I.get("handle") or "ما فيه"), "",
          "## ممنوعات", "", "- لون مميز ثاني بالنص، ونص فوق نص", "",
          "## مصدر الهوية", "", "- طلبه: " + (re.sub(r"\s+", " ", str(text or "")).strip()[:800] or "ما كتب وصف"), "- الملفات: " + ("، ".join("files/" + f for f in fs) or "ما فيه")]
    return "\n".join(L) + "\n"
def ident_add_file(name, fname, raw):
    b = os.path.basename(str(fname or "file")); safe = re.sub(r"[^\w.\- ]+", "_", b)[:80] or "file"
    if not safe.lower().endswith(IDENT_EXT): raise ValueError("صيغة الملف غير مدعومة (صور، PDF، MD، خطوط)")
    if len(raw) > 40 * 1024 * 1024: raise ValueError("الملف أكبر من 40 ميقا")
    fd = os.path.join(ident_dir(name), "files"); os.makedirs(fd, exist_ok=True); open(os.path.join(fd, safe), "wb").write(raw); return "files/" + safe
def ident_adopt(key, name):
    """الملفات اللي انرفعت بمفتاح مؤقت (قبل ما يكتب الاسم) تنتقل لمجلد الهوية."""
    if not key or ident_slug(key) == ident_slug(name): return
    src = os.path.join(ident_dir(key), "files")
    if os.path.isdir(src):
        dst = os.path.join(ident_dir(name), "files"); os.makedirs(dst, exist_ok=True)
        for f in os.listdir(src): shutil.move(os.path.join(src, f), os.path.join(dst, f))
    if not os.path.isfile(os.path.join(ident_dir(key), "identity.json")): shutil.rmtree(ident_dir(key), ignore_errors=True)
def ident_new(name, text="", files=(), default=None):
    """ينشئ الهوية أو يزيد عليها: الملفات بـ files/، والطلب بـ request.md، وقراءة أولى للألوان والخط والحساب. identity.md مسودة لين يكملها Claude."""
    d = ident_dir(name); fd = os.path.join(d, "files"); os.makedirs(fd, exist_ok=True)
    for f in files or []:
        if os.path.isfile(f): shutil.copy2(f, os.path.join(fd, os.path.basename(f)))
    old = rj(os.path.join(d, "identity.json")) or {}; P = ident_parse(text)
    I = {**old, "name": (str(name).strip()[:60] or old.get("name") or os.path.basename(d))}
    I["colors"] = {**(old.get("colors") or {}), **P["colors"]}; I["fonts"] = {**(old.get("fonts") or {}), **{k: v for k, v in P["fonts"].items() if v}}
    for k in ("handle", "cta"):
        if P.get(k): I[k] = P[k]
    fl = sorted(os.listdir(fd)); imgs = [x for x in fl if x.lower().endswith((".png", ".svg", ".webp", ".jpg", ".jpeg"))]
    lg = next((x for x in imgs if re.search(r"logo|شعار", x, re.I)), imgs[0] if len(imgs) == 1 else "")
    if lg and not I.get("logo"): I["logo"] = "files/" + lg
    I["fontFiles"] = ["files/" + x for x in fl if x.lower().endswith((".ttf", ".otf", ".woff", ".woff2"))]
    md = os.path.join(d, "identity.md"); I["draft"] = bool(old.get("draft", True)) or not os.path.isfile(md); I["updated"] = int(time.time())
    if str(text or "").strip():
        with open(os.path.join(d, "request.md"), "a", encoding="utf-8") as f: f.write("\n## %s\n\n%s\n" % (time.strftime("%Y-%m-%d %H:%M"), str(text).strip()))
    wj(os.path.join(d, "identity.json"), I); G = ident_get(name)
    if not os.path.isfile(md) or I["draft"]: open(md, "w", encoding="utf-8").write(ident_md_draft(G, text or (open(os.path.join(d, "request.md"), encoding="utf-8").read() if os.path.isfile(os.path.join(d, "request.md")) else "")))
    if default or (default is None and not ident_default()): ident_default(G["slug"])
    return G
def ident_check(name):
    """يفحص identity.md: كل الأقسام موجودة، ما هي مسودة، والألوان صحيحة. لو سليمة تنشال علامة المسودة."""
    I = ident_get(name)
    if not I: return False, ["ما لقيت الهوية: %s" % name]
    md = open(I["md"], encoding="utf-8").read() if os.path.isfile(I["md"]) else ""; miss = []
    if not md: miss.append("identity.md مو موجود")
    miss += ["قسم ناقص: " + h for h in IDENT_HEADS if md and h not in md]
    if "> مسودة" in md: miss.append("لسه مسودة: اكتب سطر الهوية وكمّل الأقسام وشيل سطر «> مسودة»")
    miss += ["لون غلط: %s=%s" % (k, v) for k, v in I["colors"].items() if v and not re.fullmatch(r"#[0-9A-Fa-f]{6}", str(v))]
    if not miss and I.get("draft"):
        J_ = rj(os.path.join(I["dir"], "identity.json")) or {}; J_["draft"] = False; wj(os.path.join(I["dir"], "identity.json"), J_)
    return not miss, miss
def ident_pick(work, want=None):
    """أي هوية تنطبق: اللي اختارها («none» = بدون) ← المحفوظة بالمشروع ← الافتراضية."""
    if want == "none": return None
    return ident_get(want) or ident_get(hs_of(load_studio(work)).get("identity")) or (None if hs_of(load_studio(work)).get("identity") == "none" else ident_get(ident_default()))
def ident_apply(work, name=None):
    """يطبّق الهوية على المشروع: ألوان theme.json، خط ولون الكابشن، الحساب، كلمة الدعوة، الشعار، صندوق اسم البودكاست، والخطوط المرفوعة."""
    I = ident_pick(work, name)
    if not I: return []
    C, F = I["colors"], I["fonts"]
    tp = J(work, "theme.json"); th = rj(tp, {}) or {}
    th.update({"bg": C["bg"], "ink": C["ink"], "acc": C["acc"], "clay": _hexdark(C["acc"]), "mut": C.get("mut") or "#9A9AA5"})
    if I.get("handle"): th["handle"] = I["handle"]
    if F.get("head"): th["font"] = F["head"]
    wj(tp, th)
    st = load_studio(work); hs = hs_of(st); hs["identity"] = I["slug"]
    for rel in I.get("fontFiles") or []:
        src = os.path.join(I["dir"], rel)
        if not os.path.isfile(src): continue
        os.makedirs(J(work, "fonts"), exist_ok=True); b = os.path.basename(src); shutil.copy2(src, J(work, "fonts", b)); fl = hs.setdefault("fonts", [])
        if not any(x.get("file") == b for x in fl): fl.append({"name": os.path.splitext(b)[0], "file": b})
    cap = hs.setdefault("cap", {}); cap["active"] = C["acc"]
    if F.get("body"): cap["font"] = F["body"]
    if I.get("logo") and os.path.isfile(os.path.join(I["dir"], I["logo"])):
        os.makedirs(J(work, "assets"), exist_ok=True); lg = "assets/identity-logo" + os.path.splitext(I["logo"])[1].lower(); shutil.copy2(os.path.join(I["dir"], I["logo"]), J(work, lg)); hs["identityLogo"] = lg
    if I.get("cta"):
        ot = st.setdefault("outro", {})
        if not ot.get("word"): ot["word"] = I["cta"]
    nb = (I.get("pod") or {}).get("nameBg") or C["bg"]
    for L in hs.get("layers") or []:
        if L.get("auto") in ("name", "host") and L.get("type") == "text":
            L["bgColor"] = nb
            if F.get("head"): L["font"] = F["head"]
    wj(J(work, "studio.json"), st)
    return ["الهوية: %s%s" % (I.get("name") or I["slug"], " (مسودة، Claude يكمّلها)" if I.get("draft") else "")]
def ident_task(I):
    """سطر مهمة لـ Claude لو الهوية لسه مسودة."""
    if not I or not I.get("draft"): return ""
    return ("الهوية «%s» لسه مسودة: اقرأ engine/references/identity.md، وطلبه (%s)، وملفاته (%s)، واكتب %s كامل (الألوان والخطوط والشعار والكابشن والموشن والبودكاست والدعوة)، "
            "وحدّث الألوان والخطوط: hs identity set %s colors.acc=#… fonts.head=… cta=…، ثم hs identity check %s لين يطلع سليم. بعدها hs identity apply <work>") % (
            I.get("name") or I["slug"], os.path.join(I["dir"], "request.md"), os.path.join(I["dir"], "files"), I["md"], I["slug"], I["slug"])
def cmd_identity(args):
    sub = args[0] if args else "list"; rest = args[1:]
    if sub == "list":
        L = ident_list()
        if not L: print("ما فيه هويات. سوّ وحدة: hs identity new \"الاسم\" --text \"وصفها\" [--file شعار.png]"); return
        for x in L: print("%s %-18s %s · %s%s%s" % ("★" if x["default"] else " ", x["slug"], x["colors"]["acc"], x["fonts"].get("head") or "بدون خط", " · مسودة" if x["draft"] else "", (" · " + x["handle"]) if x["handle"] else ""))
        return
    if sub == "new":
        if not rest: sys.exit('identity new "الاسم" [--text "الوصف"] [--file ملف]... [--default]')
        text, files, i = "", [], 1
        while i < len(rest):
            if rest[i] == "--text" and i + 1 < len(rest): text = rest[i + 1]; i += 2
            elif rest[i] == "--file" and i + 1 < len(rest): files.append(rest[i + 1]); i += 2
            else: i += 1
        I = ident_new(rest[0], text, files, default=True if "--default" in rest else None); print("انحفظت الهوية:", I["slug"], "·", I["md"]); t = ident_task(I)
        if t: print("□ " + t)
        return
    I = ident_get(rest[0]) if rest else ident_get(ident_default())
    if sub in ("show", "path"):
        if not I: sys.exit("ما لقيت الهوية. hs identity list")
        if sub == "path": print(I["dir"]); return
        print(json.dumps({k: I[k] for k in ("slug", "name", "colors", "fonts", "handle", "cta", "logo", "mg", "draft") if k in I}, ensure_ascii=False, indent=1)); print("الملف:", I["md"])
        if os.path.isfile(I["md"]): print(open(I["md"], encoding="utf-8").read())
        return
    if sub == "set":
        if not I: sys.exit("identity set <الاسم> colors.acc=#E8202A fonts.head=Cairo cta=ستوديو handle=@x mg=MG-05 logo=files/logo.png pod.nameBg=#141413")
        jp = os.path.join(I["dir"], "identity.json"); J_ = rj(jp, {}) or {}
        for k, v in parse_kv(rest[1:]).items():
            cur = J_; ps = k.split(".")
            for p_ in ps[:-1]: cur = cur.setdefault(p_, {})
            cur[ps[-1]] = (str(v).upper() if re.fullmatch(_HEX, str(v)) else v) if ps[-1] != "draft" else str(v).lower() in ("1", "true", "yes")
        J_["updated"] = int(time.time()); wj(jp, J_); print("تحدّثت:", I["slug"]); return
    if sub == "check":
        ok, miss = ident_check(rest[0] if rest else ident_default())
        print("سليمة: جاهزة لكل مونتاج وموشن وبودكاست" if ok else "ناقص:\n  " + "\n  ".join(miss)); sys.exit(0 if ok else 4)
    if sub == "default":
        if not I: sys.exit("ما لقيت الهوية. hs identity list")
        print("الافتراضية الحين:", ident_default(I["slug"])); return
    if sub == "apply":
        if not rest: sys.exit("identity apply <work> [الاسم]")
        w = os.path.abspath(rest[0]); done = ident_apply(w, rest[1] if len(rest) > 1 else None); print("، ".join(done) or "ما فيه هوية تنطبق (hs identity list)")
        t = ident_task(ident_pick(w, rest[1] if len(rest) > 1 else None))
        if t: print("□ " + t)
        return
    sys.exit("identity: list | new \"الاسم\" [--text …] [--file …] | show [الاسم] | set <الاسم> key=value… | check [الاسم] | default <الاسم> | apply <work> [الاسم] | path [الاسم]")
def cmd_brand(work, args):
    sub = args[0] if args else "list"
    if sub == "list": print("\n".join(sorted(os.path.splitext(f)[0] for f in os.listdir(brand_dir()))) or "ما فيه هويات محفوظة.")
    elif sub == "save": wj(os.path.join(brand_dir(), args[1] + ".json"), brand_pack(work)); print("انحفظت الهوية:", args[1])
    elif sub == "apply": brand_apply(work, rj(os.path.join(brand_dir(), args[1] + ".json")) or sys.exit("ما لقيت هوية: " + args[1])); print("انطبقت الهوية:", args[1])
    else: sys.exit("brand: list | save <name> | apply <name>")
def cmd_status(work):
    for s in stages(work): print(("✓ " if s["done"] else "· ") + s["ar"] + (" (%d٪)" % s["pct"] if s.get("pct") else ""))
    for e in activity(work)[-6:]: print("  [%s] %s" % (time.strftime("%H:%M", time.localtime(e["t"])), e["text"]))
    u = J(work, ".hs", "url.txt")
    if os.path.exists(u): print(open(u).read().strip())
def cmd_doctor(engine):
    ok = True
    def chk(name, good, hint=""):
        nonlocal ok; ok = ok and bool(good); print(("OK   " if good else "ناقص ") + name + ("" if good else "  ← " + hint))
    eng = find_engine(engine); chk("المحرّك (مجلد engine)", eng, "مجلد engine ناقص من مجلد السكل: نزّل السكل كامل من جديد")
    if eng: print("     " + eng); remember_engine(eng)
    for tool in ("ffmpeg", "ffprobe", "node"): chk(tool, shutil.which(tool), "ثبّته وأضفه للـPATH")
    try: deps_keep()
    except Exception: pass
    chk("مكتبة التصدير (puppeteer-core)", deps_ok(), "بعد موافقة المستخدم: hs deps (ينزّلها مرة وحدة لـ ~/.hojas-studio، 8 ميقا تقريباً، وتبقى مع كل تحديث)")   # 4.34
    fix_windows_path()
    if os.name == "nt": chk("Git Bash", shutil.which("bash"), "ثبّت Git for Windows")
    chk("ملفات الاستوديو", all(os.path.exists(os.path.join(HERE, f)) for f in ("studio.html", "app.js", "i18n.js", "ext.js", "qr.js", "review.html", "AGENT.md")), "أعد نسخ مجلد hojas-studio")
    wd = whisper_device()
    if wd: print(("OK   " if wd == "gpu" else "—    ") + "التفريغ (whisper) يشتغل على " + ("كرت الشاشة، سريع وما يثقل الجهاز" if wd == "gpu" else "المعالج، يثقل الجهاز وقت التفريغ  ← لو عندك كرت NVIDIA: ثبّت نسخة torch اللي تدعم CUDA (اسأل Claude يسويها لك بعد إذنك)"))
    print("     وضع الجهاز: " + ("خفيف (أولوية أقل وتخلي أنوية لك)" if cpu_mode() == "light" else "أقصى سرعة") + " · غيّره من المكتبة ← الجهاز، أو: hs hub --cpu light|full")
    print(("OK   " if find_claude() else "—    ") + "Claude Code (لزر «نفّذ» داخل الاستوديو)" + ("" if find_claude() else "  ← اختياري: بدونه تنسخ الطلب وتلصقه في المحادثة"))
    eng2 = find_engine(engine); vis = bool(eng2) and all(os.path.exists(os.path.join(eng2, "vision", f)) for f in ("vision_bundle.mjs", "wasm/vision_wasm_internal.wasm", "selfie_segmentation.tflite", "face_detection_short_range.tflite"))
    print(("OK   " if vis else "—    ") + "ملفات العين (engine/vision): مكان الوجه وقص الشخص" + ("" if vis else "  ← ناقصة: الكروت تشتغل بس بدون ضبط الوجه وبدون تغيير الخلفية"))
    print("\nالنتيجة:", "جاهز" if ok else "فيه نواقص فوق")
    if not ok: print("\nقبل ما تثبّت أي شي: اعرض على المستخدم ناتج `python hs.py tools` (وش كل أداة وليش) وخذ موافقته.")
    return ok

def port_alive(port, work=None):
    try:
        with urllib.request.urlopen("http://127.0.0.1:%d/hs/info" % port, timeout=1.2) as r: d = json.loads(r.read().decode())
        return (os.path.normcase(os.path.abspath(d.get("work", ""))) == os.path.normcase(os.path.abspath(work))) if work else True
    except Exception: return False
def port_free(port):
    s = socket.socket()
    try: s.bind(("0.0.0.0", port)); return True
    except OSError: return False
    finally: s.close()
def cmd_open(work, port, engine, browser=True):
    os.makedirs(J(work, ".hs"), exist_ok=True); eng = find_engine(engine) or sys.exit("ما لقيت مجلد engine بجنب hs.py — نزّل السكل كامل من جديد")
    if not ready(work): studio_mode_set(work, "claude", only_if_unset=True)   # 4.18: Claude بادي يمنتج ← الاستوديو يفتح على وضعه
    remember_engine(eng); use = None
    for p in range(port, port + 20):
        if port_alive(p, work): use = p; break
    if use is None:
        use = next((p for p in range(port, port + 20) if port_free(p)), None) or sys.exit("ما لقيت بورت فاضي")
        lg = open(J(work, ".hs", "server.log"), "ab"); kw = {"stdin": subprocess.DEVNULL, "stdout": lg, "stderr": lg, "cwd": work}
        if os.name == "nt": kw["creationflags"] = 0x00000008 | 0x00000200 | 0x08000000      # DETACHED · NEW_GROUP · NO_WINDOW
        else: kw["start_new_session"] = True
        subprocess.Popen([PY, os.path.abspath(__file__), "serve", work, "--port", str(use), "--engine", eng], **kw)
        for _ in range(60):
            if port_alive(use, work): break
            time.sleep(0.25)
        else: sys.exit("الخادم ما اشتغل — شوف " + J(work, ".hs", "server.log"))
    url = "http://127.0.0.1:%d/" % use
    if browser:
        try:
            import webbrowser; webbrowser.open(url)
        except Exception: pass
    print("الاستوديو شغّال: " + url); u = J(work, ".hs", "url.txt")
    if os.path.exists(u): print(open(u).read().strip().split("\n")[-1])

def voice_transcribe(work, nid, path):
    """4.3: ملاحظة صوتية من المايك ← نص (وِسبر على جهازه). لو ما فيه وِسبر تبقى الملاحظة صوت وClaude يفرّغه."""
    txt = ""
    try:
        wav = path + ".wav"; subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-ac", "1", "-ar", "16000", wav], check=True, timeout=120)
        model = hub_cfg().get("voiceModel") or "small"; od = os.path.dirname(path)
        r = subprocess.run([PY, "-m", "whisper", wav, "--model", model, "--language", "ar", "--output_format", "txt", "--output_dir", od, "--fp16", "False", "--verbose", "False"], capture_output=True, timeout=900)
        tp = os.path.splitext(wav)[0] + ".txt"
        if os.path.exists(tp): txt = open(tp, encoding="utf-8").read().strip()
    except Exception: pass
    notes = rj(J(work, "notes.json"), []) or []
    for n in notes:
        if str(n["id"]) == str(nid): n["text"] = txt or "ملاحظة صوتية (ما قدرت أفرّغها. Claude: فرّغ الملف %s بوِسبر واسمعها)" % n.get("audio", "")
    wj(J(work, "notes.json"), notes)

# ───────────────────────── الخادم ─────────────────────────
def serve(work, port, engine):
    eng = find_engine(engine) or sys.exit("ما لقيت مجلد engine بجنب hs.py — نزّل السكل كامل من جديد (شغّل: python hs.py doctor)")
    remember_engine(eng); fix_windows_path(); os.makedirs(work, exist_ok=True); changed = patch(work, quiet=True)
    D = J(work, ".hs"); os.makedirs(D, exist_ok=True)
    try: pod_repair(work)   # 4.31: مقاطع بودكاست قديمة: «&gt;&gt;» بالكابشن واسم متكلم غلط
    except Exception: pass
    sys.argv = [os.path.join(eng, "studio", "studio.py"), work, str(port)]
    spec = importlib.util.spec_from_file_location("hs_base_studio", sys.argv[0]); base = importlib.util.module_from_spec(spec); spec.loader.exec_module(base)
    _bjob = base.job
    def _hjob(kind, fn):   # 4.14: اللي تغيّره العملية (قص، إعادة بناء) يصير خطوة بالسجل أول ما تخلص
        def wrapped():
            try: fn()
            finally:
                try: hist_checkpoint(work, {"remove": "قص", "recut": "قص", "drop": "حذف جملة", "undo_cut": "ترجيع القص"}.get(kind, "تعديل"))
                except Exception: pass
        return _bjob(kind, wrapped)
    base.job = _hjob
    try: hist_checkpoint(work, "تعديل من Claude")
    except Exception: pass
    P = base.P; S = base.S
    def tok(name, n):
        p = os.path.join(D, name)
        if os.path.exists(p): return open(p).read().strip()
        v = ("%0" + str(n) + "d") % secrets.randbelow(10 ** n); open(p, "w").write(v); return v
    TOKEN = tok("token", 6); RTOKEN = tok("rtoken", 8)
    LAN = base.lan_ip(); BG = {"thumbsDone": False, "mt": None, "patched": bool(changed is not None)}
    AG = {"running": False, "proc": None, "started": 0}; VIS = {"busy": False, "what": "", "retry": time.time() + 25}; HK = {"t": 0, "patch": None, "vis": None}   # 4.4.1: العين تستنى شوي بعد الفتح عشان الصفحة تفتح بسرعة
    FAILS = {}; FAILS_ALL = [0]
    projects_remember(work); KIDS = []; _RealPopen = subprocess.Popen
    class _TrackPopen(_RealPopen):          # 4.3: نتتبّع عمليات الرسم والتصدير عشان «أوقف التصدير» من المكتبة
        def __init__(self, *a, **k): super().__init__(*a, **k); KIDS.append(self); del KIDS[:-60]
    subprocess.Popen = _TrackPopen
    def kill_tree(pr):
        try:
            if os.name == "nt": subprocess.run(["taskkill", "/F", "/T", "/PID", str(pr.pid)], capture_output=True, creationflags=0x08000000)
            else: pr.kill()
        except Exception: pass

    def peaks():
        src = P("cutz.mp4"); cp = os.path.join(D, "peaks.json")
        if not os.path.exists(src): return {"rate": 50, "p": []}
        mt = int(os.path.getmtime(src)); c = rj(cp)
        if c and c.get("mt") == mt: return c
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-vn", "-ac", "1", "-ar", "4000", "-f", "s16le", "-"], capture_output=True).stdout
        a = array.array("h"); a.frombytes(raw[: len(raw) // 2 * 2])
        if sys.byteorder == "big": a.byteswap()
        step = 80; p = [max((abs(x) for x in a[i:i + step]), default=0) for i in range(0, len(a), step)]
        mx = max(p) if p else 1; c = {"mt": mt, "rate": 50, "p": [round(x / (mx or 1), 3) for x in p]}; wj(cp, c); return c
    def build_thumbs():
        src = P("cutz.mp4"); td = os.path.join(D, "th")
        if not os.path.exists(src): BG["thumbsDone"] = True; return
        stamp = os.path.join(td, ".mt"); mt = str(int(os.path.getmtime(src)))
        if os.path.exists(stamp) and open(stamp).read() == mt and glob.glob(os.path.join(td, "*.jpg")): BG["thumbsDone"] = True; return
        if time.time() - os.path.getmtime(src) < 5: time.sleep(5)   # الفيديو لسه ينكتب
        shutil.rmtree(td, ignore_errors=True); os.makedirs(td)
        r = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-vf", "fps=1,scale=-2:128", "-q:v", "6", "-y", os.path.join(td, "%04d.jpg")], capture_output=True)
        if glob.glob(os.path.join(td, "*.jpg")): open(stamp, "w").write(mt)   # 4.4: الختم بس لو انبنت فعلاً (قبل كان يختم وهي فاضية فالتايم لاين يحمّل فريمات كاملة)
        else: print("الصور المصغّرة ما انبنت:", (r.stderr or b"")[-300:].decode("utf-8", "replace"), flush=True)
        BG["thumbsDone"] = True
    def refresh_bg(): BG["thumbsDone"] = False; threading.Thread(target=build_thumbs, daemon=True).start()
    def housekeeping():
        """يتابع الملفات: يركّب الإضافة أول ما يطلع compose.html، ويعيد بناء الصور المصغّرة لو تغيّر الفيديو.
        4.4.1: كل 4 ثواني بالكثير، وما يعيد القراءة إلا لو ملف تغيّر (كان يقرأ compose.html كامل مع كل نبضة)."""
        if time.time() - HK["t"] < 4: return
        HK["t"] = time.time()
        def mt_(f):
            try: return os.path.getmtime(f)
            except OSError: return 0
        if os.path.exists(P("compose.html")):
            k = (mt_(P("compose.html")), mt_(os.path.join(HERE, "ext.js")), mt_(P("hs-ext.js")))
            if k != HK["patch"]:
                try: patch(work, quiet=True)
                except Exception: pass
                HK["patch"] = (mt_(P("compose.html")), mt_(os.path.join(HERE, "ext.js")), mt_(P("hs-ext.js")))
        mt = int(os.path.getmtime(P("cutz.mp4"))) if os.path.exists(P("cutz.mp4")) else None
        if mt != BG["mt"]: BG["mt"] = mt; refresh_bg()
        vk = (signature(work), aux_sig(), mt_(P("vfr")))
        if not VIS["busy"] and time.time() > VIS["retry"] and not base.JOB["running"] and vk != HK["vis"] and ready(work):
            try: todo_v = face_stale(work) or bool(mask_need(work))
            except Exception: todo_v = False
            if not todo_v: HK["vis"] = vk
            if todo_v:
                VIS.update(busy=True, what="face" if face_stale(work) else "mask")
                def vgo():
                    try:
                        did = vision_ensure(work, base.log)
                        if any(x.endswith("!") for x in did) or face_stale(work) or mask_need(work): VIS["retry"] = time.time() + 90
                    except Exception as e: VIS["retry"] = time.time() + 90; base.log("vision: " + str(e)[:200])
                    finally: VIS["busy"] = False
                threading.Thread(target=vgo, daemon=True).start()
    def aux_sig():
        o = 0
        for f in ("hs-face.js", "hs-mask.js"):
            try: o += int(os.path.getmtime(P(f)) * 10)
            except OSError: pass
        return o
    AUL = threading.Lock()
    def audio_file():
        """صوت المقطع لحاله (أخف من تحميل الفيديو كامل، ويبدأ فوراً على الجوال)."""
        src = P("cutz.mp4")
        if not os.path.exists(src): return None
        f = os.path.join(D, "au-%s.m4a" % vsig(work))
        with AUL:
            if not os.path.exists(f):
                for old in glob.glob(os.path.join(D, "au-*.m4a")):
                    try: os.remove(old)
                    except OSError: pass
                tmp = f + ".part.m4a"; r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vn", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", tmp], capture_output=True)
                if r.returncode or not os.path.exists(tmp): return None
                os.replace(tmp, f)
        return f
    def sv_audio_file():
        """4.12: نفس الصوت بعد صوت الاستوديو (أو اللي عالجته من برا)، عشان تسمع اللي بيطلع بالتصدير."""
        mix = hs_of(load_studio(work)).get("mix") or {}
        src = J(work, "dub.wav") if (mix.get("dub") and os.path.isfile(J(work, "dub.wav"))) else ((sv_ext_file(work) if sv_mode(mix) == "ext" else None) or studio_voice(work, log=lambda m: None)[0])
        if not src: return None
        f = os.path.join(D, "au-sv-%s.m4a" % hashlib.md5((src + str(os.path.getmtime(src))).encode()).hexdigest()[:10])
        with AUL:
            if not os.path.exists(f):
                for old in glob.glob(os.path.join(D, "au-sv-*.m4a")):
                    try: os.remove(old)
                    except OSError: pass
                tmp = f + ".part.m4a"; r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vn", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", tmp], capture_output=True)
                if r.returncode or not os.path.exists(tmp): return None
                os.replace(tmp, f)
        return f

    def versions():
        vd = os.path.join(D, "versions"); out = []
        if os.path.isdir(vd):
            for n in sorted(os.listdir(vd), reverse=True):
                meta = rj(os.path.join(vd, n, "meta.json"), {}) or {}; out.append({"id": n, "name": meta.get("name", n), "at": meta.get("at", "")})
        return out
    def ver_restore(vid):
        vd = os.path.join(D, "versions", os.path.basename(vid))
        if not os.path.isdir(vd): raise ValueError("ما لقيت النسخة")
        old_keep = (rj(P("cut.json"), {}) or {}).get("keep"); snapshot(work, "قبل الاسترجاع (تلقائي)")
        for f in SNAP_FILES:
            if os.path.exists(os.path.join(vd, f)): shutil.copy(os.path.join(vd, f), P(f))
        return (rj(P("cut.json"), {}) or {}).get("keep") != old_keep            # تغيّر القص ← لازم إعادة بناء الفيديو
    def gen_view(q): return [{**r, "site": GEN_SITES[r["kind"]], "text": gen_prompt(r)} for r in q][-12:]
    def export_mt():
        ed = os.path.join(D, "exports"); fs = glob.glob(os.path.join(ed, "*.mp4")) if os.path.isdir(ed) else []
        return int(max(os.path.getmtime(f) for f in fs)) if fs else 0
    def hub_url():
        c = hub_cfg(); pt = c.get("port") or HUB_PORT
        try:
            with urllib.request.urlopen("http://127.0.0.1:%d/hub/api/ping" % pt, timeout=0.4) as r: return "http://127.0.0.1:%d/library" % pt if b"hub" in r.read() else None
        except Exception: return None
    def exports():
        ed = os.path.join(D, "exports"); return sorted(os.listdir(ed), reverse=True) if os.path.isdir(ed) else []
    def latest_preview():
        best = None
        for pat in ("sheet.jpg", "prev/*.jpg", "safe.jpg", "hook_sheet.jpg"):
            for f in glob.glob(P(pat)):
                m = os.path.getmtime(f)
                if not best or m > best[1]: best = (os.path.relpath(f, work).replace("\\", "/"), m)
        return {"path": best[0], "mt": int(best[1])} if best else None
    def notes_md(notes, caps):
        L = ["# ملاحظات الاستوديو", "", "المشروع: " + work, ""]
        for n in notes:
            if n.get("status") in ("done", "ask"): continue
            ci = n.get("card"); ctx = card_key(caps["cards"][ci]) if isinstance(ci, int) and 0 <= ci < len(caps["cards"]) else "—"
            L += ["## #%s عند %.2f ث" % (n["id"], n["t"]), ("- اقتراحك (Claude): " if n.get("by") == "claude" else "- الملاحظة: ") + n["text"], "- الجملة وقتها: " + ctx]
            if n.get("answer"): L.append("- رده: " + n["answer"])
            if n.get("pin"): L.append("- المؤشر على الشاشة: x=%d y=%d (من 1080×1920)" % (n["pin"]["x"] * 1080, n["pin"]["y"] * 1920))
            if n.get("img"): L.append("- لقطة: " + n["img"])
            if n.get("audio"): L.append("- تسجيل صوتي: " + n["audio"])
            L.append("")
        return "\n".join(L)
    def review(): return rj(P("review.json"), {"approved": None, "comments": []}) or {"approved": None, "comments": []}

    # ── تشغيل Claude Code من الاستوديو ──
    def agent_run(task, label, gen=False):
        exe = find_claude(); oc = None if exe else shutil.which("opencode")
        if not exe and not oc: return False, "ما لقيت Claude Code ولا OpenCode على الجهاز"
        if AG["running"]: return False, "الوكيل شغّال الحين على طلب سابق"
        if oc: return agent_run_opencode(oc, task, label)
        cmd = [exe, "-p", "Follow the task given on stdin. Work only inside the current project folder.", "--output-format", "stream-json", "--verbose",
               "--permission-mode", "acceptEdits", "--append-system-prompt-file", os.path.join(HERE, "AGENT.md"),
               "--add-dir", HERE, eng, "--allowedTools", "Bash", "Read", "Edit", "Write", "Glob", "Grep"] + (["mcp__claude-in-chrome", "mcp__higgsfield", "WebSearch", "WebFetch"] if gen else [])
        if exe.lower().endswith((".cmd", ".bat")): cmd = ["cmd", "/c"] + cmd
        full = ("مجلد المشروع: %s\nمجلد الاستوديو (hs.py): %s\nمجلد المحرّك: %s\nمفسّر بايثون: %s\n\nالمطلوب:\n%s\n" % (work, HERE, eng, PY, task))
        AG.update(running=True, started=time.time()); say(work, label, "ask")
        try: snap_id = snapshot(work, "قبل: " + label[:80])
        except Exception: snap_id = None
        cid = cmd_log_add(work, label, task, snap_id)
        def go():
            final = None
            try:
                kw = {"creationflags": 0x08000000} if os.name == "nt" else {}
                p = subprocess.Popen(cmd, cwd=work, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, **kw); AG["proc"] = p
                p.stdin.write(full.encode("utf-8")); p.stdin.close(); final = None; plain = []
                for raw in p.stdout:
                    try: ev = json.loads(raw.decode("utf-8", "replace"))
                    except Exception: plain = (plain + [raw.decode("utf-8", "replace")])[-30:]; continue
                    if ev.get("type") == "assistant":
                        for b in (ev.get("message") or {}).get("content") or []:
                            if b.get("type") == "text" and b.get("text", "").strip(): say(work, b["text"].strip(), "claude")
                            elif b.get("type") == "tool_use":
                                i = b.get("input") or {}; d = i.get("description") or i.get("command") or i.get("file_path") or i.get("pattern") or ""
                                say(work, "%s: %s" % (b.get("name"), str(d)[:160]), "tool")
                    elif ev.get("type") == "result": final = ev
                p.wait()
                cmd_log_set(cid, status="err" if (final and final.get("is_error")) or (p.returncode not in (0, None) and not final) else "done", result=str((final or {}).get("result") or "")[:800])
                if final and final.get("is_error"): say(work, claude_why(str(final.get("result", "")) + "\n" + "".join(plain), p.returncode)["msg"], "err")
                elif p.returncode not in (0, None) and not final: say(work, claude_why("".join(plain), p.returncode)["msg"], "err")
                else: say(work, "خلص Claude من الطلب.", "done")
            except Exception as e: say(work, "تعذّر تشغيل Claude: " + str(e)[:200], "err")
            finally: AG.update(running=False, proc=None)
        threading.Thread(target=go, daemon=True).start(); return True, ""

    def agent_run_opencode(exe, task, label):
        """4.1: نفس زر «نفّذ» لكن مع OpenCode (تجريبي): نمرّر تعليمات AGENT.md داخل الطلب ونعرض مخرجاته سطر سطر."""
        guide = open(os.path.join(HERE, "AGENT.md"), encoding="utf-8").read()
        full = "%s\n\nمجلد المشروع: %s\nمجلد الاستوديو (hs.py): %s\nمجلد المحرّك: %s\nمفسّر بايثون: %s\n\nالمطلوب:\n%s\n" % (guide, work, HERE, eng, PY, task)
        cmd = [exe, "run", full]
        if exe.lower().endswith((".cmd", ".bat")): cmd = ["cmd", "/c"] + cmd
        AG.update(running=True, started=time.time()); say(work, label + " (OpenCode)", "ask")
        try: cid = cmd_log_add(work, label, task, snapshot(work, "قبل: " + label[:80]))
        except Exception: cid = None
        def go():
            try:
                kw = {"creationflags": 0x08000000} if os.name == "nt" else {}
                p = subprocess.Popen(cmd, cwd=work, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, **kw); AG["proc"] = p
                for raw in p.stdout:
                    ln = re.sub(r"\x1b\[[0-9;]*[A-Za-z]", "", raw.decode("utf-8", "replace")).strip()
                    if ln: say(work, ln[:300], "claude")
                p.wait(); cmd_log_set(cid, status="done" if p.returncode == 0 else "err"); say(work, "خلص OpenCode من الطلب." if p.returncode == 0 else "OpenCode وقف (رمز %s)." % p.returncode, "done" if p.returncode == 0 else "err")
            except Exception as e: say(work, "تعذّر تشغيل OpenCode: " + str(e)[:200], "err")
            finally: AG.update(running=False, proc=None)
        threading.Thread(target=go, daemon=True).start(); return True, ""

    class HS(base.H):
        def _local(self): return self.client_address[0] in ("127.0.0.1", "::1", "localhost")
        def _q(self): return urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        def _role(self):
            if self._local(): return "owner"
            # حماية الرمز على الشبكة: 10 محاولات خاطئة من نفس الجهاز = قفل 15 دقيقة، و200 بالمجموع = قفل الشبكة لين يعاد التشغيل
            ip = self.client_address[0]; now = time.time(); f = FAILS.get(ip)
            if f and now - f[1] > 900: FAILS.pop(ip, None); f = None
            if FAILS_ALL[0] >= 200 or (f and f[0] >= 10): return None
            ck = self.headers.get("Cookie") or ""; q = self._q()
            if ("hs_k=" + TOKEN) in ck or (q.get("k") or [""])[0] == TOKEN: return "owner"
            if ("hs_r=" + RTOKEN) in ck or (q.get("r") or [""])[0] == RTOKEN: return "review"
            if q.get("k") or q.get("r") or "hs_k=" in ck or "hs_r=" in ck:
                FAILS[ip] = [(f[0] if f else 0) + 1, f[1] if f else now]; FAILS_ALL[0] += 1
                if FAILS_ALL[0] == 200: print("تنبيه: محاولات دخول خاطئة كثيرة من الشبكة، قفلت الدخول من الجوال لين تعيد تشغيل الاستوديو"); sys.stdout.flush()
            return None
        protocol_version = "HTTP/1.1"      # اتصال واحد يخدم طلبات كثيرة: بدونه التشغيل (30 فريم بالثانية) يستهلك منافذ ويندوز والاستوديو يعلّق بعد دقايق
        timeout = 75
        def end_headers(self):
            buf = b"".join(getattr(self, "_headers_buffer", [])).lower()
            if b"content-length:" not in buf and not buf.startswith(b"http/1.1 304") and not buf.startswith(b"http/1.1 204"): self.send_header("Connection", "close"); self.close_connection = True
            if b"cache-control:" not in buf: self.send_header("Cache-Control", "max-age=86400, immutable" if getattr(self, "_cache", False) else "no-store")
            self.send_header("Accept-Ranges", "bytes"); http.server.SimpleHTTPRequestHandler.end_headers(self)
        def _file(self, path, ctype, dl=None):
            b = open(path, "rb").read(); self.send_response(200); self.send_header("Content-Type", ctype)
            if dl: self.send_header("Content-Disposition", 'attachment; filename="%s"' % dl)
            self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
        def _deny(self):
            ip = self.client_address[0]; f = FAILS.get(ip); q = self._q()
            locked = FAILS_ALL[0] >= 200 or bool(f and f[0] >= 10 and time.time() - f[1] <= 900)
            b = login_html(urllib.parse.urlparse(self.path).path or "/", "بالاستوديو على الكمبيوتر (زر «الجوال»)", len(TOKEN), "الرمز غلط، جرّب مرة ثانية." if q.get("k") else "", locked).encode()
            self.send_response(403); self.send_header("Content-Type", "text/html; charset=utf-8"); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
        def _review_video(self):
            ex = exports(); return ("/hs/export/" + ex[0]) if ex else ("/ad-master.mp4" if os.path.exists(P("ad-master.mp4")) else None)
        def do_GET(self):
            u = urllib.parse.urlparse(self.path); p = u.path; q = self._q(); role = self._role()
            self._cache = bool(q.get("v")) and (p.startswith("/vfr/") or p.startswith("/hs/th/") or p.startswith("/hs/pv/") or p.startswith("/bt/") or p in ("/hs/qr.js", "/hs/app.js", "/hs/i18n.js"))
            if not role: return self._deny()
            ck = self.headers.get("Cookie") or ""
            for key, val, name in (("k", TOKEN, "hs_k"), ("r", RTOKEN, "hs_r")):
                if (q.get(key) or [""])[0] == val and not self._local() and (name + "=" + val) not in ck:
                    self.send_response(302); self.send_header("Set-Cookie", "%s=%s; Path=/; Max-Age=2592000; SameSite=Lax" % (name, val))
                    self.send_header("Location", p or "/"); self.send_header("Content-Length", "0"); self.end_headers(); return
            # ── صفحة المراجعة (العميل): صلاحيات محدودة ──
            if p == "/hs/ui-font.otf":
                f = ui_font()
                if not os.path.isfile(f): return self.send_error(404)
                b = open(f, "rb").read(); self.send_response(200); self.send_header("Content-Type", "font/otf"); self.send_header("Cache-Control", "max-age=86400"); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b); return
            if p == "/review": return self._file(os.path.join(HERE, "review.html"), "text/html; charset=utf-8")
            if p == "/hs/review_state": return self._json(200, {**review(), "video": self._review_video(), "name": os.path.basename(work.rstrip("/\\")), "owner": role == "owner"})
            if p.startswith("/hs/export/"):
                f = os.path.join(D, "exports", os.path.basename(p))
                if not os.path.isfile(f): return self.send_error(404)
                self.path = "/.hs/exports/" + os.path.basename(p); return self._ranged() if self._wants_range() else self._file(f, "video/mp4")
            if role == "review":
                if p == "/ad-master.mp4" and os.path.exists(P("ad-master.mp4")): return self._ranged() if self._wants_range() else self._file(P("ad-master.mp4"), "video/mp4")
                return self._deny()
            # ── المالك ──
            if p in ("/", "/hs", "/hs/", "/m", "/m/"):   # 4.4: السكربتات بختم نسختها فالمتصفح يخزّنها (أخف بكثير على الجوال)
                b = open(os.path.join(HERE, "studio.html"), encoding="utf-8").read()
                for f in ("qr.js", "i18n.js", "app.js"):
                    try: b = b.replace('src="/hs/%s"' % f, 'src="/hs/%s?v=%d"' % (f, int(os.path.getmtime(os.path.join(HERE, f)))))
                    except OSError: pass
                if p.startswith("/m"): b = b.replace("<body>", '<body class="m">', 1)
                b = b.encode("utf-8")
                self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.send_header("Content-Length", str(len(b))); self.send_header("Cache-Control", "no-store"); self.end_headers(); self.wfile.write(b); return
            if p in ("/hs/qr.js", "/hs/app.js", "/hs/i18n.js"): return self._file(os.path.join(HERE, os.path.basename(p)), "application/javascript; charset=utf-8")
            if p == "/hs/pulse":
                housekeeping(); since = int((q.get("since") or ["0"])[0])
                return self._json(200, {"sig": signature(work), "ready": ready(work), "mode": studio_mode(work), "brief": brief_state(work), "genPending": sum(1 for r in gen_list(work) if r["status"] != "done"), "stages": stages(work), "act": activity(work, since), "preview": latest_preview(), "vis": {"busy": VIS["busy"], "what": VIS["what"]}, "aux": aux_sig(),
                                        "job": {"running": base.JOB["running"], "kind": base.JOB["kind"], "outs": base.JOB.get("outs"), "err": base.JOB["err"]}, "agent": {"running": AG["running"], "elapsed": int(time.time() - AG["started"]) if AG["running"] else 0}})
            if p == "/hs/dub_state":   # 4.26
                Dd = dub_get(work) or {}; segs = Dd.get("segs") or []; txt = open(J(work, "dub-script.txt"), encoding="utf-8").read() if os.path.isfile(J(work, "dub-script.txt")) else ""   # Dd مو D: D مجلد الكاش حق السيرفر
                return self._json(200, {"ok": True, "has": bool(Dd), "lang": Dd.get("lang"), "name": DUB_LANGS.get(Dd.get("lang") or "", ""), "n": len(segs), "tr": sum(1 for x in segs if x.get("tr")), "aud": sum(1 for x in segs if x.get("file")), "track": bool(Dd.get("track")),
                                        "on": dub_on(work), "want": hs_of(load_studio(work)).get("dubWant") or "", "script": txt})
            if p == "/hs/vpos_info": return self._json(200, vpos_info(work))   # 4.27
            if p == "/hs/vpos_thumb":
                try: f_ = vpos_thumb(work, float((q.get("t") or ["0"])[0]))
                except Exception as e: return self._json(500, {"ok": False, "msg": str(e)[:200]})
                b_ = open(f_, "rb").read(); self.send_response(200); self.send_header("Content-Type", "image/jpeg"); self.send_header("Content-Length", str(len(b_))); self.send_header("Cache-Control", "no-store"); self.end_headers(); self.wfile.write(b_); return
            if p == "/hs/quality_preview":   # 4.25: قبل وبعد
                try: f_ = quality_preview(work, float((q.get("t") or ["0"])[0]), (q.get("level") or ["light"])[0])
                except Exception as e: return self._json(500, {"ok": False, "msg": str(e)[:200]})
                b_ = open(f_, "rb").read(); self.send_response(200); self.send_header("Content-Type", "image/jpeg"); self.send_header("Content-Length", str(len(b_))); self.send_header("Cache-Control", "no-store"); self.end_headers(); self.wfile.write(b_); return
            if p == "/hs/info":
                return self._json(200, {"version": VERSION, "vmap": media_map(work)[1], "vsig": vsig(work), "token": TOKEN, "lan": "http://%s:%d/?k=%s" % (LAN, port, TOKEN), "lanM": "http://%s:%d/m?k=%s" % (LAN, port, TOKEN), "review": "http://%s:%d/review?r=%s" % (LAN, port, RTOKEN),
                                        "work": work, "name": os.path.basename(work.rstrip("/\\")), "thumbsDone": BG["thumbsDone"], "versions": versions(), "exports": exports(), "exportMt": export_mt(), "hub": hub_url(), "title": (hs_of(load_studio(work)).get("title") or (hs_of(load_studio(work)).get("pod") or {}).get("title") or (hs_of(load_studio(work)).get("dahih") or {}).get("title") or ""),
                                        "brands": sorted(os.path.splitext(f)[0] for f in os.listdir(brand_dir())), "local": self._local(), "claude": bool(find_claude() or shutil.which("opencode")), "agent": "claude" if find_claude() else ("opencode" if shutil.which("opencode") else ""), "notify": bool(notify_cfg().get("on")), "tokenAsk": token_ask(), "gen": gen_view(gen_list(work)), "safe": safe_of((load_studio(work).get("hs") or {}).get("platforms"), *frame_of(load_studio(work).get("hs") or {})), "platforms": {k: {"safe": v["safe"], "frames": v["frames"], "best": v["best"], "max": v["max"]} for k, v in PLATFORMS.items()},
                                        "assets": sorted(f for f in os.listdir(P("assets")) if os.path.splitext(f)[1].lower() in (".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg")) if os.path.isdir(P("assets")) else [], "seams": keep_seams(work), "looks": looks_all(), "beats": rj(P("beats.json")), "music": os.path.basename(music_file(work) or ""), "sv": sv_info(work),
                                        "post": open(P("post.txt"), encoding="utf-8").read() if os.path.exists(P("post.txt")) else "", "ready": ready(work),
                                        "finals": [f for f in sorted(os.listdir(work)) if re.match(r"ad-(master|clean|hook-\d+|\d+x\d+)\.mp4$", f)]})
            if p == "/hs/notify":
                c = notify_cfg(); return self._json(200, {"on": bool(c.get("on")), "topic": c.get("topic", "") if role == "owner" else "", "sub": notify_sub(c) if c.get("topic") and role == "owner" else ""})
            if p == "/hs/peaks": return self._json(200, peaks())
            if p == "/hs/notes": return self._json(200, rj(P("notes.json"), []) or [])
            if p == "/hs/check":
                ck = check(work)
                try: ck["reqs"] = brief_reqs(work)
                except Exception as e: ck["reqs"] = []; print("brief_reqs:", e, file=sys.stderr)
                return self._json(200, ck)
            if p == "/hs/brief":
                caps = rj(P("caps.json"), {"cards": []}) or {"cards": []}; ck = check(work) if caps.get("cards") else {"fillers": [], "dupes": []}
                return self._json(200, {"ask": rj(brief_paths(work)[0], {}), "answers": rj(brief_paths(work)[1]), "last": rj(os.path.join(HOME_CFG, "last-brief.json")), "state": brief_state(work),
                                        "cards": [card_key(c) for c in caps["cards"]], "fillers": len(ck["fillers"]), "dupes": [[d["a"], d["b"]] for d in ck["dupes"]],
                                        "brands": sorted(os.path.splitext(f)[0] for f in os.listdir(brand_dir())), "name": os.path.basename(work.rstrip("/\\")), "platforms": {k: {"frames": v["frames"]} for k, v in PLATFORMS.items()}, "reqs": brief_reqs(work), "sound": sound_providers(),
                                        "ids": ident_list(), "idDefault": ident_default(), "want": {"style": hs_of(load_studio(work)).get("wantStyle") or "", "identity": hs_of(load_studio(work)).get("identity") or ""}})
            if p == "/hs/media_search":
                try: return self._json(200, {"ok": True, "items": (video_search if (q.get("kind") or [""])[0] == "video" else media_search)(work, (q.get("q") or [""])[0], 12)})
                except Exception as e: return self._json(200, {"ok": False, "msg": "البحث فشل (تأكد من النت): " + str(e)[:160], "items": []})
            if p == "/hs/retention": return self._json(200, retention(work))
            if p == "/hs/covers": return self._json(200, covers(work))
            if p == "/hs/repurpose": return self._json(200, repurpose(work))
            if p == "/hs/perf": return self._json(200, {"rows": perf_get(item_id(work)), "tokenAsk": token_ask()})
            if p == "/hs/carousel.zip":
                cd = P("carousel"); zp = os.path.join(D, "carousel.zip")
                with zipfile.ZipFile(zp, "w") as z:
                    for f in sorted(glob.glob(os.path.join(cd, "*.png"))): z.write(f, os.path.basename(f))
                    rp = rj(P("repurpose.json"), {}) or {}
                    if rp: z.writestr("thread.txt", "\n\n".join(rp.get("thread") or [])); z.writestr("youtube.txt", (rp.get("yt") or {}).get("title", "") + "\n\n" + (rp.get("yt") or {}).get("desc", ""))
                return self._file(zp, "application/zip", dl=os.path.basename(work.rstrip("/\\")) + "-carousel.zip")
            if p == "/hs/pack.zip" and os.path.exists(os.path.join(D, "pack.zip")): return self._file(os.path.join(D, "pack.zip"), "application/zip", dl=os.path.basename(work.rstrip("/\\")) + "-publish.zip")
            if p.startswith("/sfx_prev/"):
                k = os.path.splitext(os.path.basename(p))[0]
                if sfx_have(k): return self._file(sfx_path(k), "audio/wav")
            if p == "/hs/sfxlib": return self._json(200, {"items": sfx_all(), "myDir": my_dir()})
            if p == "/hs/takes": return self._json(200, tk_view(work))   # 4.10: اختيار الجمل
            if p == "/hs/steps": return self._json(200, {"steps": steps(work)})
            if p == "/hs/plan": return self._json(200, plan_view(work))
            if p in ("/hs/raw.m4a", "/hs/takes_prev.m4a"):
                os.makedirs(P(".hs"), exist_ok=True)
                if p == "/hs/raw.m4a":
                    s_, e_ = float((q.get("s") or ["0"])[0]), float((q.get("e") or ["1"])[0]); f = P(".hs", "raw-%d-%d.m4a" % (int(s_ * 100), int(e_ * 100)))
                    f = f if os.path.isfile(f) else raw_audio(work, s_, min(e_, s_ + 60), f)
                else: f = tk_preview(work, P(".hs", "takes-prev.m4a"))
                if not f: return self.send_error(404)
                self.path = "/.hs/" + os.path.basename(f); return self._ranged() if self._wants_range() else self._file(f, "audio/mp4")
            if p == "/hs/au.m4a":
                f = sv_audio_file() if (q.get("sv") or [""])[0] == "1" else audio_file()
                if not f: return self.send_error(404)
                self.path = "/.hs/" + os.path.basename(f); return self._ranged() if self._wants_range() else self._file(f, "audio/mp4")
            if p == "/hs/tools":
                tl = []
                for name, why, src, okf in TOOLS:
                    try: g = bool(okf())
                    except Exception: g = False
                    tl.append({"name": name, "why": why, "src": src, "ok": g})
                return self._json(200, {"tools": tl, "net": NET_USE})
            if p.startswith("/hs/pv/"):       # فريم معاينة مصغّر (540 عرض): أخف 4 مرات من الأصلي، والتصدير ما يستخدمه
                n = max(1, int(re.sub(r"\D", "", p) or 1)); src = P("vfr", "%05d.jpg" % n); f = os.path.join(D, "pv", "%05d.jpg" % n)
                if not os.path.exists(src): return self.send_error(404)
                try: fresh = os.path.getmtime(f) >= os.path.getmtime(src)
                except OSError: fresh = False
                if not fresh: pv_build(work)
                return self._file(f if fresh else src, "image/jpeg")
            if p.startswith("/hs/th/"):
                n = int(re.sub(r"\D", "", p) or 1); f = os.path.join(D, "th", "%04d.jpg" % max(1, n))
                if not os.path.exists(f):   # ما انبنت للحين: نعطيه فريم المعاينة المصغّر بدل الفريم الكامل
                    fn = max(1, (n - 1) * 30 + 1); f = os.path.join(D, "pv", "%05d.jpg" % fn)
                    if not os.path.exists(f): f = P("vfr", "%05d.jpg" % fn)
                return self._file(f, "image/jpeg") if os.path.exists(f) else self.send_error(404)
            if p.startswith("/hs/brand/"):
                b = rj(os.path.join(brand_dir(), os.path.basename(urllib.parse.unquote(p)) + ".json")); return self._json(200 if b else 404, b or {})
            if p.startswith("/.hs/") or p.startswith("/.studio_bak"): return self.send_error(404)
            self.path = p + (("?" + u.query) if u.query and "k=" not in u.query else "")
            return super().do_GET()
        def do_POST(self):
            p0 = urllib.parse.urlparse(self.path).path
            if p0 in ("/hs/undo", "/hs/redo") or not self._role(): return self._do_POST()
            try: hist_checkpoint(work, "تعديل من Claude")
            except Exception: pass
            try: return self._do_POST()
            finally:
                try: hist_checkpoint(work, HIST_WHY.get(p0, "تعديل"))
                except Exception: pass
        def _do_POST(self):
            role = self._role()
            if not role: return self._deny()
            p = urllib.parse.urlparse(self.path).path
            if role == "review" and p not in ("/hs/review_comment", "/hs/review_approve"): return self._deny()
            if p in ("/hs/undo", "/hs/redo"):   # 4.14: التراجع من السجل اللي على القرص
                self.rfile.read(int(self.headers.get("Content-Length") or 0))
                if base.JOB["running"]: return self._json(409, {"ok": False, "msg": "فيه عملية شغّالة، انتظرها تخلص"})
                ok, rb, why = hist_step(work, p == "/hs/undo"); u, r = hist_counts(work)
                if ok and rb:
                    def go(): rebuild_video(work, S, base.log); base.JOB["reload"] = True
                    base.job("remove", go)
                return self._json(200, {"ok": ok, "rebuild": rb, "why": why, "undo": u, "redo": r})
            if p.startswith("/api/save"):   # 4.10: قاموسك يتعلّم من تصحيحاتك للكابشن
                n_ = int(self.headers.get("Content-Length") or 0); raw_ = self.rfile.read(n_)
                if base.JOB["running"] and base.JOB["kind"] == "remove":   # 4.20: القص يعاد بناؤه: حفظ النسخة القديمة اللي بالصفحة يخرّبه
                    return self._json(409, {"ok": False, "busy": True, "msg": "القص لسه يتركّب، انتظره يخلص"})
                try:
                    d_ = json.loads(raw_ or b"{}")
                    if d_.get("caps"): gloss_learn(rj(P("caps.json"), None), d_["caps"])
                except Exception: pass
                import io as _io; self.rfile = _io.BytesIO(raw_); return super().do_POST()
            if not (p.startswith("/hs/") or p.startswith("/api/recut") or p.startswith("/api/drop") or p.startswith("/api/undo_cut") or p.startswith("/api/render")):
                return super().do_POST()
            n = int(self.headers.get("Content-Length") or 0); raw = self.rfile.read(n)
            try:
                if p == "/hs/voice_note":
                    if n > 25 * 1024 * 1024: return self._json(400, {"ok": False, "msg": "التسجيل طويل"})
                    qq = self._q(); ct = (self.headers.get("Content-Type") or "").lower(); ext = ".mp4" if "mp4" in ct or "aac" in ct else ".ogg" if "ogg" in ct else ".wav" if "wav" in ct else ".webm"
                    notes = rj(P("notes.json"), []) or []; nid = next_note_id(notes); os.makedirs(P("notes"), exist_ok=True); af = "notes/voice-%d%s" % (nid, ext); open(P(af), "wb").write(raw)
                    ci = (qq.get("card") or [""])[0]
                    note = {"id": nid, "t": round(float((qq.get("t") or ["0"])[0]), 2), "card": int(ci) if ci.isdigit() else None, "text": "(يتفرّغ صوتك…)", "audio": af, "pin": None, "status": "open",
                            "who": "أنا" if self._local() else "جوال", "at": time.strftime("%Y-%m-%d %H:%M")}
                    notes.append(note); wj(P("notes.json"), notes)
                    threading.Thread(target=voice_transcribe, args=(work, nid, P(af)), daemon=True).start()
                    return self._json(200, {"ok": True, "notes": notes, "id": nid})
                if p == "/hs/gen_import":
                    name = os.path.basename(urllib.parse.unquote(self.headers.get("X-Name") or "file")); ext = os.path.splitext(name)[1].lower()
                    if ext not in IMG_EXT + VID_EXT: return self._json(400, {"ok": False, "msg": "ارفع صورة png/jpg/webp أو مقطع mp4/mov/webm"})
                    if n > 300 * 1024 * 1024: return self._json(400, {"ok": False, "msg": "الملف أكبر من 300 ميقا"})
                    os.makedirs(D, exist_ok=True); tmp = os.path.join(D, "up" + ext); open(tmp, "wb").write(raw); at = self.headers.get("X-At")
                    res = gen_import(work, self.headers.get("X-Id") or "-", tmp, name=name, at=(float(at) if at else None), fit=self.headers.get("X-Fit") or None, log=base.log)
                    try: os.remove(tmp)
                    except OSError: pass
                    return self._json(200, {"ok": True, **res, "gen": gen_view(gen_list(work))})
                if p == "/hs/dub_track":   # 4.26: ملف دبلجة كامل يرفعه هو
                    name = os.path.basename(urllib.parse.unquote(self.headers.get("X-Name") or "dub.mp3"))
                    if not name.lower().endswith(AUD_EXT): return self._json(400, {"ok": False, "msg": "ارفع ملف صوت (mp3 · wav · m4a …)"})
                    tmp = J(work, ".hs", "up-" + re.sub(r"[^\w.\-]+", "_", name)); os.makedirs(J(work, ".hs"), exist_ok=True); open(tmp, "wb").write(raw)
                    try: dub_track(work, tmp); dub_build(work, base.log); st_ = load_studio(work); hs_of(st_).setdefault("mix", {})["dub"] = True; wj(J(work, "studio.json"), st_)
                    except Exception as e: return self._json(400, {"ok": False, "msg": str(e)[:200]})
                    finally:
                        try: os.remove(tmp)
                        except OSError: pass
                    return self._json(200, {"ok": True})
                if p == "/hs/mysfx":
                    name = os.path.basename(urllib.parse.unquote(self.headers.get("X-Name") or "sound.mp3"))
                    if not name.lower().endswith(AUD_EXT): return self._json(400, {"ok": False, "msg": "ارفع ملف صوت (mp3 · wav · m4a …)"})
                    if n > 60 * 1024 * 1024: return self._json(400, {"ok": False, "msg": "الملف أكبر من 60 ميقا"})
                    safe = re.sub(r"[^\w.\- ]+", "_", name); open(os.path.join(my_dir(), safe), "wb").write(raw); meta = my_list(); m = next((x for x in meta if x.get("file") == safe), None)
                    if not m:
                        try: os.remove(os.path.join(my_dir(), safe))
                        except OSError: pass
                        return self._json(400, {"ok": False, "msg": "ما قدرت أقرأ الملف كصوت"})
                    return self._json(200, {"ok": True, "id": m["id"], "items": sfx_all()})
                if p == "/hs/identity_file":   # 4.37: ملف الهوية (شعار، دليل PDF، صور، خطوط، MD)
                    qq = self._q()
                    try: rel = ident_add_file((qq.get("name") or ["هويتي"])[0] or "هويتي", urllib.parse.unquote(self.headers.get("X-Name") or "file"), raw)
                    except ValueError as e: return self._json(400, {"ok": False, "msg": str(e)})
                    return self._json(200, {"ok": True, "file": rel})
                if p in ("/hs/font", "/hs/asset"):
                    name = os.path.basename(urllib.parse.unquote(self.headers.get("X-Name") or "file"))
                    pat = r"\.(ttf|otf|woff2?)$" if p == "/hs/font" else r"\.(png|jpe?g|webp|gif|svg)$"
                    if not re.search(pat, name, re.I): return self._json(400, {"ok": False, "msg": "صيغة الملف غير مدعومة"})
                    if n > 40 * 1024 * 1024: return self._json(400, {"ok": False, "msg": "الملف أكبر من 40 ميقا"})
                    safe = re.sub(r"[^\w.\- ]+", "_", name); folder = "fonts" if p == "/hs/font" else "assets"; os.makedirs(P(folder), exist_ok=True); open(P(folder, safe), "wb").write(raw)
                    return self._json(200, {"ok": True, "name": os.path.splitext(safe)[0], "file": safe, "src": folder + "/" + safe})
                data = json.loads(raw or b"{}")
                # ── العميل ──
                if p == "/hs/review_comment":
                    rv = review(); cid = max([c["id"] for c in rv["comments"]] or [0]) + 1
                    rv["comments"].append({"id": cid, "t": round(float(data.get("t", 0)), 2), "who": str(data.get("who") or "عميل")[:40], "text": str(data.get("text", ""))[:800],
                                           "draw": (data.get("draw") or [])[:40], "at": time.strftime("%Y-%m-%d %H:%M"), "status": "open"})
                    wj(P("review.json"), rv); return self._json(200, {"ok": True, **rv})
                if p == "/hs/review_approve":
                    rv = review(); rv["approved"] = {"by": str(data.get("who") or "عميل")[:40], "at": time.strftime("%Y-%m-%d %H:%M")} if data.get("ok", True) else None
                    wj(P("review.json"), rv); say(work, "العميل %s اعتمد المقطع" % rv["approved"]["by"] if rv["approved"] else "انسحب الاعتماد", "info"); return self._json(200, {"ok": True, **rv})
                # ── المالك ──
                if p == "/hs/review_promote":
                    rv = review(); c = next((x for x in rv["comments"] if x["id"] == int(data["id"])), None)
                    if not c: return self._json(404, {"ok": False})
                    notes = rj(P("notes.json"), []) or []; nid = next_note_id(notes)
                    notes.append({"id": nid, "t": c["t"], "card": None, "text": c["text"], "pin": None, "status": "open", "who": c["who"], "at": time.strftime("%Y-%m-%d %H:%M")})
                    c["status"] = "promoted"; wj(P("notes.json"), notes); wj(P("review.json"), rv); return self._json(200, {"ok": True, "notes": notes, **rv})
                if p.startswith("/api/recut") or p.startswith("/api/drop") or p.startswith("/api/undo_cut"):
                    return self._json(410, {"ok": False, "msg": "استخدم /hs/remove"})
                if p == "/hs/mysfx_edit":
                    my_edit(str(data.get("id") or ""), data.get("name"), data.get("note"), bool(data.get("delete"))); return self._json(200, {"ok": True, "items": sfx_all()})
                if p == "/hs/open_sounds":
                    if not self._local(): return self._json(200, {"ok": False, "msg": "يفتح من الجهاز نفسه فقط", "dir": my_dir()})
                    try:
                        if os.name == "nt": os.startfile(my_dir())
                        else: subprocess.Popen(["open" if sys.platform == "darwin" else "xdg-open", my_dir()])
                    except Exception: pass
                    return self._json(200, {"ok": True, "dir": my_dir()})
                if p == "/hs/sfx_fetch":
                    d = json.loads(raw or b"{}"); ok, bad = sfx_fetch(d.get("ids") or None)
                    return self._json(200, {"ok": not bad, "got": ok, "bad": bad, "msg": ("ما قدرت أنزّل %d صوت. تأكد من النت." % len(bad)) if bad else ""})
                if p in ("/hs/cover_save", "/hs/carousel_save"):   # 4.5: الصورة ترتسم بالمتصفح بخط المقطع وتنحفظ هنا
                    m = re.match(r"data:image/(png|jpeg);base64,(.+)$", str(data.get("data") or ""), re.S)
                    if not m: return self._json(400, {"ok": False})
                    i = max(1, min(20, int(data.get("i") or 1)))
                    if p == "/hs/cover_save": out = P("cover-%d.jpg" % i)
                    else:
                        os.makedirs(P("carousel"), exist_ok=True)
                        if data.get("clear"):
                            for f in glob.glob(os.path.join(P("carousel"), "*.png")): os.remove(f)
                        out = os.path.join(P("carousel"), "slide-%02d.png" % i)
                    open(out, "wb").write(base64.b64decode(m.group(2))); return self._json(200, {"ok": True, "file": os.path.relpath(out, work).replace("\\", "/")})
                if p == "/hs/repurpose":
                    if data.get("save"):
                        R = rj(P("repurpose.json"), {}) or {}; R.update({k: v for k, v in data["save"].items() if k in ("title", "points", "cta", "thread", "yt", "tags")}); wj(P("repurpose.json"), R); return self._json(200, R)
                    return self._json(200, repurpose(work, fresh=True))
                if p == "/hs/logo":   # 4.9: شعار شركة باسمها (ينزل أول مرة من Simple Icons وينحفظ بالجهاز)
                    nm_ = str(data.get("name") or "").strip()[:60]; src_ = logo_to_project(work, nm_) if nm_ else ""
                    return self._json(200, {"ok": bool(src_), "src": src_, "name": nm_})
                if p == "/hs/logos":   # 4.9: يقترح شارات الشعار من الكابشن، والاستديو يضيفها كطبقات
                    pl = logos_plan(work)
                    for x_ in pl:
                        x_["src"] = logo_to_project(work, x_["name"])
                        if x_.get("name2"): x_["src2"] = logo_to_project(work, x_["name2"])
                    return self._json(200, {"ok": True, "plan": pl})
                if p == "/hs/perf":
                    perf_set(item_id(work), str(data.get("plat") or "all")[:20], **{k: data.get(k) for k in ("views", "likes", "comments", "shares", "saves", "watch", "ret", "posted", "url")})
                    return self._json(200, {"ok": True, "rows": perf_get(item_id(work))})
                if p == "/hs/claude_fix":   # 4.5: اختياري ويستهلك من حدّك (الواجهة تنبّهه قبلها)
                    what = str(data.get("what") or "retention"); items = [str(x)[:300] for x in (data.get("items") or [])][:12]
                    if what == "rmbg":   # 4.11
                        src_ = str(data.get("src") or "")[:300]
                        task = ("شيل خلفية الصورة %s بمشروع \"%s\". جرّب أول: python hs.py rmbg \"%s\" \"%s\" . لو قال ما قدر (خلفية معقدة ومو شخص): استخدم أداة شيل الخلفية من حساب المستخدم (Higgsfield remove_background، أو Canva remove-background) وقل له قبلها إنها تستهلك من رصيده، "
                                "واحفظ الناتج PNG بمجلد assets باسم الصورة-nobg.png، وبعدها غيّر src بالطبقة اللي تستخدمها لهذا الملف بـ studio.json (وخلّ srcOrig بالأصل).") % (src_, work, work, src_)
                        ok, msg = agent_run(task, "Claude يشيل الخلفية"); return self._json(200, {"ok": ok, "msg": msg})
                    if what in ("unsure", "plan", "plan2"):   # 4.10
                        ask = str(data.get("text") or "").strip()[:800]
                        if what == "unsure":
                            task = ("راجع الكلمات اللي ما تأكد منها التفريغ بكابشن هذا المشروع: python hs.py caps \"%s\" unsure . صحّح الغلط منها بالمعنى من سياق الجملة (python hs.py text \"%s\" <رقم الجملة> \"النص الصح\")، "
                                    "والأسماء المعروفة بالإنجليزي. لا تغيّر كلامه ولا أسلوبه، صحّح الإملاء والسماع بس. بعدها python hs.py caps \"%s\" unsure مرة ثانية.") % (work, work, work)
                        elif what == "plan":
                            task = ("أعد كتابة خطة المقطع بملف plan.json بمجلد المشروع على كلام المستخدم: «%s». كل بند: id، s، e، title، speech (كلامه بهذا الجزء)، show (وش يطلع)، motion (الحركة)، kind (web أو archive أو gen أو overlay أو screen أو text أو none)، query أو source. "
                                    "خلّ approved=false و feedback فاضي، وتأكد: python hs.py plan \"%s\" check") % (ask or "خطة أوضح", work)
                        else:
                            task = ("من plan.json بهذا المشروع خذ أول بندين نوعهم gen واصنع صورهم (بالوصف نفسه وستايل واحد) من حساب المستخدم بالترتيب المكتوب بقسم الصور في SKILL.md، ثم python hs.py gen \"%s\" import … عند وقت كل بند، وحط src بالبند وstatus=done. "
                                    "لا تصنع أكثر من صورتين. %s") % (work, ("ملاحظته: " + ask) if ask else "")
                        ok, msg = agent_run(task, {"unsure": "Claude يراجع الكلمات", "plan": "Claude يعيد الخطة", "plan2": "Claude يصنع أول صورتين"}[what]); return self._json(200, {"ok": ok, "msg": msg})
                    if what == "takes":   # 4.10: Claude يختار الأفضل بين الإعادات
                        ask = str(data.get("text") or "").strip()[:600]
                        task = ("راجع «اختيار الجمل» بهذا المشروع. شغّل: python hs.py takes \"%s\" list --all واقرأ كل المحاولات. بكل مجموعة إعادة اختار الأفضل بالمعنى (الكاملة، الصح بالمعلومة، الأوضح، وغالباً الأخيرة لكن مو دايم) بـ: "
                                "python hs.py takes \"%s\" use <رقم> --why \"السبب بكلمتين\" --claude. واحذف أي بداية متروكة أو جملة قالها وأعادها بصياغة ثانية (drop <رقم> --why …)، ورجّع أي شي انحذف وهو مهم (keep). "
                                "لا تحذف كلام فيه معلومة ما انقالت بمكان ثاني. بعدها: python hs.py takes \"%s\" note \"ملخص سطر\" ثم python hs.py takes \"%s\" apply. %s") % (work, work, work, work, ("طلب المستخدم: " + ask) if ask else "")
                        ok, msg = agent_run(task, "Claude يختار الجمل"); return self._json(200, {"ok": ok, "msg": msg})
                    if what == "repurpose":
                        task = ("حسّن نصوص النشر بملف repurpose.json بمجلد المشروع بلهجة صاحب المقطع: عنوان يشد، 4 إلى 5 نقاط للكاروسيل (كل وحدة جملة قصيرة)، ثريد X، وعنوان ووصف يوتيوب. "
                                "لا تغيّر شكل الملف ولا تلمس أي ملف ثاني. خلّ by = claude.")
                    else: task = "صلّح هالمشاكل بالمقطع (فحص الاحتفاظ). أقل تعديل يكفي، وبعدها قل وش سويت بسطرين:\n- " + "\n- ".join(items)
                    ok, msg = agent_run(task, "تحسين بـClaude: " + ("نصوص النشر" if what == "repurpose" else "فحص الاحتفاظ"))
                    return self._json(200, {"ok": ok, "msg": msg})
                if p == "/hs/sv":     # 4.12: صوت استوديو (يعالج مرة وحدة لكل قص)
                    try: f, r = studio_voice(work, log=lambda m: None, force=bool(data.get("redo")))
                    except Exception as ex: return self._json(200, {"ok": False, "msg": str(ex)[:300]})
                    return self._json(200, {**(r or {}), "ok": bool(f), "line": sv_line(r or {}), "sig": sv_sig(work)})
                if p == "/hs/rmbg":   # 4.11: شيل الخلفية من صورة مضافة
                    r = rmbg(work, str(data.get("src") or ""), str(data.get("mode") or "auto")); return self._json(200, r)
                if p == "/hs/plan_set":   # 4.10: الخطة قبل البناء
                    pl = plan_load(work) or {"items": []}
                    if "approve" in data: pl["approved"] = bool(data["approve"])
                    if data.get("rm") is not None: pl["items"] = [x for x in pl.get("items") or [] if str(x.get("id")) != str(data["rm"])]
                    if data.get("feedback") is not None: pl["feedback"] = str(data["feedback"])[:1500]; pl["approved"] = False
                    wj(P("plan.json"), pl); return self._json(200, plan_view(work))
                if p == "/hs/plan_build":   # 4.16: ابنِ الصور والموشن من الخطة
                    n_, miss_ = plan_build(work); return self._json(200, {"ok": True, "n": n_, "miss": miss_, "plan": plan_view(work)})
                if p == "/hs/unsure":
                    u = caps_unsure(work); return self._json(200, {"ok": True, "n": len(u), "items": u[:200]})
                if p == "/hs/cuts_fix":
                    def go():
                        bad, o_, n_ = cut_on_sound(work)
                        if bad and not _same_keep(o_, n_, 0.005): apply_keep(work, o_, n_, S, base.log, snap="قبل تصليح القطعات")
                        base.JOB["reload"] = True
                    ok = base.job("remove", go); return self._json(200 if ok else 409, {"ok": ok, "msg": "" if ok else "فيه عملية شغالة"})
                if p == "/hs/takes_set":
                    try:
                        for x in data.get("ids") or [data.get("id")]: tk_set(work, x, str(data.get("action") or "drop"), str(data.get("why") or ""))
                    except Exception as e: return self._json(400, {"ok": False, "msg": str(e)[:200]})
                    return self._json(200, tk_view(work))
                if p == "/hs/takes_scan":
                    try: tk_scan(work)
                    except SystemExit as e: return self._json(400, {"ok": False, "msg": str(e)})
                    return self._json(200, tk_view(work))
                if p == "/hs/takes_apply":
                    def go(): tk_apply(work, S, base.log); base.JOB["reload"] = True
                    ok = base.job("remove", go); return self._json(200 if ok else 409, {"ok": ok, "msg": "" if ok else "فيه عملية شغالة"})
                if p == "/hs/dub":   # 4.26: تشغيل وإطفاء الدبلجة
                    st_ = load_studio(work); mx = hs_of(st_).setdefault("mix", {})
                    if data.get("on"):
                        try: dub_build(work, base.log)
                        except Exception as e: return self._json(400, {"ok": False, "msg": str(e)[:200]})
                    mx["dub"] = bool(data.get("on")); wj(J(work, "studio.json"), st_); return self._json(200, {"ok": True, "on": mx["dub"]})
                if p == "/hs/vpos":   # 4.27: مكان الفيديو بالكادر ← يتقص من الأصل من جديد
                    if not vpos_info(work)["can"]: return self._json(400, {"ok": False, "msg": "هالمشروع ما فيه الفيديو الأصلي، فما أقدر أحرك مكانه"})
                    if base.JOB["running"]: return self._json(409, {"ok": False, "msg": "فيه عملية شغالة"})
                    vpos_set(work, None if data.get("reset") else data)
                    def go(): rebuild_video(work, S, base.log); base.JOB["reload"] = True
                    ok = base.job("vpos", go); return self._json(200 if ok else 409, {"ok": ok, "msg": "" if ok else "فيه عملية شغالة"})
                if p == "/hs/quality":   # 4.25: تحسين الجودة (يطلّع الفريمات من جديد بالتحسين)
                    lv = data.get("level") if data.get("level") in ENH_LEVELS else "off"
                    st_ = load_studio(work); hs_of(st_)["enhance"] = {"level": lv}; wj(J(work, "studio.json"), st_)
                    def go(): vfr_extract(work, base.log, lv); base.JOB["reload"] = True
                    ok = base.job("quality", go); return self._json(200 if ok else 409, {"ok": ok, "msg": "" if ok else "فيه عملية شغالة"})
                if p == "/hs/move_shot":   # 4.23: نقل لقطة لمكان ثاني (فوري)
                    if base.JOB["running"]: return self._json(409, {"ok": False, "msg": "فيه عملية شغالة"})
                    try: r_ = move_shot(work, data.get("s"), data.get("e"), data.get("to"))
                    except ValueError as e: return self._json(400, {"ok": False, "msg": str(e)})
                    except Exception as e: base.log("❌ نقل اللقطة: %s" % e); return self._json(500, {"ok": False, "msg": "ما قدرت أنقل اللقطة: " + str(e)[:160]})
                    if not media_map(work)[0]:
                        def go(): rebuild_video(work, S, base.log); base.JOB["reload"] = True
                        base.job("remove", go); return self._json(200, {"ok": True, "rebuild": True})
                    return self._json(200, {"ok": True, "instant": True, "to": r_["to"]})
                if p == "/hs/remove":   # 4.23: القص فوري (الكابشن والطبقات والتايم لاين)، والمعاينة تتخطّى المقصوص من الفيديو الحالي
                    if base.JOB["running"]: return self._json(409, {"ok": False, "msg": "فيه عملية شغالة"})
                    try: r_ = remove_ranges(work, S, base.log, ranges=data.get("ranges") or [], cards=data.get("cards") or [], words=data.get("words") or [], rebuild=False)
                    except ValueError as e: return self._json(400, {"ok": False, "msg": str(e)})
                    except Exception as e: base.log("❌ القص: %s" % e); return self._json(500, {"ok": False, "msg": "ما قدرت أقص: " + str(e)[:160]})
                    if not media_map(work)[0]:
                        def go(): rebuild_video(work, S, base.log); base.JOB["reload"] = True
                        base.job("remove", go); return self._json(200, {"ok": True, "rebuild": True})
                    return self._json(200, {"ok": True, "instant": True, "gone": r_["gone"], "total": r_["total"]})
                if p.startswith("/api/render") or p == "/hs/export":
                    kind = data.get("kind", "final"); hooks = bool(data.get("hooks")); frm = data.get("frame")
                    def go(): outs = export(work, S, base.log, kind=kind, hooks=hooks, frame=frm); base.JOB["done"] = outs[0]; base.JOB["outs"] = outs
                    ok = base.job("render", go); return self._json(200 if ok else 409, {"ok": ok, "msg": "" if ok else "فيه عملية شغالة"})
                if p == "/hs/pack": return self._json(200, {"ok": True, "files": pack(work), "zip": "/hs/pack.zip"})
                if p == "/hs/brief_save":
                    ans = data.get("answers") or {}; ans["savedAt"] = int(time.time()); th_ = ans.get("theme") or {}
                    if th_.get("mode") == "newid":   # 4.37: هوية جديدة (ملفات رفعها أو وصف كتبه) تنحفظ وتصير هويته لكل مقاطعه
                        try: nm_ = str(th_.get("idName") or "").strip() or "هويتي"; ident_adopt(th_.get("idKey"), nm_); I_ = ident_new(nm_, str(th_.get("idText") or ""), default=True); th_.update({"mode": "identity", "identity": I_["slug"]}); ans["theme"] = th_
                        except Exception as e: return self._json(400, {"ok": False, "msg": "ما قدرت أحفظ الهوية: " + str(e)[:160]})
                    wj(brief_paths(work)[1], ans)
                    try: os.makedirs(HOME_CFG, exist_ok=True); wj(os.path.join(HOME_CFG, "last-brief.json"), {k: v for k, v in ans.items() if k not in ("cut", "hook", "notes", "ref", "extra", "savedAt")})
                    except Exception: pass
                    say(work, "حفظ إجاباته. Claude يبدأ المونتاج.", "done"); return self._json(200, {"ok": True})
                if p == "/hs/media_add":
                    if (data.get("item") or {}).get("kind") == "video":
                        key, n = video_add(work, data["item"], data.get("at"), data.get("dur", 4)); return self._json(200, {"ok": True, "clip": key, "frames": n})
                    lid, name = media_add(work, data["item"], data.get("at"), data.get("dur", 3), data.get("fit", "card")); return self._json(200, {"ok": True, "id": lid, "file": name})
                if p == "/hs/shot":
                    lid, name = shot_add(work, str(data.get("url", "")).strip(), data.get("at"), data.get("dur", 4), log=lambda *_: None); return self._json(200, {"ok": True, "id": lid, "file": name})
                if p == "/hs/auto": return self._json(200, {"ok": True, "n": auto_layers(work, data["kind"], bool(data.get("on", True)))})
                if p == "/hs/gen":
                    kind = data.get("kind"); prompt = str(data.get("prompt", "")).strip()
                    if not prompt: return self._json(400, {"ok": False, "msg": "اكتب وصف المطلوب"})
                    rid = gen_request(work, kind, prompt, data.get("at"), data.get("fit", "card")); q = gen_list(work)
                    return self._json(200, {"ok": True, "id": rid, "gen": gen_view(q)})
                if p == "/hs/gen_rm": return self._json(200, {"ok": True, "gen": gen_view(gen_rm(work, data.get("id")))})
                if p == "/hs/frame":
                    st = load_studio(work); h = hs_of(st); f = h.setdefault("frame", {})
                    if data.get("ar") in FRAMES: f["ar"] = data["ar"]
                    if data.get("cy") is not None: f["cy"] = max(0.2, min(0.8, float(data["cy"])))
                    if isinstance(data.get("platforms"), list): h["platforms"] = [x for x in data["platforms"] if x in PLATFORMS]
                    wj(P("studio.json"), st); return self._json(200, {"ok": True, "safe": safe_of(h.get("platforms"), *frame_of(h))})
                if p == "/hs/post": open(P("post.txt"), "w", encoding="utf-8").write(str(data.get("text", ""))); return self._json(200, {"ok": True})
                if p == "/hs/text":
                    caps, hs = apply_text(work, int(data["card"]), data["text"]); return self._json(200, {"ok": True, "caps": caps, "hs": hs})
                if p == "/hs/note":
                    notes = rj(P("notes.json"), []) or []; nid = next_note_id(notes)
                    note = {"id": nid, "t": round(float(data.get("t", 0)), 2), "card": data.get("card"), "text": str(data.get("text", ""))[:1000],
                            "pin": data.get("pin"), "status": "open", "who": str(data.get("who") or ("أنا" if self._local() else "جوال"))[:30], "at": time.strftime("%Y-%m-%d %H:%M")}
                    img = data.get("img") or ""
                    if img.startswith("data:image/jpeg;base64,"):
                        os.makedirs(P("notes"), exist_ok=True); open(P("notes", "%d.jpg" % nid), "wb").write(base64.b64decode(img.split(",", 1)[1])); note["img"] = "notes/%d.jpg" % nid
                    notes.append(note); wj(P("notes.json"), notes); return self._json(200, {"ok": True, "notes": notes})
                if p == "/hs/note_edit":
                    notes = rj(P("notes.json"), []) or []
                    for x in notes:
                        if str(x["id"]) == str(data["id"]):
                            if "text" in data: x["text"] = str(data["text"])[:1000]
                            if "status" in data: x["status"] = data["status"]
                            if data.get("answer") and x.get("by") == "claude":
                                ans = str(data["answer"])[:600]; x["answeredAt"] = time.strftime("%Y-%m-%d %H:%M")
                                if ans == "fixed": x["answer"] = "صلّحتها"; x["status"] = "done"   # 4.29: ملاحظة «لازم تعدّلها» خلصت
                                elif ans == "no": x["answer"] = "لا، خلّه مثل ما هو"; x["status"] = "done"; x["reply"] = "رفض الاقتراح"
                                else: x["answer"] = "موافق، سوّه" if ans == "yes" else ans; x["status"] = "open"
                    if data.get("delete"): notes = [x for x in notes if str(x["id"]) != str(data["id"])]
                    wj(P("notes.json"), notes); return self._json(200, {"ok": True, "notes": notes})
                if p == "/hs/notes_send":
                    notes = rj(P("notes.json"), []) or []; caps = rj(P("caps.json"), {"cards": []})
                    open(P("NOTES.md"), "w", encoding="utf-8").write(notes_md(notes, caps))
                    for x in notes:
                        if x.get("status") == "open": x["status"] = "sent"
                    wj(P("notes.json"), notes); cnt = sum(1 for x in notes if x.get("status") == "sent"); started = False; msg = ""
                    if data.get("run"):
                        started, msg = agent_run("طبّق ملاحظات الاستوديو المفتوحة على هذا المشروع (python hs.py notes <work> list)، وعلّم كل ملاحظة تنفّذها بـ done مع جملة وش سويت. الملاحظة اللي مو واضحة خلّها مفتوحة واذكرها بآخر ردّك.", "طلب: طبّق %d ملاحظة" % cnt)
                    return self._json(200, {"ok": True, "notes": notes, "count": cnt, "started": started, "msg": msg, "prompt": "طبّق ملاحظات الاستوديو على المشروع: " + work})
                if p == "/hs/agent":
                    task = str(data.get("task", "")).strip()
                    if not task: return self._json(400, {"ok": False, "msg": "اكتب الطلب"})
                    ctx = "\n\n(سياق من الاستوديو: المؤشر عند %.2f ث%s)" % (float(data.get("t", 0)), ("، المحدد: " + str(data.get("sel"))) if data.get("sel") else "")
                    ok, msg = agent_run(task + ctx, "طلب: " + task[:140], gen=bool(data.get("gen"))); return self._json(200 if ok else 409, {"ok": ok, "msg": msg, "prompt": task + " — المشروع: " + work})
                if p == "/hs/quit":
                    if not self._local(): return self._json(403, {"ok": False})
                    self._json(200, {"ok": True}); threading.Thread(target=lambda: (time.sleep(0.3), os._exit(0)), daemon=True).start(); return
                if p == "/hs/export_stop":
                    n = 0
                    for pr in list(KIDS):
                        if pr.poll() is None and pr is not AG.get("proc"): kill_tree(pr); n += 1
                    return self._json(200, {"ok": True, "n": n})
                if p == "/hs/agent_stop":
                    pr = AG.get("proc")
                    if pr: kill_tree(pr)
                    return self._json(200, {"ok": True})
                if p == "/hs/notify":
                    if role != "owner": return self._deny()
                    act = data.get("action")
                    if act == "setup": c = notify_setup(); return self._json(200, {"ok": True, "on": True, "topic": c["topic"], "sub": notify_sub(c)})
                    if act == "off": c = notify_cfg(); c["on"] = False; wj(notify_cfg_path(), c); return self._json(200, {"ok": True, "on": False})
                    if act == "test": ok, err = notify_send("وصلك هذا الإشعار؟ معناه Hojas Studio يقدر يكلّمك ويرسل لك مقاطعك.", title="Hojas Studio: تجربة"); return self._json(200 if ok else 502, {"ok": ok, "msg": err})
                    if act == "send":
                        f = P(os.path.basename(str(data.get("file", "")))) if data.get("file") else None
                        ok, err = notify_send(str(data.get("text") or "المقطع"), title="Hojas Studio", file=f if f and os.path.exists(f) else None, work=work); return self._json(200 if ok else 502, {"ok": ok, "msg": err})
                    return self._json(400, {"ok": False})
                if p == "/hs/ver_save": return self._json(200, {"ok": True, "id": snapshot(work, data.get("name")), "versions": versions()})
                if p == "/hs/ver_restore":
                    if base.JOB["running"]: return self._json(409, {"ok": False, "busy": True, "msg": "فيه عملية شغّالة، انتظرها تخلص"})   # 4.20: لا ترجّع نص النسخة والفيديو ما يقدر يتركّب
                    media_pin(work); need = ver_restore(data["id"]) and not media_map(work)[0]   # 4.23
                    if need:
                        def go(): rebuild_video(work, S, base.log); base.JOB["reload"] = True
                        base.job("remove", go)
                    return self._json(200, {"ok": True, "versions": versions(), "rebuild": need})
                if p == "/hs/brand_save":
                    name = re.sub(r"[^\w\- ]+", "", str(data.get("name", ""))).strip()[:40]
                    if not name: return self._json(400, {"ok": False, "msg": "اكتب اسم الهوية"})
                    wj(os.path.join(brand_dir(), name + ".json"), brand_pack(work)); return self._json(200, {"ok": True, "brands": sorted(os.path.splitext(f)[0] for f in os.listdir(brand_dir()))})
                return self._json(404, {"ok": False})
            except Exception as e:
                return self._json(500, {"ok": False, "msg": str(e)[:300]})

    import http.server
    srv = http.server.ThreadingHTTPServer(("0.0.0.0", port), HS)
    local = "http://127.0.0.1:%d/" % port; lan = "http://%s:%d/m?k=%s" % (LAN, port, TOKEN)
    open(os.path.join(D, "url.txt"), "w").write(local + "\n" + lan + "\n")
    print("Hojas Studio %s شغّال" % VERSION); print("  على الجهاز : " + local)
    print("  على الجوال : " + lan + "   (نفس الواي فاي · رمز الدخول %s)" % TOKEN); print("  المحرّك    : " + eng); sys.stdout.flush()
    try: srv.serve_forever()
    except KeyboardInterrupt: pass

# ───────────────────────── 4.1: إشعارات للجوال (ntfy · بلا حساب ولا مفاتيح) ─────────────────────────
NTFY_MAX = 15 * 1024 * 1024
def notify_cfg_path(): return os.path.join(HOME_CFG, "notify.json")
def notify_cfg(): return rj(notify_cfg_path(), {}) or {}
def notify_setup(server=None):
    c = notify_cfg()
    if not c.get("topic"): c["topic"] = "hojas-" + secrets.token_hex(8)
    c["server"] = (server or c.get("server") or "https://ntfy.sh").rstrip("/"); c["on"] = True
    os.makedirs(HOME_CFG, exist_ok=True); wj(notify_cfg_path(), c); return c
def notify_sub(c): return "%s/%s" % (c["server"], c["topic"])
def notify_url(c, **q):
    qs = urllib.parse.urlencode({k: v for k, v in q.items() if v})
    return notify_sub(c) + (("?" + qs) if qs else "")
def notify_send(text, title="Hojas Studio", file=None, click=None, tags="clapper", work=None):
    """يرسل إشعار لجوال المستخدم. الملف (لو أصغر من 15MB) يوصله مرفق. يرجّع (نجح؟, رسالة)."""
    c = notify_cfg()
    if not c.get("on") or not c.get("topic"): return False, "الإشعارات مطفية. فعّلها: python hs.py notify setup"
    try:
        if file and os.path.exists(file) and os.path.getsize(file) <= NTFY_MAX:
            with open(file, "rb") as f: data = f.read()
            req = urllib.request.Request(notify_url(c, title=title, message=text, filename=os.path.basename(file), click=click, tags=tags), data=data, method="PUT")
        else:
            if file and os.path.exists(file): text += "\n(الملف أكبر من 15MB، تلقاه بمجلد المشروع)"
            req = urllib.request.Request(notify_url(c, title=title, click=click, tags=tags), data=text.encode("utf-8"), method="POST")
        with urllib.request.urlopen(req, timeout=180) as r: ok = 200 <= r.status < 300
        if work and ok: say(work, "انرسل لجوالك: " + text.split("\n")[0][:90], "info")
        return ok, ""
    except Exception as e: return False, str(e)[:200]
def notify_quiet(text, **kw):
    """للإشعارات التلقائية: ما توقف الشغل لو النت فاصل أو الإشعارات مطفية."""
    if not notify_cfg().get("on"): return
    threading.Thread(target=lambda: notify_send(text, **kw), daemon=False).start()   # مو daemon: الأمر من التيرمنال ينتظره قبل ما يطلع
def cmd_notify(args):
    sub = args[0] if args else "status"
    def o(nm):
        if nm in args: i = args.index(nm); v = args[i + 1]; del args[i:i + 2]; return v
    if sub == "setup":
        c = notify_setup(o("--server"))
        print("انفعلت الإشعارات.\n1) نزّل تطبيق ntfy على جوالك (مجاني: App Store أو Google Play).\n2) اضغط + واكتب اسم القناة: %s\n   (أو افتح الرابط من جوالك: %s)\n3) جرّب: python hs.py notify test" % (c["topic"], notify_sub(c)))
        print("\nتنبيه خصوصية: الإشعار والمقطع المرفق يمرّون على خادم %s ويبقون فيه ساعات قليلة. اسم القناة هو كلمة السر، لا تنشره." % c["server"])
    elif sub == "test":
        ok, err = notify_send("وصلك هذا الإشعار؟ معناه Hojas Studio يقدر يكلّمك ويرسل لك مقاطعك.", title="Hojas Studio: تجربة")
        print("انرسل. شيّك جوالك." if ok else "ما انرسل: " + err)
    elif sub == "off": c = notify_cfg(); c["on"] = False; wj(notify_cfg_path(), c); print("انطفت الإشعارات.")
    elif sub == "send":
        f = o("--file"); w = o("--work"); click = o("--click")
        ok, err = notify_send(" ".join(args[1:]) or "Hojas Studio", file=f, click=click, work=os.path.abspath(w) if w else None)
        print("انرسل." if ok else "ما انرسل: " + err)
    else:
        c = notify_cfg(); print(("شغّالة · القناة: %s · الخادم: %s" % (c.get("topic"), c.get("server"))) if c.get("on") else "مطفية. فعّلها: python hs.py notify setup")

# ───────────────────────── 4.1: يتعلّم أسلوبك من تعديلاتك على التايم لاين ─────────────────────────
STYLE_FILES = ("studio.json", "caps.json", "theme.json")
def style_path(): return os.path.join(HOME_CFG, "style.json")
def style_prof(): return rj(style_path(), {}) or {}
def style_base(work): return J(work, ".hs", "style-base")
def style_snap(work):
    """لقطة لمونتاج Claude قبل ما يستلمه المستخدم. اللي يغيّره بعدها هو ذوقه."""
    d = style_base(work); os.makedirs(d, exist_ok=True)
    for f in STYLE_FILES:
        if os.path.exists(J(work, f)): shutil.copy(J(work, f), os.path.join(d, f))
    return d
def _words(card): return [str(w.get("t", "")) for w in (card.get("w") or [])]
def style_diff(b, c):
    """يقارن نسخة Claude (b) بنسخة المستخدم (c). كل وحدة dict فيها studio, caps, theme."""
    out = {"cap": {}, "en": {}, "theme": {}, "outro": {}, "removed": {}, "added": {}, "kept": {}, "words": {}}
    bh = (b.get("studio") or {}).get("hs") or {}; ch = (c.get("studio") or {}).get("hs") or {}
    for sec in ("cap", "en"):
        bb, cc = bh.get(sec) or {}, ch.get(sec) or {}
        for k, v in cc.items():
            if k != "map" and bb.get(k) != v and isinstance(v, (str, int, float, bool)): out[sec][k] = v
    bt, ct = b.get("theme") or {}, c.get("theme") or {}
    for k in ("bg", "ink", "acc", "font", "handle"):
        if k in ct and bt.get(k) != ct[k]: out["theme"][k] = ct[k]
    bo, co = (b.get("studio") or {}).get("outro") or {}, (c.get("studio") or {}).get("outro") or {}
    for k in ("font", "l1", "l2", "cta", "word", "sub"):
        if k in co and bo.get(k) != co[k]: out["outro"][k] = co[k]
    bl = {str(l.get("id")): l.get("type", "?") for l in bh.get("layers") or []}; cl = {str(l.get("id")): l.get("type", "?") for l in ch.get("layers") or []}
    for i, ty in bl.items(): out["removed" if i not in cl else "kept"][ty] = out["removed" if i not in cl else "kept"].get(ty, 0) + 1
    for i, ty in cl.items():
        if i not in bl: out["added"][ty] = out["added"].get(ty, 0) + 1
    bc, cc = (b.get("caps") or {}).get("cards") or [], (c.get("caps") or {}).get("cards") or []
    if len(bc) == len(cc):
        for x, y in zip(bc, cc):
            a1, a2 = _words(x), _words(y)
            for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a1, a2).get_opcodes():
                if op == "replace" and (i2 - i1) <= 3 and (j2 - j1) <= 3:
                    k, v = " ".join(a1[i1:i2]), " ".join(a2[j1:j2])
                    if k.strip() and v.strip() and k != v: out["words"][k] = v
    return out
def style_learn(work):
    """يقارن لقطة Claude بالموجود الحين، يضيف الفرق لملف الأسلوب، ويحدّث اللقطة (عشان ما ينحسب نفس التعديل مرتين)."""
    d = style_base(work)
    if not os.path.isdir(d): return None
    ld = lambda root: {"studio": rj(os.path.join(root, "studio.json"), {}) or {}, "caps": rj(os.path.join(root, "caps.json"), {}) or {}, "theme": rj(os.path.join(root, "theme.json"), {}) or {}}
    df = style_diff(ld(d), ld(work))
    if not any(df[k] for k in df): return df
    p = style_prof(); p["n"] = int(p.get("n", 0)) + 1; p["updated"] = time.strftime("%Y-%m-%d")
    for sec in ("cap", "en", "theme", "outro"): p.setdefault(sec, {}).update(df[sec])
    for sec in ("removed", "added", "kept"):
        q = p.setdefault(sec, {})
        for k, v in df[sec].items(): q[k] = q.get(k, 0) + v
    W, N = p.setdefault("words", {}), p.setdefault("wordsN", {})
    for k, v in df["words"].items(): N[k] = (N.get(k, 0) + 1) if W.get(k) == v else 1; W[k] = v
    if len(W) > 300:
        for k in list(W)[:-300]: W.pop(k, None); N.pop(k, None)
    os.makedirs(HOME_CFG, exist_ok=True); wj(style_path(), p); style_snap(work); return df
def style_text(p=None):
    p = p if p is not None else style_prof()
    if not p.get("n"): return "ما تعلّمت أسلوبه للحين. يتعلّم لحاله من تعديلاته بعد ما تسلّمه التايم لاين (style snap قبل التسليم)."
    L = ["تعلّمت من تعديلاته على %d مونتاج (آخرها %s). طبّق هذا من البداية:" % (p["n"], p.get("updated", "?"))]
    if p.get("cap"): L.append("- الكابشن اللي يرجع له: " + json.dumps(p["cap"], ensure_ascii=False) + "  ← hs set cap.<key>=<value>")
    if p.get("en"): L.append("- الترجمة الإنجليزية: " + json.dumps(p["en"], ensure_ascii=False))
    if p.get("theme"): L.append("- ألوانه وحسابه: " + json.dumps(p["theme"], ensure_ascii=False) + "  (theme.json)")
    if p.get("outro"): L.append("- كرت الختام: " + json.dumps(p["outro"], ensure_ascii=False) + "  ← hs set outro.<key>=<value>")
    rm = sorted(((k, v) for k, v in (p.get("removed") or {}).items() if v >= 2 and v > (p.get("kept") or {}).get(k, 0)), key=lambda x: -x[1])
    if rm: L.append("- طبقات يحذفها أكثر ما يخليها، قلّل منها: " + "، ".join("%s (%d)" % kv for kv in rm))
    ad = sorted(((k, v) for k, v in (p.get("added") or {}).items() if v >= 2), key=lambda x: -x[1])
    if ad: L.append("- طبقات يضيفها بنفسه، حطها له: " + "، ".join("%s (%d)" % kv for kv in ad))
    if p.get("words"):
        N = p.get("wordsN") or {}; sure = [(k, v) for k, v in p["words"].items() if N.get(k, 0) >= 2]; once = [(k, v) for k, v in p["words"].items() if N.get(k, 0) < 2]
        if sure: L.append("- تصحيحات يكررها (style apply يطبّقها لحاله): " + "، ".join("%s ← %s" % kv for kv in sure[-12:]))
        if once: L.append("- تصحيحات سواها مرة (انتبه لها بالتفريغ، ما تنطبق لحالها): " + "، ".join("%s ← %s" % kv for kv in once[-8:]))
    return "\n".join(L)
def style_apply(work):
    """يطبّق تصحيحات الكلمات اللي علّمها المستخدم على caps.json. يرجّع عدد الكلمات اللي تغيّرت."""
    words = style_prof().get("words") or {}; cp = J(work, "caps.json"); caps = rj(cp)
    if not caps or not words: return 0
    cnt = style_prof().get("wordsN") or {}
    n = 0; one = {k: v for k, v in words.items() if " " not in k and " " not in v and cnt.get(k, 0) >= 2}   # نفس التصحيح مرتين = عادة، مو تعديل لمرة وحدة
    for c in caps.get("cards") or []:
        for w in c.get("w") or []:
            if str(w.get("t")) in one: w["t"] = one[w["t"]]; n += 1
    if n: wj(cp, caps)
    return n
def cmd_style(args):
    sub = args[0] if args else "show"
    if sub == "show": print(style_text())
    elif sub == "reset":
        try: os.remove(style_path())
        except OSError: pass
        print("انمسح الأسلوب المتعلَّم.")
    elif sub in ("snap", "learn", "apply"):
        if len(args) < 2: sys.exit("style %s <work>" % sub)
        work = os.path.abspath(args[1])
        if sub == "snap": style_snap(work); print("انحفظت لقطة مونتاجك. اللي يغيّره المستخدم بعدها ينحسب من ذوقه.")
        elif sub == "learn":
            df = style_learn(work)
            print("ما فيه لقطة (style snap) لهذا المشروع." if df is None else ("ما غيّر شي من بعد اللقطة." if not any(df[k] for k in df) else "تعلّمت: " + json.dumps({k: v for k, v in df.items() if v}, ensure_ascii=False)[:900]))
        else: print("تصحيحات انطبقت على الكابشن: %d" % style_apply(work))
    else: sys.exit("style show | snap <work> | learn <work> | apply <work> | reset")

# ───────────────────────── 4.1: النشر من متصفح المستخدم (بلا مفاتيح) ─────────────────────────
PUBLISH_PRIVATE = os.path.join(HERE, "publish-private.md")
PUBLISH_PUBLIC = {"tiktok": {"ar": "تيك توك", "url": "https://www.tiktok.com/tiktokstudio/upload", "frame": "9:16"}}
def publish_platforms():
    d = dict(PUBLISH_PUBLIC)
    if os.path.exists(PUBLISH_PRIVATE):
        for m in re.finditer(r"^platform:\s*(\w+)\s*\|\s*([^|]+)\|\s*(\S+)\s*\|\s*(\S+)", open(PUBLISH_PRIVATE, encoding="utf-8").read(), re.M):
            d[m.group(1)] = {"ar": m.group(2).strip(), "url": m.group(3), "frame": m.group(4), "private": True}
    return d
def post_for(work, plat):
    """نص البوست الخاص بالمنصة من post.txt (تحت عنوان باسمها)، وإلا النص كامل."""
    p = J(work, "post.txt")
    if not os.path.exists(p): return ""
    txt = open(p, encoding="utf-8").read().strip()
    names = {"tiktok": ("تيك توك", "tiktok"), "instagram": ("انستقرام", "إنستقرام", "انستا", "instagram"), "x": ("إكس", "x"), "linkedin": ("لينكدإن", "linkedin")}
    pat = r"^[ \t]*#*[ \t]*(" + "|".join(re.escape(n) for ns in names.values() for n in ns) + r")[ \t]*:?[ \t]*$"
    parts = re.split(pat, txt, flags=re.M | re.I)
    for i in range(1, len(parts) - 1, 2):
        if parts[i].lower() in [n.lower() for n in names.get(plat, (plat,))]: return parts[i + 1].strip()
    return txt
def publish_plan(work, plat, when=None):
    P = publish_platforms()
    if plat not in P: return None, "النشر على %s مو متاح بهذي النسخة. المتاح: %s" % (plat, "، ".join(P))
    pi = P[plat]; ar = pi["frame"]; f = J(work, "ad-master.mp4") if ar == "9:16" else J(work, "ad-%dx%d.mp4" % tuple(FRAMES.get(ar, (1080, 1920))))
    if not os.path.exists(f): f = J(work, "ad-master.mp4")
    if not os.path.exists(f): return None, "ما فيه ملف نهائي. صدّر أول: python hs.py export <work>"
    plan = {"platform": plat, "name": pi["ar"], "url": pi["url"], "file": os.path.abspath(f), "caption": post_for(work, plat), "when": when or "now",
            "guide": PUBLISH_PRIVATE if pi.get("private") else None, "at": int(time.time()), "status": "ready"}
    os.makedirs(J(work, ".hs"), exist_ok=True); wj(J(work, ".hs", "publish-%s.json" % plat), plan); return plan, ""
def cmd_publish(work, args):
    if not args: sys.exit("publish <work> list | <المنصة> [--at \"2026-10-12 20:00\"] | done <المنصة> <الرابط>")
    if args[0] == "list":
        for k, v in publish_platforms().items(): print("%s  %s%s" % (k, v["ar"], "  (خاص)" if v.get("private") else ""))
        return
    if args[0] == "done":
        p = J(work, ".hs", "publish-%s.json" % args[1]); plan = rj(p, {}) or {}; plan.update(status="done", link=(args[2] if len(args) > 2 else ""), doneAt=int(time.time())); wj(p, plan)
        say(work, "انتشر على %s %s" % (args[1], plan.get("link", "")), "done"); notify_quiet("انتشر المقطع على %s %s" % (args[1], plan.get("link", "")), title="Hojas Studio: انتشر"); print("تمام."); return
    when = None
    if "--at" in args: i = args.index("--at"); when = args[i + 1]; del args[i:i + 2]
    plan, err = publish_plan(work, args[0], when)
    if not plan: sys.exit(err)
    print(json.dumps(plan, ensure_ascii=False, indent=1))
    print("\nخطوات النشر: اقرأ قسم «النشر» في SKILL.md%s. وقف قبل زر النشر النهائي واطلب موافقته." % ((" ثم " + plan["guide"]) if plan.get("guide") else ""))

# ───────────────────────── 4.1: تحديث السكل ─────────────────────────
def cmd_update():
    if not os.path.isdir(os.path.join(HERE, ".git")):
        print("هذي النسخة منزّلة كملف مضغوط. للتحديث: نزّل النسخة الجديدة من https://github.com/rakaga66/hojas-studio وشغّل التثبيت مرة ثانية.\nأو ثبّتها بـ git عشان يصير التحديث أمر واحد (شوف README)."); return
    if not shutil.which("git"): sys.exit("ما لقيت git على الجهاز.")
    r = subprocess.run(["git", "-C", HERE, "pull", "--ff-only"], capture_output=True, text=True); print((r.stdout + r.stderr).strip())
    if r.returncode == 0: print("الإصدار الحين: " + (open(os.path.join(HERE, "VERSION")).read().strip() if os.path.exists(os.path.join(HERE, "VERSION")) else "?"))

# ───────────────────────── 4.2: أسلوب «ورق متحرك» وأسلوب «الدحيح» ─────────────────────────
KIN_STOP = set("في من على الى إلى عن مع اللي الي التي الذي هذا هذي هذه ذا ذي و ف يا لو ما لا هو هي انا أنا انت إنت انتو إنتوا كان كانت يعني بس كل عشان علشان لأن لان او أو ثم بعد قبل عند فيه فيها منه منها له لها لي لك هنا هناك اذا إذا لما حتى قد لقد وش ايش إيش شي شيء كذا".split())
def kin_compose(words, i):
    """يحوّل كلام جملة لنص ورق متحرك: سطر صغير، كلمة كبيرة (أطول كلمة لها معنى)، وصندوق أسود كل ثالث شاشة."""
    ws = [w for w in words if w.strip()]
    if not ws: return ""
    if len(ws) <= 2: return "* " + " ".join(ws)
    cand = [j for j, w in enumerate(ws) if _norm(w) not in KIN_STOP and len(_norm(w)) >= 3] or list(range(len(ws)))
    late = [j for j in cand if j >= len(ws) * 0.35] or cand
    k = max(late, key=lambda j: (len(_norm(ws[j])), j))
    big = [ws[k]]
    if k + 1 < len(ws) and len(_norm(ws[k + 1])) <= 4 and len(ws) - k - 2 >= 0 and len(" ".join(big + [ws[k + 1]])) <= 14: big.append(ws[k + 1])
    pre, post = ws[:k], ws[k + len(big):]
    lines = []
    for j in range(0, len(pre), 6): lines.append(" ".join(pre[j:j + 6]))
    lines.append("* " + " ".join(big))
    if post: lines.append(("> " if i % 3 == 2 and len(post) <= 3 else "") + " ".join(post))
    return "\n".join(lines)
def kin_auto(work, a=None, b=None, deco="flowers", card_end=False):
    caps = rj(J(work, "caps.json")) or sys.exit("ما فيه caps.json")
    cards = [c for c in caps["cards"] if (a is None or c["e"] > a) and (b is None or c["s"] < b)]
    if not cards: sys.exit("ما فيه كلام بهالمدى")
    sp = J(work, "studio.json"); st = load_studio(work); hs = hs_of(st); Ls = hs.setdefault("layers", [])
    lo = a if a is not None else cards[0]["s"]; hi = b if b is not None else cards[-1]["e"]
    Ls[:] = [L for L in Ls if not (L.get("type") == "kinetic" and L.get("auto") and float(L["s"]) < hi and float(L["e"]) > lo)]
    ids = []
    for i, c in enumerate(cards):
        s0 = max(lo, c["s"] - (0.12 if i else 0)); e0 = min(hi, cards[i + 1]["s"] - 0.12) if i + 1 < len(cards) else min(hi, c["e"] + 0.35)
        if e0 - s0 < 0.4: continue
        L = {"type": "kinetic", "s": round(s0, 3), "e": round(e0, 3), "text": kin_compose([w["t"] for w in c["w"]], i), "deco": deco if i == 0 or deco == "flowers" else "none", "auto": True, "track": 2}
        if i == 0 and deco == "badges": L["deco"] = "badges"
        L["id"] = new_id(Ls); Ls.append(L); ids.append(L["id"])
    if ids and len(ids) > 1:   # كل الشاشات متصلة: آخر وحدة تخلص على أول اللي بعدها
        ks = [L for L in Ls if L.get("id") in ids]; ks.sort(key=lambda L: L["s"])
        for x, y in zip(ks, ks[1:]):
            if 0 < y["s"] - x["e"] < 0.35: x["e"] = y["s"]
    if card_end and ids: Ls[-1]["card"] = "profile"
    wj(sp, st); return ids
def cmd_kinetic(work, args):
    sub = args[0] if args else "help"
    def o(nm, d=None):
        if nm in args: i = args.index(nm); v = args[i + 1]; del args[i:i + 2]; return v
        return d
    if sub == "auto":
        a = o("--from"); b = o("--to"); deco = o("--deco", "flowers"); end = "--profile" in args
        ids = kin_auto(work, float(a) if a else None, float(b) if b else None, deco, end)
        print("انضافت %d شاشة ورق متحرك: %s" % (len(ids), " ".join(ids))); print("راجع كل شاشة: layer list ثم layer set <id> text=\"سطر\\n* كلمة كبيرة\\n> صندوق\" card=terminal cardText=\"…\"  (الدليل: engine/references/styles.md)")
    elif sub == "clear":
        sp = J(work, "studio.json"); st = load_studio(work); hs = hs_of(st); n0 = len(hs.get("layers") or []); hs["layers"] = [L for L in hs.get("layers") or [] if L.get("type") != "kinetic"]; wj(sp, st); print("انحذفت %d شاشة" % (n0 - len(hs["layers"])))
    elif sub == "set":
        sp = J(work, "studio.json"); st = load_studio(work); hs = hs_of(st); hs["kin"] = {**(hs.get("kin") or {}), **parse_kv(args[1:])}; wj(sp, st); print(json.dumps(hs["kin"], ensure_ascii=False))
    else: sys.exit("kinetic <work> auto [--from ث --to ث] [--deco flowers|badges|both|none] [--profile] | clear | set mark=@حسابك avatar=assets/me.jpg font=Cairo")
DAHIH_CAP = {"on": True, "font": "Cairo", "weight": 800, "size": 34, "color": "#FFFFFF", "active": "#FFFFFF", "bg": "box", "bgColor": "#E8541E", "bgOpacity": 1,
             "y": 63.2, "x": 71, "width": 440, "lines": 1, "chunk": 4, "shadow": False, "stroke": 0, "enter": "pop", "hl": "none"}
def cmd_dahih(work, args):
    sub = args[0] if args else "help"; rest = args[1:]
    def o(nm, d=None):
        if nm in rest: i = rest.index(nm); v = rest[i + 1]; del rest[i:i + 2]; return v
        return d
    sp = J(work, "studio.json"); st = load_studio(work); hs = hs_of(st); D = hs.setdefault("dahih", {})
    if sub == "on":
        D.update({"on": True, "layout": o("--layout", D.get("layout") or "window"), "bg": o("--bg", D.get("bg") or "paper")})
        for k in ("title", "tag", "avatar", "logo", "side", "font"):
            v = o("--" + k)
            if v is not None: D[k] = v
        D.setdefault("title", ""); D.setdefault("bgs", [])
        if "--keep-cap" not in rest:
            cap = dict(DAHIH_CAP)
            if D["layout"] == "full": cap.update({"y": 70, "x": 50, "size": 52, "width": 760})
            elif D.get("side") == "left": cap["x"] = 29
            hs["cap"] = {**(hs.get("cap") or {}), **cap}
        wj(sp, st); print("أسلوب الدحيح شغّال: %s" % json.dumps(D, ensure_ascii=False))
        try: vision_ensure(work)
        except Exception as e: print("تنبيه: قص الشخص ما جهز (%s). المكتب يظهر بدون قص لين يجهز." % str(e)[:120])
    elif sub == "bg":
        if not rest: sys.exit("dahih <work> bg paper|navy|orange|green|dark|original --at <ثانية>")
        at = float(o("--at", 0)); D.setdefault("bgs", []); D["bgs"] = [b for b in D["bgs"] if abs(float(b["s"]) - at) > 0.05] + [{"s": round(at, 3), "mode": rest[0]}]; D["bgs"].sort(key=lambda b: b["s"])
        wj(sp, st); print("الخلفيات: " + " · ".join("%s من %.2f" % (b["mode"], b["s"]) for b in D["bgs"]))
        try: vision_ensure(work)
        except Exception as e: print("تنبيه: " + str(e)[:120])
    elif sub == "off": D["on"] = False; wj(sp, st); print("انطفى أسلوب الدحيح (الكروت باقية)")
    elif sub == "show": print(json.dumps(D, ensure_ascii=False, indent=1))
    else: sys.exit("dahih <work> on [--title \"…\"] [--tag \"#…\"] [--avatar assets/x.jpg] [--logo claude|none|assets/x.png] [--layout window|full] [--side right|left] [--bg paper] | bg <mode> --at ث | off | show")

# ───────────────────────── 4.3: مقاطع من حلقة طويلة (بودكاست مترجم) ─────────────────────────
# 4.27: شكل البودكاست الافتراضي (من مقطع أرسله راكان): سطرين أبيض بظل بدون خلفية، والكلمة المهمة ذهبي، واسم المتكلم بصندوق غامق فوق يمين
POD_CAP = {"on": True, "font": "Cairo", "weight": 800, "size": 56, "color": "#FFFFFF", "active": "#F5A524", "bg": "none", "shadow": True, "stroke": 0,
           "hl": "color", "enter": "fade", "chunk": 0, "lines": 2, "width": 760, "x": 50, "y": 74, "actScale": 1}
POD_NAME = {"type": "text", "x": 0.74, "y": 0.088, "size": 44, "weight": 800, "font": "Cairo", "color": "#FFFFFF", "bg": "box", "bgColor": "#1E1915", "bgOpacity": 0.88, "track": 3, "anim": "fade", "auto": "name"}
def title_clean(s):
    """عنوان أو نص مرشّح من ترجمة يوتيوب: بدون &gt;&gt; ولا [موسيقى]."""
    s = html.unescape(str(s or "")); s = re.sub(r"\[[^\]]*\]", " ", s.replace(">>", " ")); return re.sub(r"\s+", " ", s).strip()
def cap_clean(w):
    """4.31: كلمة نظيفة من ترجمة يوتيوب: بدون &gt;&gt; ولا [موسيقى]."""
    w = html.unescape(str(w or "")).lstrip(">").strip()
    return "" if not w or re.fullmatch(r"\[[^\]]*\]", w) else w
POD_NOTNAME = set("الله ربي ربنا نفسك نفسي نفسه الناس الآخرين الاخرين اهلك أهلك اهلي أهلي زوجتك زوجك اولادك أولادك الفلوس المال الوقت النجاح الحياة".split())
def pod_repair(work):
    """يصلّح مقطع بودكاست سوّته نسخة أقدم: يشيل &gt;&gt; و[موسيقى] من الكابشن، ويصحّح اسم المتكلم لو طلع «الله» وأمثالها. ياخذ نسخة قبل."""
    cp = J(work, "caps.json"); caps = rj(cp, None); ch = False
    if caps and "&gt;" in json.dumps(caps, ensure_ascii=False) or (caps and any(re.fullmatch(r"\[[^\]]*\]", str(w.get("t") or "")) for c in caps.get("cards") or [] for w in c.get("w") or [])):
        os.makedirs(J(work, ".hs"), exist_ok=True); shutil.copy2(cp, J(work, ".hs", "caps.before-4.31.json"))
        cards = []
        for c in caps.get("cards") or []:
            ws = [{**w, "t": cap_clean(w.get("t"))} for w in c.get("w") or []]; ws = [w for w in ws if w["t"]]
            if ws: cards.append({**c, "w": ws})
        caps["cards"] = cards; wj(cp, caps); ch = True
    for fn in ("a.json", "fixes.json"):
        fp = J(work, fn); dj = rj(fp, None)
        if dj and ("&gt;" in json.dumps(dj, ensure_ascii=False) or "[موسيقى]" in json.dumps(dj, ensure_ascii=False)):
            if fn == "a.json":
                for sg in dj.get("segments") or []:
                    sg["words"] = [{**x, "word": cap_clean(x.get("word"))} for x in sg.get("words") or [] if cap_clean(x.get("word"))]; sg["text"] = " ".join(x["word"] for x in sg["words"])
                dj["segments"] = [sg for sg in dj.get("segments") or [] if sg.get("words")]; dj["text"] = " ".join(sg["text"] for sg in dj["segments"])
            else:
                dj["fix"] = [[cap_clean(x) for x in f if cap_clean(x)] for f in dj.get("fix") or []]; dj["fix"] = [f for f in dj["fix"] if f]
            wj(fp, dj); ch = True
    st = load_studio(work); h = hs_of(st); P_ = h.get("pod") or {}
    for k_, o_ in (("title", h), ("title", P_)):
        if o_.get(k_) and title_clean(o_[k_]) != o_[k_]: o_[k_] = title_clean(o_[k_]); ch = True; wj(J(work, "studio.json"), st)
    epc = os.path.join(os.path.dirname(os.path.abspath(work)), "clips.json"); ec = rj(epc, None)
    if ec and "&gt;" in json.dumps(ec, ensure_ascii=False):
        for x in (ec.get("clips") or []) + (ec.get("cands") or []):
            for k_ in ("title", "hook", "text"):
                if x.get(k_): x[k_] = title_clean(x[k_])
        wj(epc, ec); ch = True
    if P_.get("on"):
        cfg = rj(os.path.join(os.path.dirname(os.path.abspath(work)), "clips.json"), {}) or {}; good = pod_speaker(cfg.get("title") or "")
        for L in h.get("layers") or []:
            if L.get("auto") == "name" and (str(L.get("text") or "").split() or [""])[0] in POD_NOTNAME:
                if good: L["text"] = good; P_["speaker"] = good
                else: L["off"] = True
                ch = True; wj(J(work, "studio.json"), st)
    return ch
def pod_speaker(title):
    """اسم الضيف من عنوان الحلقة: «… مع ياسر الحزيمي | بودكاست فنجان» ← ياسر الحزيمي."""
    t_ = str(title or ""); m = re.search(r"(?:^|\s)(?:مع|with|ft\.?|feat\.?)\s+([^|\-–—:(\[\]#،,]{3,40})", t_, re.I)
    nm = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    if nm and nm.split()[0] not in POD_NOTNAME and nm not in POD_NOTNAME: return nm
    # 4.31: «مركزية العلاقة مع الله | ياسر الحزيمي»: «الله» مو اسم، والاسم هو الجزء اللي بعد |
    for part in re.split(r"\s*[|｜]\s*|\s+[-–—]\s+", t_)[1:]:
        p_ = part.strip(); w_ = p_.split()
        if 2 <= len(w_) <= 3 and not re.search(r"بودكاست|podcast|حلقة|episode|فنجان|ثمانية|#|\d", p_, re.I) and w_[0] not in POD_NOTNAME: return p_
    return ""
def pod_hot(segs, every=8):
    """كلمة مهمة وحدة لكل 8 كلمات تقريباً (تنلوّن ذهبي). Claude يقدر يغيّرها بعدين."""
    out = []
    for s in segs:
        ws = [x["word"].strip() for x in (s.get("words") or []) if x.get("word")]
        for i in range(0, len(ws), every):
            best, sc = None, 0
            for w in ws[i:i + every]:
                b = re.sub(r"[^\w]", "", _bare(w.lower()))
                if not b or b in STOP_W or w in WEAK_START or len(b) < 4: continue
                v = len(b) + (4 if (b in HOOK_W or w in HOOK_W) else 0) + (3 if w.startswith(("ال", "وال", "بال", "فال", "لل")) else 0)   # الأسماء أوضح من الأفعال
                if v > sc: best, sc = w, v
            if best and best not in out: out.append(best)
    return out
def tsec(v):
    """12:30 · 1:02:03 · 754.2 ← ثواني"""
    v = str(v).strip(); p = v.split(":")
    try:
        x = 0.0
        for k in p: x = x * 60 + float(k)
        return x
    except ValueError: sys.exit("وقت غلط: " + v + " (اكتبه 12:30 أو 750)")
def tfmt(x): x = int(round(x)); return ("%d:%02d:%02d" % (x // 3600, x // 60 % 60, x % 60)) if x >= 3600 else "%d:%02d" % (x // 60, x % 60)
def clips_cfg(d): return rj(J(d, "clips.json"), {}) or {}
# ───────────────────────── 4.4: سحب من رابط · ترشيح اللقطات · تجهيز للمونتاج اليدوي ─────────────────────────
def probe_dur(path):
    try: return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip() or 0)
    except Exception: return 0.0
def whisper_run(wav, outdir, model="medium", lang=None, logf=None):
    cmd = [PY, "-m", "whisper", wav, "--model", model, "--word_timestamps", "True", "--output_format", "json", "--output_dir", outdir, "--fp16", "False", "--verbose", "False"]
    if lang: cmd += ["--language", lang]
    with open(logf or os.devnull, "w") as lg: r = subprocess.run(cmd, stdout=lg, stderr=subprocess.STDOUT)
    out = J(outdir, os.path.splitext(os.path.basename(wav))[0] + ".json")
    if r.returncode != 0 or not os.path.isfile(out): raise RuntimeError("التفريغ فشل: شوف " + (logf or "whisper") + " (هل Whisper مثبّت؟ python -m whisper --help)")
    return out
def clips_scan(src, d, model="medium", lang=None, log=print):
    """يفرّغ الحلقة الطويلة كاملة مرة وحدة، ويجهّز نسخة خفيفة للمعاينة وصورة."""
    if not os.path.isfile(src): raise RuntimeError("ما لقيت الفيديو: " + src)
    os.makedirs(J(d, ".hs"), exist_ok=True); cfg = clips_cfg(d)
    pr = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,width,height", "-of", "json", src], capture_output=True, text=True)
    info = json.loads(pr.stdout or "{}"); vs = [s for s in info.get("streams", []) if s.get("codec_type") == "video"]
    dur = float((info.get("format") or {}).get("duration") or 0)
    cfg.update({"src": src, "dur": round(dur, 2), "w": vs[0]["width"] if vs else 0, "h": vs[0]["height"] if vs else 0}); cfg.setdefault("clips", []); cfg.setdefault("cands", [])
    wj(J(d, "clips.json"), cfg)
    th = J(d, ".hs", "th.jpg")
    if not os.path.isfile(th): subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "%.2f" % max(0, dur * 0.12), "-i", src, "-frames:v", "1", "-vf", "scale=-2:360", th], capture_output=True)
    pv = J(d, ".hs", "preview.mp4")
    def mk_preview():
        if os.path.isfile(pv): return
        tmp = pv + ".tmp.mp4"
        r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf", "scale=-2:'min(480,ih)'", "-c:v", "libx264", "-preset", "veryfast", "-crf", "30", "-g", "60", "-c:a", "aac", "-b:a", "64k", "-movflags", "+faststart", tmp], capture_output=True)
        if r.returncode == 0: os.replace(tmp, pv)
    pth = threading.Thread(target=mk_preview, daemon=True); pth.start()
    wav, aj = J(d, "long.wav"), J(d, "long.json")
    if not os.path.isfile(wav): subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
    if not os.path.isfile(aj):
        log("أفرّغ الحلقة كاملة (%s). تقريباً %d دقيقة على جهاز عادي، شغّله بالخلفية." % (tfmt(dur), max(2, int(dur / 60 * (0.6 if model in ("small", "base") else 1.2)))))
        whisper_run(wav, d, model, lang, J(d, "whisper.log"))
    a = rj(aj); cfg = clips_cfg(d); cfg["lang"] = lang or a.get("language") or "en"; segs = a.get("segments") or []
    L = ["# %s · %s · اللغة: %s" % (os.path.basename(src), tfmt(dur), cfg["lang"]), ""]
    for s in segs: L.append("[%s] %s" % (tfmt(s["start"]), s["text"].strip()))
    open(J(d, "transcript.txt"), "w", encoding="utf-8").write("\n".join(L)); wj(J(d, "clips.json"), cfg)
    pth.join(); return cfg
def clip_bounds(A, a_, b_, src_dur=None, back=6.0, ahead=8.0):
    """4.9: لو حد اللقطة طاح بنص جملة: البداية ترجع لأول الجملة، والنهاية تكمل لين آخرها (بحد 6 ث قبل و8 ث بعد).
    قبل: المقطع كان ينتهي والمتكلم لسه يتكلم."""
    segs = [s for s in (A.get("segments") or []) if s.get("end", 0) > s.get("start", 0)]
    if not segs: return a_, b_
    for s in segs:
        if s["start"] < a_ < s["end"] - 0.15:
            if a_ - s["start"] <= back: a_ = max(0.0, s["start"] - 0.12)
            else:
                ws = [w for w in s.get("words") or [] if w["start"] >= a_ - 0.05]
                if ws: a_ = max(0.0, ws[0]["start"] - 0.1)
            break
    for s in segs:
        if s["start"] + 0.15 < b_ < s["end"]:
            if s["end"] - b_ <= ahead: b_ = s["end"] + 0.3
            else:
                ws = [w for w in s.get("words") or [] if w["end"] <= b_ + 0.05]
                if ws: b_ = ws[-1]["end"] + 0.25
            break
    try:   # 4.32: يكمل لين آخر الفكرة، ويبدأ من أولها
        for t0, t1 in thoughts(segs):
            if segs[t0]["start"] - 0.2 <= a_ <= segs[t1]["end"] and a_ - segs[t0]["start"] <= 15: a_ = max(0.0, min(a_, segs[t0]["start"] - 0.12))
            if segs[t0]["start"] <= b_ - 0.3 and b_ <= segs[t1]["end"] + 0.05 and segs[t1]["end"] - b_ <= 45: b_ = max(b_, segs[t1]["end"] + 0.3)
    except Exception: pass
    if src_dur: b_ = min(b_, src_dur)
    return round(a_, 3), round(b_, 3)
def clip_make(d, a_, b_, title="", credit="", name=None, style=None):
    cfg = clips_cfg(d)
    if not cfg.get("src") and not cfg.get("remote"): raise RuntimeError("شغّل أول: hs clips scan <الفيديو> " + d)
    if b_ <= a_ + 3: raise RuntimeError("المقطع قصير جداً")
    n = len(cfg.get("clips") or []) + 1; name = name or "clip-%d" % n
    w = J(d, re.sub(r"[^\w\-]+", "-", name).strip("-") or "clip-%d" % n)
    while os.path.exists(J(w, "src.mov")): n += 1; w = J(d, "clip-%d" % n)
    os.makedirs(w, exist_ok=True)
    A = rj(J(d, "long.json"), {}) or {}
    remote = cfg.get("remote") if not (cfg.get("src") and os.path.isfile(cfg["src"])) else None
    a_, b_ = clip_bounds(A, a_, b_, float(cfg.get("dur") or 0) if remote else probe_dur(cfg["src"]))   # 4.9: البداية والنهاية على حدود جملة، ما ينقطع وهو يتكلم
    fo = max(0.0, b_ - a_ - 0.25); src_, off_ = cfg.get("src"), a_
    if remote:   # 4.26: ينزل الجزء هذا بس (مع ثانية زيادة من كل طرف) بدل الحلقة كاملة
        pa = max(0.0, a_ - 1.0); src_ = yt_section(remote, pa, b_ + 1.0, J(w, ".part.mp4")); off_ = a_ - pa
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "%.3f" % off_, "-t", "%.3f" % (b_ - a_), "-i", src_, "-c:v", "libx264", "-preset", "veryfast", "-crf", "17",
                    "-af", "afade=t=in:st=0:d=0.06,afade=t=out:st=%.3f:d=0.25" % fo, "-c:a", "aac", "-b:a", "192k", J(w, "src.mov")], check=True)
    if remote:
        try: os.remove(J(w, ".part.mp4"))
        except OSError: pass
    segs = []; fix = []
    for s in A.get("segments") or []:
        ws = [{**x, "word": cap_clean(x.get("word"))} for x in (s.get("words") or []) if x["start"] >= a_ - 0.05 and x["end"] <= b_ + 0.05]
        ws = [x for x in ws if x["word"]]
        if not ws: continue
        ws = [{**x, "start": round(max(0, x["start"] - a_), 3), "end": round(max(0, x["end"] - a_), 3)} for x in ws]
        segs.append({"start": ws[0]["start"], "end": ws[-1]["end"], "text": " ".join(x["word"].strip() for x in ws), "words": ws}); fix.append([x["word"].strip() for x in ws])
    lang = cfg.get("lang", "en")
    wj(J(w, "a.json"), {"text": " ".join(s["text"] for s in segs), "segments": segs, "language": lang})
    style = style or ("pod" if (cfg.get("lang", "en") != "ar" or (cfg.get("want") or {}).get("pod")) else "plain")   # 4.27: اللي من صفحة البودكاست بودكاست حتى لو عربي
    if not os.path.isfile(J(w, "fixes.json")): wj(J(w, "fixes.json"), {"fix": fix, "hot": pod_hot(segs) if style == "pod" else []})
    eng = find_engine(None)
    if eng and not os.path.isfile(J(w, "compose.html")): shutil.copy(os.path.join(eng, "scripts", "compose.REFERENCE.html"), J(w, "compose.html"))
    if not os.path.isfile(J(w, "theme.json")): wj(J(w, "theme.json"), dict(THEME_DEF))
    wj(J(w, "sfx.json"), {"outro": 0})
    st = load_studio(w); hs = hs_of(st)
    if title: hs["title"] = title
    if style == "pod":
        want_ = cfg.get("want") or {}; trl = want_.get("tr") or ("ar" if lang != "ar" else "en")
        spk = want_.get("speaker") or pod_speaker(cfg.get("title"))
        hs["pod"] = {"on": True, "title": title, "titleOn": False, "speaker": spk, "credit": credit, "lang": lang, "orig": lang != trl, "tr": trl, "src": os.path.basename(cfg.get("src") or "") or cfg.get("remote") or "", "from": round(a_, 2), "to": round(b_, 2)}
        hs["vpos"] = {**(hs.get("vpos") or {}), "still": True}   # 4.27: بدون زوم يتغيّر بين اللقطات
        if spk: hs.setdefault("layers", []).append({**POD_NAME, "id": "LN1", "text": spk, "s": 0, "e": round(b_ - a_, 2)})
        if want_.get("dub"): hs["dubWant"] = want_["dub"]   # 4.26: طلب دبلجة: Claude يكمّلها (hs dub)
        H = host_cfg()
        if want_.get("host", False) and H.get("on"):   # 4.26: شخصية المقدّم الثابتة بزاوية المقطع
            hs.setdefault("layers", []).append({"id": "LH1", "type": "char", "char": H.get("char") or "robo", "color": H.get("color") or "#D97757", "x": 0.84, "y": 0.8, "size": 0.16, "s": 0, "e": round(b_ - a_, 2), "track": 3, "auto": "host"})
            if H.get("name") and H["name"].strip() != spk: hs["layers"].append({"id": "LH2", "type": "text", "text": H["name"], "x": 0.84, "y": 0.885, "size": 34, "weight": 800, "color": "#FFFFFF", "bg": "box", "bgColor": "#141413", "s": 0, "e": round(b_ - a_, 2), "track": 3, "anim": "fade", "auto": "host"})
        hs["cap"] = {**(hs.get("cap") or {}), **POD_CAP}; hs["en"] = {**(hs.get("en") or {}), "on": True}
    hs["clip"] = {"from": round(a_, 2), "to": round(b_, 2), "ep": os.path.basename(d)}
    wj(J(w, "studio.json"), st)
    try: ident_apply(w, (cfg.get("want") or {}).get("identity") or None)   # 4.37: نفس هويته بكل مقطع (صندوق الاسم ولون الكلمة والخط)
    except Exception: pass
    if os.path.isfile(J(d, "brief.json")) and not os.path.isfile(J(w, "brief.json")): shutil.copy(J(d, "brief.json"), J(w, "brief.json"))
    cfg = clips_cfg(d); cfg.setdefault("clips", []).append({"name": os.path.basename(w), "from": round(a_, 2), "to": round(b_, 2), "title": title, "credit": credit}); wj(J(d, "clips.json"), cfg)
    return w

# ── ترشيح اللقطات: تقدير «كم تضرب» من النص والصوت (بدون إنترنت). Claude يراجعه ويعدّله بـ clips cand ──
HOOK_W = ("ليش ليه كيف شلون وش ايش إيش هل سر أسرار اسرار أكبر اكبر أخطر اخطر أهم اهم أسوأ اسوأ أفضل افضل غلط خطأ غلطة الحقيقة حقيقة محد مستحيل انتبه تخيل تخيّل صدمة فلوس مليون ملايين ريال دولار نصيحة قصة فشلت فشل نجحت نجاح تجربتي المشكلة السبب ترى والله للأسف أبدا أبداً ابدا "
          "why how what secret biggest worst best mistake truth never nobody stop million money dollars imagine crazy insane story failed problem reason honestly actually wrong rich broke").split()
HOOK_P = ("لا تسوي", "لا تسوّي", "ما أحد", "ما احد", "أول مرة", "اول مرة", "آخر مرة", "كل يوم", "لو تبي", "أقول لك", "اقول لك", "the problem", "here's", "you need", "you should", "don't", "the reason", "no one", "nobody tells")
WEAK_START = set("و ف بس لكن يعني اللي هذا هذي فهذا وهذا وبعدين وبعدها فبعدين and but so because or which that then it he she they also".split())
STOP_W = set("في من على عن إلى الى مع هذا هذي هذه اللي التي الذي هو هي هم انا أنا انت أنت كان يكون ما لا لم لن قد ان أن إن كل بعض او أو ثم يعني بس عشان علشان the a an of to in on for and or is are was were be it this that with you i we they".split())
def _bare(w):
    for p in ("وال", "بال", "فال", "لل", "ال", "و", "ف"):
        if w.startswith(p) and len(w) - len(p) >= 2: return w[len(p):]
    return w
def _tok(s): return [w for w in re.sub(r"[^\w\s]", " ", str(s).lower()).split() if w]
# 4.32: الكلام أفكار كاملة. المقطع يبدأ من أول الفكرة ويخلص بآخرها، ولو طولها أكثر من اللي طلبه عادي، ولو طويلة مرة ما تنقص بنصها: تنترك
WEAK_END = set("في على من عن الى إلى اللي الي التي الذي عشان علشان لأن لان لانه لأنه إن ان انه أنه إنه و ف بس لكن يعني مع هو هي كان كانت يكون ما لا لو اذا إذا ثم حتى عند بين زي مثل اكثر أكثر of the to and because that a an with for is are was so but if when than".split())
CONT_START = WEAK_START | set("ولكن ولا وبعدين وكذا وهذا وهذي وأنا وانا وهو وهي وهم واللي وإذا واذا ولو وحتى وكان وكانت ويعني وبس فلما فإذا فاذا فهو فهي فأنا فانا فاللي فيعني فكان لأن لان لانه لأنه عشان علشان يعني ثم حتى مثلا مثلاً because and but so then which".split())
def thoughts(segs, gap=1.2, fine=False):
    """[(أول جملة، آخر جملة)] لكل فكرة: الجملة تكمل اللي بعدها لو ما خلصت (تنتهي بـ«في» أو «لأن»…) أو اللي بعدها تبدأ بـ«و/بس/يعني/لأن»…، أو انقطعت بدون سكتة.
    وتنقطع الفكرة عند سكتة طويلة أو لما يتغيّر المتكلم."""
    out, s0 = [], 0; pause = 0.8 if fine is False else 0.55
    punct = sum(1 for x in segs if re.search(r"[.!?؟…]\s*$", str(x.get("text") or "").strip())) > len(segs) * 0.2   # ترجمة يوتيوب التلقائية بدون ترقيم: نعتمد على السكتات
    for k in range(len(segs) - 1):
        a, b = segs[k], segs[k + 1]; ta, tb = _tok(a.get("text")), _tok(b.get("text")); g = float(b["start"]) - float(a["end"])
        txa = str(a.get("text") or "").strip(); endp = bool(re.search(r"[.!?؟…]\s*$", txa)); q = bool(re.search(r"[?؟]\s*$", txa))
        link = (ta and ta[-1] in WEAK_END) or (tb and tb[0] in CONT_START)
        if b.get("spk") and not q: cont = False
        elif punct: cont = g <= gap and (link or not endp or (q and g < 0.9))   # سؤال وجوابه فكرة وحدة
        else: cont = g < pause or (g <= 3.0 and bool(ta and ta[-1] in WEAK_END)) or (g <= gap and link)   # «… على» / «… اللي» ما تخلص فيها جملة
        if not cont: out.append((s0, k)); s0 = k + 1
    if segs: out.append((s0, len(segs) - 1))
    return out
def audio_rms(wav, step=0.5):
    try:
        import wave
        with wave.open(wav, "rb") as f:
            sr, n = f.getframerate(), f.getnframes(); hop = int(sr * step); out = []
            while True:
                raw = f.readframes(hop)
                if not raw: break
                a = array.array("h"); a.frombytes(raw[: len(raw) // 2 * 2])
                if sys.byteorder == "big": a.byteswap()
                out.append((sum(x * x for x in a[::8]) / max(1, len(a[::8]))) ** 0.5)
            return out
    except Exception: return []
def clips_suggest(d, n=None, ln=None, note=None, count=None, fresh=False):
    """count: كم مرشّح بالضبط (البودكاست: ضعف اللي طلبه). fresh: «هات غيرها» = مرشّحات جديدة ما تتداخل مع اللي شافها."""
    cfg = clips_cfg(d); A = rj(J(d, "long.json"), {}) or {}; segs = [s for s in A.get("segments") or [] if str(s.get("text", "")).strip()]
    if not segs: return []
    want = cfg.get("want") or {}
    if n: want["n"] = int(n)
    if ln: want["len"] = ln
    if note is not None: want["note"] = note
    cfg["want"] = want; n = int(want.get("n") or 6)
    try: mn, mx = [float(x) for x in str(want.get("len") or "25-75").split("-")]
    except ValueError: mn, mx = 25.0, 75.0
    mid = (mn + mx) / 2; topic = [w for w in _tok(want.get("note") or "") if len(w) > 2 and w not in STOP_W]
    rms = audio_rms(J(d, "long.wav")); med = sorted(rms)[len(rms) // 2] if rms else 0
    LP = learned() if (learned().get("n") or 0) >= 5 else {}
    wps = sorted(len(_tok(s["text"])) / max(0.3, s["end"] - s["start"]) for s in segs); wmed = wps[len(wps) // 2] or 2.5
    def hook_of(text):
        tk = _tok(text); low = " " + " ".join(tk) + " "; why = []; h = 0.0
        if re.search(r"[?؟]", text): h += 1; why.append("تبدأ بسؤال")
        hw = sum(1 for w in tk if w in HOOK_W or _bare(w) in HOOK_W) + sum(1 for p in HOOK_P if p in low)
        if hw: h += min(2, hw) * 0.7; why.append("فيها كلمة تشد")
        if re.search(r"\d|مليون|ألف|الف|million|thousand|percent|٪|%", text): h += 0.6; why.append("فيها رقم")
        return h, why
    def score(i, j):
        a, b = segs[i]["start"], segs[j]["end"]; dur = b - a; first = " ".join(s["text"] for s in segs[i:i + 2] if s["start"] - a < 8)
        allt = " ".join(s["text"] for s in segs[i:j + 1]); tk = _tok(allt)
        h, why = hook_of(first); sc = 1.6 * min(2.4, h)
        dens = sum(1 for w in tk if w in HOOK_W) / max(1, len(tk)) * 100; sc += min(1.2, dens * 0.35)
        f0 = (_tok(segs[i]["text"]) or [""])[0]
        if f0 in WEAK_START: sc -= 1.3
        else: sc += 0.4
        if re.search(r"[.!?؟。…]\s*$", segs[j]["text"].strip()): sc += 0.6; why.append("تنتهي بفكرة كاملة")
        else: sc -= 0.4
        gap = (segs[j + 1]["start"] - segs[j]["end"]) if j + 1 < len(segs) else 1.0
        if gap > 0.6: sc += 0.3
        rate = len(tk) / max(1, dur) / wmed
        if rate > 1.08: sc += min(0.8, (rate - 1) * 3); why.append("كلامها سريع وحماسي")
        if rms and med:
            seg = rms[int(a / 0.5): int(b / 0.5) + 1]
            if seg:
                lv = sum(seg) / len(seg) / med; pk = max(seg) / med
                if lv > 1.1: sc += min(0.9, (lv - 1) * 2.2); why.append("صوته عالي فيها")
                if pk > 2.2: sc += 0.3
        if topic:
            hit = sum(1 for w in set(topic) if any(w in x or x in w for x in tk if len(x) > 2))
            if hit: sc += 1.5 * hit / len(set(topic)); why.append("قريبة من طلبك")
        if dur <= mx: sc -= abs(dur - mid) / max(10, mx - mn) * 0.8
        if LP:   # 4.5: من أرقام مقاطعك المنشورة
            hw0 = hook_score(first)[1]; b0 = sum(LP.get(k, 0) for k, nm in (("q", "سؤال"), ("num", "رقم"), ("hookw", "كلمة تشد")) if nm in hw0)
            if LP.get("len") and LP["len"][0] <= dur <= LP["len"][1]: b0 += 0.5
            if b0 > 0.2: why.append("يشبه مقاطعك اللي ضربت")
            sc += b0
        return sc, why
    C = []; cap = min(max(mx * 2.0, mx + 30.0), 120.0)
    for fine in (False, True):   # لو الأفكار كلها أطول من اللي يصير، نجرّب سكتات أقصر (برضو ما ينقطع بنص جملة)
        TH = thoughts(segs, fine=fine); TS = {a for a, b in TH}; TE = {b for a, b in TH}
        if C and len(C) >= (count or n): break
        C = []
        for i in range(len(segs)):   # 4.32: يبدأ من أول فكرة ويخلص بآخر فكرة، وما ينقطع بنصها
          if i not in TS: continue
          best = None
          for j in range(i, len(segs)):
              if j not in TE or ((_tok(segs[j]["text"]) or [""])[-1] in WEAK_END): continue   # ما يخلص على «على» أو «اللي»
              dur = segs[j]["end"] - segs[i]["start"]
              if dur > cap: break
              if dur < mn * 0.8: continue
              sc, why = score(i, j)
              if dur > mx: sc -= (dur - mx) / max(10.0, mx) * 0.6   # أطول من طلبه: مقبول عشان الفكرة تكمل، بس الأقصر أحسن
              why = why + ["الفكرة كاملة"]
              if not best or sc > best[0]: best = (sc, why, j)
              if dur > mx: break   # أول فكرة تكمّل الطول تكفي، ما نزيد فوقها
          if best: C.append((best[0], i, best[2], best[1]))
    C.sort(key=lambda x: -x[0]); pick = []; seen = [tuple(x) for x in cfg.get("seen") or []] + [(c["from"], c["to"]) for c in cfg.get("cands") or [] if c.get("by") == "auto" and not c.get("made")]
    for sc, i, j, why in C:
        a, b = segs[i]["start"], segs[j]["end"]
        if any(min(b, p["to"]) - max(a, p["from"]) > 2 for p in pick): continue
        if fresh and any(min(b, s_[1]) - max(a, s_[0]) > 3 for s_ in seen): continue
        pick.append({"from": round(max(0, a - 0.15), 2), "to": round(b + 0.25, 2), "raw": sc, "why": list(dict.fromkeys(why))[:4], "hook": segs[i]["text"].strip()[:140], "text": " ".join(segs[k]["text"].strip() for k in range(i, j + 1))[:1600]})
        if len(pick) >= (count or max(n + 4, int(n * 1.6))): break
    if pick:
        lo, hi = min(p["raw"] for p in pick), max(p["raw"] for p in pick)
        for p in pick: p["score"] = int(round(48 + 46 * ((p.pop("raw") - lo) / ((hi - lo) or 1)) ** 0.8))
    keep = [c for c in cfg.get("cands") or [] if c.get("by") != "auto" or c.get("made") or c.get("keep")]
    ids = [int(re.sub(r"\D", "", c["id"]) or 0) for c in cfg.get("cands") or []]; k = max(ids or [0])
    for p in pick:
        if any(min(p["to"], c["to"]) - max(p["from"], c["from"]) > 3 for c in keep): continue
        k += 1; keep.append({"id": "c%d" % k, "by": "auto", "title": "", **p})
    if fresh: cfg["seen"] = [list(s_) for s_ in seen][-200:]
    keep.sort(key=lambda c: -c.get("score", 0)); cfg["cands"] = keep; wj(J(d, "clips.json"), cfg); return keep
def cmd_cand(rest):
    rest = list(rest)
    if not rest: sys.exit("clips cand <مجلد> list|add|set|rm|clear …")
    if os.path.isdir(rest[0]): d = rest.pop(0); sub = rest.pop(0) if rest else "list"
    else: sub = rest.pop(0); d = rest.pop(0) if rest else sys.exit("clips cand <مجلد> list")
    d = os.path.abspath(d); cfg = clips_cfg(d); C = cfg.setdefault("cands", [])
    def o(nm, dv=None):
        if nm in rest: i = rest.index(nm); v = rest[i + 1]; del rest[i:i + 2]; return v
        return dv
    by = o("--by", "claude")
    def upd(c):
        for k, f in (("--from", tsec), ("--to", tsec), ("--score", int), ("--title", str), ("--hook", str)):
            v = o(k)
            if v is not None: c[k[2:]] = f(v) if f is not str else v
        w = o("--why")
        if w is not None: c["why"] = [x.strip() for x in w.split("|") if x.strip()]
        c["by"] = by
    if sub == "list":
        for c in sorted(C, key=lambda c: -c.get("score", 0)):
            print("[%s] %s ← %s (%ds) %d%% %s%s\n     %s · %s" % (c["id"], tfmt(c["from"]), tfmt(c["to"]), c["to"] - c["from"], c.get("score", 0), c.get("by", ""), " ✓" if c.get("made") else "", c.get("title") or "", " · ".join(c.get("why") or [])))
        return
    if sub == "add":
        ids = [int(re.sub(r"\D", "", c["id"]) or 0) for c in C]; c = {"id": "c%d" % (max(ids or [0]) + 1), "score": 70, "why": [], "title": ""}; upd(c)
        if "from" not in c or "to" not in c: sys.exit("لازم --from و --to")
        C.append(c); print("انضاف:", c["id"])
    elif sub == "set":
        cid = rest.pop(0) if rest else sys.exit("cand <مجلد> set <id> --score 88 --why \"…|…\" --title \"…\"")
        c = next((x for x in C if x["id"] == cid), None) or sys.exit("ما لقيت " + cid); upd(c); print("تعدّل:", cid)
    elif sub == "rm":
        ids = set(rest); cfg["cands"] = [c for c in C if c["id"] not in ids]; print("انشال:", " ".join(ids))
    elif sub == "clear": cfg["cands"] = [c for c in C if c.get("made")]; print("انمسحت المرشّحات")
    else: sys.exit("cand list|add|set|rm|clear")
    cfg["cands"].sort(key=lambda c: -c.get("score", 0)); wj(J(d, "clips.json"), cfg)
def clips_build(d, picks, edit="none", log=print):
    """picks: ["c1", …] أو [{"from","to","title"}]. edit: none · me (يجهّزها للتعديل اليدوي) · claude."""
    cfg = clips_cfg(d); C = {c["id"]: c for c in cfg.get("cands") or []}; out = []
    for i, p in enumerate(picks):
        c = C.get(p) if isinstance(p, str) else (C.get(p.get("id")) if isinstance(p, dict) and p.get("id") else p)
        if not c: log("ما لقيت: %s" % p); continue
        title = (p.get("title") if isinstance(p, dict) else None) or c.get("title") or re.sub(r"\s+", " ", c.get("hook") or "").strip()[:60]
        if isinstance(p, dict): c = {**c, **{k: p[k] for k in ("from", "to") if k in p}}
        log("أقص %s ← %s ..." % (tfmt(c["from"]), tfmt(c["to"])))
        w = clip_make(d, float(c["from"]), float(c["to"]), title_clean(title), cfg.get("credit", ""), None, None); out.append(w)
        cfg = clips_cfg(d)
        for x in cfg.get("cands") or []:
            if x["id"] == c.get("id"): x["made"] = os.path.basename(w)
        wj(J(d, "clips.json"), cfg)
    for w in out: studio_mode_set(w, "claude" if edit == "claude" else "manual")   # 4.18
    if edit in ("me", "claude"):   # 4.32: حتى مع «Claude يمنتج» تتجهّز أول، فلو Claude ما اشتغل (تسجيل دخول منتهي) المقاطع جاهزة تفتحها
        for w in out:
            try: prep(w, log=log)
            except Exception as e: log("التجهيز وقف بـ %s: %s" % (os.path.basename(w), e))
    elif edit == "claude" and out:
        task = ("سوّيت %d مقاطع من الحلقة %s:\n%s\nمنتج كل وحدة كاملة حسب <engine>/references/clips.md و MONTAGE.md من «خطة القص» (التفريغ جاهز فلا تعيده)."
                % (len(out), d, "\n".join("- " + w for w in out)))
        note = (cfg.get("want") or {}).get("note")
        if note: task += "\nطلب المستخدم: " + note
        claude_spawn(out[0], task, "مقاطع من حلقة")
    return out

# ── تجهيز مشروع للتعديل اليدوي بدون Claude: قص السكتات ← تفريغ ← كابشن ← زوم ← فريمات ──
THEME_DEF = {"bg": "#101014", "ink": "#FFFFFF", "acc": "#4C8DFF", "clay": "#3f7ff0", "mut": "#9A9AA5", "font": "Cairo", "grade": False, "badgeUntil": 0}
PREP_STEPS = ["cut", "transcribe", "captions", "zoom", "frames", "ready"]
def prep_state(work): return rj(J(work, ".hs", "prep.json"), {}) or {}
def prep(work, model=None, lang=None, keep_silence=False, log=print):
    eng = find_engine(None)
    if not eng: raise RuntimeError("ما لقيت المحرّك (engine)")
    S = os.path.join(eng, "scripts"); src = J(work, "src.mov"); os.makedirs(J(work, ".hs"), exist_ok=True)
    if not os.path.isfile(src): raise RuntimeError("ما لقيت src.mov في " + work)
    cfg = hub_cfg(); model = model or cfg.get("prepModel") or "medium"; lang = lang or cfg.get("prepLang") or None
    dur = probe_dur(src); t0 = time.time()
    def st(k, **kw):
        wj(J(work, ".hs", "prep.json"), {"stage": k, "i": PREP_STEPS.index(k), "n": len(PREP_STEPS) - 1, "t0": int(t0), "at": int(time.time()), "dur": round(dur, 1), **kw})
    def py(script):
        r = subprocess.run([PY, os.path.join(S, script), work], capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0: raise RuntimeError(script + ": " + (r.stderr or r.stdout).strip()[-400:])
        return r.stdout
    try:
        st("cut")
        if not os.path.isfile(J(work, "cut.json")):
            if keep_silence: wj(J(work, "cut.json"), {"keep": [[0, round(dur, 3)]], "total": round(dur, 3), "src_dur": round(dur, 3)})
            else: py("01_cut_plan.py")
        if not os.path.isfile(J(work, "a.json")):
            st("transcribe", eta=int(max(40, dur * (0.6 if model in ("small", "base", "tiny") else 1.6))))
            wav = J(work, "a.wav")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
            whisper_run(wav, work, model, lang, J(work, "whisper.log"))
        A = rj(J(work, "a.json"), {}) or {}
        if not os.path.isfile(J(work, "fixes.json")):
            wj(J(work, "fixes.json"), {"fix": [[(x.get("word") or "").strip() or "…" for x in (s.get("words") or [])] for s in A.get("segments") or []], "hot": []})
        st("captions")
        if not os.path.isfile(J(work, "caps.json")): py("02_captions.py")
        if not os.path.isfile(J(work, "theme.json")): wj(J(work, "theme.json"), dict(THEME_DEF))
        if not os.path.isfile(J(work, "sfx.json")): wj(J(work, "sfx.json"), {"outro": 0})
        st("zoom")
        if not os.path.isfile(J(work, "cutz.mp4")): py("03_cut_zoom.py")
        st("frames")
        vf = J(work, "vfr")
        if not os.path.isdir(vf) or not os.listdir(vf):
            vfr_extract(work, lambda *a: None)
        if not os.path.isfile(J(work, "compose.html")): shutil.copy(os.path.join(S, "compose.REFERENCE.html"), J(work, "compose.html"))
        try: notes_auto(work)   # 4.29: ملاحظات «لازم تعدّلها» (كلمة ما وضحت، كابشن سريع)
        except Exception: pass
        try:   # 4.28: الطبقات اللي انحطت قبل قص السكتات (اسم المتكلم مثلاً) ما تطول عن المقطع
            tot_ = float((rj(J(work, "caps.json"), {}) or {}).get("total") or 0); st_ = load_studio(work); ch_ = False
            for L_ in hs_of(st_).get("layers") or []:
                if tot_ and float(L_.get("e") or 0) > tot_ + 0.01 and float(L_.get("s") or 0) < tot_: L_["e"] = round(tot_, 3); ch_ = True
            if ch_: wj(J(work, "studio.json"), st_)
        except Exception: pass
        st("ready", done=True); projects_remember(work); return True
    except Exception as e:
        st(prep_state(work).get("stage") or "cut", err=str(e)[:400]); raise

# ── 4.4.1: خفيف على الجهاز ──
# الأداة (وكل اللي تشغّله: ffmpeg وwhisper وكروم) تشتغل بأولوية أقل من برامجك، فالكمبيوتر يبقى سلس وهي تفرّغ أو تصدّر.
# «light» (الافتراضي): أولوية أقل + نخلي ربع الأنوية لك · «full»: أقصى سرعة مثل قبل.
CPU_MODES = ("light", "full")
def cpu_mode(): m = os.environ.get("HS_CPU") or hub_cfg().get("cpu") or "light"; return m if m in CPU_MODES else "light"
def lighten(mode=None):
    mode = mode or cpu_mode(); n = os.cpu_count() or 4
    if mode == "light":
        use = str(max(1, n - max(2, n // 4)))
        for k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"): os.environ[k] = use
    else:
        for k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"): os.environ.pop(k, None)
    try:
        if os.name == "nt":
            import ctypes; k = ctypes.windll.kernel32; k.GetCurrentProcess.restype = ctypes.c_void_p
            k.SetPriorityClass(ctypes.c_void_p(k.GetCurrentProcess()), 0x4000 if mode == "light" else 0x20)   # BELOW_NORMAL · NORMAL (البرامج اللي نشغّلها تورثها)
        elif mode == "light" and os.getpriority(os.PRIO_PROCESS, 0) < 10: os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
    except Exception: pass
    return mode
_WD = {}
def whisper_device():
    """هل التفريغ يشتغل على كرت الشاشة؟ نسأل بعملية منفصلة (torch ثقيل) ونحفظ الجواب ساعة."""
    if _WD.get("t", 0) > time.time() - 3600: return _WD.get("v")
    v = None
    try:
        r = subprocess.run([PY, "-c", "import torch;print('gpu' if torch.cuda.is_available() else 'cpu')"], capture_output=True, text=True, timeout=60,
                           **({"creationflags": 0x08000000} if os.name == "nt" else {}))
        v = (r.stdout or "").strip().splitlines()[-1] if r.returncode == 0 and r.stdout.strip() else None
    except Exception: pass
    _WD.update(t=time.time(), v=v); return v
# ── 4.5.1: صفحة رمز الدخول من الجوال (6 خانات، لصق، إرسال تلقائي، رسالة واضحة لو غلط أو انقفل) ──
LOGIN_CSS = """*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}html,body{margin:0;height:100%}
body{background:#1f1e1d;color:#faf9f5;font-family:"IBM Plex Sans Arabic",system-ui,sans-serif;display:flex;align-items:center;justify-content:center;padding:24px 16px calc(24px + env(safe-area-inset-bottom))}
.c{width:100%;max-width:380px;text-align:center}.logo{width:44px;height:44px;margin:0 auto 18px;color:#faf9f5}.logo svg{display:block;width:100%;height:100%}
h1{font-size:24px;margin:0 0 8px;font-weight:700}p{color:#9c9a92;font-size:14.5px;line-height:1.8;margin:0 0 22px}
.d{display:flex;gap:8px;justify-content:center;direction:ltr;margin-bottom:18px}
.d input{width:46px;height:58px;border-radius:14px;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.05);color:#fff;font-size:26px;font-weight:600;text-align:center;outline:none;caret-color:#d97757;font-family:inherit}
.d input:focus{border-color:#d97757;background:rgba(217,119,87,.08)}.err .d input{border-color:rgba(239,106,90,.7)}
button{width:100%;height:52px;border:0;border-radius:14px;background:#d97757;color:#fff;font-size:17px;font-weight:600;font-family:inherit;cursor:pointer}button:disabled{opacity:.45}
.m{min-height:22px;font-size:13.5px;margin:-6px 0 14px;color:#ef6a5a}.h{margin-top:22px;padding:14px;border-radius:14px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);font-size:13px;color:#9c9a92;line-height:1.9;text-align:start}
.h b{color:#faf9f5;font-weight:600}a.btn,button.btn{display:flex;align-items:center;justify-content:center;width:100%;height:52px;border-radius:14px;font-size:16px;font-weight:600;font-family:inherit;text-decoration:none;margin-top:10px}a.btn.sec{background:transparent;color:#faf9f5;border:1px solid rgba(222,220,209,.18)}.st{display:inline-flex;align-items:center;gap:8px;font-size:13px;color:#9c9a92;margin-top:18px}.st i{width:8px;height:8px;border-radius:50%;background:#d97757;animation:pl 1.4s ease-in-out infinite}@keyframes pl{50%{opacity:.25}}.lk{color:#d97757}"""
def stopped_html(name=""):   # 4.21: صفحة «المشروع وقف» بتصميم المكتبة، وترجع لحالها أول ما يرجع
    logo = "<div class=logo><svg viewBox='0 0 260 260' aria-hidden=true><rect width=150.5 height=46.8 fill=currentColor /><rect x=62.5 y=106.6 width=197.5 height=46.8 fill=currentColor /><rect y=213.2 width=103.7 height=46.8 fill=currentColor /></svg></div>"
    return ("<!doctype html><html lang=ar dir=rtl><head><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1,viewport-fit=cover'><meta name=theme-color content='#1f1e1d'>"
            "<title>المشروع وقف · Hojas Studio</title><link href='https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;600;700&display=swap' rel=stylesheet><style>" + LOGIN_CSS + "</style></head><body>"
            "<div class=c>" + logo + "<h1>الاستوديو وقف</h1><p>تشغيل المشروع" + (" «" + html.escape(name) + "»" if name else "") + " انقفل (يصير لو قفلت الاستوديو أو انطفى الجهاز أو تحدّثت النسخة). شغلك كله محفوظ وما ضاع منه شي.</p>"
            "<button class=btn onclick='location.reload()'>حاول من جديد</button><a class='btn sec' href='/library'>ارجع للمكتبة</a>"
            "<div class=st><i></i>أحاول أوصله لحالي، وأول ما يرجع أفتحه لك</div></div>"
            "<script>setInterval(()=>{ fetch(location.href,{method:'HEAD',cache:'no-store'}).then(r=>{ if(r.ok) location.reload(); }).catch(()=>{}); },3000);</script></body></html>")
def login_html(action, where, n=6, err="", locked=False):
    msg = "انقفل الدخول من الجوال مؤقتاً بعد محاولات كثيرة غلط. جرّب بعد ربع ساعة، أو افتح من الكمبيوتر." if locked else err
    return ("<!doctype html><html lang=ar dir=rtl><head><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1,viewport-fit=cover'><meta name=theme-color content='#1f1e1d'>"
            "<title>رمز الدخول · Hojas Studio</title><link href='https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;600;700&display=swap' rel=stylesheet><style>" + LOGIN_CSS.replace("%", "%%") + "</style></head><body>"
            "<form class='c%s' method=get action='%s' id=f><div class=logo><svg viewBox='0 0 260 260' aria-hidden=true><rect width=150.5 height=46.8 fill=currentColor /><rect x=62.5 y=106.6 width=197.5 height=46.8 fill=currentColor /><rect y=213.2 width=103.7 height=46.8 fill=currentColor /></svg></div><h1>اكتب رمز الدخول</h1>"
            "<p>الرمز من %d أرقام، تلقاه %s.</p><div class=d id=d>%s</div><input type=hidden name=k id=k>"
            "<div class=m id=m>%s</div><button id=b%s>دخول</button>"
            "<div class=h><b>وين ألقى الرمز؟</b><br>على الكمبيوتر افتح المكتبة ← <b>جهازك</b> ← «افتحه من جوالك». تلقى الرمز تحت رمز QR، ومسح الرمز يدخلك على طول بدون كتابة.<br>لازم الجوال والكمبيوتر على نفس الواي فاي.</div></form>"
            "<script>const N=%d,D=[...document.querySelectorAll('.d input')],f=document.getElementById('f');"
            "const v=()=>D.map(x=>x.value).join('');function go(){ if(v().length===N){ document.getElementById('k').value=v(); document.getElementById('b').disabled=true; f.submit(); } }"
            "D.forEach((x,i)=>{ x.addEventListener('input',()=>{ x.value=x.value.replace(/\\D/g,'').slice(-1); if(x.value&&i<N-1) D[i+1].focus(); document.getElementById('m').textContent=''; f.classList.remove('err'); go(); });"
            "x.addEventListener('keydown',e=>{ if(e.key==='Backspace'&&!x.value&&i>0){ D[i-1].focus(); D[i-1].value=''; } });"
            "x.addEventListener('paste',e=>{ const t=(e.clipboardData.getData('text')||'').replace(/\\D/g,'').slice(0,N); if(!t) return; e.preventDefault(); t.split('').forEach((c,j)=>{ if(D[j]) D[j].value=c; }); (D[t.length]||D[N-1]).focus(); go(); }); });"
            "f.addEventListener('submit',e=>{ if(v().length!==N){ e.preventDefault(); document.getElementById('m').textContent='اكتب الأرقام كلها'; } else document.getElementById('k').value=v(); });"
            "if(!%s) D[0].focus();</script></body></html>") % (
            " err" if msg else "", action, n, where, "".join("<input inputmode=numeric autocomplete=one-time-code maxlength=1 aria-label='رقم %d'%s>" % (i + 1, " disabled" if locked else "") for i in range(n)),
            msg, " disabled" if locked else "", n, "true" if locked else "false")
# ── تشغيل Claude Code بالخلفية على مجلد (من المكتبة) ──
# 4.4.1: نلقى Claude حتى لو المكتبة اشتغلت بـ PATH ناقص (مع تشغيل ويندوز، أو من تطبيق Claude)، ونفهم ليش وقف ونقوله بكلام واضح.
_CL = {"t": 0, "v": None}
def claude_cfg_path(): return os.path.join(HOME_CFG, "claude.json")
def _win_path():
    if os.name != "nt": return ""
    try:
        import winreg; out = []
        for hk, sub in ((winreg.HKEY_CURRENT_USER, r"Environment"), (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment")):
            try:
                with winreg.OpenKey(hk, sub) as k: out.append(os.path.expandvars(winreg.QueryValueEx(k, "Path")[0]))
            except OSError: pass
        return os.pathsep.join(out)
    except Exception: return ""
def _cl_spots():
    h = os.path.expanduser("~")
    if os.name == "nt":
        A = os.environ.get("APPDATA") or J(h, "AppData", "Roaming"); L = os.environ.get("LOCALAPPDATA") or J(h, "AppData", "Local")
        s = [J(h, ".local", "bin", "claude.exe"), J(h, ".claude", "local", "claude.exe"), J(h, ".claude", "local", "claude.cmd"), J(A, "npm", "claude.cmd"),
             J(L, "Microsoft", "WinGet", "Links", "claude.exe"), J(h, "scoop", "shims", "claude.exe"), J(h, ".bun", "bin", "claude.exe"), J(L, "Volta", "bin", "claude.exe"), J(L, "pnpm", "claude.cmd")]
    else:
        s = [J(h, ".local", "bin", "claude"), J(h, ".claude", "local", "claude"), "/opt/homebrew/bin/claude", "/usr/local/bin/claude", J(h, ".npm-global", "bin", "claude"), J(h, ".bun", "bin", "claude"), J(h, ".volta", "bin", "claude")]
        s += sorted(glob.glob(J(h, ".nvm", "versions", "node", "*", "bin", "claude")))[-1:]
    return s
def _parent_exes(limit=10):
    """مسارات البرامج اللي شغّلتنا (أب ثم جدّ…). لو Claude Code هو اللي شغّل hs نلقاه هنا حتى لو مو بالـ PATH."""
    out = []
    try:
        if os.name == "nt":
            import ctypes, ctypes.wintypes as W
            class PE(ctypes.Structure):
                _fields_ = [("dwSize", W.DWORD), ("cntUsage", W.DWORD), ("th32ProcessID", W.DWORD), ("th32DefaultHeapID", ctypes.c_size_t), ("th32ModuleID", W.DWORD),
                            ("cntThreads", W.DWORD), ("th32ParentProcessID", W.DWORD), ("pcPriClassBase", ctypes.c_long), ("dwFlags", W.DWORD), ("szExeFile", ctypes.c_wchar * 260)]
            k = ctypes.windll.kernel32; k.CreateToolhelp32Snapshot.restype = ctypes.c_void_p; k.OpenProcess.restype = ctypes.c_void_p
            snap = k.CreateToolhelp32Snapshot(2, 0); par = {}; e = PE(); e.dwSize = ctypes.sizeof(PE)
            ok = k.Process32FirstW(ctypes.c_void_p(snap), ctypes.byref(e))
            while ok: par[e.th32ProcessID] = e.th32ParentProcessID; ok = k.Process32NextW(ctypes.c_void_p(snap), ctypes.byref(e))
            k.CloseHandle(ctypes.c_void_p(snap)); pid = os.getpid()
            for _ in range(limit):
                pid = par.get(pid)
                if not pid: break
                hp = k.OpenProcess(0x1000, False, pid)
                if not hp: continue
                buf = ctypes.create_unicode_buffer(1024); n = W.DWORD(1024)
                if k.QueryFullProcessImageNameW(ctypes.c_void_p(hp), 0, buf, ctypes.byref(n)): out.append(buf.value)
                k.CloseHandle(ctypes.c_void_p(hp))
        elif os.path.isdir("/proc"):
            pid = os.getppid()
            for _ in range(limit):
                if pid <= 1: break
                try: out.append(os.readlink("/proc/%d/exe" % pid)); pid = int(open("/proc/%d/stat" % pid).read().rsplit(")", 1)[1].split()[1])
                except Exception: break
        else:
            pid = os.getppid()
            for _ in range(limit):
                if pid <= 1: break
                r = subprocess.run(["ps", "-o", "ppid=,comm=", "-p", str(pid)], capture_output=True, text=True, timeout=3).stdout.strip().split(None, 1)
                if len(r) < 2: break
                out.append(r[1]); pid = int(r[0])
    except Exception: pass
    return out
def _is_claude_cli(p):
    try:
        if not p or not os.path.isfile(p): return False
        cmd = ["cmd", "/c", p, "--version"] if p.lower().endswith((".cmd", ".bat")) else [p, "--version"]
        kw = {"creationflags": 0x08000000} if os.name == "nt" else {}
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=15, stdin=subprocess.DEVNULL, **kw)
        return "claude code" in (r.stdout + r.stderr).lower()
    except Exception: return False
def claude_remember(p, how):
    try:
        old = rj(claude_cfg_path(), {}) or {}
        if old.get("path") != p: os.makedirs(HOME_CFG, exist_ok=True); wj(claude_cfg_path(), {"path": p, "how": how, "at": int(time.time())})
    except Exception: pass
def find_claude(fresh=False):
    """مسار Claude Code: PATH ← PATH الجديد من الريجستري ← آخر مسار نجح ← الأماكن المعروفة للتثبيت."""
    if os.environ.get("HS_NO_CLAUDE"): return None
    if not fresh and time.time() - _CL["t"] < 30: return _CL["v"]
    saved = (rj(claude_cfg_path(), {}) or {}).get("path"); how = "path"
    v = os.environ.get("HS_CLAUDE") if os.path.isfile(os.environ.get("HS_CLAUDE") or "") else None
    v = v or shutil.which("claude")
    if not v and os.name == "nt":
        wp = _win_path(); v = shutil.which("claude", path=wp) if wp else None; how = "registry"
    if not v and saved and os.path.isfile(saved): v = saved; how = "saved"
    if not v: v = next((p for p in _cl_spots() if os.path.isfile(p)), None); how = "known"
    if v and v != saved: claude_remember(v, how)
    _CL.update(t=time.time(), v=v); return v
def claude_learn():
    """يشتغل وقت ما Claude Code نفسه يشغّل hs (مثل hs sync من بداية الجلسة): يحفظ مكانه للمكتبة."""
    if os.environ.get("HS_NO_CLAUDE"): return None
    v = shutil.which("claude"); saved = (rj(claude_cfg_path(), {}) or {}).get("path")
    if not v:
        for p in _parent_exes():
            b = os.path.basename(p).lower()
            if b in ("claude", "claude.exe") and (p == saved or _is_claude_cli(p)): v = p; break
    if v: claude_remember(v, "session"); _CL.update(t=0)
    return v
def have_claude(): return bool(find_claude())
AR_RESET = {"am": "ص", "pm": "م"}
def claude_why(txt, rc=None):
    """يقرأ آخر كلام Claude ويقول ليش وقف بكلام واضح."""
    t = re.sub(r"\x1b\[[0-9;]*[A-Za-z]", "", str(txt or "")); low = t.lower()
    if re.search(r"hit your (session |usage |weekly |daily )?limit|usage limit|limit reached|out of (extra )?usage|5-hour limit|rate.?limit", low):
        m = re.search(r"resets?\s+(?:at\s+)?([0-9]{1,2}(?::[0-9]{2})?\s*(am|pm)?)", t, re.I); r = ""
        if m: r = re.sub(r"\s*(am|pm)", lambda x: AR_RESET[x.group(1).lower()], m.group(1), flags=re.I)
        return {"why": "limit", "reset": r, "msg": "خلص حد استخدامك في Claude" + (" ويرجع الساعة %s" % r if r else " لين يتجدد") + "."}
    if re.search(r"not logged in|please (run )?/?login|invalid api key|authentication|unauthori[sz]ed|oauth token|401", low):
        return {"why": "login", "msg": "Claude Code مو مسجّل دخول. افتح Claude Code مرة واكتب /login ثم أعد."}
    if re.search(r"credit balance|billing|payment required", low): return {"why": "credit", "msg": "حسابك في Claude يبي اشتراك أو رصيد."}
    if re.search(r"overloaded|529|internal server error|\b500\b|api error", low): return {"why": "busy", "msg": "خوادم Claude مزحومة الحين. أعد بعد دقايق."}
    if re.search(r"enotfound|econnrefused|econnreset|getaddrinfo|network|timed? ?out|offline|socket hang up", low): return {"why": "net", "msg": "Claude ما قدر يتصل بالنت. تأكد من النت وأعد."}
    last = next((x.strip() for x in reversed(t.strip().splitlines()) if x.strip()), "")
    return {"why": "other", "msg": "Claude وقف" + (" (رمز %s)" % rc if rc not in (None, 0) else "") + (": " + last[:160] if last else ".")}
def claude_spawn(work, task, label="طلب", on_done=None, on_fail=None):
    exe = find_claude()
    task = task.replace("<engine>", find_engine(None) or "engine") + '\n\n(سياق: `hs` = `"%s" "%s"` · السكل: %s)' % (PY, os.path.abspath(__file__), HERE)
    if not exe: return False, "ما لقيت Claude Code على الجهاز. افتح Claude Code مرة وحدة (عشان أعرف مكانه) أو قل له: " + task[:200]
    cmd = [exe, "-p", task, "--permission-mode", "acceptEdits", "--add-dir", HERE, "--allowedTools", "Bash", "Read", "Edit", "Write", "Glob", "Grep"]
    if exe.lower().endswith((".cmd", ".bat")): cmd = ["cmd", "/c"] + cmd
    lg = J(work, "claude.log")
    try: off = os.path.getsize(lg)
    except OSError: off = 0
    kw = {"cwd": work, "stdin": subprocess.DEVNULL, "stdout": open(lg, "ab"), "stderr": subprocess.STDOUT}
    if os.name == "nt": kw["creationflags"] = 0x08000000
    try: pr = subprocess.Popen(cmd, **kw); cid = cmd_log_add(work, label, task, None); t0 = time.time()
    except Exception as e: return False, str(e)[:200]
    def wait():
        rc = pr.wait()
        try:
            with open(lg, "rb") as f: f.seek(off); out = f.read().decode("utf-8", "replace")
        except Exception: out = ""
        bad = rc != 0 or (time.time() - t0 < 180 and len(out) < 3000 and claude_why(out)["why"] in ("limit", "login", "credit"))
        if bad:
            w = claude_why(out, rc); cmd_log_set(cid, status="err", result=w["msg"], why=w["why"])
            try: say(work, w["msg"], "err")
            except Exception: pass
            try: job_set(work, claudeErr=w["msg"], why=w["why"], ranking=False)
            except Exception: pass
            if on_fail:
                try: on_fail(w)
                except Exception as e: print("بعد ما وقف Claude:", e, file=sys.stderr)
        else:
            cmd_log_set(cid, status="done")
            try: job_set(work, claudeErr=None, why=None, ranking=False)
            except Exception: pass
            if on_done:
                try: on_done()
                except Exception: pass
    threading.Thread(target=wait, daemon=True).start(); return True, ""
def cmd_claude(args):
    """hs claude            وين Claude Code؟
hs claude set <مسار>   حدد مكانه بنفسك
hs claude test         يجرّب يرد بكلمة (يتأكد من الدخول والحد)"""
    sub = args[0] if args else "where"
    if sub == "set":
        p = os.path.abspath(args[1]) if len(args) > 1 else sys.exit(cmd_claude.__doc__)
        if not _is_claude_cli(p): sys.exit("هذا مو Claude Code: " + p)
        claude_remember(p, "manual"); print("تمام، المكتبة بتستخدم:", p); return
    v = claude_learn() or find_claude(True)
    if not v: sys.exit("ما لقيت Claude Code. ثبّته من claude.com/claude-code أو حدد مكانه: hs claude set <المسار>")
    print("Claude Code:", v, "·", (rj(claude_cfg_path(), {}) or {}).get("how", ""))
    if sub == "test":
        cmd = (["cmd", "/c"] if v.lower().endswith((".cmd", ".bat")) else []) + [v, "-p", "Reply with the single word: ok"]
        kw = {"creationflags": 0x08000000} if os.name == "nt" else {}
        try: r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120, stdin=subprocess.DEVNULL, **kw)
        except subprocess.TimeoutExpired: sys.exit("Claude ما رد خلال دقيقتين.")
        out = (r.stdout or "") + (r.stderr or "")
        if r.returncode == 0 and "ok" in out.lower() and claude_why(out)["why"] == "other": print("شغّال ويرد.")
        else: sys.exit(claude_why(out, r.returncode)["msg"])

# ══════════ 4.5: ثمان ميزات. كلها تشتغل على جهازك بدون Claude، وأي شي يحتاج Claude زر اختياري ينبّهك إنه يستهلك ══════════
def token_ask(): return hub_cfg().get("tokenAsk", True) is not False
CTA_W = set("تابع تابعني تابعونا تابعوني اشترك اشتركوا احفظ احفظه احفظوه شارك شاركه شاركوه رابط الرابط البايو علق علّق علقوا كومنت follow subscribe save share link comment bio".split())
WEAK_END = set("و ف بس لكن يعني اللي عشان علشان and but so because the a to of".split())
CONJ_REST = set("من إذا اذا راح هذا هذي هذه انا أنا انت أنت بعدين بعدها كمان لو إن ان أن ما لا كل تبي يعني اللي هو هي هم في على عشان لما حتى".split())
def _conj(w):
    """هل أول حرف واو/فاء عطف؟ «ومن» «وتشوف» «والله» لا، «وقت» لا."""
    if len(w) < 3 or w[0] not in "وف" or w in ("والله", "وش", "وين"): return False
    r = w[1:]
    return r in CONJ_REST or r.startswith("ال") or (len(r) >= 4 and r[0] in "تينأا")
def _weak0(w): return w in WEAK_START or _conj(w)
def _unconj(t):
    """يشيل واو العطف من أول كلمة: «وراح يوصلك» ← «راح يوصلك»."""
    w = t.split()
    if w and _conj(w[0]): w[0] = w[0][1:]
    return " ".join(w)
def hook_score(text):
    """كم الجملة تشد (0 إلى 3) وليش."""
    tk = _tok(text); low = " " + " ".join(tk) + " "; why = []; h = 0.0
    if re.search(r"[?؟]", text) or (tk and tk[0] in ("ليش", "ليه", "كيف", "شلون", "وش", "ايش", "إيش", "هل", "why", "how", "what")): h += 1; why.append("سؤال")
    hw = sum(1 for w in tk if w in HOOK_W or _bare(w) in HOOK_W) + sum(1 for p in HOOK_P if p in low)
    if hw: h += min(2, hw) * 0.7; why.append("كلمة تشد")
    if re.search(r"\d|مليون|ألف|الف|million|thousand|percent|٪|%", text): h += 0.6; why.append("رقم")
    if tk and _weak0(tk[0]): h -= 0.6; why.append("بداية ضعيفة")
    return max(0.0, min(3.0, h)), why
def _sentences(cards, gap=0.5, maxw=22):
    """يجمع جمل الكابشن القصيرة لجمل كاملة حسب الوقفات."""
    out = []; cur = None
    for i, c in enumerate(cards):
        if not c.get("w"): continue
        tx = " ".join(w["t"] for w in c["w"])
        if cur and c["w"][0]["s"] - cur["e"] <= gap and len(cur["text"].split()) + len(c["w"]) <= maxw: cur["text"] += " " + tx; cur["e"] = c["w"][-1]["e"]; cur["cards"].append(i)
        else:
            cur = {"s": c["w"][0]["s"], "e": c["w"][-1]["e"], "text": tx, "cards": [i]}; out.append(cur)
    return out

# ── (4) أحسن إعادة: لو قلت الجملة كذا مرة نخلي الأوضح ──
def takes(work):
    caps = rj(J(work, "caps.json"), {"cards": []}) or {"cards": []}; cards = caps.get("cards") or []
    if len(cards) < 2: return []
    probs = []
    for s in (rj(J(work, "a.json"), {}) or {}).get("segments") or []:
        for w in s.get("words") or []:
            if w.get("probability") is not None: probs.append((float(w["start"]), float(w["probability"])))
    probs.sort(); fl = set(_norm(x) for x in FILLERS)
    N = [[_norm(w["t"]) for w in c["w"]] for c in cards]
    par = list(range(len(cards)))
    def root(x):
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    for i in range(len(cards)):
        for j in range(i + 1, min(i + 5, len(cards))):
            a, b = N[i], N[j]
            if not a or not b: continue
            r = _sim(a, b); k = min(len(a), len(b))
            pre = k >= 3 and a[:k] == b[:k] and k >= 0.6 * min(len(a), len(b))   # بدأ الجملة وقطعها ثم أعادها
            if r >= 0.6 or pre: par[root(j)] = root(i)
    G = {}
    for i in range(len(cards)): G.setdefault(root(i), []).append(i)
    out = []
    for g in G.values():
        if len(g) < 2: continue
        g.sort(); mx = max(len(N[i]) for i in g); q = {}; why = {}
        for i in g:
            ws = cards[i]["w"]; n = len(ws); pauses = sum(1 for a, b in zip(ws, ws[1:]) if b["s"] - a["e"] > 0.45); fil = sum(1 for w in ws if _norm(w["t"]) in fl)
            pr = [p for t, p in probs if ws[0]["s"] - 0.3 <= t <= ws[-1]["e"] + 0.3]   # تقريبي: وقت التفريغ قبل القص
            pv = sum(pr) / len(pr) if pr else 0.8
            sc = 45 * n / mx + 25 * pv - 9 * pauses - 6 * fil + (6 if i == g[-1] else 0)
            q[i] = round(sc, 1); why[i] = [x for x, ok in (("الأكمل", n == mx), ("بدون وقفات", pauses == 0), ("بدون حشو", fil == 0), ("آخر محاولة", i == g[-1])) if ok]
        keep = max(g, key=lambda i: q[i])
        out.append({"cards": g, "keep": keep, "q": q, "why": why[keep]})
    return out

# ── (1) فحص الاحتفاظ قبل النشر (تقدير من المقطع نفسه، مو أرقام مشاهدين حقيقية) ──
def retention(work):
    caps = rj(J(work, "caps.json"), {"cards": [], "total": 0}) or {}; cards = [c for c in caps.get("cards") or [] if c.get("w")]; total = float(caps.get("total") or 0)
    if not cards or total < 3: return {"ok": False, "msg": "المقطع ما تجهّز للحين"}
    ck = check(work); hs = hs_of(load_studio(work)); n = max(1, int(total + 0.999))
    W = [w for c in cards for w in c["w"]]; speak = [0.0] * n; wc = [0] * n; fil = [0] * n; fl = set(_norm(x) for x in FILLERS)
    for w in W:
        a, b = float(w["s"]), float(w["e"]); i = int(a)
        if i < n: wc[i] += 1
        if _norm(w["t"]) in fl and i < n: fil[i] += 1
        while i < n and i < b:
            speak[i] += max(0.0, min(b, i + 1) - max(a, i)); i += 1
    silent = [1.0 if speak[i] < 0.25 else (0.5 if speak[i] < 0.5 else 0.0) for i in range(n)]
    med = sorted(x for x in wc if x)[len([x for x in wc if x]) // 2] if any(wc) else 2
    slow = []
    for i in range(n):
        lo, hi = max(0, i - 2), min(n, i + 2); r = sum(wc[lo:hi]) / max(1, hi - lo)
        slow.append(1.0 if r < max(1.1, med * 0.55) and speak[i] > 0.3 else 0.0)
    static = [0.0] * n; gap = ck.get("gap", 2.5)
    for g in ck.get("gaps") or []:
        for i in range(int(g["s"]), min(n, int(g["e"]) + 1)):
            k = (i - g["s"]) / max(0.5, gap)
            if k > 0.6: static[i] = max(static[i], min(1.0, (k - 0.6) / 1.2))
    rep = [0.0] * n; tk = takes(work)
    for gr in tk:
        for ci in gr["cards"]:
            if ci == gr["keep"]: continue
            c = caps["cards"][ci]
            for i in range(int(c["w"][0]["s"]), min(n, int(c["w"][-1]["e"]) + 1)): rep[i] = 1.0
    risk = [min(1.0, 0.45 * silent[i] + 0.35 * static[i] + 0.3 * slow[i] + 0.55 * rep[i] + 0.15 * min(1, fil[i])) for i in range(n)]
    # الأبعاد
    S = _sentences(cards); first = S[0]["text"] if S else ""; h0, hwhy = hook_score(first); op = ck.get("open") or {}; miss = op.get("miss") or []
    fw = float(cards[0]["w"][0]["s"])
    hook = 100 - (25 if fw > 0.7 else 0) - 15 * len([m for m in miss if m != "voice"]) - (30 if h0 < 0.5 else 12 if h0 < 1.2 else 0)
    if (hs.get("hooks") or {}).get("on") and (hs.get("hooks") or {}).get("items"): hook += 10
    pace = 100 - 140 * sum(silent) / n - 70 * sum(slow) / n
    visual = 100 - 150 * sum(1 for x in static if x > 0.3) / n
    fpm = len(ck.get("fillers") or []) / max(0.25, total / 60)
    clarity = 100 - 7 * fpm - 12 * sum(len(g["cards"]) - 1 for g in tk) - 4 * len(ck.get("longCaps") or [])
    lastS = S[-1] if S else {"text": "", "e": total}; ltk = _tok(lastS["text"]); tail = total - float(cards[-1]["w"][-1]["e"])
    cta = any(w in CTA_W or _bare(w) in CTA_W for s in S[-2:] for w in _tok(s["text"]))
    payoff = 100 - (30 if ltk and ltk[-1] in WEAK_END else 0) - (25 if tail > 1.4 else 0) - (0 if cta else 15)
    plats = hs.get("platforms") or []; ln = len_check(total, plats)
    length = 100 - (40 if any(x["k"] == "over" for x in ln) else 20 if ln else 0) - (0 if plats or 12 <= total <= 75 else 20)
    dims = {k: int(max(0, min(100, v))) for k, v in (("hook", hook), ("pace", pace), ("visual", visual), ("clarity", clarity), ("payoff", payoff), ("length", length))}
    score = int(round(dims["hook"] * 0.3 + dims["pace"] * 0.2 + dims["visual"] * 0.2 + dims["clarity"] * 0.15 + dims["payoff"] * 0.1 + dims["length"] * 0.05))
    # منحنى تقديري: كم يكمل من المشاهدين لكل ثانية
    ret = 100.0; curve = []; drop3 = max(8.0, 34 - dims["hook"] * 0.22)
    for i in range(n):
        if i < 3: ret -= drop3 / 3
        ret *= 1 - (0.004 + 0.028 * risk[i]); curve.append(round(max(0.0, ret), 1))
    zones = []; i = 0
    while i < n:
        lv = 2 if risk[i] >= 0.55 else 1 if risk[i] >= 0.3 else 0
        if not lv: i += 1; continue
        j = i
        while j + 1 < n and (2 if risk[j + 1] >= 0.55 else 1 if risk[j + 1] >= 0.3 else 0) == lv: j += 1
        zones.append({"s": i, "e": min(total, j + 1), "lvl": "red" if lv == 2 else "yellow"}); i = j + 1
    # التصليحات مرتّبة بالأهم
    fixes = []
    if dims["hook"] < 75:
        S2 = [x for x in _sentences(cards, 0.45, 12) if 4 <= len(x["text"].split()) <= 12 and _tok(x["text"])[:1] and not _weak0(_tok(x["text"])[0])]
        best = max(S2, key=lambda s: hook_score(s["text"])[0]) if S2 else None
        if best and hook_score(best["text"])[0] >= 0.7 and hook_score(best["text"])[0] > h0 + 0.4:
            fixes.append({"k": "hook", "t": 0, "imp": 3, "fix": "hook", "arg": best["text"][:70], "msg": "أول 3 ثواني ما تشد كفاية. أقوى جملة عندك: «%s». حطها عنوان فوق أول المقطع." % best["text"][:60]})
        else: fixes.append({"k": "hook", "t": 0, "imp": 3, "fix": "claude", "msg": "أول 3 ثواني ما تشد كفاية (" + ("، ".join(hwhy) or "ما فيها سؤال أو رقم أو كلمة تشد") + ")."})
    if fw > 0.7: fixes.append({"k": "start", "t": 0, "imp": 3, "fix": "cut", "arg": [[0, round(fw - 0.12, 2)]], "msg": "أول كلمة تبدأ بعد %.1f ث. الناس تسحب قبلها." % fw})
    pauses = []
    for z in zones:
        for a, b in zip(W, W[1:]):
            if z["s"] <= a["e"] < z["e"] and b["s"] - a["e"] > 0.45: pauses.append([round(a["e"] + 0.12, 2), round(b["s"] - 0.08, 2)])
    pauses = [p for p in pauses if p[1] - p[0] > 0.2]
    if pauses: fixes.append({"k": "pace", "t": pauses[0][0], "imp": 2, "fix": "cut", "arg": pauses, "msg": "فيه %d وقفة بين الكلام بالمناطق الحمراء (%.1f ث كلها). أشيلها وأخلي الكلام متصل." % (len(pauses), sum(b - a for a, b in pauses))})
    for g in (ck.get("gaps") or [])[:6]:
        if g["d"] >= gap + 0.8: fixes.append({"k": "visual", "t": g["s"], "imp": 2, "fix": "zoom", "arg": [round(g["s"] + gap * 0.6, 2), round(min(g["e"], g["s"] + gap * 0.6 + 2.6), 2)], "msg": "%.1f ث بدون أي تغيير بالصورة من %s. أحط زوم بطيء يحركها." % (g["d"], tfmt(g["s"]))})
    if tk: fixes.append({"k": "takes", "t": caps["cards"][tk[0]["cards"][0]]["s"], "imp": 2, "fix": "takes", "msg": "قلت %d جملة أكثر من مرة. خليت لك الأحسن بكل وحدة تحت «الإعادات»." % len(tk)})
    if fpm > 3: fixes.append({"k": "clarity", "t": 0, "imp": 1, "fix": "fillers", "msg": "%d كلمة حشو بالدقيقة. شيلها من «كلمات الحشو»." % round(fpm)})
    if tail > 1.4: fixes.append({"k": "payoff", "t": round(total - tail, 2), "imp": 2, "fix": "cut", "arg": [[round(total - tail + 0.35, 2), round(total, 2)]], "msg": "بعد آخر كلمة %.1f ث فاضية. الناس تطلع قبل النهاية ويحسب عليك." % tail})
    if not cta: fixes.append({"k": "payoff", "t": round(lastS["s"], 2), "imp": 1, "fix": "claude", "msg": "النهاية ما تطلب شي (تابع، احفظ، علّق). جملة وحدة ترفع التفاعل."})
    for x in ln: fixes.append({"k": "length", "t": 0, "imp": 2 if x["k"] == "over" else 1, "fix": None, "msg": ("أطول من حد %s (%d ث)." % (x["p"], x["max"])) if x["k"] == "over" else ("الأنسب لـ%s بين %d و%d ث، ومقطعك %d ث." % (x["p"], x["lo"], x["hi"], round(total)))})
    fixes.sort(key=lambda f: -f["imp"])
    return {"ok": True, "score": score, "dims": dims, "curve": curve, "zones": zones, "fixes": fixes, "end": curve[-1] if curve else 0, "total": total, "takes": tk}

# ── (2) يتعلّم من أرقامك: أداء كل مقطع (تدخله بيدك أو تستورده CSV) ──
PERF_COLS = {"views": ("views", "plays", "video views", "total views", "view count", "المشاهدات", "مشاهدات", "عدد المشاهدات", "reach"),
             "likes": ("likes", "like count", "الإعجابات", "اعجابات", "إعجابات", "reactions"), "comments": ("comments", "التعليقات", "تعليقات"),
             "shares": ("shares", "المشاركات", "مشاركات", "reposts"), "saves": ("saves", "saved", "bookmarks", "favorites", "المحفوظات", "حفظ"),
             "watch": ("average watch time", "avg. watch time", "avg watch time", "average view duration", "متوسط وقت المشاهدة", "متوسط المشاهدة"),
             "ret": ("watched full video", "completion rate", "retention", "average percentage viewed", "نسبة المشاهدة الكاملة", "نسبة الاحتفاظ"),
             "date": ("date", "post time", "posted", "published", "publish time", "created", "time", "التاريخ", "تاريخ النشر"),
             "title": ("title", "caption", "description", "text", "video title", "content", "النص", "الوصف", "العنوان"), "url": ("link", "url", "permalink", "الرابط")}
def perf_conn():
    c, _ = db_conn()
    c.execute("CREATE TABLE IF NOT EXISTS perf (item TEXT, plat TEXT, views INTEGER, likes INTEGER, comments INTEGER, shares INTEGER, saves INTEGER, watch REAL, ret REAL, posted TEXT, url TEXT, src TEXT, at REAL, PRIMARY KEY (item, plat))")
    return c
def _num(v):
    s = str(v or "").strip().replace(",", "").replace("٬", "").replace(" ", "")
    s = s.translate(str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")); m = re.match(r"^([\d.]+)\s*([kKmMبألف]*)", s)
    if not m: return None
    try: x = float(m.group(1))
    except ValueError: return None
    u = m.group(2).lower()
    return x * (1e3 if u in ("k", "ألف", "الف") else 1e6 if u == "m" else 1)
def _secs(v):
    s = str(v or "").strip()
    if re.match(r"^\d+:\d+(:\d+)?$", s):
        p = [float(x) for x in s.split(":")]; return p[0] * 60 + p[1] if len(p) == 2 else p[0] * 3600 + p[1] * 60 + p[2]
    return _num(s.rstrip("sث "))
def perf_set(item, plat="all", **v):
    c = perf_conn()
    try:
        old = c.execute("SELECT views, likes, comments, shares, saves, watch, ret, posted, url FROM perf WHERE item=? AND plat=?", (item, plat)).fetchone()
        keys = ("views", "likes", "comments", "shares", "saves", "watch", "ret", "posted", "url"); row = dict(zip(keys, old or [None] * 9))
        for k in keys:
            if v.get(k) not in (None, ""): row[k] = v[k] if k in ("posted", "url") else (_secs(v[k]) if k == "watch" else _num(v[k]))
        with _DBL:
            c.execute("INSERT OR REPLACE INTO perf VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (item, plat, *(row[k] for k in keys[:7]), row["posted"], row["url"], v.get("src") or "manual", time.time())); c.commit()
    finally: c.close()
    try: learn_prefs()
    except Exception: pass
def perf_get(item):
    c = perf_conn()
    try: return [dict(zip(("plat", "views", "likes", "comments", "shares", "saves", "watch", "ret", "posted", "url"), r)) for r in c.execute("SELECT plat, views, likes, comments, shares, saves, watch, ret, posted, url FROM perf WHERE item=?", (item,)).fetchall()]
    finally: c.close()
def perf_all():
    c = perf_conn()
    try:
        R = {}
        for item, views, likes, sh, sv, ret in c.execute("SELECT item, views, likes, shares, saves, ret FROM perf").fetchall():
            x = R.setdefault(item, {"views": 0, "likes": 0, "shares": 0, "saves": 0, "ret": None})
            x["views"] += views or 0; x["likes"] += likes or 0; x["shares"] += sh or 0; x["saves"] += sv or 0
            if ret is not None: x["ret"] = ret
        items = {r[0]: {"work": r[1], "title": r[2], "dur": r[3]} for r in c.execute("SELECT id, work, title, dur FROM items").fetchall()}
        return {k: {**v, **items.get(k, {})} for k, v in R.items() if k in items}
    finally: c.close()
def perf_import(text, plat="", name=""):
    """يستورد CSV من تيك توك أو انستقرام أو Metricool ويربط كل صف بمقطعه (بالنص والتاريخ)."""
    import csv, io
    rows = list(csv.reader(io.StringIO(text.lstrip("﻿"))))
    if len(rows) < 2: return {"ok": False, "msg": "الملف فاضي أو مو CSV"}
    hi = next((i for i, r in enumerate(rows[:6]) if sum(1 for x in r if x.strip()) >= 2), 0); head = [h.strip().lower() for h in rows[hi]]
    col = {}
    for k, names in PERF_COLS.items():
        for i, h in enumerate(head):
            if any(h == n or (len(n) > 4 and n in h) for n in names) and i not in col.values(): col[k] = i; break
    if "views" not in col: return {"ok": False, "msg": "ما لقيت عمود المشاهدات بالملف (views / plays / المشاهدات)"}
    pl = plat or ("tiktok" if "tiktok" in name.lower() else "instagram" if re.search(r"insta|reel", name, re.I) else "youtube" if "youtube" in name.lower() else "all")
    db_sync(hub_cfg().get("root"))
    c, _ = db_conn()
    try: items = c.execute("SELECT id, work, title, made FROM items WHERE kind='proj'").fetchall()
    finally: c.close()
    docs = {}
    for iid, w, title, made in items:
        tx = " ".join(x for x in (title, open(J(w, "post.txt"), encoding="utf-8", errors="replace").read()[:600] if os.path.exists(J(w, "post.txt")) else "",
                                  " ".join(card_key(cc) for cc in ((rj(J(w, "caps.json"), {}) or {}).get("cards") or [])[:4])) if x)
        docs[iid] = (set(t for t in _tok(norm_txt(tx)) if len(t) > 2 and t not in STOP_W), made or 0)
    ok, miss = 0, []
    for r in rows[hi + 1:]:
        if not any(x.strip() for x in r): continue
        g = lambda k: r[col[k]] if k in col and col[k] < len(r) else ""
        cap = g("title"); toks = set(t for t in _tok(norm_txt(cap)) if len(t) > 2 and t not in STOP_W); best = None
        for iid, (dt, made) in docs.items():
            if not toks or not dt: continue
            s = len(toks & dt) / max(3, min(len(toks), len(dt)))
            if not best or s > best[0]: best = (s, iid)
        row = {k: g(k) for k in ("views", "likes", "comments", "shares", "saves", "watch", "ret", "url")}; row["posted"] = g("date")
        if best and best[0] >= 0.3: perf_set(best[1], pl, src="csv", **row); ok += 1
        else: miss.append({"title": cap[:120], "views": _num(row["views"]), "row": row})
    return {"ok": True, "matched": ok, "unmatched": miss[:60], "plat": pl}
def item_feats(work):
    caps = rj(J(work, "caps.json"), {}) or {}; cards = [c for c in caps.get("cards") or [] if c.get("w")]; hs = hs_of(load_studio(work)); total = float(caps.get("total") or 0)
    S = _sentences(cards); first = S[0]["text"] if S else ""; h, why = hook_score(first)
    nw = sum(len(c["w"]) for c in cards)
    return {"dur": total, "q": "سؤال" in why, "num": "رقم" in why, "hookw": "كلمة تشد" in why, "rate": nw / max(1, total), "start": float(cards[0]["w"][0]["s"]) if cards else 0,
            "layers": len([L for L in hs.get("layers") or [] if not L.get("off")]) / max(0.25, total / 60), "hookOn": bool((hs.get("hooks") or {}).get("on")), "style": (hs.get("cap") or {}).get("preset") or (hs.get("cap") or {}).get("style") or ""}
def insights():
    P = perf_all(); rows = []
    for iid, p in P.items():
        if not p.get("views") or not p.get("work") or not os.path.isdir(p["work"]): continue
        try: rows.append((p["views"], item_feats(p["work"]), p))
        except Exception: pass
    out = {"n": len(rows), "tips": [], "top": [], "need": max(0, 5 - len(rows))}
    if not rows: return out
    rows.sort(key=lambda r: -r[0]); out["top"] = [{"title": r[2].get("title"), "views": r[0], "work": r[2]["work"]} for r in rows[:5]]
    if len(rows) < 5: return out
    med = lambda L: sorted(L)[len(L) // 2] if L else 0
    def cmp(name, yes, no_msg=None):
        a = [v for v, f, _ in rows if yes(f)]; b = [v for v, f, _ in rows if not yes(f)]
        if len(a) >= 2 and len(b) >= 2 and med(b):
            r = med(a) / med(b)
            if r >= 1.4: out["tips"].append({"k": name, "r": round(r, 1), "up": True, "msg": TIPS_AR[name][0] % r})
            elif r <= 0.7 and med(a): out["tips"].append({"k": name, "r": round(1 / r, 1), "up": False, "msg": TIPS_AR[name][1] % (1 / r)})
    cmp("q", lambda f: f["q"]); cmp("num", lambda f: f["num"]); cmp("hookw", lambda f: f["hookw"]); cmp("hookOn", lambda f: f["hookOn"])
    cmp("fast", lambda f: f["rate"] >= med([x["rate"] for _, x, _ in rows])); cmp("busy", lambda f: f["layers"] >= med([x["layers"] for _, x, _ in rows]))
    cmp("early", lambda f: f["start"] <= 0.4)
    B = ((0, 20), (20, 35), (35, 60), (60, 999)); bm = []
    for lo, hi in B:
        vs = [v for v, f, _ in rows if lo <= f["dur"] < hi]
        if len(vs) >= 2: bm.append((med(vs), lo, hi, len(vs)))
    if len(bm) >= 2:
        bm.sort(reverse=True); allm = med([v for v, _, _ in rows])
        if allm and bm[0][0] / allm >= 1.25: out["tips"].append({"k": "len", "r": round(bm[0][0] / allm, 1), "lo": bm[0][1], "hi": min(bm[0][2], 120), "msg": "مقاطعك بين %d و%d ثانية تجيب %.1f ضعف متوسطك." % (bm[0][1], min(bm[0][2], 120), bm[0][0] / allm)})
    out["tips"].sort(key=lambda x: -x["r"]); return out
TIPS_AR = {"q": ("المقاطع اللي تبدأ بسؤال تجيب %.1f ضعف غيرها. ابدأ بسؤال.", "البداية بسؤال تجيب أقل بـ %.1f مرة عند جمهورك."),
           "num": ("لما تذكر رقم بأول جملة تجيب %.1f ضعف.", "الأرقام بأول جملة ما تنفع جمهورك (أقل %.1f مرة)."),
           "hookw": ("الكلمات اللي تشد بالبداية (سر، غلط، أكبر…) ترفع مشاهداتك %.1f ضعف.", "الكلمات القوية بالبداية ما فرقت معك (أقل %.1f مرة)."),
           "hookOn": ("العنوان فوق أول المقطع يجيب %.1f ضعف. خله دايم.", "العنوان فوق أول المقطع ما يفرق (أقل %.1f مرة)."),
           "fast": ("كلامك السريع يجيب %.1f ضعف الهادي.", "مقاطعك الهادية تجيب %.1f ضعف السريعة."),
           "busy": ("المقاطع اللي فيها عناصر وحركة أكثر تجيب %.1f ضعف.", "المقاطع البسيطة تجيب عندك %.1f ضعف المليانة."),
           "early": ("لما تبدأ الكلام من أول لحظة تجيب %.1f ضعف.", "البداية الهادية ما ضرتك (أعلى %.1f مرة).")}
def learned():
    return rj(os.path.join(HOME_CFG, "learned.json"), {}) or {}
def learn_prefs():
    I = insights(); L = {"n": I["n"], "at": int(time.time())}
    for tp in I["tips"]:
        if tp["k"] == "len": L["len"] = [tp["lo"], tp["hi"]]
        elif tp["k"] in ("q", "num", "hookw"): L[tp["k"]] = round(min(1.2, 0.35 * (tp["r"] - 1)), 2) if tp.get("up") else -round(min(0.8, 0.25 * (tp["r"] - 1)), 2)
    os.makedirs(HOME_CFG, exist_ok=True); wj(os.path.join(HOME_CFG, "learned.json"), L); return L

# ── (6) مصنع الليل: مجلد ترمي فيه مقاطعك وتتجهّز لحالها ──
VID_EXTS = (".mp4", ".mov", ".m4v", ".mkv", ".webm", ".avi", ".3gp")
FAC = {"sizes": {}, "doing": None, "done": 0, "batch": 0, "last": None, "err": None}
def scripts_path(): return os.path.join(HOME_CFG, "scripts.json")
def factory_cfg():
    f = hub_cfg().get("factory") or {}; root = FAC.get("root") or hub_cfg().get("root") or os.path.join(os.path.expanduser("~"), "Documents", "hojas-studio-projects")
    return {"on": bool(f.get("on")), "dir": f.get("dir") or os.path.join(root, "_inbox"), "mode": f.get("mode") if f.get("mode") in ("manual", "auto") else "manual", "night": bool(f.get("night")), "root": root}
def factory_state():
    c = factory_cfg(); q = []
    if os.path.isdir(c["dir"]): q = sorted(f for f in os.listdir(c["dir"]) if f.lower().endswith(VID_EXTS))
    return {**c, "queue": len(q), "files": q[:20], "doing": FAC["doing"], "done": FAC["done"], "last": FAC["last"], "err": FAC["err"], "now": factory_window(c)}
def factory_window(c=None):
    c = c or factory_cfg(); h = time.localtime().tm_hour
    return FAC.get("force") or (not c["night"]) or h < 7
def factory_tick():
    c = factory_cfg()
    if not (c["on"] or FAC.get("force")) or FAC["doing"] or not factory_window(c): return
    os.makedirs(c["dir"], exist_ok=True)
    for f in sorted(os.listdir(c["dir"])):
        p = os.path.join(c["dir"], f)
        if not f.lower().endswith(VID_EXTS) or not os.path.isfile(p): continue
        sz = os.path.getsize(p)
        if FAC["sizes"].get(p) != sz or time.time() - os.path.getmtime(p) < 20: FAC["sizes"][p] = sz; continue   # لسه ينسخ
        FAC["sizes"].pop(p, None); base = re.sub(r"[^\w\-]+", "-", os.path.splitext(f)[0]).strip("-")[:40] or time.strftime("clip-%m%d-%H%M")
        d = os.path.join(c["root"], base); k = 1
        while os.path.exists(d): d = os.path.join(c["root"], "%s-%d" % (base, k)); k += 1
        os.makedirs(d); dst = os.path.join(d, "upload" + os.path.splitext(f)[1].lower())
        try: shutil.move(p, dst)
        except Exception as e: FAC["err"] = str(e)[:200]; continue
        FAC["doing"] = os.path.basename(d); FAC["batch"] += 1
        def go(d=d, dst=dst, mode=c["mode"]):
            try: job_run(d, dst, mode, "me", 5, None, "", None); FAC["done"] += 1; FAC["last"] = os.path.basename(d); FAC["err"] = None
            except Exception as e: FAC["err"] = "%s: %s" % (os.path.basename(d), str(e)[:200])
            finally:
                FAC["doing"] = None
                left = [x for x in os.listdir(c["dir"]) if x.lower().endswith(VID_EXTS)] if os.path.isdir(c["dir"]) else []
                if not left: FAC["force"] = False
                if not left and FAC["batch"]:
                    n = FAC["batch"]; FAC["batch"] = 0
                    try: notify_send("جهّزت %d مقطع من مجلد الوارد، وهي بالمكتبة تنتظرك." % n, title="مصنع الليل")
                    except Exception: pass
        threading.Thread(target=go, daemon=True).start(); return

# ── (7) 3 أغلفة: لقطات وجهك فيها واضح ومعبّر ──
def covers(work, k=3):
    vf = J(work, "vfr"); fr = sorted(f for f in os.listdir(vf) if f.endswith(".jpg")) if os.path.isdir(vf) else []
    if not fr: return {"ok": False, "msg": "المقطع ما تجهّز"}
    n = len(fr); total = n / 30.0; face = rj(J(work, "face.json"), {}) or {}; pts = face.get("pts") or []
    au = J(work, ".hs", "au8.wav")
    if not os.path.exists(au) or os.path.getmtime(au) < os.path.getmtime(J(work, "cutz.mp4")):
        os.makedirs(J(work, ".hs"), exist_ok=True); subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", J(work, "cutz.mp4"), "-vn", "-ac", "1", "-ar", "8000", au])
    rms = audio_rms(au, 0.5); rmed = sorted(rms)[len(rms) // 2] if rms else 1
    seams = keep_seams(work); C = []
    t = 0.6
    while t < total - 0.5:
        i = min(n - 1, int(t * 30)); f = os.path.join(vf, fr[i]); sz = os.path.getsize(f)
        fc = min(pts, key=lambda p: abs(p[0] - t)) if pts else None
        fs = (fc[3] if fc and abs(fc[0] - t) < 1.5 else 0)
        a = rms[int(t / 0.5)] / rmed if rms and int(t / 0.5) < len(rms) and rmed else 1
        near = min([abs(t - s) for s in seams] or [9])
        C.append({"t": round(t, 2), "f": i + 1, "sz": sz, "face": fs, "au": a, "near": near}); t += 0.5
    if not C: return {"ok": False, "msg": "المقطع قصير"}
    smax = max(c["sz"] for c in C) or 1
    for c in C: c["sc"] = c["sz"] / smax * 1.0 + min(1.6, c["au"]) * 0.9 + (min(0.6, c["face"]) * 2.2 if face.get("found") else 0) - (0.8 if c["near"] < 0.25 else 0)
    C.sort(key=lambda c: -c["sc"]); pick = []
    for c in C:
        if all(abs(c["t"] - p["t"]) > max(2.0, total * 0.15) for p in pick): pick.append(c)
        if len(pick) >= k: break
    hs = hs_of(load_studio(work)); S = _sentences((rj(J(work, "caps.json"), {}) or {}).get("cards") or [])
    title = hs.get("title") or next((x.get("text") for x in (hs.get("hooks") or {}).get("items") or [] if x.get("text")), None)
    if not title:
        try: title = repurpose(work).get("title") or ""
        except Exception: title = S[0]["text"] if S else ""
    have = sorted(os.path.basename(f) for f in glob.glob(J(work, "cover-*.jpg")))
    return {"ok": True, "frames": [{"t": p["t"], "f": p["f"]} for p in sorted(pick, key=lambda p: p["t"])], "title": title[:60], "have": have}

# ── (8) مقطع واحد يطلع منه: كاروسيل + ثريد X + عنوان ووصف يوتيوب ──
def keywords(text, k=6):
    cnt = {}
    for w in _tok(text):
        b = _bare(w)
        if len(b) < 3 or w in STOP_W or b in STOP_W or w.isdigit(): continue
        cnt[b] = cnt.get(b, 0) + 1
    return [w for w, _ in sorted(cnt.items(), key=lambda x: -x[1])[:k]]
def repurpose(work, fresh=False):
    p = J(work, "repurpose.json")
    if os.path.exists(p) and not fresh: return rj(p, {})
    caps = rj(J(work, "caps.json"), {}) or {}; S = _sentences(caps.get("cards") or [], 0.45, 13); hs = hs_of(load_studio(work))
    if not S: return {"ok": False, "msg": "ما فيه كلام بالمقطع"}
    full = " ".join(s["text"] for s in S); title = (hs.get("title") or "").strip()
    sc = sorted(((hook_score(s["text"])[0] + min(1.0, len(s["text"].split()) / 9) - (0.6 if _weak0((_tok(s["text"]) or [""])[0]) else 0), i) for i, s in enumerate(S) if len(s["text"].split()) >= 4), reverse=True)
    if not title: title = S[sc[0][1]]["text"] if sc else S[0]["text"]
    title = _unconj(" ".join(title.split()[:12]))
    pts = sorted(i for _, i in sc[:6]); points = [_unconj(S[i]["text"]) for i in pts if _unconj(S[i]["text"]) != title][:5]
    kw = keywords(full); tags = ["#" + w.replace(" ", "_") for w in kw[:5]]
    thread = [title + "\n\nثريد:"] + ["%d. %s" % (i + 1, x) for i, x in enumerate(points)] + ["لو فادك، رتوِت أول تغريدة وتابعني لأكثر."]
    yt_title = (title if len(title) <= 90 else title[:88] + "…")
    desc = "\n".join([title, "", "بهالمقطع:"] + ["• " + x for x in points[:4]] + ["", " ".join(tags)])
    R = {"ok": True, "title": title, "points": points, "cta": "احفظه عشان ترجع له، وتابعني للجاي", "thread": thread, "yt": {"title": yt_title, "desc": desc}, "tags": tags, "by": "local", "at": int(time.time())}
    wj(p, R); return R

# ── سحب فيديو من رابط (تيك توك · يوتيوب · انستقرام · X · سناب …) بأداة yt-dlp المجانية ──
LONG_SEC = 360
def job_path(d): return J(d, ".hs", "job.json")
def job_get(d): return rj(job_path(d), {}) or {}
def job_set(d, **kw):
    os.makedirs(J(d, ".hs"), exist_ok=True)
    with _WJ_LOCK: j = job_get(d); j.update(kw); j["at"] = int(time.time()); wj(job_path(d), j)   # 4.33: قراءة وكتابة وحدة بوقتها
    return j
def ytdlp_cmd():
    try:
        if importlib.util.find_spec("yt_dlp"): return [PY, "-m", "yt_dlp"]
    except Exception: pass
    exe = shutil.which("yt-dlp")
    return [exe] if exe else None
# ── 4.26: بودكاست (beta): النص أول بدون تحميل الفيديو، وبعد ما تختار ينزل بس الأجزاء اللي اخترتها ──
_YTJS = {}
def yt_base():
    y = ytdlp_cmd()
    if not y: raise RuntimeError("NEED_YTDLP")
    if "js" not in _YTJS:
        try: _YTJS["js"] = bool(shutil.which("node")) and "--js-runtimes" in subprocess.run(y + ["--help"], capture_output=True, text=True, errors="replace", timeout=60).stdout
        except Exception: _YTJS["js"] = False
    out = y + (["--js-runtimes", "node"] if _YTJS["js"] else []); ck = hub_cfg().get("cookies")
    return out + (["--cookies-from-browser", ck] if ck else [])
def _vtt_t(s):
    p = s.strip().replace(",", ".").split(":"); p = [0] * (3 - len(p)) + p; return int(p[0]) * 3600 + int(p[1]) * 60 + float(p[2])
def vtt_segments(path):
    """VTT ← جمل بكلماتها. ترجمة يوتيوب التلقائية فيها وقت كل كلمة؛ اليدوية نوزّع الكلمات على وقت السطر."""
    txt = open(path, encoding="utf-8", errors="replace").read().replace("\r", ""); blocks = [b for b in txt.split("\n\n") if "-->" in b]
    timed = "<c>" in txt; words = []; prev = ""
    for b in blocks:
        ls = b.split("\n"); i = next(k for k, l in enumerate(ls) if "-->" in l); m = re.match(r"\s*([\d:.,]+)\s*-->\s*([\d:.,]+)", ls[i])
        if not m: continue
        cs, ce = _vtt_t(m.group(1)), _vtt_t(m.group(2)); body = [l for l in ls[i + 1:] if l.strip()]
        if timed:
            for l in body:
                plain = re.sub(r"<[^>]+>", "", l).strip()
                if "<c>" not in l and not re.search(r"<\d\d:", l):
                    if not plain or plain == prev: continue   # السطر المكرر من الجملة اللي قبل (ترجمة يوتيوب التلقائية تعيده)
                    w = plain.split(); prev = plain
                    for k, ww in enumerate(w): words.append([cs + (ce - cs) * k / max(1, len(w)), ww])
                    continue
                prev = plain; t0 = cs
                for tok in re.split(r"(<\d\d:\d\d:\d\d[.,]\d+>)", l):
                    mm = re.match(r"<([\d:.,]+)>", tok)
                    if mm: t0 = _vtt_t(mm.group(1)); continue
                    w = re.sub(r"<[^>]+>", "", tok).strip()
                    for k, ww in enumerate(w.split()): words.append([t0 + k * 0.01, ww])
        else:
            w = re.sub(r"<[^>]+>", "", " ".join(body)).split()
            for k, ww in enumerate(w): words.append([cs + (ce - cs) * k / max(1, len(w)), ww])
    words.sort(key=lambda x: x[0]); W = []; brk = False
    for k, (t, w) in enumerate(words):
        w = html.unescape(w); brk = brk or w.startswith(">>"); w = w.lstrip(">").strip()   # 4.31: «>>» تغيّر المتكلم بترجمة يوتيوب، كانت تطلع «&gt;&gt;» بالكابشن
        if not w or re.fullmatch(r"\[[^\]]*\]", w): continue
        if W and W[-1]["word"] == w and abs(W[-1]["start"] - t) < 0.05: continue
        W.append({"word": w, "start": round(t, 3), **({"brk": True} if brk else {})}); brk = False
    for k, w in enumerate(W): w["end"] = round(min(W[k + 1]["start"] if k + 1 < len(W) else w["start"] + 0.5, w["start"] + 1.2), 3)
    segs, cur = [], []
    for w in W:
        if cur and (w.get("brk") or w["start"] - cur[-1]["end"] > 0.7 or w["start"] - cur[0]["start"] > 10 or re.search(r"[.!?؟]$", cur[-1]["word"])): segs.append(cur); cur = []
        cur.append(w)
    if cur: segs.append(cur)
    return [{"start": s[0]["start"], "end": s[-1]["end"], "text": " ".join(x["word"] for x in s), "words": s, **({"spk": True} if s[0].get("brk") else {})} for s in segs if s]
def clips_text(url, d, lang=None, log=print):
    """النص والمعلومات بدون تحميل: يرجّع cfg أو None لو ما فيه ترجمة (فيرجع للتحميل الكامل والتفريغ)."""
    os.makedirs(J(d, ".hs"), exist_ok=True); y = yt_base()
    r = subprocess.run(y + ["--no-playlist", "--skip-download", "--dump-json", url], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
    try: info = json.loads((r.stdout or "").strip().split("\n")[-1])
    except Exception: raise RuntimeError("ما قدرت أقرأ الرابط: " + (r.stderr or "")[-200:])
    subs, auto = info.get("subtitles") or {}, info.get("automatic_captions") or {}
    l0 = (lang or info.get("language") or "").split("-")[0]
    cand = [("s", k) for k in subs if k.split("-")[0] == l0 and k != "live_chat"] + [("a", k) for k in auto if k == l0 + "-orig"] + [("a", k) for k in auto if k == l0]
    if not cand and not l0: cand = [("a", k) for k in auto if k.endswith("-orig")] + [("s", k) for k in subs if k != "live_chat"]
    if not cand: return None
    kind, key = cand[0]
    for f in glob.glob(J(d, "long.*.vtt")): os.remove(f)
    subprocess.run(y + ["--no-playlist", "--skip-download", "--write-subs" if kind == "s" else "--write-auto-subs", "--sub-langs", key, "--sub-format", "vtt", "-o", J(d, "long.%(ext)s"), url], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
    vt = (glob.glob(J(d, "long.*.vtt")) or [None])[0]
    if not vt: return None
    segs = vtt_segments(vt)
    if len(segs) < 3: return None
    lg = key.split("-")[0] or "en"; wj(J(d, "long.json"), {"text": " ".join(s["text"] for s in segs), "segments": segs, "language": lg, "from": "subs:" + key})
    dur = float(info.get("duration") or segs[-1]["end"]); cfg = clips_cfg(d)
    cfg.update({"src": "", "remote": info.get("webpage_url") or url, "vid": info.get("id"), "dur": round(dur, 2), "w": info.get("width") or 0, "h": info.get("height") or 0, "lang": lg,
                "title": info.get("title") or cfg.get("title") or "", "credit": info.get("uploader") or info.get("channel") or ""}); cfg.setdefault("clips", []); cfg.setdefault("cands", []); wj(J(d, "clips.json"), cfg)
    L = ["# %s · %s · اللغة: %s" % (cfg["title"], tfmt(dur), lg), ""] + ["[%s] %s" % (tfmt(s["start"]), s["text"].strip()) for s in segs]
    open(J(d, "transcript.txt"), "w", encoding="utf-8").write("\n".join(L))
    th = info.get("thumbnail")
    if th:
        try: open(J(d, ".hs", "th.jpg"), "wb").write(urllib.request.urlopen(urllib.request.Request(th, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read())
        except Exception: pass
    return cfg
def yt_section(url, a, b, out, log=print):
    """ينزّل جزء واحد من الفيديو بس (من a لين b)."""
    y = yt_base(); base = os.path.splitext(out)[0] + ".dl"
    for f in glob.glob(base + ".*"): os.remove(f)
    r = subprocess.run(y + ["--no-playlist", "--no-part", "--download-sections", "*%.2f-%.2f" % (a, b), "--force-keyframes-at-cuts", "-f", "bv*[height<=1920]+ba/b", "--merge-output-format", "mp4", "-o", base + ".%(ext)s", url],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=900)
    got = (glob.glob(base + ".mp4") or glob.glob(base + ".*") or [None])[0]
    if not got: raise RuntimeError("ما قدرت أنزّل الجزء: " + (r.stdout + r.stderr)[-200:])
    os.replace(got, out); return out
# ── 4.26: شخصية المقدّم الثابتة (نفسها لكل عملائك) ──
def pod_want(w, data):
    """اختيارات البودكاست من المكتبة (لغة الترجمة، الدبلجة، المقدّم) تنحفظ قبل ما يبدأ الشغل."""
    if (data or {}).get("mode") != "clips": return
    tr = str(data.get("tr") or "").strip()[:5]; dub = str(data.get("dub") or "").strip()[:5]; host = str(data.get("host", "0")) not in ("0", "false", "False", "")
    cfg = clips_cfg(w); W_ = cfg.get("want") or {}; W_.update({"tr": tr if tr in DUB_LANGS else "", "dub": dub if dub in DUB_LANGS else "", "host": host, "pod": True}); cfg["want"] = W_
    if data.get("identity"): W_["identity"] = str(data["identity"])[:40]   # 4.37: هويته لكل مقاطع الحلقة
    os.makedirs(w, exist_ok=True); wj(J(w, "clips.json"), cfg)
def host_cfg(): return {"on": True, "name": "", "char": "robo", "color": "#D97757", **(rj(os.path.join(HOME_CFG, "host.json"), {}) or {})}
def host_set(**kw):
    h = host_cfg(); h.update({k: v for k, v in kw.items() if v is not None}); os.makedirs(HOME_CFG, exist_ok=True); wj(os.path.join(HOME_CFG, "host.json"), h); return h
def grab_url(url, d, base, prog=None):
    y = ytdlp_cmd()
    if not y: raise RuntimeError("NEED_YTDLP")
    cmd = y + ["--no-playlist", "--newline", "--no-part", "--restrict-filenames", "-f", "bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1080]+ba/b[height<=1080]/b",
               "--merge-output-format", "mp4", "--write-info-json", "-o", J(d, base + ".%(ext)s"), url]
    ck = hub_cfg().get("cookies")
    if ck: cmd[len(y):len(y)] = ["--cookies-from-browser", ck]
    kw = {"stdout": subprocess.PIPE, "stderr": subprocess.STDOUT, "text": True, "encoding": "utf-8", "errors": "replace"}
    if os.name == "nt": kw["creationflags"] = 0x08000000
    pr = subprocess.Popen(cmd, **kw); tail = []
    for line in pr.stdout:
        tail = (tail + [line.strip()])[-12:]; m = re.search(r"\[download\]\s+([\d.]+)%", line)
        if m and prog: prog(float(m.group(1)))
    pr.wait()
    files = [f for f in glob.glob(J(d, base + ".*")) if not f.endswith((".json", ".part", ".ytdl")) and ".f" not in os.path.basename(f)[len(base):len(base) + 2]]
    if pr.returncode != 0 or not files:
        err = " ".join(x for x in tail if "ERROR" in x)[-300:] or " ".join(tail[-2:])[-300:]
        if re.search(r"login|cookies|sign in|private|rate.limit|Requested format", err, re.I): err += " ← NEED_COOKIES"
        raise RuntimeError(err or "ما قدرت أسحب الفيديو")
    meta = rj(J(d, base + ".info.json"), {}) or {}
    for f in glob.glob(J(d, base + "*.info.json")):
        try: os.remove(f)
        except Exception: pass
    f = max(files, key=os.path.getsize)
    if not f.lower().endswith((".mp4", ".mov", ".m4v")):
        out = J(d, base + ".mp4"); subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "aac", "-b:a", "192k", out], check=True)
        os.remove(f); f = out
    return f, {"title": meta.get("title") or "", "by": meta.get("uploader") or meta.get("channel") or "", "url": meta.get("webpage_url") or url, "site": meta.get("extractor_key") or "", "dur": meta.get("duration") or 0}
def job_run(d, src, mode="auto", pick="claude", n=5, ln=None, note="", lang=None, style="", ident=""):
    """المسار كامل بعد ما يوصل الفيديو (رابط أو ملف): auto = Claude يمنتجه · manual = يتجهّز وتمنتجه بنفسك · clips = لقطات من فيديو طويل."""
    os.makedirs(d, exist_ok=True); job_set(d, stage="grab", pct=0, mode=mode, pick=pick, note=note, err=None, done=False, t0=int(time.time()), src=src, n=n, len=ln)
    try:
        info = {}
        if mode == "clips" and re.match(r"https?://", src):   # 4.26: البودكاست: النص أول بدون تحميل
            job_set(d, stage="text", pct=None); tc = None
            try: tc = clips_text(src, d, lang)
            except Exception as e: job_set(d, note2=str(e)[:160])
            if tc:
                cfg = clips_cfg(d); W_ = cfg.get("want") or {}; W_.update({"n": int(n or 5), "len": ln or W_.get("len") or "25-75", "note": note or ""}); cfg["want"] = W_; wj(J(d, "clips.json"), cfg)
                projects_remember(d); job_set(d, stage="suggest"); clips_suggest(d, int(n or 5), ln, note, count=int(n or 5) * 2)
                job_set(d, stage="pick", done=True, textFirst=True); return d
        if re.match(r"https?://", src):
            f, info = grab_url(src, d, "download", prog=lambda p: job_set(d, pct=round(p, 1)))
        else:
            f = os.path.abspath(src)
            if not os.path.isfile(f): raise RuntimeError("ما لقيت الملف: " + f)
            if not f.lower().endswith((".mp4", ".mov", ".m4v")):   # 4.5: تسجيل الملقّن (webm) أو mkv: نحوّله mp4 بسرعة ثابتة
                job_set(d, stage="grab", pct=None); out = os.path.splitext(f)[0] + "-fixed.mp4"
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-vf", "fps=30", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", out], check=True)
                try: os.remove(f)
                except OSError: pass
                f = out
        dur = probe_dur(f); info["dur"] = round(dur, 1); wj(J(d, "source.json"), {**info, "src": src if re.match(r"https?://", src) else os.path.basename(f), "at": int(time.time())})
        if mode in ("auto", "manual") and dur > LONG_SEC: mode = "clips"; job_set(d, mode="clips", switched=True, pick=pick if pick in ("claude", "me") else "me")
        if mode == "clips":
            ext = os.path.splitext(f)[1].lower() or ".mp4"; lf = J(d, "long" + ext)
            if os.path.abspath(f) != os.path.abspath(lf): (shutil.move if os.path.dirname(os.path.abspath(f)) == os.path.abspath(d) else shutil.copy2)(f, lf)
            cfg = clips_cfg(d); cfg.update({"title": info.get("title") or cfg.get("title") or "", "credit": info.get("by") or "", "want": {**(cfg.get("want") or {}), "n": int(n or 5), "len": ln or "25-75", "note": note or ""}}); wj(J(d, "clips.json"), cfg)
            projects_remember(d); job_set(d, stage="transcribe", eta=int(max(60, dur * 1.2)), pct=None)
            clips_scan(lf, d, hub_cfg().get("prepModel") or "medium", lang)
            job_set(d, stage="suggest"); clips_suggest(d, n, ln, note, count=int(n or 5) * 2 if pick == "me" else None)
            C = clips_cfg(d).get("cands") or []
            if pick == "claude":
                task = ("حلقة طويلة جاهزة بمجلد %s (التفريغ: transcript.txt، والمرشّحات: hs clips cand %s list).\n"
                        "1) اقرأ النص كامل وقيّم المرشّحات كمحرّر محتوى قصير: الهوك بأول 3 ثواني، فكرة مكتملة، مشاعر أو رقم أو رأي جريء. عدّل الدرجات والأسباب (cand set) وأضف أي لحظة أقوى فاتت (cand add) واكتب لكل وحدة عنوان قصير.\n"
                        "2) اختر أقوى %d وسوّها: hs clips build %s --picks <ids> --edit none\n3) منتج كل مقطع حسب references/clips.md." % (d, d, int(n or 5), d))
                if note: task += "\nطلب المستخدم: " + note
                def fallback(w=None, C=C):   # بدون Claude أو وقف: ناخذ الأعلى ونجهّزها للتعديل اليدوي
                    if any(c.get("made") for c in clips_cfg(d).get("cands") or []): job_set(d, stage="done", done=True); return
                    job_set(d, stage="build", note2=(w or {}).get("msg")); clips_build(d, [c["id"] for c in C[: int(n or 5)]], "me"); job_set(d, stage="done", done=True)
                ok, msg = claude_spawn(d, task, "لقطات من فيديو طويل", on_done=lambda: job_set(d, stage="done", done=True), on_fail=fallback)
                if not ok: fallback({"msg": msg})
                else: job_set(d, stage="claude", done=True)
            else:
                task = ("حلقة طويلة بمجلد %s والمستخدم بيختار اللقطات بنفسه من المكتبة. لا تقص ولا تمنتج شي.\n"
                        "اقرأ transcript.txt والمرشّحات (hs clips cand %s list) وقيّم كل وحدة كم يتوقع تضرب (0-100) مع سبب قصير وعنوان، وعدّل البداية والنهاية عشان تبدأ بهوك وتنتهي بفكرة كاملة (cand set)، وأضف أقوى لحظات فاتت (cand add)." % (d, d))
                if note: task += "\nطلب المستخدم: " + note
                ok, _ = claude_spawn(d, task, "تقييم اللقطات") if hub_cfg().get("rankWithClaude", False) and have_claude() else (False, "")
                job_set(d, stage="pick", ranking=ok, done=True)
            return d
        sm = J(d, "src.mov")
        if os.path.abspath(f) != os.path.abspath(sm): (shutil.move if os.path.dirname(os.path.abspath(f)) == os.path.abspath(d) else shutil.copy2)(f, sm)
        st = load_studio(d)
        if info.get("title"): hs_of(st)["title"] = info["title"][:80]
        hs_of(st)["mode"] = "manual" if mode == "manual" else "claude"   # 4.18: اختيارك بالمكتبة يحدد وضع الاستوديو
        if style: hs_of(st)["wantStyle"] = style   # 4.37: «موشن جرافيك» من المكتبة
        if ident: hs_of(st)["identity"] = ident   # 4.37: هويته («none» = بدون)
        wj(J(d, "studio.json"), st)
        projects_remember(d)
        if mode == "manual":
            job_set(d, stage="prep"); prep(d, lang=lang)
            try: ident_apply(d)   # 4.37: يفتح الاستوديو بألوان هويته وخطوطها
            except Exception: pass
            job_set(d, stage="done", done=True)
        else:
            task = "فيديو جديد وصل من المكتبة: %s. منتجه كامل حسب SKILL.md من البداية (البث الحي ثم صفحة الأسئلة ثم المونتاج)." % sm
            if note: task += "\nملاحظته: " + note
            if style == "motion": task += "\nاختار «موشن جرافيك» من المكتبة: الموشن أساسي بهالمقطع، مو زينة. اقرأ engine/references/motion-graphics.md، وبصفحة الأسئلة الأسلوب مختار «موشن جرافيك»."
            I_ = ident_pick(d, ident or None)
            if I_: task += "\nهويته «%s» محفوظة: اقرأ %s وصمّم عليها (بصفحة الأسئلة مختارة لحالها)." % (I_.get("name") or I_["slug"], I_["md"]) + ((" " + ident_task(I_)) if I_.get("draft") else "")
            def fallback(w=None):   # Claude مو موجود أو وقف (حد، دخول، نت): نجهّزه تمنتجه بنفسك بدل ما يعلق
                if ready(d): job_set(d, stage="done", done=True); return
                studio_mode_set(d, "manual")   # Claude ما قدر يكمّل ← يفتح لك المونتاج اليدوي
                job_set(d, stage="prep", note2=(w or {}).get("msg"), done=False)
                try: prep(d, lang=lang); job_set(d, stage="done", done=True)
                except Exception as e: job_set(d, stage="error", err=str(e)[:500], done=True)
            ok, msg = claude_spawn(d, task, "مقطع جديد", on_done=lambda: job_set(d, stage="done", done=True), on_fail=fallback)
            if ok: job_set(d, stage="claude", done=True)
            else: job_set(d, claudeErr=msg, why="missing"); fallback({"msg": msg})
        return d
    except Exception as e:
        job_set(d, stage="error", err=str(e)[:500], done=True); raise
def cmd_grab(args):
    """hs grab <رابط أو ملف> [--root مجلد] [--into مجلد] [--name اسم] [--mode auto|manual|clips] [--pick claude|me] [--n 5] [--len 30-60] [--note "…"] [--lang ar]"""
    rest = list(args)
    def o(nm, dv=None):
        if nm in rest: i = rest.index(nm); v = rest[i + 1]; del rest[i:i + 2]; return v
        return dv
    if not rest: sys.exit(cmd_grab.__doc__)
    into = o("--into"); root = o("--root") or hub_cfg().get("root") or os.path.join(os.path.expanduser("~"), "Documents", "hojas-studio-projects")
    name = o("--name"); mode = o("--mode", "auto"); pick = o("--pick", "claude"); n = int(o("--n", "5")); ln = o("--len"); note = o("--note", ""); lang = o("--lang"); style = o("--style", ""); ident = o("--identity", "")
    src = rest[0]
    if not into:
        base = re.sub(r"[^\w\-]+", "-", name or ("long-" if mode == "clips" else "clip-") + time.strftime("%m%d-%H%M")).strip("-")[:40]
        into = os.path.join(root, base); k = 1
        while os.path.exists(into): into = os.path.join(root, "%s-%d" % (base, k)); k += 1
    try: d = job_run(os.path.abspath(into), src, mode, pick, n, ln, note, lang, style=style, ident=ident)
    except RuntimeError as e:
        m = str(e)
        if "NEED_YTDLP" in m: sys.exit("أداة السحب yt-dlp مو مثبّتة. استأذن المستخدم أول، ثم: %s -m pip install -U yt-dlp" % PY)
        if "NEED_COOKIES" in m: sys.exit("الموقع يبي تسجيل دخول. سجّل دخولك بالمتصفح ثم: python hs.py hub --cookies chrome (أو edge/firefox) وأعد. التفاصيل: " + m)
        sys.exit(m)
    j = job_get(d); print("جاهز:", d, "·", j.get("stage"))
    if j.get("mode") == "clips": print("المرشّحات: hs clips cand %s list" % d)
def cmd_prep(work, args):
    try: prep(work, model=(args[args.index("--model") + 1] if "--model" in args else None), lang=(args[args.index("--lang") + 1] if "--lang" in args else None), keep_silence="--keep-silence" in args)
    except RuntimeError as e: sys.exit(str(e))
    print("جاهز للتعديل اليدوي: افتح الاستوديو (hs open %s) أو من المكتبة." % work)

def cmd_clips(args):
    sub = args[0] if args else "help"; rest = list(args[1:])
    def o(nm, d=None):
        if nm in rest: i = rest.index(nm); v = rest[i + 1]; del rest[i:i + 2]; return v
        return d
    if sub == "scan":
        if len(rest) < 2: sys.exit("clips scan <الفيديو الطويل> <مجلد المقاطع> [--model medium] [--lang en|ar]")
        model = o("--model", "medium"); lang = o("--lang"); src, d = os.path.abspath(rest[0]), os.path.abspath(rest[1])
        try: cfg = clips_scan(src, d, model, lang)
        except RuntimeError as e: sys.exit(str(e))
        print("جاهز: %s" % J(d, "transcript.txt"))
        try: clips_suggest(d)
        except Exception as e: print("ما قدرت أرشّح لحالي:", e)
        print("المرشّحات بالترتيب: hs clips cand %s list" % d)
        print("اقرأ النص كامل وقيّم المرشّحات (cand set/add/rm)، ثم سوّ اللي تختاره:\n  hs clips make %s --from 12:30 --to 13:45 --title \"عنوان قصير بالعربي\" --credit \"اسم الضيف من اسم البرنامج\"\n  أو: hs clips build %s --picks c1,c3 --edit none" % (d, d))
    elif sub == "make":
        if not rest: sys.exit('clips make <مجلد المقاطع> --from 12:30 --to 13:45 --title "…" [--credit "…"] [--name اسم] [--style pod|plain]')
        d = os.path.abspath(rest[0]); a_, b_ = tsec(o("--from") or sys.exit("لازم --from")), tsec(o("--to") or sys.exit("لازم --to"))
        try: w = clip_make(d, a_, b_, o("--title", ""), o("--credit", ""), o("--name"), o("--style"))
        except RuntimeError as e: sys.exit(str(e))
        lang = clips_cfg(d).get("lang", "en")
        print("جاهز: %s (%s)" % (w, tfmt(b_ - a_)))
        print("كمّل عليه خطوات المونتاج العادية من «خطة القص» (MONTAGE.md الخطوة 3). التفريغ جاهز (a.json + fixes.json) فلا تعيده. وبعد الكابشن:")
        if lang != "ar": print("  hs tr %s export   ← اكتب الترجمة العربية لكل جملة ثم tr import" % w)
        print("  أو جهّزه للتعديل اليدوي كامل: hs prep " + w)
    elif sub == "suggest":
        d = os.path.abspath(rest[0]) if rest else sys.exit("clips suggest <مجلد> [--n 6] [--len 30-60] [--note \"طلبه\"]")
        ln = o("--len"); C = clips_suggest(d, int(o("--n", "0") or 0) or None, ln, o("--note"))
        for c in C: print("  %s  %s ← %s  %d%%  %s" % (c["id"], tfmt(c["from"]), tfmt(c["to"]), c["score"], " · ".join(c.get("why") or [])))
    elif sub == "cand": cmd_cand(rest)
    elif sub == "build":
        d = os.path.abspath(rest[0]) if rest else sys.exit("clips build <مجلد> --picks c1,c3 [--edit none|me|claude]")
        picks = [x.strip() for x in (o("--picks") or "").split(",") if x.strip()]; edit = o("--edit", "none")
        pf = o("--json")
        if pf: picks = rj(pf, []) or []
        if not picks: sys.exit("لازم --picks")
        ws = clips_build(d, picks, edit)
        for w in ws: print("جاهز:", w)
    elif sub == "list":
        d = os.path.abspath(rest[0]) if rest else sys.exit("clips list <مجلد المقاطع>"); cfg = clips_cfg(d)
        print("%s · %s" % (os.path.basename(cfg.get("src", "")), tfmt(cfg.get("dur", 0))))
        for c in cfg.get("clips") or []: print("  %s  %s ← %s  %s" % (c["name"], tfmt(c["from"]), tfmt(c["to"]), c.get("title", "")))
        for c in cfg.get("cands") or []: print("  [%s] %s ← %s  %d%%%s  %s" % (c["id"], tfmt(c["from"]), tfmt(c["to"]), c.get("score", 0), " ✓" if c.get("made") else "", c.get("title") or ""))
    else: sys.exit("clips scan <فيديو> <مجلد> | suggest <مجلد> | cand <مجلد> list|add|set|rm | make <مجلد> --from 12:30 --to 13:45 --title \"…\" | build <مجلد> --picks c1,c3 --edit none|me|claude | list <مجلد>")

# ───────────────────────── 4.3: المكتبة (كل المشاريع من مكان واحد · جوال وكمبيوتر) ─────────────────────────
HUB_PORT = 8800
def hub_cfg_path(): return os.path.join(HOME_CFG, "hub.json")
def hub_cfg(): return rj(hub_cfg_path(), {}) or {}
def projects_reg_path(): return os.path.join(HOME_CFG, "projects.json")
def projects_remember(work):
    try:
        os.makedirs(HOME_CFG, exist_ok=True); reg = rj(projects_reg_path(), []) or []; w = os.path.abspath(work)
        reg = [x for x in reg if os.path.normcase(x) != os.path.normcase(w)]; reg.insert(0, w); wj(projects_reg_path(), reg[:200])
    except Exception: pass
def cmds_path(): return os.path.join(HOME_CFG, "commands.json")
def cmd_log_add(work, label, task, snap):
    try:
        os.makedirs(HOME_CFG, exist_ok=True); L = rj(cmds_path(), []) or []; cid = "c%d" % int(time.time() * 1000)
        L.insert(0, {"id": cid, "at": time.time(), "work": os.path.abspath(work), "label": label[:200], "task": task[:1500], "snap": snap, "status": "running", "result": ""})
        wj(cmds_path(), L[:300]); return cid
    except Exception: return None
def cmd_log_set(cid, **kw):
    if not cid: return
    try:
        L = rj(cmds_path(), []) or []
        for x in L:
            if x["id"] == cid: x.update(kw)
        wj(cmds_path(), L)
    except Exception: pass
def claude_last_err(hours=8):
    """آخر مرة Claude وقف بسبب يخص الحساب (حد، دخول، رصيد) ولا نجح شي بعدها: نعرضه فوق المكتبة."""
    try:
        for x in rj(cmds_path(), []) or []:
            if x.get("status") == "done" or time.time() - x.get("at", 0) > hours * 3600: return None
            if x.get("status") == "err" and x.get("why") in ("limit", "login", "credit") and not x.get("seen"): return {"msg": x.get("result") or "", "why": x["why"], "at": x.get("at")}
    except Exception: pass
    return None
def cmd_log_clear_err():
    try:
        L = rj(cmds_path(), []) or []
        for x in L:
            if x.get("status") == "err": x["seen"] = True
        wj(cmds_path(), L)
    except Exception: pass
def is_ep(d): return os.path.isdir(d) and os.path.exists(os.path.join(d, "clips.json"))
def ep_card(d):
    cfg = clips_cfg(d); jb = job_get(d); so = rj(J(d, "source.json"), {}) or {}; C = cfg.get("cands") or []; made = cfg.get("clips") or []
    stg = jb.get("stage") or ("pick" if C else "transcribe"); err = jb.get("err")
    if stg == "error": state, sub = "err", "وقف: " + (err or "")[:90]
    elif stg in ("grab", "transcribe", "suggest", "build"): state, sub = "work", {"grab": "يسحب الفيديو", "transcribe": "يفرّغ الكلام", "suggest": "يرشّح اللقطات", "build": "يقص اللقطات"}[stg]
    elif stg == "claude" and not jb.get("claudeErr"): state, sub = "work", "Claude يختار ويمنتج"
    elif made: state, sub = "ready", "%d مقطع جاهز · %d مرشّح" % (len(made), len(C))
    else: state, sub = "wait", "اختر لقطاتك (%d مرشّح)" % len(C)
    return {"kind": "ep", "id": hashlib.md5(os.path.normcase(os.path.abspath(d)).encode()).hexdigest()[:10], "work": os.path.abspath(d), "name": os.path.basename(d.rstrip("/\\")),
            "title": cfg.get("title") or so.get("title") or os.path.basename(d.rstrip("/\\")), "by": so.get("by") or cfg.get("credit") or "", "url": so.get("url"), "dur": cfg.get("dur") or so.get("dur") or 0,
            "thumb": ".hs/th.jpg" if os.path.exists(J(d, ".hs", "th.jpg")) else None, "stage": stg, "pct": jb.get("pct"), "t0": jb.get("t0"), "eta": jb.get("eta"), "err": err,
            "cands": len(C), "made": len(made), "state": state, "sub": sub, "note": jb.get("claudeErr"), "why": jb.get("why"), "w": cfg.get("w") or 0, "h": cfg.get("h") or 0, "mt": int(max([os.path.getmtime(J(d, f)) for f in ("clips.json", ".hs/job.json") if os.path.exists(J(d, f))] or [os.path.getmtime(d)]))}
def job_card(d):
    jb = job_get(d); so = rj(J(d, "source.json"), {}) or {}; stg = jb.get("stage") or "grab"
    sub = {"grab": "يسحب الفيديو", "prep": "يتجهّز", "transcribe": "يفرّغ", "error": "وقف: " + (jb.get("err") or "")[:90]}.get(stg, stg)
    return {"kind": "job", "id": hashlib.md5(os.path.normcase(os.path.abspath(d)).encode()).hexdigest()[:10], "work": os.path.abspath(d), "name": os.path.basename(d.rstrip("/\\")),
            "title": so.get("title") or jb.get("src") or os.path.basename(d), "dur": so.get("dur") or 0, "thumb": None, "stage": stg, "pct": jb.get("pct"), "err": jb.get("err"), "mode": jb.get("mode"),
            "state": "err" if stg == "error" else "work", "sub": sub, "note": jb.get("claudeErr"), "why": jb.get("why"), "mt": jb.get("at") or 0}
def hub_eps(root):
    seen, out = set(), []
    cands = [w for w in rj(projects_reg_path(), []) or []]
    if root and os.path.isdir(root): cands += [os.path.join(root, n) for n in sorted(os.listdir(root)) if not n.startswith(".")]
    for d in cands:
        k = os.path.normcase(os.path.abspath(d))
        if k in seen or not os.path.isdir(d): continue
        seen.add(k)
        if is_ep(d): out.append(ep_card(d))
        elif os.path.exists(job_path(d)) and not is_project(d):
            jb = job_get(d)
            if not jb.get("done") or jb.get("stage") == "error": out.append(job_card(d))
    return out
# ── 4.4: قاعدة بيانات المقاطع (SQLite على جهازه فقط): العناوين والكلام بالتوقيت والملاحظات ──
DB_VER = 1
AR_NORM = str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ة": "ه", "ى": "ي", "ؤ": "و", "ئ": "ي", "ـ": ""})
def norm_txt(s): return re.sub(r"[ً-ٰٟۖ-ۭ]", "", str(s or "")).translate(AR_NORM).lower()
def db_path(): return os.path.join(HOME_CFG, "library.db")
_DBL = threading.Lock()
def db_conn():
    import sqlite3
    os.makedirs(HOME_CFG, exist_ok=True); c = sqlite3.connect(db_path(), timeout=15, check_same_thread=False)
    c.execute("PRAGMA journal_mode=WAL")
    c.execute("CREATE TABLE IF NOT EXISTS meta (k TEXT PRIMARY KEY, v TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS items (id TEXT PRIMARY KEY, kind TEXT, work TEXT, title TEXT, dur REAL, sig TEXT, at REAL, made REAL, src TEXT, by TEXT, lang TEXT, words INTEGER)")
    fts = True
    try: c.execute("CREATE VIRTUAL TABLE IF NOT EXISTS fx USING fts5(body, item UNINDEXED, t UNINDEXED, field UNINDEXED, orig UNINDEXED, tokenize='unicode61')")
    except Exception:
        fts = False; c.execute("CREATE TABLE IF NOT EXISTS fx (body TEXT, item TEXT, t REAL, field TEXT, orig TEXT)")
    return c, fts
def item_id(work): return hashlib.md5(os.path.normcase(os.path.abspath(work)).encode()).hexdigest()[:10]
def db_sig(work, kind):
    fs = ("caps.json", "studio.json", "notes.json", "a.json", "source.json") if kind == "proj" else ("clips.json", "long.json", "source.json")
    return "%d:" % DB_VER + ",".join("%d" % int(os.path.getmtime(J(work, f))) if os.path.exists(J(work, f)) else "-" for f in fs)
def db_rows(work, kind):
    """يرجّع (معلومات المقطع، صفوف البحث [(النص، التوقيت، الحقل)])"""
    rows = []; so = rj(J(work, "source.json"), {}) or {}
    if kind == "ep":
        cfg = clips_cfg(work); title = cfg.get("title") or so.get("title") or os.path.basename(work.rstrip("/\\")); dur = cfg.get("dur") or so.get("dur") or 0; lang = cfg.get("lang")
        for s in (rj(J(work, "long.json"), {}) or {}).get("segments") or []:
            if str(s.get("text", "")).strip(): rows.append((s["text"].strip(), round(float(s["start"]), 2), "say"))
        for c in cfg.get("cands") or []:
            if c.get("title"): rows.append((c["title"], round(float(c["from"]), 2), "cand"))
    else:
        hs = hs_of(load_studio(work)); caps = rj(J(work, "caps.json"), {}) or {}
        title = (hs.get("title") or (hs.get("pod") or {}).get("title") or (hs.get("dahih") or {}).get("title") or "").strip() or os.path.basename(work.rstrip("/\\"))
        dur = float(caps.get("total") or so.get("dur") or 0); lang = (hs.get("pod") or {}).get("lang") or "ar"
        cards = caps.get("cards") or []
        if cards:
            for c in cards:
                tx = " ".join(str(w.get("t", "")) for w in c.get("w") or []).strip()
                if tx: rows.append((tx, round(float(c.get("s", 0)), 2), "say"))
        else:
            for s in (rj(J(work, "a.json"), {}) or {}).get("segments") or []:
                if str(s.get("text", "")).strip(): rows.append((s["text"].strip(), round(float(s["start"]), 2), "say"))
        for n in rj(J(work, "notes.json"), []) or []:
            tx = " ".join(x for x in (n.get("text"), n.get("reply")) if x)
            if tx: rows.append((tx, round(float(n.get("t") or 0), 2), "note"))
        for L in hs.get("layers") or []:
            tx = " ".join(str(L.get(k) or "") for k in ("text", "title", "sub") if isinstance(L.get(k), str)).strip()
            if tx: rows.append((tx[:300], round(float(L.get("s", 0)), 2), "layer"))
        for h in ((hs.get("hooks") or {}).get("items") or []):
            if h.get("text"): rows.append((h["text"], 0.0, "hook"))
        pt = J(work, "post.txt")
        if os.path.exists(pt): rows.append((open(pt, encoding="utf-8", errors="replace").read()[:2000], None, "post"))
    meta = " ".join(x for x in (title, os.path.basename(work.rstrip("/\\")), so.get("title"), so.get("by"), so.get("site")) if x)
    rows.insert(0, (meta, None, "title"))
    info = {"title": title, "dur": round(float(dur or 0), 1), "src": so.get("url") or "", "by": so.get("by") or "", "lang": lang or "",
            "made": os.path.getctime(work) if os.path.exists(work) else 0, "words": sum(len(r[0].split()) for r in rows if r[2] == "say")}
    return info, rows
def db_index(work, kind="proj", force=False, c=None):
    own = c is None
    if own: c, _ = db_conn()
    iid = item_id(work); sig = db_sig(work, kind)
    try:
        r = c.execute("SELECT sig FROM items WHERE id=?", (iid,)).fetchone()
        if r and r[0] == sig and not force: return False
        info, rows = db_rows(work, kind)
        with _DBL:
            c.execute("DELETE FROM fx WHERE item=?", (iid,))
            c.executemany("INSERT INTO fx (body, item, t, field, orig) VALUES (?,?,?,?,?)", [(norm_txt(tx), iid, t, f, tx) for tx, t, f in rows])
            c.execute("INSERT OR REPLACE INTO items (id, kind, work, title, dur, sig, at, made, src, by, lang, words) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                      (iid, kind, os.path.abspath(work), info["title"], info["dur"], sig, time.time(), info["made"], info["src"], info["by"], info["lang"], info["words"]))
            c.commit()
        return True
    finally:
        if own: c.close()
def db_sync(root=None, force=False):
    c, _ = db_conn(); n = 0; seen = set()
    try:
        for w in hub_projects(root):
            seen.add(item_id(w))
            try: n += db_index(w, "proj", force, c)
            except Exception: pass
        for e in hub_eps(root):
            if e.get("kind") != "ep": continue
            seen.add(e["id"])
            try: n += db_index(e["work"], "ep", force, c)
            except Exception: pass
        gone = [r[0] for r in c.execute("SELECT id FROM items").fetchall() if r[0] not in seen]
        with _DBL:
            for i in gone: c.execute("DELETE FROM fx WHERE item=?", (i,)); c.execute("DELETE FROM items WHERE id=?", (i,))
            c.execute("INSERT OR REPLACE INTO meta VALUES ('synced', ?)", (str(time.time()),)); c.commit()
        return n, len(gone)
    finally: c.close()
def _hl(orig, toks):
    out = []
    for w in re.split(r"(\s+)", str(orig)):
        nw = norm_txt(re.sub(r"[^\w]", "", w))
        out.append([w, bool(nw) and any(nw.startswith(t) or (len(t) > 2 and t in nw) for t in toks)])
    return out
def db_search(q, limit=30, kind=None):
    toks = [t for t in re.findall(r"\w+", norm_txt(q)) if t][:8]
    if not toks: return {"q": q, "items": []}
    c, fts = db_conn()
    try:
        if fts:
            mq = " ".join('"%s"*' % t.replace('"', "") for t in toks)
            try: rows = c.execute("SELECT item, t, field, orig, bm25(fx) FROM fx WHERE fx MATCH ? ORDER BY bm25(fx) LIMIT 600", (mq,)).fetchall()
            except Exception: rows = []
        else:
            sql = " AND ".join("body LIKE ?" for _ in toks)
            rows = [r + (0,) for r in c.execute("SELECT item, t, field, orig FROM fx WHERE " + sql + " LIMIT 600", ["%" + t + "%" for t in toks]).fetchall()]
        if not rows:   # بحث أوسع: أي كلمة من الكلمات
            mq = " OR ".join('"%s"*' % t for t in toks)
            try: rows = c.execute("SELECT item, t, field, orig, bm25(fx) FROM fx WHERE fx MATCH ? ORDER BY bm25(fx) LIMIT 300", (mq,)).fetchall() if fts else []
            except Exception: rows = []
        items = {r[0]: r for r in c.execute("SELECT id, kind, work, title, dur, made, src, by, words FROM items").fetchall()}
        by = {}
        for iid, t, field, orig, rank in rows:
            it = items.get(iid)
            if not it or (kind and it[1] != kind): continue
            g = by.setdefault(iid, {"id": iid, "kind": it[1], "work": it[2], "title": it[3], "dur": it[4], "made": it[5], "src": it[6], "by": it[7], "score": 0.0, "titleHit": False, "hits": []})
            g["score"] += -float(rank or 0) * (3 if field == "title" else 1) + (2 if field == "title" else 0.4)
            if field == "title": g["titleHit"] = True
            elif len(g["hits"]) < 6: g["hits"].append({"t": t, "field": field, "text": _hl(str(orig)[:260], toks)})
        out = sorted(by.values(), key=lambda g: -g["score"])[:limit]
        for g in out: g["hits"].sort(key=lambda h: (h["t"] is None, h["t"] or 0))
        return {"q": q, "items": out, "total": sum(len(g["hits"]) for g in by.values())}
    finally: c.close()
def db_stats():
    c, fts = db_conn()
    try:
        n = c.execute("SELECT COUNT(*), COALESCE(SUM(dur),0), COALESCE(SUM(words),0) FROM items").fetchone(); s = c.execute("SELECT COUNT(*) FROM fx WHERE field='say'").fetchone()[0]
        syn = (c.execute("SELECT v FROM meta WHERE k='synced'").fetchone() or [0])[0]
        return {"items": n[0], "secs": round(n[1]), "words": n[2], "lines": s, "fts": fts, "path": db_path(), "size": os.path.getsize(db_path()) if os.path.exists(db_path()) else 0, "synced": float(syn or 0)}
    finally: c.close()
def cmd_db(args):
    """hs db index [--full] · search "كلمة" [--n 20] · stats · reset"""
    sub = args[0] if args else "stats"; rest = list(args[1:]); root = hub_cfg().get("root")
    if sub == "index":
        n, g = db_sync(root, "--full" in rest); s = db_stats(); print("انفهرس %d مقطع (وانشال %d محذوف). بالقاعدة: %d مقطع · %d جملة · %s" % (n, g, s["items"], s["lines"], s["path"]))
    elif sub == "search":
        q = " ".join(x for x in rest if not x.startswith("--")) or sys.exit('db search "كلمة"'); n = int(rest[rest.index("--n") + 1]) if "--n" in rest else 20
        db_sync(root); R = db_search(q, n)
        if not R["items"]: print("ما لقيت شي لـ «%s»" % q); return
        for g in R["items"]:
            print("● %s  [%s] %s" % (g["title"], "حلقة" if g["kind"] == "ep" else "مقطع", g["work"]))
            for h in g["hits"]: print("    %s  %s" % (tfmt(h["t"]) if h["t"] is not None else "  -  ", "".join(w for w, _ in h["text"])[:150]))
    elif sub == "stats":
        s = db_stats(); print("القاعدة: %s\n%d مقطع · %d جملة · %d كلمة · %s ساعة كلام · %.1f ميقا · بحث %s" % (s["path"], s["items"], s["lines"], s["words"], round(s["secs"] / 3600, 1), s["size"] / 1e6, "سريع (FTS5)" if s["fts"] else "عادي"))
    elif sub == "reset":
        for f in (db_path(), db_path() + "-wal", db_path() + "-shm"):
            if os.path.exists(f): os.remove(f)
        print("انمسحت القاعدة (مقاطعك نفسها ما انلمست). تنبني من جديد أول ما تفتح المكتبة أو: hs db index")
    else: sys.exit(cmd_db.__doc__)
def proj_dup(w):
    base = os.path.basename(w.rstrip("/\\")); dst = os.path.join(os.path.dirname(w), base + "-v2"); k = 2
    while os.path.exists(dst): k += 1; dst = os.path.join(os.path.dirname(w), "%s-v%d" % (base, k))
    def ign(dd, names): return [n for n in names if n in (".hs", "out", "prev", "claude.log", "whisper.log", "mk") or n.endswith(".wav")] if os.path.abspath(dd) == os.path.abspath(w) else []
    shutil.copytree(w, dst, ignore=ign)   # نسخة كاملة مستقلة (الروابط الصلبة تخرّب الأصل لو انعاد رسم الفيديو)
    st = load_studio(dst); hs = hs_of(st); t0 = proj_card(w)["title"]; hs["title"] = t0 + " (نسخة)"; wj(J(dst, "studio.json"), st)
    projects_remember(dst); return dst
def spawn_bg(args, logf):
    kw = {"stdin": subprocess.DEVNULL, "stdout": open(logf, "ab"), "stderr": subprocess.STDOUT}
    if os.name == "nt": kw["creationflags"] = 0x00000008 | 0x00000200 | 0x08000000
    else: kw["start_new_session"] = True
    return subprocess.Popen([PY, os.path.abspath(__file__)] + args, **kw)
def is_project(d): return os.path.isdir(d) and any(os.path.exists(os.path.join(d, f)) for f in ("caps.json", "studio.json", "src.mov", "cutz.mp4"))
def project_trash(w, root=None):
    """ينقل المشروع (أو الحلقة كاملة) لـ <مجلد المشاريع>/.trash/ بدل ما يمسحه، ويشيله من القائمة ومن مقاطع الحلقة."""
    w = os.path.abspath(w); base = os.path.abspath(root) if root and os.path.isdir(root) else os.path.dirname(w)
    if os.path.normcase(os.path.dirname(w)) != os.path.normcase(base) and os.path.isfile(os.path.join(os.path.dirname(w), "clips.json")):
        base = os.path.dirname(os.path.dirname(w))   # مقطع داخل حلقة: سلة مجلد المشاريع نفسه
    tr = os.path.join(base, ".trash"); os.makedirs(tr, exist_ok=True)
    dst = os.path.join(tr, "%s-%s" % (os.path.basename(w), time.strftime("%Y%m%d-%H%M%S")))
    ep = os.path.dirname(w) if os.path.isfile(os.path.join(os.path.dirname(w), "clips.json")) else None
    shutil.move(w, dst)
    try:
        reg = [x for x in (rj(projects_reg_path(), []) or []) if not os.path.normcase(os.path.abspath(x)).startswith(os.path.normcase(w))]; wj(projects_reg_path(), reg)
    except Exception: pass
    if ep:
        try:
            cfg = clips_cfg(ep); nm = os.path.basename(w); cfg["clips"] = [c for c in cfg.get("clips") or [] if c.get("name") != nm]
            for c in cfg.get("cands") or []:
                if c.get("made") == nm: c.pop("made", None)
            wj(os.path.join(ep, "clips.json"), cfg)
        except Exception: pass
    return dst
def hub_projects(root):
    seen, out = set(), []
    def add(d):
        k = os.path.normcase(os.path.abspath(d))
        if k in seen or not is_project(d): return
        seen.add(k); out.append(os.path.abspath(d))
    for w in rj(projects_reg_path(), []) or []: add(w)
    if root and os.path.isdir(root):
        for n in sorted(os.listdir(root)):
            d = os.path.join(root, n)
            if not os.path.isdir(d) or n.startswith("."): continue
            if is_project(d): add(d)
            elif os.path.exists(os.path.join(d, "clips.json")):
                for m in sorted(os.listdir(d)): add(os.path.join(d, m))
    return out
_PM = {"t": 0, "m": {}}; _PML = threading.Lock()
def port_map(fresh=False):
    """4.4: خريطة المشاريع الشغّالة {مسار: بورت}. فحص سريع ومتوازي ومخزّن ثواني (ويندوز يتأخر ثانيتين على كل بورت مقفل)."""
    with _PML:
        if not fresh and time.time() - _PM["t"] < 4: return _PM["m"]
        m = {}
        def one(p):
            s = socket.socket(); s.settimeout(0.25)
            try:
                if s.connect_ex(("127.0.0.1", p)) != 0: return
            except Exception: return
            finally: s.close()
            try:
                with urllib.request.urlopen("http://127.0.0.1:%d/hs/info" % p, timeout=2) as r: d = json.loads(r.read().decode())
                if d.get("work"): m[os.path.normcase(os.path.abspath(d["work"]))] = p
            except Exception: pass
        th = [threading.Thread(target=one, args=(p,), daemon=True) for p in range(HUB_PORT + 1, HUB_PORT + 40)]
        for t in th: t.start()
        for t in th: t.join(3)
        _PM.update(t=time.time(), m=m); return m
def proj_port(work, fresh=False): return port_map(fresh).get(os.path.normcase(os.path.abspath(work)))
def proj_live(port):
    try:
        with urllib.request.urlopen("http://127.0.0.1:%d/hs/pulse" % port, timeout=1.5) as r: return json.loads(r.read().decode())
    except Exception: return None
CL_IDLE = 20 * 60   # لو Claude ما كتب شي من 20 دقيقة وآخر خطوة مو «خلص» نعتبره وقف (التفريغ الطويل ياخذ ربع ساعة)
def proj_card(work, live=False):
    caps = rj(J(work, "caps.json"), {"cards": [], "total": 0}) or {"cards": [], "total": 0}; st = load_studio(work); hs = hs_of(st)
    sfx = rj(J(work, "sfx.json"), {"outro": 0}) or {}; total = float(caps.get("total") or 0); dur = total + float(sfx.get("outro") or 0)
    title = (hs.get("title") or (hs.get("pod") or {}).get("title") or (hs.get("dahih") or {}).get("title") or "").strip() or os.path.basename(work.rstrip("/\\"))
    pst = prep_state(work); jb = job_get(work)
    ed = J(work, ".hs", "exports"); exps = sorted(glob.glob(os.path.join(ed, "*.mp4")), key=os.path.getmtime) if os.path.isdir(ed) else []
    smt = max([os.path.getmtime(J(work, f)) for f in ("studio.json", "caps.json", "theme.json") if os.path.exists(J(work, f))] or [0])
    notes = rj(J(work, "notes.json"), []) or []; ask = sum(1 for n in notes if n.get("status") == "ask"); openn = sum(1 for n in notes if n.get("status") in ("open", "sent"))
    bstate = brief_state(work); port = proj_port(work) if live else None; pl = proj_live(port) if port else None
    agent = bool(pl and (pl.get("agent") or {}).get("running")); job = bool(pl and (pl.get("job") or {}).get("running"))
    # 4.7.1: وين وصل Claude؟ من آخر سطر كتبه بسجل المشروع (Claude من الطرفية ما يبان كـ agent)
    acts = activity(work, 0, 400); la = acts[-1] if acts else {}; lt = int(la.get("t") or 0); age = time.time() - lt if lt else 1e9
    lkind = la.get("kind") or ""; ltext = (la.get("text") or "").strip()
    if lkind == "done" and ltext.startswith("حفظ إجاباته"): lkind = "step"   # حفظ الأسئلة مو نهاية الشغل
    cl_on = bool(agent or (lt and lkind not in ("done",) and age < CL_IDLE))
    cl_stop = bool(lt and not agent and not job and lkind not in ("done",) and age >= CL_IDLE and not (exps and os.path.getmtime(exps[-1]) > lt))
    if bstate == "pending" or ask: state = "wait"
    elif cl_stop: state = "wait"
    elif agent or job or cl_on or not exps: state = "work"
    else: state = "ready"
    prepping = bool(pst and not pst.get("done") and not pst.get("err") and time.time() - pst.get("at", 0) < 3600)
    if prepping or (pst and pst.get("err")): state = "work"
    if prepping: sub = "يتجهّز للمونتاج اليدوي (%d/%d)" % (pst.get("i", 0) + 1, pst.get("n", 5))
    elif pst and pst.get("err"): sub = "التجهيز وقف: " + pst["err"][:80]
    elif agent or (cl_on and ltext): sub = ("Claude: " + ltext[:110]) if ltext else "Claude يشتغل عليه"
    elif cl_stop: sub = "Claude وقف عند: " + (ltext[:110] or "خطوة ما انكتبت")
    elif job: sub = "يصدّر الحين"
    elif bstate == "pending": sub = "ينتظر إجاباتك"
    elif ask: sub = "Claude ينتظر ردك (%d)" % ask
    elif jb.get("stage") == "claude" and not jb.get("claudeErr"): sub = "Claude يمنتجه"; state = "work"
    elif jb.get("claudeErr") and not caps.get("cards"): sub = jb["claudeErr"][:90]; state = "work"
    elif not caps.get("cards"): sub = "يتجهّز"
    elif not exps: sub = "ما تصدّر بعد"
    elif smt > os.path.getmtime(exps[-1]) + 2: sub = "فيه تعديل ما تصدّر"
    else: sub = "جاهز"
    D = max(dur, 0.1); lanes = {"img": [], "cap": [], "vid": [], "sfx": []}
    for L in hs.get("layers") or []:
        if L.get("off") or L.get("type") == "fx": continue
        lanes["img"].append([round(float(L.get("s", 0)) / D, 4), round(float(L.get("e", 0)) / D, 4)])
    for c in caps.get("cards") or []: lanes["cap"].append([round(c["s"] / D, 4), round(c["e"] / D, 4)])
    cut = (rj(J(work, "cut.json"), {}) or {}).get("keep") or []; acc = 0
    for a, b in cut: lanes["vid"].append([round(acc / D, 4), round((acc + b - a) / D, 4)]); acc += b - a
    if not cut and total: lanes["vid"].append([0, round(total / D, 4)])
    for k, v in sfx.items():
        if isinstance(v, list):
            for x in v:
                t0 = float(x[0] if isinstance(x, list) else x); lanes["sfx"].append([round(t0 / D, 4), round(min(D, t0 + 0.35) / D, 4)])
    th = None
    for f in ("vfr/00045.jpg", "vfr/00001.jpg", ".hs/th/2.jpg", ".hs/th/1.jpg"):
        if os.path.exists(J(work, f)): th = f; break
    return {"work": work, "id": hashlib.md5(os.path.normcase(work).encode()).hexdigest()[:10], "name": os.path.basename(work.rstrip("/\\")), "title": title, "dur": round(dur, 1), "note": jb.get("claudeErr"), "why": jb.get("why"),
            "state": state, "sub": sub, "lanes": lanes, "thumb": th, "final": os.path.relpath(exps[-1], work).replace("\\", "/") if exps else None, "last": ltext[:160] if (agent or cl_on) else "", "lastT": lt, "lastKind": lkind, "stopped": cl_stop, "steps": len(acts), "mt": int(max(smt, os.path.getmtime(work))), "notes": openn, "ask": ask, "port": port, "agent": agent, "job": job,
            "prep": ({"stage": pst.get("stage"), "i": pst.get("i", 0), "n": pst.get("n", 5), "t0": pst.get("t0"), "eta": pst.get("eta"), "err": pst.get("err")} if pst and not pst.get("done") else None),
            "manual": (jb.get("mode") == "manual") or bool(pst), "src": (rj(J(work, "source.json"), {}) or {}).get("url"), "clip": hs.get("clip"), "pod": bool((hs.get("pod") or {}).get("on"))}
def battery():
    try:
        if os.name == "nt":
            import ctypes
            class SPS(ctypes.Structure): _fields_ = [("ac", ctypes.c_byte), ("flag", ctypes.c_byte), ("pct", ctypes.c_byte), ("r", ctypes.c_byte), ("life", ctypes.c_ulong), ("full", ctypes.c_ulong)]
            s = SPS()
            if ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(s)):
                if s.flag & 128 or s.pct == -1 or (s.pct & 0xFF) == 255: return {"has": False, "ac": True}
                return {"has": True, "pct": s.pct & 0xFF, "ac": s.ac == 1}
        elif sys.platform == "darwin":
            o = subprocess.run(["pmset", "-g", "batt"], capture_output=True, text=True, timeout=3).stdout; m = re.search(r"(\d+)%", o)
            if m: return {"has": True, "pct": int(m.group(1)), "ac": "AC Power" in o}
            return {"has": False, "ac": True}
        else:
            for b in glob.glob("/sys/class/power_supply/BAT*"):
                pct = int(open(os.path.join(b, "capacity")).read().strip()); stt = open(os.path.join(b, "status")).read().strip()
                return {"has": True, "pct": pct, "ac": stt != "Discharging"}
    except Exception: pass
    return {"has": False, "ac": True}
AWAKE = {"on": False, "proc": None, "thread": None}
def keep_awake(on):
    if on == AWAKE["on"]: return
    AWAKE["on"] = on
    if os.name == "nt":
        import ctypes
        def run():
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x00000001 | 0x00000040)   # CONTINUOUS · SYSTEM_REQUIRED · AWAYMODE
            while AWAKE["on"]: time.sleep(5)
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
        if on: AWAKE["thread"] = threading.Thread(target=run, daemon=True); AWAKE["thread"].start()
    else:
        if on:
            cmd = ["caffeinate", "-s", "-i"] if sys.platform == "darwin" else (["systemd-inhibit", "--what=sleep:idle", "--why=Hojas Studio", "sleep", "infinity"] if shutil.which("systemd-inhibit") else None)
            if cmd and shutil.which(cmd[0]): AWAKE["proc"] = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif AWAKE["proc"]:
            try: AWAKE["proc"].kill()
            except Exception: pass
            AWAKE["proc"] = None
def screen_off():
    if os.name == "nt":
        import ctypes; ctypes.windll.user32.PostMessageW(0xFFFF, 0x0112, 0xF170, 2); return True
    if sys.platform == "darwin": subprocess.run(["pmset", "displaysleepnow"]); return True
    if shutil.which("xset"): subprocess.run(["xset", "dpms", "force", "off"]); return True
    return False
def tailscale_url():
    ts = shutil.which("tailscale") or (r"C:\Program Files\Tailscale\tailscale.exe" if os.name == "nt" and os.path.exists(r"C:\Program Files\Tailscale\tailscale.exe") else None)
    if not ts: return None, None
    try:
        d = json.loads(subprocess.run([ts, "status", "--json"], capture_output=True, text=True, timeout=6).stdout or "{}"); dn = ((d.get("Self") or {}).get("DNSName") or "").rstrip(".")
        return ts, ("https://" + dn + "/") if dn else None
    except Exception: return ts, None
def proj_start(work, engine=None):
    p = proj_port(work, True)
    if p: return p
    eng = find_engine(engine) or sys.exit("ما لقيت المحرّك"); use = next((p for p in range(HUB_PORT + 1, HUB_PORT + 40) if port_free(p)), None)
    if not use: raise RuntimeError("ما لقيت بورت فاضي")
    os.makedirs(J(work, ".hs"), exist_ok=True); lg = open(J(work, ".hs", "server.log"), "ab"); kw = {"stdin": subprocess.DEVNULL, "stdout": lg, "stderr": lg, "cwd": work}
    if os.name == "nt": kw["creationflags"] = 0x00000008 | 0x00000200 | 0x08000000
    else: kw["start_new_session"] = True
    subprocess.Popen([PY, os.path.abspath(__file__), "serve", work, "--port", str(use), "--engine", eng], **kw)
    for _ in range(80):
        if port_alive(use, work): _PM["t"] = 0; return use
        time.sleep(0.25)
    raise RuntimeError("الخادم ما اشتغل: " + J(work, ".hs", "server.log"))
# ───────────────────────── 4.4: بلقن Claude Code والتحديث التلقائي ─────────────────────────
UI_FONT = "nt-panorama-naskh-long.otf"
def ui_font():
    for d in (os.path.join(HERE, "fonts"), os.path.join(HOME_CFG, "fonts")):
        f = os.path.join(d, UI_FONT)
        if os.path.isfile(f): return f
    return os.path.join(HERE, "fonts", UI_FONT)
def current_path(): return os.path.join(HOME_CFG, "current.json")
LAUNCHER = """# Hojas Studio: يشغّل أحدث نسخة مركّبة (يكتبه hs sync، لا تعدّله)
import json, os, sys, glob, subprocess
H = os.path.join(os.path.expanduser("~"), ".hojas-studio")
def pick():
    try:
        r = json.load(open(os.path.join(H, "current.json"), encoding="utf-8")).get("root")
        if r and os.path.isfile(os.path.join(r, "hs.py")): return os.path.join(r, "hs.py")
    except Exception: pass
    c = glob.glob(os.path.join(os.path.expanduser("~"), ".claude", "plugins", "cache", "*", "hojas-studio", "*", "hs.py"))
    c += [os.path.join(os.path.expanduser("~"), d, "hs.py") for d in (os.path.join(".claude", "skills", "hojas-studio"), os.path.join("Documents", "hojas-studio"))]
    c = [x for x in c if os.path.isfile(x)]
    return max(c, key=os.path.getmtime) if c else None
hs = pick()
if not hs: sys.exit("Hojas Studio files not found")
sys.exit(subprocess.call([sys.executable, hs] + sys.argv[1:]))
"""
def launcher_path(): return os.path.join(HOME_CFG, "launch.py")
def hub_ping(port=None):
    port = port or hub_cfg().get("port") or HUB_PORT
    try:
        with urllib.request.urlopen("http://127.0.0.1:%d/hub/api/ping" % port, timeout=1.5) as r: return json.loads(r.read().decode())
    except Exception: return None
def hub_busy(port):
    try:
        with urllib.request.urlopen("http://127.0.0.1:%d/hub/api/device" % port, timeout=8) as r: d = json.loads(r.read().decode())
        return any(x.get("job") or x.get("agent") for x in d.get("live") or [])
    except Exception: return False
def deps_dir(): return os.path.join(HOME_CFG, "node_modules")
def deps_ok():
    e = find_engine(None)
    return bool((e and os.path.isdir(os.path.join(e, "node_modules", "puppeteer-core"))) or os.path.isdir(os.path.join(deps_dir(), "puppeteer-core")))
def deps_keep():
    """لو التصدير يحتاج puppeteer-core والنسخة الحالية (البلقن) ما فيها: ننسخه مرة من نسخة ثانية على نفس الجهاز (مجلد التطوير أو بلقن أقدم) لـ ~/.hojas-studio. بدون إنترنت."""
    if os.path.isdir(os.path.join(deps_dir(), "puppeteer-core")): return True
    e = find_engine(None); cands = ([os.path.join(e, "node_modules")] if e else []) + [os.path.join(os.path.expanduser("~"), "Documents", "hojas-studio", "engine", "node_modules")] + glob.glob(os.path.join(os.path.expanduser("~"), ".claude", "plugins", "cache", "*", "hojas-studio", "*", "engine", "node_modules"))
    for c in cands:
        if os.path.isdir(os.path.join(c, "puppeteer-core")):
            shutil.copytree(c, deps_dir(), dirs_exist_ok=True); return True
    return False
def cmd_deps(args):
    """hs deps: يثبّت puppeteer-core (يتحكم بكروم وقت التصدير) مرة وحدة بـ ~/.hojas-studio. لا تشغّله إلا بموافقة المستخدم."""
    if deps_keep(): print("مكتبة التصدير جاهزة: " + deps_dir()); return
    npm = shutil.which("npm") or shutil.which("npm.cmd")
    if not npm: sys.exit("ما لقيت npm: ثبّت Node.js من nodejs.org أول")
    os.makedirs(HOME_CFG, exist_ok=True)
    r = subprocess.run([npm, "install", "--prefix", HOME_CFG, "puppeteer-core@25", "--no-audit", "--no-fund", "--loglevel=error"])
    print("مكتبة التصدير جاهزة" if deps_ok() else "ما انثبّتت (رمز %s): جرّب يدوياً: npm install --prefix \"%s\" puppeteer-core" % (r.returncode, HOME_CFG))
def cmd_sync(args):
    """يشتغل مع بداية كل جلسة Claude Code (من البلقن): يسجّل أحدث نسخة، ولو المكتبة شغّالة بنسخة أقدم يعيد تشغيلها من الجديدة."""
    os.makedirs(HOME_CFG, exist_ok=True)
    cur = rj(current_path(), {}) or {}; changed = cur.get("version") != VERSION or os.path.normcase(cur.get("root") or "") != os.path.normcase(HERE)
    wj(current_path(), {"root": HERE, "version": VERSION, "at": int(time.time()), "plugin": bool(os.environ.get("CLAUDE_PLUGIN_ROOT"))})
    try:
        if not os.path.isfile(launcher_path()) or open(launcher_path(), encoding="utf-8").read() != LAUNCHER: open(launcher_path(), "w", encoding="utf-8").write(LAUNCHER)
    except Exception: pass
    fd = os.path.join(HOME_CFG, "fonts")   # خط الواجهة الخاص ما ينرفق بالنسخة العامة: نحفظه مرة من التثبيت القديم
    if not os.path.isfile(os.path.join(HERE, "fonts", UI_FONT)) and not os.path.isfile(os.path.join(fd, UI_FONT)):
        for d in (os.path.join(os.path.expanduser("~"), "Documents", "hojas-studio", "fonts"), os.path.join(os.path.expanduser("~"), ".claude", "skills", "hojas-studio", "fonts")):
            if os.path.isfile(os.path.join(d, UI_FONT)):
                os.makedirs(fd, exist_ok=True); shutil.copy2(os.path.join(d, UI_FONT), os.path.join(fd, UI_FONT)); break
    find_engine(None) and remember_engine(find_engine(None))
    try: deps_keep()   # 4.31: مكتبة التحكم بكروم تنحفظ برّا البلقن عشان التصدير ما يوقف بعد التحديث
    except Exception: pass
    if changed and cur.get("version"):   # 4.31: نسخة احتياطية من قائمة المشاريع قبل ما تتغيّر النسخة
        try: shutil.copy2(os.path.join(HOME_CFG, "projects.json"), os.path.join(HOME_CFG, "projects.json.bak-" + str(cur.get("version"))))
        except Exception: pass
    if "--now" not in args:
        try: claude_learn()   # 4.4.1: المكتبة تعرف وين Claude حتى لو اشتغلت مع ويندوز بدون PATH
        except Exception: pass
    port = hub_cfg().get("port") or HUB_PORT; pg = hub_ping(port)
    if pg and (pg.get("version") != VERSION or os.path.normcase(pg.get("root") or "") != os.path.normcase(HERE)):
        if "--now" not in args:   # لا نأخّر بداية الجلسة: نكمّل بالخلفية
            spawn_bg(["sync", "--now"], os.path.join(HOME_CFG, "sync.log"))
        elif hub_busy(port): print("المكتبة مشغولة بتصدير أو Claude، بتتحدّث بالجلسة الجاية")
        else:
            try: urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:%d/hub/api/restart" % port, data=json.dumps({"latest": True}).encode(), headers={"Content-Type": "application/json"}), timeout=5).read()
            except Exception: pass
            time.sleep(4); pg2 = hub_ping(port)
            if not pg2 or pg2.get("version") != VERSION or os.path.normcase(pg2.get("root") or "") != os.path.normcase(HERE):   # مكتبة قديمة ما تعرف «latest»
                if pg2:
                    try: urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:%d/hub/api/shutdown" % port, data=b"{}", headers={"Content-Type": "application/json"}), timeout=5).read()
                    except Exception: pass
                    time.sleep(2)
                if not hub_ping(port): spawn_bg(["hub", "--no-browser"], os.path.join(HOME_CFG, "hub.log")); time.sleep(4)
            pg3 = hub_ping(port)
            print("المكتبة انتقلت لنسخة " + VERSION if pg3 and pg3.get("version") == VERSION else "ما قدرت أنقل المكتبة للنسخة الجديدة، شغّل: hs hub --restart")
    if changed and "--now" not in args and cur.get("version"):
        print("Hojas Studio اتحدّث من %s إلى %s. الجديد في %s" % (cur.get("version"), VERSION, os.path.join(HERE, "CHANGELOG.md")))
def cmd_autoupdate(args):
    """hs autoupdate on|off: يشغّل التحديث التلقائي لبلقن Hojas في إعدادات Claude Code (~/.claude/settings.json)."""
    on = (args[0] if args else "on") != "off"; sp = os.path.join(os.path.expanduser("~"), ".claude", "settings.json")
    st = rj(sp, {}) or {}; ek = st.setdefault("extraKnownMarketplaces", {})
    e = ek.setdefault("hojas", {"source": {"source": "github", "repo": "rakaga66/hojas-studio"}}); e["autoUpdate"] = on
    os.makedirs(os.path.dirname(sp), exist_ok=True)
    if os.path.exists(sp): shutil.copy2(sp, sp + ".bak-hojas")
    wj(sp, st); print(("شغّلت" if on else "طفّيت") + " التحديث التلقائي لـ Hojas Studio في " + sp + " (نسخة احتياطية: settings.json.bak-hojas)")
def plugin_skill_text():
    """نسخة SKILL.md للبلقن (skills/hojas-studio/SKILL.md): نفس السكل مع مسار البلقن."""
    src = open(os.path.join(HERE, "SKILL.md"), encoding="utf-8").read(); fm, body = src.split("\n---\n", 1)
    body = body.replace("تحت: `hs` = `python <skill>/hs.py`.", "تحت: `hs` أمر جاهز بالطرفية من البلقن (ولو ما اشتغل: `python \"${CLAUDE_PLUGIN_ROOT}/hs.py\"`).", 1)
    note = ("\n> **مثبّت كبلقن Claude Code:** مجلد السكل `<skill>` = `${CLAUDE_PLUGIN_ROOT}`، والمحرّك `${CLAUDE_PLUGIN_ROOT}/engine`. "
            "`hs` أمر جاهز. التحديث تلقائي من البلقن، فلا تستخدم `hs update`. مشاريعه وإعداداته وقاعدة بياناته في `~/.hojas-studio` وما تتأثر بالتحديث.\n")
    return fm + "\n---\n" + note + body
def cmd_release(args):
    """hs release: يجهّز البلقن قبل الرفع (نسخة SKILL.md للبلقن + رقم النسخة من VERSION)."""
    sk = os.path.join(HERE, "skills", "hojas-studio", "SKILL.md"); os.makedirs(os.path.dirname(sk), exist_ok=True)
    try:   # 4.33: عنوان السكل ياخذ رقم النسخة لحاله
        rp = os.path.join(HERE, "SKILL.md"); tx = open(rp, encoding="utf-8").read(); tx2 = re.sub(r"(?m)^# Hojas Studio [0-9.]+:", "# Hojas Studio %s:" % VERSION, tx, count=1)
        if tx2 != tx: open(rp, "w", encoding="utf-8", newline="").write(tx2)
    except Exception: pass
    open(sk, "w", encoding="utf-8").write(plugin_skill_text())
    pj = os.path.join(HERE, ".claude-plugin", "plugin.json"); d = rj(pj, {}) or {}; d["version"] = VERSION; wj(pj, d)
    print("البلقن جاهز: %s · النسخة %s" % (sk, VERSION))
def cmd_hub(args):
    """hs hub [--root <مجلد المشاريع>] [--port 8800] [--no-browser] [--tailscale] [--restart] [--cookies chrome|off] [--autostart [off]]"""
    rest = list(args)
    def o(nm, d=None):
        if nm in rest: i = rest.index(nm); v = rest[i + 1]; del rest[i:i + 2]; return v
        return d
    cfg = hub_cfg(); root = os.path.abspath(o("--root") or cfg.get("root") or os.path.join(os.path.expanduser("~"), "Documents", "hojas-studio-projects"))
    port = int(o("--port", cfg.get("port") or HUB_PORT)); os.makedirs(root, exist_ok=True); cfg.update(root=root, port=port)
    cm = o("--cpu")
    if cm in CPU_MODES: cfg["cpu"] = cm; os.makedirs(HOME_CFG, exist_ok=True); wj(hub_cfg_path(), cfg); print("وضع الجهاز: " + ("خفيف" if cm == "light" else "أقصى سرعة") + " (يطبّق على الشغل الجديد)"); lighten(cm)
    ck = o("--cookies")
    if ck: cfg["cookies"] = None if ck == "off" else ck; print("السحب بيستخدم دخولك من متصفح: " + ck if ck != "off" else "انطفى استخدام دخول المتصفح"); os.makedirs(HOME_CFG, exist_ok=True); wj(hub_cfg_path(), cfg)
    if "--serve" in rest: return hub_serve(root, port)
    if "--autostart" in rest:
        i = rest.index("--autostart"); off = len(rest) > i + 1 and rest[i + 1] == "off"
        if os.name != "nt": sys.exit("التشغيل التلقائي مجهّز لويندوز. بالماك: أضف الأمر لـ Login Items")
        sd = os.path.join(os.environ.get("APPDATA", ""), "Microsoft", "Windows", "Start Menu", "Programs", "Startup"); vb = os.path.join(sd, "Hojas Library.vbs")
        if off:
            if os.path.exists(vb): os.remove(vb)
            print("انطفى التشغيل التلقائي للمكتبة."); return
        pyw = PY[:-10] + "pythonw.exe" if PY.lower().endswith("python.exe") and os.path.exists(PY[:-10] + "pythonw.exe") else PY
        cmd_sync(["--quiet"]) if not os.path.isfile(launcher_path()) else None
        open(vb, "w", encoding="utf-8").write('CreateObject("WScript.Shell").Run """%s"" ""%s"" hub --no-browser", 0, False\r\n' % (pyw, launcher_path() if os.path.isfile(launcher_path()) else os.path.abspath(__file__)))
        print("المكتبة بتشتغل لحالها كل ما يشتغل الجهاز (بدون نافذة). للإطفاء: python hs.py hub --autostart off"); return
    alive = False
    try:
        with urllib.request.urlopen("http://127.0.0.1:%d/hub/api/ping" % port, timeout=1.2) as r: alive = b"hub" in r.read()
    except Exception: pass
    if alive and "--restart" in rest:   # 4.4: يقفل المكتبة القديمة ويشغّل نسخة الملفات الجديدة
        try: urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:%d/hub/api/restart" % port, data=b"{}", headers={"Content-Type": "application/json"}), timeout=5).read()
        except Exception: pass
        print("أعيد تشغيل المكتبة…", flush=True); time.sleep(2.5); alive = False
        for _ in range(40):
            try:
                with urllib.request.urlopen("http://127.0.0.1:%d/hub/api/ping" % port, timeout=1) as r:
                    if b"hub" in r.read(): alive = True; break
            except Exception: time.sleep(0.5)
    if not alive:
        lg = open(os.path.join(HOME_CFG, "hub.log"), "ab"); kw = {"stdin": subprocess.DEVNULL, "stdout": lg, "stderr": lg, "cwd": root}
        if os.name == "nt": kw["creationflags"] = 0x00000008 | 0x00000200 | 0x08000000
        else: kw["start_new_session"] = True
        subprocess.Popen([PY, os.path.abspath(__file__), "hub", "--serve", "--root", root, "--port", str(port)], **kw)
        for _ in range(60):
            try:
                with urllib.request.urlopen("http://127.0.0.1:%d/hub/api/ping" % port, timeout=1) as r:
                    if b"hub" in r.read(): alive = True; break
            except Exception: time.sleep(0.25)
        if not alive: sys.exit("المكتبة ما اشتغلت: " + os.path.join(HOME_CFG, "hub.log"))
    url = "http://127.0.0.1:%d/library" % port
    if "--tailscale" in rest:
        ts, tu = tailscale_url()
        if not ts: print("Tailscale مو مثبّت. ثبّته من tailscale.com وسجّل بنفس حساب جوالك، ثم أعد الأمر.")
        else:
            r = subprocess.run([ts, "serve", "--bg", "http://127.0.0.1:%d" % port], capture_output=True, text=True, timeout=30)
            if r.returncode != 0: print("Tailscale رفض: " + (r.stderr or r.stdout).strip()[:300] + "\nفعّل HTTPS من لوحة Tailscale (DNS ← HTTPS Certificates) ثم أعد الأمر.")
            elif tu: print("رابط آمن للجوال (المايك يشتغل فيه): " + tu + "library"); cfg["ts"] = tu; wj(hub_cfg_path(), cfg)
    if "--no-browser" not in rest:
        try:
            import webbrowser; webbrowser.open(url)
        except Exception: pass
    tok = open(os.path.join(HOME_CFG, "hub-token")).read().strip() if os.path.exists(os.path.join(HOME_CFG, "hub-token")) else ""
    print("المكتبة شغّالة: " + url); print("على الجوال: http://%s:%d/library?k=%s" % (lan_ip(), port, tok) + ((" · أو الرابط الآمن: " + cfg["ts"] + "library") if cfg.get("ts") else ""))
def lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(("8.8.8.8", 80)); ip = s.getsockname()[0]; s.close(); return ip
    except Exception: return "127.0.0.1"
def hub_serve(root, port):
    import http.server, http.client
    tp = os.path.join(HOME_CFG, "hub-token")
    if not os.path.exists(tp): open(tp, "w").write("%06d" % secrets.randbelow(10 ** 6))
    TOKEN = open(tp).read().strip(); FAILS = {}; FAILS_ALL = [0]; POOL = threading.local(); LAN = lan_ip()
    STATE = {"started": time.time()}
    def conn(p):
        d = getattr(POOL, "c", None)
        if d is None: d = POOL.c = {}
        c = d.get(p)
        if c is None: c = d[p] = http.client.HTTPConnection("127.0.0.1", p, timeout=120)
        return c
    def card_by(pid):
        for w in hub_projects(root):
            if hashlib.md5(os.path.normcase(w).encode()).hexdigest()[:10] == pid: return w
        for e in hub_eps(root):
            if e["id"] == pid: return e["work"]
        return None
    def new_dir(name, prefix):
        base = re.sub(r"[^\w\-]+", "-", name or "").strip("-")[:40] or prefix + time.strftime("%m%d-%H%M"); w = os.path.join(root, base); k = 1
        while os.path.exists(w): w = os.path.join(root, "%s-%d" % (base, k)); k += 1
        return w
    def grab_bg(src, w, data):
        os.makedirs(J(w, ".hs"), exist_ok=True); mode = data.get("mode") or "auto"; style = ""
        if mode == "motion": mode, style = "auto", "motion"   # 4.37: موشن جرافيك = Claude يمنتجه والموشن أساسي
        if mode not in ("auto", "manual", "clips"): mode = "auto"
        job_set(w, stage="grab", pct=0, mode=mode, src=src, done=False, err=None, t0=int(time.time()))
        args = ["grab", src, "--into", w, "--mode", mode, "--pick", data.get("pick") or "claude", "--n", str(int(data.get("n") or 5))]
        if data.get("len"): args += ["--len", str(data["len"])]
        if data.get("note"): args += ["--note", str(data["note"])[:1500]]
        if data.get("lang"): args += ["--lang", str(data["lang"])]
        if style: args += ["--style", style]
        if data.get("identity"): args += ["--identity", str(data["identity"])[:40]]
        spawn_bg(args, J(w, ".hs", "job.log")); projects_remember(w) if mode != "clips" else None
    class HB(http.server.BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"; timeout = 75
        def log_message(self, *a): pass
        def _local(self): return self.client_address[0] in ("127.0.0.1", "::1", "localhost")
        def _q(self): return urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        def _ok(self):
            if self._local(): return True
            ip = self.client_address[0]; now = time.time(); f = FAILS.get(ip)
            if f and now - f[1] > 900: FAILS.pop(ip, None); f = None
            if FAILS_ALL[0] >= 200 or (f and f[0] >= 10): return False
            ck = self.headers.get("Cookie") or ""; q = self._q()
            if ("hs_k=" + TOKEN) in ck or (q.get("k") or [""])[0] == TOKEN: return True
            if q.get("k") or "hs_k=" in ck: FAILS[ip] = [(f[0] if f else 0) + 1, f[1] if f else now]; FAILS_ALL[0] += 1
            return False
        def _send(self, code, body, ctype="application/json; charset=utf-8", extra=None):
            b = body if isinstance(body, bytes) else body.encode("utf-8"); self.send_response(code); self.send_header("Content-Type", ctype); self.send_header("Content-Length", str(len(b)))
            if "Cache-Control" not in (extra or {}): self.send_header("Cache-Control", "no-store")
            for k, v in (extra or {}).items(): self.send_header(k, v)
            self.end_headers(); self.wfile.write(b)
        def _json(self, code, o, extra=None): self._send(code, json.dumps(o, ensure_ascii=False), extra=extra)
        def _deny(self):
            ip = self.client_address[0]; f = FAILS.get(ip); q = self._q()
            locked = FAILS_ALL[0] >= 200 or bool(f and f[0] >= 10 and time.time() - f[1] <= 900)
            pth = urllib.parse.urlparse(self.path).path
            self._send(403, login_html(pth if pth in ("/tele", "/library") else "/library", "بالمكتبة على الكمبيوتر", len(TOKEN), "الرمز غلط، جرّب مرة ثانية." if q.get("k") else "", locked), "text/html; charset=utf-8")
        def _body(self):
            n = int(self.headers.get("Content-Length") or 0); return self.rfile.read(n) if n else b""
        def _cookie(self, name):
            m = re.search(r"(?:^|;\s*)" + name + r"=([^;]*)", self.headers.get("Cookie") or ""); return m.group(1) if m else None
        def _proxy(self, port):
            body = self._body() if self.command in ("POST", "PUT") else None
            hd = {k: v for k, v in self.headers.items() if k.lower() not in ("host", "connection", "keep-alive", "proxy-connection", "te", "trailer", "upgrade", "cookie")}
            hd["Host"] = "127.0.0.1:%d" % port
            for attempt in (0, 1):
                c = conn(port)
                try: c.request(self.command, self.path, body=body, headers=hd); r = c.getresponse(); break
                except Exception:
                    try: c.close()
                    except Exception: pass
                    POOL.c.pop(port, None)
                    if attempt: return self._send(502, stopped_html(), "text/html; charset=utf-8")
            self.send_response(r.status); ln = r.getheader("Content-Length")
            for k, v in r.getheaders():
                if k.lower() in ("connection", "keep-alive", "transfer-encoding", "content-length"): continue
                self.send_header(k, v)
            if ln is not None: self.send_header("Content-Length", ln)
            else: self.send_header("Connection", "close"); self.close_connection = True
            self.end_headers()
            while True:
                ch = r.read(65536)
                if not ch: break
                try: self.wfile.write(ch)
                except Exception: r.close(); POOL.c.pop(port, None); return
            if ln is None or r.will_close:
                try: c.close()
                except Exception: pass
                POOL.c.pop(port, None)
        def _route(self):
            u = urllib.parse.urlparse(self.path); p = u.path; q = self._q()
            if p == "/hub/api/ping": return self._json(200, {"hub": True, "version": VERSION, "root": HERE})
            if not self._ok(): return self._deny()
            if (q.get("k") or [""])[0] == TOKEN and not self._local() and ("hs_k=" + TOKEN) not in (self.headers.get("Cookie") or ""):
                self.send_response(302); self.send_header("Set-Cookie", "hs_k=%s; Path=/; Max-Age=2592000; SameSite=Lax" % TOKEN); self.send_header("Location", p or "/library"); self.send_header("Content-Length", "0"); self.end_headers(); return
            if p in ("/tele", "/tele/"):   # 4.5.2: الملقّن قريباً (tele.html موجود للتطوير وما ينفتح للحين)
                b = login_html("/library", "", 6).split("<body>")[0] + "<body><div class=c><div class=logo><svg viewBox='0 0 260 260' aria-hidden=true><rect width=150.5 height=46.8 fill=currentColor /><rect x=62.5 y=106.6 width=197.5 height=46.8 fill=currentColor /><rect y=213.2 width=103.7 height=46.8 fill=currentColor /></svg></div><h1>الملقّن قريباً</h1><p>جاي بالتحديث الجاي.</p><a href=/library class=lk>ارجع للمكتبة</a></div></body></html>"
                return self._send(200, b.replace("%%", "%"), "text/html; charset=utf-8")
            if p in ("/library", "/library/"):
                b = open(os.path.join(HERE, "hub.html"), "rb").read(); return self._send(200, b, "text/html; charset=utf-8", {"Set-Cookie": "hs_hub=1; Path=/; SameSite=Lax"})
            if p == "/hub/ui-font.otf":
                f = ui_font()
                return self._send(200, open(f, "rb").read(), "font/otf", {"Cache-Control": "max-age=604800"}) if os.path.isfile(f) else self._send(404, b"")
            if p == "/hub/qr.js": return self._send(200, open(os.path.join(HERE, "qr.js"), "rb").read(), "application/javascript; charset=utf-8", {"Cache-Control": "max-age=86400"})
            if p.startswith("/hub/api/"): return self._api(p[9:], q)
            if p in ("/hub/manifest.json", "/manifest.json"):
                return self._send(200, json.dumps({"name": "Hojas Studio", "short_name": "Hojas", "start_url": "/library", "display": "standalone", "background_color": "#0a0c11", "theme_color": "#0a0c11", "dir": "rtl", "lang": "ar",
                                                   "icons": [{"src": "/hub/icon.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}]}, ensure_ascii=False), "application/manifest+json")
            if p == "/hub/icon.png":
                f = os.path.join(HERE, "hub-icon.png")
                return self._send(200, open(f, "rb").read(), "image/png", {"Cache-Control": "max-age=86400"}) if os.path.isfile(f) else self._send(404, b"")
            if p.startswith("/hub/video/"):
                w = card_by(p.split("/")[3]); f = q.get("f", [""])[0]
                if not w or not f or ".." in f or not f.endswith(".mp4"): return self._send(404, b"")
                fp = J(w, f)
                if not os.path.isfile(fp): return self._send(404, b"")
                size = os.path.getsize(fp); rg = re.match(r"bytes=(\d*)-(\d*)", self.headers.get("Range") or ""); a, b = 0, size - 1
                if rg:
                    if rg.group(1): a = int(rg.group(1))
                    if rg.group(2): b = min(size - 1, int(rg.group(2)))
                    if not rg.group(1) and rg.group(2): a, b = max(0, size - int(rg.group(2))), size - 1
                self.send_response(206 if rg else 200); self.send_header("Content-Type", "video/mp4"); self.send_header("Accept-Ranges", "bytes"); self.send_header("Content-Length", str(b - a + 1))
                if rg: self.send_header("Content-Range", "bytes %d-%d/%d" % (a, b, size))
                self.end_headers()
                with open(fp, "rb") as fh:
                    fh.seek(a); left = b - a + 1
                    while left > 0:
                        ch = fh.read(min(1 << 20, left))
                        if not ch: break
                        self.wfile.write(ch); left -= len(ch)
                return
            if p.startswith("/hub/thumb/"):
                w = card_by(p.split("/")[3]); f = q.get("f", [""])[0]
                if not w or not f or ".." in f: return self._send(404, b"")
                fp = J(w, f)
                if not os.path.isfile(fp): return self._send(404, b"")
                sm = J(w, ".hs", "hub-th-" + hashlib.md5(f.encode()).hexdigest()[:8] + ".jpg")   # 4.4: صورة مصغّرة (20 كيلو بدل 250)
                try:
                    if not os.path.isfile(sm) or os.path.getmtime(sm) < os.path.getmtime(fp):
                        os.makedirs(J(w, ".hs"), exist_ok=True)
                        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", fp, "-vf", "scale=360:-2", "-q:v", "5", sm], capture_output=True, timeout=20)
                    if os.path.isfile(sm) and os.path.getsize(sm) > 0: fp = sm
                except Exception: pass
                return self._send(200, open(fp, "rb").read(), "image/jpeg", {"Cache-Control": "max-age=86400"})
            pp = self._cookie("hs_p")
            if pp and pp.isdigit(): return self._proxy(int(pp))
            self.send_response(302); self.send_header("Location", "/library"); self.send_header("Content-Length", "0"); self.end_headers()
        def do_GET(self):
            try: self._route()
            except (BrokenPipeError, ConnectionResetError): pass
        def do_HEAD(self): self.do_GET()
        def do_POST(self):
            try: self._route()
            except (BrokenPipeError, ConnectionResetError): pass
        def _api(self, a, q):
            if self.command == "POST" and a not in ("upload", "identity_file"):
                try: data = json.loads(self._body() or b"{}")
                except Exception: data = {}
            else: data = {}
            if a == "projects":
                cards = [proj_card(w, live=True) for w in hub_projects(root)]; cards.sort(key=lambda c: -c["mt"])
                eps = hub_eps(root); eps.sort(key=lambda c: -c["mt"])
                return self._json(200, {"root": root, "projects": cards, "eps": eps, "awake": AWAKE["on"], "battery": battery(), "ytdlp": bool(ytdlp_cmd()), "claude": have_claude(), "claudeErr": claude_last_err(), "tokenAsk": token_ask(), "factory": factory_state()})
            if a == "search":
                qq = (q.get("q") or [""])[0].strip()
                if len(qq) < 2: return self._json(200, {"q": qq, "items": []})
                try: R = db_search(qq, 40, (q.get("kind") or [None])[0] or None)
                except Exception as e: return self._json(500, {"ok": False, "msg": str(e)[:200]})
                for g in R["items"]:
                    w = g["work"]; g["thumb"] = None
                    if g["kind"] == "ep": g["thumb"] = ".hs/th.jpg" if os.path.exists(J(w, ".hs", "th.jpg")) else None
                    else:
                        for f in ("vfr/00045.jpg", "vfr/00001.jpg", ".hs/th/2.jpg"):
                            if os.path.exists(J(w, f)): g["thumb"] = f; break
                    g["mt"] = int(os.path.getmtime(w)) if os.path.exists(w) else 0
                return self._json(200, R)
            if a == "db":
                if self.command == "POST": threading.Thread(target=lambda: db_sync(root, bool(data.get("full"))), daemon=True).start()
                try: return self._json(200, db_stats())
                except Exception as e: return self._json(200, {"items": 0, "err": str(e)[:200]})
            if a == "link":
                url = str(data.get("url") or "").strip()
                m = re.search(r"https?://\S+", url)
                if not m: return self._json(400, {"ok": False, "msg": "الصق رابط يبدأ بـ https://"})
                if not ytdlp_cmd(): return self._json(200, {"ok": False, "need": "ytdlp", "msg": "أداة السحب yt-dlp مو مثبّتة"})
                w = new_dir(data.get("name"), "long-" if data.get("mode") == "clips" else "clip-"); pod_want(w, data); grab_bg(m.group(0), w, data)
                return self._json(200, {"ok": True, "work": w})
            if a == "identity":   # 4.37: الهويات المحفوظة، وهوية جديدة من وصف وملفات
                if self.command == "POST":
                    if data.get("setDefault") is not None: ident_default(str(data.get("setDefault") or ""))
                    elif str(data.get("name") or "").strip() or str(data.get("text") or "").strip():
                        try: nm_ = str(data.get("name") or "").strip() or "هويتي"; ident_adopt(data.get("key"), nm_); I_ = ident_new(nm_, str(data.get("text") or ""), default=bool(data.get("default", True)))
                        except Exception as e: return self._json(400, {"ok": False, "msg": str(e)[:160]})
                        return self._json(200, {"ok": True, "slug": I_["slug"], "list": ident_list(), "default": ident_default()})
                return self._json(200, {"ok": True, "list": ident_list(), "default": ident_default()})
            if a == "identity_file":
                try: rel = ident_add_file((q.get("name") or ["هويتي"])[0] or "هويتي", (q.get("file") or ["file"])[0], self._body())
                except ValueError as e: return self._json(400, {"ok": False, "msg": str(e)})
                return self._json(200, {"ok": True, "file": rel})
            if a == "tokens":   # 4.5: اسألني قبل أي شي يستهلك من حدّي في Claude
                c = hub_cfg(); c["tokenAsk"] = bool(data.get("ask", True)); wj(hub_cfg_path(), c); return self._json(200, {"ok": True, "tokenAsk": token_ask()})
            if a == "insights":
                c = perf_conn()
                try: last = (c.execute("SELECT MAX(at) FROM perf").fetchone() or [None])[0]; srcs = [r[0] for r in c.execute("SELECT DISTINCT src FROM perf").fetchall()]
                finally: c.close()
                return self._json(200, {**insights(), "learned": learned(), "last": last, "srcs": srcs, "perf": {k: {"views": v.get("views"), "likes": v.get("likes")} for k, v in perf_all().items()}})
            if a == "perf":
                w = card_by((q.get("id") or [data.get("id") or ""])[0])
                if not w: return self._json(404, {"ok": False})
                if self.command == "POST": perf_set(item_id(w), str(data.get("plat") or "all")[:20], **{k: data.get(k) for k in ("views", "likes", "comments", "shares", "saves", "watch", "ret", "posted", "url")})
                return self._json(200, {"ok": True, "rows": perf_get(item_id(w))})
            if a == "perf_import": return self._json(200, perf_import(str(data.get("text") or ""), str(data.get("plat") or ""), str(data.get("name") or "")))
            if a == "factory":
                if self.command == "POST":
                    if data.get("open"):
                        fd = factory_cfg()["dir"]; os.makedirs(fd, exist_ok=True)
                        if self._local():
                            try:
                                if os.name == "nt": os.startfile(fd)
                                else: subprocess.Popen(["open" if sys.platform == "darwin" else "xdg-open", fd])
                            except Exception: pass
                    elif data.get("now"): FAC["force"] = True; factory_tick()
                    else:
                        c = hub_cfg(); f = c.get("factory") or {}
                        for k in ("on", "night"):
                            if k in data: f[k] = bool(data[k])
                        if data.get("mode") in ("manual", "auto"): f["mode"] = data["mode"]
                        if data.get("dir"): f["dir"] = os.path.abspath(os.path.expanduser(str(data["dir"])))
                        c["factory"] = f; wj(hub_cfg_path(), c)
                        if f.get("on"): os.makedirs(factory_cfg()["dir"], exist_ok=True)
                return self._json(200, factory_state())
            if a == "scripts": return self._json(200, {"items": rj(scripts_path(), []) or [], "claude": have_claude(), "tokenAsk": token_ask()})
            if a == "script_save":
                L = rj(scripts_path(), []) or []; sid = str(data.get("id") or "") or "s%d" % int(time.time() * 1000)
                it = next((x for x in L if x["id"] == sid), None) or {"id": sid}
                if it not in L: L.insert(0, it)
                it.update(title=str(data.get("title") or "")[:120], text=str(data.get("text") or "")[:20000], at=int(time.time())); wj(scripts_path(), L[:200]); return self._json(200, {"ok": True, "id": sid, "items": L})
            if a == "script_del":
                L = [x for x in rj(scripts_path(), []) or [] if x["id"] != data.get("id")]; wj(scripts_path(), L); return self._json(200, {"ok": True, "items": L})
            if a == "script_ai":   # اختياري ويستهلك: Claude يكتب السكربت
                v = find_claude()
                if not v: return self._json(200, {"ok": False, "msg": "ما لقيت Claude Code على الجهاز"})
                topic = str(data.get("topic") or "")[:800]; secs = int(data.get("secs") or 45)
                pr = ("اكتب سكربت مقطع قصير (talking head) بلهجة سعودية بيضاء عن: %s. مدته تقريباً %d ثانية (حوالي %d كلمة). أول جملة هوك قوي (سؤال أو رقم أو جملة صادمة)، "
                      "جمل قصيرة سهلة تنقال، وآخر جملة تطلب شي (تابع أو احفظ). اكتب السكربت فقط بدون عناوين أو شرح." % (topic, secs, int(secs * 2.3)))
                cmd = (["cmd", "/c"] if v.lower().endswith((".cmd", ".bat")) else []) + [v, "-p", pr]
                kw = {"creationflags": 0x08000000} if os.name == "nt" else {}
                try: r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180, stdin=subprocess.DEVNULL, cwd=HOME_CFG, **kw)
                except subprocess.TimeoutExpired: return self._json(200, {"ok": False, "msg": "Claude ما رد خلال 3 دقايق"})
                out = (r.stdout or "").strip()
                if r.returncode != 0 or not out or claude_why(out)["why"] in ("limit", "login", "credit"): return self._json(200, {"ok": False, "msg": claude_why(out + (r.stderr or ""), r.returncode)["msg"]})
                return self._json(200, {"ok": True, "text": out})
            if a == "cpu":   # 4.4.1: خفيف على الجهاز / أقصى سرعة
                m = data.get("mode")
                if data.get("probe"): whisper_device()
                if m in CPU_MODES: c = hub_cfg(); c["cpu"] = m; wj(hub_cfg_path(), c); lighten(m)
                return self._json(200, {"ok": True, "cpu": cpu_mode(), "whisper": whisper_device()})
            if a == "claude_check":   # 4.4.1: «دوّر مرة ثانية» و«جرّب Claude»
                v = find_claude(True)
                if not v or not data.get("test"): return self._json(200, {"ok": bool(v), "path": v or "", "msg": "" if v else "ما لقيت Claude Code. افتح Claude Code مرة وحدة وأرجع اضغط «دوّر»، أو ثبّته من claude.com/claude-code"})
                cmd = (["cmd", "/c"] if v.lower().endswith((".cmd", ".bat")) else []) + [v, "-p", "Reply with the single word: ok"]
                kw = {"creationflags": 0x08000000} if os.name == "nt" else {}
                try: r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=90, stdin=subprocess.DEVNULL, cwd=HOME_CFG, **kw); out = (r.stdout or "") + (r.stderr or ""); rc = r.returncode
                except subprocess.TimeoutExpired: out, rc = "timed out", -1
                good = rc == 0 and "ok" in out.lower() and claude_why(out)["why"] == "other"
                if good: cmd_log_clear_err()
                return self._json(200, {"ok": good, "path": v, "msg": "Claude شغّال ويرد." if good else claude_why(out, rc)["msg"]})
            if a == "ytdlp_install":
                r = subprocess.run([PY, "-m", "pip", "install", "-U", "yt-dlp"], capture_output=True, text=True, timeout=600)
                return self._json(200, {"ok": r.returncode == 0 and bool(ytdlp_cmd()), "out": (r.stdout + r.stderr)[-600:]})
            if a == "ep":
                w = card_by((q.get("id") or [""])[0])
                if not w or not is_ep(w): return self._json(404, {"ok": False, "msg": "ما لقيت الحلقة"})
                cfg = clips_cfg(w); A = rj(J(w, "long.json"), {}) or {}; made = []
                for c in cfg.get("clips") or []:
                    cw = J(w, c["name"]); made.append({**c, "pid": hashlib.md5(os.path.normcase(cw).encode()).hexdigest()[:10], "card": proj_card(cw) if is_project(cw) else None})
                return self._json(200, {"ok": True, "card": ep_card(w), "cands": cfg.get("cands") or [], "clips": made, "want": cfg.get("want") or {}, "lang": cfg.get("lang"),
                                        "segs": [[round(x["start"], 2), round(x["end"], 2), x["text"].strip()] for x in A.get("segments") or []],
                                        "preview": ".hs/preview.mp4" if os.path.exists(J(w, ".hs", "preview.mp4")) else None, "ranking": bool(job_get(w).get("ranking")), "claude": have_claude(),
                                        "remote": cfg.get("remote") if not (cfg.get("src") and os.path.isfile(cfg.get("src") or "")) else None, "vid": cfg.get("vid"), "host": host_cfg()})
            if a == "ep_build":
                w = card_by(data.get("id", ""))
                if not w or not is_ep(w): return self._json(404, {"ok": False})
                picks = [p for p in data.get("picks") or [] if isinstance(p, (str, dict))][:30]
                if not picks: return self._json(400, {"ok": False, "msg": "اختر لقطة وحدة على الأقل"})
                edit = data.get("edit") if data.get("edit") in ("me", "claude", "none") else "me"
                pf = J(w, ".hs", "picks.json"); wj(pf, picks); job_set(w, stage="build", err=None)
                pr = spawn_bg(["clips", "build", w, "--json", pf, "--edit", edit], J(w, ".hs", "job.log"))
                def fin(): rc = pr.wait(); job_set(w, stage=("claude" if edit == "claude" else "pick") if rc == 0 else "error", err=None if rc == 0 else "القص وقف: شوف .hs/job.log")
                threading.Thread(target=fin, daemon=True).start()
                return self._json(200, {"ok": True})
            if a == "ep_more":   # 4.26: «هات غيرها»: نفس العدد مرشّحات جديدة ما تتداخل مع اللي شفتها
                w = card_by(data.get("id", ""))
                if not w or not is_ep(w): return self._json(404, {"ok": False, "msg": "ما لقيت الحلقة"})
                cfg = clips_cfg(w); nn = int((cfg.get("want") or {}).get("n") or 5); ks = set(data.get("keep") or [])
                for c in cfg.get("cands") or []: c["keep"] = c.get("id") in ks or bool(c.get("keep"))   # اللي حددتها تبقى
                wj(J(w, "clips.json"), cfg); C = clips_suggest(w, nn, None, None, count=nn * 2, fresh=True)
                return self._json(200, {"ok": True, "cands": C, "added": sum(1 for c in C if c.get("by") == "auto" and not c.get("made"))})
            if a == "host":   # 4.26: شخصية المقدّم الثابتة
                if self.command == "POST": return self._json(200, {"ok": True, "host": host_set(name=str(data.get("name"))[:30] if data.get("name") is not None else None, char=data.get("char") if data.get("char") in ("robo", "sprout", "star", "cube") else None, color=data.get("color") if re.match(r"^#[0-9A-Fa-f]{6}$", str(data.get("color") or "")) else None, on=bool(data.get("on")) if "on" in data else None)})
                return self._json(200, {"ok": True, "host": host_cfg()})
            if a == "ep_suggest":
                w = card_by(data.get("id", ""))
                if not w or not is_ep(w): return self._json(404, {"ok": False})
                C = clips_suggest(w, int(data.get("n") or 0) or None, data.get("len"), data.get("note")); return self._json(200, {"ok": True, "cands": C})
            if a == "ep_cand":
                w = card_by(data.get("id", ""))
                if not w or not is_ep(w): return self._json(404, {"ok": False})
                cfg = clips_cfg(w); C = cfg.setdefault("cands", []); c = data.get("cand") or {}
                if c.get("rm"): cfg["cands"] = [x for x in C if x["id"] != c["rm"]]
                elif c.get("id") and any(x["id"] == c["id"] for x in C):
                    for x in C:
                        if x["id"] == c["id"]: x.update({k: c[k] for k in ("from", "to", "title") if k in c})
                else:
                    ids = [int(re.sub(r"\D", "", x["id"]) or 0) for x in C]
                    C.append({"id": "c%d" % (max(ids or [0]) + 1), "from": float(c["from"]), "to": float(c["to"]), "title": c.get("title", ""), "score": 0, "why": ["اختيارك"], "by": "me", "hook": c.get("hook", "")[:140]})
                wj(J(w, "clips.json"), cfg); return self._json(200, {"ok": True, "cands": cfg["cands"]})
            if a == "ep_rank":
                w = card_by(data.get("id", ""))
                if not w or not is_ep(w): return self._json(404, {"ok": False})
                note = (clips_cfg(w).get("want") or {}).get("note") or ""
                task = ("حلقة طويلة بمجلد %s والمستخدم بيختار اللقطات بنفسه. لا تقص ولا تمنتج شي.\nاقرأ transcript.txt والمرشّحات (hs clips cand %s list) وقيّم كل وحدة كم يتوقع تضرب (0-100) مع سبب قصير وعنوان (cand set)، وعدّل البداية والنهاية عشان تبدأ بهوك وتنتهي بفكرة كاملة، وأضف أقوى لحظات فاتت (cand add).\nأهم قاعدة: المعنى كامل. اقرأ النص قبل كل مرشّح وبعده بـ transcript.txt: لو يبدأ بنص قصة أو يرد على شي انقال قبل (مثل جواب لغز بدون اللغز، أو «هذا» و«اياه» بدون ما ينعرف وش هي)، رجّع بدايته لأول القصة؛ ولو الكلام ما خلص، طوّل نهايته لين تخلص الفكرة، حتى لو صار أطول من اللي طلبه. ولو الفكرة كاملة أطول من ضعف اللي طلبه، احذفه (cand rm) ولا تقصه بنصه." % (w, w)) + (("\nطلب المستخدم: " + note) if note else "")
                ok, msg = claude_spawn(w, task, "تقييم اللقطات"); job_set(w, ranking=ok); return self._json(200, {"ok": ok, "msg": msg})
            if a == "retry":
                w = card_by(data.get("id", ""))
                if not w: return self._json(404, {"ok": False})
                jb = job_get(w)
                if not jb.get("src"): return self._json(400, {"ok": False, "msg": "ما فيه شي أعيده"})
                grab_bg(jb["src"], w, {"mode": jb.get("mode"), "pick": jb.get("pick"), "n": jb.get("n"), "len": jb.get("len"), "note": jb.get("note")}); return self._json(200, {"ok": True})
            if a == "resume":   # 4.7.1: كمّل مع Claude من حيث وقف (يسأل قبل عن الحد من الواجهة)
                w = card_by(data.get("id", ""))
                if not w or not is_project(w): return self._json(404, {"ok": False})
                acts = activity(w, 0, 400); tail = "\n".join("- " + (e.get("text") or "")[:200] for e in acts[-6:])
                task = ("كمّل مونتاج المقطع اللي بمجلد %s من حيث وقفت. لا تعيد الخطوات اللي خلصت.\nآخر اللي كتبته بسجل المشروع:\n%s\n"
                        "شوف الملفات الموجودة (cut.json وcaps.json وstudio.json) عشان تعرف وين وصلت، واكتب كل خطوة بـ hs say، وآخر شي hs say \"جهز\" بنوع done." % (w, tail or "- ما فيه سجل"))
                ok, msg = claude_spawn(w, task, "تكملة المونتاج"); return self._json(200, {"ok": ok, "msg": msg})
            if a == "dup":
                w = card_by(data.get("id", ""))
                if not w or not is_project(w): return self._json(404, {"ok": False})
                try: d2 = proj_dup(w)
                except Exception as e: return self._json(500, {"ok": False, "msg": str(e)[:200]})
                return self._json(200, {"ok": True, "id": hashlib.md5(os.path.normcase(d2).encode()).hexdigest()[:10]})
            if a == "trash":   # 4.35: حذف مقطع أو حلقة: ينتقل لمجلد .trash بمجلد المشاريع (يرجع لو غيّرت رأيك)
                w = card_by(data.get("id", ""))
                if not w: return self._json(404, {"ok": False, "msg": "ما لقيت المقطع"})
                try: dst = project_trash(w, root)
                except PermissionError: return self._json(409, {"ok": False, "msg": "المقطع مفتوح بالاستوديو أو برنامج ثاني: سكّره وجرّب"})
                except Exception as e: return self._json(500, {"ok": False, "msg": "ما قدرت أحذفه: " + str(e)[:160]})
                return self._json(200, {"ok": True, "to": dst})
            if a == "rename":
                w = card_by(data.get("id", ""))
                if not w: return self._json(404, {"ok": False})
                tt = str(data.get("title") or "").strip()[:80]
                if is_ep(w): cfg = clips_cfg(w); cfg["title"] = tt; wj(J(w, "clips.json"), cfg)
                else: st = load_studio(w); hs_of(st)["title"] = tt; wj(J(w, "studio.json"), st)
                return self._json(200, {"ok": True})
            if a == "prep":
                w = card_by(data.get("id", ""))
                if not w or not is_project(w): return self._json(404, {"ok": False})
                if os.path.exists(J(w, ".hs", "prep.json")): os.remove(J(w, ".hs", "prep.json"))
                spawn_bg(["prep", w], J(w, ".hs", "prep.log")); return self._json(200, {"ok": True})
            if a == "open":
                w = card_by(data.get("id", ""))
                if not w: return self._json(404, {"ok": False, "msg": "ما لقيت المشروع"})
                try: pt = proj_start(w)
                except Exception as e: return self._json(500, {"ok": False, "msg": str(e)[:200]})
                projects_remember(w)
                return self._json(200, {"ok": True, "url": "/m" if data.get("mobile") else "/"}, {"Set-Cookie": "hs_p=%d; Path=/; SameSite=Lax" % pt})
            if a == "commands":
                L = rj(cmds_path(), []) or []; out = []
                for x in L[:80]:
                    w = x.get("work", ""); c = {"work": w, "id": hashlib.md5(os.path.normcase(w).encode()).hexdigest()[:10]}
                    out.append({**x, "pid": c["id"], "title": proj_card(w)["title"] if is_project(w) else os.path.basename(w), "thumb": proj_card(w)["thumb"] if is_project(w) else None})
                return self._json(200, {"commands": out})
            if a == "revert":
                L = rj(cmds_path(), []) or []; x = next((c for c in L if c["id"] == data.get("id")), None)
                if not x or not x.get("snap"): return self._json(404, {"ok": False, "msg": "ما فيه نسخة قبل هذا الطلب"})
                try:
                    pt = proj_start(x["work"]); req = urllib.request.Request("http://127.0.0.1:%d/hs/ver_restore" % pt, data=json.dumps({"id": x["snap"]}).encode(), headers={"Content-Type": "application/json"})
                    with urllib.request.urlopen(req, timeout=30) as r: res = json.loads(r.read().decode())
                except Exception as e: return self._json(500, {"ok": False, "msg": str(e)[:200]})
                cmd_log_set(x["id"], status="reverted"); return self._json(200, {"ok": True, "rebuild": res.get("rebuild")})
            if a == "device":
                du = shutil.disk_usage(root); live = []
                for w in hub_projects(root)[:40]:
                    pt = proj_port(w)
                    if pt:
                        pl = proj_live(pt) or {}; live.append({"name": os.path.basename(w), "port": pt, "agent": bool((pl.get("agent") or {}).get("running")), "job": bool((pl.get("job") or {}).get("running")), "jobKind": (pl.get("job") or {}).get("kind")})
                ts, tu = (None, hub_cfg().get("ts"))
                return self._json(200, {"battery": battery(), "disk": {"free": du.free, "total": du.total}, "awake": AWAKE["on"], "version": VERSION, "live": live,
                                        "notify": bool(notify_cfg().get("topic")), "ts": tu, "lan": "http://%s:%d/library?k=%s" % (LAN, port, TOKEN), "token": TOKEN, "os": sys.platform, "up": int(time.time() - STATE["started"]), "cpu": cpu_mode(), "whisper": _WD.get("v"), "cores": os.cpu_count() or 0})
            if a == "awake": keep_awake(bool(data.get("on"))); return self._json(200, {"ok": True, "awake": AWAKE["on"]})
            if a == "screen_off": return self._json(200, {"ok": screen_off()})
            if a == "notify_test":
                if not notify_cfg().get("topic"): return self._json(200, {"ok": False, "msg": "الإشعارات مو مفعّلة. فعّلها من زر «الجوال» داخل أي مشروع."})
                notify_send("تجربة من المكتبة: الإشعارات شغّالة"); return self._json(200, {"ok": True})
            if a in ("stop_agent", "stop_export"):
                n = 0
                for w in hub_projects(root)[:40]:
                    pt = proj_port(w)
                    if not pt: continue
                    try:
                        ep = "/hs/agent_stop" if a == "stop_agent" else "/hs/export_stop"
                        urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:%d%s" % (pt, ep), data=b"{}", headers={"Content-Type": "application/json"}), timeout=5); n += 1
                    except Exception: pass
                return self._json(200, {"ok": True, "n": n})
            if a == "shutdown" and self._local():
                for w in hub_projects(root)[:60]:
                    pt = proj_port(w)
                    if pt:
                        try: urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:%d/hs/quit" % pt, data=b"{}", headers={"Content-Type": "application/json"}), timeout=3)
                        except Exception: pass
                self._json(200, {"ok": True}); threading.Thread(target=lambda: (time.sleep(0.4), os._exit(0)), daemon=True).start(); return
            if a == "restart":
                for w in hub_projects(root)[:60]:
                    pt = proj_port(w)
                    if pt:
                        try: urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:%d/hs/quit" % pt, data=b"{}", headers={"Content-Type": "application/json"}), timeout=3)
                        except Exception: pass
                self._json(200, {"ok": True})
                def again():
                    time.sleep(0.6); kw = {"stdin": subprocess.DEVNULL, "stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}
                    if os.name == "nt": kw["creationflags"] = 0x00000008 | 0x00000200 | 0x08000000
                    else: kw["start_new_session"] = True
                    tgt = (rj(current_path(), {}) or {}).get("root") if data.get("latest") else None
                    hp = os.path.join(tgt, "hs.py") if tgt and os.path.isfile(os.path.join(tgt, "hs.py")) else os.path.abspath(__file__)
                    subprocess.Popen([PY, hp, "hub", "--no-browser"], **kw); time.sleep(0.2); os._exit(0)
                threading.Thread(target=again, daemon=True).start(); return
            if a == "upload":
                name = re.sub(r"[^\w\-]+", "-", (q.get("name") or [""])[0]).strip("-")[:40] or time.strftime("clip-%m%d-%H%M")
                ext = os.path.splitext((q.get("file") or ["v.mov"])[0])[1].lower() or ".mov"; kind = (q.get("kind") or ["edit"])[0]
                w = os.path.join(root, name); n = 1
                while os.path.exists(w): w = os.path.join(root, "%s-%d" % (name, n)); n += 1
                mode0 = (q.get("mode") or ["clips" if kind == "long" else "manual"])[0]   # motion = Claude يمنتجه والموشن أساسي
                os.makedirs(w); dst = J(w, ("long" + ext) if mode0 == "clips" else "upload" + ext); left = int(self.headers.get("Content-Length") or 0)
                with open(dst, "wb") as f:
                    while left > 0:
                        ch = self.rfile.read(min(1 << 20, left))
                        if not ch: break
                        f.write(ch); left -= len(ch)
                note = (q.get("note") or [""])[0][:1500]; mode = (q.get("mode") or ["clips" if kind == "long" else "manual"])[0]
                idq = (q.get("identity") or [""])[0][:40]
                pod_want(w, {"mode": mode, "tr": (q.get("tr") or [""])[0], "dub": (q.get("dub") or [""])[0], "host": (q.get("host") or ["1"])[0], "identity": idq})
                grab_bg(dst, w, {"mode": mode, "pick": (q.get("pick") or ["me"])[0], "n": (q.get("n") or ["5"])[0], "len": (q.get("len") or [""])[0], "note": note, "identity": idq})
                return self._json(200, {"ok": True, "work": w, "started": True, "msg": ""})
            return self._json(404, {"ok": False})
    def db_loop():   # 4.4: يحدّث قاعدة البيانات بالخلفية (بس المقاطع اللي تغيّرت)
        while True:
            try: db_sync(root)
            except Exception: pass
            time.sleep(45)
    threading.Thread(target=db_loop, daemon=True).start()
    FAC["root"] = root
    def fac_loop():   # 4.5: مصنع الليل
        while True:
            try: factory_tick()
            except Exception as e: FAC["err"] = str(e)[:200]
            time.sleep(20)
    threading.Thread(target=fac_loop, daemon=True).start()
    threading.Thread(target=lambda: (time.sleep(40), whisper_device()), daemon=True).start()
    srv = http.server.ThreadingHTTPServer(("0.0.0.0", port), HB); srv.daemon_threads = True
    print("المكتبة شغّالة: http://127.0.0.1:%d/library · الجوال: http://%s:%d/library?k=%s" % (port, LAN, port, TOKEN)); sys.stdout.flush()
    try: srv.serve_forever()
    except KeyboardInterrupt: pass

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"): print(__doc__); return
    def opt(name, default=None):
        if name in a:
            i = a.index(name); v = a[i + 1]; del a[i:i + 2]; return v
        return default
    def flag(name):
        if name in a: a.remove(name); return True
        return False
    def multi(name):
        if name not in a: return []
        i = a.index(name); j = i + 1
        while j < len(a) and not a[j].startswith("--"): j += 1
        v = a[i + 1:j]; del a[i:j]; return v
    engine = opt("--engine"); port = int(opt("--port", "8800")); cmd = a[0]
    if os.environ.get("CLAUDECODE") and cmd != "claude":   # Claude نفسه شغّل hs: نحفظ مكانه للمكتبة (لو ما هو بالـ PATH نلقاه من العملية الأم)
        try: claude_learn()
        except Exception: pass
    if cmd not in ("sync", "claude", "db", "tools", "platform", "release", "autoupdate", "selftest"): lighten()
    if cmd == "doctor": sys.exit(0 if cmd_doctor(engine) else 1)
    if cmd == "platform": return cmd_platform(a[1:])
    if cmd == "tools": print(tools_text()); return
    if cmd == "deps": return cmd_deps(a[1:])
    if cmd == "identity": return cmd_identity(a[1:])   # 4.37
    if cmd == "notify": return cmd_notify(a[1:])
    if cmd == "style": return cmd_style(a[1:])
    if cmd == "sound": return cmd_sound(a[1:])
    if cmd == "update": return cmd_update()
    if cmd == "fonts": return cmd_fonts(a[1:])
    if cmd == "gloss": return cmd_gloss(a[1:])
    if cmd == "clips": return cmd_clips(a[1:])
    if cmd == "grab": return cmd_grab(a[1:])
    if cmd == "db": return cmd_db(a[1:])
    if cmd == "sync": return cmd_sync(a[1:])
    if cmd == "claude": return cmd_claude(a[1:])
    if cmd == "release": return cmd_release(a[1:])
    if cmd == "autoupdate": return cmd_autoupdate(a[1:])
    if cmd == "hub": return cmd_hub(a[1:] + (["--port", str(port)] if "--port" in sys.argv else []))   # 4.26: --port كان ينأكل قبل ما يوصل للمكتبة
    if cmd == "selftest": sys.exit(0 if cmd_selftest(os.path.abspath(a[1]) if len(a) > 1 else None, engine) else 1)
    if len(a) < 2: sys.exit("لازم مجلد الشغل: python hs.py %s <work>" % cmd)
    work = os.path.abspath(a[1])
    if cmd == "open": return cmd_open(work, port, engine, browser=not flag("--no-browser"))
    if cmd == "serve": return serve(work, port, engine)
    if not os.path.isdir(work): sys.exit("ما لقيت مجلد الشغل: " + work)
    if cmd in ("undo", "redo"): return cmd_undo(work, cmd == "undo")
    if cmd == "say": kind = opt("--kind", "step"); say(work, " ".join(a[2:]), kind); return
    if os.path.isdir(J(work, ".hs", "hist")) and cmd not in ("status", "steps", "facts", "check", "list", "plan"):   # 4.14: أوامرك تنحفظ خطوات بالسجل
        try: hist_checkpoint(work, "تعديل")
        except Exception: pass
        import atexit
        def _hc():
            try: hist_checkpoint(work, "Claude: " + cmd)
            except Exception: pass
        atexit.register(_hc)
    if cmd in ("remove", "export"):
        eng = find_engine(engine) or sys.exit("ما لقيت المحرّك — مرّر --engine"); S = os.path.join(eng, "scripts"); fix_windows_path(); log = lambda s: print(s, flush=True)
        if cmd == "remove":
            cards = [int(x) - 1 for x in multi("--cards")]; rngs = [[float(y) for y in x.split("-")] for x in multi("--ranges")]
            words = [(f["card"], f["idx"]) for f in check(work)["fillers"]] if flag("--fillers") else []
            if not flag("--force"):   # 4.9: الكلام المهم (رقم، اسم، نصيحة، آخر المقطع) ما ينشال بدون موافقته
                cs_ = (rj(J(work, "caps.json"), {}) or {}).get("cards") or []; cm_ = cutmap_mod(); risky = []
                for i in cards:
                    if 0 <= i < len(cs_):
                        why = cm_.important(card_key(cs_[i])) + (["آخر كلامك بالمقطع"] if i >= len(cs_) - 2 else [])
                        if why: risky.append("  %d. %s   ← %s" % (i + 1, card_key(cs_[i]), "، ".join(why)))
                for a2, b2 in rngs:
                    for i, c in enumerate(cs_):
                        if c["s"] < b2 and c["e"] > a2 and i not in cards:
                            why = cm_.important(card_key(c))
                            if why: risky.append("  %d. %s   ← %s (جزء منها بالمقطع المحذوف)" % (i + 1, card_key(c), "، ".join(why)))
                if risky: print("⛔ ما حذفت شي. فيه كلام مهم:\n" + "\n".join(risky) + "\nاسأله أول (اعرض الجمل كما هي). لو وافق: أعد الأمر مع --force"); sys.exit(2)
            print(json.dumps(remove_ranges(work, S, log, ranges=rngs, cards=cards, words=words), ensure_ascii=False))
        else:
            miss = [r for r in brief_reqs(work) if not r["ok"]]
            if miss and not flag("--force"):
                print("ما طبّقت كل إجاباته بصفحة الأسئلة:"); [print("  □ %s %s%s" % (r["k"], r["label"], ("  ← " + r["why"]) if r["why"] else "")) for r in miss]
                sys.exit("طبّقها ثم صدّر. (لو هو طلب يصدّر كذا: export --force)")
            print("الملفات:", ", ".join(export(work, S, log, kind="clean" if flag("--clean") else "final", hooks=flag("--hooks"), frame=opt("--frame"))))
        return
    rest = a[2:]
    if cmd == "patch": r = patch(work); print("انركّبت الإضافة" if r else "الإضافة مركّبة من قبل (حدّثت نسختها)")
    elif cmd == "prep": cmd_prep(work, rest)
    elif cmd == "notes": cmd_notes(work, rest)
    elif cmd == "tr": cmd_tr(work, rest)
    elif cmd == "text": cmd_text(work, rest)
    elif cmd == "set": cmd_set(work, rest)
    elif cmd == "layer": cmd_layer(work, rest)
    elif cmd == "kf": cmd_kf(work, rest)   # 4.29
    elif cmd == "hook": cmd_hook(work, rest)
    elif cmd == "check": cmd_check(work)
    elif cmd == "retention":   # 4.5: فحص قبل النشر
        R = retention(work)
        if not R.get("ok"): sys.exit(R.get("msg") or "ما قدرت أفحص")
        print("فحص قبل النشر: %d/100 · تقدير اللي يكملون للنهاية %d%%" % (R["score"], R["end"]))
        print("  " + " · ".join("%s %d" % (k, v) for k, v in R["dims"].items()))
        for f in R["fixes"]: print("- [%s] %s %s" % (tfmt(f["t"]), f["msg"], ("(تصليح: %s)" % f["fix"]) if f.get("fix") else ""))
        for g in R["takes"]: print("- إعادات: الجمل %s ← خلّ %d" % (", ".join(str(i + 1) for i in g["cards"]), g["keep"] + 1))
    elif cmd == "brief": cmd_brief(work, rest)
    elif cmd == "media": cmd_media(work, rest)
    elif cmd == "sfx": cmd_sfx(work, rest)
    elif cmd == "bleep": cmd_bleep(work, rest)
    elif cmd == "face":
        try: os.remove(J(work, "face.json"))
        except OSError: pass
        vision_run(work, ["face"], print)
    elif cmd == "mask": vision_run(work, ["mask"] + (rest or mask_need(work) or ["all"]), print)
    elif cmd == "shot":
        if not rest: sys.exit('shot <work> <url> [--at <ث>] [--dur 4] [--top]   (--top = أول شاشة فقط بدل الصفحة كاملة)')
        def _o(nm, d=None):
            if nm in rest: i = rest.index(nm); x = rest[i + 1]; del rest[i:i + 2]; return x
            return d
        at = _o("--at", 0); dur = _o("--dur", 4); top = "--top" in rest
        if top: rest.remove("--top")
        lid, name = shot_add(work, rest[0], float(at), float(dur), not top); print("انضافت لقطة الموقع %s كطبقة %s بإطار متصفح عند %s ث" % (name, lid, at))
    elif cmd == "gen": cmd_gen(work, rest)
    elif cmd == "auto": cmd_auto(work, rest)
    elif cmd == "caps": cmd_caps(work, rest)
    elif cmd == "look": cmd_look(work, rest)
    elif cmd == "mode": cmd_mode(work, rest)
    elif cmd == "dub":   # 4.26
        sub = rest[0] if rest else "status"
        if sub == "script":
            D = dub_script(work, rest[1] if len(rest) > 1 else "ar"); print("كتبت %d جملة بـ dub.json و dub-script.txt. ترجم كل وحدة بنفس طولها تقريباً (words) ثم: hs dub <work> import <ملف.json>  بشكل [{\"i\":0,\"tr\":\"…\"}]" % len(D["segs"]))
        elif sub == "import": print("انضافت %d ترجمة (وصارت سطر الترجمة بالكابشن)" % dub_import(work, rj(os.path.abspath(rest[1]), [])))
        elif sub == "add": print("انضاف: " + dub_add(work, rest[1], os.path.abspath(rest[2])))
        elif sub == "track": print("انضاف ملف الدبلجة الكامل: " + dub_track(work, os.path.abspath(rest[1])))
        elif sub in ("build", "on"):
            f, miss = dub_build(work); st_ = load_studio(work); hs_of(st_).setdefault("mix", {})["dub"] = True; wj(J(work, "studio.json"), st_); print("الدبلجة تركّبت (%s) وصارت بدل الصوت الأصلي%s" % (f, ("، وناقص صوت %d جملة" % miss) if miss else ""))
        elif sub == "off": st_ = load_studio(work); hs_of(st_).setdefault("mix", {})["dub"] = False; wj(J(work, "studio.json"), st_); print("رجع الصوت الأصلي")
        else:
            D = dub_get(work)
            if not D: print("ما فيه دبلجة. ابدأ: hs dub <work> script ar|en|es|…"); return
            segs = D.get("segs") or []; print("الدبلجة: %s · %d جملة · مترجم %d · فيه صوت %d%s · %s" % (DUB_LANGS.get(D.get("lang"), D.get("lang")), len(segs), sum(1 for x in segs if x.get("tr")), sum(1 for x in segs if x.get("file")), " · ملف كامل" if D.get("track") else "", "شغّالة" if dub_on(work) else "مطفية"))
    elif cmd == "quality":   # 4.25
        if not rest or rest[0] == "status": print("التحسين: " + {"off": "مطفي", "light": "خفيف", "strong": "قوي"}[enh_level(work)]); return
        if rest[0] == "preview": print(quality_preview(work, float(rest[1]) if len(rest) > 1 else 3.0, rest[2] if len(rest) > 2 else "light")); return
        if rest[0] not in ENH_LEVELS: sys.exit("quality <work> off | light | strong | preview <ثانية> [light|strong]")
        st_ = load_studio(work); hs_of(st_)["enhance"] = {"level": rest[0]}; wj(J(work, "studio.json"), st_); vfr_extract(work, print, rest[0]); print("تم. الفريمات صارت بالتحسين (%s)، والتصدير بياخذها" % rest[0])
    elif cmd == "media":   # 4.23: الفيديو مبني من أي قص، و fresh يبنيه على آخر قص
        ok_, vm_ = media_map(work)
        if rest[:1] == ["fresh"]:
            eng_ = find_engine(engine) or sys.exit("ما لقيت مجلد engine"); print("بنيته من جديد" if ensure_media(work, os.path.join(eng_, "scripts"), print) else "الفيديو أصلاً على آخر قص")
        else: print("الفيديو على آخر قص" if vm_ is None and ok_ else ("القص فوري (%d قطعة)، والفيديو ينبني وقت التصدير. للبناء الحين: hs media <work> fresh" % len(vm_) if ok_ else "فيه جزء رجّعته مو موجود بالفيديو الحالي: hs media <work> fresh"))
    elif cmd == "logo": cmd_logo(work, rest)
    elif cmd == "takes": cmd_takes(work, rest)
    elif cmd == "plan": cmd_plan(work, rest)
    elif cmd == "rmbg": cmd_rmbg(work, rest)
    elif cmd == "voice": cmd_voice(work, rest)
    elif cmd == "steps":
        for s_ in steps(work): print("%s %d %s%s" % ({"done": "✓", "now": "←", "todo": "·"}[s_["state"]], s_["n"], s_["label"], ("  (%d كلمة تراجعها)" % s_["unsure"]) if s_.get("unsure") else ""))
    elif cmd == "facts":
        F_ = facts(work); print(("تأكد من هذي قبل النشر:\n" + "\n".join("  %s  %s  (%s)" % (fmt_t(x["s"]), x["text"][:90], "، ".join(x["why"])) for x in F_)) if F_ else "ما فيه أرقام ولا أسماء منتجات تحتاج تأكيد.")
    elif cmd == "cuts":
        bad, old_, new_ = cut_on_sound(work)
        if not bad: print("ولا قطعة نازلة على صوت.")
        elif "fix" in rest:
            if _same_keep(old_, new_, 0.005): print("فيه %d قطعة على صوت بس ما لقيت سكتة قريبة تنزل عليها." % len(bad))
            else: r_ = apply_keep(work, old_, new_, os.path.join(find_engine(None), "scripts"), print, "--no-rebuild" not in rest, snap="قبل تصليح القطعات"); print("صلّحت %d قطعة: المدة %.2f ث" % (sum(1 for b_ in bad if b_["to"] is not None), r_["total"]))
        else: print("%d قطعة نازلة على صوت (تقص حرف):\n" % len(bad) + "\n".join("  مقطع %d %s عند %.2f%s" % (b_["seg"] + 1, "بدايته" if b_["edge"] == "s" else "نهايته", b_["t"], (" ← %.2f" % b_["to"]) if b_["to"] is not None else " (ما فيه سكتة قريبة)") for b_ in bad) + "\nصلّحها: hs cuts <work> fix")
    elif cmd == "beat": cmd_beat(work, rest)
    elif cmd == "pack": print("\n".join(pack(work))); print("→ " + J(work, ".hs", "pack.zip"))
    elif cmd == "brand": cmd_brand(work, rest)
    elif cmd == "publish": cmd_publish(work, rest)
    elif cmd == "kinetic": cmd_kinetic(work, rest)
    elif cmd == "dahih": cmd_dahih(work, rest)
    elif cmd == "status": cmd_status(work)
    else: sys.exit("أمر غير معروف: " + cmd)

if __name__ == "__main__": main()
