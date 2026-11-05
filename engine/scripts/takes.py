"""4.10: اختيار الجمل من التسجيل الخام. مشترك بين hs.py و 02_captions.py.

المشكلة: المتكلم يتلعثم، أو يبدأ الجملة ويتركها، أو يعيدها مرتين وثلاث، وأحياناً الصح هي الأخيرة
وأحياناً وحدة بالنص. قص السكتات لحاله يخلّيها كلها بالمقطع.

الحل:
1. نقسم كلامه (كلمات whisper بوقت التسجيل الأصلي) لمحاولات على الوقفات.
2. نوسم كل محاولة: إعادة (نفس الجملة أكثر من مرة) · بداية متعثرة (بدأها وتركها وأعادها) · بلا كلام (whisper اخترعها فوق السكوت)
   · ضجيج (كحة، نفس، كلمة مقطوعة) · حشو (آ، امم) · تحية بالبداية (اقتراح).
3. داخل الجملة الباقية: نقص التلعثم لين تبدأ الجملة فعلاً («كل يوم.. كل يوم يطلع لك» ← «كل يوم يطلع لك»)، و«آ.. امم» بنصها.
4. لكل مجموعة إعادات نختار مبدئياً آخر محاولة كاملة، و Claude يراجع ويختار الأفضل بالمعنى (الكاملة، الصح، الأوضح).
5. التطبيق: القص الجديد = قص السكتات ناقص المحذوف، والحدود على أهدأ نقطة بين الكلمتين.
"""
import json, os, re, difflib

PAUSE = 0.45          # وقفة تفصل محاولة عن اللي بعدها
HES = {"ا", "اا", "ااا", "امم", "ام", "مم", "ممم", "اممم", "امممم", "هم", "همم", "هممم", "ءء", "اه اه"}   # أصوات تردد (مو «آه» بمعنى نعم)
HALLU = ["اشتركوا في القناة", "اشترك في القناة", "لا تنسوا الاشتراك", "ترجمة نانسي قنقر", "نانسي قنقر", "شكرا للمشاهدة", "شكرا على المشاهدة",
         "اشتركو في القناة", "سبتايتل", "ترجمة اسعد", "شكرا لكم على المشاهدة", "موسيقى", "تصفيق"]
GREET = ["السلام عليكم", "سلام عليكم", "مساكم الله", "مساء الخير", "صباح الخير", "صباحكم", "مساكم", "هلا والله", "هلا وغلا", "اهلا وسهلا", "اهلين", "مرحبا",
         "حياكم الله", "يا هلا", "هلا يا", "كيف الحال", "شلونكم", "كيفكم"]
STOP = {"في", "من", "علي", "الي", "عن", "مع", "هذا", "هذي", "هذه", "ذلك", "اللي", "الي", "و", "او", "ثم", "بس", "يا", "ان", "ما", "لا", "كل", "كان", "صار", "هو", "هي", "يعني"}
TAGS = {"retake": "إعادة", "stumble": "بداية متعثرة", "nospeech": "بلا كلام", "noise": "ضجيج", "filler": "حشو", "greet": "تحية بالبداية",
        "stutter": "تلعثم", "hes": "تردد", "cutoff": "جملة متروكة", "farrep": "فكرة مكررة", "fit": "للتقصير"}


def norm(w):
    w = re.sub(r"[ً-ْـ]", "", str(w))
    w = w.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ة", "ه").replace("ى", "ي")
    return re.sub(r"[^\w]", "", w).lower()


def _toks(ws): return [norm(w["t"]) for w in ws if norm(w["t"])]


def key(x):
    """جذر بسيط للمقارنة: بدون واو العطف و«ال»."""
    if len(x) > 3 and x[0] == "و": x = x[1:]
    if len(x) > 4 and x.startswith("ال"): x = x[2:]
    return x


def sim(a, b):
    """تشابه محاولتين (0 إلى 1): الكلمات المشتركة من الأقصر، أو تشابه الحروف."""
    wa, wb = [key(w) for w in a if w not in STOP], [key(w) for w in b if w not in STOP]
    if not wa or not wb: return 0.0
    shared = len(set(wa) & set(wb)) / min(len(wa), len(wb))
    return max(shared * min(1.0, min(len(wa), len(wb)) / 2.0), difflib.SequenceMatcher(None, " ".join(a), " ".join(b)).ratio())


