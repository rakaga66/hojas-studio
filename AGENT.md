# Hojas Studio: دليل التشغيل للوكيل، Claude Code أو OpenCode (يُحمَّل تلقائياً لما يضغط المستخدم «نفّذ» من الاستوديو)

أنت تشتغل داخل مجلد مشروع مونتاج. المستخدم يتابعك من صفحة الاستوديو في المتصفح، وكل تعديل تكتبه على ملفات المشروع يظهر عنده خلال ثانيتين بدون ما يحدّث الصفحة.

## القواعد
- عربي بسيط ومختصر. نفّذ ولا تسأل إلا لو الطلب يحتمل معنيين مختلفين فعلاً.
- قبل كل خطوة لها وقت، اكتب سطراً يراه المستخدم: `python "<studio>/hs.py" say . "وش بسوي"`.
- لا تعدّل ملفات المحرّك (مجلد engine) ولا ملفات الاستوديو. شغلك في ملفات المشروع فقط.
- لا تنشر ولا ترفع أي شي من هنا. النشر يصير من المحادثة الأساسية وبموافقة المستخدم.
- لو خلصت شي ينتظر المستخدم: `notify send "وش تحتاج منه بجملة" --work .` (يوصله على جواله لو مفعّل).
- لا تحذف ملاحظة، ولا تعلّمها «تمّت» إلا بعد ما تنفّذها فعلاً.
- على ويندوز: `python` مو `python3`.

`<studio>` و`<engine>` مساراتهم مكتوبة أول رسالة المهمة.

## الأدوات (كلها: `python "<studio>/hs.py" <أمر> .`)
| تبغى | الأمر |
|---|---|
| تشوف الجمل مرقّمة | `text . show` |
| تعدّل نص جملة | `text . 4 "النص الجديد"` |
| شكل الكابشن والترجمة والصوت | `set . cap.size=70 cap.y=72 cap.font=Tajawal cap.enter=pop en.size=40 mix.voice=1.2` |
| الترجمة الإنجليزية | `tr . export` ثم اكتب `en.json` بشكل `[{"i":0,"en":"…"}]` ثم `tr . import en.json` |
| طبقة (نص · صورة · شخصية · مؤثر) | `layer . add type=text text="عنوان" s=1.2 e=4 x=0.5 y=0.25 size=96 bg=pill bgColor="#D2558F" anim=pop` |
| | `layer . add type=char char=robo s=0 e=20 x=0.2 y=0.62 size=0.26 color="#8F73F5"` |
| | `layer . add type=fx fx=punch s=6.1 e=7.4 amount=0.7` |
| | `layer . list` · `layer . set L3 y=0.4` · `layer . rm L3` |
| صيغ الهوك | `hook . set "صيغة 1" "صيغة 2" "صيغة 3"` · `hook . active 2` |
| فحص الاحتفاظ والحشو والإعادات ومدة المقطع مقابل منصاته | `check .` |
| تقص من الفيديو والصوت | `remove . --cards 3 7` · `remove . --ranges 4.2-5.1` · `remove . --fillers` |
| الملاحظات | `notes . list` ثم لكل وحدة `notes . done <id> "وش سويت"` |
| ملاحظة صوتية | فيها `audio`. لو نصها «ما قدرت أفرّغها» فرّغ الملف بوِسبر قبل التنفيذ |
| حلقة طويلة | اقرأ `<engine>/references/clips.md` ثم `clips scan` (يرشّح لحاله) · `clips cand <مجلد> list` · `cand <مجلد> set c3 --score 88 --why "…\|…" --title "…"` · `clips build <مجلد> --picks c1,c3 --edit none` |
| وين قال كلام معيّن (كل مقاطعه) | `db search "كلمة"` (بلا مجلد) |
| فيديو من رابط | `grab "<الرابط>" --mode clips\|manual\|auto` (لو yt-dlp مو مثبّت استأذنه أول) |
| رسم حر | `layer . add type=draw pts='[[0.3,0.3],[0.6,0.3],null,[0.4,0.6],[0.6,0.6]]' color="#FFD21F" lw=12 reveal=0.9 s=4 e=7` |
| ملاحظة منك له | `notes . add <ثانية> "اقتراح" [--kind question\|info]`، ولا تنفّذ قبل رده |
| إجاباته | `brief . check` لازم يطلع كله ✓ قبل التسليم. البند اليدوي: `brief . ok <رمز> "وش سويت"` |
| صور حقيقية برخص حرّة | `media . search "World War II"` ثم `media . add 2 --at 12.4 --dur 3 --fit card` (أو `cover` ملء الشاشة) |
| توليد صورة أو مقطع من حسابه (بلا مفاتيح API) | `gen . request image "وصف بالإنجليزي" --at 12.4` · `gen . request video "وصف" --at 20` · `gen . list` · `gen . import <رقم> <ملف>` |
| وش تحتاج كل منصة | `platform tiktok instagram x linkedin` (بلا مجلد) |
| المقاس | `set . frame.ar="4:5"` (9:16 · 4:5 · 1:1 · 16:9) · `set . frame.cy=0.47` مكان القص · `export . --frame 1:1` |
| تقريب وانتقالات تلقائية | `auto . zooms` · `auto . transitions` · `auto . clear zooms` |
| مكان أو شكل جملة وحدة فقط | `studio.json ← hs.capOv["نص الجملة"] = {"y":30,"size":80,"color":"#FFE14D"}` |
| التصدير النهائي | `export .` (`--clean` بلا كابشن · `--hooks` نسخة لكل هوك) |
| حزمة النشر | `pack .` |
| خط كرت الختام ونصوصه | `set . outro.font="Lalezar" outro.cta="تابعني"` |
| أسلوب المستخدم المتعلَّم | `style show` (بلا مجلد) |
| ورق متحرك (اقرأ engine/references/styles.md) | `kinetic . auto --deco both` · `layer . set L12 text="سطر\n* كبير\n> صندوق" card=pill cardText="…"` |
| موشن جرافيك (اقرأ engine/references/motion-graphics.md كامل) | القالب من جدول قسم 3 (مقاطع حسابه MG-05)، وأوامر «البناء بـ hs» فيه، وفحص قسم 7 قبل ما تقول خلصت، والصفحة الفاضية بقسم 6. أساسي لأي طلب حركة، إلا لو قال ثابت |
| هويته (اقرأ engine/references/identity.md) | `identity show` (بلا مجلد) قبل أي تصميم · `identity apply .` · لو مسودة: اكتب identity.md ثم `identity check <الاسم>` |
| الدحيح (اقرأ engine/references/styles.md) | `dahih . on --title "…" --tag "#…"` · `dahih . bg navy --at 20` · `layer . add type=desk kind=number n=24 sub="ساعة متاح" s=6 e=9 x=0.3 y=0.45` |

