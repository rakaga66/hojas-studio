"""4.9: خريطة القص المشتركة. أي حذف (جملة، كلمة، مقطع) يمر من هنا عشان الصوت والصورة والكابشن يبقون على نفس الوقت.

قبل: الحذف كان يزحّف الكابشن بحساب، ويرمي قطع الفيديو الأقصر من 0.12 أو 0.20 ث بدون ما يحسبها،
فكل حذف يخلّي الكابشن متأخر شوي، ومع كم حذف يصير متأخر نص ثانية. وحدود القص كانت ثابتة بالحشوة،
فأحياناً تاكل أول كلمة من الجملة اللي بعدها وكابشنها يبقى.
الحين: كل وقت ينحسب من مكانه بالمصدر: وقت قديم ← وقته بالتسجيل الأصلي ← وقته بالقص الجديد.
اللي انحذف مصدره ينحذف معه (كلمة، مؤثر، طبقة)، وحدود القص تنزل على أهدأ نقطة بين الكلمتين.
"""
import json, os, re, subprocess
from fractions import Fraction

MIN_PART = 0.12   # أقصر قطعة فيديو تبقى بعد الحذف (أقصر من كذا رمش)


def offsets(keep):
    o, acc = [], 0.0
    for a, b in keep: o.append(acc); acc += b - a
    return o, acc


def out_to_src(keep, off, t):
    """وقت بالفيديو المقصوص ← وقته بالتسجيل الأصلي."""
    if not keep: return t
    for (a, b), o in zip(keep, off):
        if t < o + (b - a) + 1e-9: return a + max(0.0, t - o)
    a, b = keep[-1]; return b + (t - off[-1] - (b - a))


def src_to_out(keep, off, s, snap=None):
    """وقت بالأصل ← وقته بالمقصوص. None لو انحذف. snap='prev'|'next' يلزقه بأقرب حد باقي."""
    for (a, b), o in zip(keep, off):
        if a - 1e-6 <= s <= b + 1e-6: return o + min(max(s, a), b) - a
    if snap is None: return None
    best = None
    for (a, b), o in zip(keep, off):
        if snap == "next" and a >= s: return o
        if snap == "prev" and b <= s: best = o + (b - a)
    if snap == "next": return off[-1] + (keep[-1][1] - keep[-1][0]) if keep else 0.0
    return best if best is not None else 0.0


def fps_of(work, cut=None):
    f = (cut or {}).get("fps")
    if f: return Fraction(f).limit_denominator(1001)
    src = os.path.join(work, "src.mov")
    if not os.path.isfile(src) and os.path.isfile(os.path.join(work, "src-cutz.mp4")): src = os.path.join(work, "src-cutz.mp4")   # 4.25
    try:
        r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate", "-of", "csv=p=0", src], capture_output=True, text=True).stdout.strip().split("\n")[0]
        F = Fraction(r) if r and r != "0/0" else Fraction(30)
        return F if 10 <= F <= 121 else Fraction(30)
    except Exception: return Fraction(30)


def snap(t, F): return float(round(Fraction(t).limit_denominator(100000) * F) / F)


