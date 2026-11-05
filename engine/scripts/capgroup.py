"""4.9: تقسيم الكابشن وكتابة الأسماء المعروفة بالإنجليزي. مشترك بين 02_captions.py و hs.py.

قاعدة الأسطر (طلب المستخدم):
- كل سطر 5 كلمات.
- لو الجملة زادت كلمة أو كلمتين: الزايد يروح لبداية الكابشن اللي بعده (ما يبقى سطر فيه كلمة لحالها).
- لو زادت 3 كلمات أو أكثر: تصير سطرين بنفس الكابشن (10 كلمات بالكثير، وأطول من كذا تنقسم).
- القطع على أنفاس الكلام: سكتة نص ثانية، نهاية جملة، أو فاصلة بعدها سكتة.
"""
import re

END = re.compile(r"[.!?؟…]$")
COMMA = re.compile(r"[،,؛;:]$")


def breaths(words, pause=0.5, comma=0.25, max_words=10, max_dur=5.0):
    groups, cur = [], []
    for w in words:
        if cur:
            p = cur[-1]; gap = w["s"] - p["e"]; t = str(p["t"]).strip()
            if gap >= pause or END.search(t) or (COMMA.search(t) and gap >= comma) or len(cur) >= max_words or (w["e"] - cur[0]["s"]) > max_dur:
                groups.append(cur); cur = []
        cur.append(w)
    if cur: groups.append(cur)
    return groups


def pack(words, wpl=5, lines=2, pause=0.5, carry_gap=1.0):
    """يرجّع قائمة مجموعات كلمات، كل مجموعة = كابشن واحد (سطر أو سطرين من wpl كلمة)."""
    cap = wpl * max(1, lines)
    groups = breaths(words, pause=pause, max_words=cap)
    out, carry = [], []
    for gi, g in enumerate(groups):
        if carry:
            if g and g[0]["s"] - carry[-1]["e"] <= carry_gap: g = carry + g
            else: out.append(carry)
            carry = []
        nxt = groups[gi + 1] if gi + 1 < len(groups) else None
        close = bool(nxt) and bool(g) and nxt[0]["s"] - g[-1]["e"] <= carry_gap
        while len(g) > cap:                       # أطول من سطرين: كابشن كامل والباقي يكمل
            out.append(g[:cap]); g = g[cap:]
        if not g: continue
        extra = len(g) - wpl
        if lines < 2 or extra <= 0: out.append(g); continue
        if extra <= 2:                            # كلمة أو كلمتين زيادة: للكابشن اللي بعده
            out.append(g[:wpl])
            if close: carry = g[wpl:]
            else: out.append(g[wpl:])
            continue
        out.append(g)                             # 3 كلمات زيادة أو أكثر: سطرين بنفس الكابشن
    if carry: out.append(carry)
    return [g for g in out if g]


def cards_of(groups, total=None):
    cards = []
    for i, g in enumerate(groups):
        s = max(0.0, g[0]["s"] - 0.08); e = g[-1]["e"] + 0.6
        if cards: s = max(s, cards[-1]["e"] + 0.02)
        if i + 1 < len(groups): e = min(e, groups[i + 1][0]["s"] - 0.05)
        if total: e = min(e, total)
        cards.append({"s": round(min(s, g[0]["s"]), 3), "e": round(max(e, g[-1]["e"]), 3), "w": g})
    for i in range(len(cards) - 1):
        if cards[i]["e"] > cards[i + 1]["s"] - 0.02: cards[i]["e"] = round(max(cards[i]["w"][-1]["e"], cards[i + 1]["s"] - 0.02), 3)
    return cards