def _prefix(a, b, need=0.7):
    """a بداية b (المتكلم بدأ الجملة ثم أعادها): أول كلمات a تطابق أول كلمات b."""
    if not a or not b or len(a) > len(b): return False
    k = len(a); same = sum(1 for x, y in zip(a, b[:k]) if x == y or (len(x) >= 2 and y.startswith(x)))
    return same / k >= need


def words_of(a_json, fixes=None):
    """كلمات whisper بوقت التسجيل الأصلي، والنص المصحح من fixes.json لو موجود وبنفس العدد."""
    out = []
    for si, seg in enumerate((a_json or {}).get("segments") or []):
        ws = seg.get("words") or []; fx = None
        if fixes and si < len(fixes.get("fix") or []) and len(fixes["fix"][si]) == len(ws): fx = fixes["fix"][si]
        for wi, w in enumerate(ws):
            t = (fx[wi] if fx else str(w.get("word", ""))).strip()
            if not t: continue
            out.append({"t": t, "s": float(w["start"]), "e": float(w["end"]), "p": float(w.get("probability", 0.8) or 0.8), "si": si, "wi": wi})
    out.sort(key=lambda w: w["s"])
    return out


def split_attempts(words, pause=PAUSE):
    att, cur = [], []
    for w in words:
        if cur:
            gap = w["s"] - cur[-1]["e"]; end = re.search(r"[.!?؟…]$", cur[-1]["t"])
            newseg = w.get("si") is not None and w.get("si") != cur[-1].get("si")   # whisper يفصل العبارات، وحدودها أدق من الوقفات
            if gap >= pause or (end and gap >= 0.15) or newseg or len(cur) >= 40: att.append(cur); cur = []
        cur.append(w)
    if cur: att.append(cur)
    return att


