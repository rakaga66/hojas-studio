# -*- coding: utf-8 -*-
"""قص السكتات + زوم مختلف لكل مقطع + تدرّج دافئ.  python3 03_cut_zoom.py <workdir>"""
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
import json, subprocess, sys, os
W=os.path.abspath(sys.argv[1]); SRC=os.path.join(W,"src.mov")
_cj=json.load(open(os.path.join(W,"cut.json"))); k=_cj["keep"]
if _cj.get("base") and os.path.isfile(os.path.join(W,_cj["base"])):   # 4.54: فيه مقاطع مضافة بزر +: الأصل هو base، مو src.mov
    _b=os.path.join(W,_cj["base"]); _ha="audio" in subprocess.run(["ffprobe","-v","error","-show_entries","stream=codec_type","-of","csv=p=0",_b],capture_output=True,text=True).stdout
    _fc=[]; _in=""
    for _i,(_a,_e) in enumerate(k):
        _fc.append("[0:v]trim=start=%.4f:end=%.4f,setpts=PTS-STARTPTS[v%d]"%(_a,_e,_i)); _in+="[v%d]"%_i
        if _ha: _fc.append("[0:a]atrim=start=%.4f:end=%.4f,asetpts=PTS-STARTPTS[a%d]"%(_a,_e,_i)); _in+="[a%d]"%_i
    _fc.append("%sconcat=n=%d:v=1:a=%d[v]%s"%(_in,len(k),1 if _ha else 0,"[a]" if _ha else ""))
    subprocess.run(["ffmpeg","-v","error","-y","-i",_b,"-filter_complex",";".join(_fc),"-map","[v]"]+(["-map","[a]","-c:a","aac","-b:a","192k"] if _ha else [])+["-c:v","libx264","-preset","veryfast","-crf","17","-pix_fmt","yuv420p","-r","30","-movflags","+faststart",os.path.join(W,"cutz.mp4")],check=True)
    print("cutz.mp4 من الأصل المضاف (%d قطعة)"%len(k)); sys.exit(0)
# 4.7.1: حدود كل جزء على فريم بالضبط. قبل كان كل جزء يطلع أطول أو أقصر من صوته بجزء من فريم، ومع 100 قطعة
# يتراكم الفرق وتتأخر حركة الفم عن الصوت. الحين الصوت والصورة نفس الطول بالضبط بكل جزء.
from fractions import Fraction as _Fr
def _fps():
    try:
        r=subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=r_frame_rate","-of","csv=p=0",SRC],capture_output=True,text=True).stdout.strip().split("\n")[0]
        f=_Fr(r); return f if 10<=f<=121 else _Fr(30)
    except Exception: return _Fr(30)
_F=_fps()
def _snap(t): return float(round(_Fr(t).limit_denominator(100000)*_F)/_F)
k=[[_snap(s),_snap(e)] for s,e in k]; k=[x for x in k if x[1]-x[0]>=1.0/float(_F)]
_tp=os.path.join(W,"theme.json")
_th=json.load(open(_tp)) if os.path.exists(_tp) else {}
GRADE=_th.get("grade",False)
# 🆕 v2.5 إيقاع «هادي» (theme.json ← "pace":"calm"): زوم أخف وأقل، وما يتغيّر قبل ما تمر 4 ثوانٍ
#    على نفس اللقطة — القطعات الكثيرة كانت تزعج (بلاغ المستخدم ٣ سبتمبر). الافتراضي زي ما هو.
CALM=str(_th.get("pace","")).lower()=="calm"
Z=([1.00,1.00,1.04,1.00,1.00,1.06,1.00,1.03] if CALM
   else [1.00,1.08,1.00,1.06,1.00,1.12,1.04,1.14,1.00,1.08,1.00,1.05,1.10,1.00]); ANCH=0.30