_ENV = {}
def env(work):
    """شدة الصوت بالأصل كل 10 جزء من الثانية (dB). من a.wav لو موجود، وإلا من src.mov."""
    if work in _ENV: return _ENV[work]
    src = os.path.join(work, "a.wav") if os.path.isfile(os.path.join(work, "a.wav")) else os.path.join(work, "src.mov")
    if not os.path.isfile(src) and os.path.isfile(os.path.join(work, "src-cutz.mp4")): src = os.path.join(work, "src-cutz.mp4")   # 4.25
    try: _b = json.load(open(os.path.join(work, "cut.json"), encoding="utf-8")).get("base")
    except Exception: _b = None
    if _b and os.path.isfile(os.path.join(work, _b)): src = os.path.join(work, _b)   # 4.54: فيه مقاطع مضافة: الصوت من الأصل الجديد
    db = []
    try:
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-vn", "-ac", "1", "-ar", "16000", "-af", "highpass=f=90", "-f", "s16le", "-"], capture_output=True).stdout
        try:
            import numpy as np
            x = np.frombuffer(raw, dtype="<i2").astype(np.float32) / 32768.0; n = len(x) // 160
            if n: db = list(20 * np.log10(np.sqrt(np.mean(x[:n * 160].reshape(n, 160) ** 2, axis=1)) + 1e-9))
        except Exception:
            import array, math
            a = array.array("h"); a.frombytes(raw[:len(raw) // 2 * 2])
            for i in range(0, len(a) - 160, 160):
                s = sum(v * v for v in a[i:i + 160]) / 160.0; db.append(10 * math.log10(s / 32768.0 ** 2 + 1e-18))
    except Exception: db = []
    _ENV[work] = db; return db


def quiet_point(db, a, b):
    """أهدأ نقطة (متوسط 50 جزء من الثانية) بين a و b بالثواني. بدون صوت محسوب: النص."""
    if b - a < 0.04 or not db: return (a + b) / 2
    i0, i1 = max(0, int(a * 100)), min(len(db) - 1, int(b * 100))
    if i1 - i0 < 2: return (a + b) / 2
    best, bi = 1e9, (i0 + i1) // 2
    for i in range(i0, i1 + 1):
        lo, hi = max(i0, i - 2), min(i1, i + 2); m = sum(db[lo:hi + 1]) / (hi - lo + 1)
        if m < best - 0.5: best, bi = m, i
    return bi / 100.0


def remove(work, keep, out_ranges, guards=(), slack=0.15):
    """يشيل مقاطع (بزمن الإخراج القديم). يرجّع (keep جديد، دالة تحويل الوقت، الثواني اللي انشالت).
    guards: كلمات باقية بزمن الإخراج القديم [(s,e)…]، حدود القص ما تدخل فيها."""
    cut = {}
    try: cut = json.load(open(os.path.join(work, "cut.json"), encoding="utf-8"))
    except Exception: pass
    F = fps_of(work, cut); db = env(work)
    off, total = offsets(keep)
    g_src = [(out_to_src(keep, off, s), out_to_src(keep, off, e)) for s, e in guards]
    src_del = []
    for ds, de in sorted(out_ranges):
        ds, de = max(0.0, ds), min(total, de)
        if de - ds <= 0.02: continue
        for (a, b), o in zip(keep, off):
            lo, hi = max(ds, o), min(de, o + (b - a))
            if hi <= lo: continue
            sa, sb = a + (lo - o), a + (hi - o)
            # الحد ينزل على أهدأ نقطة قريبة، بدون ما يدخل كلمة باقية
            if lo > o + 1e-6:
                wa = max(sa - slack, max([e for s, e in g_src if e <= sa + 1e-6] or [a]))
                sa = quiet_point(db, wa, min(sa + slack, sb - 0.02))
            if hi < o + (b - a) - 1e-6:
                wb = min(sb + slack, min([s for s, e in g_src if s >= sb - 1e-6] or [b]))
                sb = quiet_point(db, max(sb - slack, sa + 0.02), wb)
            if sb - sa > 0.01: src_del.append([sa, sb])
    new = []
    for a, b in keep:
        parts = [[a, b]]
        for x0, x1 in src_del:
            o2 = []
            for x, y in parts:
                if x1 <= x or x0 >= y: o2.append([x, y]); continue
                if x0 > x: o2.append([x, x0])
                if x1 < y: o2.append([x1, y])
            parts = o2
        new += parts
    new = [[snap(a, F), snap(b, F)] for a, b in new]
    new = [[round(a, 6), round(b, 6)] for a, b in new if b - a >= MIN_PART]
    if not new: raise ValueError("ما يبقى شي من الفيديو")
    noff, ntot = offsets(new)

    def remap(t, mode=None):
        """وقت بالإخراج القديم ← الجديد. None لو انحذف (mode='prev'/'next' يلزقه بأقرب حد)."""
        return src_to_out(new, noff, out_to_src(keep, off, t), mode)
    return new, remap, round(total - ntot, 3)


def remap_caps(caps, remap, total):
    """يحرك الكابشن على القص الجديد: الكلمة اللي انحذف أكثر من نصها تنشال، وكل كرت يتبع كلماته."""
    out = []
    for c in caps.get("cards") or []:
        ws = []
        for w in c.get("w") or []:
            m = remap((w["s"] + w["e"]) / 2)
            if m is None: continue
            s = remap(w["s"], "next"); e = remap(w["e"], "prev")
            s = m if s is None or s > m else s; e = m if e is None or e < m else e
            ws.append({**w, "s": round(s, 3), "e": round(max(e, s + 0.08), 3)})
        if not ws: continue
        cs = remap(c["s"], "next"); ce = remap(c["e"], "prev")
        cs = ws[0]["s"] if cs is None else min(cs, ws[0]["s"]); ce = ws[-1]["e"] if ce is None else max(ce, ws[-1]["e"])
        out.append({**c, "s": round(max(0.0, cs), 3), "e": round(min(total, ce), 3), "w": ws})
    for i in range(len(out) - 1):
        if out[i]["e"] > out[i + 1]["s"] - 0.02: out[i]["e"] = round(max(out[i]["w"][-1]["e"], out[i + 1]["s"] - 0.02), 3)
    return {**caps, "total": round(total, 3), "cards": out}


# ── الكلام المهم: لا ينحذف بدون ما يوافق المستخدم ──
_NUM = r"[0-9٠-٩%$]|(?<!\w)[وبلف]?(?:واحد|وحدة|اثنين|ثنتين|ثلاث|ثلاثة|أربع|اربع|أربعة|اربعة|خمس|خمسة|ست|ستة|سبع|سبعة|ثمان|ثمانية|تسع|تسعة|عشر|عشرة|عشرين|ثلاثين|أربعين|اربعين|خمسين|مية|مئة|ميه|ألف|الف|آلاف|الاف|ألفين|مليون|ملايين|بالمية|بالمئة|دولار|ريال)(?!\w)"
_ADV = r"لازم|لا ت|ما ت|حاول|انتبه|احذر|مهم|أهم|اهم|دائماً|دايم|أبد|ابد|أبتعد|ابتعد|تبتعد|نصيحة|أنصح|انصح|السر|الخطأ|غلط|مجاني|بلاش|خصم|عرض|أفضل|افضل|أسرع|اسرع|أدق|ادق|أرخص|ارخص|أغلى|اغلى|أقوى|اقوى|أضعف|بدل|لأن|لان|عشان"
def important(text, names=()):
    """أسباب إن الجملة فيها معلومة (أرقام، أسماء، نصيحة أو تحذير أو مقارنة). فاضية = جملة عادية."""
    t = str(text); why = []
    if re.search(_NUM, t): why.append("رقم أو سعر")
    if re.search(r"[A-Za-z]{2,}", t) or any(n and n in t for n in names): why.append("اسم")
    if re.search(_ADV, t): why.append("نصيحة أو مقارنة")
    return why