class Energy:
    """نسبة الصوت الفعلي داخل فترة (من شدة الصوت كل 10 جزء من الثانية)."""
    def __init__(self, db):
        self.db = db or []
        if self.db:
            s = sorted(self.db); self.floor = s[len(s) // 10]; self.thr = max(self.floor + 9.0, min(-50.0, s[int(len(s) * 0.9)] - 18.0))
        else: self.floor = self.thr = -60.0
    def voiced(self, a, b):
        if not self.db: return 1.0
        i0, i1 = max(0, int(a * 100)), min(len(self.db), max(int(a * 100) + 1, int(b * 100)))
        seg = self.db[i0:i1]; return sum(1 for v in seg if v > self.thr) / max(1, len(seg))


def refine(words, E):
    """whisper يمد وقت الكلمة على السكتة اللي بعدها، فالوقفات تختفي. نضيّق كل كلمة على صوتها الفعلي عشان تبان الوقفات."""
    if not E.db: return words
    out = []; n = len(E.db)
    for w in words:
        i0, i1 = max(0, int(w["s"] * 100)), min(n, max(int(w["s"] * 100) + 1, int(w["e"] * 100)))
        v = [k for k in range(i0, i1) if E.db[k] > E.thr]
        # نجمع الصوت لكتل (وقفة 0.15 ث تفصل)، وناخذ أكبر كتلة: بداية الكلمة اللي بعدها أحياناً تطيح داخل وقت هذي
        runs = []
        for k in v:
            if runs and k - runs[-1][1] <= 15: runs[-1][1] = k
            else: runs.append([k, k])
        if runs:
            a, b = max(runs, key=lambda r: r[1] - r[0])
            if b - a >= 4: out.append({**w, "s": round(a / 100.0, 3), "e": round((b + 3) / 100.0, 3)}); continue
        out.append(dict(w))
    return out


def scan(words, db=None, total=None):
    """يرجّع قائمة المحاولات بوسومها ومجموعات الإعادة والاختيار المبدئي."""
    E = Energy(db); words = refine(words, E); att = split_attempts(words); items = []
    for i, ws in enumerate(att):
        tk = _toks(ws); txt = " ".join(w["t"] for w in ws); s, e = ws[0]["s"], ws[-1]["e"]
        it = {"id": str(i + 1), "s": round(s, 3), "e": round(e, 3), "text": txt, "n": len(tk), "p": round(sum(w["p"] for w in ws) / len(ws), 2),
              "v": round(E.voiced(s, e), 2), "tags": [], "drop": False, "why": "", "trims": []}
        nt = " " + " ".join(tk) + " "
        if any(" " + " ".join(norm(x) for x in h.split()) + " " in nt for h in HALLU) or it["v"] < 0.12: it["tags"].append("nospeech")
        elif tk and all(x in HES for x in tk): it["tags"].append("filler")
        elif len(tk) <= 2 and (((e - s) < 0.6 and it["p"] < 0.2) or ((e - s) < 0.9 and re.search(r"(\.\.|…|ـ|-)$", txt))): it["tags"].append("noise")   # الأسماء النادرة ثقة whisper فيها قليلة، فنشترط إنها قصيرة جداً
        if s < 10.0 and i <= 2 and any(" " + " ".join(norm(x) for x in g.split()) in nt for g in GREET) and len(tk) <= 8: it["tags"].append("greet")
        items.append(it); it["_w"] = ws; it["_t"] = tk
    # بداية متعثرة: بدأها وتركها ثم أعادها مباشرة (المحاولة الأولى أقصر وبداية اللي بعدها)
    for i, it in enumerate(items):
        if it["tags"]: continue
        for j in range(i + 1, min(len(items), i + 4)):
            nx = items[j]
            if nx["s"] - it["e"] > 6.0: break
            if nx["tags"] and "greet" not in nx["tags"]: continue
            if len(it["_t"]) < len(nx["_t"]) and len(it["_t"]) <= 8 and _prefix(it["_t"], nx["_t"]):
                it["tags"].append("stumble"); it["drop"] = True; it["why"] = "بدأتها وأعدتها"; break
    # مجموعات الإعادة: نفس الجملة أكثر من مرة خلال 40 ث
    par = list(range(len(items)))
    def root(x):
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    content = lambda t: [x for x in t if x not in STOP and len(x) >= 2]
    for i, a in enumerate(items):
        ca = content(a["_t"])
        if a["tags"] or len(ca) < 2: continue
        for j in range(i + 1, min(len(items), i + 7)):
            b = items[j]; cb = content(b["_t"]); near = j - i <= 3 and b["s"] - a["e"] <= 15
            if b["s"] - a["e"] > 40: break
            if b["tags"] or len(cb) < 2: continue
            r = sim(a["_t"], b["_t"])
            restart = ca[:2] == cb[:2] or (min(len(a["_t"]), len(b["_t"])) >= 3 and a["_t"][:3] == b["_t"][:3])   # بدأ الجملة نفسها من جديد
            if (near and (restart or r >= 0.8)) or r >= 0.92: par[root(j)] = root(i)
            elif len(cb) >= 2: break   # بينهم كلام ثاني: هذا تكرار مقصود أو فكرة ثانية، مو إعادة (Claude يحكم عليه من القائمة الكاملة)
    G = {}
    for i in range(len(items)): G.setdefault(root(i), []).append(i)
    groups = []
    for g in G.values():
        if len(g) < 2: continue
        g.sort(); gid = "g%d" % (len(groups) + 1); mx = max(items[i]["n"] for i in g)
        pick = g[best_take([items[i] for i in g])]
        for i in g:
            items[i]["group"] = gid
            if i != pick: items[i]["tags"].append("retake"); items[i]["drop"] = True
        why = "آخر محاولة كاملة" if pick == g[-1] else ("الأنظف: أقل تأتأة وحشو" if items[pick]["n"] >= 0.8 * mx else "الأكمل")
        items[pick]["why"] = why; items[pick]["chosen"] = True
        groups.append({"id": gid, "items": [items[i]["id"] for i in g], "pick": items[pick]["id"], "by": "auto", "why": why})
    # المحذوف مبدئياً: بلا كلام، ضجيج، حشو (التحية اقتراح بس)
    for it in items:
        if any(t in it["tags"] for t in ("nospeech", "noise", "filler")): it["drop"] = True; it["why"] = it["why"] or TAGS[it["tags"][0]]
    # جملة متروكة: آخرها «..» أو «…» واللي بعدها تبدأ بكلمة منها (اقتراح، Claude يقرر)
    for i, it in enumerate(items[:-1]):
        if it["drop"] or it.get("group"): continue
        nx = items[i + 1]
        if re.search(r"(\.\.|…|-)$", it["text"]) and nx["s"] - it["e"] < 3 and set(it["_t"][:3]) & set(nx["_t"][:4]): it["tags"].append("cutoff")
    # داخل الجملة الباقية: التلعثم والتردد
    for it in items:
        if it["drop"]: continue
        it["trims"] = stutters(it["_w"], it["id"])
    for it in items: it.pop("_w", None); it.pop("_t", None)
    return {"v": 1, "items": items, "groups": groups}


# 4.70: كلمات كاملة قصيرة تبدأ فيها كلمة ثانية («كل كلمة»، «من منا»، «لا لازم»، «ان انا»): مو تلعثم وما تنقص
FULLW = set("كل من في لا ان انا هو هي ما يا لو مع عن قد كم لم لن اي ذا هذا هذي هذه الي اللي بس او ثم يعني عشان علي على الى الا وش شو ليش كيف متى وين لين منا منه منها له لها لك لي بي به بها فيه فيها هم هن احنا نحن انت انتم كان صار".split())
def best_take(cands):
    """4.70: الإعادة الأنظف مو الأخيرة: الكلام الفعلي (بدون الحشو والكلمات المتلعثمة) لازم 80% من أكملها، وبعدها الأعلى:
    الاكتمال والوضوح، ناقص الحشو والتلعثم والتردد (وقفات 0.25 إلى 0.45 ث بنص الجملة)، وميزة صغيرة للأخيرة. يرجع رقمها بالقائمة."""
    def parts(it):
        ws_ = it.get("_w") or []; fl = sum(1 for w in ws_ if norm(w["t"]) in HES); st = sum(len(str(c.get("text", "")).split()) for c in stutters(ws_, "x") if c.get("kind") == "stutter")
        hz = sum(1 for a, b in zip(ws_, ws_[1:]) if 0.25 < b["s"] - a["e"] <= 0.45); return max(0, it["n"] - fl - st), fl, st, hz
    P = [parts(it) for it in cands]; mx = max([p[0] for p in P] + [1]); last = len(cands) - 1
    ok = [i for i, it in enumerate(cands) if P[i][0] >= 0.8 * mx and it["p"] >= 0.45]
    if not ok: return max(range(len(cands)), key=lambda i: (cands[i]["n"], i))
    return max(ok, key=lambda i: (45 * P[i][0] / mx + 25 * cands[i]["p"] - 6 * P[i][1] - 5 * P[i][2] - 4 * P[i][3] + (3 if i == last else 0), i))
def frag(w, x, y):
    """الكلمة الأولى قطعة مبتورة من الثانية؟ («ك… كلمة»، «الكتا… الكتاب»). الكلمة الكاملة الشائعة ما تنحسب."""
    if not x or not y.startswith(x) or len(y) - len(x) < 1 or x in FULLW: return False
    return len(x) <= 3 or str(w.get("t", "")).endswith(("..", "…", "-", "ـ")) or (w.get("p") is not None and w.get("p") < 0.4)
def stutters(ws, pid="0"):
    """التلعثم داخل المحاولة: كلمة أو كلمتين أو ثلاث تتكرر بعد تردد (وقفة صغيرة، كلمة مقطوعة، «آ» بينهم)، و«آ امم» بنص الكلام.
    التكرار السلس للتأكيد («قوية قوية»، «خلصنا خلصنا منها») ما ينقص."""
    tk = [norm(w["t"]) for w in ws]; out = []; used = set(); n = len(ws)
    # تردد بنص الكلام
    for i, x in enumerate(tk):
        if x in HES and i not in used:
            a = ws[i - 1]["e"] if i > 0 else ws[i]["s"] - 0.03; b = ws[i + 1]["s"] if i + 1 < n else ws[i]["e"] + 0.03
            out.append({"kind": "hes", "s": round(max(a, ws[i]["s"] - 0.12), 3), "e": round(min(b, ws[i]["e"] + 0.12), 3), "text": ws[i]["t"]}); used.add(i)
    # تكرار بعد تردد (نتجاهل «آ امم» بين النسختين، ونقص من أول النسخة الأولى لين تبدأ الثانية)
    idx = [k for k in range(n) if tk[k] and tk[k] not in HES]; p = 0; cuts = []
    while p < len(idx):
        hit = False
        for L in (3, 2, 1):
            if p + 2 * L > len(idx): continue
            A, B = idx[p:p + L], idx[p + L:p + 2 * L]
            same = all(tk[x] == tk[y] or frag(ws[x], tk[x], tk[y]) for x, y in zip(A, B))
            if not same: continue
            gap = ws[B[0]]["s"] - ws[A[-1]]["e"]
            cut = ws[A[-1]]["t"].endswith(("..", "…", "-", "ـ")) or any(tk[x] != tk[y] for x, y in zip(A, B)) or ws[A[-1]]["p"] < 0.4
            hes_between = B[0] - A[-1] > 1
            if gap >= (0.12 if p == 0 else 0.2) or cut or hes_between:
                cuts.append({"kind": "stutter", "s": round(ws[A[0]]["s"] - 0.02, 3), "e": round(ws[B[0]]["s"] - 0.03, 3), "text": " ".join(w["t"] for w in ws[A[0]:B[0]])})
                p += L; hit = True; break
        if not hit: p += 1
    out = [h for h in out if not any(c["s"] <= h["s"] and h["e"] <= c["e"] + 0.15 for c in cuts)] + cuts
    out.sort(key=lambda x: x["s"])
    for k, t in enumerate(out): t["id"] = "%s.%d" % (pid, k + 1); t["drop"] = True
    return out


def drops(data, db=None, quiet=None):
    """فترات الحذف بوقت التسجيل الأصلي: المحاولات المحذوفة (من نص الوقفة قبلها لنص الوقفة بعدها) والتلعثم داخل الباقية."""
    if quiet is None:
        try:
            import cutmap
            quiet = cutmap.quiet_point
        except Exception: quiet = None
    items = data.get("items") or []; out = []
    for k, it in enumerate(items):
        prev_e = items[k - 1]["e"] if k > 0 else max(0.0, it["s"] - 0.6)
        next_s = items[k + 1]["s"] if k + 1 < len(items) else it["e"] + 0.6
        if it.get("drop"):
            a = max(prev_e, it["s"] - 0.35); b = min(next_s, it["e"] + 0.35)
            if quiet and db: a = quiet(db, a, it["s"]); b = quiet(db, it["e"], b)
            out.append([round(min(a, it["s"]), 3), round(max(b, it["e"]), 3)])
        else:
            for t in it.get("trims") or []:
                if t.get("drop"): out.append([t["s"], t["e"]])
    out.sort(); merged = []
    for a, b in out:
        if b - a < 0.03: continue
        if merged and a <= merged[-1][1] + 0.02: merged[-1][1] = max(merged[-1][1], b)
        else: merged.append([a, b])
    return merged


def subtract(keep, rngs, min_part=0.12):
    out = []
    for a, b in keep:
        parts = [[a, b]]
        for x0, x1 in rngs:
            o = []
            for x, y in parts:
                if x1 <= x or x0 >= y: o.append([x, y]); continue
                if x0 > x: o.append([x, x0])
                if x1 < y: o.append([x1, y])
            parts = o
        out += parts
    return [[round(a, 6), round(b, 6)] for a, b in out if b - a >= min_part]


def missing(keep_a, keep_b):
    """اللي موجود بـ keep_a ومو موجود بـ keep_b (بوقت الأصل)."""
    return [x for x in subtract(keep_a, keep_b, 0.0) if x[1] - x[0] > 0.02]


def summary(data, raw=None, kept=None):
    it = data.get("items") or []
    c = lambda tag: sum(1 for x in it if tag in x.get("tags", []) and x.get("drop"))
    nt = sum(1 for x in it for t in x.get("trims") or [] if t.get("drop"))
    parts = []
    if c("retake"): parts.append("%d إعادة" % c("retake"))
    if c("stumble"): parts.append("%d بداية متعثرة" % c("stumble"))
    if nt: parts.append("%d تلعثم وتردد داخل الجمل" % nt)
    if c("nospeech"): parts.append("%d جملة اخترعها التفريغ" % c("nospeech"))
    if c("noise") + c("filler"): parts.append("%d ضجيج وحشو" % (c("noise") + c("filler")))
    return "شلت: " + "، ".join(parts) if parts else "ما لقيت إعادات ولا تلعثم."