القيم المتاحة:
- `cap.enter`: rise · pop · slide · drop · zoom · fade · words · none
- `cap.bg`: none · box · lines (كل سطر بكرته) · bar (شريط بعرض الشاشة) · pill ، ولون الكرت `cap.bgColor` وشفافيته `cap.bgOpacity`
- `cap.hl` تمييز الكلمة المنطوقة: color · under (خط تحتها) · dim (الباقي باهت لين ينقال) · `cap.chunk` كم كلمة تظهر مع بعض (0 = الجملة كاملة، 1 إلى 4) · `cap.actScale` تكبير المنطوقة (1 إلى 1.5) · `cap.fill`: solid · outline · `cap.shadow`: true · false · "hard" مع `cap.shadowColor`
- `anim` للطبقات: pop · rise · drop · slide · slideL · zoom · fade · type · none
- `char`: robo · sprout · star · cube ، أو صورة: `src="assets/اسم.png"`
- `fx`: zoom · punch · shake · flash · bw · blur · vignette · letterbox · tint · glitch · grain
- المواقع `x` و`y` نسبة من 0 إلى 1 من الشاشة (1080×1920). الأزمنة بالثواني على زمن الإخراج.

كل هذا محفوظ في `studio.json ← hs`، وتقدر تعدّله مباشرة لو الأمر ما يغطي اللي تبغاه.

## لما الطلب مونتاج أعمق (مشهد موشن، بي-رول، مؤثر صوتي)
استخدم أدوات المحرّك: `compose.html` (المشاهد)، `sfx.json` (المؤثرات الصوتية)، وسكربتات `<engine>/scripts/`. اقرأ `<engine>/MONTAGE.md` قبلها.

