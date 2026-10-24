# -*- coding: utf-8 -*-
"""خطة القص: يقيس السكتات بالصوت ويطلع مقاطع الكلام.  الاستخدام: python3 01_cut_plan.py <workdir>"""
# ── توافق ويندوز/UTF-8 (مضاف) ─────────────────────────────────────
import sys as _sys, builtins as _bi
try:
    _sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    _sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
_real_open = _bi.open
def _utf8_open(f, mode="r", *a, **k):
    if "b" not in mode:
        k.setdefault("encoding", "utf-8")
    return _real_open(f, mode, *a, **k)
_bi.open = _utf8_open
# ──────────────────────────────────────────────────────────────────
import subprocess, re, json, sys, os
DB = None
from fractions import Fraction
W = os.path.abspath(sys.argv[1]); SRC = os.path.join(W, "src.mov")
# 4.7.1: القص كان يخلي سكتات لين 0.6 ث (ما يشيل إلا اللي فوق 0.35 ث ويحط 0.13 قبل وبعد)، وعتبة الصمت ثابتة -32dB.
# الحين: عتبة تتكيّف مع ضجيج الغرفة، وكل سكتة أطول من النفَس الطبيعي تنقص لـ 0.22 ث (الإيقاع الهادي 0.30)،
# وحدود القص على فريمات الفيديو بالضبط عشان الصوت والصورة ما ينزاحون عن بعض مع كثرة القطعات.
def _rj(n):
    try: return json.load(open(os.path.join(W, n)))
    except Exception: return {}
_th, _br = _rj("theme.json"), _rj("brief.json")
CALM = str(_th.get("pace") or _br.get("pace") or "").lower() == "calm"
GAP = float(os.environ.get("HS_GAP") or (0.24 if CALM else 0.16))   # أطول سكتة تبقى بين جملتين (4.9: أضيق، كانت 0.22)
EDGE = 0.12                                                           # قبل أول كلمة وبعد آخر كلمة
MINSEG = 0.25

def probe(entries, sel=None):
    a = ["ffprobe", "-v", "error"] + (["-select_streams", sel] if sel else []) + ["-show_entries", entries, "-of", "csv=p=0", SRC]
    return subprocess.run(a, capture_output=True, text=True).stdout.strip()
dur = float(probe("format=duration"))
try:
    _fr = probe("stream=r_frame_rate", "v:0").split("\n")[0].strip()
    FPS = Fraction(_fr) if _fr and _fr != "0/0" else Fraction(30)
    if not (10 <= FPS <= 121): FPS = Fraction(30)
except Exception: FPS = Fraction(30)
def snap(t): return float(round(Fraction(t).limit_denominator(100000) * FPS) / FPS)

def vad():
    """مستوى الصوت كل 10 جزء من الثانية، والعتبة = أرضية ضجيج المكان + 10 dB."""
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", SRC, "-vn", "-ac", "1", "-ar", "16000", "-af", "highpass=f=90", "-f", "s16le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, dtype="<i2").astype(np.float32) / 32768.0
    hop = 160; n = len(x) // hop
    if n < 50: raise ValueError("صوت قصير")
    db = 20 * np.log10(np.sqrt(np.mean(x[:n * hop].reshape(n, hop) ** 2, axis=1)) + 1e-9)
    db = np.convolve(db, np.ones(3) / 3, mode="same")
    floor = float(np.percentile(db, 10)); peak = float(np.percentile(db, 95))
    thr = min(max(floor + 10.0, -52.0), peak - 12.0)
    v = db > thr
    # نسد الفراغات الصغيرة جوّا الكلمة (أقل من 80 جزء) ونشيل النقرات (أقل من 60 جزء)
    def runs(mask, val):
        out = []; i = 0
        while i < n:
            if mask[i] == val:
                j = i
                while j < n and mask[j] == val: j += 1
                out.append((i, j)); i = j
            else: i += 1
        return out
    for a, b in runs(v, False):
        if b - a < 8 and a > 0 and b < n: v[a:b] = True
    for a, b in runs(v, True):
        if b - a < 6: v[a:b] = False
    global DB
    DB = db
    return [(a / 100.0, b / 100.0) for a, b in runs(v, True)], thr, floor

try:
    speech, THR, FLOOR = vad()
    how = "عتبة %.0f dB (ضجيج المكان %.0f dB)" % (THR, FLOOR)