# ── الأسماء المعروفة تنكتب بالإنجليزي ──
# المفتاح بدون "ال" وبدون همزات، والقيمة اسمه المعروف. الأسماء اللي تتكون من كم كلمة تنكتب بمسافات.
NAMES = {
    "كلود": "Claude", "انثروبيك": "Anthropic", "انثروبك": "Anthropic", "هايكو": "Haiku", "سونيت": "Sonnet", "سونت": "Sonnet",
    "اوبوس": "Opus", "اوبس": "Opus", "فيبل": "Fable", "ميثوس": "Mythos", "كلود كود": "Claude Code",
    "شات جي بي تي": "ChatGPT", "تشات جي بي تي": "ChatGPT", "شات جبت": "ChatGPT", "شات جيبيتي": "ChatGPT", "شاتجبت": "ChatGPT", "جي بي تي": "GPT",
    "اوبن اي اي": "OpenAI", "اوبن ايه اي": "OpenAI", "اوبن اية اي": "OpenAI", "كودكس": "Codex", "سورا": "Sora",
    "جيميناي": "Gemini", "جيميني": "Gemini", "جمناي": "Gemini", "جميناي": "Gemini", "قوقل": "Google", "جوجل": "Google", "غوغل": "Google",
    "جوجل درايف": "Google Drive", "قوقل درايف": "Google Drive", "درايف": "Drive", "جيميل": "Gmail", "جي ميل": "Gmail",
    "يوتيوب": "YouTube", "تيك توك": "TikTok", "تيكتوك": "TikTok", "انستقرام": "Instagram", "انستغرام": "Instagram", "انستا": "Instagram",
    "سناب شات": "Snapchat", "سناب": "Snapchat", "تويتر": "Twitter", "واتساب": "WhatsApp", "واتس اب": "WhatsApp", "تيليجرام": "Telegram", "تلقرام": "Telegram",
    "ميتا": "Meta", "فيسبوك": "Facebook", "لينكدان": "LinkedIn", "لينكد ان": "LinkedIn", "مايكروسوفت": "Microsoft", "كوبايلوت": "Copilot",
    "ايفون": "iPhone", "ايباد": "iPad", "ماك بوك": "MacBook", "سامسونج": "Samsung", "نتفلكس": "Netflix", "امازون": "Amazon",
    "تسلا": "Tesla", "انفيديا": "Nvidia", "اكس اي": "xAI", "جروك": "Grok", "قروك": "Grok", "ديب سيك": "DeepSeek", "بيربلكسيتي": "Perplexity",
    "ميسترال": "Mistral", "ميدجورني": "Midjourney", "هيقزفيلد": "Higgsfield", "هيغزفيلد": "Higgsfield", "رن واي": "Runway", "ران واي": "Runway",
    "كلينق": "Kling", "كلينج": "Kling", "اليفن لابز": "ElevenLabs", "كانفا": "Canva", "نوشن": "Notion", "فيقما": "Figma", "فيجما": "Figma",
    "كاب كت": "CapCut", "كابكت": "CapCut", "فاينل كت": "Final Cut", "بريمير": "Premiere", "افتر افكتس": "After Effects", "افتر افكت": "After Effects",
    "فوتوشوب": "Photoshop", "اليستريتر": "Illustrator", "باوربوينت": "PowerPoint", "سلاك": "Slack", "زابير": "Zapier",
    "جيت هب": "GitHub", "قيت هب": "GitHub", "كيرسر": "Cursor", "كيرسور": "Cursor", "ريبليت": "Replit", "لوفابل": "Lovable", "فيرسل": "Vercel",
    "سوبابيس": "Supabase", "نتلايفي": "Netlify", "بايثون": "Python", "جافاسكربت": "JavaScript", "رياكت": "React", "انتي جرافيتي": "Antigravity",
    "شوبيفاي": "Shopify", "سلة ستور": "Salla", "منصة زد": "Zid", "سبوتيفاي": "Spotify", "ديسكورد": "Discord", "ريديت": "Reddit", "بنترست": "Pinterest",
    "ايفل": "Eiffel", "برج ايفل": "Eiffel Tower", "تايمز سكوير": "Times Square", "بيق بن": "Big Ben", "هوليوود": "Hollywood", "سيليكون فالي": "Silicon Valley",
}
_PRE = ("وبال", "فبال", "وال", "بال", "فال", "كال", "لل", "ال", "و", "ب", "ل", "ف", "ك")


def _norm(s):
    s = re.sub(r"[ً-ْـ]", "", str(s))                     # تشكيل وتطويل
    s = s.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ة", "ه").replace("ى", "ي")
    return re.sub(r"[^\w\s]", "", s).strip()