## بعد أي تعديل بصري
عاين برسم حقيقي قبل ما تقول خلصت:
`node "<engine>/scripts/04_render_frames.js" . preview <وقت> <وقت> <وقت>` ثم اقرأ الصور في `prev/`.
الاستوديو يعرض آخر معاينة للمستخدم تلقائياً.

## المنصات والمقاس
- المنصات المختارة في `studio.json ← hs.platforms` والمقاس في `hs.frame`. قبل أي تعديل على مكان نص أو كابشن شغّل `platform <المنصات>` والتزم بالحدود.
- المونتاج دايماً عمودي 1080×1920. المقاسات الثانية تطلع وقت التصدير: 4:5 و1:1 قص من فوق وتحت (خلّ كل شي مهم داخل الحزام اللي يطبعه `brief apply`)، و16:9 المقطع بالنص وخلفية مغبّشة.
- لو المنصات فيها إكس والمقطع أطول من 140 ثانية نبّهه.

## الطلبات اللي تحتاج أدوات خارجية
- توليد صورة أو مقطع: بلا مفاتيح API أبداً. `gen . list` يعطيك النص الجاهز لكل طلب ينتظر. لو عندك أدوات المتصفح: افتح ChatGPT للصور أو Gemini للمقاطع (المستخدم مسجّل دخوله)، الصق النص، انتظر، نزّل الناتج، ثم `gen . import <رقم> <مسار الملف>`. لو ما عندك متصفح وعندك موصل التوليد المربوط بحسابه استخدمه واحفظ الناتج ثم `gen . import`. لو ما عندك ولا واحد قل له بجملة وحدة وخلّ الطلب ينتظر (يقدر يولّده بنفسه من زر «افتح» ثم «ارفع الناتج»).
- الصور الحقيقية: استعلام البحث بالإنجليزي وبكلمات بسيطة. الرخص الحرّة فقط، والمصدر ينحفظ تلقائياً.
- دبلجة إنجليزية: تحتاج موصل Higgsfield وتكلّف رصيد.
- نص البوست والهاشتاقات: اكتبه في `post.txt` بمجلد المشروع، يظهر عنده في تبويب المشروع. اكتبه بأسلوب المنصة المختارة.

- كرت شرح (الشرح المتحرك فوق والمتحدث تحت): `python hs.py layer <work> add type=split style=list|steps|flow|versus|stat|check|timeline|funnel|quote|draw title="…" "text=سطر\nسطر" s=<ث> e=<ث>`. تفاصيل كل شكل والرسم الحر في SKILL.md قسم «كروت الشرح». ارسم معاينة بعد كل كرت.
- خلفية المتحدث: `layer <work> add type=bg mode=blur|bw|dim|color|grad|studio|image s= e=` · نص خلف الشخص: `type=behind text="…"`. القص ينبني لحاله.
- أصوات المستخدم تطلع آخر `sfx <work> list` بأرقام `my1`… وتنضاف مثل المكتبة. قدّمها لما تناسب.
- لا تثبّت أي أداة بدون ما تشرح له وش هي وليش (`python hs.py tools`) وتاخذ موافقته.

- مكتبة الأصوات (30 صوت): `python hs.py sfx <work> list` ثم `python hs.py sfx <work> add <id> <ثانية>` · حذف: `sfx <work> rm <id> <ثانية>`.

- حركات أرقام: `layer add type=viz kind=pctdots|people|fill|bars|route|cta …` · شاشة كلمة: `type=cover text="…"` · نص قزاز: `type=text bg=glass` · إطار صورة: `frame=glass|ring|browser|post` · لقطة موقع: `python hs.py shot <work> <رابط> --at <ث>` · مقاطع حقيقية: `python hs.py media <work> search "…" --video` ثم `media <work> add <رقم> --at <ث>`.
- 4.5: المستخدم يهمه حدّه في Claude. لا تسوي بنفسك شي الأداة تسويه بدون Claude (`hs retention`، الإعادات، الأغلفة، نصوص النشر بـ`repurpose.json`). خلّ ردك قصير وشغلك أقل شي يكفي.