except Exception as e:   # بلا numpy: الطريقة القديمة بعتبة ثابتة
    out = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", SRC, "-af", "silencedetect=noise=-32dB:d=%.2f" % GAP, "-f", "null", "-"], capture_output=True, text=True).stderr
    sil = []; s0 = None
    for m in re.finditer(r"silence_(start|end): ([0-9.]+)", out):
        k, val = m.group(1), float(m.group(2))
        if k == "start": s0 = val
        else: sil.append(((0.0 if s0 is None else s0), val)); s0 = None
    if s0 is not None: sil.append((s0, dur))
    speech = []; cur = 0.0
    for a, b in sil:
        if a - cur > 0.01: speech.append((cur, a))
        cur = b
    if dur - cur > 0.01: speech.append((cur, dur))
    how = "عتبة ثابتة -32 dB (" + str(e)[:40] + ")"
    FLOOR = -60.0

# 4.9: آخر الكلمة الهادية ما ينقص. قبل: آخر مقطع بالجملة لو انقال بصوت واطي كان تحت العتبة وينقص،
# فكل مقطع كلام يمتد قدام لين 0.25 ث وورا 0.12 ث ما دام فيه صوت فوق أرضية ضجيج المكان بـ 6 dB.
# (توقيت whisper ما نعتمد عليه هنا: أحياناً يمد الكلمة على سكتة ثانيتين)
if DB is not None and speech:
    soft = FLOOR + 6.0; grown = []
    for a, b in speech:
        ia, ib = int(a * 100), int(b * 100)
        k = ib
        while k < min(len(DB), ib + 25) and DB[k] > soft: k += 1
        j = ia
        while j > max(0, ia - 12) and DB[j - 1] > soft: j -= 1
        grown.append((j / 100.0, k / 100.0))
    merged = []
    for a, b in grown:
        if merged and a <= merged[-1][1] + 0.02: merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else: merged.append((a, b))
    speech = merged

# 4.43: الكلام الواطي ما ينقص (القص ما يشيل معنى): لو التفريغ (a.json) موجود، كل كلمة فيه ينحسب صوتها كلام بعتبة أوطى
# (فوق ضجيج المكان بـ 4 dB) بس داخل حدود الكلمة نفسها، لأن whisper أحياناً يمد الكلمة على سكتة. كلمة ما فيها صوت أبد = هلوسة، ما تنحسب.
_A = _rj("a.json"); _add = []
for _sg in _A.get("segments") or []:
    for _wd in _sg.get("words") or []:
        try: _a, _b = float(_wd.get("start") or 0), float(_wd.get("end") or 0)
        except (TypeError, ValueError): continue
        if _b <= _a or not (_wd.get("word") or "").strip(): continue
        if DB is None: _add.append((_a, min(_b, _a + 1.2))); continue
        _ia, _ib = max(0, int(_a * 100)), min(len(DB), int(_b * 100) + 1)
        _on = [k for k in range(_ia, _ib) if DB[k] > FLOOR + 4.0]
        if _on: _add.append((_on[0] / 100.0, (_on[-1] + 1) / 100.0))
if _add:
    _was = sum(b - a for a, b in speech); merged = []
    for a, b in sorted(list(speech) + _add):
        if merged and a <= merged[-1][1] + 0.02: merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else: merged.append((a, b))
    speech = merged; _gain = sum(b - a for a, b in speech) - _was
    if _gain > 0.05: print("رجّعت %.1f ث كلام واطي كان بينقص (من التفريغ)" % _gain)

# نبني المقاطع: أي سكتة أطول من GAP تنقص لـ GAP بالضبط (نص قبلها ونص بعدها، والميل للي بعدها)
keep = []
if speech:
    s0 = max(0.0, speech[0][0] - EDGE); e0 = speech[0][1]
    for a, b in speech[1:]:
        if a - e0 <= GAP: e0 = b; continue
        keep.append([s0, e0 + GAP * 0.45]); s0 = a - GAP * 0.55; e0 = b
    keep.append([s0, min(dur, e0 + EDGE)])
keep = [[snap(max(0.0, a)), snap(min(dur, b))] for a, b in keep]
keep = [x for x in keep if x[1] - x[0] >= MINSEG] or [[0.0, snap(dur)]]
tot = sum(b - a for a, b in keep)
json.dump({"keep": [[round(a, 6), round(b, 6)] for a, b in keep], "total": round(tot, 3), "src_dur": dur, "gap": GAP, "fps": float(FPS)},
          open(os.path.join(W, "cut.json"), "w"), indent=1)
print(f"{how} · أطول سكتة باقية {GAP:.2f} ث")
print(f"مقاطع={len(keep)}  الباقي={tot:.2f}s  انشال={dur-tot:.2f}s ({(dur-tot)/dur*100:.0f}%)")