_NKEYS = {}
for k, v in NAMES.items(): _NKEYS[_norm(k).replace("ه", "ه")] = v
_MAXN = max(len(k.split()) for k in _NKEYS)


def _split_prefix(tok):
    """«والسونيت» ← («و»، «سونيت»). «ال» تنشال لأن الاسم الإنجليزي ما ياخذها."""
    n = _norm(tok)
    if n in _NKEYS: return "", n
    for p in _PRE:
        if n.startswith(p) and _norm(n[len(p):]) in _NKEYS:
            keep = {"وبال": "وب", "فبال": "فب", "وال": "و", "بال": "ب", "فال": "ف", "كال": "ك", "لل": "ل", "ال": ""}.get(p, p)
            return keep, _norm(n[len(p):])
    return None, None


def english_names(words):
    """يمر على كلمات الكابشن ويبدّل الأسماء المعروفة باسمها الإنجليزي. الأسماء اللي من كم كلمة تندمج بكلمة وحدة بوقتها."""
    out, i, n = [], 0, len(words)
    while i < n:
        hit = None
        for L in range(min(_MAXN, n - i), 0, -1):
            toks = [str(w["t"]) for w in words[i:i + L]]
            pre, first = _split_prefix(toks[0]) if L == 1 else _split_prefix(toks[0] + " " + " ".join(toks[1:]))
            if pre is None and L > 1:
                # البادئة على أول كلمة بس: «بجوجل درايف»
                p0, f0 = None, None
                for p in _PRE:
                    n0 = _norm(toks[0])
                    if n0.startswith(p):
                        cand = _norm(n0[len(p):] + " " + " ".join(toks[1:]))
                        if cand in _NKEYS:
                            p0 = {"وبال": "وب", "فبال": "فب", "وال": "و", "بال": "ب", "فال": "ف", "كال": "ك", "لل": "ل", "ال": ""}.get(p, p); f0 = cand; break
                pre, first = p0, f0
            if pre is not None and first in _NKEYS:
                hit = (L, pre, _NKEYS[first]); break
        if hit:
            L, pre, name = hit; w0, w1 = words[i], words[i + L - 1]
            trail = re.search(r"[؟?!.،,]+$", str(w1["t"]))
            txt = (pre + " " if pre else "") + name + (trail.group(0) if trail else "")
            nw = {**w0, "t": txt, "e": w1["e"], "en": name}
            if any(x.get("hot") for x in words[i:i + L]): nw["hot"] = True
            out.append(nw); i += L
        else:
            out.append(words[i]); i += 1
    return out


def names_text(text):
    """نفس english_names على نص عادي (العنوان فوق، نصوص الطبقات)."""
    toks = str(text).split()
    if not toks: return text
    return " ".join(str(w["t"]) for w in english_names([{"t": x, "s": i, "e": i + 0.5} for i, x in enumerate(toks)]))


def gloss_file():
    import os
    return os.path.join(os.path.expanduser("~"), ".hojas-studio", "glossary.json")


def apply_gloss(words, G=None):
    """قاموس المستخدم (يتعلّم من تصحيحاته بالاستوديو): الغلط ← الصح، كلمة أو عبارة لين 3 كلمات."""
    import json, os
    if G is None:
        try: G = json.load(open(gloss_file(), encoding="utf-8")) if os.path.isfile(gloss_file()) else {}
        except Exception: G = {}
    if not G: return words
    out, i, n = [], 0, len(words)
    while i < n:
        hit = None
        for L in (3, 2, 1):
            if i + L > n: continue
            k = " ".join(_norm(w["t"]) for w in words[i:i + L])
            if k in G: hit = (L, G[k]); break
            if len(k) > 3 and k[0] == "و" and k[1:] in G: r_ = G[k[1:]]; hit = (L, ("و " if re.search(r"[A-Za-z]", r_) else "و") + r_); break
        if hit:
            L, rep = hit; w0, w1 = words[i], words[i + L - 1]; tail = re.search(r"[؟?!.،,]+$", str(w1["t"]))
            nw = {**w0, "t": rep + (tail.group(0) if tail else ""), "e": w1["e"]}; nw.pop("lo", None); out.append(nw); i += L
        else: out.append(words[i]); i += 1
    return out