MINHOLD=4.0 if CALM else 0.0
# 4.27: مكان الفيديو بالكادر يحدده هو من الاستوديو (studio.json ← hs.vpos): x مكان القص بالعرض، y بالطول، z تكبير، still بدون زوم متغيّر
try: _FR=(json.load(open(os.path.join(W,"studio.json"))).get("hs") or {}).get("vpos") or {}
except Exception: _FR={}
FZ=max(1.0,min(3.0,float(_FR.get("z") or 1.0))); FX=_FR.get("x")
if _FR.get("still"): Z=[1.00]
if _FR.get("y") is not None: ANCH=max(0.0,min(1.0,float(_FR["y"])))
print("الإيقاع:", "هادي (زوم أخف · لا تغيير قبل 4 ثوانٍ)" if CALM else "عادي")
p=subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-show_entries",
   "stream=width,height","-of","csv=p=0:s=x",SRC],capture_output=True,text=True).stdout.strip()
SW,SH=[int(x) for x in p.split("x")[:2]]
# 4.5: فيديو عرضي (بودكاست/مقابلة): نقص عمودي 9:16 على اللي يتكلم بدل ما نمطّ الصورة. 22_reframe.py يحسب المكان.
WIDE=SW/max(1,SH)>0.75
RK=[]
if WIDE:
    _rp=os.path.join(W,"reframe.json")
    if not os.path.exists(_rp) or os.path.getmtime(_rp)<os.path.getmtime(SRC):
        subprocess.run([sys.executable,os.path.join(os.path.dirname(os.path.abspath(__file__)),"22_reframe.py"),W])
    try: RK=json.load(open(_rp)).get("keys") or []
    except Exception: RK=[]
    if RK:   # نقسم أي جزء يمر فيه تبديل متكلم
        _sw=[t for t,_ in RK[1:]]; _k2=[]
        for s,e in k:
            cut=[t for t in _sw if s+0.3<t<e-0.3]
            for t in cut: _k2.append([s,t]); s=t
            _k2.append([s,e])
        k=_k2
    print("فيديو عرضي: قص عمودي", "يتبع المتكلم" if len(RK)>1 else "على الشخص")
    k=[[_snap(s),_snap(e)] for s,e in k]
def _cx(t):
    c=0.5
    for kt,kc in RK:
        if kt<=t+0.01: c=kc
    return c
fc=[];v=[];a=[]
zi=0; held=0.0
for i,(s,e) in enumerate(k):
    # بالوضع الهادي: نفس الزوم يستمر لين تتجمّع 4 ثوانٍ، ثم ينتقل للي بعده
    if i and (not CALM or held>=MINHOLD): zi+=1; held=0.0
    held+=(e-s)
    z=Z[zi%len(Z)]
    if WIDE:
        bw=SH*9/16; cw=int(bw/(z*FZ))//2*2; ch=int(SH/(z*FZ))//2*2
        _c=float(FX) if FX is not None else _cx((s+e)/2)
        x=int(max(0,min(SW-cw,_c*SW-cw/2)))//2*2; y=int((SH-ch)*ANCH)
    else:
        cw=int(SW/(z*FZ))//2*2; ch=int(SH/(z*FZ))//2*2
        x=int(max(0,min(SW-cw,(float(FX) if FX is not None else 0.5)*SW-cw/2)))//2*2; y=int((SH-ch)*ANCH)
    _h=0.5/float(_F)   # نص فريم قبل الحد: كل جزء ياخذ فريماته بالضبط مهما كان تقريب الأرقام
    fc.append(f"[0:v]trim=start={max(0.0,s-_h):.6f}:end={e-_h:.6f},setpts=PTS-STARTPTS,crop={cw}:{ch}:{x}:{y},"
              f"scale=1080:1920:flags=lanczos,setsar=1[v{i}]")
    # تلاشي 12 جزء من الثانية أول وآخر كل لقطة: بدونه يطلع «تك» أو قطع بالصوت عند كل قصة
    _d=max(0.0,(e-s)-0.012)
    fc.append(f"[0:a]atrim=start={s:.6f}:end={e:.6f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.012,afade=t=out:st={_d:.4f}:d=0.012[a{i}]")
    v.append(f"[v{i}]"); a.append(f"[a{i}]")
fc.append("".join(v)+f"concat=n={len(k)}:v=1:a=0[vc]")
fc.append("".join(a)+f"concat=n={len(k)}:v=0:a=1[ac]")
# التدرّج اللوني اختياري تماماً — الافتراضي مطفي (الفيديو يطلع بألوانه الأصلية)
_g = ("eq=brightness=0.015:saturation=0.96:contrast=1.05,"
      "colorbalance=rs=0.02:gs=0.005:bs=-0.02,") if GRADE else ""
# ⚠️ مصدر آيفون HDR يجي موسوماً bt2020/HLG — أي متصفح يحترم الوسم ويطلّع صورة برتقالية.
# setparams يعيد الوسم لـbt709 فتطلع الألوان طبيعية بكل مكان.
fc.append("[vc]fps=30," + _g +
          "setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709,format=yuv420p[vo]")
print("التدرّج اللوني:", "مفعّل" if GRADE else "مطفي (ألوان أصلية)")
fc.append("[ac]afade=t=in:st=0:d=0.06,dynaudnorm=f=200:g=5:p=0.9[ao]")
# 🎨 هوجاس (8 سبتمبر): «صفر تعديل لوني». فيديو الآيفون يجي HDR (HLG/Dolby Vision) وتحويله الساذج لـSDR يغيّر الألوان
#    (باهت وبارد) — نحوّله بمكتبة أبل نفسها (AVFoundation) قبل أي شي، فيطلع بنفس مظهره على الجوال.
def _hdr_to_sdr(src):
    try:
        ct = subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=color_transfer","-of","csv=p=0",src],capture_output=True,text=True).stdout.strip().strip(",")   # ffprobe يرجّع «arib-std-b67,» بفاصلة — كانت تُسقط الكشف بصمت (13 سبتمبر)
    except Exception: return src
    if ct not in ("arib-std-b67","smpte2084"): return src
    here=os.path.dirname(os.path.abspath(__file__)); binp=os.path.join(here,"hdr2sdr")
    if not os.path.exists(binp):
        try: r=subprocess.run(["swiftc","-O","-o",binp,os.path.join(here,"hdr2sdr.swift")],capture_output=True)
        except OSError: r=None   # 4.41: ويندوز ولينكس ما فيها swiftc، كان القص يطيح كامل. الألوان تتصلّح بعدين بـ«hs hdr» على الفريمات
        if r is None or r.returncode!=0: print("⚠️ الفيديو HDR وما فيه محوّل أبل هنا. الألوان تتصلّح على الفريمات (hs hdr <work> auto)"); return src
    out=os.path.join(W,"src_sdr.mov")
    if not os.path.exists(out):
        print("🎨 الفيديو HDR — أحوّله SDR بمحوّل أبل حتى تبقى الألوان مثل الجوال…")
        r=subprocess.run([binp,src,out]); 
        if r.returncode!=0 or not os.path.exists(out): print("⚠️ فشل التحويل — أكمل بالأصل"); return src
    return out
SRC=_hdr_to_sdr(SRC)
_OUT=os.path.join(W,"cutz.mp4")
print(f"✂️  أقص وأركّب {len(k)} مقطعاً… (بلا عدّاد — سطر واحد بالنهاية)", flush=True)
_rc=subprocess.call(["ffmpeg","-v","error","-nostats","-i",SRC,"-filter_complex",";".join(fc),
 "-map","[vo]","-map","[ao]","-c:v","libx264","-preset","medium","-crf","16",
 "-c:a","aac","-b:a","192k","-movflags","+faststart","-y",_OUT])
if _rc==0:
    _d=subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",_OUT],capture_output=True,text=True).stdout.strip()
    print(f"✅ cutz.mp4 — {float(_d or 0):.2f} ث · {len(k)} مقطع")
    try:   # 4.23: الفيديو انبنى من هالقص (الاستوديو يعرض القص الفوري منه بدون ما يعيد بناءه)
        os.makedirs(os.path.join(W,".hs"),exist_ok=True); json.dump({"keep":k},open(os.path.join(W,".hs","media.json"),"w"))
    except Exception: pass
sys.exit(_rc)
