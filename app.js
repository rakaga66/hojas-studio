'use strict';
/* Hojas Studio 2 — واجهة الاستوديو */
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const F=$('#frame'), AU=$('#au'), FPS=30;
let LANG='ar'; try{ LANG=localStorage.getItem('hsLang')||'ar'; }catch(e){} langCookie();
const t=(k,...a)=>{ const v=I18N[k]; let s=v?v[LANG==='ar'?0:1]:k; a.forEach((x,i)=>{ s=s.split('{'+i+'}').join(x); }); return s; };
let ST=null, INFO=null, NOTES=[], REV={approved:null,comments:[]}, PEAKS=null, CHECK=null;
let T=0, PX=80, playing=false, lastFrame=-1, LTAB='text', RTAB='cap', Q='', SEL=null, TOOL='select', MAG=true, SKIM=false, MARKS=[];
/* 4.14: الصوت والصورة مربوطين (تضغط وحدة يتحدد الاثنين) أو مفصولين (كل واحد لحاله). L يبدّل */
let LINK=true; try{ LINK=localStorage.getItem('hs.link')!=='0'; }catch(e){}
let ACT=[], lastAct=0, SIG=null, adoptSig=false, READY=false, PULSE={}, dragging=false, frameReady=false, auKey='';
const AR_FONTS=['Cairo','Tajawal','Vazirmatn','IBM Plex Sans Arabic','Alexandria','El Messiri','Noto Sans Arabic','Noto Kufi Arabic','Readex Pro','Almarai','Changa','Rubik','Aref Ruqaa','Lalezar','Reem Kufi','Amiri','Baloo Bhaijaan 2','Lemonada'];   // 4.47: خط Marhey انشال نهائياً
const EN_FONTS=['Inter','Poppins','Montserrat','Bebas Neue','Oswald','Space Grotesk'];
const SWATCH=['#FFFFFF','#F2B33D','#FFE14D','#111111','#FF5A4E','#43D17A','#4C8DFF','#F472B6','#8F73F5'];
const DEFCAP={on:false,font:'Cairo',weight:800,size:56,wpl:5,color:'#FFFFFF',active:'#F2B33D',bg:'none',stroke:0,strokeColor:'#000000',shadow:true,y:76,width:760,lines:2,gap:16,mode:'line',enter:'rise',bgColor:'#000000',bgOpacity:0.62,hl:'color',chunk:0,actScale:1,fill:'solid',shadowColor:'#000000'};
const DEFEN={on:false,font:'Inter',weight:700,size:40,color:'#FFFFFF',pos:'below',gap:18,map:{}};
const FXS=['confetti','zoom','punch','shake','flash','bw','blur','vignette','letterbox','tint','glitch','grain','facezoom','spotlight','pulse','tilt','rgb','vhs','pixel','duotone','sepia','invert','mirror','leak','strobe','speed'];
const BGM=['blur','bw','dim','color','grad','studio','image'];
const CARDS=['list','steps','flow','versus','stat','check','timeline','funnel','quote'];
const ANIMS=['pop','rise','drop','slide','slideL','zoom','fade','glow','type','none'];
/* 4.0: الدمج */
/* 4.15: تعليق على الصورة وحركة الصور (من مونتاج الصور التوضيحية) */
const ANK=['ring','spots','route','path','wave','tap','boxes','tags','screen','spinner','arrow','scribble','underline','highlight','cross','check','lens','spotlight','blur','bubble','frame','scan','burst','stars','price'], IMOVES=['push','pull','panL','panR','panU','panD','drift','float','none'], INFX=['','focus','zoomblur','whip','stretch'], OUTFX=['','zoomblur','whip','focus'];
const ANDEF={ring:{x:.5,y:.45,r:.08},spots:{pts:[[.3,.45],[.7,.55]],r:.07},route:{pts:[[.35,.35],[.65,.6]],labels:[]},path:{pts:[[.3,.62],[.5,.42],[.72,.5]]},wave:{y:.86,amp:.12,burst:[[0.6,1.6]]},tap:{x:.5,y:.5},boxes:{rects:[[.2,.35,.25,.13],[.55,.5,.25,.13]],tag:''},tags:{pts:[[.5,.4]],labels:['أنا']},screen:{rect:[.36,.3,.28,.36],zoom:.6,bg:'#0B0D10'},spinner:{x:.5,y:.45,r:.035},
  arrow:{pts:[[.28,.68],[.52,.46]],labels:['']},scribble:{x:.5,y:.45,r:.09},underline:{pts:[[.3,.55],[.7,.55]]},highlight:{rects:[[.25,.42,.5,.05]]},cross:{rects:[[.3,.38,.4,.2]]},check:{x:.5,y:.45,r:.07},lens:{x:.5,y:.45,r:.12,zoom:2.2},
  spotlight:{pts:[[.4,.4],[.62,.55]],r:.16,dim:.68,labels:[]},blur:{rects:[[.3,.4,.4,.06]],mode:'blur'},bubble:{x:.55,y:.5,text:'هذا هو'},frame:{rects:[[.3,.35,.4,.25]],labels:['']},scan:{rects:[[.25,.3,.5,.3]],labels:['تم']},burst:{x:.5,y:.4,r:.14,text:'واو'},stars:{x:.5,y:.4,r:.034,value:4.5},price:{x:.5,y:.3,text:'$20',len:.06}};
const ANPV={ring:'<svg viewBox="0 0 60 40"><circle cx="30" cy="20" r="11" fill="none" stroke="#F2B33D" stroke-width="3"/><circle cx="30" cy="20" r="17" fill="none" stroke="#F2B33D" stroke-opacity=".35" stroke-width="2"/><text x="6" y="27" fill="#F2B33D" font-size="16" font-weight="900">3</text></svg>',
  spots:'<svg viewBox="0 0 60 40"><circle cx="16" cy="24" r="7" fill="none" stroke="#F2B33D" stroke-opacity=".4" stroke-width="2"/><circle cx="44" cy="16" r="9" fill="none" stroke="#F2B33D" stroke-width="3"/><path d="M22 22 L36 17" stroke="#F2B33D" stroke-dasharray="2 3"/></svg>',
  route:'<svg viewBox="0 0 60 40"><path d="M12 30 Q30 2 48 26" fill="none" stroke="#F2B33D" stroke-width="2.5"/><circle cx="12" cy="22" r="4" fill="#F2B33D"/><path d="M12 22 V30" stroke="#F2B33D" stroke-width="2"/><circle cx="48" cy="18" r="4" fill="#F2B33D"/><path d="M48 18 V26" stroke="#F2B33D" stroke-width="2"/></svg>',
  path:'<svg viewBox="0 0 60 40"><path d="M8 32 Q24 6 40 20" fill="none" stroke="#F2B33D" stroke-opacity=".35" stroke-width="5" stroke-linecap="round"/><circle cx="40" cy="20" r="4.5" fill="#FFF4DC"/><path d="M40 20 L52 36" stroke="#F2B33D" stroke-dasharray="3 3"/></svg>',
  wave:'<svg viewBox="0 0 60 40"><path d="M4 20 Q10 20 14 20 T20 12 T26 28 T32 8 T38 30 T44 18 T50 20 T56 20" fill="none" stroke="#F2B33D" stroke-width="2.5"/></svg>',
  tap:'<svg viewBox="0 0 60 40"><circle cx="30" cy="20" r="6" fill="#fff" fill-opacity=".35"/><circle cx="30" cy="20" r="11" fill="none" stroke="#fff" stroke-width="2.5"/><circle cx="30" cy="20" r="17" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2"/></svg>',
  boxes:'<svg viewBox="0 0 60 40"><rect x="6" y="14" width="18" height="16" rx="2" fill="none" stroke="#F2B33D" stroke-width="2.5"/><rect x="34" y="8" width="18" height="16" rx="2" fill="none" stroke="#F2B33D" stroke-width="2.5"/><rect x="39" y="3" width="8" height="6" rx="2" fill="#F2B33D"/></svg>',
  tags:'<svg viewBox="0 0 60 40"><rect x="10" y="13" width="18" height="12" rx="4" fill="#F2B33D"/><rect x="34" y="20" width="18" height="12" rx="4" fill="#5CD6FF"/></svg>',
  screen:'<svg viewBox="0 0 60 40"><rect x="20" y="3" width="20" height="34" rx="4" fill="#0B0D10" stroke="#888" stroke-width="1.5"/><rect x="25" y="14" width="10" height="10" rx="2" fill="#F4EFE6"/></svg>',
  spinner:'<svg viewBox="0 0 60 40"><path d="M30 10 A10 10 0 1 1 20.5 23" fill="none" stroke="#F2B33D" stroke-width="3.5" stroke-linecap="round"/></svg>',arrow:'<svg viewBox="0 0 60 40"><path d="M10 32 Q22 8 46 12" fill="none" stroke="#F2B33D" stroke-width="3.5" stroke-linecap="round"/><path d="M38 6 L47 12 L39 19" fill="none" stroke="#F2B33D" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',scribble:'<svg viewBox="0 0 60 40"><path d="M18 22 C16 10 44 8 45 19 C46 30 18 33 16 22 C15 15 30 11 40 14" fill="none" stroke="#F2B33D" stroke-width="3" stroke-linecap="round"/></svg>',underline:'<svg viewBox="0 0 60 40"><rect x="14" y="12" width="32" height="7" rx="2" fill="#8d8d9b"/><path d="M12 27 Q30 23 48 27" fill="none" stroke="#F2B33D" stroke-width="4" stroke-linecap="round"/></svg>',highlight:'<svg viewBox="0 0 60 40"><rect x="12" y="15" width="36" height="10" rx="2" fill="#FFE14D" fill-opacity=".55"/><rect x="14" y="18" width="30" height="4" rx="1" fill="#8d8d9b"/></svg>',cross:'<svg viewBox="0 0 60 40"><rect x="16" y="10" width="28" height="20" rx="3" fill="#8d8d9b" fill-opacity=".5"/><path d="M16 10 L44 30 M44 10 L16 30" stroke="#E5484D" stroke-width="3.5" stroke-linecap="round"/></svg>',check:'<svg viewBox="0 0 60 40"><circle cx="30" cy="20" r="13" fill="#F2B33D" fill-opacity=".25" stroke="#F2B33D" stroke-width="2.5"/><path d="M24 20 L28.5 25 L37 15" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',lens:'<svg viewBox="0 0 60 40"><circle cx="27" cy="18" r="11" fill="#2a2a34" stroke="#FAF9F5" stroke-width="3"/><text x="27" y="23" text-anchor="middle" fill="#F2B33D" font-size="13" font-weight="900">A</text><path d="M35 26 L44 35" stroke="#F2B33D" stroke-width="4.5" stroke-linecap="round"/></svg>',spotlight:'<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#000" fill-opacity=".55"/><circle cx="34" cy="20" r="10" fill="#8d8d9b"/></svg>',blur:'<svg viewBox="0 0 60 40"><rect x="12" y="14" width="36" height="12" rx="3" fill="#8d8d9b" fill-opacity=".7"/><rect x="14" y="16" width="8" height="8" fill="#b9b9c4"/><rect x="24" y="16" width="8" height="8" fill="#6d6d7c"/><rect x="34" y="16" width="8" height="8" fill="#a3a3ae"/></svg>',bubble:'<svg viewBox="0 0 60 40"><rect x="10" y="6" width="40" height="20" rx="7" fill="#FAF9F5"/><path d="M22 25 L20 34 L30 25 Z" fill="#FAF9F5"/><rect x="16" y="13" width="22" height="3" rx="1.5" fill="#141413"/></svg>',frame:'<svg viewBox="0 0 60 40"><path d="M14 14 V8 H20 M40 8 H46 V14 M46 26 V32 H40 M20 32 H14 V26" fill="none" stroke="#F2B33D" stroke-width="3" stroke-linecap="round"/><circle cx="17" cy="4" r="2" fill="#E5484D"/></svg>',scan:'<svg viewBox="0 0 60 40"><rect x="12" y="8" width="36" height="24" rx="2" fill="none" stroke="#F2B33D" stroke-opacity=".5" stroke-width="1.5"/><path d="M12 18 H48" stroke="#F2B33D" stroke-width="3"/><rect x="12" y="13" width="36" height="5" fill="#F2B33D" fill-opacity=".25"/></svg>',burst:'<svg viewBox="0 0 60 40"><path d="M30 4 L34 13 L44 9 L40 18 L50 22 L40 25 L44 35 L34 30 L30 38 L26 30 L16 35 L20 25 L10 22 L20 18 L16 9 L26 13 Z" fill="#F2B33D" stroke="#141413" stroke-width="1.5"/></svg>',stars:'<svg viewBox="0 0 60 40"><path transform="translate(8 20)" d="M0 -6 L1.8 -1.9 L6 -1.9 L2.6 0.8 L3.7 5 L0 2.5 L-3.7 5 L-2.6 0.8 L-6 -1.9 L-1.8 -1.9 Z" fill="#F5C443" /><path transform="translate(19 20)" d="M0 -6 L1.8 -1.9 L6 -1.9 L2.6 0.8 L3.7 5 L0 2.5 L-3.7 5 L-2.6 0.8 L-6 -1.9 L-1.8 -1.9 Z" fill="#F5C443" /><path transform="translate(30 20)" d="M0 -6 L1.8 -1.9 L6 -1.9 L2.6 0.8 L3.7 5 L0 2.5 L-3.7 5 L-2.6 0.8 L-6 -1.9 L-1.8 -1.9 Z" fill="#F5C443" /><path transform="translate(41 20)" d="M0 -6 L1.8 -1.9 L6 -1.9 L2.6 0.8 L3.7 5 L0 2.5 L-3.7 5 L-2.6 0.8 L-6 -1.9 L-1.8 -1.9 Z" fill="#F5C443" /><path transform="translate(52 20)" d="M0 -6 L1.8 -1.9 L6 -1.9 L2.6 0.8 L3.7 5 L0 2.5 L-3.7 5 L-2.6 0.8 L-6 -1.9 L-1.8 -1.9 Z" fill="#F5C443" fill-opacity=".3"/></svg>',price:'<svg viewBox="0 0 60 40"><path d="M30 4 V12" stroke="#FAF9F5" stroke-width="1.5"/><path d="M25 12 H35 L40 17 V34 H20 V17 Z" fill="#F2B33D"/><text x="30" y="29" text-anchor="middle" fill="#141413" font-size="9" font-weight="900">$20</text></svg>'};
let PICK=null;
function annoInsp(L){ const k=L.kind||'ring', at=Array.isArray(L.at)?L.at:[]; let o=seg(t('akKind'),'L.kind',ANK.map(x=>[x,t('ak_'+x)]),k)+swatches(t('color'),'L.color',L.color||'#F2B33D');
  const P=(L.pts||[]), lab=L.labels||[], row=(i,txt)=>'<div class="row"><span class="t" style="direction:ltr">'+(i+1)+'</span><input type="text" data-anlab="'+i+'" dir="auto" value="'+esc(lab[i]||'')+'" placeholder="'+esc(t('akLabelPh'))+'"><button class="sm ghost" data-ancue="'+i+'" title="'+esc(t('akCueTip'))+'">'+(at[i]!=null?fmt(L.s+(+at[i])):t('akCueNow'))+'</button><button class="sm ghost" data-anrm="'+i+'">×</button></div>';
  if(k==='screen'){ const as=(INFO.assets||[]); o+='<div class="row"><label>'+t('akScreenSrc')+'</label><select data-k="L.src"><option value="">'+t('bgNone')+'</option>'+as.map(a=>'<option value="assets/'+esc(a)+'"'+(L.src==='assets/'+a?' selected':'')+'>'+esc(a)+'</option>').join('')+'</select></div>'
      +'<div class="row"><label></label><button class="sm" data-anpick="screen">'+t('akScreenPick')+'</button></div>'+slider(t('size'),'L.zoom',0.2,1.2,L.zoom||0.6,0.02)+tog('L.spin',t('akSpin'),t('akSpinSub'),!!L.spin)
      +'<div class="row"><label>'+t('akScreenText')+'</label><input type="text" data-k="L.text" dir="auto" value="'+esc(L.text||'')+'" placeholder="6"></div>'; }
  if(k==='spinner') o+=slider(t('posX'),'L.x',0,1,L.x==null?.5:L.x,0.005)+slider(t('posY'),'L.y',0,1,L.y==null?.45:L.y,0.005)+'<div class="row"><label></label><button class="sm" data-anpick="xy">'+t('akPickXY')+'</button></div>'+slider(t('size'),'L.r',0.015,0.12,L.r||0.035,0.005);
  if(['scribble','check','lens','bubble','burst','stars','price'].includes(k)){ o+=slider(t('posX'),'L.x',0,1,L.x==null?.5:L.x,0.005)+slider(t('posY'),'L.y',0,1,L.y==null?.45:L.y,0.005)+'<div class="row"><label></label><button class="sm" data-anpick="xy">'+t('akPickXY')+'</button></div>'+(k!=='bubble'&&k!=='price'?slider(t('size'),'L.r',0.02,0.25,L.r||ANDEF[k].r||0.08,0.005):'');
    if(k==='bubble'||k==='burst'||k==='price') o+='<div class="row"><label>'+t('akText')+'</label><input type="text" data-k="L.text" dir="auto" value="'+esc(L.text||'')+'"></div>'+slider(t('akTextSize'),'L.size',40,200,L.size||86,2);
    if(k==='scribble'||k==='check'||k==='lens') o+='<div class="row"><label>'+t('akLabel')+'</label><input type="text" data-k="L.label" dir="auto" value="'+esc(L.label||'')+'"></div>';
    if(k==='lens') o+=slider(t('akZoom'),'L.zoom',1.3,4,L.zoom||2.2,0.1);
    if(k==='stars') o+=slider(t('akValue'),'L.value',0,5,L.value==null?4:L.value,0.5)+'<div class="row"><label>'+t('akLabel')+'</label><input type="text" data-k="L.label" dir="auto" value="'+esc(L.label==null?'':L.label)+'" placeholder="4.5/5"></div>'; }
  if(k==='ring'||k==='tap'){ o+=slider(t('posX'),'L.x',0,1,L.x==null?.5:L.x,0.005)+slider(t('posY'),'L.y',0,1,L.y==null?.5:L.y,0.005)+'<div class="row"><label></label><button class="sm" data-anpick="xy">'+t('akPickXY')+'</button></div>'+slider(t('size'),'L.r',0.03,0.25,L.r||0.08,0.005);
    if(k==='ring') o+='<div class="row"><label>'+t('akLabel')+'</label><input type="text" data-k="L.label" dir="auto" value="'+esc(L.label||'')+'"></div><div class="row"><label>'+t('akCount')+'</label><input type="number" data-k="L.from" value="'+(L.from==null?'':L.from)+'" placeholder="1"><input type="number" data-k="L.to" value="'+(L.to==null?'':L.to)+'" placeholder="3"></div><div class="row"><label>'+t('akPre')+'</label><input type="text" data-k="L.pre" dir="ltr" value="'+esc(L.pre||'')+'" placeholder="×"><input type="text" data-k="L.suf" dir="ltr" value="'+esc(L.suf||'')+'" placeholder="%"></div>'+seg(t('akSide'),'L.side',[['left',t('akLeft')],['right',t('akRight')],['top',t('akTop')],['bottom',t('akBottom')]],L.side||'right')+slider(t('akTextSize'),'L.size',40,220,L.size||86,2); }
  if(k==='spots'||k==='route'||k==='path'||k==='tags'||k==='arrow'||k==='underline'||k==='spotlight'){ o+='<div class="sec" style="padding:0;border:0;margin:0 0 6px"><h4 style="margin:0 0 6px">'+t('akPoints')+'</h4>'+P.map((p,i)=>row(i)).join('')+'<button class="sm" data-anpick="pts">'+t('akAddPt')+'</button>'+(k==='path'?' <button class="sm ghost" data-anpick="from">'+t(L.from?'akFromRe':'akFrom')+'</button>'+(L.from?' <button class="sm ghost" data-anfromrm="1">×</button>':''):'')+'</div>'+(k!=='path'&&k!=='underline'?slider(t('akTextSize'),'L.size',40,200,L.size||86,2):''); if(k==='spots'||k==='spotlight') o+=slider(t('size'),'L.r',0.03,0.35,L.r||(k==='spotlight'?0.16:0.07),0.005); if(k==='spotlight') o+=slider(t('akDim'),'L.dim',0.2,0.9,L.dim==null?0.68:L.dim,0.02); if(k==='arrow') o+=slider(t('akCurve'),'L.lift',-0.6,0.6,L.lift==null?0.22:L.lift,0.02); }
  if(['highlight','cross','blur','frame','scan'].includes(k)){ const R=L.rects||[]; o+='<div class="sec" style="padding:0;border:0;margin:0 0 6px"><h4 style="margin:0 0 6px">'+t('akBoxes')+'</h4>'+R.map((q,i)=>row(i)).join('')+'<button class="sm" data-anpick="rect">'+t('akAddBox')+'</button></div>'+(k==='blur'?seg(t('style'),'L.mode',[['blur',t('akBlur')],['pixel',t('akPixel')]],L.mode||'blur'):'')+slider(t('akTextSize'),'L.size',40,200,L.size||86,2); }
  if(k==='boxes'){ const R=L.rects||[]; o+='<div class="sec" style="padding:0;border:0;margin:0 0 6px"><h4 style="margin:0 0 6px">'+t('akBoxes')+'</h4>'+R.map((q,i)=>row(i)).join('')+'<button class="sm" data-anpick="rect">'+t('akAddBox')+'</button></div><div class="row"><label>'+t('akTag')+'</label><input type="text" data-k="L.tag" dir="auto" value="'+esc(L.tag||'')+'" placeholder="'+(LANG==='en'?'Me':'أنا')+'"></div>'+slider(t('akTextSize'),'L.size',40,200,L.size||86,2); }
  if(k==='wave') o+=slider(t('posY'),'L.y',0.05,0.98,L.y==null?.86:L.y,0.005)+slider(t('akCalm'),'L.amp',0,0.6,L.amp==null?.12:L.amp,0.01)+'<div class="row"><label>'+t('akBursts')+'</label><button class="sm" data-anburst="1">'+t('akBurstHere')+'</button>'+((L.burst||[]).length?'<button class="sm ghost" data-anburst="clear">'+t('akClear')+' ('+(L.burst||[]).length+')</button>':'')+'</div>';
  return o+'<p class="hint">'+t('akHint_'+k)+'</p>'; }
function imgMoveInsp(L){ const mv=L.move||(L.kb===false?'none':'push'), sh=L.shake||[];
  return '<div class="sec" style="padding:0;border:0;margin:0 0 9px"><h4 style="margin:0 0 6px">'+t('imMotion')+'</h4>'+pick(t('imMove'),'L.move',IMOVES.map(x=>[x,t('im_'+x)]),mv)
    +(mv==='push'||mv==='pull'?'<div class="row"><label>'+t('imFocus')+'</label><button class="sm" data-anpick="focus">'+t(L.fx!=null?'imFocusRe':'imFocusSet')+'</button></div>':'')+(mv!=='none'?slider(t('imAmount'),'L.amount',0.2,2.5,L.amount==null?1:L.amount,0.05):'')
    +tog('L.hand',t('imHand'),t('imHandSub'),!!L.hand)
    +pick(t('imIn'),'L.inFx',INFX.map(x=>[x,t('imfx_'+(x||'none'))]),L.inFx||'')+pick(t('imOut'),'L.outFx',OUTFX.map(x=>[x,t('imfx_'+(x||'none'))]),L.outFx||'')
    +'<div class="row"><label>'+t('imShake')+'</label><button class="sm" data-imshake="1">'+t('imShakeHere')+'</button>'+(sh.length?'<button class="sm ghost" data-imshake="clear">'+t('akClear')+' ('+sh.length+')</button>':'')+'</div><p class="hint">'+t('imHint')+'</p></div>'; }
/* تختار مكان من الشاشة: الضغطة الجاية على الفيديو تحط النقطة */
function pickStart(kind){ const L=selLayer(); if(!L) return; if(playing) stop(); PICK={kind,id:L.id,a:null}; $('#wrap').classList.add('picking'); toast(t(kind==='rect'||kind==='screen'?'akPickRect':'akPickTip')); }
function pickEnd(){ PICK=null; $('#wrap').classList.remove('picking'); }
function pickAt(x,y){ const L=hs().layers.find(l=>l.id===(PICK&&PICK.id)); if(!L){ pickEnd(); return; } const k=PICK.kind;
  if(L.type==='anno'&&L.stick!==false){ try{ const u=F.contentWindow.__hsUnmap&&F.contentWindow.__hsUnmap(T,x,y); if(u){ x=clamp(u[0],0,1); y=clamp(u[1],0,1); } }catch(e){} }
  const p=[r3(x),r3(y)];
  if(k==='rect'||k==='screen'){ if(!PICK.a){ PICK.a=p; toast(t('akPickRect2')); return; } snap(); const a=PICK.a, q=[r3(Math.min(a[0],p[0])),r3(Math.min(a[1],p[1])),r3(Math.max(0.02,Math.abs(p[0]-a[0]))),r3(Math.max(0.02,Math.abs(p[1]-a[1])))]; if(k==='screen'){ L.rect=q; pickEnd(); live(); renderRight(); return; } (L.rects=L.rects||[]).push([r3(Math.min(a[0],p[0])),r3(Math.min(a[1],p[1])),r3(Math.max(0.02,Math.abs(p[0]-a[0]))),r3(Math.max(0.02,Math.abs(p[1]-a[1])))]); }
  else { snap(); if(k==='xy'){ L.x=p[0]; L.y=p[1]; } else if(k==='focus'){ L.fx=p[0]; L.fy=p[1]; } else if(k==='from') L.from=p; else (L.pts=L.pts||[]).push(p); }
  pickEnd(); live(); renderRight(); }
const TRS=['curve','push','pull','rack','whip','spin','iris'], MKK=['circle','underline','arrow','box','highlight','check','cross'], LTS=['bar','card','tag','line'], PIPS=['tr','tl','br','bl'];
const GRADES=['none','cine','natural','skin','studio','warm','cool','night','muted','pop','teal','bw','film'];
const GRADEF={none:'none',cine:'contrast(1.16) saturate(.78) brightness(.96) sepia(.2)',natural:'contrast(1.05) saturate(1.06)',skin:'contrast(.97) saturate(.94) brightness(1.04) sepia(.08)',studio:'contrast(1.09) saturate(1.03) brightness(1.03)',warm:'saturate(1.08) sepia(.2) brightness(1.02)',cool:'contrast(1.06) saturate(.95) hue-rotate(-12deg)',night:'brightness(1.13) contrast(.95) saturate(.9)',muted:'saturate(.7) contrast(1.05)',pop:'saturate(1.32) contrast(1.08)',teal:'contrast(1.1) saturate(1.1) hue-rotate(-18deg)',bw:'grayscale(1) contrast(1.18)',film:'contrast(1.04) saturate(.85) sepia(.25)'};
const MKPV={circle:'<svg viewBox="0 0 60 40"><ellipse cx="30" cy="20" rx="24" ry="13" fill="none" stroke="#FFD21F" stroke-width="3.5" stroke-linecap="round"/></svg>',underline:'<svg viewBox="0 0 60 40"><path d="M8 28 Q30 33 52 27" fill="none" stroke="#FFD21F" stroke-width="4" stroke-linecap="round"/><rect x="12" y="12" width="36" height="7" rx="3" fill="#ffffff55"/></svg>',arrow:'<svg viewBox="0 0 60 40"><path d="M50 32 Q34 8 12 10 M12 10 l8 -5 M12 10 l6 7" fill="none" stroke="#FF4D6D" stroke-width="3.5" stroke-linecap="round"/></svg>',box:'<svg viewBox="0 0 60 40"><path d="M10 9 L50 8 L51 31 L9 32 Z" fill="none" stroke="#FFD21F" stroke-width="3.5" stroke-linejoin="round"/></svg>',highlight:'<svg viewBox="0 0 60 40"><rect x="8" y="14" width="44" height="12" fill="#FFD21F99"/><rect x="12" y="17" width="36" height="6" rx="2" fill="#ffffffaa"/></svg>',check:'<svg viewBox="0 0 60 40"><path d="M18 21 L27 30 L44 10" fill="none" stroke="#2FBF9B" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>',cross:'<svg viewBox="0 0 60 40"><path d="M20 10 L40 30 M40 10 L20 30" fill="none" stroke="#FF4D6D" stroke-width="5" stroke-linecap="round"/></svg>'};
const LTPV={bar:'<span style="all:unset;display:block;border-right:4px solid var(--cap);background:#000a;color:#fff;font-size:11px;padding:3px 7px">الاسم</span>',card:'<span style="all:unset;display:block;background:#fff;color:#15151C;border-radius:6px;font-size:11px;padding:3px 8px">الاسم</span>',tag:'<span style="all:unset;display:block;background:var(--cap);color:#fff;border-radius:20px;font-size:11px;padding:3px 9px">الاسم</span>',line:'<span style="all:unset;display:block;border-bottom:3px solid var(--cap);color:#fff;font-size:11px;padding:2px 6px">الاسم</span>'};
function lookAccOf(h){ return (h.look&&h.cardDefault&&h.cardDefault.accent)||(h.grade&&h.grade.preset==='cine'?'#F4C55A':''); }
function lookApply(name){ snap(); const h=hs();
  const oldAcc=h.cardDefault&&h.cardDefault.accent; if(oldAcc) h.layers.forEach(Ly=>{ if((Ly.type==='mg'||Ly.type==='anno')&&Ly.accent===oldAcc) delete Ly.accent; });
  if(!name){ delete h.look; delete h.grade; } else { const L=(INFO.looks||{})[name]; if(!L) return; h.look={name,overlay:L.overlay||'none',amount:L.amount==null?0.5:L.amount}; if(L.grade) h.grade={preset:L.grade,amount:0.85}; Object.assign(h.cap,L.cap||{}); h.cardDefault={...(L.card||{})};
    h.layers.forEach(Ly=>{ if(Ly.type==='split'||Ly.type==='viz'||Ly.type==='pip'){ for(const k in L.card||{}){ if(!(k==='deco'&&Ly.type==='viz')) Ly[k]=L.card[k]; } } if(Ly.type==='fx'&&(Ly.auto==='transitions'||Ly.auto==='trans')&&L.tr) Ly.fx=L.tr; }); }
  renderAll(); live(); toast(name?t('lookDone',(LANG==='ar'?(INFO.looks[name].ar):INFO.looks[name].en)):t('lookOff')); }
function trAdd(f,at){ const h=hs(); return {type:'fx',fx:f,seam:r3(at),dir:h.trDir||'right',amount:0.6,auto:'trans',track:2}; }
const ENTERS=['rise','pop','slide','drop','zoom','fade','words','none'];
const EXITS=['auto','fade','rise','sink','shrink','punch','blur','slide','wipe','words','none']; /* 4.21: خروج الكابشن */
const CHARS=['robo','sprout','star','cube'];
const RTABS=['sel','cap','plan','tr','audio','check','pub','claude','proj'];   // 4.50: «الملاحظات» صارت «المساعد» (claude)
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const fmt=x=>{ const m=Math.floor(x/60), s=(x%60).toFixed(2).padStart(5,'0'); return String(m).padStart(2,'0')+':'+s; };
const key=c=>c.w.map(w=>w.t).join(' ');
const clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
const r3=x=>Math.round(x*1000)/1000;
const total=()=>ST.caps.total, dur=()=>ST.caps.total+(ST.outro||0);
function toast(m){ const x=$('#toast'); x.textContent=m; x.style.opacity=1; clearTimeout(x._t); x._t=setTimeout(()=>x.style.opacity=0,2400); }
/* 4.20: أي حفظ أو تعديل منك يتسجّل وقته، عشان النبضة ما تحسبه «Claude عدّل» وتحدّث العرض عليك وأنت تعدّل */
let LOCALW=0;
async function api(url,body,headers){ const post=body!==undefined; if(post) LOCALW=Date.now(); let r; try{ r=await fetch(url,!post?{}:{method:'POST',headers:headers||{'Content-Type':'application/json'},body:headers?body:JSON.stringify(body)}); } finally{ if(post){ LOCALW=Date.now(); adoptSig=true; } } try{ return await r.json(); }catch(e){ return {ok:false,msg:'HTTP '+r.status}; } }
function hs(){ ST.studio.hs=ST.studio.hs||{}; const h=ST.studio.hs; h.cap={...DEFCAP,...(h.cap||{})}; h.en={...DEFEN,...(h.en||{})}; h.en.map=h.en.map||{};
  h.fonts=h.fonts||[]; h.layers=h.layers||[]; h.hooks={on:false,active:0,dur:2.6,style:'box',items:[],...(h.hooks||{})}; h.mix={voice:1,clean:false,bg:0.28,...(h.mix||{})}; h.mix.sfx=h.mix.sfx||{}; h.check={gap:2.5,...(h.check||{})}; h.frame={ar:'9:16',cy:0.47,...(h.frame||{})}; h.platforms=h.platforms||[]; h.win=h.win||{}; h.mb=h.mb||{}; h.emoji={on:false,pos:'word',anim:'pop',size:88,gap:2.5,only:'all',auto:true,...(h.emoji||{})}; if(!h.emoji.set||typeof h.emoji.set!=='object'||Array.isArray(h.emoji.set)) h.emoji.set={};   /* 4.48: إيموجي الكابشن */
  if(h.cap.font==='Marhey') h.cap.font='Cairo'; h.layers.forEach(L=>{ if(L.font==='Marhey') L.font='Cairo'; });   /* 4.47 */ h.bleep={mode:'beep',cap:'stars',tone:1000,...(h.bleep||{})}; if(!Array.isArray(h.bleep.items)) h.bleep.items=[]; return h; }
const cardAt=x=>ST.caps.cards.findIndex(c=>x>=c.s&&x<c.e);
const selLayer=()=>SEL&&SEL.kind==='layer'?hs().layers.find(l=>l.id===SEL.id):null;
const allFonts=()=>[...[...new Set(hs().fonts.map(f=>f.name))],...AR_FONTS,...EN_FONTS];

/* ───── اللغة ───── */
function applyLang(){ document.documentElement.lang=LANG; document.documentElement.dir=LANG==='ar'?'rtl':'ltr'; $$('.side,#top,#stageBtns,#live').forEach(e=>e.dir=LANG==='ar'?'rtl':'ltr');
  $$('[data-t]').forEach(e=>e.textContent=t(e.dataset.t)); $('#bLang').textContent=LANG==='ar'?'EN':'ع'; $('#pp').textContent=t(playing?'pause':'play');
  $('#tabs').innerHTML=RTABS.map(k=>'<button data-tab="'+k+'">'+t('tab_'+k)+'</button>').join(''); loadSteps(); markTabs(); if(typeof mTabs==='function') mTabs(); }
function markTabs(){ $$('#tabs button').forEach(b=>b.classList.toggle('on',b.dataset.tab===RTAB)); setTimeout(stepsLive,0); { const cur=document.body.dataset.mv==='bin'?LTAB:RTAB; $$('#mtabs button').forEach(b=>b.classList.toggle('on',b.dataset.mv===cur)); } $$('#binTabs button').forEach(b=>b.classList.toggle('on',b.dataset.ltab===LTAB));
  $$('[data-tool]').forEach(b=>b.classList.toggle('on',b.dataset.tool===TOOL)); $('#bMag').classList.toggle('on',MAG); if($('#bLink')) $('#bLink').classList.toggle('on',LINK); $('#bSkim').classList.toggle('on',SKIM); $('#lane').classList.toggle('blade',TOOL==='blade'); }
$('#bLang').onclick=()=>{ LANG=LANG==='ar'?'en':'ar'; try{ localStorage.setItem('hsLang',LANG); }catch(e){} langCookie(); applyLang(); if(ST){ buildTL(); renderAll(); } renderLive(); if($('#brief').classList.contains('on')) renderBrief(); };

/* ───── 4.12: صوت استوديو. المعاينة تسمّعك نفس الصوت اللي بيطلع بالتصدير ───── */
let SVS={busy:false,line:'',ab:'sv',n:0}, MUP=null;   // 4.44: «تسمع الأصل/الاستوديو» انشال: تسمع اللي اخترته على طول
const svOn=()=>!!(hs().mix&&(hs().mix.studio||hs().mix.dub))&&SVS.ab!=='raw';   // 4.26: الدبلجة تنسمع بالمعاينة
function auLoad(force){ const sv=svOn(), cl=!sv&&!!(hs().mix&&hs().mix.clean), k=ST.nvf+':'+ST.caps.total+':'+(INFO.vsig||'')+(sv?':sv'+SVS.n:'')+(cl?':cl':''); if(k===auKey&&!force) return; const nv=String(auKey).split(':').slice(0,3).join(':')!==k.split(':').slice(0,3).join(':'); auKey=k;
  /* 4.20: لو الصوت ما حمّل (السيرفر يعيد تشغيله أو فتحت المشروع من المكتبة) يعيد المحاولة لحاله بدل ما يسكت */
  AU._fb=0; clearTimeout(AU._rt); AU.onerror=()=>{ const n=++AU._fb; if(n>8) return; const src=n%2?'/cutz.mp4?v='+encodeURIComponent(k)+'&r='+n:'/hs/au.m4a?'+(sv?'sv=1&':'')+'v='+encodeURIComponent(k)+'&r='+n; clearTimeout(AU._rt); AU._rt=setTimeout(()=>{ AU.src=src; AU.load(); },n===1?0:Math.min(6000,800*n)); }; AU.preload='auto'; AU.src='/hs/au.m4a?'+(sv?'sv=1&':cl?'clean=1&':'')+'v='+encodeURIComponent(k); if(nv) PEAKS=null; }
function auSwap(){ const pl=playing; if(pl) stop(); auLoad(); if(pl) play(); }
async function svApply(redo){ if(!hs().mix.studio){ auSwap(); renderRight(); return; }
  SVS.busy=true; SVS.ab='sv'; renderRight(); const r=await api('/hs/sv',{redo:!!redo}); SVS.busy=false;
  if(!r||!r.ok){ SVS.line=''; toast((r&&(srvEn(r.msg)||r.line))||t('svFail')); } else { SVS.line=r.line||''; SVS.n++; } auSwap(); renderRight(); }
/* صوت جزء معيّن (لقطة أو جملة): نفس نطاقات mix.vr، بس من اللي ضغطت عليه مباشرة */
function rngG(s,e){ const r=(hs().mix.vr||[]).find(r=>Math.abs(r.s-s)<0.02&&Math.abs(r.e-e)<0.02); return r?r.g:1; }
function rngRow(s,e,lbl){ const g=rngG(s,e); return '<div class="row"><label>'+lbl+'</label><input type="range" data-rngv="'+r3(s)+','+r3(e)+'" min="0" max="2" step="0.05" value="'+g+'"><span class="val" id="rngv">'+(g===0?t('vMuted'):g)+'</span></div>'; }
/* يشيل [s,e] من النطاقات الموجودة ويخلّي اللي برّاه (ما يمسح نطاق أكبر كامل) */
function vrCut(list,s,e){ const out=[]; for(const r of list||[]){ if(r.e<=s+0.001||r.s>=e-0.001){ out.push(r); continue; } if(s-r.s>=0.1) out.push({...r,e:r3(s)}); if(r.e-e>=0.1) out.push({...r,s:r3(e)}); } return out; }
function rngSet(s,e,g){ const h=hs(); h.mix.vr=vrCut(h.mix.vr,s,e); if(Math.abs(g-1)>0.001) h.mix.vr.push({s:r3(s),e:r3(e),g:r3(g)}); h.mix.vr.sort((a,b)=>a.s-b.s); vrDraw(); dirty(); }
function svBlock(m){ let o=tog('mix.studio',t('svOn'),t('svSub'),!!m.studio);
  if(m.studio){ o+=SVS.busy?'<p class="hint svst">'+t('svBusy')+'</p>':(SVS.line?'<p class="hint svst">'+esc(SVS.line)+'</p>':'');
    if(m.studio==='ext') o+='<p class="hint">'+t(INFO.sv&&INFO.sv.ext?'svExtOn':'svExtOld')+'</p>';
    if(INFO.sv&&INFO.sv.rnn===false) o+='<p class="hint">'+t('svOld')+'</p>'; }
  else o+=tog('mix.clean',t('cleanVoice'),t('cleanVoiceSub'),m.clean);
  return o+'<p class="hint">'+t('svExtHint')+'</p>'; }
/* ───── تحميل وحفظ ───── */
/* 4.23: تحديث خفيف بعد القص والنقل والتراجع: البيانات بس، بدون إعادة تحميل صفحة الرسم (كانت تاخذ 6 ثواني) */
async function reloadLite(){ ST=await api('/api/state'); INFO=await api('/hs/info'); hs(); drawSafe(); lastFrame=-1; setTimeout(pendSync,0); VK=(INFO.vsig||'0')+'-'+ST.nvf; MARKS=(hs().marks||[]).filter(m=>m>0.05&&m<total()-0.05); if(SEL&&SEL.kind!=='layer') SEL=null; auLoad(); await initFrame(false); buildTL(); renderAll(); seek(Math.min(T,dur())); if(!PEAKS) api('/hs/peaks').then(p=>{ PEAKS=p; drawWave(); }); refreshCheck(); applyMode(); pinMark(); guideSync(); }
async function load(keep){
  ST=await api('/api/state'); INFO=await api('/hs/info'); if(!SFXLIB.length) await sfxLibLoad(); NOTES=await api('/hs/notes'); REV=await api('/hs/review_state'); hs(); drawSafe();
  $('#proj').textContent=INFO.title||INFO.name; hubBack(); pillSync(); lastFrame=-1; setTimeout(pendSync,0); VK=(INFO.vsig||'0')+'-'+ST.nvf; if(INFO.sv&&!SVS.busy) SVS.line=INFO.sv.line||''; auLoad();
  MARKS=(hs().marks||[]).filter(m=>m>0.05&&m<total()-0.05); if(SEL&&SEL.kind!=='layer') SEL=null;
  await initFrame(true); buildTL(); renderAll(); seek(keep?Math.min(T,dur()):0); if(!keep) posRestore(); if(!PEAKS) api('/hs/peaks').then(p=>{ PEAKS=p; drawWave(); }); refreshCheck(); applyMode(); pinMark(); guideSync(); }
function frameLoad(){ return new Promise(res=>{ F.onload=()=>res(); F.src='/compose.html?v='+Date.now(); }); }
async function initFrame(reload){ if(reload||!frameReady){ frameReady=false; await frameLoad(); }
  return new Promise(res=>{ let n=0; const go=()=>{ const w=F.contentWindow; if(!w||!w.init||!w.__hsExt){ if(++n>80){ res(); return; } setTimeout(go,120); return; }
    if(!w.document.getElementById('mfit')){ const st=w.document.createElement('style'); st.id='mfit'; st.textContent='html,body{margin:0;overflow:hidden;background:#000}#cv{width:100vw!important;height:100vh!important;display:block}'; w.document.head.appendChild(st); }
    frameReady=true; if(MOBILE&&w.hsLowRes){ try{ w.hsLowRes(0.5); }catch(e){} } Promise.resolve(w.init({cards:ST.caps.cards,total:ST.caps.total,outro:ST.outro,theme:ST.theme,behind:ST.behind,studio:ST.studio})).then(res,res); }; go(); }); }
let _frP=null, VK='0'; const frU=i=>'/hs/pv/'+String(Math.min(ST.nvf,Math.max(1,i))).padStart(5,'0')+'.jpg?v='+VK;
async function drawNow(x){ const w=F.contentWindow; if(!w||!w.draw||!ST||!ST.nvf) return; if(PEND){ if(!w.__hsPend) w.__hsPend=PEND.box; await pendPrep(x); } let i=Math.min(ST.nvf,Math.max(1,Math.round(vm(w.hsWarp?w.hsWarp(x):x)*FPS)+1)); if(MOBILE&&playing) i-=((i-1)%2); const id=String(i).padStart(5,'0');
  if(i!==lastFrame){ lastFrame=i; try{ await w.setFrame(frU(i)); }catch(e){} if(playing&&w.hsPrefetch) w.hsPrefetch((MOBILE?[2,4,6]:[1,2,3,4,5,6]).map(d=>frU(i+d))); if(ST.behind&&ST.hasPerson&&w.setPerson){ const inR=(ST.behind.ranges||[]).some(r=>i>=r[0]&&i<=r[1]); try{ await w.setPerson(inR?('/bt/person/'+id+'.png'):null,(ST.behind.faces&&ST.behind.faces[i])||null); }catch(e){} } }
  try{ w.draw(x); }catch(e){} }
/* 3.8: رسمة وحدة بكل مرة. لو الطلبات أسرع من الرسم (جوال أو جهاز مشغول) ينرسم آخر طلب فقط بدل ما تتراكم وتعلّق */
let _pump=false, _want=null;
function drawT(x){ _want=x; if(_pump) return _frP; _pump=true; _frP=(async()=>{ try{ while(_want!==null){ const v=_want; _want=null; await drawNow(v); } } finally { _pump=false; } })(); return _frP; }
const HIST=[]; let _saveT=null, _chkT=null;
function snap(){ HIST.push(JSON.stringify({caps:ST.caps,theme:ST.theme,studio:ST.studio})); if(HIST.length>40) HIST.shift(); FUT.length=0; }
const FUT=[];
let DIRTY=false;
function dirty(){ DIRTY=true; $('#saved').textContent=t('saving'); clearTimeout(_saveT); _saveT=setTimeout(save,450); }
async function save(){ if(cutBusy()){ clearTimeout(_saveT); _saveT=setTimeout(save,2500); return; } clearTimeout(_saveT); DIRTY=false; adoptSig=true; LASTSAVE=Date.now(); await api('/api/save',{caps:ST.caps,theme:ST.theme,studio:ST.studio,outro:ST.outro||0}); $('#saved').textContent=t('saved'); clearTimeout(_chkT); _chkT=setTimeout(refreshCheck,700); }
async function live(){ const w=F.contentWindow; if(w&&w.hsSet){ await w.hsSet(ST.studio.hs); } drawT(T); placeGiz(); dirty(); }
async function hard(){ await initFrame(false); lastFrame=-1; drawT(T); dirty(); }
/* 4.14: التراجع والإعادة من سجل محفوظ بالمشروع (.hs/hist): كل تعديل، وكل قص، وكل شي سواه Claude. ما يضيع لو حدّثت الصفحة أو قفلت الاستوديو */
async function histGo(back){ if(cutBusy()){ toast(t('cutBusy')); return; } if(HISTBUSY) return; HISTBUSY=true; try{ if(DIRTY) await save(); const r=await api(back?'/hs/undo':'/hs/redo',{});
    if(!r||!r.ok){ toast(r&&srvEn(r.msg)?srvEn(r.msg):t(back?'nothingUndo':'nothingRedo')); return; }
    const msg=t(back?'undoneX':'redoneX',srvEn(r.why)||t('stepEdit')); SEL=null;
    if(r.rebuild){ stLoader('rebuild',t('rebuildSub')); pollJob(async()=>{ try{ await load(true); toast(msg); } finally{ stLoaderHide(); } }); return; }
    await reloadLite(); toast(msg); }
  finally{ HISTBUSY=false; } }
let HISTBUSY=false;
async function redo(){ return histGo(false); }
/* 4.9: القص بالاستوديو يعيد بناء الفيديو، فالتراجع العادي ما يقدر يرجّعه. نحفظ علامة بالنسخة التلقائية «قبل القص» والتراجع يرجّعها */
function cutUndoMark(p){ if(p&&p.err) return; const v=(INFO.versions||[]).find(x=>/^قبل (القص|اختيار الجمل|إضافة مقطع)/.test(x.name||'')); if(!v) return; HIST.length=0; FUT.length=0; HIST.push(JSON.stringify({cutUndo:v.id})); }
async function cutUndo(id){ toast(t('cutUndoing')); const r=await api('/hs/ver_restore',{id}); if(r&&r.ok===false){ toast(srvEn(r.msg)||t('failed')); return; } HIST.length=0; FUT.length=0; if(r.rebuild){ stLoader('rebuild',t('rebuildSub')); pollJob(async()=>{ try{ await load(true); toast(t('cutUndone')); } finally{ stLoaderHide(); } }); } else { await load(true); toast(t('cutUndone')); } }
async function undo(){ return histGo(true); }
async function refreshCheck(){ if(!READY) return; refreshRet(); loadSteps(); CHECK=await api('/hs/check'); drawCheck(); if(RTAB==='check') renderRight(); const b=$('#tabs [data-tab="check"]'); if(b) b.innerHTML=t('tab_check')+((CHECK.issues||(CHECK.reqs||[]).some(r=>!r.ok))?'<i class="dot"></i>':''); }

/* ───── التشغيل ───── */
/* 4.7.1: كل فريم كان يكتب بالصفحة ثم يقرأ مكان التمرير، فالمتصفح يعيد حساب التخطيط كامل 30 مرة بالثانية. الحين يقرأ أول ثم يكتب، وما يكتب إلا اللي تغيّر */
let _tmS='', _phX=-1, _scW=0, _scL=0, _scAt=0;
function seek(x,quiet){ T=clamp(x,0,dur()); const sc=$('#scroller'), px=T*PX, now=performance.now();
  if(!quiet&&(!playing||now-_scAt>250)){ _scL=sc.scrollLeft; _scW=sc.clientWidth; _scAt=now; if(px<_scL+10||px>_scL+_scW-30){ sc.scrollLeft=Math.max(0,px-_scW*(MOBILE?0.5:0.3)); _scAt=0; } }
  if(!MOBILE){ const s=fmt(T)+' / '+fmt(dur()); if(s!==_tmS){ _tmS=s; $('#tm').textContent=s; const aa=document.getElementById('agAt'); if(aa) aa.textContent=fmt(T); } } mSync(); const pr=Math.round(px); if(pr!==_phX){ _phX=pr; $('#ph').style.left=pr+'px'; }
  drawT(T); placeGiz(); if(!playing){ try{ const o_=vm(T); AU.currentTime=Math.min(o_,AU.duration||o_); }catch(e){} } if(typeof posSave==='function') posSave(); }
let _loop=0; const SFXA={};
/* ───── 4.6: كتم الكلمات (بيب) ← hs.bleep ───── */
const BL_PRE=['وال','بال','فال','كال','لل','ال','و','ف','ب','ل','ك'];
const blNorm=s=>String(s||'').replace(/[\u064B-\u0670\u06D6-\u06ED]/g,'').replace(/[أإآٱ]/g,'ا').replace(/ة/g,'ه').replace(/ى/g,'ي').replace(/ؤ/g,'و').replace(/ئ/g,'ي').replace(/ـ/g,'').toLowerCase().replace(/[^\p{L}\p{N}_]/gu,'');
function blMatch(w,T){ const n=blNorm(w); if(!n) return false; if(T.has(n)) return true; return BL_PRE.some(p=>n.startsWith(p)&&n.length-p.length>=2&&T.has(n.slice(p.length))); }
const blItems=()=>hs().bleep.items;
const blIdx=w=>{ const m=(w.s+w.e)/2; return blItems().findIndex(x=>m>=x.s-1e-6&&m<=x.e+1e-6); };
const blNew=w=>({s:r3(Math.max(0,w.s-0.03)),e:r3(w.e+0.03),t:w.t});
function blToggle(w){ const i=blIdx(w); if(i>=0) blItems().splice(i,1); else { blItems().push(blNew(w)); blItems().sort((a,b)=>a.s-b.s); } }
function blFind(str){ const T=new Set(String(str||'').split(/[\s,،]+/).map(blNorm).filter(Boolean)); let f=0,n=0; if(!T.size) return [0,0];
  ST.caps.cards.forEach(c=>c.w.forEach(w=>{ if(!blMatch(w.t,T)) return; f++; if(blIdx(w)<0){ blItems().push(blNew(w)); n++; } })); blItems().sort((a,b)=>a.s-b.s); return [f,n]; }
let BLP=null;
function blOff(){ if(!BLP) return; try{ if(BLP.o) BLP.o.stop(); }catch(e){} BLP=null; AU.volume=clamp(hs().mix.voice,0,1); }
function bleepPreview(x){ const b=hs().bleep, it=b.items.find(i=>x>=i.s&&x<i.e);
  if(it&&!BLP){ AU.volume=0; BLP={}; if(b.mode!=='mute'){ try{ const C=window.__blCtx||(window.__blCtx=new (window.AudioContext||window.webkitAudioContext)()); if(C.state==='suspended') C.resume(); const o=C.createOscillator(), g=C.createGain(); o.type='sine'; o.frequency.value=b.tone||1000; g.gain.value=0.12; o.connect(g); g.connect(C.destination); o.start(); BLP.o=o; }catch(e){} } }
  else if(!it&&BLP) blOff(); }
/* 4.7.1: وقت التشغيل على الكمبيوتر نرسم بنص الدقة (المعاينة صغيرة أصلاً)، ولما توقف ترجع الدقة الكاملة */
function lowRes(on){ if(MOBILE) return; const w=F.contentWindow; if(!w||!w.hsLowRes) return; try{ w.hsLowRes(on?0.5:1); }catch(e){} }
function stop(){ const was=playing; playing=false; _loop++; AU.pause(); blOff(); sxStopAll(); $('#pp').textContent=t('play'); mSync(); document.body.classList.remove('playing'); if(was&&!MOBILE){ lowRes(false); lastFrame=-1; drawT(T); } }
function sfxPreview(a,b){ sxTick(b); }
async function play(){ if(playing){ stop(); return; } if(T>=dur()-0.05) T=0; playing=true; $('#pp').textContent=t('pause'); const my=++_loop; document.body.classList.add('playing'); lowRes(true);
  let clock=false; AU.volume=clamp(hs().mix.voice,0,1); try{ AU.currentTime=vm(T); await AU.play(); }catch(e){ clock=true; } if(AU.paused||AU.error) clock=true;
  let t0=T, n0=performance.now(); let prev=T, PSEG=-1; if(T>=total()-0.03){ clock=true; AU.pause(); } AU.playbackRate=RATE; PLAY_REBASE=()=>{ t0=T; n0=performance.now(); };
  let tk=0; const tick=()=>{ if(!playing||my!==_loop) return; if(MOBILE&&(++tk%2)){ requestAnimationFrame(tick); return; } let ax=null; const M_=VM(); if(!clock&&M_){ if(PSEG<0||PSEG>=M_.length) PSEG=vmSegAt(prev); const S_=M_[PSEG], L_=S_[1]-S_[0], o=AU.currentTime;
      if(o<S_[2]-0.3||o>S_[2]+L_+0.3){ PSEG=vmSegAt(prev); const S2=M_[PSEG]; try{ AU.currentTime=S2[2]+Math.max(0,prev-S2[0]); }catch(e){} ax=prev; }
      else if(o>=S_[2]+L_-0.012){ PSEG++; if(PSEG<M_.length){ try{ AU.currentTime=M_[PSEG][2]; }catch(e){} ax=M_[PSEG][0]; } else ax=total(); }
      else ax=S_[0]+Math.max(0,o-S_[2]); }
    const atx=ax!=null?ax:AU.currentTime;
    if(!clock&&(AU.ended||atx>=total()-0.03)&&dur()>total()+0.05){ clock=true; t0=Math.max(total(),atx); n0=performance.now(); AU.pause(); }
    const x=clock?t0+(performance.now()-n0)/1000*RATE:atx; if(x>=dur()-0.03||(!clock&&AU.ended)){ stop(); seek(dur()); return; } sfxPreview(prev,x); bleepPreview(x); if(!BLP){ const r_=vrAt(x); AU.volume=clamp(hs().mix.voice*(r_?r_.g:1)*gkAt(hs().mix.vkf,x,1),0,1); } prev=x; seek(x); requestAnimationFrame(tick); };
  requestAnimationFrame(tick); }

/* ───── التايم لاين ───── */
const lname=L=>(L.type==='image'&&L.name)?L.name:(L.type==='image'&&L.src&&!/^data:/.test(L.src))?decodeURIComponent(String(L.src).split(/[\/\\]/).pop().replace(/\.[a-z0-9]+(\?.*)?$/i,'')).replace(/^plan-\d+-/,'')||t('type_image'):L.type==='anno'?t('ak_'+(L.kind||'ring')):L.type==='mg'?mgName(L):L.type==='draw'?t('type_draw'):L.type==='mark'?t('mk_'+(L.kind||'circle')):L.type==='cursor'?t('type_cursor'):L.type==='lt'?(L.text||t('type_lt')):L.type==='pip'?t('type_pip'):L.type==='collage'?t('type_collage'):L.type==='text'?(L.text||'').split('\n')[0]:L.type==='char'?t('char_'+(L.char||'custom')):L.type==='fx'?t('fx_'+L.fx):L.type==='split'?(L.title||t('type_split')):L.type==='viz'?(L.title||t('vk_'+L.kind)):L.type==='kinetic'?(String(L.text||'').replace(/^[*>+]\s*/gm,'').split('\n').join(' ').slice(0,40)||t('type_kinetic')):L.type==='desk'?((L.text||'')+' '+t('dk_'+(L.kind||'note'))).trim():L.type==='cover'?(L.text||t('type_cover')):L.type==='bg'?t('bg_'+(L.mode||'blur')):L.type==='behind'?(L.text||t('type_behind')):t('image');
/* 4.12: كل طبقة تتداخل مع طبقة ثانية تاخذ سطر لحالها، والسطر الأعلى يطلع فوق بالفيديو. وفوقها سطر فاضي تسحب له الطبقة عشان تصير فوق الكل */
let LROWS=[];
function layerRows(){ const Ls=hs().layers||[], tracks=[...new Set(Ls.map(L=>L.track||0))].sort((a,b)=>b-a), rows=[{track:(tracks.length?tracks[0]:0)+1,sub:0,add:true}], where={};
  for(const tr of tracks){ const subs=[]; Ls.forEach(L=>{ if((L.track||0)!==tr) return; let k=0; while(k<subs.length&&subs[k].some(([a,b])=>L.s<b-0.001&&L.e>a+0.001)) k++; (subs[k]=subs[k]||[]).push([L.s,L.e]); where[L.id]=[tr,k]; });
    for(let k=subs.length-1;k>=0;k--) rows.push({track:tr,sub:k}); }
  return {rows,where}; }
function layerToRow(id,row,row0){ const h=hs(), R=LROWS[row], L=h.layers.find(x=>x.id===id); if(!R||!L) return;
  L.track=R.track; const i=h.layers.indexOf(L); h.layers.splice(i,1); if(row<row0) h.layers.push(L); else h.layers.unshift(L); ST.studio.hs.layers=h.layers; }
/* 4.44: طبقة الصورة تبان صورتها ببداية الطبقة والباقي اسمها */
function freshMark(){ const ids=new Set((hs().layers||[]).map(L=>L.id)); if(KNOWNL){ ids.forEach(id=>{ if(KNOWNL.has(id)){ return; } const c=$('#tLs .clip[data-id="'+CSS.escape(String(id))+'"]'); if(c){ c.classList.add('fresh'); setTimeout(()=>c.classList.remove('fresh'),1400); } }); } KNOWNL=ids; }
function lthumb(L){ const sr=L.src||(L.items&&L.items[0]&&L.items[0].src)||''; if(!sr||!/\.(png|jpe?g|webp|gif|svg)(\?|$)/i.test(sr)) return ''; const u=/^(https?:|data:|\/)/.test(sr)?sr:'/'+sr; return '<img class="lth" alt="" loading="lazy" src="'+esc(u)+'">'; }
let KNOWNL=null;   // 4.46: الطبقة الجديدة تدخل التايم لاين بحركة
function buildTL(){ if(!ST) return; const D=dur(), Wd=Math.max(D*PX+80,$('#scroller').clientWidth); $('#lane').style.width=Wd+'px'; const h=hs();
  const step=PX>=120?1:PX>=50?2:PX>=28?5:10; let o='';
  for(let s=0;s<=D;s+=step) o+='<span style="left:'+(s*PX)+'px">'+(s<60?s+'s':Math.floor(s/60)+':'+String(s%60).padStart(2,'0'))+'</span>';
  $('#ruler').innerHTML=o;
  const on=(k,id)=>SEL&&SEL.kind===k&&String(SEL.id)===String(id)?' on':'';
  const box=(s,e)=>'left:'+(s*PX)+'px;width:'+Math.max(7,(e-s)*PX-1)+'px';
  { const LR=layerRows(); LROWS=LR.rows; $('#tl').style.setProperty('--lo',(LR.rows.length*21-63)+'px'); $('#tLs').style.height=(LR.rows.length*21)+'px';
    $('#tLs').innerHTML=LR.rows.map((r,i)=>'<div class="lrow'+(r.add?' add':'')+'" style="top:'+(i*21)+'px"'+(r.add?' title="'+esc(t('lrowAdd'))+'"':'')+'>'+(r.add?hookClip(on,box):'')+h.layers.filter(L=>{ const w=LR.where[L.id]; return w&&w[0]===r.track&&w[1]===r.sub&&!r.add; }).map(L=>'<div class="clip '+L.type+on('layer',L.id)+(layerPinned(L)?'':' free')+'" data-kind="layer" data-id="'+L.id+'" style="'+box(L.s,L.e)+(L.off?';opacity:.4':'')+'"><i class="hl"></i>'+lthumb(L)+esc(lname(L))+kfDots(L)+'<i class="hr"></i></div>').join('')+'</div>').join(''); }
  freshMark();
  $('#tCap').innerHTML='<span class="lbl">'+t('trkCaps')+'</span>'+ST.caps.cards.map((c,i)=>'<div class="clip cap'+on('cap',i)+'" data-kind="cap" data-id="'+i+'" style="'+box(c.s,c.e)+'"><i class="hl"></i>'+esc(key(c))+'<i class="hr"></i></div>').join('');
  setTimeout(insBtn,0);   // 4.54
  let fx='<span class="lbl">'+t('trkFx')+'</span>';
  (ST.studio.scenes||[]).filter(s=>s.m&&s.m!=='R_FULL').forEach(s=>{ fx+='<div class="clip sc" style="'+box(s.s,Math.min(s.e,D))+'">'+esc(t('scene'))+'</div>'; });
  (ST.studio.brollClips||[]).forEach((b,i)=>{ fx+='<div class="clip broll'+on('broll',i)+'" data-kind="broll" data-id="'+i+'" style="'+box(b.s,b.e)+'"><i class="hl"></i>'+esc(t('broll'))+'<i class="hr"></i></div>'; });
  const sf=ST.studio.sfx||{}; for(const k in sf){ if(!Array.isArray(sf[k])||k==='soft') continue; sf[k].forEach((v,j)=>{ const o=sxGet(k,j), wpx=Math.max(24,o.d*PX-1), nm=t('sfx_'+k); fx+='<div class="clip sfx'+on('sfx',k+':'+j)+(o.g===0?' mute':'')+'" data-kind="sfx" data-id="'+k+':'+j+'" title="'+esc(nm)+'" style="left:'+(o.t*PX)+'px;width:'+wpx+'px"><i class="hl"></i>'+esc(nm.slice(0,Math.max(2,Math.floor(wpx/9))))+'<i class="hr"></i></div>'; }); }
  $('#tFx').innerHTML=fx;
  const every=Math.max(1,Math.ceil(26/PX)); let fm='';
  for(let s=0;s<total();s+=every) fm+='<div class="film" style="left:'+(s*PX)+'px;width:'+(every*PX)+'px;background-image:url(/hs/th/'+(Math.floor(vm(s))+1)+'.jpg?v='+VK+')"></div>';
  (INFO.seams||[]).forEach(s=>{ const tr=seamFx(s); fm+='<div class="cutgap" style="left:'+(s*PX)+'px"></div><div class="cutbtn'+(tr?' on':'')+'" data-seam="'+s+'" title="'+esc(tr?t('fx_'+tr.fx):t('cutAdd'))+'" style="left:'+(s*PX)+'px"></div>'; }); MARKS.forEach(m=>{ fm+='<div class="cutgap" style="left:'+(m*PX)+'px"></div>'; }); (h.blank||[]).forEach((b,i)=>{ fm+='<div class="blk'+(SEL&&SEL.kind==='blank'&&+SEL.id===i?' on':'')+'" data-blk="'+i+'" title="'+esc(t('blankTitle'))+'" style="left:'+(b.s*PX)+'px;width:'+Math.max(4,(b.e-b.s)*PX)+'px">'+esc(t('blankShort'))+'</div>'; });
  { const b=shotBounds(), IR=INFO.ins||[];   // 4.55: كل لقطة كلّيب لحاله، والمضاف بزر + لقطة كاملة
    for(let i=0;i<b.length-1;i++){ const ir=IR.some(r=>Math.abs(r[0]-b[i])<0.05&&Math.abs(r[1]-b[i+1])<0.08), cam=(hs().cams||[]).some(c=>Math.abs(c.s-b[i])<0.03&&Math.abs(c.e-b[i+1])<0.03); fm+='<div class="vclip'+(ir?' ins':'')+'" style="left:'+(b[i]*PX+1)+'px;width:'+Math.max(2,(b[i+1]-b[i])*PX-2)+'px">'+(ir?'<span>'+t('insClip')+'</span>':'')+(cam?'<i class="vcam" title="'+esc(t('camT'))+'"></i>':'')+'</div>'; }
    (hs().cams||[]).forEach(c=>camKfList(c).forEach(k=>{ fm+='<b class="gkd" style="left:'+((c.s+k.t)*PX)+'px" title="'+esc(fmt(c.s+k.t))+'"></b>'; })); }
  const rg=SEL&&(SEL.kind==='video'||(SEL.kind==='audio'&&!SEL.solo))?SEL:null; if(ST.outro>0) fm+='<div class="clip outro'+on('outro',0)+'" data-kind="outro" data-id="0" title="'+esc(t('endCardTip'))+'" style="'+box(total(),dur())+'">'+esc(t('endCard'))+'<i class="hr"></i></div>';
  fm+='<div class="region'+(rg?' on':'')+'" style="'+(rg?'left:'+(rg.s*PX)+'px;width:'+((rg.e-rg.s)*PX)+'px':'')+'"><i class="rl"></i><i class="rr"></i></div><div class="trim"></div><span class="lbl">'+t('trkVideo')+'</span>';
  $('#tFilm').innerHTML=fm;
  $('#tMk').innerHTML=NOTES.map(n=>'<div class="mk'+(n.status==='done'?' done':'')+(n.by==='claude'?' ai':'')+'" data-n="'+n.id+'" title="'+esc(n.text)+'" style="left:'+(n.t*PX)+'px"></div>').join('')+(REV.comments||[]).filter(c=>c.status==='open').map(c=>'<div class="mk cl" data-c="'+c.id+'" title="'+esc(c.who+': '+c.text)+'" style="left:'+(c.t*PX)+'px"></div>').join('');
  drawWave(); vrDraw(); drawCheck(); $('#ph').style.left=(T*PX)+'px'; tlFit(); placeGiz(); }
/* 4.13: التايم لاين يطول لحاله على قد التراكات (لحد 55% من الشاشة) عشان تراك الصوت ما يختفي تحت، وتقدر تسحب حدّه الفوقاني. دبل كلك يرجّعه تلقائي */
let TLH_USER=null; try{ TLH_USER=+localStorage.getItem('hs.tlh')||null; }catch(e){}
function tlFit(){ if(MOBILE) return; const gp=$('#tlGrip'); if(gp&&!gp.title) gp.title=t('tlGrip'); const need=$('#lane').offsetHeight-20+38+10, lo=Math.min(290,Math.round(innerHeight*0.4)), h=Math.round(TLH_USER?clamp(TLH_USER,Math.min(200,lo),Math.max(lo,innerHeight-240)):clamp(need,lo,innerHeight<760?lo:Math.max(lo,innerHeight*0.55)));   /* 4.31: شاشة قصيرة: التايم لاين ما ياخذ أكثر من حقه */
  const hh=uiMode()==='claude'?Math.min(h,190):h; if(document.body.style.getPropertyValue('--tlh')!==hh+'px') document.body.style.setProperty('--tlh',hh+'px'); }
(function(){ const g=$('#tlGrip'); if(!g) return; let on=false;
  g.addEventListener('pointerdown',e=>{ on=true; g.setPointerCapture(e.pointerId); e.preventDefault(); });
  g.addEventListener('pointermove',e=>{ if(!on) return; TLH_USER=clamp(innerHeight-e.clientY,200,innerHeight-240); tlFit(); });
  g.addEventListener('pointerup',()=>{ if(!on) return; on=false; try{ localStorage.setItem('hs.tlh',String(Math.round(TLH_USER))); }catch(e){} buildTL(); });
  g.addEventListener('dblclick',()=>{ TLH_USER=null; try{ localStorage.removeItem('hs.tlh'); }catch(e){} buildTL(); }); })();
function drawWave(){ const cv=$('#wave'); if(!ST) return; const Wd=Math.min(16000,Math.max(1,Math.round(total()*PX))), H=32; cv.width=Wd; cv.height=H; cv.style.width=Wd+'px';
  const x=cv.getContext('2d'); x.fillStyle='#24251f'; x.fillRect(0,0,Wd,H); if(!PEAKS||!PEAKS.p.length) return; x.fillStyle='#8fa36f';
  for(let px=0;px<Wd;px++){ const a=Math.floor(vm(px/PX)*PEAKS.rate), b=Math.max(a+1,Math.floor(vm((px+1)/PX)*PEAKS.rate)); let m=0; for(let i=a;i<b&&i<PEAKS.p.length;i++) if(PEAKS.p[i]>m) m=PEAKS.p[i]; const hh=Math.max(1,m*(H-4)); x.fillRect(px,(H-hh)/2,1,hh); } }
function drawCheck(){ const el=$('#tChk'); if(!el) return; el.innerHTML=((RET&&RET.zones)||[]).map(z=>'<div class="rz '+z.lvl+'" style="left:'+(z.s*PX)+'px;width:'+((z.e-z.s)*PX)+'px"></div>').join('')+(CHECK&&CHECK.gaps||[]).map(g=>'<div class="gap" data-gap="'+g.s+'" title="'+esc(t('gapTitle',g.d))+'" style="left:'+(g.s*PX)+'px;width:'+((g.e-g.s)*PX)+'px"></div>').join(''); }
function shotBounds(){ return [...new Set([0,...(INFO.seams||[]),...MARKS,total()].map(v=>r3(v)))].filter(v=>v>=0&&v<=total()).sort((a,b)=>a-b); }
function tlTime(e,far){ const r=$('#lane').getBoundingClientRect(); return clamp((e.clientX-r.left)/PX,0,far?dur()+12:dur()); }
function snapPts(skip){ const p=[0,total(),T,...(INFO.seams||[]),...MARKS]; ST.caps.cards.forEach((c,i)=>{ if(!(skip&&skip.kind==='cap'&&skip.id===i)) p.push(c.s,c.e); });
  hs().layers.forEach(L=>{ if(!(skip&&skip.kind==='layer'&&skip.id===L.id)) p.push(L.s,L.e); }); return p; }
let ALT=false; function snapTo(x,pts){ if(!MAG||ALT) return x; let best=x, d=6/PX; for(const p of pts){ const dd=Math.abs(p-x); if(dd<d){ d=dd; best=p; } } return best; }
/* 3.9: الكابشن يتحرك داخل السكتة اللي حوله، والجيران يتقلصون لحد كلماتهم بدل ما يقفلونه */
function capNb(i){ const cs=ST.caps.cards, p=cs[i-1], n=cs[i+1]; return {p:p?{s:p.s,e:p.e}:null,n:n?{s:n.s,e:n.e}:null,lim:[p?p.w[p.w.length-1].e+0.02:0,n?n.w[0].s-0.02:total()]}; }
function capPush(D,o){ const i=+D.id, cs=ST.caps.cards, p=cs[i-1], n=cs[i+1];
  if(p&&D.nb.p){ p.e=r3(Math.max(p.w[p.w.length-1].e,Math.min(D.nb.p.e,o.s-0.02))); } if(n&&D.nb.n){ n.s=r3(Math.min(n.w[0].s,Math.max(D.nb.n.s,o.e+0.02))); }
  for(const [c,j] of [[p,i-1],[n,i+1]]){ if(!c) continue; const de=document.querySelector('#lane .clip[data-kind="cap"][data-id="'+j+'"]'); if(de){ de.style.left=(c.s*PX)+'px'; de.style.width=Math.max(7,(c.e-c.s)*PX-1)+'px'; } } }
function objOf(kind,id){ if(kind==='layer') return hs().layers.find(l=>l.id===id); if(kind==='cap') return ST.caps.cards[+id]; if(kind==='broll') return ST.studio.brollClips[+id]; return null; }
function select(s){ SEL=s; if(MOBILE&&s&&s.kind!=='cap') document.body.dataset.mv='panel'; if(s&&RTAB!=='sel'&&s.kind!=='cap'){ RTAB='sel'; markTabs(); } buildTL(); renderRight(); if(s&&s.kind==='cap'&&LTAB==='text'){ const el=$('#lbody .card[data-card="'+s.id+'"]'); $$('#lbody .card').forEach(c=>c.classList.toggle('on',c===el)); if(el) el.scrollIntoView({block:'nearest'}); } }
function blade(el,x){ const pts=snapPts(null); x=snapTo(x,pts);
  if(!el){ return; }
  const kind=el.dataset.kind, id=el.dataset.id;
  if(kind==='sfx'){ const [k,j]=String(id).split(':'), o=sxGet(k,+j); if(x<o.t+0.05||x>o.t+o.d-0.05) return; snap(); const d1=r3(x-o.t);
    sxPut(k,+j,{...o,d:d1,fo:Math.min(o.fo==null?0.25:o.fo,0.03)}); ST.studio.sfx[k].push(null); sxPut(k,ST.studio.sfx[k].length-1,{...o,t:r3(x),off:r3(o.off+d1),d:r3(o.d-d1),fi:0.02}); buildTL(); dirty(); toast(t('splitDone')); return; }
  if(kind==='layer'){ const L=objOf('layer',id); if(x<L.s+0.1||x>L.e-0.1) return; snap(); const h=hs(), n={...L,id:'L'+(Math.max(0,...h.layers.map(l=>parseInt(String(l.id).replace(/\D/g,''))||0))+1),s:r3(x)}; if(Array.isArray(L.kf)) n.kf=L.kf.map(k=>({...k,t:r3(k.t-(x-L.s))})); L.e=r3(x); h.layers.push(n); buildTL(); live(); toast(t('splitDone')); }
  else if(kind==='broll'){ const b=objOf('broll',id); if(x<b.s+0.1||x>b.e-0.1) return; snap(); ST.studio.brollClips.push({...b,s:r3(x)}); b.e=r3(x); buildTL(); dirty(); toast(t('splitDone')); }
  else if(kind==='cap'){ const i=+id, c=ST.caps.cards[i]; if(c.w.length<2) return; let j=1, bd=1e9; for(let k=1;k<c.w.length;k++){ const m=(c.w[k-1].e+c.w[k].s)/2, d=Math.abs(m-x); if(d<bd){ bd=d; j=k; } }
    snap(); const old=key(c), a=c.w.slice(0,j), b=c.w.slice(j), mid=r3((a[a.length-1].e+b[0].s)/2), c2={s:r3(Math.max(mid,b[0].s-0.08)),e:c.e,w:b}; c.w=a; c.e=r3(Math.min(mid,c2.s-0.02)); if(c.e<a[a.length-1].e) c.e=a[a.length-1].e;
    ST.caps.cards.splice(i+1,0,c2); const mp=hs().en.map; if(mp[old]){ mp[key(c)]=mp[old]; delete mp[old]; } buildTL(); renderLeft(); hard(); toast(t('splitDone')); } }
(function(){ const sc=$('#scroller'); let D=null;
  sc.addEventListener('pointerdown',e=>{ if(!ST||e.button>0) return; { const kd=e.target.closest('.kfd'); if(kd){ e.preventDefault(); e.stopPropagation(); const L=hs().layers.find(l=>l.id===kd.dataset.l); if(L){ if(playing) stop(); select({kind:'layer',id:L.id}); seek(r3(L.s+(+kd.dataset.t))); renderRight(); placeGiz(); } return; } } const x=tlTime(e), el=e.target.closest('.clip[data-kind]'), mk=e.target.closest('.mk'), gp=e.target.closest('.gap'), cb=e.target.closest('.cutbtn');
    if(cb){ e.preventDefault(); D={kind:'cbmaybe',seam:+cb.dataset.seam,x0:x,moved:false}; dragging=true; sc.setPointerCapture(e.pointerId); return; }   // 4.23: ضغطة = الانتقال، سحب = قص الطرف
    const rh=e.target.closest('.rl,.rr'); if(rh&&SEL&&(SEL.kind==='video'||SEL.kind==='audio')){ if(SEL.solo&&!!rh.closest('#tAu')!==(SEL.kind==='audio')) return; e.preventDefault(); if(playing) stop(); D={kind:'trim',side:rh.classList.contains('rr')?'r':'l',s:SEL.s,e:SEL.e,x:rh.classList.contains('rr')?SEL.e:SEL.s}; dragging=true; sc.setPointerCapture(e.pointerId); return; }
    if(mk){ if(mk.dataset.n){ seek(NOTES.find(n=>String(n.id)===mk.dataset.n).t); } else { seek(REV.comments.find(c=>String(c.id)===mk.dataset.c).t); } RTAB='notes'; markTabs(); renderRight(); return; }
    if(gp){ seek(+gp.dataset.gap+0.05); RTAB='check'; markTabs(); renderRight(); return; }
    const inFilm=!!e.target.closest('#tFilm,#tAu');
    if(TOOL==='blade'){ if(el) blade(el,x); else if(inFilm){ const m=r3(snapTo(x,[T,...(INFO.seams||[]),...ST.caps.cards.flatMap(c=>[c.s,c.e])])); if(m>0.1&&m<total()-0.1&&!MARKS.some(q=>Math.abs(q-m)<0.05)){ MARKS.push(m); MARKS.sort((a,b)=>a-b); marksSave(); buildTL(); toast(t('markAdded')); } } return; }
    if(playing) stop();
    if(el){ e.preventDefault(); ALT=e.altKey; const kind=el.dataset.kind, id=kind==='layer'?el.dataset.id:(kind==='sfx'?el.dataset.id:+el.dataset.id); select({kind,id});
      if(kind==='hook'){ D={kind,x0:x,o:hs().hooks.dur||2.6,edge:e.target.classList.contains('hr'),moved:false}; if(T>=(hs().hooks.dur||2.6)) seek(0.4); dragging=true; sc.setPointerCapture(e.pointerId); return; }
      if(kind==='outro'){ D={kind,x0:x,o:ST.outro,edge:e.target.classList.contains('hr'),moved:false}; if(!D.edge) seek(Math.min(dur()-0.05,total()+1.6)); dragging=true; sc.setPointerCapture(e.pointerId); return; }
      const mode=e.target.classList.contains('hl')?'l':e.target.classList.contains('hr')?'r':'move';
      if(kind==='sfx'){ const [k,j]=String(id).split(':'); D={kind,k,j:+j,x0:x,orig:ST.studio.sfx[k][+j],o:sxGet(k,+j),mode,moved:false}; }
      else { const o=objOf(kind,id); D={kind,id,mode,x0:x,y0:e.clientY,s:o.s,e:o.e,track:o.track||0,moved:false,pts:snapPts({kind,id}),words:kind==='cap'?o.w.map(w=>[w.s,w.e]):null,nb:kind==='cap'?capNb(+id):null}; }
      dragging=true; sc.setPointerCapture(e.pointerId); return; }
    if(e.target.closest('#tAu .mus')){ select({kind:'music',id:0}); return; }
    if(e.target.closest('.vr')){ const i=+e.target.closest('.vr').dataset.vr; select({kind:'vr',id:i}); RTAB='sel'; markTabs(); renderRight(); return; }
    if(e.target.closest('#tAu')&&TOOL==='select'){ D={kind:'vsel',x0:x,moved:false}; dragging=true; sc.setPointerCapture(e.pointerId); seek(x); return; }
    if(e.target.closest('#tFilm .blk')){ select({kind:'blank',id:+e.target.closest('.blk').dataset.blk}); return; }
    { const nb=inFilm&&TOOL==='select'?edgeNear(x,e.target):null; if(nb){ select({kind:'video',s:nb.s,e:nb.e,id:nb.i,solo:!LINK}); D={kind:'trim',side:nb.side,s:nb.s,e:nb.e,x:nb.side==='r'?nb.e:nb.s}; dragging=true; sc.setPointerCapture(e.pointerId); return; } }
    if(inFilm&&!e.target.closest('#tAu')&&SEL&&SEL.kind==='video'&&x>SEL.s&&x<SEL.e){ D={kind:'mvshot',s:SEL.s,e:SEL.e,x0:x,moved:false,to:null}; dragging=true; sc.setPointerCapture(e.pointerId); return; }
    if(inFilm){ const b=shotBounds(); for(let i=0;i<b.length-1;i++){ if(x>=b[i]&&x<b[i+1]){ select({kind:'video',s:b[i],e:b[i+1],id:i,solo:!LINK}); break; } } }
    else if(SEL){ SEL=null; buildTL(); renderRight(); }
    D={kind:'scrub'}; dragging=true; sc.setPointerCapture(e.pointerId); seek(x); });
  sc.addEventListener('pointermove',e=>{ if(D&&D.kind!=='scrub'){ const r=sc.getBoundingClientRect(); if(e.clientX>r.right-36) sc.scrollLeft+=14; else if(e.clientX<r.left+36) sc.scrollLeft-=14; }
    const x=tlTime(e,D&&D.kind==='outro');
    if(!D){ if(ST){ const ed_=e.target.closest('#tFilm')&&TOOL==='select'?edgeNear(x,e.target):null; sc.style.cursor=ed_?'col-resize':''; }
      if(SKIM&&!playing&&ST){ $('#sk').style.display='block'; $('#sk').style.left=(x*PX)+'px'; drawT(x); } return; }
    if(D.kind==='scrub'){ seek(x); return; }
    if(D.kind==='cbmaybe'){ if(Math.abs(x-D.x0)*PX<5) return; const b=shotBounds(), i=b.findIndex(v=>Math.abs(v-D.seam)<1e-3); if(i<1){ D={kind:'scrub'}; return; }
      if(x<D.seam){ select({kind:'video',s:b[i-1],e:b[i],id:i-1,solo:!LINK}); D={kind:'trim',side:'r',s:b[i-1],e:b[i],x:b[i]}; } else if(i<b.length-1){ select({kind:'video',s:b[i],e:b[i+1],id:i,solo:!LINK}); D={kind:'trim',side:'l',s:b[i],e:b[i+1],x:b[i]}; } else { D={kind:'scrub'}; return; } }
    if(D.kind==='mvshot'){ if(!D.moved&&Math.abs(x-D.x0)*PX<8) return; D.moved=true; const b=shotBounds().filter(v=>v<=D.s+1e-3||v>=D.e-1e-3); let best=null, bd=1e9; for(const v of b){ const d=Math.abs(v-x); if(d<bd){ bd=d; best=v; } } D.to=(best!=null&&Math.abs(best-D.s)>0.01&&Math.abs(best-D.e)>0.01)?best:null; mvMark(D.to); mvGhost(D.s,D.e,D.x0,x); return; }
    if(D.kind==='vsel'){ if(!D.moved&&Math.abs(x-D.x0)*PX<4) return; D.moved=true; const s=r3(Math.max(0,Math.min(D.x0,x))), en=r3(Math.min(total(),Math.max(D.x0,x))); SEL={kind:'voice',s,e:en}; vrDraw(); return; }
    if(D.kind==='trim'){ D.x=D.side==='r'?clamp(snapTo(x,[T,...ST.caps.cards.flatMap(c=>[c.s,c.e])]),D.s+0.15,D.e):clamp(snapTo(x,[T,...ST.caps.cards.flatMap(c=>[c.s,c.e])]),D.s,D.e-0.15);
      const a=D.side==='r'?[D.x,D.e]:[D.s,D.x]; trimBadge(e.clientX,e.clientY,a[1]-a[0]); document.querySelectorAll(SEL&&SEL.solo?(SEL.kind==='audio'?'#tAu .trim':'#tFilm .trim'):'#tFilm .trim,#tAu .trim').forEach(tm=>{ tm.style.display='block'; tm.style.left=(a[0]*PX)+'px'; tm.style.width=((a[1]-a[0])*PX)+'px'; }); drawT(D.x); return; }
    let dt=x-D.x0; const vy=D.kind==='layer'&&D.mode==='move'&&Math.abs(e.clientY-D.y0)>=6; if(!D.moved&&Math.abs(dt)*PX<3&&!vy) return; if(!D.moved){ D.moved=true; snap(); }
    if(D.kind==='layer'&&D.mode==='move'&&Math.abs(dt)*PX<8) dt=0;   // سحب لفوق أو لتحت بس: الوقت ما يتغيّر
    if(D.kind==='hook'){ if(!D.edge) return; const H=hs().hooks; H.dur=r3(clamp(D.o+dt,0.8,8)); const he=document.querySelector('#tLs .clip.hook'); if(he) he.style.width=Math.max(7,H.dur*PX-1)+'px'; const w=F.contentWindow; if(w&&w.hsSet) w.hsSet(ST.studio.hs); return; }
    if(D.kind==='outro'){ if(!D.edge) return; ST.outro=r3(clamp(D.o+dt,0.8,12)); const oe=document.querySelector('#tFilm .clip.outro'); if(oe) oe.style.width=Math.max(7,ST.outro*PX-1)+'px'; $('#lane').style.width=Math.max(dur()*PX+80,sc.clientWidth)+'px'; $('#tm').textContent=fmt(T)+' / '+fmt(dur()); return; }
    if(D.kind==='sfx'){ const o={...D.o}, pts=[T,...ST.caps.cards.flatMap(c=>c.w.map(w=>w.s))];
      if(D.mode==='move') o.t=r3(clamp(snapTo(D.o.t+dt,pts),0,total()));
      else if(D.mode==='r') o.d=r3(clamp(D.o.d+dt,0.1,Math.max(0.1,D.o.L-D.o.off)));
      else { const m=clamp(dt,-D.o.off,D.o.d-0.1); o.t=r3(D.o.t+m); o.off=r3(D.o.off+m); o.d=r3(D.o.d-m); }
      sxPut(D.k,D.j,o); const de=document.querySelector('#lane .clip.sfx[data-id="'+D.k+':'+D.j+'"]'); if(de){ de.style.left=(o.t*PX)+'px'; de.style.width=Math.max(24,o.d*PX-1)+'px'; } else buildTL(); return; }
    const o=objOf(D.kind,D.id), len=D.e-D.s, lim=D.kind==='cap'?D.nb.lim:[0,total()];
    if(D.mode==='move'){ let s=D.s+dt; const s1=snapTo(s,D.pts), e1=snapTo(s+len,D.pts); if(s1!==s) s=s1; else if(e1!==s+len) s=e1-len; s=clamp(s,lim[0],Math.max(lim[0],lim[1]-len)); const d=s-D.s; o.s=r3(s); o.e=r3(s+len);
      if(D.kind==='cap'){ o.w.forEach((w,i)=>{ w.s=r3(D.words[i][0]+d); w.e=r3(D.words[i][1]+d); }); capPush(D,o); if(Math.abs(D.s+dt-s)*PX>24&&!D.told){ D.told=1; toast(t('capLimit')); } }
      if(D.kind==='layer'){ const r=$('#tLs').getBoundingClientRect(), i=Math.floor((e.clientY-r.top)/21); if(D.row0==null){ const w=layerRows().where[D.id]; D.row0=Math.max(0,LROWS.findIndex(x=>!x.add&&w&&x.track===w[0]&&x.sub===w[1])); } D.row=clamp(i,0,LROWS.length-1); } }
    else if(D.mode==='l'){ let s=clamp(snapTo(D.s+dt,D.pts),lim[0],D.e-0.15); o.s=r3(s);   /* 4.29: الكابشن يتقصّر بحرية، ما يتقيّد بكلماته */ if(D.kind==='cap') capPush(D,o); if(D.kind==='layer'&&Array.isArray(o.kf)&&o.kf.length){ if(!D.kf0) D.kf0=o.kf.map(k=>({...k})); o.kf=D.kf0.map(k=>({...k,t:r3(k.t+(D.s-o.s))})); } }
    else { let en=clamp(snapTo(D.e+dt,D.pts),D.s+0.15,lim[1]); o.e=r3(en); if(D.kind==='cap') capPush(D,o); }
    const dl=document.querySelector('#lane .clip[data-kind="'+D.kind+'"][data-id="'+D.id+'"]');
    if(!dl) buildTL(); else { dl.style.left=(o.s*PX)+'px'; dl.style.width=Math.max(7,(o.e-o.s)*PX-1)+'px'; if(D.kind==='layer'&&D.row!=null) dl.style.transform='translateY('+((D.row-D.row0)*21)+'px)'; }
    if(!D.raf) D.raf=requestAnimationFrame(()=>{ if(D) D.raf=0; drawT(T); placeGiz(); }); });
  const end=()=>{ if(D&&D.kind==='cbmaybe'){ const s_=D.seam; D=null; dragging=false; seamPick(s_); return; }
    if(D&&D.kind==='mvshot'){ const d=D; D=null; dragging=false; mvMark(null); mvGhost(null); if(d.moved&&d.to!=null) moveShot(d.s,d.e,d.to); else seek(d.x0); return; }
    if(D&&!D.moved&&D.x0!=null&&['layer','cap','sfx','hook','broll'].includes(D.kind)) seek(D.x0);   // 4.21: الضغط على أي شي بالتايم لاين ينقل المعاينة له
    if(D&&D.kind==='vsel'){ const mv=D.moved, x0=D.x0; D=null; dragging=false;
      if(mv&&SEL&&SEL.kind==='voice'&&SEL.e-SEL.s>=0.05){ RTAB='sel'; markTabs(); renderRight(); }
      else auSelectAt(x0); return; }
    if(D&&D.kind==='trim'){ trimBadge(); const a=D.side==='r'?[D.x,D.e]:[D.s,D.x]; document.querySelectorAll('#tFilm .trim,#tAu .trim').forEach(tm=>tm.style.display='none'); D=null; dragging=false; if(a[1]-a[0]<0.08) return;
      if(SEL&&SEL.solo&&SEL.kind==='audio'){ rngSet(a[0],a[1],0); toast(t('delAudioDone')); return; }
      if(SEL&&SEL.solo&&SEL.kind==='video'){ blankAdd(a[0],a[1]); toast(t('delVideoDone')); return; }
      askRemove({ranges:[[r3(a[0]),r3(a[1])]]},fmt(a[0])+' ← '+fmt(a[1])); return; }
    if(D&&D.kind==='hook'){ const mv=D.moved; D=null; dragging=false; ALT=false; if(mv){ buildTL(); renderRight(); live(); } return; }
    if(D&&D.kind==='outro'){ const mv=D.moved; D=null; dragging=false; ALT=false; if(mv){ buildTL(); renderRight(); hard(); } return; }
    if(D&&D.moved&&D.kind==='layer'&&D.row!=null&&D.row!==D.row0) layerToRow(D.id,D.row,D.row0);
    if(D&&D.moved){ buildTL(); if(D.kind==='layer') live(); else dirty(); if(D.kind!=='sfx') renderRight(); } D=null; dragging=false; ALT=false; };
  sc.addEventListener('pointerup',end); sc.addEventListener('pointercancel',end);
  sc.addEventListener('pointerleave',()=>{ if(SKIM&&!D){ $('#sk').style.display='none'; drawT(T); } });
  sc.addEventListener('scroll',()=>{ $('#gut').scrollTop=sc.scrollTop; });
  sc.addEventListener('wheel',e=>{ if(e.ctrlKey||e.metaKey){ e.preventDefault(); setZoom(PX*(e.deltaY<0?1.15:0.87)); } },{passive:false});
})();
function setZoom(v){ PX=clamp(v,16,260); $('#zoom').value=PX; buildTL(); const sc=$('#scroller'); sc.scrollLeft=Math.max(0,T*PX-sc.clientWidth/2); }
$('#zoom').oninput=e=>setZoom(+e.target.value);
$$('[data-tool]').forEach(b=>b.onclick=()=>{ TOOL=b.dataset.tool; markTabs(); });
$('#bMag').onclick=()=>{ MAG=!MAG; markTabs(); };
function linkToggle(){ LINK=!LINK; try{ localStorage.setItem('hs.link',LINK?'1':'0'); }catch(e){} if(SEL&&(SEL.kind==='audio'||SEL.kind==='video')) SEL={...SEL,solo:!LINK}; markTabs(); buildTL(); renderRight(); toast(t(LINK?'linkOn':'linkOff')); }
if($('#bLink')) $('#bLink').onclick=linkToggle; $('#bSkim').onclick=()=>{ SKIM=!SKIM; markTabs(); if(!SKIM){ $('#sk').style.display='none'; drawT(T); } };
const OUTRO_DEF={l1:'شكراً على المشاهدة',l2:'',cta:'تابعني',word:'للمزيد',sub:'',chips:[]};
function outroT(){ return {...DF('outro'),...(ST.studio.outro||{})}; }
function outroSet(sec){ snap(); ST.outro=sec; if(sec>0&&!ST.studio.outro) ST.studio.outro=DF('outro'); if(sec>0) SEL={kind:'outro',id:0}; else if(SEL&&SEL.kind==='outro') SEL=null; buildTL(); renderRight(); hard().then(()=>seek(sec>0?Math.min(dur()-0.05,total()+1.6):Math.min(T,dur()))); }
function delSel(){ if(!SEL) return; const h=hs();
  if(SEL.kind==='hook'){ snap(); h.hooks.on=false; SEL=null; live(); buildTL(); renderRight(); placeGiz(); toast(t('hookOffDone')); return; }
  if(SEL.kind==='outro'){ outroSet(0); return; }
  if(SEL.kind==='vr'){ snap(); (h.mix.vr||[]).splice(+SEL.id,1); SEL=null; vrDraw(); renderRight(); dirty(); return; }
  if(SEL.kind==='music'){ snap(); h.mix.bg=0; if(MUP){ MUP.pause(); MUP=null; } vrDraw(); renderRight(); dirty(); toast(t('musOff')); return; }
  if(SEL.kind==='blank'){ (h.blank||[]).splice(+SEL.id,1); SEL=null; buildTL(); renderRight(); live(); return; }
  if((SEL.kind==='audio'||SEL.kind==='video')&&SEL.solo){ avDel(SEL.kind); return; }
  if(SEL.kind==='voice'||SEL.kind==='audio'){ askRemove({ranges:[[r3(SEL.s),r3(SEL.e)]]},fmt(SEL.s)+' ← '+fmt(SEL.e)); return; }
  if(SEL.kind==='layer'){ snap(); h.layers=h.layers.filter(l=>l.id!==SEL.id); ST.studio.hs.layers=h.layers; SEL=null; buildTL(); renderRight(); live(); }
  else if(SEL.kind==='sfx'){ snap(); const [k,j]=String(SEL.id).split(':'); ST.studio.sfx[k].splice(+j,1); SEL=null; buildTL(); renderRight(); dirty(); }
  else if(SEL.kind==='broll'){ snap(); ST.studio.brollClips.splice(+SEL.id,1); SEL=null; buildTL(); renderRight(); dirty(); drawT(T); }
  else if(SEL.kind==='cap'){ askRemove({cards:[+SEL.id]},'«'+key(ST.caps.cards[+SEL.id])+'»'); }
  else if(SEL.kind==='video'){ askRemove({ranges:[[SEL.s,SEL.e]]},fmt(SEL.s)+' ← '+fmt(SEL.e)); } }
function dupSel(){ const L=selLayer(); if(!L) return; snap(); const h=hs(), n={...L,id:'L'+(Math.max(0,...h.layers.map(l=>parseInt(String(l.id).replace(/\D/g,''))||0))+1)}; const d=L.e-L.s; n.s=r3(Math.min(L.e,total()-0.3)); n.e=r3(Math.min(total(),n.s+d)); h.layers.push(n); select({kind:'layer',id:n.id}); live(); }

/* ───── عناصر الواجهة العامة ───── */
const vid=k=>'v-'+k.replace(/\./g,'-');
/* 4.39: شيل الشاشة الخضراء من لقطة البي-رول */
function keyPanel(b){ const K=b.key||{}, on=!!K.on, c=K.color||'auto', pre=['auto','#00B140','#0047BB'], hx=/^#[0-9a-f]{6}$/i.test(c)?c:((ST.studio.brKey||{})[b.k]||'#00B140');
  let o='<div class="sec"><h4>'+t('brKey')+'</h4>'+seg(t('brKeyOn'),'B.key.on',[[true,t('yes')],[false,t('no')]],on);
  if(on){ o+=seg(t('brKeyCol'),'B.key.color',[['auto',t('brKeyAuto')],['#00B140',t('brKeyGreen')],['#0047BB',t('brKeyBlue')]],pre.includes(c)?c:'')
      +'<div class="row"><label>'+t('brKeyPick')+'</label><input type="color" data-k="B.key.color" value="'+esc(hx)+'"></div>'
      +slider(t('brKeySim'),'B.key.sim',0,100,K.sim==null?40:K.sim)+slider(t('brKeySoft'),'B.key.soft',0,100,K.soft==null?12:K.soft)+slider(t('brKeySpill'),'B.key.spill',0,100,K.spill==null?60:K.spill);
    if((b.mode||'full')==='full') o+=slider(t('brKeySize'),'B.ks',20,200,b.ks==null?100:b.ks)+slider(t('brKeyX'),'B.kx',-540,540,b.kx||0,2)+slider(t('brKeyY'),'B.ky',-960,960,b.ky||0,2); }
  return o+'<p class="hint">'+t('brKeyHint')+'</p></div>'; }
function slider(lbl,k,min,max,val,step){ return '<div class="row"><label>'+lbl+'</label><input type="range" data-k="'+k+'" min="'+min+'" max="'+max+'" step="'+(step||1)+'" value="'+val+'"><span class="val" id="'+vid(k)+'">'+val+'</span></div>'; }
function swatches(lbl,k,val){ val=val||'#FFFFFF'; return '<div class="row"><label>'+lbl+'</label><div class="sw">'+SWATCH.map(c=>'<i data-k="'+k+'" data-c="'+c+'" class="'+(c.toLowerCase()===String(val).toLowerCase()?'on':'')+'" style="background:'+c+'"></i>').join('')+'<input type="color" data-k="'+k+'" value="'+esc(val)+'"></div></div>'; }
function seg(lbl,k,opts,val){ return '<div class="row"><label>'+lbl+'</label><div class="seg">'+opts.map(o=>'<button data-k="'+k+'" data-v="'+o[0]+'" class="'+(String(o[0])===String(val)?'on':'')+'">'+o[1]+'</button>').join('')+'</div></div>'; }
function pick(lbl,k,opts,val){ return '<div class="row"><label>'+lbl+'</label><select data-k="'+k+'">'+opts.map(o=>{ const [v,l]=Array.isArray(o)?o:[o,o]; return '<option value="'+esc(v)+'"'+(String(v)===String(val)?' selected':'')+'>'+esc(l)+'</option>'; }).join('')+'</select></div>'; }
function tog(k,title,sub,val){ return '<div class="tog"><div>'+title+(sub?'<small>'+sub+'</small>':'')+'</div><div class="sw-t'+(val?' on':'')+'" data-tog="'+k+'"></div></div>'; }
function ref(k){ const p=k.split('.'); let o; if(p[0]==='L') o=selLayer(); else if(p[0]==='th') o=ST.theme; else if(p[0]==='B') o=ST.studio.brollClips[+SEL.id]; else if(p[0]==='C'){ hs().cap.on=true; o=SCOPE==='all'?hs().cap:capOvOf(+SEL.id,true); } else { const h=hs(); o=h[p[0]]; } for(let i=1;i<p.length-1;i++){ o[p[i]]=o[p[i]]||{}; o=o[p[i]]; } return [o,p[p.length-1]]; }
const getK=k=>{ const [o,f]=ref(k); return o?o[f]:undefined; }, setK=(k,v)=>{ const [o,f]=ref(k); if(o) o[f]=v; if(k==='L.kind'&&o&&o.type==='anno'){ const D=DF('an',v)||{}; for(const x in D) if(o[x]==null) o[x]=JSON.parse(JSON.stringify(D[x])); } if(k==='L.move'&&o) o.kb=v!=='none'; };
function weightsOf(f){ const w=F.contentWindow, G=(w&&w.__hsFonts)||{}; return G[f]||[400,500,600,700,800,900]; }
function fontLink(){ if($('#fprev')) return; const l=document.createElement('link'); l.id='fprev'; l.rel='stylesheet'; l.href='https://fonts.googleapis.com/css2?'+AR_FONTS.map(f=>'family='+encodeURIComponent(f).replace(/%20/g,'+')+':wght@700').join('&')+'&text='+encodeURIComponent('متابعة')+'&display=swap'; document.head.appendChild(l); }
function localFace(f){ const id='lf-'+f.file; if(document.getElementById(id)) return; const st=document.createElement('style'); st.id=id; st.textContent='@font-face{font-family:"'+f.name+'";src:url("/fonts/'+encodeURIComponent(f.file)+'")'+(f.weight?';font-weight:'+f.weight:'')+'}'; document.head.appendChild(st); }
function renderAll(){ markTabs(); renderLeft(); renderRight(); }

/* ───── اليسار: النص + الملفات ───── */
/* ═══ 4.11: تعديل تراك الصوت (مستوى، قص، ظهور واختفاء) ومستوى صوتك لأجزاء، وشيل الخلفية ═══ */
function sxLen(k){ const it=SFXLIB.find(x=>x.id===k); return it&&parseFloat(it.dur)>0?parseFloat(it.dur):({whoosh_up:0.34,whoosh_down:0.3,thud:0.3,tap:0.09})[k]||1; }
function sxGet(k,j){ const v=((ST.studio.sfx||{})[k]||[])[j]; const a=Array.isArray(v)?v:[v], L=sxLen(k), off=+a[3]||0; return {t:+a[0]||0, g:a[1]==null?1:+a[1], d:a[2]==null?Math.max(0.1,L-off):+a[2], off, fi:+a[4]||0, fo:a[5]==null?null:+a[5], L}; }
function sxPut(k,j,o){ const full=Math.abs(o.d-(o.L-o.off))<0.02, arr=[r3(o.t),r3(o.g),full?null:r3(o.d),r3(o.off||0),r3(o.fi||0),o.fo==null?null:r3(o.fo)], def=[null,1,null,0,0,null];
  while(arr.length>1&&arr[arr.length-1]===def[arr.length-1]) arr.pop(); ST.studio.sfx[k][j]=arr.length===1?arr[0]:arr; }
let SXP=[];
function sxStopAll(){ SXP.forEach(p=>{ try{ p.au.pause(); }catch(e){} }); SXP=[]; }
function sxTick(x){ const sf=ST.studio.sfx||{}, mix=hs().mix;
  for(const k in sf){ if(!Array.isArray(sf[k])||k==='soft') continue; sf[k].forEach((v,j)=>{ const o=sxGet(k,j), id=k+':'+j, end=o.t+o.d, inside=x>=o.t&&x<end; let p=SXP.find(q=>q.id===id);
    if(inside&&!p){ try{ const au=new Audio('/sfx_prev/'+k+'.wav'); au.currentTime=o.off+(x-o.t); p={id,au}; SXP.push(p); au.play().catch(()=>{}); }catch(e){} }
    if(p&&!inside){ try{ p.au.pause(); }catch(e){} SXP=SXP.filter(q=>q!==p); return; }
    if(p){ const base=(o.L>8?0.35:0.55)*(mix.sfx&&mix.sfx[k]!=null?mix.sfx[k]:1), fo=o.fo==null?0.25:o.fo; let env=1; if(o.fi>0) env=Math.min(env,(x-o.t)/o.fi); if(fo>0) env=Math.min(env,(end-x)/fo); p.au.volume=clamp(base*o.g*clamp(env,0,1),0,1); } }); } }
function vrAt(x){ return (hs().mix.vr||[]).find(r=>x>=r.s&&x<r.e)||null; }
/* 4.13: صوتك مقاطع زي أي برنامج مونتاج: تضغط وحدة تتحدد (وتتحدد صورتها معها)، تسحب طرفها تقصها، تقسمها بالمقص، وتحذفها أو تكتمها */
function auSelectAt(x){ const b=shotBounds(); for(let i=0;i<b.length-1;i++){ if(x>=b[i]&&x<b[i+1]){ select({kind:'audio',s:b[i],e:b[i+1],id:i,solo:!LINK}); return; } } }
function marksSave(){ hs().marks=MARKS.slice(); dirty(); }
/* «الصورة بس» تنحذف: الجزء يصير أسود وصوتك يكمل */
function blankAdd(s,e){ const h=hs(); h.blank=vrCut(h.blank||[],s,e); h.blank.push({s:r3(s),e:r3(e)}); h.blank.sort((a,b)=>a.s-b.s); buildTL(); live(); }
function avDel(what){ if(!SEL) return; const s=SEL.s, e=SEL.e; if(what==='audio'){ rngSet(s,e,0); toast(t('delAudioDone')); renderRight(); return; }
  if(what==='video'){ blankAdd(s,e); toast(t('delVideoDone')); renderRight(); return; } askRemove({ranges:[[r3(s),r3(e)]]},fmt(s)+' ← '+fmt(e)); }
function auClips(el){ el.querySelectorAll('.aclip,.trim,.cutgap').forEach(n=>n.remove()); const b=shotBounds();
  for(let i=0;i<b.length-1;i++){ const d=document.createElement('div'), sel=SEL&&(SEL.kind==='audio'||(SEL.kind==='video'&&!SEL.solo))&&Math.abs(SEL.s-b[i])<0.002&&Math.abs(SEL.e-b[i+1])<0.002; d.className='aclip'+(sel?' on':''); d.style.left=(b[i]*PX)+'px'; d.style.width=Math.max(2,(b[i+1]-b[i])*PX)+'px'; if(sel) d.innerHTML='<i class="rl"></i><i class="rr"></i>'; el.appendChild(d); }
  for(let i=1;i<b.length-1;i++){ const g=document.createElement('div'); g.className='cutgap'; g.style.left=(b[i]*PX)+'px'; el.appendChild(g); }
  const tr=document.createElement('div'); tr.className='trim'; el.appendChild(tr); }
function vrDraw(){ const el=$('#tAu'); if(!el) return; el.querySelectorAll('.vr,.vsel,.mus').forEach(n=>n.remove()); const h=hs(); auClips(el);
  if(INFO&&INFO.music){ const d=document.createElement('div'); d.className='mus'+(SEL&&SEL.kind==='music'?' on':''); d.style.width=Math.max(20,total()*PX)+'px'; d.title=t('musTitle')+': '+INFO.music; d.textContent=t('musTitle')+' · '+INFO.music+' · ×'+(h.mix.bg==null?0.28:h.mix.bg); el.appendChild(d); }
  (h.mix.vr||[]).forEach((r,i)=>{ const d=document.createElement('div'); d.className='vr'+(r.g===0?' m':'')+(SEL&&SEL.kind==='vr'&&+SEL.id===i?' on':''); d.dataset.vr=i; d.style.left=(r.s*PX)+'px'; d.style.width=Math.max(4,(r.e-r.s)*PX)+'px'; d.title=r.g===0?t('vMuted'):'×'+r.g; d.textContent=r.g===0?t('vMuted'):'×'+r.g; el.appendChild(d); });
  ['vkf','mkf'].forEach(k=>(h.mix[k]||[]).forEach(p=>{ const d=document.createElement('b'); d.className='gkd'+(k==='mkf'?' mus':''); d.style.left=(p.t*PX)+'px'; d.title=fmt(p.t)+' · '+Math.round(p.g*100)+'%'; el.appendChild(d); }));   // 4.56
  if(SEL&&SEL.kind==='voice'){ const d=document.createElement('div'); d.className='vsel'; d.style.left=(SEL.s*PX)+'px'; d.style.width=Math.max(2,(SEL.e-SEL.s)*PX)+'px'; el.appendChild(d); } }
function vrAdd(s,e,g){ snap(); const h=hs(); h.mix.vr=vrCut(h.mix.vr,s,e); h.mix.vr.push({s:r3(s),e:r3(e),g:r3(g)}); h.mix.vr.sort((a,b)=>a.s-b.s); const i=h.mix.vr.findIndex(r=>r.s===r3(s)); SEL={kind:'vr',id:i}; vrDraw(); renderRight(); dirty(); }
async function audioClick(el){ const b=el.closest('[data-sxplay],[data-sxhere],[data-vact],[data-vrdel],[data-rmbg],[data-svab],[data-muplay],[data-auact]'); if(!b) return false; const d=b.dataset;
  if(d.auact==='unblank'&&SEL&&SEL.kind==='blank'){ hs().blank.splice(+SEL.id,1); SEL=null; buildTL(); renderRight(); live(); return true; }
  if(d.auact&&SEL&&(SEL.kind==='audio'||SEL.kind==='video')){ const s=SEL.s, e=SEL.e;
    if(d.auact==='unmute'){ rngSet(s,e,1); renderRight(); return true; }
    if(d.auact==='split'){ splitAt(T); return true; }
    if(d.auact==='del'){ avDel('both'); return true; }
    if(d.auact==='delA'){ avDel('audio'); return true; }
    if(d.auact==='delV'){ avDel('video'); return true; } }
  if(d.svab){ if(SVS.ab!==d.svab){ SVS.ab=d.svab; auSwap(); } renderRight(); return true; }
  if(d.muplay){ if(MUP){ MUP.pause(); MUP=null; } else { MUP=new Audio(hs().mix.fit?'/hs/mfit.wav?v='+Date.now():'/'+encodeURIComponent(INFO.music||'')); MUP.volume=clamp(hs().mix.bg==null?0.28:hs().mix.bg,0,1); MUP.loop=true; MUP.play().catch(()=>{ MUP=null; renderRight(); }); } renderRight(); return true; }
  if(d.sxplay&&SEL&&SEL.kind==='sfx'){ const [k,j]=String(SEL.id).split(':'), o=sxGet(k,+j); sxStopAll(); const au=new Audio('/sfx_prev/'+k+'.wav'); au.currentTime=o.off; au.volume=clamp(0.6*o.g,0,1); au.play().catch(()=>{}); SXP.push({id:'_p',au}); setTimeout(()=>{ try{ au.pause(); }catch(e){} },o.d*1000); return true; }
  if(d.sxhere&&SEL&&SEL.kind==='sfx'){ snap(); const [k,j]=String(SEL.id).split(':'), o=sxGet(k,+j); o.t=r3(T); sxPut(k,+j,o); buildTL(); renderRight(); dirty(); return true; }
  if(d.vact&&SEL&&SEL.kind==='voice'){ const s=SEL.s, e=SEL.e;
    if(d.vact==='cut'){ askRemove({ranges:[[r3(s),r3(e)]]},fmt(s)+' ← '+fmt(e)); return true; }
    vrAdd(s,e,d.vact==='mute'?0:d.vact==='low'?0.5:1.5); toast(t('vDone')); return true; }
  if(d.vrdel&&SEL&&SEL.kind==='vr'){ snap(); hs().mix.vr.splice(+SEL.id,1); SEL=null; vrDraw(); renderRight(); dirty(); return true; }
  if(d.rmbg){ const L=selLayer(); if(!L||L.type!=='image') return true;
    if(d.rmbg==='undo'){ snap(); L.src=L.srcOrig; delete L.srcOrig; renderRight(); live(); return true; }
    if(d.rmbg==='claude'){ const r=await api('/hs/claude_fix',{what:'rmbg',src:L.srcOrig||L.src}); toast((r&&srvEn(r.msg))||t(r&&r.ok?'rbClaudeSent':'failed')); return true; }
    toast(t('rbWorking')); await save(); const r=await api('/hs/rmbg',{src:L.srcOrig||L.src,mode:'auto'});
    if(r&&r.ok){ snap(); if(!L.srcOrig) L.srcOrig=L.src; L.src=r.src; renderRight(); await live(); toast(t(r.mode==='person'?'rbDonePerson':'rbDone')); }
    else toast(t('rbFail')); return true; }
  return false; }
/* ═══ 4.10: خطوات المشروع · الفحص الجديد · الخطة قبل البناء ═══ */
let STEPS=null, PLAN=null;
async function loadSteps(){ try{ const r=await api('/hs/steps'); const prev=STEPS; STEPS=r.steps||null; stepNews(prev,STEPS); const el=$('#stepsbar'); if(el) el.outerHTML=stepsBar(); }catch(e){} }
/* 4.47: الخطوات تمشي معك: كل ما تخلص خطوة يطلع لك خبر «خلصنا… والحين…» */
function stepNews(a,b){ if(!a||!b) return; const done=b.filter(s=>s.state==='done'&&(a.find(x=>x.k===s.k)||{}).state!=='done'); if(!done.length) return; const nx=b.find(s=>s.state==='now'), last=done[done.length-1];
  let w=$('#stepnews'); if(!w){ w=document.createElement('div'); w.id='stepnews'; document.body.appendChild(w); }
  w.innerHTML='<b>✓ '+esc(srvEn(last.label))+'</b><span>'+(nx?t('stepNext',esc(srvEn(nx.label))):t('stepAll'))+'</span>'; w.classList.remove('on'); void w.offsetWidth; w.classList.add('on'); clearTimeout(w._t); w._t=setTimeout(()=>w.classList.remove('on'),5200); }
setInterval(()=>{ if(ST&&document.visibilityState==='visible') loadSteps(); },9000);
function stepsLive(){ const b=$('#stepsbar'); if(!b||!STEPS) return; const cur=$('#planv')?'plan':LTAB==='takes'?'takes':LTAB==='audio'?'audio':LTAB==='text'?'caps':LTAB==='files'?'build':RTAB==='plan'?'plan':RTAB==='claude'?'notes':''; b.querySelectorAll('.stp').forEach(x=>x.classList.toggle('cur',x.dataset.step===cur)); }
function stepsBar(){ if(!STEPS) return '<div id="stepsbar"></div>'; return '<div id="stepsbar" class="steps">'+STEPS.map(s=>'<button class="stp '+s.state+'" data-step="'+s.k+'"><i>'+(s.state==='done'?'<svg width="10" height="10" viewBox="0 0 24 24"><path d="M5 12l5 5 9-10" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>':s.n)+'</i>'+esc(srvEn(s.label))+'</button>').join('')+'</div>'; }
/* 4.43: الخطوات: مقطع جديد من المكتبة يفتح على «اختر الجمل»، وقبل القص ما يبان إلا المساعد؛ وبعد ما يعتمد القص تظهر باقي الأدوات */
let GUIDE_INIT=false, TKEDIT=false;
function guidePre(){ const h=ST&&hs(); return !!(h&&h.guide&&!h.stepTakes); }
function guideSync(){ const pre=guidePre(); document.body.classList.toggle('guide-pre',pre); document.body.classList.toggle('guide',!!(ST&&hs().guide));
  if(ST&&hs().guide&&!GUIDE_INIT){ GUIDE_INIT=true; const cur=(STEPS||[]).find(x=>x.state==='now'); if(pre||!cur){ LTAB='takes'; if(INFO.claude){ document.body.classList.add('asking'); RTAB='claude'; } markTabs(); renderLeft(); renderRight(); loadTakes(); } else stepGo(cur.k); } }
async function guideTakesDone(){ hs().stepTakes=1; TKEDIT=false; await save(); guideSync(); await loadSteps(); if(document.body.classList.contains('asking')) askClose(); toast(t('tkCutToast')); stepGo('audio'); }
async function guideAudioDone(){ hs().stepAudio=1; await save(); await loadSteps(); stepGo('caps'); }
function audioStep(){ const m=hs().mix, ch=m.studio?'sv':(m.clean?'clean':'raw');
  let o='<div class="sec aust"><h4>'+t('auStepT')+'</h4><p class="hint" style="margin-top:0">'+t('auStepSub')+'</p><div class="auopts">'
   +[['raw','auRaw','auRawS'],['clean','auClean','auCleanS'],['sv','auSv','auSvS']].map(([k,a,b])=>'<button class="auopt'+(ch===k?' on':'')+'" data-aupick="'+k+'"><b>'+t(a)+'</b><small>'+t(b)+'</small></button>').join('')+'</div>';
  if(m.studio&&SVS.busy) o+='<p class="hint svst">'+t('svBusy')+'</p>';
  o+='<p class="hint">'+t('auPlayHint')+'</p><div class="tkgo"><button class="pri" data-audone="1">'+t(hs().stepAudio?'auAgain':'auDone')+'</button><button class="sm" data-aumore="1">'+t('auMore')+'</button></div></div>';
  return o; }
async function auStepClick(el){ const b=el.closest('[data-aupick],[data-audone],[data-aumore]'); if(!b) return false; const d=b.dataset;
  if(d.aupick){ const m=hs().mix; snap(); m.clean=d.aupick==='clean'; const sv=d.aupick==='sv', was=!!m.studio; m.studio=sv?(m.studio||true):false; SVS.ab='sv'; dirty(); renderLeft(); if(sv!==was) await svApply(); else auSwap(); renderLeft(); toast(t('auNow')); return true; }
  if(d.audone){ await guideAudioDone(); return true; }
  if(d.aumore){ RTAB='audio'; markTabs(); renderRight(); return true; }
  return false; }
function sideFlash(sel){ const el=$(sel); if(!el) return; el.classList.remove('flash'); void el.offsetWidth; el.classList.add('flash'); setTimeout(()=>el.classList.remove('flash'),900); }
/* 4.47: «البناء»: Claude يبني المقطع من الخطة (صور بحركتها وموشن مع الكلام)، وأنت تشوف الطبقات تدخل التايم لاين */
async function buildRun(){ const pl=(STEPS||[]).find(s=>s.k==='plan'); if(pl&&pl.state!=='done'){ toast(t('buildNeedPlan')); stepGo('plan'); return; }
  if(PULSE&&PULSE.agent&&PULSE.agent.running){ toast(t('buildBusy')); return; }
  if(!INFO.claude){ await save(); const r=await api('/hs/plan_build',{}); if(r&&r.ok){ await load(true); toast(t('planBuiltT').replace('{0}',r.n)); } else toast((r&&srvEn(r.msg))||t('failed')); return; }
  if(!(await tokenGo('build','big'))) return; await save(); const r=await api('/hs/claude_fix',{what:'build'}); if(r&&r.ok){ toast(t('buildStarted')); BUILDAG=true; } else toast((r&&srvEn(r.msg))||t('failed')); }
let BUILDAG=false;
/* 4.56: المفاتيح (Keyframes) بزر ◆ جنب «ربط النصوص» و«ربط الصوت بالصورة»: على الطبقات، كاميرا اللقطة، مستوى صوتك، والموسيقى */
function gkAt(K,x,d){ const P=(K||[]).slice().sort((a,b)=>a.t-b.t); if(!P.length) return d; if(x<=P[0].t) return +P[0].g; const L_=P[P.length-1]; if(x>=L_.t) return +L_.g; let i=0; while(i<P.length-2&&x>=P[i+1].t) i++; const a=P[i], b=P[i+1]; return +a.g+(+b.g-+a.g)*(x-a.t)/Math.max(1e-6,b.t-a.t); }
function gkKey(){ return SEL&&SEL.kind==='music'?'mkf':'vkf'; }
function gkList(k){ return (hs().mix[k]||[]).slice().sort((a,b)=>a.t-b.t); }
function gkHere(k){ return gkList(k).findIndex(p=>Math.abs(p.t-T)<0.04); }
function gkSec(k){ const K=gkList(k), i=gkHere(k), g=i>=0?K[i].g:gkAt(K,T,1);
  return '<div class="sec gksec"><h4>'+t(k==='mkf'?'gkMusT':'gkVoiceT')+(K.length?'<span class="st">'+t('kfCount',K.length)+'</span>':'')+'</h4>'
    +'<div class="row"><button class="sm'+(i>=0?' on':'')+'" data-gka="add">'+t(i>=0?'kfOnKey':'kfAdd')+'</button>'+(K.length?'<button class="sm ghost" data-gka="prev">'+t('kfPrev')+'</button><button class="sm ghost" data-gka="next">'+t('kfNext')+'</button>':'')+'</div>'
    +(i>=0?'<div class="row"><label>'+t('gkLevel')+'</label><input type="range" min="0" max="200" value="'+Math.round(g*100)+'" data-gk="'+k+'"><span class="val" id="gkv">'+Math.round(g*100)+'%</span></div>':'')
    +'<p class="hint">'+t('gkHint')+'</p>'+(K.length?'<div class="row">'+(i>=0?'<button class="sm ghost" data-gka="del">'+t('kfDel')+'</button>':'')+'<button class="sm ghost" data-gka="clear">'+t('kfClear')+'</button></div>':'')+'</div>'; }
document.addEventListener('input',e=>{ const k=e.target.dataset&&e.target.dataset.gk; if(!k) return; const i=gkHere(k); if(i<0) return; const K=gkList(k); K[i].g=r3(+e.target.value/100); hs().mix[k]=K; const s_=$('#gkv'); if(s_) s_.textContent=e.target.value+'%'; if(k==='vkf'&&!playing) AU.volume=clamp(hs().mix.voice*K[i].g,0,1); dirty(); });
document.addEventListener('pointerdown',e=>{ if(e.target.closest&&e.target.closest('input[data-gk]')) snap(); },true);
document.addEventListener('click',e=>{ const b=e.target.closest('[data-gka]'); if(!b) return; const k=gkKey(), K=gkList(k), a=b.dataset.gka;
  if(a==='prev'||a==='next'){ const p=a==='prev'?K.filter(x=>x.t<T-0.04).pop():K.find(x=>x.t>T+0.04); if(!p){ toast(t('kfNone')); return; } seek(p.t); renderRight(); return; }
  snap(); if(a==='add'){ if(gkHere(k)<0){ K.push({t:r3(T),g:r3(gkAt(K,T,1))}); hs().mix[k]=K.sort((x,y)=>x.t-y.t); toast(t('kfAdded',fmt(T))); } }
  else if(a==='del'){ const i=gkHere(k); if(i>=0){ K.splice(i,1); hs().mix[k]=K; } } else if(a==='clear'){ delete hs().mix[k]; toast(t('kfCleared')); }
  dirty(); vrDraw(); renderRight(); });
function camKfList(c){ return Array.isArray(c&&c.kf)?c.kf.slice().sort((a,b)=>a.t-b.t):[]; }
function camVal(c){ if(!c) return {z:1,x:0,y:0}; const K=camKfList(c); if(!K.length) return {z:c.z||1,x:c.x||0,y:c.y||0}; const w=F&&F.contentWindow; const u=T-c.s, v=k=>({z:k.z==null?(c.z||1):+k.z,x:k.x==null?(c.x||0):+k.x,y:k.y==null?(c.y||0):+k.y});
  if(u<=K[0].t) return v(K[0]); if(u>=K[K.length-1].t) return v(K[K.length-1]); let i=0; while(i<K.length-2&&u>=K[i+1].t) i++; const a=v(K[i]), b=v(K[i+1]), r=clamp((u-K[i].t)/Math.max(1e-6,K[i+1].t-K[i].t),0,1), q=r<0.5?4*r*r*r:1-Math.pow(-2*r+2,3)/2; return {z:a.z+(b.z-a.z)*q,x:a.x+(b.x-a.x)*q,y:a.y+(b.y-a.y)*q}; }
function camKfHere(c){ const u=T-c.s; return camKfList(c).findIndex(k=>Math.abs(k.t-u)<0.04); }
function kfTool(){ if(!ST) return; if(!SEL){ toast(t('kfPick')); return; }
  if(SEL.kind==='layer'){ const L=selLayer(); if(!kfOk(L)){ toast(t('kfNoType')); return; } if(T<L.s||T>L.e){ toast(t('kfOut')); return; } if(kfHere(L)<0){ snap(); kfSet(L,{}); toast(t('kfAdded',fmt(T))); } RTAB='sel'; markTabs(); live(); buildTL(); renderRight(); return; }
  if(SEL.kind==='video'){ snap(); const h=hs(), L=(h.cams||[]).slice(); let c=L.find(x=>Math.abs(x.s-SEL.s)<0.03&&Math.abs(x.e-SEL.e)<0.03); if(!c){ c={s:r3(SEL.s),e:r3(SEL.e),z:1,x:0,y:0}; L.push(c); } if(T<c.s||T>c.e){ toast(t('kfOut')); return; }
    if(camKfHere(c)<0){ const v=camVal(c), K=camKfList(c); K.push({t:r3(T-c.s),z:r3(v.z),x:r3(v.x),y:r3(v.y)}); c.kf=K.sort((a,b)=>a.t-b.t); toast(t('kfAdded',fmt(T))); } h.cams=L.sort((a,b)=>a.s-b.s); RTAB='sel'; markTabs(); live(); buildTL(); renderRight(); return; }
  if(SEL.kind==='audio'||SEL.kind==='voice'||SEL.kind==='music'||SEL.kind==='vr'){ const k=SEL.kind==='music'?'mkf':'vkf', K=gkList(k); if(gkHere(k)<0){ snap(); K.push({t:r3(T),g:r3(gkAt(K,T,1))}); hs().mix[k]=K.sort((x,y)=>x.t-y.t); toast(t('kfAdded',fmt(T))); dirty(); } RTAB='sel'; markTabs(); vrDraw(); renderRight(); return; }
  toast(t('kfNoType')); }
document.addEventListener('click',e=>{ if(e.target.closest('#bKf')) kfTool(); });
/* 4.55: كاميرا كل لقطة: تقرّب وتحرك داخل اللقطة بس، فوري بالمعاينة والتصدير (hs.cams) */
function camGet(s,e){ return (hs().cams||[]).find(c=>Math.abs(c.s-s)<0.03&&Math.abs(c.e-e)<0.03)||null; }
function camSec(s,e){ const c0=camGet(s,e), c=c0?{...c0,...camVal(c0)}:{z:1,x:0,y:0}, z=c.z||1, K=camKfList(c0), ki=c0?camKfHere(c0):-1;
  return '<div class="sec camsec"><h4>'+t('camT')+'</h4><div class="chips">'+[['wide',1],['mid',1.35],['close',1.75]].map(([k,v])=>'<button data-campre="'+v+'" class="'+(Math.abs(z-v)<0.03?'on':'')+'">'+t('cam_'+k)+'</button>').join('')+'</div>'
    +'<label class="cmr"><span>'+t('camZ')+'</span><input type="range" min="100" max="300" step="1" value="'+Math.round(z*100)+'" data-cam="z"><b id="camZv">'+Math.round(z*100)+'%</b></label>'
    +'<label class="cmr"><span>'+t('camX')+'</span><input type="range" min="-100" max="100" value="'+Math.round((c.x||0)*100)+'" data-cam="x"'+(z>1.001?'':' disabled')+'><b></b></label>'
    +'<label class="cmr"><span>'+t('camY')+'</span><input type="range" min="-100" max="100" value="'+Math.round((c.y||0)*100)+'" data-cam="y"'+(z>1.001?'':' disabled')+'><b></b></label>'
    +'<div class="row" style="gap:6px;margin-top:8px"><button class="sm" data-camall="1">'+t('camAll')+'</button><button class="sm ghost" data-camreset="1">'+t('camReset')+'</button></div>'
    +'<div class="row" style="gap:6px;margin-top:8px;align-items:center"><button class="sm'+(ki>=0?' on':'')+'" id="bKf2">◆ '+t(ki>=0?'kfOnKey':'kfAdd')+'</button>'+(K.length?'<span class="st">'+t('kfCount',K.length)+'</span><button class="sm ghost" data-camkf="del">'+t('kfDel')+'</button><button class="sm ghost" data-camkf="clear">'+t('kfClear')+'</button>':'')+'</div>'
    +'<p class="hint">'+t(K.length?'camKfHint2':'camHint')+'</p></div>'; }
document.addEventListener('click',e=>{ if(e.target.closest('#bKf2')){ kfTool(); return; } const b=e.target.closest('[data-camkf]'); if(!b||!SEL||SEL.kind!=='video') return; const c=camGet(SEL.s,SEL.e); if(!c) return; snap();
  if(b.dataset.camkf==='del'){ const i=camKfHere(c); if(i>=0){ const K=camKfList(c); K.splice(i,1); c.kf=K; if(!K.length) delete c.kf; } } else { delete c.kf; toast(t('kfCleared')); }
  hs().cams=(hs().cams||[]).filter(x=>x.z>1.001||camKfList(x).length); live(); buildTL(); renderRight(); });
function camSet(s,e,p){ const h=hs(), L=(h.cams||[]).slice(); let c=L.find(x=>Math.abs(x.s-s)<0.03&&Math.abs(x.e-e)<0.03); if(!c){ c={s:r3(s),e:r3(e),z:1,x:0,y:0}; L.push(c); }
  if(camKfList(c).length&&T>=c.s&&T<=c.e){ const K=camKfList(c); let i=camKfHere(c); if(i<0){ const v=camVal(c); K.push({t:r3(T-c.s),z:r3(v.z),x:r3(v.x),y:r3(v.y)}); K.sort((a,b)=>a.t-b.t); i=K.findIndex(k=>Math.abs(k.t-(T-c.s))<0.04); } Object.assign(K[i],p); K[i].z=Math.max(1,Math.min(3,+K[i].z||1)); c.kf=K; }   // 4.56: فيها مفاتيح: تعدّل مفتاح المؤشر
  else { Object.assign(c,p); c.z=Math.max(1,Math.min(3,+c.z||1)); if(c.z<=1.001){ c.x=0; c.y=0; } }
  h.cams=L.filter(x=>x.z>1.001||camKfList(x).length).sort((a,b)=>a.s-b.s); live(); }
document.addEventListener('pointerdown',e=>{ if(e.target.closest&&e.target.closest('.camsec input[data-cam]')) snap(); },true);
document.addEventListener('input',e=>{ const k=e.target.dataset&&e.target.dataset.cam; if(!k||!SEL||SEL.kind!=='video') return; const v=+e.target.value/100; camSet(SEL.s,SEL.e,{[k]:v});
  if(k==='z'){ const b=$('#camZv'); if(b) b.textContent=Math.round(v*100)+'%'; $$('.camsec input[data-cam="x"],.camsec input[data-cam="y"]').forEach(x=>x.disabled=v<=1.001); } });
document.addEventListener('change',e=>{ if(e.target.dataset&&e.target.dataset.cam) buildTL(); });
document.addEventListener('click',e=>{ const b=e.target.closest('[data-campre],[data-camall],[data-camreset]'); if(!b||!SEL||SEL.kind!=='video') return; snap(); const d=b.dataset;
  if(d.campre){ const z=+d.campre, c=camGet(SEL.s,SEL.e)||{}; camSet(SEL.s,SEL.e,{z,x:z>1?(c.x||0):0,y:z>1?(c.y==null?-0.25:c.y):0}); }
  else if(d.camreset){ hs().cams=(hs().cams||[]).filter(x=>!(Math.abs(x.s-SEL.s)<0.03&&Math.abs(x.e-SEL.e)<0.03)); live(); }
  else if(d.camall){ const c=camGet(SEL.s,SEL.e)||{z:1,x:0,y:0}, b_=shotBounds(); const L=[]; for(let i=0;i<b_.length-1;i++){ if(c.z>1.001) L.push({s:r3(b_[i]),e:r3(b_[i+1]),z:c.z,x:c.x||0,y:c.y||0}); } hs().cams=L; live(); toast(t('camAllDone',b_.length-1)); }
  buildTL(); renderRight(); });
/* 4.54: زر + بآخر سطر الفيديو (مثل كب كت): ثابت ما يتحرك مع التايم لاين. صورة أو مقطع يندرج عند المؤشر ويدف اللي بعده، والمقطع يطول */
function insBtn(){ const tl=$('#tl'), sc=$('#scroller'), fm=$('#tFilm'); if(!tl||!sc||!fm||MOBILE) return; let b=$('#insAdd');
  if(!b){ b=document.createElement('label'); b.id='insAdd'; b.title=t('insT'); b.innerHTML='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg><input type="file" accept="image/*,video/*" hidden id="insFile">'; tl.appendChild(b); sc.addEventListener('scroll',insPos,{passive:true}); window.addEventListener('resize',insPos); }
  insPos(); }
function insPos(){ const b=$('#insAdd'), tl=$('#tl'), sc=$('#scroller'), fm=$('#tFilm'); if(!b||!tl||!sc||!fm) return; const T_=tl.getBoundingClientRect(), S_=sc.getBoundingClientRect(), F_=fm.getBoundingClientRect();
  const sbw=sc.offsetWidth-sc.clientWidth; b.style.top=Math.round(F_.top-T_.top+(F_.height-34)/2)+'px'; b.style.left=Math.round(S_.right-T_.left-sbw-46)+'px'; b.style.display=(F_.bottom<S_.top||F_.top>S_.bottom)?'none':''; }
document.addEventListener('change',async e=>{ if(e.target.id!=='insFile') return; const f=e.target.files[0]; e.target.value=''; if(!f) return;
  const img=/^image\//.test(f.type), at=T; if(playing) stop();
  let dur=3, mute=false;
  const ok=true; if(false) await new Promise(res=>{ modal('<h3>'+t('insQ',fmt(at))+'</h3><p class="hint" dir="auto" style="margin:0 0 10px">'+esc(f.name)+'</p><p class="hint" style="margin:0 0 12px;line-height:1.8">'+t('insSub')+'</p>'
    +(img?'<label class="hint" style="display:block;margin-bottom:6px">'+t('insDur')+'</label><div class="chips" id="insDur">'+[2,3,5,8].map(s=>'<button class="'+(s===3?'on':'')+'" data-d="'+s+'">'+s+' '+t('secShort')+'</button>').join('')+'</div>':'<label class="item"><input type="checkbox" id="insMute"> <span>'+t('insMute')+'</span></label>')
    +'<div class="row" style="margin-top:14px"><button class="pri" id="insGo">'+t('insGo')+'</button><button id="insNo">'+t('cancel')+'</button></div>');
    $$('#insDur [data-d]').forEach(x=>x.onclick=()=>{ $$('#insDur [data-d]').forEach(y=>y.classList.remove('on')); x.classList.add('on'); dur=+x.dataset.d; });
    $('#insGo').onclick=()=>{ mute=!!($('#insMute')&&$('#insMute').checked); closeModal(); res(true); }; $('#insNo').onclick=()=>{ closeModal(); res(false); }; });
  if(!ok) return; await save();   // 4.56: يندرج على طول (بدون نافذة)، بصوته، عند المؤشر
  const up=await api('/hs/asset',f,{'X-Name':encodeURIComponent('ins-'+Date.now()+'-'+f.name)}); if(!up||!up.ok){ toast((up&&srvEn(up.msg))||t('failed')); return; }
  const r=await api('/hs/insert',{src:up.src,at,dur,mute}); if(!r||!r.ok){ toast((r&&srvEn(r.msg))||t('busyJob')); return; }
  pollJob(async(p)=>{ try{ await load(true); await loadSteps(); cutUndoMark(p); const J_=(p&&p.ins)||null; if(J_){ seek(J_.at+0.02); toast(t('insDone',fmt(J_.at),fmtm(J_.total))); pendSync(); setTimeout(()=>{ const c=document.querySelector('#tFilm'); if(c) sideFlash('#tFilm'); },60); } else if(p&&p.err) toast(srvEn(p.err)); } finally{ insPos(); } }); });
/* 4.56: المضاف يتعرض من ملفه نفسه لين تجهز فريماته بالخلفية: فوري مثل كب كت */
let PEND=null;
function pendSync(){ const P=INFO&&INFO.pend, w=F&&F.contentWindow;
  if(!P){ if(PEND){ try{ PEND.el.pause(); PEND.el.remove(); }catch(e){} PEND=null; } if(w) w.__hsPend=null; return; }
  if(PEND&&PEND.src===P.src&&Math.abs(PEND.at-P.at)<0.001){ if(w) w.__hsPend=PEND.box; return; }
  if(PEND){ try{ PEND.el.remove(); }catch(e){} }
  const el=document.createElement(P.img?'img':'video'); if(!P.img){ el.muted=true; el.preload='auto'; el.playsInline=true; } el.src='/'+String(P.src).replace(/^\/+/,''); el.style.cssText='position:fixed;width:2px;height:2px;opacity:0;pointer-events:none;left:-9px;top:-9px'; document.body.appendChild(el);
  PEND={src:P.src,at:+P.at,dur:+P.dur,img:!!P.img,el,box:{el,at:+P.at,dur:+P.dur}}; if(w) w.__hsPend=PEND.box; if(P.img) el.onload=()=>{ lastFrame=-1; drawT(T); }; else el.onloadeddata=()=>{ lastFrame=-1; drawT(T); }; }
async function pendPrep(x){ if(!PEND||PEND.img) return; const el=PEND.el, inR=x>=PEND.at&&x<PEND.at+PEND.dur;
  if(!inR){ if(!el.paused) el.pause(); return; } const u=x-PEND.at;
  if(playing){ if(el.paused){ try{ el.currentTime=u; el.play().catch(()=>{}); }catch(e){} } else if(Math.abs(el.currentTime-u)>0.3) el.currentTime=u; return; }
  if(!el.paused) el.pause(); if(Math.abs(el.currentTime-u)>0.02){ el.currentTime=u; await new Promise(r=>{ const f=()=>{ el.removeEventListener('seeked',f); r(); }; el.addEventListener('seeked',f); setTimeout(r,500); }); } }
/* 4.52: «البناء» نافذة كبيرة بالنص: وش بالخطة، وتبني مع Claude أو الصور بس، وتشوف Claude وهو يبني، وبالأخير كم طبقة انضافت */
let BV=null, BV0=0, BVT0=0, BVDONE=null;
async function buildOpen(){ BV={}; BVDONE=null; let w=$('#buildv'); if(!w){ w=document.createElement('div'); w.id='buildv'; document.body.appendChild(w); w.addEventListener('mousedown',e=>{ if(e.target===w) buildClose(); }); }
  if(BUILDAG&&!BVT0) BVT0=Date.now(); w.innerHTML='<div class="bvin"><p class="hint" style="text-align:center">…</p></div>'; requestAnimationFrame(()=>w.classList.add('on')); try{ PLAN=await api('/hs/plan'); }catch(e){} bvDraw(); }
function buildClose(){ const w=$('#buildv'); if(w){ w.classList.remove('on'); setTimeout(()=>{ if(!BV) w.remove(); },220); } BV=null; }
function bvRunning(){ return !!(BUILDAG&&PULSE&&PULSE.agent&&PULSE.agent.running); }
function bvDraw(){ const w=$('#buildv'); if(!w||!BV) return; const added=()=>Math.max(0,(hs().layers||[]).length-BV0);
  if(bvRunning()){ const el=Math.round((Date.now()-BVT0)/1000);
    if(w.querySelector('#bvLoad')){ clLoaderTick(w,el); const a=w.querySelector('#bvAdd'); if(a) a.textContent=t('bvAdded',added()); return; }
    w.innerHTML='<div class="bvin">'+clLoader('bvLoad',t('bvRunning'),t('bvRunningS'))+'<p class="bvadd" id="bvAdd">'+t('bvAdded',added())+'</p><div class="bvacts c"><button class="sm" data-bvx="1">'+t('bvBg')+'</button><button class="sm ghost" data-bvstop="1">'+t('tkStop')+'</button></div></div>'; clLoaderTick(w,el); return; }
  let o='<div class="bvin"><button class="bvclose" data-bvx="1" aria-label="'+esc(t('close'))+'">×</button><div class="bvh">'+clLogo(28)+'<div><h3>'+t('bvT')+'</h3><p>'+t('bvSub')+'</p></div></div>';
  if(BVDONE!=null){ w.innerHTML=o+'<div class="bvempty"><b>'+t('bvDone')+'</b><p>'+t('bvDoneS',BVDONE)+'</p><button class="pri" data-bvx="1">'+t('bvSee')+'</button></div></div>'; return; }
  const P_=PLAN&&PLAN.ok?PLAN:null, items=(P_&&P_.items)||[];
  if(!items.length){ w.innerHTML=o+'<div class="bvempty"><b>'+t('bvNoPlan')+'</b><p>'+t('bvNoPlanS')+'</p><button class="pri" data-bvplan="1">'+t('bvOpenPlan')+'</button></div></div>'; return; }
  const nimg=items.filter(x=>x.src||x.mg||x.logo).length;
  o+=scriptNote(P_)+'<p class="bvsum">'+t('bvItems',items.length,nimg)+(P_.approved?'':' · <span class="st">'+t('planWaiting')+'</span>')+'</p><div class="bvlist">'
    +items.map((it,i)=>'<div class="bvr'+(it.built?' built':'')+'">'+(it.src?'<img alt="" src="'+esc(it.src)+'">':'<span class="bvph">'+(i+1)+'</span>')+'<div><b dir="auto">'+esc(it.title||'')+'</b><small dir="auto">'+esc(it.kindAr||'')+(it.built?' · '+t('planBuilt'):'')+'</small></div><span class="t" data-bvseek="'+(+it.s||0)+'">'+fmt(+it.s||0)+'</span></div>').join('')+'</div>';
  o+='<div class="bvacts">'+(INFO.claude?'<button class="pri" data-bvgo="claude">'+clLogo(16,'#fff')+t('bvClaude')+'<span class="tkb">'+t('tokBadge')+'</span></button>':'')+'<button data-bvgo="local">'+t('bvLocal')+'</button><button class="sm ghost" data-bvplan="1">'+t('bvEditPlan')+'</button></div><p class="hint bvhint">'+t(P_.approved?'bvLocalS':'bvApproveS')+'</p></div>';
  w.innerHTML=o; }
document.addEventListener('keydown',e=>{ if(e.key==='Escape'&&BV&&!$('#modal.on')) buildClose(); });
document.addEventListener('click',async e=>{ const b=e.target.closest('#buildv [data-bvx],#buildv [data-bvplan],#buildv [data-bvgo],#buildv [data-bvstop],#buildv [data-bvseek]'); if(!b) return; const d=b.dataset;
  if(d.bvx){ buildClose(); BVDONE=null; return; }
  if(d.bvplan){ buildClose(); planBoard(); return; }
  if(d.bvseek!==undefined){ buildClose(); seek(+d.bvseek); return; }
  if(d.bvstop){ await api('/hs/agent_stop',{}); return; }
  if(d.bvgo==='local'){ await save(); if(!PLAN.approved) PLAN=await api('/hs/plan_set',{approve:true}); const n0=(hs().layers||[]).length; const r=await api('/hs/plan_build',{}); if(r&&r.ok){ await load(true); await loadSteps(); BVDONE=r.n; PLAN=r.plan||PLAN; if(!BV) BV={}; bvDraw(); } else toast((r&&srvEn(r.msg))||t('failed')); return; }
  if(d.bvgo==='claude'){ if(PULSE&&PULSE.agent&&PULSE.agent.running){ toast(t('buildBusy')); return; } if(!(await tokenGo('build','big'))) return; await save();
    if(!PLAN.approved){ PLAN=await api('/hs/plan_set',{approve:true}); loadSteps(); }
    const r=await api('/hs/claude_fix',{what:'build'}); if(r&&r.ok){ BUILDAG=true; BV0=(hs().layers||[]).length; BVT0=Date.now(); if(PULSE) PULSE.agent={running:true,elapsed:0}; bvDraw(); } else toast((r&&srvEn(r.msg))||t('failed')); } });
function stepGo(k){ setTimeout(()=>{ stepsLive(); sideFlash(k==='notes'?'#panel':'#bin'); },0); if(k==='plan'){ planBoard(); return; } if(k==='audio'){ LTAB='audio'; markTabs(); renderLeft(); return; } if(k==='notes'){ RTAB='claude'; markTabs(); renderRight(); setTimeout(()=>{ const x=$('#agTx'); if(x) x.focus(); },0); return; }
  if(k==='takes'||k==='caps'){ LTAB=k==='takes'?'takes':'text'; markTabs(); renderLeft(); if(LTAB==='takes') loadTakes(); return; } if(k==='build'){ buildOpen(); return; } RTAB=k==='plan'?'plan':'proj'; markTabs(); renderRight(); if(RTAB==='plan') loadPlan(); }
function check410(c){ let o='';
  if(c.unsure) o+='<div class="sec"><h4>'+t('chkUnsure')+'</h4><div class="item" data-step="caps"><span>'+t('loCount',c.unsure)+'</span></div><p class="hint">'+t('chkUnsureHint')+'</p></div>';
  if((c.speechGaps||[]).length) o+='<div class="sec"><h4>'+t('chkSpeechGap')+'</h4>'+c.speechGaps.map(g=>'<div class="item" data-seek="'+g.s+'"><span>'+t('chkSpeechGapItem',(g.e-g.s).toFixed(1))+'</span><span class="st" style="flex:none;direction:ltr">'+fmt(g.s)+'</span></div>').join('')+'<p class="hint">'+t('chkSpeechGapHint')+'</p></div>';
  if(c.cutSound) o+='<div class="sec"><h4>'+t('chkCutSound')+'</h4><p class="hint">'+t('chkCutSoundHint',c.cutSound)+'</p><button class="sm" data-cutsfix="1">'+t('chkCutSoundFix')+'</button></div>';
  if((c.facts||[]).length) o+='<div class="sec"><h4>'+t('chkFacts')+'</h4>'+c.facts.map(f=>'<div class="item" data-seek="'+f.s+'"><span dir="rtl">'+esc(f.text.slice(0,90))+'<small style="display:block;color:var(--mut)">'+esc(f.why.map(srvEn).join(LANG==='en'?', ':'، '))+'</small></span><span class="st" style="flex:none;direction:ltr">'+fmt(f.s)+'</span></div>').join('')+'<p class="hint">'+t('chkFactsHint')+'</p></div>';
  return o; }
async function loadPlan(){ PLAN=await api('/hs/plan'); if(RTAB==='plan') renderRight(); }
function planPanel(){ if(!PLAN){ loadPlan(); return '<p class="hint">…</p>'; }
  let o='<div class="sec"><h4>'+t('planTitle')+(PLAN.ok?'<span class="st '+(PLAN.approved?'ok':'')+'" style="font-size:12px">'+t(PLAN.approved?'planApproved':'planWaiting')+'</span>':'')+'</h4>';
  if(!PLAN.ok) return o+'<p class="hint">'+t('planNone')+'</p><button class="pri" data-planopen="1" style="width:100%">'+t('planOpen')+'</button></div>';
  const items=PLAN.items||[], ngen=items.filter(x=>x.kind==='gen'&&!x.src).length;
  if(PLAN.motif) o+='<p class="hint" style="margin:0 0 8px"><b>'+t('planMotif')+':</b> '+esc(PLAN.motif)+'</p>';
  o+='<div style="display:flex;flex-direction:column;gap:6px"><button class="'+(PLAN.approved?'sm ghost':'pri')+'" data-planok="'+(PLAN.approved?0:1)+'">'+t(PLAN.approved?'planUnapprove':'planApprove')+'</button>'+(ngen?'<button class="sm" data-plan2="1">'+t('planTwo')+'</button>':'')+(PLAN.approved&&items.some(x=>x.src||x.mg||x.logo||x.glow||(x.anno||[]).length)?'<button class="sm" data-planbuild="1">'+t('planBuild')+'</button>':'')+'</div>';
  o+='<textarea id="planAsk" rows="3" dir="auto" placeholder="'+t('planAskPh')+'" style="margin-top:8px">'+esc(PLAN.feedback||'')+'</textarea><button class="sm" data-planre="1" style="margin-top:6px">'+t('planRewrite')+'</button></div>';
  items.forEach((it,i)=>{ o+='<div class="sec plc'+(it.built?' built':'')+'"><div class="plh"><b>'+(i+1)+'</b><span>'+esc(it.title||'')+'</span><span class="st" data-seek="'+(+it.s||0)+'" style="direction:ltr;cursor:pointer">'+fmt(+it.s||0)+'</span></div>'
    +'<div class="plb">'+(it.src?'<div class="plimg" style="background-image:url('+esc(it.src)+')"></div>':'<div class="plimg e"><span>'+esc(it.kindAr||'')+'</span></div>')+'<div class="plt">'
    +(it.speech?'<label>'+t('planSpeech')+'</label><p>'+esc(it.speech)+'</p>':'')+(it.idea?'<label>'+t('planIdea')+'</label><p>'+esc(it.idea)+'</p>':'')+(it.example?'<label>'+t('planExample')+'</label><p>'+esc(it.example)+'</p>':'')+(it.show?'<label>'+t('planShow')+'</label><p>'+esc(it.show)+'</p>':'')+(it.motion?'<label>'+t('planMotion')+'</label><p>'+esc(it.motion)+'</p>':'')+(it.source||it.query?'<label>'+t('planSource')+'</label><p dir="auto">'+esc(it.source||it.query)+'</p>':'')+'</div></div>'
    +'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:6px"><span class="hint" style="margin:0">'+esc(it.kindAr||'')+(it.built?' · '+t('planBuilt'):'')+'</span><button class="sm ghost" data-planrm="'+esc(it.id)+'">'+t('planRm')+'</button></div></div>'; });
  return o; }
async function planClick(el){ const b=el.closest('[data-planopen],[data-planok],[data-planrm],[data-planre],[data-plan2],[data-planbuild],[data-cutsfix],[data-step]'); if(!b) return false; const d=b.dataset;
  if(d.planbuild){ await save(); const r=await api('/hs/plan_build',{}); if(!r||!r.ok){ toast((r&&srvEn(r.msg))||t('failed')); return true; } PLAN=r.plan; await load(true); renderRight(); toast(t(r.miss&&r.miss.length?'planBuiltMiss':'planBuiltT').replace('{0}',r.n).replace('{1}',(r.miss||[]).join('، '))); return true; }
  if(d.step){ stepGo(d.step); return true; }
  if(d.planopen){ planBoard(1); return true; }
  if(d.cutsfix){ await save(); const r=await api('/hs/cuts_fix',{}); if(!r.ok){ toast(srvEn(r.msg)||t('busyJob')); return true; } stLoader('rebuild',t('rebuildSub')); pollJob(async(p)=>{ try{ await load(true); cutUndoMark(p); } finally{ stLoaderHide(); } }); return true; }
  if(d.planok!==undefined){ PLAN=await api('/hs/plan_set',{approve:d.planok==='1'}); renderRight(); loadSteps(); toast(t(d.planok==='1'?'planApprovedT':'planUnapprovedT')); return true; }
  if(d.planrm){ PLAN=await api('/hs/plan_set',{rm:d.planrm}); renderRight(); return true; }
  if(d.planre){ const tx=($('#planAsk')||{}).value||''; PLAN=await api('/hs/plan_set',{feedback:tx}); renderRight(); const r=await api('/hs/claude_fix',{what:'plan',text:tx}); toast((r&&srvEn(r.msg))||t(r&&r.ok?'planSent':'failed')); return true; }
  if(d.plan2){ const r=await api('/hs/claude_fix',{what:'plan2',text:($('#planAsk')||{}).value||''}); toast((r&&srvEn(r.msg))||t(r&&r.ok?'planTwoSent':'failed')); return true; }
  return false; }
/* ═══ 4.10: اختيار الجمل — الإعادات والتلعثم من التسجيل الخام، و Claude يختار الأفضل ═══ */
let TK=null, TKALL=false, TKAU=null;
async function loadTakes(){ TK=await api('/hs/takes'); if(LTAB==='takes') renderLeft(); }
const fmtm=x=>{ x=Math.max(0,x||0); const m=Math.floor(x/60), s=Math.floor(x%60); return m+':'+String(s).padStart(2,'0'); };
const TKPLAY='<svg width="11" height="11" viewBox="0 0 24 24"><path d="M7 4l13 8-13 8z" fill="currentColor"/></svg>';
function takesRow(it,cls){ const lab=TK.labels||{}, tags=(it.tags||[]).map(g=>'<i class="tkt'+(it.drop?'':' k')+'">'+esc(lab[g]||g)+'</i>').join('');
  let act=''; if(it.group) act=it.chosen?'<span class="tkc">'+t('tkChosen')+'</span>':'<button class="sm" data-tkact="use" data-tkid="'+it.id+'">'+t('tkUse')+'</button>';
  else act='<button class="sm ghost" data-tkact="'+(it.drop?'keep':'drop')+'" data-tkid="'+it.id+'">'+t(it.drop?'tkKeep':'tkDrop')+'</button>';
  let o='<div class="tkr'+(it.drop?' off':'')+(cls||'')+'"><button class="sm ghost tkpl" data-tkplay="'+it.s+','+it.e+'" title="'+t('tkListen')+'">'+TKPLAY+'</button><span class="t"'+(it.out!=null?' data-tkseek="'+it.out+'"':'')+'>'+fmtm(it.s)+'</span><div class="tx" dir="rtl"><span>'+esc(it.text)+'</span>'+tags+(it.why&&!it.drop?'<small>'+esc(srvEn(it.why))+'</small>':'')+'</div><div class="acts">'+act+'</div></div>';
  (it.trims||[]).forEach(tr=>{ o+='<div class="tkr tktr'+(tr.drop?' off':'')+'"><button class="sm ghost tkpl" data-tkplay="'+Math.max(0,tr.s-0.6)+','+(tr.e+0.9)+'">'+TKPLAY+'</button><span class="t">'+fmtm(tr.s)+'</span><div class="tx" dir="rtl"><i class="tkt'+(tr.drop?'':' k')+'">'+esc(lab[tr.kind]||tr.kind)+'</i><span>«'+esc(tr.text)+'»</span></div><div class="acts"><button class="sm ghost" data-tkact="'+(tr.drop?'keep':'drop')+'" data-tkid="'+tr.id+'">'+t(tr.drop?'tkKeep':'tkDrop')+'</button></div></div>'; });
  return o; }
/* 4.43: «اختر الجمل» مثل الخطوة الأولى بالمونتاج: الخام وبعد القص، مراجعة المساعد (اختيارية)، ملخص المحذوف، المجموعات، و«اقطع المقطع» */
let TKAG=false;
function tkCounts(){ const c={}; (TK.items||[]).forEach(it=>{ if(!it.drop) return; const g=(it.tags||[])[0]||(it.group?'retake':'other'); c[g]=(c[g]||0)+1; }); return c; }
function takesPanel(){
  if(!TK) return '<div class="sec"><p class="hint">'+t('tkLoading')+'</p></div>';
  if(TK.locked) return '<div class="sec"><h4>'+t('tkTitle')+'</h4><p class="hint">'+t('tkLocked')+'</p></div>';   // 4.54
  if(!TK.ok) return '<div class="sec"><h4>'+t('tkTitle')+'</h4><p class="hint">'+t(TK.has?'tkNone':'tkNoStt')+'</p>'+(TK.has?'<button class="pri" data-tkscan="1" style="width:100%">'+t('tkScan')+'</button>':'')+'</div>';
  const raw=TK.raw||1, items=TK.items||[], lab=TK.labels||{}, pre=guidePre(), ag=!!(PULSE&&PULSE.agent&&PULSE.agent.running&&TKAG);
  if(!pre&&!TK.pending&&hs().guide&&!TKEDIT) return '<div class="sec tkp"><h4>'+t('tkTitle')+'</h4><p class="tkdone">'+t('tkCutDone',fmtm(raw),fmtm(TK.now||TK.kept))+'</p><button class="sm" data-tkedit="1">'+t('tkEdit')+'</button></div>';
  let o='<div class="sec tkp"><div class="tkhd"><h4>'+t('tkTitle')+'</h4><span>'+t('tkRawCut',fmtm(raw),fmtm(TK.kept))+'</span></div>';
  o+='<div class="tkstrip">'+items.map(it=>'<b class="'+(it.drop?'d':'k')+'" style="right:'+(100*it.s/raw).toFixed(2)+'%;width:'+Math.max(0.25,100*(it.e-it.s)/raw).toFixed(2)+'%"'+(it.out!=null?' data-tkseek="'+it.out+'"':'')+'></b>').join('')+'</div>';
  if(ag) o+='<div class="tkai on"><p>'+t('tkAiBusy')+'</p><button class="sm ghost" data-tkstop="1">'+t('tkStop')+'</button></div>';
  else if(TK.by!=='claude'&&INFO.claude) o+='<div class="tkai"><p>'+t('tkAiAsk')+'</p><button class="sm" data-tkclaude="1">'+t('tkAiGo')+'<span class="tkb">'+t('tokBadge')+'</span></button></div>';
  const n=items.length, dn=items.filter(x=>x.drop).length, c=tkCounts(), parts=Object.keys(c).map(k=>(lab[k]||k)+' '+c[k]).join('، '), groups=(TK.groups||[]).length;
  o+='<div class="tksum"><p>'+(dn?t('tkSumm',dn,n)+(parts?' ('+esc(parts)+')':''):t('tkSumm0',n))+'</p>'+(TK.note?'<p class="hint" dir="auto" style="margin:0 0 6px">'+esc(srvEn(TK.note))+'</p>':'')+(dn?'<span>'+t('tkGone',(TK.gone||0).toFixed(1))+'</span>':'')+(groups?'<span>'+t('tkPickN',groups)+'</span>':'')+'<span>'+t(TK.by==='claude'?'tkByClaude':'tkByAuto')+'</span></div>';
  o+='<div class="seg" style="margin:8px 0"><button class="'+(TKALL?'':'on')+'" data-tkall="0">'+t('tkImportant')+'</button><button class="'+(TKALL?'on':'')+'" data-tkall="1">'+t('tkAll')+'</button></div><div class="tklist">';
  let g=null, k=0;
  items.forEach(it=>{ const show=TKALL||it.drop||(it.tags||[]).length||it.group||(it.trims||[]).length; if(!show) return;
    if(it.group!==g){ if(g) o+='</div>'; g=it.group||null; if(g){ const m=items.filter(x=>x.group===g).length; o+='<div class="tkgrp"><div class="tkgh">'+t('tkGroupN',m)+'</div>'; } }
    o+=takesRow(it); k++; });
  if(g) o+='</div>';
  if(!k) o+='<p class="hint">'+t('tkClean')+'</p>';
  o+='</div>'+(INFO.claude?'<div class="tkask"><textarea id="tkAsk" rows="2" dir="auto" placeholder="'+t('tkAskPh2')+'"></textarea><button class="sm" data-tkclaude="1" title="'+esc(t('tkSend'))+'"'+(ag?' disabled':'')+'>'+t('tkSend')+'</button></div>':'');
  o+='<div class="tkgo"><button class="pri" data-tkapply="1"'+(TK.pending||pre?'':' disabled')+'>'+t(TK.pending?'tkCutGo':(pre?'tkCutOk':'tkApplied'))+'</button><button class="sm" data-tkprev="1">'+t('tkPreview')+'</button></div><p class="hint">'+t('tkApplyHint')+'</p></div>';
  return o; }
/* 4.43: «راجع الكابشن مع المساعد»: يقترح تصحيحات (تختار منها بعلامة) ويسأل عن اللي ما تأكد منه بخيارات جاهزة */
let CAPR=null, CAPRAG=false, CAPRL=0, CAPRI=-1, CAPRDONE=false;
/* 4.50: وقت مراجعة الكابشن تشوف Claude وين وصل: الجملة اللي يراجعها هنا وعلى التايم لاين، لين تطلع النتيجة */
function caprIdx(){ const p=PULSE&&PULSE.prog, n=ST.caps.cards.length; return p&&p.k==='capr'&&n?Math.max(0,Math.min(n-1,(+p.i||1)-1)):-1; }
function caprProg(){ const n=ST.caps.cards.length, i=caprIdx(), c=i>=0?ST.caps.cards[i]:null, pc=i<0?0:Math.round((i+1)/Math.max(1,n)*100);
  return '<div class="tkai on caprp"><div class="cprh"><i class="cprdot"></i><b>'+(i<0?t('caprReading'):t('caprAt',i+1,n))+'</b><span style="flex:1"></span><button class="sm ghost" data-caprstop="1">'+t('tkStop')+'</button></div>'
    +'<div class="cprbar'+(i<0?' ind':'')+'"><i style="width:'+(i<0?35:pc)+'%"></i></div>'+(c?'<p class="cprtx" dir="rtl" data-seek="'+c.s+'">«'+esc(key(c))+'»</p>':'<p class="hint" style="margin:0">'+t('caprBusy')+'</p>')+'</div>'; }
function caprFollow(){ const i=CAPRAG?caprIdx():-1; $$('#lane .clip.cap.scan').forEach(x=>{ if(+x.dataset.id!==i) x.classList.remove('scan'); }); if(i<0||i===CAPRI) return; CAPRI=i;
  const el=document.querySelector('#lane .clip[data-kind="cap"][data-id="'+i+'"]'); if(el){ el.classList.add('scan'); el.scrollIntoView({block:'nearest',inline:'center',behavior:'smooth'}); }
  if(!playing) seek(ST.caps.cards[i].s+0.02); if(LTAB==='text') renderLeft(); }
async function caprLoad(){ try{ const r=await api('/hs/caps_review',{}); CAPR=r&&r.review||null; }catch(e){} CAPRL=Date.now(); if(LTAB==='text') renderLeft();
  if(CAPRDONE){ CAPRDONE=false; if(CAPR) toast(t('caprDoneT',(CAPR.fixes||[]).length,(CAPR.asks||[]).length)); } }
function caprHtml(nlo){ if(!CAPRL) setTimeout(caprLoad,0); const ag=!!(PULSE&&PULSE.agent&&PULSE.agent.running&&CAPRAG);
  let o='<div class="lobar"><span>'+(nlo?t('loCount',nlo):t('loNone'))+'</span>'+(INFO.claude&&!ag?'<button class="sm" data-caprgo="1">'+t('caprGo')+'<span class="tkb">'+t('tokBadge')+'</span></button>':'')+'<button class="sm ghost" data-lorefresh="1">'+t('loRefresh')+'</button></div>';
  if(ag) return o+caprProg();
  const R=CAPR; if(!R) return o+capOkBtn();
  const fx=R.fixes||[], qs=R.asks||[], open=fx.filter(f=>!f.done&&!f.skip);
  o+='<div class="capr"><div class="tksum"><p dir="auto">'+esc(R.summary||t('caprSum',fx.length,qs.length))+'</p></div>';
  if(fx.length){ o+=fx.map(f=>'<label class="cfx'+(f.done||f.skip?' off':'')+'"><input type="checkbox" data-cfx="'+esc(f.id)+'"'+(f.skip?'':' checked')+(f.done||f.skip?' disabled':'')+'><span class="t" data-seek="'+f.t+'">'+fmt(f.t)+'</span><span class="ft" dir="rtl"><s>'+esc(f.from)+'</s> ← <b>'+esc(f.to)+'</b>'+(f.why?'<small>'+esc(f.why)+'</small>':'')+(f.done==='miss'?'<small>'+t('caprMiss')+'</small>':'')+'</span></label>').join('');
    if(open.length) o+='<button class="pri" data-caprapply="1" style="width:100%;margin-top:6px">'+t('caprApply')+'</button>'; }
  if(qs.length){ o+='<h5 class="caprq">'+t('caprQs')+'</h5>'+qs.map(q=>'<div class="cq"><div class="qh"><span class="t" data-seek="'+q.t+'">'+fmt(q.t)+'</span><b dir="auto">'+esc(q.q)+'</b></div>'+(q.note?'<small dir="auto">'+esc(q.note)+'</small>':'')
    +'<div class="chips">'+q.opts.map(x=>'<button class="'+(q.answer===x?'on':'')+'" data-cqid="'+esc(q.id)+'" data-cqopt="'+esc(x)+'"'+(q.answer!=null?' disabled':'')+' dir="auto">'+esc(x)+'</button>').join('')+'</div></div>').join(''); }
  return o+'<button class="sm ghost" data-caprx="1" style="margin-top:8px">'+t('caprClose')+'</button></div>'+capOkBtn(); }
function capOkBtn(){ return hs().guide?'<button class="pri" data-capok="1" style="width:100%;margin:6px 0 10px">'+t(hs().stepCaps?'capOkNext':'capOk')+'</button>':''; }
async function caprClick(el){ const b=el.closest('[data-caprgo],[data-caprstop],[data-caprapply],[data-cqid],[data-caprx],[data-capok]'); if(!b) return false; const d=b.dataset;
  if(d.capok){ hs().stepCaps=1; await save(); await loadSteps(); stepGo('plan'); return true; }
  if(d.caprgo){ if(!(await tokenGo('capr','mid'))) return true; await save(); const r=await api('/hs/claude_fix',{what:'capreview'}); if(r&&r.ok){ CAPRAG=true; CAPRI=-1; if(PULSE) PULSE.prog=null; CAPR=null; renderLeft(); } else toast((r&&srvEn(r.msg))||t('failed')); return true; }
  if(d.caprstop){ await api('/hs/agent_stop',{}); CAPRAG=false; renderLeft(); return true; }
  if(d.caprapply){ const ids=$$('#lbody [data-cfx]').filter(x=>x.checked&&!x.disabled).map(x=>x.dataset.cfx); await save(); const r=await api('/hs/caps_review',{act:'apply',ids}); if(r&&r.ok){ CAPR=r.review; await load(true); toast(t('caprApplied',ids.length)); } else toast(t('failed')); return true; }
  if(d.cqid){ await save(); const r=await api('/hs/caps_review',{act:'answer',id:d.cqid,opt:d.cqopt}); if(r&&r.ok){ CAPR=r.review; await load(true); } else toast(t('failed')); return true; }
  if(d.caprx){ const r=await api('/hs/caps_review',{act:'dismiss'}); CAPR=null; renderLeft(); return true; }
  return false; }
/* 4.43: الخطة كخطوة كاملة (لوحة عرضها كامل): ١ فكرتك ← ٢ الخطة بصورها ← ٣ وافق وابنِ */
let PV2=null, PVAG='', PVT0=0;
const PVIMG=[['pin','pvPin'],['web','pvWeb'],['me','pvMe']], PVGEN=[['code','pvCode'],['chat','pvChat'],['higgs','pvHiggs'],['api','pvApi'],['self','pvSelf']];
function pvPrefs(){ const p=(PLAN&&PLAN.prefs)||{}; return {img:p.img||['pin','web','me'],gen:p.gen||['code']}; }
async function planBoard(sub){ if(!PLAN||!PLAN.ok) PLAN=await api('/hs/plan'); PV2=PV2||{sub:PLAN&&PLAN.ok&&(PLAN.items||[]).length?2:1}; if(sub) PV2.sub=sub; let w=$('#planv'); if(!w){ w=document.createElement('div'); w.id='planv'; document.body.appendChild(w); }
  const tb=$('#top').getBoundingClientRect(); w.style.top=Math.round(tb.bottom)+'px'; pvDraw(); stepsLive(); }
function pvClose(){ const w=$('#planv'); if(w) w.remove(); PV2=null; renderRight(); }
function pvBusy(){ return !!(PVAG&&PULSE&&PULSE.agent&&PULSE.agent.running); }
function pvDraw(){ const w=$('#planv'); if(!w||!PV2) return; const P_=PLAN&&PLAN.ok?PLAN:null, items=(P_&&P_.items)||[], pr=pvPrefs(), busy=pvBusy();
  const head='<div class="pvh"><h3>'+clLogo(20)+t('pvT')+'</h3><div class="pvs">'+[1,2,3].map(k=>'<button class="'+(PV2.sub===k?'on':'')+(PV2.sub>k?' done':'')+'" data-pvsub="'+k+'"'+(k>1&&!items.length?' disabled':'')+'><i>'+k+'</i>'+t(['pvS1','pvS2','pvS3'][k-1])+'</button>').join('<span class="pvline"></span>')+'</div><button class="sm ghost" data-pvx="1">'+t('pvBack')+'</button></div>';
  if(busy&&PVAG==='planw'){ const el=Math.round((Date.now()-PVT0)/1000); if(w.querySelector('#pvLoad')){ clLoaderTick(w,el); return; }
    w.innerHTML=head+'<div class="pvb"><div class="pvwrap">'+clLoader('pvLoad',t('pvlT'),t('pvlS'))+'<div class="cll-acts"><button class="sm ghost" data-pvstop="1">'+t('tkStop')+'</button></div></div></div>'; clLoaderTick(w,el); return; }
  let o=head+'<div class="pvb"><div class="pvwrap'+(PV2.sub===2?' wide':'')+'">';
  if(busy){ const el=Math.round((Date.now()-PVT0)/1000); o+='<div class="tkai on pvbusy"><span class="cll-mini">'+clLogo(18)+'</span><p>'+t(PVAG==='planw'?'pvWriting':PVAG==='planimg'?'pvFetching':'pvMaking')+' · '+t('pvElapsed',fmtm(el))+(PVAG==='planw'?' · '+t('pvUsually'):'')+'</p><button class="sm ghost" data-pvstop="1">'+t('tkStop')+'</button></div>'; }
  if(PV2.sub===1){
    o+='<div class="pvidea"><div class="pvq"><label>'+t('pvIdeaQ')+'</label><textarea id="pvIdea" rows="4" dir="auto" placeholder="'+esc(t('pvIdeaPh'))+'">'+esc((P_&&P_.idea)||'')+'</textarea></div>'
      +'<div class="pvq"><label>'+t('pvImgQ')+'</label><div class="chips">'+PVIMG.map(([k,l])=>'<button class="'+(pr.img.includes(k)?'on':'')+'" data-pvimg="'+k+'">'+t(l)+'</button>').join('')+'</div><p class="hint">'+t('pvImgHint')+'</p></div>'
      +'<div class="pvq"><label>'+t('pvGenQ')+'</label><div class="chips">'+PVGEN.filter(([k])=>k!=='api'||(INFO.apis&&INFO.apis.length)).map(([k,l])=>'<button class="'+(pr.gen.includes(k)?'on':'')+'" data-pvgen="'+k+'">'+t(l)+'</button>').join('')+'</div><p class="hint">'+t('pvGenHint')+'</p></div>'
      +'<div class="pvgo">'+(INFO.claude?'<button class="pri" data-pvwrite="1"'+(busy?' disabled':'')+'>'+clLogo(17,'#fff')+t('pvWrite')+'<span class="tkb">'+t('tokBadge')+'</span></button>':'')+'<button data-pvdraft="1">'+t('pvDraft')+'</button></div></div>'; }
  else if(PV2.sub===2){ const nimg=items.filter(x=>x.src).length, ngen=items.filter(x=>x.kind==='gen'&&!x.src).length, nweb=items.filter(x=>(x.kind==='web'||x.kind==='archive')&&!x.src).length;
    if(P_&&P_.idea) o+='<p class="pvidea1" dir="auto">'+esc(P_.idea)+'</p>';
    o+=scriptNote(P_);
    o+='<div class="pvtools">'+(INFO.claude&&nweb?'<button class="sm" data-pvfetch="1"'+(busy?' disabled':'')+'>'+t('pvFetch',nweb)+'<span class="tkb">'+t('tokBadge')+'</span></button>':'')+(INFO.claude&&ngen?'<button class="sm" data-pvtwo="1"'+(busy?' disabled':'')+'>'+t('pvTwo',Math.min(2,ngen))+'</button>':'')+'<span class="hint">'+t('pvReady',nimg,items.length)+'</span></div>';
    o+='<div class="pvask"><textarea id="pvAsk" rows="2" dir="auto" placeholder="'+esc(t('pvAskPh'))+'">'+esc((P_&&P_.feedback)||'')+'</textarea>'+(INFO.claude?'<button class="sm" data-pvre="1"'+(busy?' disabled':'')+'>'+t('pvRe')+'</button>':'')+'</div>';
    o+='<div class="pvcards">'+items.map((it,i)=>{ const img=it.src?'<img alt="" src="'+esc(it.src)+(it.src.includes('?')?'&':'?')+'v='+(PLAN.at||0)+'">':'<div class="pvph"><span>'+t('pvNotYet')+'</span><small>'+esc(it.kindAr||'')+'</small></div>';
      return '<div class="pvc"><div class="pvch"><b>'+(i+1)+'</b><span dir="auto">'+esc(it.title||'')+'</span><span class="t" data-pvseek="'+(+it.s||0)+'">'+fmt(+it.s||0)+'</span></div><div class="pvimg">'+img
        +'<div class="pvia"><label class="sm" title="'+esc(t('pvFromMe'))+'">'+t('pvFromMe')+'<input type="file" accept="image/*" hidden data-pvup="'+esc(it.id)+'"></label>'+(INFO.claude&&it.kind!=='none'?'<button class="sm" data-pvgen1="'+esc(it.id)+'">'+t('pvGen1')+'</button>':'')+(it.src?'<button class="sm ghost" data-pvclr="'+esc(it.id)+'">×</button>':'')+'</div>'+(it.srcBy?'<i class="pvby">'+esc(t('pvBy_'+it.srcBy)||it.srcBy)+'</i>':'')+'</div>'
        +(it.skip?'<p class="pvskip">'+esc(srvEn(it.skip))+'</p>':'')+pvPrompt(it)
        +(it.speech?'<label>'+t('planSpeech')+'</label><p dir="auto">'+esc(it.speech)+'</p>':'')+(it.show?'<label>'+t('planShow')+'</label><p dir="auto">'+esc(it.show)+'</p>':'')+(it.motion?'<label>'+t('planMotion')+'</label><p dir="auto">'+esc(it.motion)+'</p>':'')
        +'<button class="sm ghost pvrm" data-pvrm="'+esc(it.id)+'">'+t('planRm')+'</button></div>'; }).join('')+'</div>'; }
  else { const nimg=items.filter(x=>x.src).length, miss=items.filter(x=>!x.src&&['gen','web','archive'].includes(x.kind));
    o+='<div class="pvok"><p>'+t('pvOkSum',items.length,nimg)+'</p>'+(miss.length?'<p class="hint">'+t('pvOkMiss',miss.map(x=>items.indexOf(x)+1).join('، '))+'</p>':'')+'<button class="pri" data-pvbuild="1">'+t('pvBuild')+'</button><p class="hint">'+t('pvBuildHint')+'</p></div>'; }
  w.innerHTML=o+'</div></div>'; }
/* 4.53: لو ما فيه حساب توليد مربوط: البرومت جاهز تنسخه، تولّدها بنفسك، وترفعها وتنحط بمكانها */
function pvPrompt(it){ if(it.src||!['gen','web','archive'].includes(it.kind)) return ''; const pr=pvPrefs(), self=it.needSelf||(pr.gen.includes('self')&&!pr.gen.some(g=>g!=='self'));
  const p=String(it.prompt||'').trim()||((it.show||it.speech||'')+' — '+t('pvPrSuffix'));
  return '<div class="pvpr'+(self?' on':'')+'"><div class="pvprh"><b>'+t('pvPrT')+'</b><button class="sm" data-copy="'+esc(p)+'">'+t('pvPrCopy')+'</button></div>'+(self?'<p dir="auto">'+esc(p)+'</p><div class="pvprl"><a href="https://chatgpt.com/" target="_blank" rel="noopener">ChatGPT</a><a href="https://gemini.google.com/app" target="_blank" rel="noopener">Gemini</a><a href="https://higgsfield.ai/" target="_blank" rel="noopener">Higgsfield</a></div><small>'+t('pvPrHow')+'</small>':'')+'</div>'; }
function scriptNote(P_){ const s=P_&&P_.script; if(!s||s.ok==null) return ''; return '<div class="scrnote '+(s.ok?'ok':'bad')+'">'+clLogo(16)+'<span dir="auto"><b>'+t(s.ok?'scrOk':'scrBad')+'</b>'+(s.note?' '+esc(s.note):'')+'</span></div>'; }
async function pvSavePrefs(extra,pr0){ const pr=pr0||pvPrefs();   // 4.53: الاختيار ينحفظ حتى لو الخطة جديدة (كان يرجع للافتراضي)
  PLAN=await api('/hs/plan_set',{prefs:pr,idea:($('#pvIdea')||{}).value,...(extra||{})}); }
/* 4.46: تأكيد من الاستوديو نفسه (بدل نافذة المتصفح) */
function okBox(text){ return new Promise(res=>{ modal('<p dir="auto" style="line-height:1.8;margin:0 0 12px">'+esc(text)+'</p><div class="row"><button class="pri" id="okbY">'+t('okbYes')+'</button><button id="okbN">'+t('cancel')+'</button></div>'); const fin=v=>{ closeModal(); res(v); }; $('#okbY').onclick=()=>fin(true); $('#okbN').onclick=()=>fin(false); }); }
async function pvRun(what,body,warn){ if(!(await tokenGo('ask','mid'))) return; if(warn&&!(await okBox(warn))) return; await save(); const r=await api('/hs/claude_fix',{what,...(body||{})}); if(r&&r.ok){ PVAG=what; PVT0=Date.now(); pvDraw(); } else toast((r&&srvEn(r.msg))||t('failed')); }
document.addEventListener('click',async e=>{ const b=e.target.closest('#planv [data-pvsub],#planv [data-pvx],#planv [data-pvimg],#planv [data-pvgen],#planv [data-pvwrite],#planv [data-pvdraft],#planv [data-pvfetch],#planv [data-pvtwo],#planv [data-pvre],#planv [data-pvgen1],#planv [data-pvclr],#planv [data-pvrm],#planv [data-pvbuild],#planv [data-pvstop],#planv [data-pvseek]'); if(!b) return; const d=b.dataset;
  if(d.pvsub){ if($('#pvIdea')) await pvSavePrefs(); PV2.sub=+d.pvsub; pvDraw(); return; }
  if(d.pvx){ if($('#pvIdea')) await pvSavePrefs(); pvClose(); return; }
  if(d.pvimg||d.pvgen){ const pr=pvPrefs(), L=d.pvimg?pr.img:pr.gen, k=d.pvimg||d.pvgen, i=L.indexOf(k); if(i>=0) L.splice(i,1); else L.push(k); await pvSavePrefs(null,pr); pvDraw(); return; }
  if(d.pvwrite){ await pvSavePrefs(); await pvRun('planw',{text:''}); return; }
  if(d.pvdraft){ await pvSavePrefs({draft:true}); PV2.sub=2; pvDraw(); loadSteps(); return; }
  if(d.pvfetch){ const pr=pvPrefs(); await pvRun('planimg',{},pr.img.includes('pin')?t('pvPinOk'):''); return; }
  if(d.pvtwo||d.pvgen1){ const pr=pvPrefs(), eng=pr.gen.includes('higgs')?'higgs':pr.gen.includes('chat')?'chat':pr.gen.includes('api')&&INFO.apis&&INFO.apis.length?'api':pr.gen.includes('code')?'code':'self'; if(eng==='self'){ toast(t('pvSelfHint')); return; } await pvRun('plangen',{engine:eng,ids:d.pvgen1?[d.pvgen1]:[]},eng==='higgs'?t('pvHiggsOk'):eng==='chat'?t('pvChatOk'):''); return; }
  if(d.pvre){ const tx=($('#pvAsk')||{}).value||''; PLAN=await api('/hs/plan_set',{feedback:tx}); await pvRun('planw',{text:tx}); return; }
  if(d.pvclr){ PLAN=await api('/hs/plan_set',{item:{id:d.pvclr,src:''}}); pvDraw(); return; }
  if(d.pvrm){ PLAN=await api('/hs/plan_set',{rm:d.pvrm}); pvDraw(); return; }
  if(d.pvstop){ await api('/hs/agent_stop',{}); PVAG=''; pvDraw(); return; }
  if(d.pvseek!==undefined){ pvClose(); seek(+d.pvseek); return; }
  if(d.pvbuild){ await save(); PLAN=await api('/hs/plan_set',{approve:true}); const r=await api('/hs/plan_build',{}); if(!r||!r.ok){ toast((r&&srvEn(r.msg))||t('failed')); return; } PLAN=r.plan; pvClose(); await load(true); await loadSteps(); toast(t(r.miss&&r.miss.length?'planBuiltMiss':'planBuiltT').replace('{0}',r.n).replace('{1}',(r.miss||[]).join('، '))); stepGo('build'); return; } });
document.addEventListener('change',async e=>{ const id=e.target.dataset&&e.target.dataset.pvup; if(!id) return; const f=e.target.files[0]; if(!f) return;
  const r=await api('/hs/asset',f,{'X-Name':encodeURIComponent('plan-'+id+'-'+f.name)}); if(!r||!r.ok){ toast((r&&srvEn(r.msg))||t('failed')); return; } PLAN=await api('/hs/plan_set',{item:{id,src:r.src}}); pvDraw(); });
/* 4.43: حركة القص: الجمل المحذوفة تنضم وتختفي من الشريط، والباقي يلتصق، وبعدها يرجع الاستوديو عادي */
function cutFx(){ const raw=TK&&TK.raw||1, it=(TK&&TK.items)||[]; let w=$('#cutfx'); if(w) w.remove(); w=document.createElement('div'); w.id='cutfx';
  w.innerHTML='<div class="in"><b>'+t('cutFxT')+'</b><div class="bars">'+it.map(x=>'<i class="'+(x.drop?'d':'k')+'" style="flex-grow:'+Math.max(0.05,x.e-x.s).toFixed(2)+'"></i>').join('')+'</div><small><bdi dir="ltr">'+fmtm(raw)+'</bdi> ← <bdi dir="ltr">'+fmtm(TK&&TK.kept)+'</bdi></small><small class="ln" dir="auto"></small></div>';
  $('#stage').appendChild(w); void w.offsetWidth; setTimeout(()=>w.classList.add('go'),30); return w; }
function cutFxEnd(){ const w=$('#cutfx'); if(!w) return; w.classList.add('out'); setTimeout(()=>w.remove(),450); }
function tkAudio(src){ try{ if(TKAU){ TKAU.pause(); } }catch(e){} if(playing) stop(); TKAU=new Audio(src); TKAU.play().catch(()=>toast(t('failed'))); }
async function takesClick(el){ const b=el.closest('[data-tkact],[data-tkplay],[data-tkseek],[data-tkscan],[data-tkall],[data-tkapply],[data-tkprev],[data-tkclaude],[data-tkstop],[data-tkedit]'); if(!b) return false; const d=b.dataset;
  if(d.tkedit){ TKEDIT=true; renderLeft(); return true; }
  if(d.tkstop){ await api('/hs/agent_stop',{}); TKAG=false; renderLeft(); return true; }
  if(d.tkact){ const r=await api('/hs/takes_set',{id:d.tkid,action:d.tkact}); if(r&&r.ok!==false){ TK=r; renderLeft(); } else toast((r&&srvEn(r.msg))||t('failed')); return true; }
  if(d.tkplay){ const [s,e]=d.tkplay.split(',').map(Number); tkAudio('/hs/raw.m4a?s='+s.toFixed(2)+'&e='+(e+0.25).toFixed(2)); return true; }
  if(d.tkseek!==undefined){ if(TKAU) TKAU.pause(); if(playing) stop(); seek(+d.tkseek); return true; }
  if(d.tkall!==undefined){ TKALL=d.tkall==='1'; renderLeft(); return true; }
  if(d.tkscan){ toast(t('tkScanning')); const r=await api('/hs/takes_scan',{}); if(r&&r.ok){ TK=r; renderLeft(); } else toast((r&&srvEn(r.msg))||t('failed')); return true; }
  if(d.tkprev){ toast(t('tkPrevBuilding')); tkAudio('/hs/takes_prev.m4a?v='+Date.now()); return true; }
  if(d.tkclaude){ if(!(await tokenGo('takes','mid'))) return true; const tx=($('#tkAsk')||{}).value||''; const r=await api('/hs/claude_fix',{what:'takes',text:tx}); if(r&&r.ok){ TKAG=true; renderLeft(); } else toast((r&&srvEn(r.msg))||t('failed')); return true; }
  if(d.tkapply){ if(TKAU) TKAU.pause(); if(!TK.pending){ await guideTakesDone(); return true; } await save(); const r=await api('/hs/takes_apply',{}); if(!r.ok){ toast(srvEn(r.msg)||t('busyJob')); return true; } const fx=guidePre()||hs().guide; if(fx) cutFx(); else stLoader('rebuild',t('rebuildSub'));
    pollJob(async(p)=>{ try{ await load(true); cutUndoMark(p); await loadTakes(); if(fx) await guideTakesDone(); } finally{ if(fx) cutFxEnd(); else stLoaderHide(); } }); return true; }
  return false; }
function renderLeft(){ const B=$('#lbody'), h=hs(); let o=stepsBar();
  if(LTAB==='takes'){ o+=takesPanel(); }
  else if(LTAB==='audio'){ o+=audioStep(); }
  else if(LTAB==='text'){ o+='<div class="sec"><input type="search" id="q" placeholder="'+t('searchText')+'" value="'+esc(Q)+'"></div><p class="hint" style="margin-top:-8px">'+t('textHint')+'</p>';
    { const nlo=ST.caps.cards.reduce((n,c)=>n+c.w.filter(w=>w.lo).length,0); o+=caprHtml(nlo); }
    ST.caps.cards.forEach((c,i)=>{ const k=key(c); if(Q&&!k.includes(Q)) return;
      o+='<div class="card'+(SEL&&SEL.kind==='cap'&&+SEL.id===i?' on':'')+'" data-card="'+i+'"><span class="t" data-seek="'+c.s+'">'+fmt(c.s)+'</span><div class="ar" dir="rtl">'+c.w.map((w,j)=>'<span class="w'+(w.hot?' hot':'')+(w.lo?' lo':'')+(blIdx(w)>=0?' bl':'')+'" data-w="'+i+':'+j+'"'+(w.lo?' title="'+t('loTip')+'"':'')+'>'+(Q&&w.t.includes(Q)?'<mark>'+esc(w.t)+'</mark>':esc(w.t))+'</span>').join(' ')+'</div><div class="acts"><button class="sm" data-edit="'+i+'">'+t('edit')+'</button><button class="sm ghost" data-drop="'+i+'">'+t('dropSentence')+'</button></div></div>'; }); }
  else { fontLink(); h.fonts.forEach(localFace);
    o+='<div class="sec"><h4>'+t('binClips')+'<button class="sm" data-up="broll">'+t('upload')+'</button></h4><div class="grid3">'+Object.keys(ST.studio.brNeed||{}).map(k=>'<div class="tile" data-add="broll:'+esc(k)+'"><div class="pv" style="background-image:url(/broll/'+esc(k)+'_0001.jpg)"></div><span>'+esc(k)+'</span></div>').join('')+'</div>'+(Object.keys(ST.studio.brNeed||{}).length?'':'<p class="hint">'+t('binClipsEmpty')+'</p>')+'</div>';
    o+=mediaHtml();
    o+='<div class="sec"><h4>'+t('binIntros')+'</h4><div class="grid3">'+['introGlass','introBox','introPill','introType','introTwo','introLower','plainText'].map(k=>'<div class="tile" data-add="text:'+k+'"><div class="pv" dir="rtl"><span style="all:unset;'+({introGlass:'background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.45);padding:2px 8px;border-radius:8px',introBox:'background:#8F73F5;padding:2px 7px;border-radius:6px',introPill:'background:#D2558F;padding:2px 9px;border-radius:12px',introType:'-webkit-text-stroke:.6px #000',introTwo:'line-height:1.2',introLower:'background:rgba(0,0,0,.7);padding:1px 6px;border-radius:5px;font-size:12px',plainText:''}[k])+'">'+t('pv_'+k)+'</span></div><span>'+t(k)+'</span></div>').join('')+'</div></div>';
    o+='<div class="sec"><h4>'+t('binViz')+'</h4><div class="grid3">'+VIZK.map(k=>'<div class="tile" data-add="viz:'+k+'"><div class="pv vz vz-'+k+'">'+pvLang(VIZPV[k])+'</div><span>'+t('vk_'+k)+'</span></div>').join('')+'<div class="tile" data-add="outro:1"><div class="pv" style="background:#1d1d24;color:#fff;font-weight:700;font-size:15px">'+t('endCardPv')+'</div><span>'+t('endCard')+'</span></div><div class="tile" data-add="cover:1"><div class="pv" style="background:#F3F2EE;color:#15151C;font-family:\'Noto Naskh Arabic\';font-weight:700;font-size:22px">'+t('coverDef')+'</div><span>'+t('type_cover')+'</span></div></div><p class="hint">'+t('binVizHint')+'</p><h4 style="margin-top:12px">'+t('shotTitle')+'</h4><div class="row"><input type="text" id="shotUrl" dir="ltr" placeholder="example.com"><button class="sm" id="shotGo">'+t('add')+'</button></div><p class="hint">'+t('webShotHint')+'</p></div>';
    o+='<div class="sec"><h4>'+t('binSplit')+'</h4><div class="grid3">'+CARDS.map(k=>'<div class="tile" data-add="split:'+k+'"><div class="pv cdp">'+CARDPV[k]+'</div><span>'+t('cs2_'+k)+'</span></div>').join('')+'</div><p class="hint">'+t('binSplitHint')+'</p></div>';
    o+='<div class="sec"><h4>'+t('binDraw')+'</h4><button class="sm" data-drawbin="1" style="width:100%;height:40px;display:flex;align-items:center;justify-content:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21c3 0 4-2 5-4s2-3 4-3 3 2 5 2 4-2 4-2"/><path d="M14 4l6 6-8 8-6-6z"/></svg>'+t('drawStartBtn')+'</button><p class="hint">'+t('binDrawHint')+'</p></div>';
    o+='<div class="sec"><h4>'+t('binPerson')+'</h4><div class="grid3">'+BGM.map(m=>'<div class="tile" data-add="bg:'+m+'"><div class="pv bgm bgm-'+m+'"><i></i></div><span>'+t('bg_'+m)+'</span></div>').join('')+'<div class="tile" data-add="behind:1"><div class="pv bgm bhd"><b>'+t('behindDef')+'</b><i></i></div><span>'+t('type_behind')+'</span></div></div><p class="hint">'+t('binPersonHint')+'</p></div>';
    o+='<div class="sec"><h4>'+t('binHooks')+'</h4>'+tog('hooks.on',t('hookLab'),t('hookLabSub'),h.hooks.on);
    if(h.hooks.on){ const it=h.hooks.items; o+=[0,1,2].map(i=>'<div class="row"><input type="radio" name="hk" data-hkact="'+i+'"'+((h.hooks.active||0)===i?' checked':'')+' style="flex:none"><input type="text" dir="auto" data-hk="'+i+'" placeholder="'+t('hookN',i+1)+'" value="'+esc((it[i]||{}).text||'')+'"></div>').join('')
        +seg(t('style'),'hooks.style',[['box',t('bgBox')],['pill',t('bgPill')],['glass',t('fr_glass')],['plain',t('bgNone')]],h.hooks.style)+slider(t('duration'),'hooks.dur',1,5,h.hooks.dur,0.1)+'<p class="hint">'+t('hookHint')+'</p>'; }
    o+='</div>';
    o+='<div class="sec"><h4>'+t('binChars')+'<button class="sm" data-up="char">'+t('upload')+'</button></h4><div class="grid3">'+CHARS.map(c=>'<div class="tile" data-add="char:'+c+'"><div class="pv"><canvas data-spr="'+c+'" width="56" height="56"></canvas></div><span>'+t('char_'+c)+'</span></div>').join('')+'</div><p class="hint">'+t('charHint')+'</p></div>';
    const hasAuto=k=>h.layers.some(l=>l.auto===k);
    o+='<div class="sec"><h4>'+t('binFx')+'</h4><div class="grid3">'+FXS.map(f=>fxTile(f,'data-add="fx:'+f+'"')).join('')+'</div><div class="chips" style="margin-top:9px"><button data-auto="zooms" class="'+(hasAuto('zooms')?'on':'')+'">'+t('autoZooms')+'</button><button data-auto="transitions" class="'+(hasAuto('transitions')?'on':'')+'">'+t('autoTrans')+'</button></div></div>';
    o+='<div class="sec"><h4>'+t('binTrans')+'</h4><div class="grid3">'+TRS.map(f=>fxTile(f,'data-add="tr:'+f+'"')).join('')+'</div><div class="row" style="margin-top:9px"><label>'+t('trDir')+'</label><div class="seg">'+['right','left','up','down'].map(d=>'<button data-k="trDir" data-v="'+d+'" class="'+((hs().trDir||'right')===d?'on':'')+'">'+t('dir_'+d)+'</button>').join('')+'</div></div><p class="hint">'+t('binTransHint')+'</p></div>';
    o+='<div class="sec"><h4>'+t('binAnno')+'</h4><div class="grid3">'+ANK.map(k=>'<div class="tile" data-add="anno:'+k+'"><div class="pv mkp">'+ANPV[k]+'</div><span>'+t('ak_'+k)+'</span></div>').join('')+'</div><p class="hint">'+t('binAnnoHint')+'</p></div>';
    o+='<div class="sec"><h4>'+t('binMarks')+'</h4><div class="grid3">'+MKK.map(k=>'<div class="tile" data-add="mark:'+k+'"><div class="pv mkp">'+MKPV[k]+'</div><span>'+t('mk_'+k)+'</span></div>').join('')+'<div class="tile" data-add="cursor:1"><div class="pv mkp"><svg viewBox="0 0 60 40"><path d="M24 6 L24 32 L31 26 L36 37 L41 35 L36 24 L45 24 Z" fill="#fff" stroke="#15151C" stroke-width="2" stroke-linejoin="round"/></svg></div><span>'+t('type_cursor')+'</span></div></div><p class="hint">'+t('binMarksHint')+'</p>'
      +'<h4 style="margin-top:12px">'+t('binLt')+'</h4><div class="grid3">'+LTS.map(k=>'<div class="tile" data-add="lt:'+k+'"><div class="pv" style="background:#2a2a33">'+pvLang(LTPV[k])+'</div><span>'+t('lt_'+k)+'</span></div>').join('')+'</div>'
      +'<h4 style="margin-top:12px">'+t('binPip')+'</h4><div class="grid3">'+PIPS.map(k=>'<div class="tile" data-add="pip:'+k+'"><div class="pv pipv pip-'+k+'"><i></i></div><span>'+t('pip_'+k)+'</span></div>').join('')+'<div class="tile" data-add="collage:1"><div class="pv" style="background:#E07A3F"><span style="all:unset;width:44%;height:52%;background:#F4EBD8;transform:rotate(-6deg);box-shadow:0 2px 4px #0005"></span></div><span>'+t('type_collage')+'</span></div></div><p class="hint">'+t('binPipHint')+'</p></div>';
    o+='<div class="sec"><h4>'+t('binMg')+'</h4><div class="grid3">'+MGK.map(k=>'<div class="tile" data-add="mg:'+k+'"><div class="pv mkp">'+MGPV[k]+'</div><span>'+t('mg_'+k)+'</span></div>').join('')+'</div><p class="hint">'+t('binMgHint')+'</p></div>';
    { const lk=INFO.looks||{}, cur=(hs().look||{}).name||'', g=(hs().grade||{}).preset||'none';
      o+='<div class="sec"><h4>'+t('binLooks')+'</h4><div class="grid3"><div class="tile'+(!cur?' sel':'')+'" data-add="look:"><div class="pv" style="background:#1d1d24;color:#fff;font-size:13px">'+t('bgNone')+'</div><span>'+t('lookNone')+'</span></div>'+Object.keys(lk).map(k=>{ const L=lk[k], c=L.card||{}; return '<div class="tile'+(cur===k?' sel':'')+'" data-add="look:'+k+'"><div class="pv" style="background:'+esc(c.bgColor||'#222')+';color:'+esc(c.accent||'#fff')+';font-weight:800;font-size:15px"><span style="all:unset;border-bottom:3px solid '+esc(c.accent||'#fff')+'">Aa</span></div><span>'+esc(LANG==='ar'?L.ar:L.en)+'</span></div>'; }).join('')+'</div>'
        +(cur?slider(t('lookAmt'),'look.amount',0,1,hs().look.amount==null?0.5:hs().look.amount,0.05):'')+'<p class="hint">'+t('binLooksHint')+'</p>'
        +'<h4 style="margin-top:12px">'+t('binGrade')+'</h4><div class="grid3">'+GRADES.map(k=>'<div class="tile fxt'+(g===k?' sel':'')+'" data-add="grade:'+k+'"><div class="pv"><i class="fxp" style="background-image:url('+thumbAt(T)+');filter:'+GRADEF[k]+'"></i></div><span>'+t('gr_'+k)+'</span></div>').join('')+'</div>'
        +(g!=='none'?slider(t('gradeAmt'),'grade.amount',0.2,1,hs().grade.amount==null?1:hs().grade.amount,0.05):'')+'<p class="hint">'+t('binGradeHint')+'</p></div>'; }
    o+='<div class="sec"><h4>'+t('binSfx')+'</h4><div class="chips">'+['whoosh_up','whoosh_down','thud','tap'].map(k=>'<button data-sfxadd="'+k+'">'+t('sfx_'+k)+'</button>').join('')+'</div><p class="hint">'+t('binSfxHint')+'</p>'+sfxLibHtml()+'</div>';
    o+='<div class="sec"><h4>'+t('binImages')+'<button class="sm" data-up="image">'+t('upload')+'</button></h4><div class="grid3">'+(INFO.assets||[]).map(a=>'<div class="tile" data-add="image:'+esc(a)+'"><div class="pv" style="background-image:url(/assets/'+encodeURIComponent(a)+');background-size:contain;background-repeat:no-repeat"></div><span>'+esc(a)+'</span></div>').join('')+'</div></div>';
    o+='<div class="sec"><h4>'+t('binFonts')+'<button class="sm" data-up="font">'+t('upload')+'</button></h4>'+(h.fonts.length?h.fonts.map(f=>'<div class="item" style="cursor:default"><span style="font-family:\''+esc(f.name)+'\';font-size:16px">'+esc(f.name)+'</span></div>').join(''):'<p class="hint">'+t('binFontsEmpty')+'</p>')+'</div>';
    if((h.ideas||[]).length) o+='<div class="sec"><h4>'+t('binIdeas')+'</h4>'+h.ideas.map(x=>'<div class="item" data-seek="'+(x.t||0)+'"><span>'+esc(x.text)+'</span></div>').join('')+'</div>'; }
  B.innerHTML=o; if(LTAB!=='takes'&&LTAB!=='text') secTabs(B,'L:'+LTAB,ELGROUPS); drawSprites(); }
function drawSprites(){ const w=F.contentWindow, S=w&&w.__hsSpr; if(!S) return; $$('canvas[data-spr]').forEach(cv=>{ const g=S[cv.dataset.spr]; if(!g) return; const x=cv.getContext('2d'), n=g[0].length, p=cv.width/n; x.clearRect(0,0,cv.width,cv.height);
  const body={robo:'#8F73F5',sprout:'#43B072',star:'#F2B33D',cube:'#4C8DFF'}[cv.dataset.spr]; for(let r=0;r<g.length;r++) for(let c=0;c<n;c++){ const ch=g[r][c]; if(ch==='.') continue; x.fillStyle=ch==='W'?'#fff':ch==='E'||ch==='M'?'#15151A':ch==='D'?'rgba(0,0,0,.35)':ch==='A'?'#F2B33D':body; if(ch==='D'){ x.fillStyle=body; x.fillRect(c*p,r*p,p+.5,p+.5); x.fillStyle='rgba(0,0,0,.3)'; } x.fillRect(c*p,r*p,p+.5,p+.5); } }); }
const _sv=b=>'<svg viewBox="0 0 64 40" width="64" height="40" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'+b+'</svg>';
const CARDPV={ list:_sv('<circle cx="54" cy="9" r="2.5" fill="currentColor"/><path d="M14 9h32"/><circle cx="54" cy="20" r="2.5" fill="currentColor"/><path d="M22 20h24"/><circle cx="54" cy="31" r="2.5" fill="currentColor"/><path d="M10 31h36"/>'),
  steps:_sv('<path d="M52 9v22" opacity=".5"/><circle cx="52" cy="8" r="5"/><circle cx="52" cy="20" r="5"/><circle cx="52" cy="32" r="5" fill="currentColor"/><path d="M18 8h24M24 20h18M14 32h28"/>'),
  flow:_sv('<rect x="16" y="2" width="32" height="9" rx="3"/><path d="M32 12v5M29 15l3 3 3-3"/><rect x="16" y="19" width="32" height="9" rx="3"/><path d="M32 29v4"/><rect x="16" y="33" width="32" height="6" rx="3" fill="currentColor"/>'),
  versus:_sv('<rect x="4" y="5" width="24" height="30" rx="4"/><rect x="36" y="5" width="24" height="30" rx="4"/><circle cx="32" cy="12" r="5" fill="currentColor"/>'),
  stat:_sv('<circle cx="32" cy="18" r="14" opacity=".4"/><path d="M32 4a14 14 0 0 1 12 21"/><path d="M22 37h20"/>'),
  check:_sv('<path d="M50 8l3 3 6-6M14 9h28"/><path d="M51 17l6 6M57 17l-6 6M20 20h22" opacity=".7"/><path d="M50 32l3 3 6-6M12 33h30"/>'),
  timeline:_sv('<path d="M46 3v34" opacity=".5"/><circle cx="46" cy="8" r="3" fill="currentColor"/><circle cx="46" cy="20" r="3" fill="currentColor"/><circle cx="46" cy="32" r="3" fill="currentColor"/><path d="M14 8h24M20 20h18M12 32h26"/><path d="M52 8h8M52 20h8M52 32h8" opacity=".6"/>'),
  funnel:_sv('<path d="M6 5h52l-6 9H12zM15 17h34l-6 9H21zM24 29h16l-4 8h-8z" fill="currentColor" fill-opacity=".35"/>'),
  quote:_sv('<path d="M46 6c-4 2-6 5-6 9h6zM57 6c-4 2-6 5-6 9h6z" fill="currentColor"/><path d="M12 24h40M18 32h28"/>'),
  draw:_sv('<circle cx="52" cy="14" r="7"/><rect x="24" y="8" width="16" height="12" rx="3" fill="currentColor"/><circle cx="12" cy="14" r="7"/><path d="M44 14h-3M23 14h-3M20 32h24"/>') };
const CARDDEF={ list:{title:'وش تستفيد',text:'[bolt] أسرع\n[money] أرخص\n[shield] أضمن'}, steps:{title:'ثلاث خطوات',text:'الخطوة الأولى\nالخطوة الثانية\nالخطوة الثالثة'}, flow:{title:'كيف يشتغل',text:'[camera] تصوّر\n[wand] يتمنتج\n[rocket] تنشر'},
  versus:{title:'الفرق',a:'قبل',b:'بعد',text:'ساعات | دقايق\nتعب | راحة'}, stat:{title:'الرقم',value:87,unit:'%',label:'وش يعني هذا الرقم'}, check:{title:'الصح والغلط',text:'+ سوّ كذا\n- لا تسوي كذا\n+ وهذا تمام'},
  timeline:{title:'القصة',text:'2021 | البداية\n2023 | أول نجاح\n2026 | اليوم'}, funnel:{title:'من يكمل؟',text:'يشوفون | 1000\nيكملون | 400\nيشترون | 60'}, quote:{text:'اكتب الجملة القوية هنا',by:''} };
const CITIES={'جدة':[21.49,39.19],'الرياض':[24.71,46.68],'مكة':[21.39,39.86],'المدينة':[24.47,39.61],'الدمام':[26.43,50.1],'أبها':[18.22,42.5],'تبوك':[28.38,36.57],'الطائف':[21.27,40.42],'نيوم':[28.0,35.2],'العلا':[26.62,37.92],'دبي':[25.2,55.27],'أبوظبي':[24.45,54.38],'الدوحة':[25.29,51.53],'الكويت':[29.38,47.99],'المنامة':[26.23,50.59],'مسقط':[23.59,58.41],'القاهرة':[30.04,31.24],'الإسكندرية':[31.2,29.92],'عمّان':[31.95,35.93],'بيروت':[33.89,35.5],'دمشق':[33.51,36.29],'بغداد':[33.31,44.37],'القدس':[31.77,35.23],'صنعاء':[15.37,44.19],'الخرطوم':[15.5,32.56],'طرابلس':[32.89,13.19],'تونس':[36.81,10.18],'الجزائر':[36.75,3.06],'الرباط':[34.02,-6.84],'الدار البيضاء':[33.57,-7.59],'مراكش':[31.63,-7.99],'إسطنبول':[41.01,28.98],'أنقرة':[39.93,32.86],'طهران':[35.69,51.39],'كراتشي':[24.86,67.01],'دلهي':[28.61,77.21],'مومباي':[19.08,72.88],'جاكرتا':[-6.21,106.85],'كوالالمبور':[3.14,101.69],'سنغافورة':[1.35,103.82],'بانكوك':[13.76,100.5],'بكين':[39.9,116.4],'شنغهاي':[31.23,121.47],'هونغ كونغ':[22.32,114.17],'طوكيو':[35.68,139.69],'سيول':[37.57,126.98],'سيدني':[-33.87,151.21],'موسكو':[55.76,37.62],'لندن':[51.51,-0.13],'باريس':[48.86,2.35],'برلين':[52.52,13.4],'مدريد':[40.42,-3.7],'برشلونة':[41.39,2.17],'روما':[41.9,12.5],'أمستردام':[52.37,4.9],'جنيف':[46.2,6.14],'فيينا':[48.21,16.37],'أثينا':[37.98,23.73],'نيروبي':[-1.29,36.82],'لاغوس':[6.52,3.38],'كيب تاون':[-33.92,18.42],'أديس أبابا':[9.03,38.74],'نيويورك':[40.71,-74.01],'واشنطن':[38.91,-77.04],'لوس أنجلوس':[34.05,-118.24],'سان فرانسيسكو':[37.77,-122.42],'شيكاغو':[41.88,-87.63],'ميامي':[25.76,-80.19],'تورنتو':[43.65,-79.38],'مكسيكو':[19.43,-99.13],'ساو باولو':[-23.55,-46.63],'بوينس آيرس':[-34.6,-58.38]};
const cityFind=n=>{ n=String(n||'').trim(); if(CITIES[n]) return n; const k=Object.keys(CITIES).find(c=>c.replace(/[ًَُِّْ]/g,'')===n.replace(/[ًَُِّْ]/g,'')||c.startsWith(n)&&n.length>=3); return k||null; };
/* 4.40: كلمات العينة بالمعاينات الصغيرة بلغة الواجهة */
const PV_EN=[['الاسم','Name'],['خبر ','Big '],['>مهم<','>news<'],[' اليوم<',' today<'],['>حركة<','>MOTION<']];
const pvLang=s=>LANG==='en'?PV_EN.reduce((a,[x,y])=>a.split(x).join(y),s):s;
const VIZPV={ line:'<svg viewBox="0 0 60 40" style="width:70%"><path d="M54 32 L40 26 L28 28 L16 14 L6 6" fill="none" stroke="#2FBF9B" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="6" cy="6" r="3.5" fill="#2FBF9B"/></svg>', slot:'<b style="font-family:monospace">2,480</b>', news:'<span style="all:unset;display:block;background:#fff;color:#15151C;font-size:10px;line-height:1.5;padding:4px;border-radius:4px;text-align:right">خبر <mark style="background:#FFD21F">مهم</mark> اليوم</span>', pctdots:'<b>60%</b>', people:'<i></i><i></i><i></i><i></i><i class="o"></i><i class="o"></i>', fill:'<u></u>', bars:'<s style="height:90%"></s><s style="height:60%"></s><s style="height:38%"></s>', route:'<em></em>', cta:'<b>حركة</b>' };
function addLayer(o){ snap(); const h=hs(); const id='L'+(Math.max(0,...h.layers.map(l=>parseInt(String(l.id).replace(/\D/g,''))||0))+1); const d=o.type==='mg'?(MGDUR[o.kind]||3.5):o.type==='fx'?1.4:o.type==='char'?total():o.type==='split'||o.type==='viz'?5:o.type==='cover'?0.9:3;
  const s=o.type==='char'?0:r3(Math.min(T,Math.max(0,total()-0.5))); const L={id,s,e:r3(Math.min(total(),s+d)),track:o.type==='fx'?2:o.type==='text'||o.type==='behind'?1:0,...o}; h.layers.push(L); select({kind:'layer',id}); live(); if(o.type==='bg'||o.type==='behind') toast(t('visMask')); }
const VIZDEF={ line:{layout:'stage',values:[5,9,7,14,22,31],labels:[],unit:'',title:''}, slot:{layout:'stage',value:2480,unit:'',label:''}, news:{layout:'full',source:'عاجل',text:'اكتب عنوان الخبر هنا',mark:'الخبر'}, pctdots:{layout:'stage',values:[60,86,31],title:''}, people:{layout:'stage',value:70}, fill:{layout:'stage',value:75,color2:'#D9643A',accent:'#1E4FA3'}, bars:{layout:'stage',unit:'م',items:[{label:'الأول',value:828},{label:'الثاني',value:601},{label:'الثالث',value:413}]},
  route:{layout:'stage',from:{name:'الدوحة',lat:25.29,lon:51.53},to:{name:'نيروبي',lat:-1.29,lon:36.82},time:'5 ساعات',mode:'plane'}, cta:{pre:'اكتب كلمة',word:'حركة',post:'يوصلك بالخاص',accent:'#E32BD0'} };
const VIZK=['pctdots','people','fill','bars','route','cta','line','slot','news'];
/* 4.8: موشن جاهز (type=mg) */
const MGK=['stat','slam','check','steps','callout','quote','ring','compare','sting','logo','stretch','rec','notif','search','apps','articles','mosaic','rewind','ba','freeze'];   // 4.28 · 4.36: تجميد اللقطة: من مقطعين أرسلهم راكان
const MGDUR={stat:3.6,slam:2.6,check:5,steps:6,callout:3,quote:4.6,ring:3.4,compare:5,sting:2.4,logo:2.2,stretch:2.4,rec:6,notif:6,search:4.5,apps:3,articles:2.5,mosaic:6,rewind:1.2,ba:5,freeze:2.2};
const MGDEF={ stat:{value:'100',prefix:'',suffix:'%',label:'',y:.24}, slam:{text:'*كلمة* قوية',y:.2}, check:{text:'النقطة الأولى\nالنقطة الثانية\nالنقطة الثالثة',y:.18,cue:'speech'},
  steps:{text:'الفكرة\nالتنفيذ\nالنشر',y:.1}, callout:{x:.5,y:.4,w:.32,h:.12,text:'هنا',at:.3,color:'#FFD21F'}, quote:{text:'اكتب الاقتباس هنا',by:'',role:'',y:.6},
  ring:{value:70,label:'',y:.24}, compare:{title:'',aLabel:'قبل',aValue:'3 ساعات',aSub:'',bLabel:'بعد',bValue:'10 دقائق',bSub:'',win:'b',y:.53}, sting:{brand:'hjs',bg:'#111111',sub:'',y:.5}, logo:{name:'Claude',src:''},
  stretch:{text:'بدون\nبرامج مونتاج',y:.12,stretch:6}, rec:{label:'خام · بدون مايك',y:.04}, notif:{text:'فرّغت كلامك | 80 كلمة بتوقيت كل كلمة\nنظّفت صوتك | بدون مايك\nركّبت الكابشن والموشن | والفيديو جاهز قدامك',app:'Claude',y:.03},
  search:{text:'فيديو',cta:'وصلك كل شي بالخاص',big:true,y:.08}, apps:{icons:'Premiere, CapCut, After Effects, InShot',style:'row',y:.1,count:'0',label:'برامج'},
  articles:{word:'Success',layout:'full',rate:7}, mosaic:{items:[],depth:70}, rewind:{back:4,label:'ترجيع'}, ba:{from:0,aLabel:'بعد كلود',bLabel:'الخام',y:.12}, freeze:{style:'flash',label:'هذا أنا',sub:'',zoom:.08,flash:true} };
const MGPV={ stat:'<svg viewBox="0 0 60 40"><text x="30" y="25" text-anchor="middle" font-size="17" font-weight="800" fill="#fff" font-family="sans-serif">128</text><rect x="12" y="30" width="36" height="3" rx="1.5" fill="#fff" opacity=".25"/><rect x="12" y="30" width="24" height="3" rx="1.5" fill="var(--acc,#D97757)"/></svg>',
  slam:'<svg viewBox="0 0 60 40"><rect x="9" y="12" width="26" height="8" rx="1" fill="#fff"/><rect x="38" y="12" width="13" height="8" rx="1" fill="var(--acc,#D97757)"/><rect x="15" y="24" width="30" height="5" rx="1" fill="#fff" opacity=".5"/></svg>',
  check:'<svg viewBox="0 0 60 40"><circle cx="47" cy="12" r="4" fill="var(--acc,#D97757)"/><rect x="13" y="10" width="28" height="4" rx="2" fill="#fff"/><circle cx="47" cy="25" r="4" fill="var(--acc,#D97757)"/><rect x="19" y="23" width="22" height="4" rx="2" fill="#fff"/><rect x="13" y="30" width="38" height="1" fill="var(--acc,#D97757)"/></svg>',
  steps:'<svg viewBox="0 0 60 40"><rect x="4" y="14" width="15" height="9" rx="4.5" fill="none" stroke="#fff" stroke-width="1.4"/><rect x="22.5" y="14" width="15" height="9" rx="4.5" fill="var(--acc,#D97757)"/><rect x="41" y="14" width="15" height="9" rx="4.5" fill="none" stroke="#fff" stroke-width="1.4" opacity=".5"/><rect x="4" y="27" width="52" height="2" rx="1" fill="#fff" opacity=".25"/><rect x="22" y="27" width="34" height="2" rx="1" fill="var(--acc,#D97757)"/></svg>',
  callout:'<svg viewBox="0 0 60 40"><ellipse cx="30" cy="14" rx="15" ry="8" fill="none" stroke="#FFD21F" stroke-width="2" transform="rotate(-4 30 14)"/><path d="M30 22v6" stroke="#FFD21F" stroke-width="1.6"/><rect x="18" y="28" width="24" height="8" rx="4" fill="#FFD21F"/></svg>',
  quote:'<svg viewBox="0 0 60 40"><rect x="6" y="7" width="48" height="27" rx="5" fill="#111" stroke="#fff" stroke-opacity=".15"/><rect x="47" y="12" width="2" height="12" fill="var(--acc,#D97757)"/><rect x="14" y="13" width="30" height="3" rx="1.5" fill="#fff"/><rect x="20" y="19" width="24" height="3" rx="1.5" fill="#fff"/><rect x="32" y="27" width="12" height="2" rx="1" fill="#fff" opacity=".5"/></svg>',
  ring:'<svg viewBox="0 0 60 40"><circle cx="30" cy="20" r="12" fill="none" stroke="#fff" stroke-opacity=".2" stroke-width="4"/><path d="M30 8a12 12 0 1 1-11.4 15.7" fill="none" stroke="var(--acc,#D97757)" stroke-width="4" stroke-linecap="round"/></svg>',
  compare:'<svg viewBox="0 0 60 40"><rect x="7" y="8" width="20" height="26" rx="3" fill="#F5F5F3" transform="skewY(4)"/><rect x="33" y="10" width="20" height="26" rx="3" fill="#F5F5F3" stroke="var(--acc,#D97757)" stroke-width="1.5" transform="skewY(-4) translate(0 4)"/><circle cx="30" cy="21" r="5" fill="#111"/></svg>',
  logo:'<svg viewBox="0 0 60 40"><rect x="10" y="13" width="40" height="14" rx="7" fill="#111" stroke="#fff" stroke-opacity=".15"/><circle cx="18" cy="20" r="3.6" fill="#F5F5F3"/><rect x="25" y="18.5" width="19" height="3" rx="1.5" fill="#F5F5F3"/></svg>',
  stretch:'<svg viewBox="0 0 60 40"><rect x="8" y="14" width="10" height="9" rx="2" fill="var(--acc,#D97757)"/><rect x="18" y="19" width="24" height="3" fill="var(--acc,#D97757)"/><rect x="42" y="14" width="10" height="9" rx="2" fill="var(--acc,#D97757)"/><rect x="18" y="28" width="24" height="3" rx="1.5" fill="#fff" opacity=".6"/></svg>',
  rec:'<svg viewBox="0 0 60 40"><path d="M6 12V6h6M54 12V6h-6M6 28v6h6M54 28v6h-6" stroke="#fff" stroke-width="1.6" fill="none"/><circle cx="12" cy="11" r="2" fill="#E5484D"/><g fill="#fff">'+[...Array(14)].map((_,i)=>'<rect x="'+(9+i*3)+'" y="'+(20-(i%4)*1.5)+'" width="1.4" height="'+(4+(i%4)*3)+'"/>').join('')+'</g></svg>',
  notif:'<svg viewBox="0 0 60 40"><rect x="6" y="5" width="48" height="10" rx="3" fill="#2a2a2c"/><rect x="45" y="7" width="6" height="6" rx="1.5" fill="var(--acc,#D97757)"/><rect x="6" y="18" width="48" height="10" rx="3" fill="#2a2a2c" opacity=".8"/><rect x="45" y="20" width="6" height="6" rx="1.5" fill="var(--acc,#D97757)" opacity=".8"/><rect x="6" y="31" width="48" height="6" rx="3" fill="#2a2a2c" opacity=".5"/></svg>',
  search:'<svg viewBox="0 0 60 40"><rect x="5" y="8" width="50" height="11" rx="5.5" fill="#fff"/><circle cx="11" cy="13.5" r="3.6" fill="var(--acc,#D97757)"/><rect x="30" y="12" width="18" height="3" rx="1.5" fill="#111"/><rect x="18" y="25" width="24" height="8" rx="4" fill="var(--acc,#D97757)"/></svg>',
  apps:'<svg viewBox="0 0 60 40"><rect x="6" y="12" width="14" height="14" rx="3.5" fill="#00005B"/><rect x="23" y="12" width="14" height="14" rx="3.5" fill="#000" stroke="#fff" stroke-opacity=".3"/><rect x="40" y="12" width="14" height="14" rx="3.5" fill="#00005B"/><path d="M8 14l10 10M18 14L8 24M42 14l10 10M52 14l-10 10" stroke="#E5484D" stroke-width="2"/></svg>',
  articles:'<svg viewBox="0 0 60 40"><rect x="8" y="3" width="44" height="34" fill="#ECE9E2" transform="rotate(-3 30 20)"/><rect x="13" y="10" width="34" height="2.5" fill="#999"/><rect x="22" y="18" width="16" height="5" fill="#F4E04D"/><rect x="13" y="19" width="8" height="3" fill="#333"/><rect x="39" y="19" width="8" height="3" fill="#333"/><rect x="13" y="27" width="34" height="2.5" fill="#999"/></svg>',
  mosaic:'<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#111"/>'+[...Array(48)].map((_,i)=>'<rect x="'+(2+(i%8)*7.2)+'" y="'+(2+Math.floor(i/8)*6.2)+'" width="6" height="5" fill="#'+['777','999','555','aaa','666'][i%5]+'"/>').join('')+'<rect x="23" y="13" width="14" height="14" fill="none" stroke="var(--acc,#D97757)" stroke-width="1.5"/></svg>',
  rewind:'<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#222"/><path d="M28 20l10-7v14zM17 20l10-7v14z" fill="#fff"/><rect y="9" width="60" height="2" fill="#fff" opacity=".2"/><rect y="29" width="60" height="3" fill="#fff" opacity=".15"/></svg>',
  ba:'<svg viewBox="0 0 60 40"><rect x="7" y="6" width="21" height="28" rx="3" fill="#444" stroke="var(--acc,#D97757)" stroke-width="1.5"/><rect x="32" y="6" width="21" height="28" rx="3" fill="#444"/><circle cx="30" cy="20" r="3.5" fill="var(--acc,#D97757)"/></svg>',
  freeze:'<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#2a2a2c"/><rect x="14" y="5" width="32" height="30" fill="#F7F5F0" transform="rotate(-5 30 20)"/><rect x="17" y="8" width="26" height="19" fill="#555" transform="rotate(-5 30 20)"/><rect x="26" y="12" width="3" height="10" fill="#fff" transform="rotate(-5 30 20)"/><rect x="31" y="12" width="3" height="10" fill="#fff" transform="rotate(-5 30 20)"/></svg>',
  sting:'<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#111"/><rect x="21" y="11" width="10.4" height="3.2" fill="#F5F5F3"/><rect x="25.3" y="18.4" width="13.7" height="3.2" fill="#F5F5F3"/><rect x="21" y="25.8" width="7.2" height="3.2" fill="#F5F5F3"/></svg>' };
const mgName=L=>{ const k=L.kind||'stat', d=k==='stat'||k==='ring'?((L.prefix||'')+(L.value==null?'':L.value)+(k==='ring'?'%':(L.suffix||''))+' '+(L.label||'')).trim():k==='compare'?[L.aLabel,L.bLabel].filter(Boolean).join(' / '):k==='sting'?(L.brand==='text'?(L.text||''):L.brand==='logo'?'':'HJS'):k==='logo'?[L.name,L.name2].filter(Boolean).join(' / '):k==='freeze'?[t('frz_'+(L.style||'flash')),L.label].filter(Boolean).join(' · '):(L.title||String(L.text||'').split('\n')[0].replace(/\*/g,'')); return t('mg_'+k)+(d?' · '+d:''); };
function mgPanel(L){ const k=L.kind, ti=(key,v,ph)=>'<input type="text" data-k="'+key+'" dir="auto" value="'+esc(v==null?'':v)+'" placeholder="'+esc(ph||'')+'" style="margin-bottom:8px">', ta=(key,v,rows)=>'<textarea data-k="'+key+'" rows="'+(rows||3)+'" dir="auto" style="margin-bottom:9px">'+esc(v||'')+'</textarea>';
  let o='<div class="grid3" style="margin-bottom:9px">'+MGK.map(x=>'<div class="tile'+(x===k?' sel':'')+'" data-mgkind="'+x+'"><div class="pv mkp" style="pointer-events:none">'+MGPV[x]+'</div><span style="pointer-events:none">'+t('mg_'+x)+'</span></div>').join('')+'</div>';
  const acc=swatches(t('accent'),'L.accent',L.accent||lookAccOf(hs())||(ST.theme&&ST.theme.acc)||'#D97757'), yS=(d)=>slider(t('posY'),'L.y',0.05,0.95,L.y==null?d:L.y,0.005), font=pick(t('font'),'L.font',[['',t('stSame')],...[...[...new Set(hs().fonts.map(f=>f.name))],...AR_FONTS].map(f=>[f,f])],L.font||'');
  if(k==='stat') o+=ti('L.value',L.value,t('mgValue'))+'<div class="row2">'+ti('L.prefix',L.prefix,t('mgPrefix'))+ti('L.suffix',L.suffix,t('mgSuffix'))+'</div>'+ti('L.label',L.label,t('mgLabel'))+ti('L.max',L.max,t('mgMax'))+yS(0.24)+slider(t('size'),'L.size',120,360,L.size||240)+acc+font;
  else if(k==='slam') o+='<p class="hint">'+t('mgSlamHint')+'</p>'+ta('L.text',L.text,2)+yS(0.2)+acc+font;
  else if(k==='check') o+=ti('L.title',L.title,t('mgTitle'))+'<p class="hint">'+t('mgItemsHint')+'</p>'+ta('L.text',L.text,4)+seg(t('mgCue'),'L.cue',[['speech',t('cueSpeech')],['even',t('cueEven')]],L.cue||'speech')+seg(t('mgScrim'),'L.scrim',[[true,t('yes')],[false,t('no')]],L.scrim!==false)+yS(0.18)+slider(t('size'),'L.size',40,80,L.size||58)+acc+font;
  else if(k==='steps') o+='<p class="hint">'+t('mgItemsHint')+'</p>'+ta('L.text',L.text,4)+ti('L.at',Array.isArray(L.at)?L.at.join(', '):L.at,t('mgAt'))+yS(0.1)+acc+font;
  else if(k==='callout') o+=ti('L.text',L.text,t('mgLabel'))+slider(t('posX'),'L.x',0,1,L.x==null?0.5:L.x,0.005)+slider(t('posY'),'L.y',0,1,L.y==null?0.42:L.y,0.005)+slider(t('mgW'),'L.w',0.05,0.9,L.w||0.3,0.01)+slider(t('mgH'),'L.h',0.03,0.5,L.h||0.12,0.005)+slider(t('mgAtOne'),'L.at',0,Math.max(0.5,+(L.e-L.s-0.6).toFixed(2)),L.at==null?0.3:L.at,0.05)+swatches(t('color'),'L.color',L.color||'#FFD21F');
  else if(k==='quote') o+=ta('L.text',L.text,3)+'<div class="row2">'+ti('L.by',L.by,t('mgBy'))+ti('L.role',L.role,t('mgRole'))+'</div>'+yS(0.6)+acc;
  else if(k==='ring') o+=slider(t('mgValue'),'L.value',0,100,L.value==null?70:+L.value,1)+ti('L.label',L.label,t('mgLabel'))+yS(0.24)+slider(t('size'),'L.size',200,560,L.size||360)+acc+font;
  else if(k==='compare') o+=ti('L.title',L.title,t('mgTitle'))+'<h4 style="margin:6px 0">'+t('mgA')+'</h4>'+ti('L.aLabel',L.aLabel,t('mgLabel'))+ti('L.aValue',L.aValue,t('mgVal'))+ti('L.aSub',L.aSub,t('mgSubT'))+'<h4 style="margin:6px 0">'+t('mgB')+'</h4>'+ti('L.bLabel',L.bLabel,t('mgLabel'))+ti('L.bValue',L.bValue,t('mgVal'))+ti('L.bSub',L.bSub,t('mgSubT'))
    +seg(t('mgWin'),'L.win',[['a',t('mgA')],['b',t('mgB')],['none',t('no')]],L.win||'none')+acc+font;
  else if(k==='sting'){ const im=(INFO.assets||[]).filter(a=>/\.(png|jpe?g|webp|svg)$/i.test(a)); o+=seg(t('mgBrand'),'L.brand',[['hjs',t('brandHjs')],['text',t('brandText')],['logo',t('brandLogo')]],L.brand||'hjs');
    if(L.brand==='text') o+=ti('L.text',L.text,t('brandText'))+font; if(L.brand==='logo') o+=im.length?pick(t('brandLogo'),'L.src',im.map(a=>['assets/'+a,a]),L.src||''):'<p class="hint">'+t('mgNoImg')+'</p>';
    o+=ti('L.sub',L.sub,t('mgTag'))+'<div class="row"><label>'+t('mgBg')+'</label><div class="sw">'+['#111111','#F5F5F3','#1C1A19','#E8DCC8','none'].map(c=>'<i data-k="L.bg" data-c="'+c+'" class="'+((L.bg==null?'#111111':L.bg)===c?'on':'')+'" style="background:'+(c==='none'?'repeating-linear-gradient(45deg,#666 0 4px,#999 4px 8px)':c)+'"></i>').join('')+'</div></div>'+seg(t('mgFlash'),'L.flash',[[true,t('yes')],[false,t('no')]],L.flash!==false)+yS(0.5); }
  else if(k==='stretch') o+='<p class="hint">'+t('mgStretchHint')+'</p>'+ta('L.text',L.text,2)+slider(t('mgStretchN'),'L.stretch',2,14,L.stretch||6,1)+slider(t('size'),'L.size',100,240,L.size||170)+yS(0.13)+acc+font;
  else if(k==='rec') o+=ti('L.label',L.label,t('mgLabel'))+seg(t('mgClock'),'L.clock',[['clip',t('mgClockClip')],['layer',t('mgClockLayer')]],L.clock||'clip')+yS(0.04)+acc;
  else if(k==='notif') o+='<p class="hint">'+t('mgNotifHint')+'</p>'+ta('L.text',L.text,4)+ti('L.app',L.app,t('mgApp'))+ti('L.at',Array.isArray(L.at)?L.at.join(', '):L.at,t('mgAt'))+yS(0.03)+acc+font;
  else if(k==='search') o+=ti('L.text',L.text,t('mgTyped'))+ti('L.cta',L.cta,t('mgCta'))+seg(t('mgBig'),'L.big',[[true,t('yes')],[false,t('no')]],L.big!==false)+yS(0.08)+acc+font;
  else if(k==='apps') o+='<p class="hint">'+t('mgAppsHint')+'</p>'+ti('L.icons',L.icons,'Premiere, CapCut')+seg(t('mgAppsStyle'),'L.style',[['row',t('mgAppsRow')],['wall',t('mgAppsWall')]],L.style||'row')
    +((L.style||'row')==='wall'?'<div class="row2">'+ti('L.count',L.count,'0')+ti('L.label',L.label,t('mgLabel'))+'</div>'+seg(t('mgLaptop'),'L.laptop',[[true,t('yes')],[false,t('no')]],L.laptop!==false):yS(0.1)+slider(t('size'),'L.size',80,200,L.size||130))+acc+font;
  else if(k==='articles') o+=ti('L.word',L.word,t('mgWord'))+seg(t('display'),'L.layout',[['full',t('brFull')],['card',t('brCard')]],L.layout||'full')+'<p class="hint">'+t('mgLinesHint')+'</p>'+ta('L.lines',L.lines,3)+slider(t('mgRate'),'L.rate',3,14,L.rate||7,1)+(L.layout==='card'?yS(0.6):'');
  else if(k==='mosaic'){ const im=(INFO.assets||[]).filter(a=>/\.(png|jpe?g|webp)$/i.test(a)), on=new Set((L.items||[]).map(e=>e&&e.src));
    o+='<p class="hint">'+t('mgMosaicHint')+'</p>'+(im.length?'<div class="grid3" style="margin-bottom:8px">'+im.slice(0,60).map(a=>'<div class="tile'+(on.has('assets/'+a)?' sel':'')+'" data-mgimg="assets/'+esc(a)+'"><div class="pv" style="background:#000 url(\'/assets/'+encodeURIComponent(a)+'\') center/cover"></div></div>').join('')+'</div>':'<p class="hint">'+t('mgNoImg')+'</p>')
      +slider(t('mgDepth'),'L.depth',20,140,L.depth||70,1)+seg(t('mgColor'),'L.color',[[false,t('mgGray')],[true,t('mgColorful')]],!!L.color); }
  else if(k==='rewind') o+='<p class="hint">'+t('mgRewindHint')+'</p>'+slider(t('mgBack'),'L.back',1,12,L.back||4,0.5)+ti('L.label',L.label,LANG==='en'?'Rewind':'ترجيع');
  else if(k==='freeze'){ const st=L.style||'flash'; o+='<p class="hint">'+t('frzHint')+'</p>'+seg(t('frzStyle'),'L.style',[['flash',t('frz_flash')],['photo',t('frz_photo')],['comic',t('frz_comic')],['film',t('frz_film')]],st)+'<p class="hint">'+t('frzH_'+st)+'</p>'+ti('L.label',L.label,t('frzLabel'))+(st!=='flash'?ti('L.sub',L.sub,t('frzSub')):'')
    +(st==='flash'?slider(t('frzZoom'),'L.zoom',0,0.3,L.zoom==null?0.08:+L.zoom,0.01):'')+(st==='photo'?slider(t('frzTilt'),'L.tilt',-12,12,L.tilt==null?-4:+L.tilt,1):'')+(st==='comic'?yS(0.1):'')
    +seg(t('mgFlash'),'L.flash',[[true,t('yes')],[false,t('no')]],L.flash!==false)+seg(t('frzCap'),'L.nocap',[[false,t('frzCapOn')],[true,t('frzCapOff')]],!!L.nocap)+(st==='flash'?acc:'')+font; }
  else if(k==='ba') o+='<p class="hint">'+t('mgBaHint')+'</p>'+slider(t('mgFrom'),'L.from',0,Math.max(1,+(total()-1).toFixed(1)),L.from||0,0.1)+'<div class="row2">'+ti('L.aLabel',L.aLabel,LANG==='en'?'After Claude':'بعد كلود')+ti('L.bLabel',L.bLabel,LANG==='en'?'Raw':'الخام')+'</div>'+yS(0.12)+acc;
  else if(k==='logo'){ const im=(INFO.assets||[]).filter(a=>/\.(png|jpe?g|webp|svg)$/i.test(a)).map(a=>['assets/'+a,a]), lg=L.src&&!im.some(x=>x[0]===L.src)?[[L.src,L.src.split('/').pop()]]:[], lg2=L.src2&&!im.some(x=>x[0]===L.src2)?[[L.src2,L.src2.split('/').pop()]]:[];
    o+='<p class="hint">'+t('mgLogoHint')+'</p>'+'<div class="row2">'+ti('L.name',L.name,t('mgLogoName'))+'<button class="btn" data-mglogo="1">'+t('mgLogoGet')+'</button></div>'+pick(t('brandLogo'),'L.src',[['',t('mgLogoMono')],...lg,...im],L.src||'');
    o+='<h4 style="margin:6px 0">'+t('mgLogoVs')+'</h4><div class="row2">'+ti('L.name2',L.name2,t('mgLogoName2'))+'<button class="btn" data-mglogo="2">'+t('mgLogoGet')+'</button></div>'+(L.name2?ti('L.rel',L.rel,LANG==='en'?'better than':'أفضل من')+pick(t('brandLogo'),'L.src2',[['',t('mgLogoMono')],...lg2,...im],L.src2||''):'');
    o+=slider(t('size'),'L.size',64,120,L.size||88)+slider(t('posY'),'L.y',0.05,0.95,L.y==null?0.62:L.y,0.005)+acc+'<button class="btn" data-mglogos="1" style="width:100%;margin-top:8px">'+t('mgLogosAuto')+'</button>'; }
  return o; }

/* 4.40: لو الواجهة إنجليزي، العنصر الجديد يجي بنص إنجليزي بداله (نفس الحقول، النص بس) */
const DEF_EN={ mg:{slam:{text:'*Bold* words'},check:{text:'First point\nSecond point\nThird point'},steps:{text:'Idea\nBuild\nPublish'},callout:{text:'Here'},quote:{text:'Write the quote here'},
    compare:{aLabel:'Before',aValue:'3 hours',bLabel:'After',bValue:'10 minutes'},stretch:{text:'No\nediting apps'},rec:{label:'Raw · no mic'},
    notif:{text:'Transcribed your words | 80 words, each one timed\nCleaned your voice | no mic needed\nAdded captions and motion | your video is ready'},search:{text:'video',cta:'Everything sent to your DMs'},
    apps:{label:'apps'},rewind:{label:'Rewind'},ba:{aLabel:'After Claude',bLabel:'Raw'},freeze:{label:"That's me"}},
  card:{list:{title:'What you get',text:'[bolt] Faster\n[money] Cheaper\n[shield] Safer'},steps:{title:'Three steps',text:'Step one\nStep two\nStep three'},flow:{title:'How it works',text:'[camera] Film\n[wand] Edit\n[rocket] Post'},
    versus:{title:'The difference',a:'Before',b:'After',text:'Hours | Minutes\nTiring | Easy'},stat:{title:'The number',label:'What this number means'},check:{title:"Do and don't",text:"+ Do this\n- Don't do that\n+ This is fine"},
    timeline:{title:'The story',text:'2021 | The start\n2023 | First win\n2026 | Today'},funnel:{title:'Who stays?',text:'Watch | 1000\nFinish | 400\nBuy | 60'},quote:{text:'Write the strong line here'}},
  viz:{news:{source:'Breaking',text:'Write the headline here',mark:'headline'},bars:{unit:'m',items:[{label:'First',value:828},{label:'Second',value:601},{label:'Third',value:413}]},
    route:{from:{name:'Doha',lat:25.29,lon:51.53},to:{name:'Nairobi',lat:-1.29,lon:36.82},time:'5 hours'},cta:{pre:'Comment',word:'MOTION',post:'and get it in your DMs'}},
  an:{tags:{labels:['Me']},bubble:{text:'This is it'},scan:{labels:['Done']},burst:{text:'Wow'}},
  pre:{introGlass:{text:'Video title'},introBox:{text:'Video title'},introPill:{text:'Video title'},introType:{text:'Video title'},introTwo:{text:'First line\nSecond line'},introLower:{text:'Name · Title'},plainText:{text:'Text'}},
  outro:{l1:'Thanks for watching',cta:'Follow',word:'for more'} };
function DF(tab,k){ const B={mg:MGDEF,card:CARDDEF,viz:VIZDEF,an:ANDEF,pre:PRE}[tab], b=tab==='outro'?OUTRO_DEF:(B&&B[k]); if(!b) return b; const o=JSON.parse(JSON.stringify(b));
  if(LANG==='en'){ const e=tab==='outro'?DEF_EN.outro:(DEF_EN[tab]||{})[k]; if(e) Object.assign(o,JSON.parse(JSON.stringify(e))); } return o; }
const PRE={ introGlass:{text:'عنوان المقطع',size:92,bg:'glass',anim:'rise',x:.5,y:.72,weight:800,font:'Noto Naskh Arabic'}, introBox:{text:'عنوان المقطع',size:104,bg:'box',bgColor:'#8F73F5',anim:'pop',x:.5,y:.2,weight:900}, introPill:{text:'عنوان المقطع',size:92,bg:'pill',bgColor:'#D2558F',anim:'rise',x:.5,y:.2,weight:900},
  introType:{text:'عنوان المقطع',size:110,bg:'none',stroke:7,anim:'type',x:.5,y:.2,weight:900}, introTwo:{text:'السطر الأول\nالسطر الثاني',size:96,bg:'none',stroke:6,anim:'drop',x:.5,y:.22,weight:900},
  introLower:{text:'الاسم · الوصف',size:54,bg:'box',bgColor:'#000000',bgOpacity:.7,anim:'slide',x:.5,y:.7,weight:700}, plainText:{text:'نص',size:80,bg:'none',anim:'fade',x:.5,y:.4,weight:800} };
$('#lbody').addEventListener('input',e=>{ const el=e.target; if(el.id==='mq'||el.id==='gTx') return; if(el.id==='sfxQ'){ SFXQ=el.value.trim(); const bx=$('#sfxBox'); if(bx) bx.innerHTML=sfxBoxHtml(); return; } if(el.id==='q'){ Q=el.value.trim(); const pos=el.selectionStart; renderLeft(); const n=$('#q'); n.focus(); n.setSelectionRange(pos,pos); return; }
  if(el.dataset.hk!==undefined){ const h=hs().hooks, i=+el.dataset.hk; while(h.items.length<=i) h.items.push({text:''}); h.items[i].text=el.value; live(); return; }
  panelInput(e); });
$('#lbody').addEventListener('keydown',e=>{ if(e.target.id==='mq'&&e.key==='Enter'){ e.preventDefault(); mediaSearch(); } });
$('#lbody').addEventListener('change',e=>{ if(e.target.dataset.hkact!==undefined){ snap(); hs().hooks.active=+e.target.dataset.hkact; live(); if(T>hs().hooks.dur) seek(0.6); } });
$('#lbody').addEventListener('click',async e=>{ const el=e.target, d=el.dataset, tile=el.closest('[data-add]');
  if(LTAB==='takes'&&await takesClick(el)) return;
  if(LTAB==='audio'&&await auStepClick(el)) return;
  { const sb=el.closest('[data-step]'); if(sb){ stepGo(sb.dataset.step); return; } }
  if(LTAB==='text'&&await caprClick(el)) return;
  if(d.loclaude){ const r=await api('/hs/claude_fix',{what:'unsure'}); toast((r&&srvEn(r.msg))||t(r&&r.ok?'loSent':'failed')); return; }
  if(d.lorefresh){ await save(); const r=await api('/hs/unsure',{}); if(r&&r.ok){ await load(true); toast(t('loCount',r.n)); } return; }
  if(d.seek!==undefined){ if(playing) stop(); seek(+d.seek+0.02); const c=el.closest('.card'); if(c) select({kind:'cap',id:+c.dataset.card}); return; }
  if(d.w){ snap(); const [i,j]=d.w.split(':').map(Number), w=ST.caps.cards[i].w[j]; w.hot=!w.hot; el.classList.toggle('hot',w.hot); drawT(T); dirty(); return; }
  if(d.edit!==undefined){ editCard(+d.edit); return; }
  if(d.drop!==undefined){ askRemove({cards:[+d.drop]},'«'+key(ST.caps.cards[+d.drop])+'»'); return; }
  if(d.up){ pickFile(d.up); return; }
  if(el.id==='mGo'){ mediaSearch(); return; }
  if(d.mfit){ MEDIA.fit=d.mfit; renderLeft(); return; }
  if(d.gen){ genAsk(d.gen); return; }
  if(d.gopen){ genOpen(d.gopen); return; } if(d.gup){ genUpload(d.gup); return; } if(d.gcl){ genClaude(d.gcl); return; } if(d.grm){ genRm(d.grm); return; }
  if(d.mkind){ MEDIA.kind=d.mkind; MEDIA.items=[]; MEDIA.msg=''; renderLeft(); return; }
  if(el.id==='shotGo'){ const u=$('#shotUrl').value.trim(); if(!u) return; el.disabled=true; await save(); const gh=ghostAdd(T,4,t('shotBusy')); let r=null; try{ r=await api('/hs/shot',{url:u,at:T,dur:4}); } finally{ ghostDone(gh); el.disabled=false; } if(!r||!r.ok){ toast((r&&srvEn(r.msg))||t('failed')); return; } await load(true); select({kind:'layer',id:r.id}); toast(t('imageAdded')); return; }
  if(d.sfxplay){ sfxPlay(d.sfxplay); return; }
  if(d.myedit){ myEdit(d.myedit); return; }
  if(el.id==='myOpen'){ const r=await api('/hs/open_sounds',{}); toast(r.ok?t('myOpened'):(r.dir||t('failed'))); return; }
  if(d.sfxlib){ const it=SFXLIB.find(x=>x.id===d.sfxlib); if(it&&!it.have){ toast(t('sfxGetting')); const r=await api('/hs/sfx_fetch',{ids:[it.id]}); if(!r.ok){ toast(srvEn(r.msg)||t('failed')); return; } it.have=true; renderLeft(); } sfxAdd(d.sfxlib); return; }
  if(el.id==='sfxAll'){ el.disabled=true; toast(t('sfxGetting')); const r=await api('/hs/sfx_fetch',{ids:sfxShown().filter(x=>!x.have).map(x=>x.id)}); await sfxLibLoad(); renderLeft(); toast(r.ok?t('sfxGotAll'):(srvEn(r.msg)||t('failed'))); return; }
  if(d.sfxcat){ SFXCAT=d.sfxcat; document.querySelectorAll('[data-sfxcat]').forEach(b=>b.classList.toggle('on',b.dataset.sfxcat===SFXCAT)); const bx=$('#sfxBox'); if(bx) bx.innerHTML=sfxBoxHtml(); return; }
  if(d.sfxadd){ sfxAdd(d.sfxadd); return; }
  if(d.auto){ autoFx(d.auto,!el.classList.contains('on')); return; }
  const mt=el.closest('[data-madd]'); if(mt){ const it=MEDIA.items[+mt.dataset.madd]; toast(t('downloading')); await save(); const r=await api('/hs/media_add',{item:it,at:T,dur:it.kind==='video'?4:3,fit:MEDIA.fit}); if(!r.ok){ toast(srvEn(r.msg)||t('failed')); return; } await load(true); if(r.id) select({kind:'layer',id:r.id}); toast(t(it.kind==='video'?'clipAdded':'imageAdded')); return; }
  if(tile){ const [kind,arg]=tile.dataset.add.split(/:(.*)/);
    if(kind==='text') addLayer({type:'text',font:hs().cap.font,color:'#FFFFFF',...DF('pre',arg)});
    else if(kind==='char') addLayer({type:'char',char:arg,x:.2,y:.62,size:.26,color:{robo:'#8F73F5',sprout:'#43B072',star:'#F2B33D',cube:'#4C8DFF'}[arg],anim:'pop',react:true});
    else if(kind==='fx') addLayer({type:'fx',fx:arg,amount:.6});
    else if(kind==='viz') addLayer({type:'viz',kind:arg,track:2,...DF('viz',arg),...(hs().cardDefault?{accent:hs().cardDefault.accent}:{})});
    else if(kind==='tr') addLayer({...trAdd(arg,T),s:r3(Math.max(0,T-0.3)),e:r3(Math.min(total(),T+0.35))});
    else if(kind==='anno') addLayer({type:'anno',kind:arg,track:1,anim:'none',...(DF('an',arg)||{})});
    else if(kind==='mark') addLayer({type:'mark',kind:arg,x:.5,y:arg==='underline'?.62:.4,w:arg==='check'||arg==='cross'?.22:.46,h:arg==='underline'?.03:arg==='highlight'?.05:.1,color:arg==='cross'||arg==='arrow'?'#FF4D6D':arg==='check'?'#2FBF9B':'#FFD21F',lw:10,track:1});
    else if(kind==='cursor') addLayer({type:'cursor',x:.5,y:.45,at:1.0,style:'light',track:1});
    else if(kind==='mg') addLayer({type:'mg',kind:arg,track:1,...(DF('mg',arg)||{})});
    else if(kind==='lt') addLayer({type:'lt',style:arg,text:(ST.theme&&ST.theme.handle&&ST.theme.handle!=='@handle'?ST.theme.handle.replace(/^@/,''):t('ltName')),sub:t('ltSub'),side:'right',y:.7,size:64,track:1});
    else if(kind==='pip') addLayer({type:'pip',pos:arg,size:.36,deco:'grid',track:2,...(hs().cardDefault?{bgColor:hs().cardDefault.bgColor,accent:hs().cardDefault.accent,deco:hs().cardDefault.deco||'grid'}:{})});
    else if(kind==='collage'){ const im=(INFO.assets||[]).filter(a=>/\.png$/i.test(a)).concat((INFO.assets||[]).filter(a=>!/\.png$/i.test(a))).slice(0,3); if(!im.length){ toast(t('collageNeed')); return; } addLayer({type:'collage',items:im.map(a=>({src:'assets/'+a})),bgColor:'#E07A3F',track:2}); }
    else if(kind==='look') lookApply(arg);
    else if(kind==='grade'){ snap(); const h=hs(); if(arg==='none') delete h.grade; else h.grade={preset:arg,amount:(h.grade&&h.grade.amount)||1}; renderLeft(); live(); }
    else if(kind==='outro'){ if(ST.outro>0){ select({kind:'outro',id:0}); seek(Math.min(dur()-0.05,total()+1.6)); } else outroSet(3.5); }
    else if(kind==='cover') addLayer({type:'cover',text:t('coverDef'),bgColor:'#F3F2EE',font:'Noto Naskh Arabic',size:230,track:2});
    else if(kind==='split') addLayer({type:'split',style:arg,size:84,track:2,...(DF('card',arg)||DF('card','list')),...(hs().cardDefault||{})});
    else if(kind==='bg') addLayer({type:'bg',mode:arg,amount:.6,...(arg==='color'||arg==='grad'||arg==='studio'?{color:(ST.theme&&ST.theme.bg)||'#101014'}:{}),...(arg==='image'&&(INFO.assets||[])[0]?{src:'assets/'+INFO.assets[0]}:{})});
    else if(kind==='behind') addLayer({type:'behind',text:t('behindDef'),size:270,color:'#FFFFFF',font:hs().cap.font,anim:'rise'});
    else if(kind==='image') addLayer({type:'image',src:'assets/'+arg,x:.5,y:.35,w:.5,anim:'pop'});
    else if(kind==='broll'){ snap(); const n=(ST.studio.brNeed[arg]||[1,90])[1]; ST.studio.brollClips=ST.studio.brollClips||[]; const gs=(ST.studio.brKey||{})[arg], bc={k:arg,s:r3(T),e:r3(Math.min(total(),T+Math.min(4,n/30))),mode:'full'}; if(gs) bc.key={on:true,color:'auto'}; ST.studio.brollClips.push(bc); select({kind:'broll',id:ST.studio.brollClips.length-1}); await hard(); if(gs) toast(t('brKeyFound')); else { const w=F.contentWindow, g=w&&w.hsKeyGuess&&w.hsKeyGuess(arg); if(g){ (ST.studio.brKey=ST.studio.brKey||{})[arg]=g; bc.key={on:true,color:'auto'}; renderRight(); drawT(T); dirty(); toast(t('brKeyFound')); } } }
    return; }
  panelClick(e); });
function pickFile(kind){ const inp=$('#fileIn'); inp.value=''; inp.accept={font:'.ttf,.otf,.woff,.woff2',broll:'video/*',image:'image/*',char:'image/*',bgimg:'image/*',sound:'audio/*,.mp3,.wav,.m4a,.aac,.ogg,.flac'}[kind]; inp.multiple=kind==='sound'; inp.onchange=async()=>{ const f=inp.files[0]; if(!f) return;
    if(kind==='sound'){ toast(t('uploading')); let n=0; for(const g of [...inp.files]){ const r=await api('/hs/mysfx',g,{'X-Name':encodeURIComponent(g.name)}); if(r.ok){ n++; sfxSet(r.items); } else toast(srvEn(r.msg)||t('failed')); } renderLeft(); if(n) toast(t('myAdded',n)); return; }
    if(kind==='font'){ const r=await api('/hs/font',f,{'X-Name':encodeURIComponent(f.name)}); if(!r.ok){ toast(srvEn(r.msg)||t('failed')); return; } snap(); const h=hs(); if(!h.fonts.some(x=>x.file===r.file)) h.fonts.push({name:r.name,file:r.file}); const L=selLayer(); if(L&&L.type==='text') L.font=r.name; else h.cap.font=r.name; renderAll(); await live(); toast(t('fontAdded',r.name)); }
    else if(kind==='broll'){ await save(); const r=await api('/api/broll',f,{'X-Name':encodeURIComponent(f.name)}); if(!r.ok){ toast(t('busyJob')); return; } toast(t('uploading')); pollJob(()=>load(true)); }
    else { const r=await api('/hs/asset',f,{'X-Name':encodeURIComponent(f.name)}); if(!r.ok){ toast(srvEn(r.msg)||t('failed')); return; } INFO.assets=[...new Set([...(INFO.assets||[]),r.file])];
      if(kind==='bgimg'){ const L=selLayer(); if(L){ snap(); L.src=r.src; L.mode='image'; renderRight(); live(); } } else if(kind==='char') addLayer({type:'char',src:r.src,x:.2,y:.62,size:.3,anim:'pop',react:true}); else addLayer({type:'image',src:r.src,x:.5,y:.35,w:.5,anim:'pop'}); renderLeft(); } }; inp.click(); }

/* ───── اليمين ───── */
/* 4.44: الملاحظات صارت محادثة مع Claude: تكتب له (وتنربط بالثانية اللي واقف عندها)، وردوده وشغله يطلعون بنفس المحادثة */
const noteAt=n=>{ const m=String(n.at||'').match(/(\d+)-(\d+)-(\d+) (\d+):(\d+)/); return m?new Date(+m[1],+m[2]-1,+m[3],+m[4],+m[5]).getTime():0; };
function revHtml(){ const cm=(REV.comments||[]); return '<div class="sec"><h4>'+t('clientReview')+(REV.approved?'<span class="st ok">'+t('approvedBy',esc(REV.approved.by))+'</span>':'')+'</h4>'+(cm.length?cm.map(c=>'<div class="note"><div style="flex:1;min-width:0"><span class="t" style="direction:ltr;color:var(--mut);font-size:11px;cursor:pointer" data-seek="'+c.t+'">'+fmt(c.t)+'</span> <span class="st">'+esc(c.who)+'</span>'+(c.status==='promoted'?' <span class="st sent">'+t('promoted')+'</span>':'')+'<p dir="auto">'+esc(c.text)+'</p>'+(c.status==='open'?'<button class="sm" data-promote="'+c.id+'">'+t('promote')+'</button>':'')+'</div></div>').join(''):'<p class="hint">'+t('reviewEmpty')+'</p>')+'<div class="copy"><span style="direction:ltr;text-align:left">'+esc(INFO.review)+'</span><button class="sm" data-copy="'+esc(INFO.review)+'">'+t('copy')+'</button></div><p class="hint">'+t('reviewHint')+'</p></div>'; }   // 4.50: مراجعة العميل انتقلت لـ«انشر»
function chatItems(){ const L=[], t0=Math.min(...NOTES.map(noteAt).filter(Boolean),Date.now());
  NOTES.forEach(n=>{ const a=noteAt(n); if(n.by==='claude') L.push({c:1,at:a,n}); else { L.push({c:0,at:a,n}); if(n.reply) L.push({c:1,at:a+1,text:n.reply}); } });
  ACT.filter(e=>e.text&&e.kind!=='ask'&&e.t*1000>=t0-60000).slice(-60).forEach(e=>L.push({c:1,at:e.t*1000,text:e.text,kind:e.kind}));
  return L.sort((a,b)=>a.at-b.at); }
function chatThread(){ const L=chatItems(); if(!L.length) return '<p class="hint chat0">'+t('chatEmpty')+'</p>';
  return L.map(x=>{ if(x.n&&x.c) return '<div class="msg c">'+aiNote(x.n)+'</div>'; if(x.n){ const n=x.n;
      return '<div class="msg u"><div class="bub">'+(n.img?'<img src="/'+n.img+'?v='+n.id+'">':'')+'<p dir="auto">'+esc(n.text)+'</p>'+(n.audio?'<audio controls preload="none" src="/'+n.audio+'"></audio>':'')+'<div class="meta"><span class="t" data-seek="'+n.t+'">'+fmt(n.t)+'</span><span class="st '+n.status+'">'+t('ns_'+n.status)+'</span><button class="sm ghost" data-delnote="'+n.id+'">'+t('delete')+'</button></div></div></div>'; }
    return '<div class="msg c'+(x.kind==='err'?' err':'')+'"><div class="bub"><b>Claude</b><p dir="auto">'+esc(srvEn(x.text))+'</p>'+(x.at?'<time>'+new Date(x.at).toTimeString().slice(0,5)+'</time>':'')+'</div></div>'; }).join(''); }
function chatHtml(){ const run=!!(PULSE&&PULSE.agent&&PULSE.agent.running);
  return '<div class="sec chat"><div class="chatlog" id="chatLog">'+chatThread()+(run?'<div class="msg c"><div class="bub typing"><b>Claude</b><p>'+t('chatWorking')+'</p></div></div>':'')+'</div>'
    +'<div class="chatin"><textarea id="chatTx" rows="2" dir="auto" placeholder="'+esc(t('chatPh',fmt(T)))+'"></textarea><button class="pri" id="chatGo">'+t(INFO.claude?'chatSend':'chatSave')+'</button></div>'
    +(run?'<button class="sm ghost" id="agStop" style="margin-top:6px">'+t('stop')+'</button>':'')+'<p class="hint">'+t(INFO.claude?'chatHint':'chatHintNo')+'</p></div>'; }
function chatFeed(){ const lg=$('#chatLog'); if(!lg) return; const atEnd=lg.scrollTop+lg.clientHeight>=lg.scrollHeight-30; const run=!!(PULSE&&PULSE.agent&&PULSE.agent.running); lg.innerHTML=chatThread()+(run?'<div class="msg c"><div class="bub typing"><b>Claude</b><p>'+t('chatWorking')+'</p></div></div>':''); if(atEnd) lg.scrollTop=1e6; }
async function chatSend(){ const tx=$('#chatTx'); const v=(tx&&tx.value||'').trim(); if(!v){ toast(t('noteEmpty')); return; }
  if(INFO.claude&&!(await tokenGo('notes','mid'))) return; await save(); const ci=cardAt(T);
  const r=await api('/hs/note',{t:T,text:v,card:ci>=0?ci:null}); if(!r||!r.ok){ toast(t('failed')); return; } NOTES=r.notes; tx.value=''; buildTL();
  if(INFO.claude){ const s2=await api('/hs/notes_send',{run:true}); if(s2&&s2.notes) NOTES=s2.notes; if(s2&&!s2.started&&s2.msg) toast(srvEn(s2.msg)); }
  renderRight(); const lg=$('#chatLog'); if(lg) lg.scrollTop=1e6; }
document.addEventListener('click',e=>{ if(e.target.closest('#chatGo')) chatSend(); });
document.addEventListener('keydown',e=>{ if(e.target.id==='chatTx'&&e.key==='Enter'&&(e.ctrlKey||e.metaKey)){ e.preventDefault(); chatSend(); } });
function aiNote(n){ const w=n.status==='ask';
  return '<div class="note ai'+(w?' wait':'')+'"><div style="flex:1;min-width:0"><span class="t" style="direction:ltr;color:var(--mut);font-size:11px;cursor:pointer" data-seek="'+n.t+'">'+fmt(n.t)+'</span> <span class="st ai">Claude</span> <span class="st">'+t('aik_'+(n.kind||'suggest'))+'</span>'+(w?'':' <span class="st '+n.status+'">'+t('ns_'+n.status)+'</span>')+'<p dir="auto">'+esc(n.text)+'</p>'+(n.answer?'<p class="rep" dir="auto" style="color:var(--note)">'+t('aiYou')+esc(n.answer)+'</p>':'')+(n.reply?'<p class="rep" dir="auto">'+esc(n.reply)+'</p>':'')+(w&&n.kind==='fix'?'<div class="row" style="gap:6px;margin-top:6px"><button class="sm pri" data-fixgo="'+n.id+'">'+t('fixGo')+'</button><button class="sm" data-aians="'+n.id+'" data-v="fixed">'+t('fixDone')+'</button></div>':'')+(w&&n.kind!=='fix'?'<div class="row" style="gap:6px;margin-top:6px;flex-wrap:wrap">'+(n.kind==='question'?'':'<button class="sm pri" data-aians="'+n.id+'" data-v="yes">'+t('aiYes')+'</button><button class="sm" data-aians="'+n.id+'" data-v="no">'+t('aiNo')+'</button>')+'<input data-aitx="'+n.id+'" dir="auto" placeholder="'+esc(t('aiReplyPh'))+'" style="flex:1;min-width:120px"><button class="sm" data-aians="'+n.id+'" data-v="text">'+t('aiSend')+'</button></div>':'<button class="sm ghost" data-delnote="'+n.id+'">'+t('delete')+'</button>')+'</div></div>'; }
/* 4.48: إيموجي الكابشن: إيموجي فوق الكلمة لما تنقال (القاموس والرسم بـ ext.js، نفس الحساب بالتصدير) */
const EMO_PAL=['🔥','😂','😮','🤯','💡','✅','❌','⚠️','💰','📈','🚀','❤️','👀','🎯','⏰','🧠','👏','🎉'];
function emoPlanAll(){ try{ const w=F.contentWindow; return w&&w.__hsEmoji?w.__hsEmoji.planOf(ST.caps.cards,hs().emoji):[]; }catch(e){ return []; } }
function emoSec(h){ const E=h.emoji; let o='<div class="sec"><h4>'+t('emoT')+'</h4>'+tog('emoji.on',t('emoOn'),t('emoSub'),E.on);
  if(E.on){ const P=emoPlanAll();
    o+=tog('emoji.auto',t('emoAutoT'),t('emoAutoSub'),E.auto!==false)+seg(t('emoPos'),'emoji.pos',[['word',t('emoPosWord')],['center',t('emoPosCenter')]],E.pos)+seg(t('emoAnim'),'emoji.anim',[['pop',t('emoAnimPop')],['bounce',t('emoAnimBounce')],['float',t('emoAnimFloat')]],E.anim)
      +(E.auto!==false?seg(t('emoOnly'),'emoji.only',[['all',t('emoOnlyAll')],['hot',t('emoOnlyHot')]],E.only)+slider(t('emoGap'),'emoji.gap',0,8,E.gap,0.5):'')+slider(t('size'),'emoji.size',48,180,E.size,2);
    o+='<p class="hint">'+t('emoCount',P.length)+'</p>'+(P.length?'<div class="bll emol">'+P.map(x=>'<div class="row"><span class="t" data-seek="'+r3(Math.max(0,x.s-0.3))+'">'+fmt(x.s)+'</span><button class="sm emob" data-emocard="'+x.ci+'" title="'+esc(t('emoChange'))+'">'+x.em+'</button><span dir="rtl" class="blt">'+esc(x.t)+'</span><button class="sm ghost" data-emorm="'+x.ci+'">'+t('delete')+'</button></div>').join('')+'</div>':'')+'<p class="hint">'+t('emoHint')+'</p>'; }
  return o+'</div>'; }
function emoCardSec(i,c){ const E=hs().emoji, k=key(c), has=Object.prototype.hasOwnProperty.call(E.set,k), cur=has?String(E.set[k]||''):null, it=E.on?emoPlanAll().find(x=>x.ci===i):null;
  return '<div class="sec"><h4>'+t('emoCard')+'</h4>'+(E.on?'':'<p class="hint">'+t('emoOffHint')+'</p>')
    +'<div class="row"><button class="sm'+(!has?' on':'')+'" data-emoset="auto">'+t('emoAuto')+(it&&it.by==='auto'?' '+it.em:'')+'</button><button class="sm'+(has&&!cur?' on':'')+'" data-emoset="-">'+t('emoNone')+'</button></div>'
    +'<div class="emopal">'+EMO_PAL.map(e=>'<button class="sm'+(cur===e?' on':'')+'" data-emoset="'+e+'">'+e+'</button>').join('')+'</div>'
    +'<div class="row"><input type="text" id="emoTx" dir="ltr" maxlength="16" placeholder="'+esc(t('emoPh'))+'" value="'+esc(cur&&!EMO_PAL.includes(cur)?cur:'')+'"><button class="sm" id="emoGo">'+t('emoUse')+'</button></div></div>'; }
function emoSet(v){ if(!SEL||SEL.kind!=='cap') return; const c=ST.caps.cards[+SEL.id]; if(!c) return; snap(); const E=hs().emoji, k=key(c);
  if(v==='auto') delete E.set[k]; else E.set[k]=v==='-'?'':v;
  if(v!=='auto'&&v!=='-'&&!E.on){ E.on=true; E.auto=false; toast(t('emoOnlyYours')); } renderRight(); live(); }
function renderRight(){ if(RTAB==='notes') RTAB='claude'; const B=$('#body'), h=hs(); let o='';
  if(RTAB==='sel') o=inspector();
  else if(RTAB==='plan') o=planPanel();
  else if(RTAB==='cap'){ fontLink(); h.fonts.forEach(localFace); const c=h.cap;
    o+=tog('cap.on',t('capFull'),t('capFullSub'),c.on);
    if(!c.on){ o+='<div class="sec"><h4>'+t('engineStyle')+'</h4><select id="capStyle">'+['card','shadow','big','underline','bar','type'].map(k=>'<option value="'+k+'"'+((ST.theme.capStyle||'card')===k?' selected':'')+'>'+t('cs_'+k)+'</option>').join('')+'</select><p class="hint">'+t('capOffHint')+'</p></div>'; }
    else { const sz=INFO.safe; if(sz&&(c.y>sz.capMax+0.01||c.y<sz.capMin-12)) o+='<div class="warnbox">'+t('capSafeWarn',sz.capMin,sz.capMax)+'</div>';
      o+=tplSec(h);   // 4.27: قوالب الكابشن مع الاسم
      o+='<div class="sec"><h4>'+t('capPresets')+'</h4><div class="grid3">'+Object.keys(CAPPRE).map(preTile).join('')+'</div></div>';
      o+='<div class="sec"><h4>'+t('font')+'<button class="sm" data-up="font">'+t('addFont')+'</button></h4><div class="fonts">'+[...h.fonts.map(f=>f.name),...AR_FONTS].map(f=>'<div class="fcard'+(c.font===f?' on':'')+'" data-font="'+esc(f)+'"><b style="font-family:\''+f+'\'">متابعة</b><span>'+esc(f)+'</span></div>').join('')+'</div></div>';
      o+='<div class="sec"><h4>'+t('look')+'</h4>'+pick(t('weight'),'cap.weight',weightsOf(c.font).map(w=>[w,t('w_'+w)]),c.weight)+slider(t('size'),'cap.size',34,150,c.size)+swatches(t('textColor'),'cap.color',c.color)+swatches(t('activeColor'),'cap.active',c.active)
        +seg(t('background'),'cap.bg',[['none',t('bgNone')],['box',t('bgBox')],['lines',t('bgLines')],['bar',t('bgBar')],['glass',t('fr_glass')],['pill',t('bgWord')]],c.bg)+(c.bg==='box'||c.bg==='bar'||c.bg==='lines'?swatches(t('cardColor'),'cap.bgColor',c.bgColor)+slider(t('cardOpacity'),'cap.bgOpacity',0.1,1,c.bgOpacity,0.05):'')
        +slider(t('stroke'),'cap.stroke',0,12,c.stroke)+(c.stroke>0?swatches(t('strokeColor'),'cap.strokeColor',c.strokeColor):'')+seg(t('shadow'),'cap.shadow',[[true,t('yes')],[false,t('no')],['hard',t('shadowHard')]],c.shadow)+(c.shadow==='hard'?swatches(t('shadowColor'),'cap.shadowColor',c.shadowColor):'')
        +seg(t('hlMode'),'cap.hl',[['color',t('hlColor')],['under',t('hlUnder')],['dim',t('hlDim')],['glow',t('hlGlow')],['marker',t('hlMarker')]],c.hl)+seg(t('fillMode'),'cap.fill',[['solid',t('fillSolid')],['outline',t('fillOutline')]],c.fill)+slider(t('actScale'),'cap.actScale',1,1.5,c.actScale,0.02)+'</div>';
      o+='<div class="sec"><h4>'+t('entrance')+'</h4><div class="seg">'+ENTERS.map(k=>'<button data-k="cap.enter" data-v="'+k+'" class="'+(c.enter===k?'on':'')+'" style="flex:1 1 22%"><span class="fxn fxi-'+k+'">'+t('en_'+k)+'</span></button>').join('')+'</div><h4 style="margin-top:12px">'+t('exitLbl')+'</h4><div class="seg">'+EXITS.map(k=>'<button data-k="cap.exit" data-v="'+k+'" class="'+((c.exit||'auto')===k?'on':'')+'" style="flex:1 1 18%"><span class="fxn fxo-'+k+'">'+t('ex_'+k)+'</span></button>').join('')+'</div><p class="hint">'+t('exitHint')+'</p>'+seg(t('display'),'cap.chunk',[[0,t('modeLine')],[1,t('chunk1')],[2,t('chunk2')],[3,t('chunk3')],[4,t('chunk4')]],c.mode==='word'?1:c.chunk).replace('class="row"','class="row" style="margin-top:9px"')+'</div>';
      o+='<div class="sec"><h4>'+t('position')+'</h4>'+slider(t('position'),'cap.y',15,92,c.y,0.5)+slider(t('lineWidth'),'cap.width',380,980,c.width,10)+seg(t('lines'),'cap.lines',[[1,'1'],[2,'2'],[3,'3']],c.lines)+seg(t('wpl'),'cap.wpl',[[0,t('wplAuto')],[3,'3'],[4,'4'],[5,'5'],[6,'6']],c.wpl==null?5:c.wpl)+'<p class="hint">'+t('capFaceHint')+'</p></div>'; o+=emoSec(h); } }
  else if(RTAB==='tr'){ const e=h.en, cards=ST.caps.cards, miss=cards.filter(c=>!e.map[key(c)]).length;
    o+=tog('en.on',t('trTitle'),t('trSub'),e.on);
    if(miss) o+='<div class="warnbox">'+t('trMissing',miss)+'<div style="margin-top:7px"><button class="sm" id="askTr">'+t('trAsk')+'</button></div></div>';
    o+='<div class="sec"><h4>'+t('trLook')+'</h4>'+pick(t('font'),'en.font',[...EN_FONTS,...AR_FONTS.slice(0,3)],e.font)+slider(t('size'),'en.size',22,110,e.size)+swatches(t('color'),'en.color',e.color)+seg(t('position'),'en.pos',[['below',t('below')],['above',t('above')]],e.pos)+'<div class="row"><label></label><button class="sm" id="matchSize">'+t('matchSize')+'</button></div></div>';
    o+='<div class="sec"><h4>'+t('sentences')+'</h4>'+cards.map((c,i)=>'<div class="card" data-card="'+i+'"><span class="t" data-seek="'+c.s+'">'+fmt(c.s)+'</span><div class="ar" dir="rtl">'+esc(key(c))+'</div><textarea dir="ltr" data-en="'+i+'" rows="1" placeholder="English">'+esc(e.map[key(c)]||'')+'</textarea></div>').join('')+'</div>'; }
  else if(RTAB==='audio'){ o+=dubSec(); const m=h.mix, sf=ST.studio.sfx||{}, types=Object.keys(sf).filter(k=>Array.isArray(sf[k])&&sf[k].length);
    o+='<div class="sec"><h4>'+t('voice')+'</h4>'+slider(t('level'),'mix.voice',0,2,m.voice,0.05)+svBlock(m)+'<div class="row"><label>'+t('voiceFx')+'</label><select data-k="mix.voiceFx">'+['','clarity','deboom','demud','soft','radio','phone'].map(k=>'<option value="'+k+'"'+((m.voiceFx||'')===k?' selected':'')+'>'+t('vfx_'+(k||'none'))+'</option>').join('')+'</select></div><p class="hint" style="margin-top:-2px">'+t('voiceFxHint')+'</p>'+slider(t('duck'),'mix.duck',0.15,1,m.duck==null?0.45:m.duck,0.05)+'<p class="hint" style="margin-top:-2px">'+t('duckHint')+'</p></div>';
    { const B=h.bleep; o+='<div class="sec"><h4>'+t('blTitle')+(B.items.length?'<button class="sm" id="blClr">'+t('blClear')+'</button>':'')+'</h4><div class="row"><input type="text" id="blTx" dir="auto" placeholder="'+esc(t('blPh'))+'"><button class="sm" id="blGo">'+t('blGo')+'</button></div>'
      +seg(t('blSound'),'bleep.mode',[['beep',t('blBeep')],['mute',t('blMute')]],B.mode)+(B.mode==='mute'?'':slider(t('blTone'),'bleep.tone',400,2000,B.tone||1000,50))
      +seg(t('blCap'),'bleep.cap',[['stars',t('blStars')],['hide',t('blHide')],['keep',t('blKeep')]],B.cap)
      +(B.items.length?'<div class="bll">'+B.items.map((x,i)=>'<div class="row"><span class="t" data-seek="'+r3(Math.max(0,x.s-0.8))+'">'+fmt(x.s)+'</span><span dir="rtl" class="blt">'+esc(x.t||t('blRange'))+'</span><button class="sm ghost" data-blrm="'+i+'">'+t('delete')+'</button></div>').join('')+'</div>':'<p class="hint">'+t('blNone')+'</p>')
      +'<p class="hint">'+t('blHint')+'</p></div>'; }
    o+='<div class="sec"><h4>'+t('sfxLevels')+'</h4>'+(types.length?'<p class="hint">'+t('sfxClickHint')+'</p>'+types.map(k=>slider(t('sfx_'+k),'mix.sfx.'+k,0,2,m.sfx[k]==null?1:m.sfx[k],0.05)).join(''):'<p class="hint">'+t('noSfx')+'</p>')+'</div>';
    o+='<div class="sec"><h4>'+t('bgAudio')+'</h4>'+slider(t('level'),'mix.bg',0,1,m.bg,0.02)+slider(t('bgFadeIn'),'mix.bgIn',0,6,m.bgIn==null?1:m.bgIn,0.1)+slider(t('bgFadeOut'),'mix.bgOut',0,6,m.bgOut==null?1.4:m.bgOut,0.1)+'<p class="hint">'+t('bgAudioHint')+' '+t('bgFadeHint')+'</p></div><p class="hint">'+t('audioHint')+'</p>'; }
  else if(RTAB==='check'){ const c=CHECK; if(!c){ o='<p class="hint">…</p>'; } else {
      const rq=c.reqs||[]; if(rq.length){ const nd=rq.filter(r=>r.ok).length;
        o+='<div class="sec"><h4>'+t('reqTitle')+' <span class="st '+(nd===rq.length?'ok':'bad')+'" style="direction:ltr;display:inline-block">'+nd+' / '+rq.length+'</span></h4><p class="hint">'+t('reqHint')+'</p>'+rq.map(r=>'<div class="item req'+(r.ok?' ok':'')+'"><span class="st '+(r.ok?'ok':'bad')+'" style="flex:none">'+(r.ok?'✓':'□')+'</span><span style="flex:1;min-width:0"><b dir="auto">'+esc(srvEn(r.label))+'</b>'+(r.why&&(!r.ok||r.man)?'<br><small dir="auto" style="color:var(--mut)">'+(r.man&&r.ok?t('reqBy'):'')+esc(r.why)+'</small>':'')+'</span></div>').join('')+'</div>'; }
      o+=retHtml()||('<div class="sec" style="display:flex;align-items:flex-end;gap:12px"><div class="score" style="color:'+(c.score>=80?'var(--au)':c.score>=55?'var(--warn)':'var(--bad)')+'">'+c.score+'</div><div class="hint" style="margin:0">'+t('checkScore')+'</div></div>');
      o+='<div class="sec"><h4>'+t('chkRetention')+'</h4>'+slider(t('chkGap'),'check.gap',1.5,5,h.check.gap,0.1);
      if(c.firstCap!=null&&c.firstCap>1) o+='<div class="item" data-seek="0"><span class="st bad">'+t('chkFirst',c.firstCap.toFixed(1))+'</span></div>';
      o+=c.gaps.map(g=>'<div class="item" data-seek="'+g.s+'"><span>'+t('chkGapItem',g.d.toFixed(1))+'</span><span class="st" style="flex:none;direction:ltr">'+fmt(g.s)+'</span></div>').join('')+c.longCaps.map(l=>'<div class="item" data-seek="'+ST.caps.cards[l.card].s+'"><span>'+t('chkLong',l.card+1,l.n)+'</span></div>').join('');
      if(!c.gaps.length&&!c.longCaps.length&&!(c.firstCap>1)) o+='<p class="hint">'+t('chkClean')+'</p>'; else o+='<p class="hint">'+t('chkGapHint')+'</p>';
      o+='</div>'; o+=check410(c); o+=stabChk(c); o+=hdrChk(c); { const om=(c.open&&c.open.miss)||[], ln=c.len||[];
        o+='<div class="sec"><h4>'+t('chkOpen')+'</h4>'+(om.length?om.map(k=>'<div class="item" data-seek="0"><span>'+t('chkOpen_'+k)+'</span></div>').join('')+'<p class="hint">'+t('chkOpenHint')+'</p>':'<p class="hint">'+t('chkOpenOk')+'</p>')+'</div>';
        if(ln.length) o+='<div class="sec"><h4>'+t('chkLen')+'</h4>'+ln.map(l=>'<div class="item"><span'+(l.k==='over'?' class="st bad"':'')+'>'+(l.k==='over'?t('chkLen_over',t('b_'+l.p),l.max,Math.round(c.total)):t('chkLen_'+l.k,t('b_'+l.p),l.lo,l.hi,Math.round(c.total)))+'</span></div>').join('')+'</div>'; }
      o+='<div class="sec" id="chkFil"><h4>'+t('chkFillers')+'</h4>'+(c.fillers.length?c.fillers.map((f,i)=>'<label class="item"><input type="checkbox" data-fil="'+f.card+':'+f.idx+'" checked><span dir="rtl">«'+esc(f.t)+'» · '+esc(key(ST.caps.cards[f.card]).slice(0,34))+'</span><span class="st" style="flex:none;direction:ltr" data-seek="'+f.s+'">'+fmt(f.s)+'</span></label>').join(''):'<p class="hint">'+t('chkNoFillers')+'</p>')+'</div>';
      o+=takesHtml(c);
      if(c.fillers.length||c.dupes.length) o+='<button class="pri" id="doClean" style="width:100%">'+t('chkRemove')+'</button><p class="hint">'+t('chkRemoveHint')+'</p>'; } }
  else if(RTAB==='claude'){ o+=askCtxHtml(); o+=agHtml();
    o+='<div class="sec"><h4>'+t('stagesTitle')+'</h4><div class="stages" id="pStages"></div></div>'; }
  else if(RTAB==='proj'){
    o+=vposSec();   // 4.27: مكان الفيديو بالكادر
    o+=barSec(h);   // 4.29: شريط التقدّم
    o+=proSec(h);   // 4.44: أدوات احترافية
    o+=qualitySec(h);
    o+=hdrSec(h);   // 4.41: ألوان الآيفون (HDR)
    o+=stabSec(h);   // 4.40: تثبيت الصورة
    o+=styleSec(h);
    o+='<div class="sec"><h4>'+t('exportTitle')+'</h4><label class="item"><input type="checkbox" id="exHooks"'+(h.hooks.on&&h.hooks.items.filter(x=>x&&x.text).length>1?'':' disabled')+'><span>'+t('exHooks')+'</span></label><div class="row"><button class="pri" id="doRender" style="flex:1">'+t('exportFinal')+'</button><button id="doClean2">'+t('exportClean')+'</button></div><div id="dl">'+(INFO.finals||[]).map(f=>'<div class="item" style="cursor:default"><span><a href="/'+f+'?v='+Date.now()+'" download>'+t('download')+' '+f+'</a></span><button class="sm" data-phone="'+f+'">'+t('toPhone')+'</button></div>').join('')+'</div><div id="log" style="margin-top:8px;display:none"></div></div>';
    o+='<div class="sec"><h4>'+t('packTitle')+'</h4><textarea id="postTx" rows="4" dir="auto" placeholder="'+t('postPh')+'">'+esc(INFO.post||'')+'</textarea><div class="row" style="margin-top:8px"><button id="doPack">'+t('packBuild')+'</button><button class="sm ghost" id="askPost">'+t('askPost')+'</button></div><div id="packOut"></div></div>';
    { const fr=h.frame||{ar:'9:16'}, pl=h.platforms||[], sz=INFO.safe||{};
      o+='<div class="sec"><h4>'+t('frameTitle')+'</h4><div class="seg" style="margin-bottom:8px">'+FRAMES.map(f=>'<button data-frame="'+f+'" class="'+((fr.ar||'9:16')===f?'on':'')+'">'+f+'</button>').join('')+'</div><div class="chips" style="margin-bottom:8px">'+PLATS.map(k=>'<button data-plat="'+k+'" class="'+(pl.includes(k)?'on':'')+'">'+t('b_'+k)+'</button>').join('')+'</div>'
        +(fr.ar==='4:5'||fr.ar==='1:1'?slider(t('frameCy'),'frame.cy',0.3,0.7,fr.cy==null?0.47:fr.cy,0.01):'')+'<p class="hint">'+t('fh_'+(fr.ar||'9:16').replace(':','x'))+' '+(sz.capMax?t('frameSafe',sz.capMin,sz.capMax):'')+'</p>'
        +pl.map(k=>'<p class="hint" style="margin-top:4px"><b>'+t('b_'+k)+'</b>: '+t('pf_'+k)+'</p>').join('')+'</div>'; }
    o+='<div class="sec"><h4>'+t('compareTitle')+'</h4>'+((INFO.exports||[]).length>1?'<div class="row"><select id="cmpA">'+INFO.exports.map((x,i)=>'<option'+(i===1?' selected':'')+'>'+x+'</option>').join('')+'</select><select id="cmpB">'+INFO.exports.map(x=>'<option>'+x+'</option>').join('')+'</select><button class="sm" id="doCmp">'+t('compare')+'</button></div>':'<p class="hint">'+t('compareEmpty')+'</p>')+'</div>';
    o+='<div class="sec"><h4>'+t('brand')+'</h4><div class="row"><select id="brandSel"><option value="">'+t('brandPick')+'</option>'+INFO.brands.map(b=>'<option>'+esc(b)+'</option>').join('')+'</select><button class="sm" id="brandApply">'+t('apply')+'</button></div><div class="row"><input type="text" id="brandName" placeholder="'+t('brandPh')+'"><button class="sm" id="brandSave">'+t('saveCurrent')+'</button></div></div>';
    o+='<div class="sec"><h4>'+t('privTitle')+'</h4><p class="hint" style="margin-top:0">'+t('privHint')+'</p><button class="sm" id="privShow">'+t('privShow')+'</button></div>';
    o+='<div class="sec"><h4>'+t('versions')+'</h4><div class="row"><input type="text" id="verName" placeholder="'+t('verPh')+'"><button class="sm" id="verSave">'+t('saveVersion')+'</button></div>'+(INFO.versions.length?INFO.versions.slice(0,8).map(v=>'<div class="item" style="cursor:default"><span>'+esc(v.name)+' <small style="color:var(--mut)">'+esc(v.at)+'</small></span><button class="sm ghost" data-ver="'+v.id+'">'+t('restore')+'</button></div>').join(''):'<p class="hint">'+t('verHint')+'</p>')+'</div>'; }
  else if(RTAB==='pub'){ o+=pubHtml(); o+=revHtml(); if(!PUB.cov&&!PUB._ld){ PUB._ld=1; loadPub(); } }
  B.innerHTML=o; if(['cap','audio','proj','tr'].includes(RTAB)) secTabs(B,'R:'+RTAB); if(RTAB==='claude') renderFeed(); if(RTAB==='pub') setTimeout(drawPub,0); }
/* 4.2: لوحة الأسلوب: كل شي بالدحيح والورق المتحرك يتعدّل من هنا */
const DCAP={on:true,font:'Cairo',weight:800,size:34,color:'#FFFFFF',active:'#FFFFFF',bg:'box',bgColor:'#E8541E',bgOpacity:1,y:63.2,x:71,width:440,lines:1,chunk:4,shadow:false,stroke:0,enter:'pop'};
const DKBG=['paper','navy','original','orange','green','dark'];
const dkStageK=()=>{ const D=hs().dahih||{}; return D.on&&D.layout!=='full'?{y0:660/1920,h:608/1920}:{y0:0,h:1}; };
function styleSec(h){ if(!h.kin) h.kin={}; if(!h.dahih) h.dahih={}; const D=h.dahih||{}, K=h.kin||{}, ON=!!D.on, A=[['',t('bgNone')],...(INFO.assets||[]).map(a=>['assets/'+a,a])], FF=[...h.fonts.map(f=>f.name),...AR_FONTS];
  const ti=(k,v,ph)=>'<div class="row"><label>'+ph+'</label><input type="text" data-k="'+k+'" dir="auto" value="'+esc(v||'')+'"></div>';
  let o='<div class="sec"><h4>'+t('stTitle')+'</h4><p class="hint" style="margin-top:0">'+t('stHint')+'</p><div class="row" style="flex-wrap:wrap;gap:6px"><button class="'+(ON?'':'pri')+'" id="dkToggle">'+t(ON?'stDahihOff':'stDahihOn')+'</button><button id="addKin">'+t('stAddKin')+'</button><button id="addDesk">'+t('stAddDesk')+'</button></div>';
  if(ON){ o+='<h4>'+t('b_dahih')+'</h4>'+ti('dahih.title',D.title,t('stTitleTx'))+ti('dahih.tag',D.tag,t('stTag'))
      +pick(t('stAvatar'),'dahih.avatar',A,D.avatar||'')+pick(t('stLogo'),'dahih.logo',[['',t('bgNone')],['claude','Claude'],...(INFO.assets||[]).map(a=>['assets/'+a,a])],D.logo||'')
      +seg(t('stLayout'),'dahih.layout',[['window',t('stWindow')],['full',t('stFull')]],D.layout||'window')+seg(t('stSide'),'dahih.side',[['right',t('dir_right')],['left',t('dir_left')]],D.side||'right')
      +slider(t('stZoom'),'dahih.zoom',0.4,1,D.zoom||0.74,0.02)+pick(t('font'),'dahih.font',FF,D.font||'Cairo')+pick(t('stNumFont'),'dahih.numFont',[['',t('stSame')],...FF.map(f=>[f,f]),['Playfair Display','Playfair Display']],D.numFont||'')
      +seg(t('stTc'),'dahih.tc',[[true,t('yes')],[false,t('no')]],D.tc!==false)
      +pick(t('stBg0'),'dahih.bg',DKBG.map(m=>[m,t('dkbg_'+m)]),D.bg||'paper')
      +'<h4>'+t('stBgs')+'</h4>'+(D.bgs||[]).map((b,i)=>'<div class="row"><input type="number" step="0.1" data-dkbs="'+i+'" value="'+b.s+'" style="max-width:90px"><select data-dkbm="'+i+'">'+DKBG.map(m=>'<option value="'+m+'"'+(b.mode===m?' selected':'')+'>'+esc(t('dkbg_'+m))+'</option>').join('')+'</select><button class="sm" data-dkbd="'+i+'">'+t('delete')+'</button></div>').join('')
      +'<div class="row"><button class="sm" id="dkBgAdd">'+t('stBgAdd')+'</button></div>'
      +'<h4>'+t('cap')+'</h4><div class="row"><button class="sm" id="dkCap">'+t('stCapReset')+'</button></div>'; }
  if(h.pod&&h.pod.on){ const P=h.pod; o+='<h4>'+t('b_podcast')+'</h4>'+ti('pod.title',P.title,t('stTitleTx'))+ti('pod.credit',P.credit,t('podCredit'))
      +slider(t('podTSize'),'pod.tsize',32,80,P.tsize||52,1)+slider(t('podTY'),'pod.ty',4,30,P.ty||12,0.5)
      +seg(t('podLang'),'pod.lang',[['en',LANG==='en'?'Arabic → English':'English ← عربي'],['ar',LANG==='en'?'Arabic':'عربي']],P.lang||'en')+seg(t('podOrig'),'pod.orig',[[true,t('yes')],[false,t('no')]],P.orig!==false)
      +slider(t('podSub'),'pod.subScale',0.4,0.9,P.subScale||0.62,0.02)+seg(t('podBar'),'pod.bar',[[true,t('yes')],[false,t('no')]],!!P.bar)
      +'<p class="hint">'+t('podHint')+'</p>'; }
  o+='<h4>'+t('b_paper')+'</h4>'+ti('kin.mark',K.mark,t('stMark'))+pick(t('stAvatar'),'kin.avatar',A,K.avatar||'')+pick(t('font'),'kin.font',FF,K.font||'Cairo')+'</div>';
  return o; }
function styleClick(el){ const h=hs(), d=el.dataset;
  if(el.id==='dkToggle'){ snap(); const D=h.dahih=h.dahih||{}; if(D.on){ D.on=false; } else { Object.assign(D,{on:true,layout:D.layout||'window',bg:D.bg||'paper',bgs:D.bgs||[]}); h.cap={...h.cap,...DCAP}; toast(t('visMask')); } live(); renderRight(); return true; }
  if(el.id==='addKin'){ addLayer({type:'kinetic',text:t('stKinSample'),deco:'none',track:2}); return true; }
  if(el.id==='addDesk'){ addLayer({type:'desk',kind:'note',text:t('stDeskSample'),x:0.3,y:0.42,track:1}); return true; }
  if(el.id==='dkBgAdd'){ snap(); const D=h.dahih; D.bgs=(D.bgs||[]).concat([{s:r3(T),mode:'navy'}]).sort((a,b)=>a.s-b.s); live(); renderRight(); return true; }
  if(d.dkbd!==undefined){ snap(); h.dahih.bgs.splice(+d.dkbd,1); live(); renderRight(); return true; }
  if(el.id==='dkCap'){ snap(); h.cap={...h.cap,...DCAP,...(h.dahih&&h.dahih.layout==='full'?{y:70,x:50,size:52,width:760}:h.dahih&&h.dahih.side==='left'?{x:29}:{})}; live(); toast(t('saved')); return true; }
  return false; }
function inspector(){ const h=hs(); if(!SEL) return '<p class="hint">'+t('selNone')+'</p>'; if(SEL.kind==='vxf') return vxfPanel();
  if(SEL.kind==='hook') return hookInspector();
  if(SEL.kind==='layer'){ const L=selLayer(); if(!L) return ''; let o='<div class="sec"><h4>'+t('type_'+L.type)+'<span><button class="sm" id="lDup">'+t('duplicate')+'</button> <button class="sm" id="lDel">'+t('delete')+'</button></span></h4>';
    o+='<div class="tog"><div>'+t('pinLayer')+'<small>'+t('pinLayerSub')+'</small></div><div class="sw-t'+(layerPinned(L)?' on':'')+'" id="lPin"></div></div>';
    o+='<div class="row"><label>'+t('timing')+'</label><input type="number" step="0.05" data-k="L.s" value="'+L.s+'" title="'+esc(t('tStart'))+'"><input type="number" step="0.05" data-k="L.e" value="'+L.e+'" title="'+esc(t('tEnd'))+'"></div><div class="row"><label></label><button class="sm ghost" data-tset="s">'+t('tFromHere')+'</button><button class="sm ghost" data-tset="e">'+t('tToHere')+'</button></div>';
    if(h.layers.filter(x=>x.type===L.type).length>1) o+=scopeRow();
    if(L.type==='text'){ o+='<textarea data-k="L.text" rows="2" dir="auto" style="margin-bottom:9px">'+esc(L.text)+'</textarea>'+pick(t('font'),'L.font',allFonts(),L.font||h.cap.font)+slider(t('size'),'L.size',30,220,L.size||96)+swatches(t('textColor'),'L.color',L.color)
        +seg(t('background'),'L.bg',[['none',t('bgNone')],['box',t('bgBox')],['pill',t('bgPill')],['glass',t('fr_glass')]],L.bg||'none')+(L.bg&&L.bg!=='none'?swatches(t('cardColor'),'L.bgColor',L.bgColor||'#000000')+slider(t('cardOpacity'),'L.bgOpacity',0.1,1,L.bgOpacity==null?1:L.bgOpacity,0.05):'')+slider(t('stroke'),'L.stroke',0,14,L.stroke||0)+slider(t('lineWidth'),'L.width',300,1040,L.width||900,10); }
    if(L.type==='char'){ if(!L.src) o+=pick(t('character'),'L.char',CHARS.map(c=>[c,t('char_'+c)]),L.char)+swatches(t('color'),'L.color',L.color)+swatches(t('accent'),'L.accent',L.accent||'#F2B33D');
      o+=slider(t('size'),'L.size',0.08,0.8,L.size||0.26,0.01)+seg(t('react'),'L.react',[[true,t('yes')],[false,t('no')]],L.react!==false)+seg(t('flip'),'L.flip',[[false,t('no')],[true,t('yes')]],!!L.flip); }
    if(L.type==='image'&&(!L.fit||L.fit==='free')) o+=seg(t('frame'),'L.frame',[['',t('bgNone')],['glass',t('fr_glass')],['ring',t('fr_ring')],['browser',t('fr_browser')],['post',t('fr_post')]],L.frame||'')+(L.frame==='browser'?'<input type="text" data-k="L.url" dir="ltr" value="'+esc(L.url||'')+'" placeholder="example.com" style="margin-bottom:9px">':'')+(L.frame==='post'?'<input type="text" data-k="L.handle" dir="ltr" value="'+esc(L.handle||'')+'" placeholder="@handle" style="margin-bottom:6px"><input type="text" data-k="L.caption" dir="auto" value="'+esc(L.caption||'')+'" placeholder="'+esc(t('postCapPh'))+'" style="margin-bottom:9px">':'')+(L.frame==='ring'?swatches(t('color'),'L.ringColor',L.ringColor||'#FFFFFF')+seg(t('ringFull'),'L.ringFull',[[false,t('ringSpin')],[true,t('ringDone')]],!!L.ringFull):'');
    if(L.type==='image') o+='<div class="sec" style="padding:0;border:0;margin:0 0 9px"><h4 style="margin:0 0 6px">'+t('rbTitle')+'</h4><div class="row2"><button class="sm" data-rmbg="auto">'+t('rbAuto')+'</button><button class="sm" data-rmbg="claude">'+t('rbClaude')+'</button></div>'+(L.srcOrig?'<button class="sm ghost" data-rmbg="undo" style="margin-top:6px">'+t('rbUndo')+'</button>':'')+'<p class="hint">'+t('rbHint')+'</p></div>';
    if(L.type==='image') o+=seg(t('display'),'L.fit',[['free',t('fitFree')],['card',t('fitCard')],['cover',t('fitCover')]],L.fit||'free')+(L.fit==='cover'?'':slider(t('size'),'L.w',0.08,1.2,L.w||(L.fit==='card'?0.76:0.5),0.01)+slider(t('round'),'L.round',0,200,L.round==null?(L.fit==='card'?36:0):L.round,2)); if(L.type==='image') o+=imgMoveInsp(L);
    if(L.type==='anno') o+=annoInsp(L);
    if(L.type==='viz'){ const kx=(lbl,key,val,ph)=>'<div class="row"><label>'+lbl+'</label><input type="text" data-kx="'+key+'" dir="auto" value="'+esc(val)+'" placeholder="'+esc(ph||'')+'"></div>', pt=p=>p?[p.name||'',p.lat,p.lon].join(', '):'';
      if(VIZK.includes(L.kind)) o+='<p class="hint">'+t('vh_'+L.kind)+'</p>';
      if(L.kind!=='cta') o+=seg(t('vLayout'),'L.layout',[['stage',t('vl_stage')],['split',t('vl_split')],['over',t('vl_over')],['full',t('vl_full')]],L.layout||'stage')+'<input type="text" data-k="L.title" dir="auto" value="'+esc(L.title||'')+'" placeholder="'+esc(t('vTitlePh'))+'" style="margin-bottom:9px">';
      if(L.kind==='pctdots') o+=kx(t('vValues'),'values',(L.values||[L.value||60]).join(', '),'60, 86, 31')+kx(t('vUnit'),'unit',L.unit==null?'%':L.unit,'%');
      if(L.kind==='people'||L.kind==='fill') o+=slider(t('vValue'),'L.value',0,100,L.value==null?70:L.value);
      if(L.kind==='bars') o+=(L.items||[]).map((b,i)=>'<div class="row"><input type="text" dir="auto" data-bar="'+i+':label" value="'+esc(b.label)+'" placeholder="'+esc(t('vName'))+'"><input type="number" data-bar="'+i+':value" value="'+esc(b.value)+'" style="max-width:104px;flex:none"><button class="sm ghost" data-brm="'+i+'" style="flex:none">×</button></div>').join('')+((L.items||[]).length<6?'<div class="row"><label></label><button class="sm" id="barAdd">'+t('vAddRow')+'</button></div>':'')+kx(t('vUnit'),'unit',L.unit||'','م');
      if(L.kind==='route') o+=['from','to'].map(k=>'<div class="row"><label>'+t(k==='from'?'vFrom':'vTo')+'</label><input type="text" dir="auto" list="hsCities" data-city="'+k+'" value="'+esc((L[k]||{}).name||'')+'" placeholder="'+esc(t('vCityPh'))+'"></div>').join('')+'<p class="hint" style="margin-top:-4px">'+t('vCityHint')+'</p>'+kx(t('vTime'),'time',L.time||'',LANG==='en'?'5 hours':'5 ساعات')+kx(t('vKm'),'km',L.km||'',t('vKmPh'))+seg(t('vMode'),'L.mode',[['plane',t('vPlane')],['car',t('vCar')]],L.mode||'plane');
      if(L.kind==='cta') o+=kx(t('vPre'),'pre',L.pre||'')+kx(t('vWord'),'word',L.word||'')+kx(t('vPost'),'post',L.post||'');
      if(L.kind==='line') o+=kx(t('vValues'),'values',(L.values||[]).join(', '),'5, 9, 14, 22')+kx(t('vLabels'),'labels',(L.labels||[]).join(LANG==='en'?', ':'، '),LANG==='en'?'January, February':'يناير، فبراير')+kx(t('vUnit'),'unit',L.unit||'','k');
      if(L.kind==='slot') o+='<div class="row"><label>'+t('vValue')+'</label><input type="number" data-k="L.value" value="'+esc(L.value==null?2480:L.value)+'"></div>'+kx(t('vUnit'),'unit',L.unit||'',LANG==='en'?'$':'ر.س');
      if(L.kind==='news') o+=kx(t('vSource'),'source',L.source||'',LANG==='en'?'Breaking':'عاجل')+'<textarea data-k="L.text" rows="3" dir="auto" style="margin-bottom:8px">'+esc(L.text||'')+'</textarea>'+kx(t('vMark'),'mark',L.mark||'',t('vMarkPh'))+pick(t('image'),'L.src',[['',t('bgNone')],...(INFO.assets||[]).map(a=>['assets/'+a,a])],L.src||'');
      if(L.kind==='card'||L.kind==='draw') o+='<div class="warnbox">'+t('byClaude')+'</div>';
      if(L.kind!=='cta'&&L.kind!=='bars'&&L.kind!=='route'&&L.kind!=='card'&&L.kind!=='draw'&&L.kind!=='news') o+=kx(t('vLabel'),'label',L.label||'',t('vLabelPh'));
      o+=swatches(t('accent'),'L.accent',L.accent||(ST.theme&&ST.theme.acc)||'#F2B33D')+(L.kind==='fill'?swatches(t('vColor2'),'L.color2',L.color2||'#C9CDD8'):'')+(L.kind!=='cta'&&(L.layout||'stage')!=='over'?swatches(t('cardColor'),'L.bgColor',L.bgColor||'#F5F6FA'):''); }
    if(L.type==='kinetic'){ const ti=(k,v,ph)=>'<input type="text" data-k="'+k+'" dir="auto" value="'+esc(v||'')+'" placeholder="'+esc(ph||'')+'" style="margin-bottom:8px">', c=L.card||'none';
      o+='<p class="hint">'+t('kinHint')+'</p><textarea data-k="L.text" rows="4" dir="auto" style="margin-bottom:9px">'+esc(L.text||'')+'</textarea>'
        +slider(t('posY'),'L.y',0.1,0.8,L.y==null?(c!=='none'?0.25:0.43):L.y,0.005)+pick(t('font'),'L.font',[['',t('stSame')],...[...[...new Set(hs().fonts.map(f=>f.name))],...AR_FONTS].map(f=>[f,f])],L.font||'')
        +pick(t('kinCard'),'L.card',[['none',t('bgNone')],['terminal',t('kc_terminal')],['phone',t('kc_phone')],['pill',t('kc_pill')],['comment',t('kc_comment')],['profile',t('kc_profile')],['image',t('image')]],c);
      if(c!=='none'){ o+=ti('L.cardText',L.cardText,t('kinCardText'));
        if(c==='terminal'||c==='phone') o+=ti('L.cardTitle',L.cardTitle,t('kinCardTitle'));
        if(c==='terminal') o+='<textarea data-k="L.cardOut" rows="3" dir="auto" style="margin-bottom:8px" placeholder="'+esc(t('kinCardOut'))+'">'+esc(Array.isArray(L.cardOut)?L.cardOut.join('\n'):(L.cardOut||''))+'</textarea>';
        if(c==='comment'||c==='profile') o+=ti('L.cardSub',L.cardSub,t('kinCardSub'));
        if(c==='image'||c==='phone'||c==='comment'||c==='profile') o+=pick(t('image'),'L.src',[['',t('bgNone')],...(INFO.assets||[]).map(a=>['assets/'+a,a])],L.src||'');
        o+=slider(t('kinCardAt'),'L.cardAt',0,Math.max(0.2,+(L.e-L.s).toFixed(2)),L.cardAt==null?0.18:L.cardAt,0.05); }
      o+=pick(t('deco'),'L.deco',[['none',t('bgNone')],['flowers',t('kd_flowers')],['badges',t('kd_badges')],['both',t('kd_both')]],L.deco||'none')
        +seg(t('kinReveal'),'L.reveal',[['spoken',t('kr_spoken')],['even',t('kr_even')],['all',t('kr_all')]],L.reveal||'spoken'); }
    if(L.type==='desk'){ const DK=['note','polaroid','number','strike','invoice','file','clock','chart','swatches','sticker','label','cta'], ti=(k,v,ph)=>'<input type="text" data-k="'+k+'" dir="auto" value="'+esc(v==null?'':v)+'" placeholder="'+esc(ph||'')+'" style="margin-bottom:8px">', yn=(lbl,k,v)=>seg(lbl,k,[[true,t('yes')],[false,t('no')]],v);
      o+='<p class="hint">'+t('deskHint')+'</p>'+pick(t('deskKind'),'L.kind',DK.map(k=>[k,t('dk_'+k)]),L.kind||'note');
      const k=L.kind||'note', ta=(key,val,rows,ph,dir)=>'<textarea data-k="'+key+'" rows="'+(rows||2)+'" dir="'+(dir||'auto')+'" style="margin-bottom:8px" placeholder="'+esc(ph||'')+'">'+esc(val||'')+'</textarea>';
      if(k==='number') o+='<div class="row"><label>'+t('vValue')+'</label><input type="number" data-k="L.n" value="'+esc(L.n==null?24:L.n)+'"></div>'+ti('L.unit',L.unit,t('vUnit'))+ti('L.sub',L.sub,t('deskSub'))+yn(t('deskCircle'),'L.circle',L.circle!==false)+yn(t('deskStrike'),'L.strike',!!L.strike);
      else if(k==='strike') o+=ti('L.text',L.text,t('deskFrom'))+ti('L.to',L.to,t('deskTo'))+ti('L.sub',L.sub,t('deskSub'))+ti('L.head',L.head,'WE VALUE SKILLS:');
      else if(k==='invoice') o+=ta('L.items',Array.isArray(L.items)?L.items.join('\n'):String(L.items||'').split('|').join('\n'),4,'EXTRA EDITS=$0','ltr')+ti('L.head',L.head,'INVOICE');
      else if(k==='chart') o+=ti('L.values',Array.isArray(L.values)?L.values.join(', '):(L.values||'100, 70, 45'),t('vValues'))+ti('L.text',L.text,t('deskUnder'))+ti('L.mark',L.mark,t('vMark'));
      else if(k==='swatches') o+=ti('L.colors',Array.isArray(L.colors)?L.colors.join(' '):(L.colors||'#FFFFFF #B3261E #3F7D4E #1A1917'),t('deskColors'))+ti('L.text',L.text,t('deskUnder'));
      else if(k!=='sticker'&&k!=='clock') o+=ta('L.text',L.text,2);
      if(k==='note'||k==='polaroid') o+=ti('L.label',L.label,'EDIT REQUEST #1')+ti('L.head',L.head,'RAW FOOTAGE');
      if(k==='note') o+=ti('L.sub',L.sub,t('deskSub'))+yn(t('deskSticker'),'L.sticker',!!L.sticker);
      if(k==='polaroid') o+=pick(t('image'),'L.src',[['video',t('dk_video')],['clock',t('dk_clock')],...(INFO.assets||[]).map(a=>['assets/'+a,a])],L.src||'video');
      if(k==='file') o+=ti('L.sub',L.sub,t('deskSub'))+ti('L.head',L.head,'FILE:')+yn(t('deskCross'),'L.cross',!!L.cross);
      if(k==='clock') o+=yn(t('deskSticker'),'L.sticker',L.sticker!==false);
      if(k==='label'||k==='cta') o+=swatches(t('color'),'L.color',L.color||'#E8541E');
      if(k==='note'||k==='polaroid'||k==='clock'||k==='chart') o+=yn(t('deskClip'),'L.clip',L.clip!==false);
      if(k==='number') o+=slider(t('size'),'L.size',80,260,L.size||170,2);
      else if(k!=='label'&&k!=='cta'&&k!=='sticker') o+=slider(t('deskW'),'L.w',0.1,0.7,L.w||({note:0.4,polaroid:0.4,strike:0.48,invoice:0.44,file:0.19,clock:0.28,chart:0.31,swatches:0.36}[k]||0.4),0.01);
      else if(k==='sticker') o+=slider(t('size'),'L.w',0.05,0.25,L.w||0.1,0.005);
      o+=seg(t('deskFrom2'),'L.from',[['drop',t('df_drop')],['left',t('dir_left')],['right',t('dir_right')],['up',t('df_up')],['pop',t('df_pop')]],L.from||'drop'); }
    if(L.type==='cover') o+='<textarea data-k="L.text" rows="2" dir="auto" style="margin-bottom:9px">'+esc(L.text||'')+'</textarea>'+pick(t('font'),'L.font',allFonts(),L.font||h.cap.font)+slider(t('size'),'L.size',90,360,L.size||230,2)+swatches(t('background'),'L.bgColor',L.bgColor||'#F3F2EE')+swatches(t('textColor'),'L.color',L.color||'#15151C');
    if(L.type==='split'){ const st=L.style||(Array.isArray(L.draw)&&L.draw.length?'draw':'list'), th=ST.theme||{};
      o+='<div class="grid3" style="margin-bottom:9px">'+CARDS.map(k=>'<div class="tile'+(st===k?' sel':'')+'" data-cstyle="'+k+'"><div class="pv cdp">'+CARDPV[k]+'</div><span>'+t('cs2_'+k)+'</span></div>').join('')+'</div>';
      if(st==='draw') o+='<div class="warnbox">'+t('byClaude')+'</div>';
      o+='<input type="text" data-k="L.title" dir="auto" value="'+esc(L.title||'')+'" placeholder="'+esc(t('splitTitlePh'))+'" style="margin-bottom:8px">';
      if(st==='versus') o+='<div class="row"><input type="text" data-k="L.a" dir="auto" value="'+esc(L.a||'')+'" placeholder="'+esc(t('vsA'))+'"><input type="text" data-k="L.b" dir="auto" value="'+esc(L.b||'')+'" placeholder="'+esc(t('vsB'))+'"></div>';
      if(st==='stat') o+='<div class="row"><label>'+t('vValue')+'</label><input type="number" data-k="L.value" value="'+esc(L.value==null?87:L.value)+'"><input type="text" data-k="L.unit" dir="auto" value="'+esc(L.unit||'')+'" placeholder="%" style="max-width:90px;flex:none"></div><input type="text" data-k="L.label" dir="auto" value="'+esc(L.label||'')+'" placeholder="'+esc(t('vLabelPh'))+'" style="margin-bottom:9px">';
      else if(st!=='draw') o+='<textarea data-k="L.text" rows="'+(st==='quote'?3:5)+'" dir="auto" placeholder="'+esc(t('splitTextPh'))+'" style="margin-bottom:6px">'+esc(L.text||'')+'</textarea><p class="hint" style="margin-top:0">'+t('ch_'+st)+'</p>';
      if(st==='quote') o+='<input type="text" data-k="L.by" dir="auto" value="'+esc(L.by||'')+'" placeholder="'+esc(t('quoteBy'))+'" style="margin-bottom:9px">';
      if(st==='list') o+=seg(t('listMark'),'L.num',[[false,t('markDot')],[true,t('markNum')]],!!L.num);
      o+=pick(t('image'),'L.src',[['',t('bgNone')],...(INFO.assets||[]).map(a=>['assets/'+a,a])],L.src||'')+pick(t('deco'),'L.deco',[['glow',t('deco_glow')],['dots',t('deco_dots')],['grid',t('deco_grid')],['waves',t('deco_waves')],['none',t('bgNone')]],L.deco||'glow')
        +'<div class="row"><label>'+t('splitRatio')+'</label><div class="seg"><button data-ratio="auto" class="'+(L.ratio?'':'on')+'">'+t('auto')+'</button><button data-ratio="man" class="'+(L.ratio?'on':'')+'">'+t('manual')+'</button></div></div>'+(L.ratio?slider(t('splitRatio'),'L.ratio',0.38,0.62,L.ratio,0.01):'<p class="hint" style="margin-top:-4px">'+t('ratioAutoHint')+'</p>')
        +slider(t('size'),'L.size',56,120,L.size||84)+swatches(t('cardColor'),'L.bgColor',L.bgColor||th.bg||'#101014')+swatches(t('textColor'),'L.color',L.color||th.ink||'#FFFFFF')+swatches(t('accent'),'L.accent',L.accent||th.acc||'#F2B33D'); }
    if(L.type==='bg'){ const m=L.mode||'blur'; o+='<p class="hint">'+t('bgHint')+'</p><div class="grid3" style="margin-bottom:9px">'+BGM.map(k=>'<div class="tile'+(m===k?' sel':'')+'" data-bgm="'+k+'"><div class="pv bgm bgm-'+k+'"><i></i></div><span>'+t('bg_'+k)+'</span></div>').join('')+'</div>';
      if(m==='blur'||m==='bw'||m==='dim') o+=slider(t('amount'),'L.amount',0.1,1,L.amount==null?0.6:L.amount,0.05);
      if(m==='color'||m==='grad'||m==='studio') o+=swatches(t('color'),'L.color',L.color||(ST.theme&&ST.theme.bg)||'#101014');
      if(m==='grad') o+=swatches(t('color2'),'L.color2',L.color2||(ST.theme&&ST.theme.acc)||'#F2B33D');
      if(m==='studio') o+=swatches(t('accent'),'L.accent',L.accent||(ST.theme&&ST.theme.acc)||'#F2B33D');
      if(m==='image') o+=pick(t('image'),'L.src',[['',t('bgNone')],...(INFO.assets||[]).map(a=>['assets/'+a,a])],L.src||'')+'<div class="row"><label></label><button class="sm" data-up="bgimg">'+t('upload')+'</button></div>'; }
    if(L.type==='behind') o+='<p class="hint">'+t('behindHint')+'</p><textarea data-k="L.text" rows="2" dir="auto" style="margin-bottom:9px">'+esc(L.text||'')+'</textarea>'+pick(t('font'),'L.font',allFonts(),L.font||h.cap.font)+slider(t('size'),'L.size',120,460,L.size||270,2)+swatches(t('textColor'),'L.color',L.color||'#FFFFFF')+seg(t('fillMode'),'L.fill',[['solid',t('fillSolid')],['outline',t('fillOutline')]],L.fill||'solid')
      +'<div class="row"><label>'+t('posY')+'</label><div class="seg"><button data-byauto="1" class="'+(L.y==null?'on':'')+'">'+t('behindAuto')+'</button><button data-byauto="0" class="'+(L.y==null?'':'on')+'">'+t('manual')+'</button></div></div>'+(L.y==null?'':slider(t('posY'),'L.y',0.05,0.9,L.y,0.005)+slider(t('posX'),'L.x',0,1,L.x==null?0.5:L.x,0.005))+pick(t('entrance'),'L.anim',ANIMS.map(a=>[a,t('an_'+a)]),L.anim||'rise');
    if(L.type==='pip') o+='<p class="hint">'+t('pipHint')+'</p>'+seg(t('pipPos'),'L.pos',PIPS.map(k=>[k,t('pip_'+k)]).concat([['free',t('pip_free')]]),L.pos||'tr')+'<p class="hint" style="margin-top:-2px">'+t('pipDrag')+'</p>'+slider(t('size'),'L.size',0.15,0.9,L.size||0.36,0.01)+seg(t('pipShape'),'L.circle',[[false,t('pipRect')],[true,t('pipCircle')]],!!L.circle)
      +pick(t('deco'),'L.deco',[['grid',t('deco_grid')],['dots',t('deco_dots')],['glow',t('deco_glow')],['lattice',t('deco_lattice')],['halftone',t('deco_halftone')],['blueprint',t('deco_blueprint')],['none',t('bgNone')]],L.deco||'grid')+swatches(t('background'),'L.bgColor',L.bgColor||(ST.theme&&ST.theme.bg)||'#101014')+swatches(t('accent'),'L.accent',L.accent||(ST.theme&&ST.theme.acc)||'#F2B33D');
    if(L.type==='mark') o+='<div class="grid3" style="margin-bottom:9px">'+MKK.map(k=>'<div class="tile'+((L.kind||'circle')===k?' sel':'')+'" data-k="L.kind" data-v="'+k+'"><div class="pv mkp" style="pointer-events:none">'+MKPV[k]+'</div><span style="pointer-events:none">'+t('mk_'+k)+'</span></div>').join('')+'</div>'
      +slider(t('posX'),'L.x',0,1,L.x==null?0.5:L.x,0.005)+slider(t('posY'),'L.y',0,1,L.y==null?0.4:L.y,0.005)+slider(t('mkW'),'L.w',0.05,1,L.w||0.42,0.01)+slider(t('mkH'),'L.h',0.01,0.4,L.h||0.07,0.005)+slider(t('lineWidth'),'L.lw',3,30,L.lw||10)+swatches(t('color'),'L.color',L.color||'#FFD21F')+'<p class="hint">'+t('mkHint')+'</p>';
    if(L.type==='draw') o+='<div class="row"><label></label><button class="sm" id="drawAgain">'+t('drawAgain')+'</button></div>'+swatches(t('color'),'L.color',L.color||'#FFD21F')+slider(t('lineWidth'),'L.lw',3,40,L.lw||12)+slider(t('drawSpeed'),'L.reveal',0,3,L.reveal==null?0.9:L.reveal,0.1)+slider(t('size'),'L.sc',0.3,2,L.sc||1,0.05)+slider(t('posX'),'L.x',0,1,L.x==null?0.5:L.x,0.005)+slider(t('posY'),'L.y',0,1,L.y==null?0.5:L.y,0.005)+seg(t('drawGlow'),'L.glow',[['shadow',t('drawShadow')],['neon',t('drawNeon')],['none',t('no')]],L.glow||'shadow')+'<p class="hint">'+t('drawHint')+'</p>';
    if(L.type==='cursor') o+=slider(t('posX'),'L.x',0,1,L.x==null?0.5:L.x,0.005)+slider(t('posY'),'L.y',0,1,L.y==null?0.45:L.y,0.005)+slider(t('curAt'),'L.at',0.3,Math.max(0.4,+(L.e-L.s).toFixed(2)),L.at==null?1:L.at,0.05)+seg(t('curFrom'),'L.from',[['bottom',t('dir_down')],['left',t('dir_left')],['right',t('dir_right')]],L.from||'bottom')+seg(t('curStyle'),'L.style',[['light',t('curLight')],['dark',t('curDark')]],L.style||'light')+slider(t('size'),'L.size',0.06,0.2,L.size||0.1,0.005)+'<p class="hint">'+t('curHint')+'</p>';
    if(L.type==='lt') o+='<input type="text" data-k="L.text" dir="auto" value="'+esc(L.text||'')+'" placeholder="'+esc(t('ltName'))+'" style="margin-bottom:8px"><input type="text" data-k="L.sub" dir="auto" value="'+esc(L.sub||'')+'" placeholder="'+esc(t('ltSub'))+'" style="margin-bottom:9px">'
      +seg(t('style'),'L.style',LTS.map(k=>[k,t('lt_'+k)]),L.style||'bar')+seg(t('ltSide'),'L.side',[['right',t('dir_right')],['left',t('dir_left')]],L.side||'right')+slider(t('posY'),'L.y',0.1,0.9,L.y==null?0.7:L.y,0.005)+slider(t('size'),'L.size',36,110,L.size||64)+pick(t('font'),'L.font',allFonts(),L.font||h.cap.font)+swatches(t('accent'),'L.accent',L.accent||(ST.theme&&ST.theme.acc)||'#F2B33D');
    if(L.type==='mg') o+=mgPanel(L);
    if(L.type==='collage'){ const its=(L.items||[]).map(x=>x.src); o+='<p class="hint">'+t('collageHint')+'</p><div class="chips" style="margin-bottom:9px">'+(INFO.assets||[]).map(a=>'<button data-colimg="assets/'+esc(a)+'" class="'+(its.includes('assets/'+a)?'on':'')+'">'+esc(a)+'</button>').join('')+'</div><div class="row"><label></label><button class="sm" data-up="image">'+t('upload')+'</button></div>'
      +'<div class="row"><label>'+t('collageMood')+'</label><div class="sw">'+[['#E07A3F','t_time'],['#E3B23C','t_tool'],['#2E6B5A','t_mind'],['#4B2E6B','t_memory'],['#1F7A80','t_team']].map(m=>'<i data-k="L.bgColor" data-c="'+m[0]+'" title="'+esc(t('cm_'+m[1]))+'" class="'+((L.bgColor||'#E07A3F')===m[0]?'on':'')+'" style="background:'+m[0]+'"></i>').join('')+'<input type="color" data-k="L.bgColor" value="'+esc(L.bgColor||'#E07A3F')+'"></div></div>'
      +seg(t('collageDots'),'L.halftone',[[true,t('yes')],[false,t('no')]],L.halftone!==false); }
    if(L.type==='fx'&&!TRS.includes(L.fx)) o+='<div class="grid3" style="margin-bottom:9px">'+FXS.map(f=>fxTile(f,'data-fxset="'+f+'"',L.fx===f,L.s)).join('')+'</div>'+slider(t('amount'),'L.amount',0.05,1,L.amount==null?0.5:L.amount,0.05)+(L.fx==='tint'||L.fx==='duotone'||L.fx==='strobe'?swatches(t('color'),'L.color',L.color||(L.fx==='duotone'?'#FF5A8A':L.fx==='strobe'?'#FFFFFF':'#F2B33D')):'')+(L.fx==='duotone'?swatches(t('color2'),'L.color2',L.color2||'#1B1F6B'):'');
    if(L.type==='fx'&&TRS.includes(L.fx)) o+='<div class="grid3" style="margin-bottom:9px">'+TRS.map(f=>fxTile(f,'data-fxset="'+f+'"',L.fx===f,L.s)).join('')+'</div>'+(['curve','whip','spin'].includes(L.fx)?seg(t('trDir'),'L.dir',[['right',t('dir_right')],['left',t('dir_left')],['up',t('dir_up')],['down',t('dir_down')]],L.dir||hs().trDir||'right'):'')+'<p class="hint">'+t('trHint')+'</p>';
    if(L.type==='fx'||L.type==='pip'||L.type==='mark'||L.type==='draw'||L.type==='cursor'||L.type==='lt'||L.type==='collage'||L.type==='kinetic'||L.type==='mg') o+='';
    else if(L.type==='anno') o+='';
    else if(L.type==='desk') o+=slider(t('posX'),'L.x',0,1,L.x==null?0.3:L.x,0.005)+slider(t('posY'),'L.y',0,1,L.y==null?0.42:L.y,0.005)+slider(t('rotate'),'L.rot',-20,20,L.rot||0,1);
    else if(L.type==='split'||L.type==='bg'||L.type==='behind'||L.type==='cover'||(L.type==='viz'&&(L.layout||'stage')!=='over')) o+='';
    else if(L.type==='image'&&L.fit==='cover') o+=slider(t('opacity'),'L.opacity',0.1,1,L.opacity==null?1:L.opacity,0.05)+pick(t('entrance'),'L.anim',ANIMS.map(a=>[a,t('an_'+a)]),L.anim||'fade');
    else o+=slider(t('posX'),'L.x',0,1,L.x==null?0.5:L.x,0.005)+slider(t('posY'),'L.y',0,1,L.y==null?0.3:L.y,0.005)+slider(t('rotate'),'L.rot',-45,45,L.rot||0,1)+slider(t('opacity'),'L.opacity',0.1,1,L.opacity==null?1:L.opacity,0.05)+pick(t('entrance'),'L.anim',ANIMS.map(a=>[a,t('an_'+a)]),L.anim||'pop')+'<p class="hint">'+t('gizHint')+'</p>';
    if(['text','image','anno','mark','lt','char','cursor','draw'].includes(L.type)){ o+=tog('L.track',t('trkFace'),t(INFO.face===false?'trkFaceNo':'trkFaceSub'),L.track==='face');   // 4.44
      o+=tog('L.mblur',t('mbOne'),t('mbOneSub'),!!L.mblur);   // 4.45: ضبابية الحركة
      const par=(hs().layers||[]).filter(x=>x.id!==L.id&&x.parent!==L.id&&['text','image','anno','mark','lt','char','draw','cursor'].includes(x.type)); if(par.length) o+=pick(t('parentL'),'L.parent',[['',t('none')],...par.map(x=>[x.id,lname(x)])],L.parent||'')+'<p class="hint">'+t('parentHint')+'</p>'; }   // 4.45: ربط الطبقات
    return o+'</div>'+kfSec(L); }
  if(SEL.kind==='cap'){ const i=+SEL.id, c=ST.caps.cards[i]; if(!c) return ''; const ov=capOvOf(i,false), V=f=>(SCOPE==='one'&&ov&&ov[f]!==undefined)?ov[f]:h.cap[f];
    return '<div class="sec"><h4>'+t('sentence')+' '+(i+1)+'<span class="st" style="direction:ltr">'+fmt(c.s)+' – '+fmt(c.e)+'</span></h4><p dir="rtl" style="line-height:1.9">'+esc(key(c))+'</p>'+rngRow(c.s,c.e,t('capVoice'))+'<div class="row"><button data-edit="'+i+'">'+t('edit')+'</button><button class="ghost" data-drop="'+i+'">'+t('dropSentence')+'</button></div></div>'
      +'<div class="sec"><h4>'+t('blWords')+'</h4><div class="blw" dir="rtl">'+c.w.map((w,j)=>'<button class="sm'+(blIdx(w)>=0?' on':'')+'" data-bl="'+i+':'+j+'">'+esc(w.t)+'</button>').join('')+'</div><p class="hint">'+t('blWordHint')+'</p></div>'+emoCardSec(i,c)
      +'<div class="sec"><h4>'+t('capLook')+(ov?'<button class="sm" id="ovReset">'+t('ovReset')+'</button>':'')+'</h4>'+scopeRow()+slider(t('position'),'C.y',15,92,V('y'),0.5)+slider(t('size'),'C.size',34,150,V('size'))+swatches(t('textColor'),'C.color',V('color'))+swatches(t('activeColor'),'C.active',V('active'))+'<p class="hint">'+t(SCOPE==='one'?'scopeOneHint':'scopeAllHint')+'</p></div>'; }
  if(SEL.kind==='music'){ const m=h.mix; return gkSec('mkf')+'<div class="sec"><h4>'+t('musTitle')+'<span><button class="sm" data-muplay="1">'+t(MUP?'stopListen':'listen')+'</button></span></h4><p class="hint" dir="ltr" style="text-align:start">'+esc(INFO.music||'')+'</p>'
      +slider(t('level'),'mix.bg',0,1,m.bg,0.02)+slider(t('bgFadeIn'),'mix.bgIn',0,6,m.bgIn==null?1:m.bgIn,0.1)+slider(t('bgFadeOut'),'mix.bgOut',0,6,m.bgOut==null?1.4:m.bgOut,0.1)+slider(t('duck'),'mix.duck',0.15,1,m.duck==null?0.45:m.duck,0.05)+'<p class="hint">'+t('musHint')+'</p>'+'<h4 style="margin-top:12px">'+t('mfitT')+'</h4><p class="hint" style="margin-top:0">'+t('mfitSub')+'</p><div class="row"><button class="'+(m.fit?'sm':'pri sm')+'" id="mfitGo">'+t(m.fit?'mfitRedo':'mfitGo')+'</button>'+(m.fit?'<button class="sm ghost" id="mfitOff">'+t('mfitOff')+'</button>':'')+'</div>'+(m.fit?'<p class="hint">'+t('mfitOn',m.fit.D)+'</p>':'')+'</div>'; }
  if(SEL.kind==='sfx'){ const [k,j]=String(SEL.id).split(':'), o=sxGet(k,+j), fo=o.fo==null?0.25:o.fo, sx=(lbl,f,mn,mx,v,st)=>'<div class="row"><label>'+lbl+'</label><input type="range" data-sx="'+f+'" min="'+mn+'" max="'+mx+'" step="'+st+'" value="'+v+'"><span class="val" id="sxv_'+f+'">'+v+'</span></div>';
    return '<div class="sec"><h4>'+esc(t('sfx_'+k))+'<span><button class="sm" data-sxplay="1">'+t('listen')+'</button> <button class="sm" id="lDel">'+t('delete')+'</button></span></h4>'
      +sx(t('sxLevel'),'g',0,2,o.g,0.05)+'<div class="row"><label>'+t('sxStart')+'</label><input type="number" step="0.05" data-sx="t" value="'+o.t+'"><button class="sm ghost" data-sxhere="1">'+t('tFromHere')+'</button></div>'
      +sx(t('sxOff'),'off',0,r3(Math.max(0,o.L-0.1)),o.off,0.05)+sx(t('sxDur'),'d',0.1,r3(Math.max(0.1,o.L-o.off)),o.d,0.05)+sx(t('sxFadeIn'),'fi',0,r3(Math.min(5,o.d)),o.fi,0.05)+sx(t('sxFadeOut'),'fo',0,r3(Math.min(5,o.d)),fo,0.05)
      +'<p class="hint">'+t('sxHint')+'</p></div>'; }
  if(SEL.kind==='voice'){ return '<div class="sec"><h4>'+t('vSel')+'<span class="st" style="direction:ltr">'+fmt(SEL.s)+' – '+fmt(SEL.e)+'</span></h4><p class="hint">'+t('vSelHint',(SEL.e-SEL.s).toFixed(2))+'</p>'
      +'<div style="display:flex;flex-direction:column;gap:6px"><button class="pri" data-vact="cut">'+t('vCut')+'</button><button class="sm" data-vact="mute">'+t('vMute')+'</button><button class="sm" data-vact="low">'+t('vLow')+'</button><button class="sm" data-vact="up">'+t('vUp')+'</button></div></div>'; }
  if(SEL.kind==='vr'){ const r=(hs().mix.vr||[])[+SEL.id]; if(!r) return ''; return '<div class="sec"><h4>'+t('vRange')+'<span><button class="sm" data-vrdel="1">'+t('delete')+'</button></span></h4>'
      +'<div class="row"><label>'+t('timing')+'</label><input type="number" step="0.05" data-vrk="s" value="'+r.s+'"><input type="number" step="0.05" data-vrk="e" value="'+r.e+'"></div>'
      +'<div class="row"><label>'+t('sxLevel')+'</label><input type="range" data-vrk="g" min="0" max="2" step="0.05" value="'+r.g+'"><span class="val" id="vrv_g">'+(r.g===0?t('vMuted'):r.g)+'</span></div><p class="hint">'+t('vRangeHint')+'</p></div>'; }
  if(SEL.kind==='broll'){ const b=ST.studio.brollClips[+SEL.id]; if(!b) return ''; return '<div class="sec"><h4>'+t('broll')+' · '+esc(b.k)+'<button class="sm" id="lDel">'+t('delete')+'</button></h4>'+seg(t('display'),'B.mode',[['full',t('brFull')],['card',t('brCard')],['phone',t('brPhone')]],b.mode||'full')+(b.mode!=='phone'?keyPanel(b):'')+(b.mode==='phone'?seg(t('brPip'),'B.pip',[[true,t('yes')],[false,t('no')]],b.pip!==false)+'<input type="text" data-k="B.badge" dir="auto" value="'+esc(b.badge||'')+'" placeholder="'+esc(t('brBadge'))+'" style="margin-top:8px"><p class="hint">'+t('brPhoneHint')+'</p>':'')+'</div>'; }
  if(SEL.kind==='outro'){ const O=outroT(); return '<div class="sec"><h4>'+t('endCard')+'<span><button class="sm" id="oDel">'+t('delete')+'</button></span></h4><p class="hint">'+t('endCardHint')+'</p>'+slider(t('endDur'),'O.dur',0.8,12,ST.outro,0.1)
    +[['l1','endL1'],['l2','endL2'],['cta','endCta'],['word','endWord'],['sub','endSub']].map(([f,k])=>'<div class="row"><label>'+t(k)+'</label><input type="text" dir="auto" data-ko="'+f+'" value="'+esc(O[f]||'')+'"></div>').join('')
    +'<div class="row"><label>'+t('endFont')+'</label><select data-ko="font"><option value="">'+t('endFontDef')+'</option>'+[...[...new Set(hs().fonts.map(f=>f.name))],...AR_FONTS,...EN_FONTS].map(f=>'<option'+(O.font===f?' selected':'')+' style="font-family:\''+esc(f)+'\'">'+esc(f)+'</option>').join('')+'</select></div>'+'<div class="row"><label>'+t('endChips')+'</label><textarea data-ko="chips" rows="3" dir="auto">'+esc((O.chips||[]).join('\n'))+'</textarea></div><button class="ghost" id="oSee">'+t('endSee')+'</button></div>'; }
  if(SEL.kind==='audio'||SEL.kind==='video'){ const A=SEL.kind==='audio', g=rngG(SEL.s,SEL.e), solo=!!SEL.solo, ttl=solo?(A?'avAudio':'avVideo'):'avBoth';
    const B=(a,lbl,cls)=>'<button class="'+(cls||'sm')+'" data-auact="'+a+'">'+t(lbl)+'</button>';
    return '<div class="sec"><h4>'+t(ttl)+'<span class="st" style="direction:ltr">'+fmt(SEL.s)+' – '+fmt(SEL.e)+'</span></h4>'+(A||!solo?rngRow(SEL.s,SEL.e,t('sxLevel')):'')
      +'<div style="display:flex;flex-direction:column;gap:6px;margin-top:4px">'+B('split','auSplit')
      +(solo?(A?B('delA','delAudio','pri'):B('delV','delVideo','pri')):B('del','delBoth','pri')+B('delA','delAudio')+B('delV','delVideo'))
      +(A&&g===0?B('unmute','auUnmute'):'')+'</div><p class="hint">'+t(solo?'avSoloHint':'avHint',(SEL.e-SEL.s).toFixed(2))+'</p>'+(MARKS.length?'<div class="row"><button class="ghost" id="clrMarks">'+t('clearMarks')+'</button></div>':'')+'</div>'+(A?gkSec('vkf'):camSec(SEL.s,SEL.e)); }
  if(SEL.kind==='blank'){ const b=(hs().blank||[])[+SEL.id]; if(!b) return ''; return '<div class="sec"><h4>'+t('blankTitle')+'<span class="st" style="direction:ltr">'+fmt(b.s)+' – '+fmt(b.e)+'</span></h4><p class="hint">'+t('blankHint')+'</p><button class="pri" data-auact="unblank">'+t('blankUndo')+'</button></div>'; }
  return ''; }
function renderFeed(){ const st=$('#pStages'), fd=$('#pFeed'); const sh=stagesHtml(), fh=feedHtml(60); if(st) st.innerHTML=sh; if(fd) fd.innerHTML=fh||'<p class="hint">'+t('feedEmpty')+'</p>'; agFeed(); }
/* 4.49: «اطلب من Claude» صار شات: طلبك فقاعة، ورد Claude فقاعة، وخطوات شغله سطر صغير بينهم. والكتابة تحت، Enter يرسل */
/* 4.51: المساعد: شعار Claude الأصلي، حالة الربط، والمحادثة بشكل أنظف (خطوات Claude مطوية بسطر) */
const CLP='m4.7144 15.9555 4.7174-2.6471.079-.2307-.079-.1275h-.2307l-.7893-.0486-2.6956-.0729-2.3375-.0971-2.2646-.1214-.5707-.1215-.5343-.7042.0546-.3522.4797-.3218.686.0608 1.5179.1032 2.2767.1578 1.6514.0972 2.4468.255h.3886l.0546-.1579-.1336-.0971-.1032-.0972L6.973 9.8356l-2.55-1.6879-1.3356-.9714-.7225-.4918-.3643-.4614-.1578-1.0078.6557-.7225.8803.0607.2246.0607.8925.686 1.9064 1.4754 2.4893 1.8336.3643.3035.1457-.1032.0182-.0728-.164-.2733-1.3539-2.4467-1.445-2.4893-.6435-1.032-.17-.6194c-.0607-.255-.1032-.4674-.1032-.7285L6.287.1335 6.6997 0l.9957.1336.419.3642.6192 1.4147 1.0018 2.2282 1.5543 3.0296.4553.8985.2429.8318.091.255h.1579v-.1457l.1275-1.706.2368-2.0947.2307-2.6957.0789-.7589.3764-.9107.7468-.4918.5828.2793.4797.686-.0668.4433-.2853 1.8517-.5586 2.9021-.3643 1.9429h.2125l.2429-.2429.9835-1.3053 1.6514-2.0643.7286-.8196.85-.9046.5464-.4311h1.0321l.759 1.1293-.34 1.1657-1.0625 1.3478-.8804 1.1414-1.2628 1.7-.7893 1.36.0729.1093.1882-.0183 2.8535-.607 1.5421-.2794 1.8396-.3157.8318.3886.091.3946-.3278.8075-1.967.4857-2.3072.4614-3.4364.8136-.0425.0304.0486.0607 1.5482.1457.6618.0364h1.621l3.0175.2247.7892.522.4736.6376-.079.4857-1.2142.6193-1.6393-.3886-3.825-.9107-1.3113-.3279h-.1822v.1093l1.0929 1.0686 2.0035 1.8092 2.5075 2.3314.1275.5768-.3218.4554-.34-.0486-2.2039-1.6575-.85-.7468-1.9246-1.621h-.1275v.17l.4432.6496 2.3436 3.5214.1214 1.0807-.17.3521-.6071.2125-.6679-.1214-1.3721-1.9246L14.38 17.959l-1.1414-1.9428-.1397.079-.674 7.2552-.3156.3703-.7286.2793-.6071-.4614-.3218-.7468.3218-1.4753.3886-1.9246.3157-1.53.2853-1.9004.17-.6314-.0121-.0425-.1397.0182-1.4328 1.9672-2.1796 2.9446-1.7243 1.8456-.4128.164-.7164-.3704.0667-.6618.4008-.5889 2.386-3.0357 1.4389-1.882.929-1.0868-.0062-.1579h-.0546l-6.3385 4.1164-1.1293.1457-.4857-.4554.0608-.7467.2307-.2429 1.9064-1.3114Z';
function clLogo(z,c){ return '<svg class="cllogo" width="'+z+'" height="'+z+'" viewBox="0 0 24 24" aria-hidden="true"><path fill="'+(c||'#D97757')+'" d="'+CLP+'"/></svg>'; }
/* 4.52: شعار Claude بالنص يتحرّك وهو يشتغل (الخطة والبناء). العنصر يبقى ثابت وتتحدّث نصوصه بس، عشان الحركة ما تنقطع */
function clLoader(id,title,sub){ return '<div class="clload" id="'+id+'"><div class="cll-ring"><span class="cll-logo">'+clLogo(54)+'</span></div><h3>'+title+'</h3><p class="cll-sub">'+sub+'</p><p class="cll-live" dir="auto"></p><p class="cll-t" dir="ltr"></p></div>'; }
function clLoaderTick(root,secs){ const l=root&&root.querySelector('.clload'); if(!l) return; l.querySelector('.cll-t').textContent=fmtm(secs);
  const t0=Date.now()-secs*1000-3000, last=[...ACT].reverse().find(a=>(a.kind==='tool'||a.kind==='claude')&&a.t*1000>=t0); l.querySelector('.cll-live').textContent=last?srvEn(String(last.text)).replace(/\s+/g,' ').slice(0,110):''; }
const AGSEND='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>';
let CLAUTH=null, CLPOLL=0, CLAL=false;
const AGCLIP='<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5l-8.6 8.6a5 5 0 0 1-7.1-7.1l8.6-8.6a3.3 3.3 0 0 1 4.7 4.7l-8.6 8.6a1.7 1.7 0 0 1-2.4-2.4l7.9-7.9"/></svg>';
document.addEventListener('change',async e=>{ if(!(e.target.dataset&&e.target.dataset.agimg)) return; const f=e.target.files[0]; if(!f) return; toast(t('agImgUp'));   // 4.53: صورة بالمحادثة: ترفعها وClaude يحطها بمكانها
  const r=await api('/hs/asset',f,{'X-Name':encodeURIComponent('chat-'+Date.now()+'-'+f.name)}); if(!r||!r.ok){ toast((r&&srvEn(r.msg))||t('failed')); return; }
  const x=$('#agTx'); if(x){ x.value=(x.value.trim()?x.value.trim()+' ':'')+'[صورة: '+r.src+'] '; x.focus(); agGrow(); } });
function agImgs(s){ return esc(s).replace(/\[صورة: ([^\]]+)\]/g,(m,p)=>'<img class="agimg" alt="" src="/'+p.replace(/^\/+/,'')+'">'); }
async function clAuthLoad(fresh){ CLAL=true; try{ CLAUTH=await api('/hs/claude_auth',{fresh:!!fresh}); }catch(e){} const c=$('#agConn'); if(c) c.outerHTML=agConn(); const s=$('#agSt'); if(s) s.outerHTML=agSt(); return CLAUTH; }
function clState(){ if(!INFO.claude) return 'none'; if(CLAUTH&&CLAUTH.loggedIn===false) return 'out'; if(CLAUTH&&CLAUTH.loggedIn) return 'on'; return 'unk'; }
function agSt(){ const k=clState(); return '<span class="agst '+k+'" id="agSt">'+t('clSt_'+k)+'</span>'; }
function agConn(){ const k=clState(); if(k!=='none'&&k!=='out') return '<div id="agConn"></div>';
  return '<div class="agconn" id="agConn"><div><b>'+t(k==='none'?'clNoneT':'clOutT')+'</b><span>'+t(k==='none'?'clNoneS':'clOutS')+'</span></div><button class="pri sm" data-clterm="'+(k==='none'?'install':'login')+'">'+t(k==='none'?'clInstall':'clLogin')+'</button></div>'; }
async function clTerm(kind){ const r=await api('/hs/claude_term',{kind}); if(!r||!r.ok){ toast((r&&srvEn(r.msg))||t('failed')); return; } toast(t(kind==='install'?'clInstOpened':'clLoginOpened'));
  clearInterval(CLPOLL); let n=0; CLPOLL=setInterval(async()=>{ n++; const a=await clAuthLoad(true); if(a&&a.found&&!INFO.claude) INFO.claude=true; if((a&&a.loggedIn)||n>45){ clearInterval(CLPOLL); if(a&&a.loggedIn){ toast(t('clConnected')); if(RTAB==='claude') renderRight(); } } },4000); }
document.addEventListener('click',e=>{ const b=e.target.closest('[data-clterm],[data-agsug]'); if(!b) return; if(b.dataset.clterm) clTerm(b.dataset.clterm); else { const x=$('#agTx'); if(x){ x.value=b.dataset.agsug; x.focus(); agGrow(); } } });
function agGrow(){ const x=$('#agTx'); if(!x) return; x.style.height='auto'; x.style.height=Math.min(140,x.scrollHeight)+'px'; }
document.addEventListener('input',e=>{ if(e.target.id==='agTx') agGrow(); });
function agItems(){ const L=ACT.slice(-100).map(e=>({at:e.t*1000,e}));
  (NOTES||[]).forEach(n=>L.push({at:noteAt(n)||0,n})); return L.sort((a,b)=>a.at-b.at); }
function agStepTx(e){ return esc(srvEn(String(e.text||'').replace(/^طلب: /,'').replace(/\s+/g,' ').slice(0,140))); }
function agThread(){ const L=agItems();
  if(!L.length) return '<div class="agempty">'+clLogo(30)+'<p>'+t('agEmpty')+'</p><div class="agsug">'+['qkFillers','qkHook','qkCaps'].map(k=>'<button class="sm" data-agsug="'+esc(t(k+'_task'))+'">'+t(k)+'</button>').join('')+'</div></div>';
  let o='', st=[]; const flush=()=>{ if(!st.length) return; o+=st.length===1?'<div class="agstep"><span dir="auto">'+st[0]+'</span></div>':'<details class="agsteps"><summary>'+t('agSteps',st.length)+'</summary>'+st.map(x=>'<div dir="auto">'+x+'</div>').join('')+'</details>'; st=[]; };
  const tm=at=>'<time>'+new Date(at).toTimeString().slice(0,5)+'</time>';
  L.forEach(({e,n})=>{
    if(n){ flush(); if(n.by==='claude'){ o+='<div class="msg c"><span class="av">'+clLogo(14)+'</span>'+aiNote(n)+'</div>'; return; }
      o+='<div class="msg u"><div class="bub">'+(n.img?'<img src="/'+n.img+'?v='+n.id+'">':'')+'<p dir="auto">'+esc(n.text)+'</p>'+(n.audio?'<audio controls preload="none" src="/'+n.audio+'"></audio>':'')+'<div class="meta"><span class="t" data-seek="'+n.t+'">'+fmt(n.t)+'</span><span class="st '+n.status+'">'+t('ns_'+n.status)+'</span><button class="sm ghost" data-delnote="'+n.id+'">'+t('delete')+'</button></div></div></div>'; return; }
    const raw=String(e.text||'');
    if(e.kind==='ask'&&e.at!=null){ flush(); o+='<div class="msg u"><div class="bub"><p dir="auto">'+agImgs(raw.replace(/^طلب: /,''))+'</p><div class="meta"><span class="t" data-seek="'+e.at+'">'+fmt(e.at)+'</span>'+tm(e.t*1000)+'</div></div></div>'; return; }
    if(e.kind==='claude'||e.kind==='done'||e.kind==='err'){ flush(); const lg=e.kind==='err'&&/تسجيل دخولك|مسجّل دخول|login/i.test(raw);
      o+='<div class="msg c'+(e.kind==='err'?' err':'')+'"><span class="av">'+clLogo(14)+'</span><div class="bub"><p dir="auto">'+esc(srvEn(raw))+'</p>'+(lg?'<button class="sm pri" data-clterm="login" style="margin-top:6px">'+t('clLogin')+'</button>':'')+tm(e.t*1000)+'</div></div>'; return; }
    st.push(agStepTx(e)); });
  flush(); return o; }
function agTyping(){ return PULSE&&PULSE.agent&&PULSE.agent.running?'<div class="msg c"><span class="av">'+clLogo(14)+'</span><div class="bub typing"><i class="dots"><b></b><b></b><b></b></i></div></div>':''; }
function agHtml(){ const run=!!(PULSE&&PULSE.agent&&PULSE.agent.running); if(!CLAUTH&&!CLAL&&INFO.claude) setTimeout(()=>clAuthLoad(),0);
  return '<div class="sec chat agchat"><div class="aghd">'+clLogo(18)+'<b>'+t('tab_claude')+'</b>'+agSt()+'<span style="flex:1"></span>'+(run?'<button class="sm ghost" id="agStop">'+t('stop')+'</button>':'')+'</div>'+agConn()
    +'<div class="chatlog" id="agLog">'+agThread()+agTyping()+'</div>'
    +'<div class="agbox"><textarea id="agTx" rows="1" dir="auto" placeholder="'+esc(t('agPh'))+'"></textarea><div class="agbar"><label class="agclip" title="'+esc(t('agImgT'))+'">'+AGCLIP+'<input type="file" accept="image/*,video/*" hidden data-agimg="1"></label><span class="agat" id="agAt" title="'+esc(t('agAtT'))+'">'+fmt(T)+'</span><span style="flex:1"></span><button class="agsend" id="agGo" title="'+esc(t(INFO.claude?'chatSend':'copyReq'))+'"'+(run?' disabled':'')+'>'+AGSEND+'</button></div></div><div id="agOut"></div></div>'; }
function agFeed(){ const lg=$('#agLog'); if(!lg) return; const k=(ACT.length?ACT[ACT.length-1].id:0)+':'+!!(PULSE&&PULSE.agent&&PULSE.agent.running)+':'+(NOTES||[]).map(n=>n.id+String(n.status||'')[0]).join('');
  if(lg.dataset.k===k) return; const atEnd=lg.dataset.k===undefined||lg.scrollTop+lg.clientHeight>=lg.scrollHeight-30; lg.dataset.k=k;
  lg.innerHTML=agThread()+agTyping(); if(atEnd) lg.scrollTop=1e6; }
document.addEventListener('keydown',e=>{ if(e.target.id==='agTx'&&e.key==='Enter'&&!e.shiftKey&&!e.isComposing){ e.preventDefault(); const g=$('#agGo'); if(g&&!g.disabled) g.click(); } });
function stagesHtml(){ const ss=PULSE.stages||[]; const now=ss.findIndex(s=>!s.done); return ss.map((s,i)=>'<div class="'+(s.done?'done':i===now?'now':'')+'"><i></i>'+esc(LANG==='ar'?s.ar:s.en)+(s.pct?' · '+s.pct+'%':'')+'</div>').join(''); }
function feedHtml(n){ return ACT.slice(-n).reverse().map(e=>'<div class="k-'+e.kind+'"><time>'+new Date(e.t*1000).toTimeString().slice(0,5)+'</time><span dir="auto">'+esc(srvEn(e.text))+'</span></div>').join(''); }
function renderLive(){ if(READY) return; $('#liveStages').innerHTML=stagesHtml(); $('#liveFeed').innerHTML=feedHtml(40)||'<p class="hint">'+t('liveWaiting')+'</p>'; const p=PULSE.preview, im=$('#livePrev'); if(p){ const u='/'+p.path+'?v='+p.mt; if(im.dataset.u!==u){ im.dataset.u=u; im.src=u; } im.style.display='block'; } else im.style.display='none'; }

function vizParse(key,raw){ raw=String(raw); if(key==='labels'){ const a=raw.split(/[,،]/).map(x=>x.trim()).filter(Boolean); return a; } if(key==='values'){ const a=raw.split(/[,،\s]+/).map(Number).filter(x=>isFinite(x)&&String(x)!=='NaN'&&raw.trim()!==''); return a.length?a:null; }
  if(key==='items'){ const a=raw.split('\n').map(l=>{ const m=l.match(/^(.*?)[=:،,]\s*(-?[\d.]+)\s*$/); return m?{label:m[1].trim(),value:+m[2]}:null; }).filter(Boolean); return a.length?a:null; }
  if(key==='from'||key==='to'){ const m=raw.split(/[,،]/).map(x=>x.trim()); if(m.length<3||!isFinite(+m[m.length-2])||!isFinite(+m[m.length-1])) return null; return {name:m.slice(0,m.length-2).join(' '),lat:+m[m.length-2],lon:+m[m.length-1]}; }
  if(key==='km'){ return raw.trim()===''?undefined:(isFinite(+raw)?+raw:null); } return raw; }
let _oT=0; function panelInput(e){ const el=e.target, k=el.dataset.k;
  if(el.dataset.dkbs!==undefined||el.dataset.dkbm!==undefined){ const D=hs().dahih, i=+(el.dataset.dkbs||el.dataset.dkbm); if(!D||!D.bgs[i]) return; if(!el._sn){ snap(); el._sn=1; setTimeout(()=>el._sn=0,1200); } if(el.dataset.dkbs!==undefined){ const v=+el.value; if(!isFinite(v)) return; D.bgs[i].s=r3(Math.max(0,v)); } else D.bgs[i].mode=el.value; live(); return; }
  if(el.dataset.ko||k==='O.dur'){ if(!el._sn){ snap(); el._sn=1; setTimeout(()=>el._sn=0,1200); } if(k==='O.dur'){ const v=+el.value; if(!isFinite(v)) return; ST.outro=r3(clamp(v,0.8,12)); const s=document.getElementById(vid(k)); if(s) s.textContent=ST.outro; buildTL(); }
    else { const O=ST.studio.outro={...outroT()}, f=el.dataset.ko; if(f==='chips') O.chips=el.value.split('\n').map(x=>x.trim()).filter(Boolean).slice(0,6); else if(f==='font'&&!el.value) delete O.font; else O[f]=el.value; if(f==='font'&&el.value) fontLink(); }
    clearTimeout(_oT); _oT=setTimeout(()=>{ hard(); if(T<total()) seek(Math.min(dur()-0.05,total()+1.6)); },350); return; }
  if(el.dataset.anlab!=null){ const L=selLayer(); if(!L) return; if(!el._sn){ snap(); el._sn=1; setTimeout(()=>el._sn=0,1200); } const i=+el.dataset.anlab; L.labels=L.labels||[]; while(L.labels.length<=i) L.labels.push(''); L.labels[i]=el.value; live(); return; }
  if(el.dataset.bar){ const L=selLayer(); if(!L||!L.items) return; const [i,f]=el.dataset.bar.split(':'); if(!L.items[+i]) return; if(!el._sn){ snap(); el._sn=1; setTimeout(()=>el._sn=0,1200); } if(f==='value'){ const v=+el.value; if(!isFinite(v)||el.value==='') return; L.items[+i].value=v; } else L.items[+i].label=el.value; live(); return; }
  if(el.dataset.city){ const L=selLayer(); if(!L) return; const n=cityFind(el.value); el.style.borderColor=n||!el.value.trim()?'':'var(--bad)'; if(!n) return; if(!el._sn){ snap(); el._sn=1; setTimeout(()=>el._sn=0,1200); } L[el.dataset.city]={name:n,lat:CITIES[n][0],lon:CITIES[n][1]}; delete L.km; live(); return; }
  if(el.dataset.kx){ const L=selLayer(); if(!L) return; const v=vizParse(el.dataset.kx,el.value); if(v===null) return; if(!el._sn){ snap(); el._sn=1; setTimeout(()=>el._sn=0,1200); } if(v===undefined) delete L[el.dataset.kx]; else L[el.dataset.kx]=v; if(el.dataset.kx==='values') delete L.value; live(); return; }
  if(el.dataset.en!==undefined){ const c=ST.caps.cards[+el.dataset.en], v=el.value.trim(); if(v) hs().en.map[key(c)]=v; else delete hs().en.map[key(c)]; live(); return; }
  if(el.dataset.sx&&SEL&&SEL.kind==='sfx'){ const [kk,jj]=String(SEL.id).split(':'), o=sxGet(kk,+jj), f=el.dataset.sx, v=+el.value; if(!isFinite(v)) return; if(!el._sn){ snap(); el._sn=1; setTimeout(()=>el._sn=0,1200); }
    o[f]=f==='t'?clamp(v,0,total()):v; if(f==='off') o.d=Math.min(o.d,Math.max(0.1,o.L-o.off)); if(o.fi+(o.fo||0)>o.d){ if(f==='fi') o.fo=Math.max(0,o.d-o.fi); else o.fi=Math.max(0,o.d-(o.fo||0)); }
    sxPut(kk,+jj,o); const sp=$('#sxv_'+f); if(sp) sp.textContent=v; buildTL(); dirty(); return; }
  if(el.dataset.rngv){ const [a,b]=el.dataset.rngv.split(',').map(Number), v=+el.value; if(!isFinite(v)) return; if(!el._sn){ snap(); el._sn=1; setTimeout(()=>el._sn=0,1200); } rngSet(a,b,v); const lb=$('#rngv'); if(lb) lb.textContent=v===0?t('vMuted'):v; return; }
  if(el.dataset.vrk&&SEL&&SEL.kind==='vr'){ const r=hs().mix.vr[+SEL.id], f=el.dataset.vrk, v=+el.value; if(!r||!isFinite(v)) return; if(!el._sn){ snap(); el._sn=1; setTimeout(()=>el._sn=0,1200); }
    r[f]=r3(f==='g'?clamp(v,0,3):clamp(v,0,total())); if(r.e<r.s+0.05) r.e=r3(r.s+0.05); const sp=$('#vrv_g'); if(sp&&f==='g') sp.textContent=r.g===0?t('vMuted'):r.g; vrDraw(); dirty(); return; }
  if(!k||el.type==='radio') return; if(!el._sn){ snap(); el._sn=1; setTimeout(()=>el._sn=0,1200); }
  let v=el.value; if(el.type==='range'||el.type==='number'){ v=+v; if(isNaN(v)) return; const s=document.getElementById(vid(k)); if(s) s.textContent=v; } else if(el.tagName==='SELECT'&&/weight$/.test(k)) v=+v;
  if(k==='L.s') v=clamp(v,0,(selLayer().e||total())-0.1); if(k==='L.e') v=clamp(v,selLayer().s+0.1,total());
  setK(k,v); propagate(k,v); if(k==='mix.voice') AU.volume=clamp(v,0,1); if(k==='mix.bg'){ if(MUP) MUP.volume=clamp(v,0,1); vrDraw(); }
  if(k.startsWith('check.')){ dirty(); return; } if(k.startsWith('mix.')){ dirty(); return; }
  live(); if(k==='L.s'||k==='L.e'||k==='L.text'||k==='L.fx'||k==='L.char') buildTL(); if(el.tagName==='SELECT'||el.type==='color') renderRight(); }
$('#body').addEventListener('input',panelInput);
$('#body').addEventListener('change',e=>{ const el=e.target; if(el.id==='capStyle'){ snap(); ST.theme.capStyle=el.value; hard(); } if(el.dataset.k==='cap.y'||el.dataset.k==='cap.stroke') renderRight(); if(el.dataset.k==='frame.cy') frameSync(); if(el.dataset.k==='emoji.gap') renderRight(); if(el.id==='postTx'){ INFO.post=el.value; api('/hs/post',{text:el.value}); } });
async function panelClick(e){ const el=e.target, d=el.dataset;
  if(d.emoset!==undefined){ emoSet(d.emoset); return true; }   /* 4.48 */
  if(el.id==='emoGo'){ const v=($('#emoTx').value||'').trim(); if(!v||v.length>16||/[؀-ۿA-Za-z0-9]/.test(v)){ toast(t('emoBad')); return true; } emoSet(v); return true; }
  if(d.emorm!==undefined){ const c=ST.caps.cards[+d.emorm]; if(c){ snap(); hs().emoji.set[key(c)]=''; renderRight(); live(); } return true; }
  if(d.emocard!==undefined){ const i=+d.emocard, c=ST.caps.cards[i]; if(c){ select({kind:'cap',id:i}); RTAB='sel'; markTabs(); renderRight(); seek(Math.max(0,c.s)); } return true; }
  if(await planClick(el)) return true;
  if(await audioClick(el)) return true;
  { const b=el.closest('[data-anpick],[data-anrm],[data-ancue],[data-anburst],[data-imshake],[data-anfromrm]'); const L=selLayer(); if(b&&L){ const q=b.dataset, lt=r3(clamp(T-L.s,0,L.e-L.s));
      if(q.anpick){ pickStart(q.anpick); return true; }
      if(q.anfromrm){ snap(); delete L.from; live(); renderRight(); return true; }
      if(q.anrm!=null){ snap(); const i=+q.anrm; if(L.kind==='boxes') (L.rects||[]).splice(i,1); else (L.pts||[]).splice(i,1); (L.labels||[]).splice(i,1); if(Array.isArray(L.at)) L.at.splice(i,1); live(); renderRight(); return true; }
      if(q.ancue!=null){ snap(); const i=+q.ancue, n=(L.kind==='boxes'?(L.rects||[]):(L.pts||[])).length; L.at=Array.from({length:n},(_,j)=>Array.isArray(L.at)&&L.at[j]!=null?L.at[j]:null); L.at[i]=lt; const firstNull=L.at.findIndex(v=>v==null); if(firstNull>=0) L.at=L.at.map((v,j)=>v==null?r3((j?L.at[j-1]||0:0)+0.6):v); live(); renderRight(); toast(t('akCueSet',fmt(T))); return true; }
      if(q.anburst){ snap(); if(q.anburst==='clear') L.burst=[]; else (L.burst=L.burst||[]).push([lt,r3(Math.min(L.e-L.s,lt+0.9))]); live(); renderRight(); return true; }
      if(q.imshake){ snap(); if(q.imshake==='clear') L.shake=[]; else (L.shake=L.shake||[]).push(lt); live(); renderRight(); return true; } } }
  if(d.mgkind){ const L=selLayer(); if(!L||L.type!=='mg') return true; snap(); const D=DF('mg',d.mgkind)||{}; L.kind=d.mgkind; for(const k in D) if(L[k]==null||L[k]==='') L[k]=JSON.parse(JSON.stringify(D[k])); renderRight(); buildTL(); live(); return true; }
  if(d.mglogo){ const L=selLayer(); if(!L||L.type!=='mg') return true; const two=d.mglogo==='2', nm=String(two?L.name2:L.name||'').trim(); if(!nm) return true; toast(t('mgLogoGetting'));
    const r=await api('/hs/logo',{name:nm}); snap(); if(r.ok){ if(two) L.src2=r.src; else L.src=r.src; await (window.__hsLoadImg?window.__hsLoadImg(r.src):0); toast(t('mgLogoGot')); } else { if(two) L.src2=''; else L.src=''; toast(t('mgLogoNone')); } renderRight(); live(); return true; }
  if(d.mglogos){ toast(t('mgLogoGetting')); const r=await api('/hs/logos',{}); const pl=(r&&r.plan)||[]; if(!pl.length){ toast(t('mgLogosNone')); return true; } snap(); const h=hs(); h.layers=h.layers.filter(L=>L.auto!=='logos'); let n=Math.max(0,...h.layers.map(l=>parseInt(String(l.id).replace(/\D/g,''))||0));
    for(const p of pl){ const L={id:'L'+(++n),type:'mg',kind:'logo',auto:'logos',track:1,s:p.s,e:p.e,name:p.name,src:p.src||''}; if(p.name2) Object.assign(L,{name2:p.name2,src2:p.src2||'',rel:p.rel}); h.layers.push(L); if(window.__hsLoadImg){ if(L.src) window.__hsLoadImg(L.src); if(L.src2) window.__hsLoadImg(L.src2); } }
    toast(t('mgLogosAdded').replace('%d',pl.length)); buildTL(); renderRight(); live(); return true; }
  if(d.k==='trDir'&&d.v){ snap(); const h=hs(); h.trDir=d.v; h.layers.forEach(L=>{ if(L.type==='fx'&&(L.auto==='trans'||L.auto==='transitions')&&['curve','whip','spin'].includes(L.fx)) L.dir=d.v; }); renderLeft(); live(); return true; }
  if(d.colimg){ const L=selLayer(); if(!L) return true; snap(); const a=(L.items||[]).map(x=>x.src), i=a.indexOf(d.colimg); if(i>=0) a.splice(i,1); else if(a.length<6) a.push(d.colimg); L.items=a.map(src=>({src})); renderRight(); live(); return true; }
  { const L=selLayer(), tl=el.closest('[data-cstyle],[data-bgm],[data-fxset]');
    if(L&&tl){ snap(); if(tl.dataset.cstyle){ const k=tl.dataset.cstyle, df=DF('card',k)||{}; L.style=k; ['text','a','b','value','unit','label'].forEach(f=>{ if((L[f]==null||L[f]==='')&&df[f]!=null) L[f]=df[f]; }); if(k==='versus'&&!/\|/.test(L.text||'')) L.text=df.text; if(k==='check'&&!/^[+\-]/m.test(L.text||'')) L.text=df.text; if((k==='timeline'||k==='funnel')&&!/\|/.test(L.text||'')) L.text=df.text; }
      else if(tl.dataset.bgm){ L.mode=tl.dataset.bgm; if((L.mode==='color'||L.mode==='grad'||L.mode==='studio')&&!L.color) L.color=(ST.theme&&ST.theme.bg)||'#101014'; if(L.mode==='image'&&!L.src&&(INFO.assets||[])[0]) L.src='assets/'+INFO.assets[0]; }
      else L.fx=tl.dataset.fxset; buildTL(); renderRight(); await live(); return true; }
    if(L&&d.tset){ snap(); if(d.tset==='s') L.s=r3(clamp(T,0,L.e-0.1)); else L.e=r3(clamp(T,L.s+0.1,total())); buildTL(); renderRight(); await live(); return true; }
    if(L&&d.ratio){ snap(); if(d.ratio==='auto') delete L.ratio; else L.ratio=0.5; renderRight(); await live(); return true; }
    if(L&&d.byauto!==undefined){ snap(); if(d.byauto==='1'){ delete L.y; delete L.x; } else { L.y=0.3; L.x=0.5; } renderRight(); await live(); return true; }
    if(L&&d.brm!==undefined&&L.items){ snap(); L.items.splice(+d.brm,1); renderRight(); await live(); return true; }
    if(L&&el.id==='barAdd'){ snap(); L.items=L.items||[]; L.items.push({label:t('vName'),value:100}); renderRight(); await live(); return true; } }
  if(d.tog==='L.track'){ snap(); const L_=selLayer(); if(L_){ if(L_.track==='face') delete L_.track; else L_.track='face'; } renderAll(); await live(); return true; }
  if(d.tog){ snap(); setK(d.tog,!getK(d.tog)); if(d.tog==='en.on'&&getK('en.on')) hs().cap.on=true; renderAll(); if(d.tog.startsWith('mix.')) dirty(); else await live(); if(d.tog==='mix.studio'){ await svApply(); return true; } if(d.tog==='mix.clean'){ auSwap(); return true; } if(d.tog==='hooks.on'&&getK('hooks.on')) seek(0.6); return true; }
  if(el.closest('.fcard')){ snap(); const f=el.closest('.fcard').dataset.font, c=hs().cap; c.font=f; const ws=weightsOf(f); c.weight=ws.reduce((b,x)=>Math.abs(x-c.weight)<Math.abs(b-c.weight)?x:b,ws[0]); renderRight(); await live(); return true; }
  if(d.scope){ SCOPE=d.scope; renderRight(); return true; }
  if(d.cappre!==undefined||el.closest('[data-cappre]')){ snap(); const k=(el.closest('[data-cappre]')||el).dataset.cappre, c=hs().cap; Object.assign(c,capStyle(k),{on:true}); renderRight(); await live(); return true; }
  if(d.c&&d.k){ snap(); setK(d.k,d.c); propagate(d.k,d.c); renderRight(); live(); return true; }
  if(d.v!==undefined&&d.k){ snap(); let v=d.v; if(v==='true') v=true; else if(v==='false') v=false; else if(/^\d+$/.test(v)) v=+v; if(d.k==='cap.chunk') hs().cap.mode='line'; setK(d.k,v); propagate(d.k,v); renderRight(); if(d.k==='B.mode'){ drawT(T); dirty(); } else if(d.k.startsWith('hooks.')){ renderLeft(); live(); } else live(); return true; }
  return false; }
$('#tabs').addEventListener('click',e=>{ const b=e.target.closest('[data-tab]'); if(b){ RTAB=b.dataset.tab; markTabs(); renderRight(); if(RTAB==='plan') loadPlan(); } });
$('#binTabs').addEventListener('click',e=>{ const b=e.target.closest('[data-ltab]'); if(b){ LTAB=b.dataset.ltab; markTabs(); renderLeft(); if(LTAB==='takes') loadTakes(); } });
$('#body').addEventListener('click',async e=>{ const el=e.target, d=el.dataset; if(styleClick(el)) return; if(el.id==='oDel'){ outroSet(0); return; } if(el.id==='oSee'){ seek(total()+0.05); play(); return; } if(await panelClick(e)) return;
  if(d.up){ pickFile(d.up); return; }
  if(d.copy){ navigator.clipboard&&navigator.clipboard.writeText(d.copy); toast(t('copied')); return; }
  if(d.bl){ snap(); const [i,j]=d.bl.split(':').map(Number), w=ST.caps.cards[i]&&ST.caps.cards[i].w[j]; if(!w) return; blToggle(w); renderRight(); renderLeft(); await live(); return; }
  if(d.blrm!==undefined){ snap(); blItems().splice(+d.blrm,1); renderRight(); renderLeft(); await live(); return; }
  if(el.id==='blClr'){ snap(); hs().bleep.items=[]; renderRight(); renderLeft(); await live(); return; }
  if(el.id==='blGo'){ const x=$('#blTx'); if(!x||!x.value.trim()) return; snap(); const [f,n]=blFind(x.value); if(!f){ toast(t('blNotFound')); return; } renderRight(); renderLeft(); await live(); toast(t('blFound',f,n)); return; }
  if(d.seek!==undefined){ if(playing) stop(); seek(+d.seek+0.02); return; }
  if(d.edit!==undefined){ editCard(+d.edit); return; }
  if(d.drop!==undefined){ askRemove({cards:[+d.drop]},'«'+key(ST.caps.cards[+d.drop])+'»'); return; }
  if(el.id==='lDel'){ delSel(); return; } if(el.id==='lDup'){ dupSel(); return; }
  if(el.id==='ovReset'){ snap(); const h=hs(); delete h.capOv[key(ST.caps.cards[+SEL.id])]; renderRight(); live(); return; }
  if(d.frame){ snap(); const h=hs(); h.frame={...(h.frame||{}),ar:d.frame}; await frameSync(); return; }
  if(d.plat){ snap(); const h=hs(), a=h.platforms||[]; h.platforms=a.includes(d.plat)?a.filter(x=>x!==d.plat):[...a,d.plat]; await frameSync(); return; }
  if(d.phone){ phoneFile(d.phone); return; }
  if(el.id==='clrMarks'){ MARKS=[]; marksSave(); SEL=null; buildTL(); renderRight(); return; }
  if(el.id==='matchSize'){ snap(); const h=hs(), m=Math.round((h.cap.size+h.en.size)/2); h.cap.size=m; h.en.size=m; renderRight(); live(); return; }
  if(el.id==='askTr'){ runAgent(t('reqTranslate')); return; }
  if(el.id==='doClean'){ const words=$$('[data-fil]:checked').map(x=>x.dataset.fil.split(':').map(Number)), cards=takesDrop(); if(!words.length&&!cards.length) return; askRemove({words,cards},t('chkRemoveWhat',words.length,cards.length)); return; }
  if(el.id==='newNote'){ openNote(); return; }
  if(d.aians){ let v=d.v; if(v==='text'){ const x=document.querySelector('[data-aitx="'+d.aians+'"]'); v=(x&&x.value||'').trim(); if(!v){ toast(t('noteEmpty')); return; } } const r=await api('/hs/note_edit',{id:d.aians,answer:v}); NOTES=r.notes; buildTL(); renderRight(); toast(t('aiSent')); return; }
  if(d.delnote){ const r=await api('/hs/note_edit',{id:d.delnote,delete:true}); NOTES=r.notes; buildTL(); renderRight(); return; }
  if(d.promote){ const r=await api('/hs/review_promote',{id:+d.promote}); if(r.ok){ NOTES=r.notes; REV={approved:r.approved,comments:r.comments}; buildTL(); renderRight(); } return; }
  if(el.id==='sendNotes'){ if(INFO.claude&&!(await tokenGo('notes','mid'))) return; await save(); const r=await api('/hs/notes_send',{run:!!INFO.claude}); NOTES=r.notes; buildTL(); renderRight(); const out=$('#sendOut');
    if(r.started){ toast(t('claudeStarted')); RTAB='claude'; markTabs(); renderRight(); } else if(out){ out.innerHTML='<p class="hint" style="margin-top:9px">'+(srvEn(r.msg)?esc(srvEn(r.msg))+' ':'')+t('pasteHint',r.count)+'</p><div class="copy"><span dir="auto">'+esc(r.prompt)+'</span><button class="sm" data-copy="'+esc(r.prompt)+'">'+t('copy')+'</button></div>'; } return; }
  if(el.id==='agGo'){ const v=$('#agTx').value.trim(); if(!v) return; if(clState()==='out'){ toast(t('clOutT')); return; } runAgent(v); return; }
  if(el.id==='agStop'){ await api('/hs/agent_stop',{}); return; }
  if(el.id==='doRender'){ doExport('final',$('#exHooks')&&$('#exHooks').checked); return; } if(el.id==='doClean2'){ doExport('clean',false); return; }
  if(el.id==='doPack'){ await api('/hs/post',{text:$('#postTx').value}); const r=await api('/hs/pack',{}); $('#packOut').innerHTML=r.ok?'<p class="hint">'+r.files.map(esc).join(' · ')+'</p><a href="/hs/pack.zip" download>'+t('packDownload')+'</a>':'<p class="hint">'+esc(srvEn(r.msg)||t('failed'))+'</p>'; return; }
  if(el.id==='askPost'){ runAgent(t('reqPost')); return; }
  if(el.id==='doCmp'){ compare($('#cmpA').value,$('#cmpB').value); return; }
  if(el.id==='privShow'){ const r=await api('/hs/tools'); modal('<h3>'+t('privTitle')+'</h3>'+(r.tools||[]).map(x=>'<div class="note"><div style="flex:1"><b>'+esc(srvEn(x.name))+'</b> <span class="st '+(x.ok?'ok':'')+'">'+t(x.ok?'privHave':'privMiss')+'</span><p dir="auto">'+esc(srvEn(x.why))+'</p><p class="hint" dir="auto" style="margin:2px 0 0">'+esc(srvEn(x.src))+'</p></div></div>').join('')+'<h4 style="margin:14px 0 6px">'+t('privNet')+'</h4>'+(r.net||[]).map(x=>'<p class="hint" dir="auto" style="margin:4px 0">'+esc(srvEn(x))+'</p>').join('')+'<div class="row" style="margin:14px 0 0"><button id="qNo">'+t('close')+'</button></div>',true); $('#qNo').onclick=closeModal; return; }
  if(el.id==='brandSave'){ await save(); const r=await api('/hs/brand_save',{name:$('#brandName').value}); if(!r.ok){ toast(srvEn(r.msg)); return; } INFO.brands=r.brands; renderRight(); toast(t('brandSaved')); return; }
  if(el.id==='brandApply'){ const n=$('#brandSel').value; if(!n) return; snap(); const b=await api('/hs/brand/'+encodeURIComponent(n)), h=hs(); h.cap={...h.cap,...(b.cap||{})}; h.en={...h.en,...(b.en||{}),map:h.en.map}; (b.fonts||[]).forEach(f=>{ if(!h.fonts.some(x=>x.file===f.file)) h.fonts.push(f); }); ST.theme={...ST.theme,...(b.theme||{})}; await hard(); renderAll(); toast(t('brandApplied')); return; }
  if(el.id==='verSave'){ await save(); const r=await api('/hs/ver_save',{name:$('#verName').value||t('version')}); INFO.versions=r.versions; renderRight(); toast(t('verSaved')); return; }
  if(d.ver){ await save(); const r=await api('/hs/ver_restore',{id:d.ver}); if(r.rebuild){ toast(t('rebuilding')); pollJob(()=>load(true)); } else { await load(true); toast(t('verRestored')); } return; } });
async function runAgent(task,gen){ if(INFO&&INFO.claude&&!(await tokenGo(gen?'gen':'ask','mid'))) return; await save(); const sel=SEL?(SEL.kind==='layer'?'طبقة '+SEL.id:SEL.kind==='cap'?'الجملة '+(+SEL.id+1):SEL.kind):null; const r=await api('/hs/agent',{task,t:T,sel,gen:!!gen});
  if(r.ok){ toast(t('claudeStarted')); RTAB='claude'; askMark(); markTabs(); renderRight(); } else { RTAB='claude'; askMark(); markTabs(); renderRight(); const out=$('#agOut'); if(out) out.innerHTML='<p class="hint">'+esc(srvEn(r.msg)||'')+' '+t('pasteHint2')+'</p><div class="copy"><span dir="auto">'+esc(r.prompt||task)+'</span><button class="sm" data-copy="'+esc(r.prompt||task)+'">'+t('copy')+'</button></div>'; } }

/* ───── 4.18: وضعين بصفحة وحدة: «Claude يمنتج» و«مونتاج يدوي» (ويدخل Claude معك لو طلبته) ───── */
const MODE_HIDE={claude:['sel','cap','tr','audio'],manual:['plan']};
function uiMode(){ const m=ST?hs().mode:(PULSE&&PULSE.mode); return m==='claude'||m==='manual'?m:(ST?'manual':'claude'); }
function applyMode(){ const m=uiMode(), b=document.body; b.dataset.mode=m; if(m!=='manual') b.classList.remove('asking');
  $$('#modeSw button').forEach(x=>x.classList.toggle('on',x.dataset.mode===m));
  const hid=MODE_HIDE[m].filter(k=>!(k==='claude'&&b.classList.contains('asking')));
  if(ST&&hid.includes(RTAB)){ RTAB=m==='claude'?'claude':'sel'; markTabs(); renderRight(); }
  if(ST) tlFit(); }
function setMode(m){ if(!ST||!MODE_HIDE[m]||uiMode()===m) return; hs().mode=m; document.body.classList.remove('asking'); RTAB=m==='claude'?'claude':'sel'; applyMode(); markTabs(); renderRight(); save(); toast(t(m==='claude'?'modeToClaude':'modeToManual')); }
let ASK_BACK='sel';
function askMark(){ if(uiMode()==='manual') document.body.classList.add('asking'); }
function askOpen(){ if(RTAB!=='claude') ASK_BACK=RTAB; document.body.classList.add('asking'); RTAB='claude'; markTabs(); renderRight(); setTimeout(()=>{ const x=$('#agTx'); if(x) x.focus(); },0); }
function askClose(){ document.body.classList.remove('asking'); RTAB=MODE_HIDE.manual.includes(ASK_BACK)?'sel':ASK_BACK; markTabs(); renderRight(); }
function askOnTx(){ if(!SEL) return t('askOnAll'); if(SEL.kind==='layer'){ const L=selLayer(); return t('askOnLayer',L?lname(L):SEL.id); } if(SEL.kind==='cap') return t('askOnCap',+SEL.id+1); return t('askOnAll'); }
function askCtxHtml(){ if(uiMode()==='manual') return '<div class="askctx"><span>'+t('askOn')+' <b>'+esc(askOnTx())+'</b></span><span class="sp"></span><button class="sm ghost" id="askX">'+t('askBack')+'</button></div>'+(SEL?'':'<p class="hint" style="margin-top:-4px">'+t('askSelHint')+'</p>');
  return '<div class="askctx"><span>'+t('toManualQ')+'</span><span class="sp"></span><button class="sm" id="toManual">'+t('toManualBtn')+'</button></div>'; }
document.addEventListener('click',e=>{ const b=e.target.closest('#modeSw [data-mode],#bAsk,#askX,#toManual'); if(!b) return;
  if(b.dataset.mode) setMode(b.dataset.mode); else if(b.id==='bAsk') (document.body.classList.contains('asking')?askClose:askOpen)(); else if(b.id==='askX') askClose(); else if(b.id==='toManual') setMode('manual'); });

/* ───── 4.20: الهوك عنصر زي غيره: بالتايم لاين، تحدده، تسحبه على الفيديو، ولوحته فيها مكانه وحجمه وألوانه ───── */
const BIDI=/[\u202a-\u202e]/g;
function hookClip(on,box){ const H=hs().hooks; if(!H||!H.on) return ''; const it=(H.items||[])[H.active||0]; if(!it||!it.text) return '';
  return '<div class="clip hook'+on('hook',0)+'" data-kind="hook" data-id="0" style="'+box(0,H.dur||2.6)+'"><i class="hl"></i>'+esc(t('hookClip')+': '+it.text.replace(BIDI,'').replace(/\n/g,' '))+'<i class="hr"></i></div>'; }
function hookInspector(){ const H=hs().hooks, it=H.items||[], a=H.active||0, acc=(ST.theme&&ST.theme.acc)||'#D97757';
  let o='<div class="sec"><h4>'+t('hookTitle')+'<span><button class="sm" id="hkOff">'+t('hookOff')+'</button></span></h4><p class="hint" style="margin-top:0">'+t('hookVer')+'</p>'
    +[0,1,2].map(i=>'<div class="row"><input type="radio" name="hk2" data-hkact="'+i+'"'+(a===i?' checked':'')+' style="flex:none"><textarea rows="2" dir="auto" data-hk="'+i+'" placeholder="'+t('hookN',i+1)+'">'+esc(((it[i]||{}).text||'').replace(BIDI,''))+'</textarea></div>').join('')+'</div>';
  o+='<div class="sec">'+seg(t('style'),'hooks.style',[['box',t('bgBox')],['pill',t('bgPill')],['glass',t('fr_glass')],['plain',t('bgNone')]],H.style||'box')
    +pick(t('font'),'hooks.font',[['',t('stSame')],...allFonts().map(f=>[f,f])],H.font||'')+slider(t('size'),'hooks.size',56,160,H.size||104)
    +swatches(t('textColor'),'hooks.color',H.color||'#FFFFFF')+((H.style||'box')!=='plain'?swatches(t('cardColor'),'hooks.bgColor',H.bgColor||acc):'')
    +slider(t('posY'),'hooks.y',0.05,0.9,H.y==null?0.2:H.y,0.005)+slider(t('posX'),'hooks.x',0.1,0.9,H.x==null?0.5:H.x,0.005)
    +pick(t('entrance'),'hooks.anim',ANIMS.filter(x=>x!=='glow').map(x=>[x,t('an_'+x)]),H.anim||'pop')+slider(t('duration'),'hooks.dur',0.8,8,H.dur||2.6,0.1)
    +'<p class="hint">'+t('hookDrag')+'</p></div>';
  return o; }
function hookVisibleAt(y){ const H=ST&&hs().hooks; if(!H||!H.on||T>=(H.dur||2.6)) return false; const it=(H.items||[])[H.active||0]; return !!(it&&it.text)&&Math.abs(y-(H.y==null?0.2:H.y))<0.12; }
$('#wrap').addEventListener('pointerdown',e=>{ if(PICK||!ST||TOOL!=='select'||e.target.closest('#giz,#drawCv,#drawBar')) return; const r=$('#wrap').getBoundingClientRect(), y=(e.clientY-r.top)/r.height;
  if(hookVisibleAt(y)){ if(playing) stop(); select({kind:'hook',id:0}); placeGiz(); return; }
  if(playing) stop(); select({kind:'vxf',id:0}); RTAB='sel'; markTabs(); renderRight(); placeGiz(); });   // 4.31: ضغطة على الفيديو تحدده: تسحبه وتكبّره
$('#body').addEventListener('input',e=>{ const el=e.target; if(el.dataset.hk!==undefined&&SEL&&SEL.kind==='hook'){ const H=hs().hooks, i=+el.dataset.hk; while(H.items.length<=i) H.items.push({text:''}); if(!el._sn){ snap(); el._sn=1; setTimeout(()=>el._sn=0,1200); } H.items[i].text=el.value; live(); buildTL(); }
  if(el.dataset.k==='hooks.dur') buildTL(); });
$('#body').addEventListener('change',e=>{ const el=e.target; if(el.dataset.hkact!==undefined&&SEL&&SEL.kind==='hook'){ snap(); hs().hooks.active=+el.dataset.hkact; live(); buildTL(); if(T>=(hs().hooks.dur||2.6)) seek(0.4); } });
document.addEventListener('click',e=>{ if(e.target.id!=='hkOff') return; snap(); hs().hooks.on=false; SEL=null; live(); buildTL(); renderRight(); placeGiz(); toast(t('hookOffDone')); });

/* ───── 4.20: الأقسام تكبر وتصغر بالسحب من طرفها، وتنحفظ على جهازك ───── */
(function(){ if(document.body.classList.contains('m')) return; const B=document.body, num=k=>{ try{ return +localStorage.getItem(k)||0; }catch(e){ return 0; } };
  const apply=()=>{ const bw=num('hs.binw'), pw=num('hs.panw'); bw?B.style.setProperty('--binw',bw+'px'):B.style.removeProperty('--binw'); pw?B.style.setProperty('--panw',pw+'px'):B.style.removeProperty('--panw'); B.classList.toggle('cw',!!(bw||pw)); };
  apply();
  const mk=(side,key,cssv,edge,min,max)=>{ const g=document.createElement('div'); g.className='colgrip '+edge; g.title=t('colGrip'); $(side).appendChild(g); let on=null;
    g.addEventListener('pointerdown',e=>{ e.preventDefault(); on={x:e.clientX,w:$(side).getBoundingClientRect().width}; g.setPointerCapture(e.pointerId); g.classList.add('on');
      for(const [s2,v2] of [['#bin','--binw'],['#panel','--panw']]){ const w2=$(s2).getBoundingClientRect().width; if(!B.style.getPropertyValue(v2)&&w2>0) B.style.setProperty(v2,Math.round(w2)+'px'); } B.classList.add('cw'); });
    g.addEventListener('pointermove',e=>{ if(!on) return; const d=edge==='r'?e.clientX-on.x:on.x-e.clientX; B.style.setProperty(cssv,Math.round(clamp(on.w+d,min,max))+'px'); dispatchEvent(new Event('resize')); });
    const end=()=>{ if(!on) return; on=null; g.classList.remove('on'); try{ for(const [k2,v2] of [['hs.binw','--binw'],['hs.panw','--panw']]){ const w2=parseInt(B.style.getPropertyValue(v2)); if(w2) localStorage.setItem(k2,w2); } }catch(e){} };
    g.addEventListener('pointerup',end); g.addEventListener('pointercancel',end);
    g.addEventListener('dblclick',()=>{ try{ localStorage.removeItem(key); }catch(e){} apply(); dispatchEvent(new Event('resize')); }); };
  mk('#bin','hs.binw','--binw','r',220,600); mk('#panel','hs.panw','--panw','l',300,680); })();

/* ───── 4.20: ربط النصوص باللقطة: لو حذفت جزء قبلها تمشي معه (زر للكل، ومفتاح لكل نص) ───── */
const pinAll=()=>hs().pinLayers!==false;
function layerPinned(L){ return L.pin!=null?!!L.pin:pinAll(); }
function pinMark(){ const b=$('#bPin'); if(b&&ST) b.classList.toggle('on',pinAll()); }
document.addEventListener('click',e=>{ if(!ST) return;
  if(e.target.closest('#bPin')){ snap(); const h=hs(); h.pinLayers=!pinAll(); (h.layers||[]).forEach(L=>{ delete L.pin; }); pinMark(); buildTL(); renderRight(); live(); toast(t(h.pinLayers?'pinOnAll':'pinOffAll')); return; }
  if(e.target.id==='lPin') pinToggle(); });
function pinToggle(){ const L=selLayer(); if(!L) return; snap(); const v=!layerPinned(L); if(v===pinAll()) delete L.pin; else L.pin=v; buildTL(); renderRight(); live(); }

/* 4.20: وقت القص يتركّب (الصفحة لسه على النسخة القديمة) لا نحفظ ولا نتراجع، عشان ما نكتب القديم فوق القص */
function cutBusy(){ return !!(PULSE&&PULSE.job&&PULSE.job.running&&PULSE.job.kind==='remove'); }

/* ───── 4.21: تعلّق على المسافة يسرّع ×2 · S يقص عند المؤشر ───── */
let RATE=1, PLAY_REBASE=null, SPACE=null;
function setRate(r){ RATE=r; try{ AU.playbackRate=r; }catch(e){} if(PLAY_REBASE) PLAY_REBASE(); document.body.classList.toggle('fast',r>1); }
function spaceDown(e){ if(e.repeat||SPACE) return; SPACE={was:playing,held:false}; SPACE.tm=setTimeout(()=>{ if(!SPACE) return; SPACE.held=true; if(!playing) play(); setRate(2); },320); }
addEventListener('keyup',e=>{ if(e.code!=='Space'||!SPACE) return; e.preventDefault(); clearTimeout(SPACE.tm); const s=SPACE; SPACE=null; if(s.held){ setRate(1); if(!s.was&&playing) stop(); } else play(); });
addEventListener('blur',()=>{ if(SPACE){ clearTimeout(SPACE.tm); if(SPACE.held) setRate(1); SPACE=null; } });
function cutHere(){ if(!ST) return; if(playing) stop(); const x=r3(T);
  if(SEL&&(SEL.kind==='layer'||SEL.kind==='cap'||SEL.kind==='sfx'||SEL.kind==='broll')){ const el=document.querySelector('#lane .clip[data-kind="'+SEL.kind+'"][data-id="'+SEL.id+'"]'); if(el){ const o=SEL.kind==='sfx'?null:objOf(SEL.kind,SEL.id); if(!o||(x>o.s+0.05&&x<o.e-0.05)){ blade(el,x); return; } } }
  if(x<0.1||x>total()-0.1){ toast(t('cutEdge')); return; }
  if(MARKS.some(q=>Math.abs(q-x)<0.05)){ toast(t('cutDup')); return; }
  MARKS.push(x); MARKS.sort((a,b)=>a-b); marksSave(); buildTL(); toast(t('cutDone',fmt(x))); }
document.addEventListener('click',e=>{ if(e.target.closest('#bCutHere')) cutHere(); });

/* ───── 4.21: كليك يمين: يحدد اللي تحته وينقل المؤشر له ويطلّع خياراته ───── */
function ctxClose(){ const c=$('#ctx'); c.classList.remove('on'); c.innerHTML=''; }
function ctxOpen(x,y,title,items){ const c=$('#ctx'); CTX=items.filter(Boolean);
  c.innerHTML=(title?'<div class="ttl">'+esc(title)+'</div>':'')+CTX.map((it,i)=>it==='-'?'<hr>':'<button data-ctx="'+i+'" class="'+(it.bad?'bad':'')+'"><span>'+esc(it.l)+'</span>'+(it.k?'<kbd>'+it.k+'</kbd>':'')+'</button>').join('');
  c.classList.add('on'); const r=c.getBoundingClientRect(); c.style.left=Math.max(6,Math.min(x,innerWidth-r.width-6))+'px'; c.style.top=Math.max(6,Math.min(y,innerHeight-r.height-6))+'px'; }
let CTX=[];
function ctxItems(){ const cut={l:t('ctxCut'),k:'S',f:cutHere}, del={l:t('ctxDel'),k:'Del',f:delSel,bad:true}, it=[];
  const frz={l:t('ctxFreeze'),f:freezeHere};   // 4.36
  const slw={l:t('ctxSlow'),f:()=>slowOpen(SEL&&(SEL.kind==='video'||SEL.kind==='audio')?SEL.s:T,SEL&&(SEL.kind==='video'||SEL.kind==='audio')?SEL.e:null)};   // 4.45
  if(!SEL) return [cut,frz,slw,{l:t('ctxNote'),k:'M',f:openNote}];
  if(SEL.kind==='layer'){ const L=selLayer(); if(!L) return [cut];
    return [cut,{l:t('ctxSwap'),f:()=>swapNote(L.s,lname(L))},{l:t('duplicate'),k:'Ctrl+D',f:dupSel},{l:t(L.off?'ctxShow':'ctxHide'),f:()=>{ snap(); L.off=!L.off; if(!L.off) delete L.off; buildTL(); live(); renderRight(); }},{l:(layerPinned(L)?'✓ ':'')+t('ctxPin'),f:pinToggle},'-',{l:t('ctxAsk'),f:()=>{ if(uiMode()==='manual') askOpen(); else { RTAB='claude'; markTabs(); renderRight(); } }},'-',del]; }
  if(SEL.kind==='cap') return [cut,{l:t('ctxEditText'),f:()=>{ LTAB='text'; markTabs(); renderLeft(); const el=$('#lbody .card[data-card="'+SEL.id+'"]'); if(el){ el.scrollIntoView({block:'center'}); el.classList.add('on'); } }},'-',{l:t('ctxDelCap'),k:'Del',f:delSel,bad:true}];
  if(SEL.kind==='video'||SEL.kind==='audio'){ const s=SEL.s, e=SEL.e;
    return [cut,frz,slw,{l:t('ctxSwapShot'),f:()=>swapNote(s,fmt(s)+' ← '+fmt(e))},'-',{l:t('ctxDelShot'),f:()=>{ askRemove({ranges:[[r3(s),r3(e)]]},fmt(s)+' ← '+fmt(e)); },bad:true},{l:t('ctxDelPic'),f:()=>{ snap(); blankAdd(s,e); toast(t('delVideoDone')); }},{l:t('ctxDelAud'),f:()=>{ snap(); rngSet(s,e,0); toast(t('delAudioDone')); renderRight(); }}]; }
  if(SEL.kind==='sfx') return [cut,{l:t('ctxListen'),f:()=>{ const b=document.createElement('button'); b.dataset.sxplay='1'; audioClick(b); }},'-',del];
  if(SEL.kind==='hook') return [{l:t('hookOff'),f:delSel,bad:true}];
  if(SEL.kind==='broll'){ const b=objOf('broll',SEL.id); if(b) return [cut,{l:t('ctxSwap'),f:()=>swapNote(b.s,b.k)},'-',del]; }
  return [cut,del]; }
/* 4.36: تجميد اللقطة من مكان المؤشر (كليك يمين) */
/* 4.45: حركة بطيئة لجزء (Speed Warp): فريمات بينية حقيقية، تغطي الجزء بدون ما يتغيّر طول المقطع */
let SLW={r:0.5,mute:true};
function slowOpen(s,e){ s=Math.max(0,s); e=e!=null?e:Math.min(total()-0.1,s+2); if(e-s<0.4){ toast(t('slowShort')); return; } e=Math.min(e,s+6); SLW.s=s; SLW.e=e;
  modal('<h3>'+t('slowT')+'</h3><p class="hint">'+t('slowSub')+'</p><div class="row"><label>'+t('slowRange')+'</label><span dir="ltr">'+fmt(s)+' ← '+fmt(e)+'</span></div>'
    +'<div class="row"><label>'+t('slowLen')+'</label><input type="range" id="slwLen" min="0.4" max="6" step="0.1" value="'+(e-s).toFixed(1)+'"><span class="val" id="slwLenV">'+(e-s).toFixed(1)+'</span></div>'
    +'<div class="row"><label>'+t('slowSpeed')+'</label><div class="seg">'+[[0.5,'½'],[0.33,'⅓'],[0.25,'¼']].map(([r,l])=>'<button data-slwr="'+r+'" class="'+(SLW.r===r?'on':'')+'">'+l+'</button>').join('')+'</div></div>'
    +'<label class="item"><input type="checkbox" id="slwMute"'+(SLW.mute?' checked':'')+'><span>'+t('slowMute')+'</span></label><p class="hint">'+t('slowHint')+'</p>'
    +'<div class="row" style="margin-top:10px"><button class="pri" id="slwGo">'+t('slowGo')+'</button><button id="slwX">'+t('cancel')+'</button></div>'); }
document.addEventListener('input',e=>{ if(e.target.id!=='slwLen') return; SLW.e=Math.min(total()-0.05,SLW.s+(+e.target.value)); $('#slwLenV').textContent=(+e.target.value).toFixed(1); });
document.addEventListener('click',async e=>{ const b=e.target.closest('[data-slwr],#slwGo,#slwX'); if(!b) return;
  if(b.dataset.slwr){ SLW.r=+b.dataset.slwr; $$('[data-slwr]').forEach(x=>x.classList.toggle('on',x===b)); return; }
  if(b.id==='slwX'){ closeModal(); return; }
  SLW.mute=!!($('#slwMute')||{}).checked; closeModal(); await save(); const r=await api('/hs/slowmo',{s:r3(SLW.s),e:r3(SLW.e),r:SLW.r,mute:SLW.mute}); if(!r.ok){ toast(srvEn(r.msg)||t('busyJob')); return; }
  stLoader('rebuild',t('slowWorking')); pollJob(async p=>{ try{ await load(true); if(!p.err) toast(t('slowDone')); } finally{ stLoaderHide(); } }); });
/* 4.46: مكان مؤقت بالتايم لاين وشارة فوق المعاينة وقت تجهيز عنصر (موقع، صورة…)، والباقي يشتغل */
function ghostAdd(s,d,label){ const g=document.createElement('div'); g.className='clip ghost'; g.style.cssText='left:'+(s*PX)+'px;width:'+Math.max(24,d*PX)+'px;top:0;position:absolute'; g.innerHTML='<span>'+esc(label)+'</span>'; const row=$('#tLs .lrow:last-child')||$('#tLs'); row.appendChild(g);
  let w=$('#workb2'); if(!w){ w=document.createElement('div'); w.id='workb2'; $('#stage').appendChild(w); } w.innerHTML='<i></i><span>'+esc(label)+'</span>'; return g; }
function ghostDone(g){ if(g) g.remove(); const w=$('#workb2'); if(w) w.remove(); }
function freezeHere(){ if(T>=total()-0.3){ toast(t('frzEnd')); return; } SEL=null; addLayer({type:'mg',kind:'freeze',track:1,...DF('mg','freeze')}); toast(t('frzAdded')); }
function ctxTitle(){ if(!SEL) return fmt(T); if(SEL.kind==='layer'){ const L=selLayer(); return L?lname(L):''; } if(SEL.kind==='cap') return key(ST.caps.cards[+SEL.id]||{w:[]}); if(SEL.kind==='video'||SEL.kind==='audio') return fmt(SEL.s)+' ← '+fmt(SEL.e); if(SEL.kind==='hook') return t('hookClip'); return ''; }
$('#scroller').addEventListener('contextmenu',e=>{ if(!ST) return; e.preventDefault(); if(playing) stop(); const x=tlTime(e), el=e.target.closest('.clip[data-kind]');
  if(el){ const kind=el.dataset.kind, id=(kind==='layer'||kind==='sfx')?el.dataset.id:+el.dataset.id; select({kind,id}); }
  else if(e.target.closest('#tFilm,#tAu')){ const au=!!e.target.closest('#tAu'), b=shotBounds(); for(let i=0;i<b.length-1;i++){ if(x>=b[i]&&x<b[i+1]){ select({kind:au?'audio':'video',s:b[i],e:b[i+1],id:i,solo:!LINK}); break; } } }
  else if(SEL){ SEL=null; buildTL(); renderRight(); }
  seek(x); ctxOpen(e.clientX,e.clientY,ctxTitle(),ctxItems()); });
$('#wrap').addEventListener('contextmenu',e=>{ if(!ST) return; e.preventDefault(); if(playing) stop(); const r=$('#wrap').getBoundingClientRect(), y=(e.clientY-r.top)/r.height; if(hookVisibleAt(y)) select({kind:'hook',id:0});
  ctxOpen(e.clientX,e.clientY,fmt(T),[{l:t('ctxNote'),k:'M',f:openNote},{l:t('ctxCover'),f:coverShot},{l:t('ctxCut'),k:'S',f:cutHere},...(SEL&&SEL.kind==='hook'?['-',{l:t('hookOff'),f:delSel,bad:true}]:[])]); });
document.addEventListener('pointerdown',e=>{ if(!e.target.closest('#ctx')) ctxClose(); },true);
document.addEventListener('click',e=>{ const b=e.target.closest('#ctx [data-ctx]'); if(!b) return; const it=CTX[+b.dataset.ctx]; ctxClose(); if(it&&it.f) it.f(); });
addEventListener('keydown',e=>{ if(e.key==='Escape') ctxClose(); }); addEventListener('resize',ctxClose); $('#scroller').addEventListener('scroll',ctxClose);

/* ───── 4.23: القص الفوري: الفيديو الحالي مبني من قص أقدم، فالمعاينة تحسب كل وقت بمكانه فيه وتتخطّى المقصوص ───── */
const VM=()=>(INFO&&INFO.vmap&&INFO.vmap.length)?INFO.vmap:null;
function vm(t){ const M=VM(); if(!M) return t; let lo=0, hi=M.length-1; while(lo<hi){ const m=(lo+hi)>>1; if(t<M[m][1]) hi=m; else lo=m+1; } const s=M[lo]; return s[2]+Math.max(0,t-s[0]); }
function vmInv(o){ const M=VM(); if(!M) return o; for(const s of M){ const L=s[1]-s[0]; if(o>=s[2]-1e-3&&o<s[2]+L-0.012) return s[0]+(o-s[2]); } return null; }
function vmNext(o){ const M=VM(); if(!M) return null; for(const s of M){ if(s[2]>o-1e-3) return s; } return null; }

function vmSegAt(t){ const M=VM(); if(!M) return -1; let lo=0, hi=M.length-1; while(lo<hi){ const m=(lo+hi)>>1; if(t<M[m][1]) hi=m; else lo=m+1; } return lo; }
/* ───── 4.23: تسحب اللقطة المحددة وتحطها مكان ثاني ───── */
let MV=null;
function mvMark(x){ let m=$('#mvMark'); if(!m){ m=document.createElement('div'); m.id='mvMark'; $('#lane').appendChild(m); } if(x==null){ m.style.display='none'; return; } m.style.display='block'; m.style.left=(x*PX)+'px'; }
function mvGhost(s,e,x0,x){ let g=$('#mvGhost'); if(!g){ g=document.createElement('div'); g.id='mvGhost'; $('#tFilm').appendChild(g); } if(s==null){ g.style.display='none'; return; } g.style.display='block'; g.style.left=((s+(x-x0))*PX)+'px'; g.style.width=((e-s)*PX)+'px'; }
async function moveShot(s,e,to){ await save(); const r=await api('/hs/move_shot',{s:r3(s),e:r3(e),to:r3(to)}); if(!r||!r.ok){ toast(r&&srvEn(r.msg)?srvEn(r.msg):t('failed')); return; }
  if(r.rebuild){ stLoader('rebuild',t('rebuildSub')); pollJob(async()=>{ try{ await load(true); } finally{ stLoaderHide(); } }); return; }
  SEL=null; MARKS=[]; await reloadLite(); seek(r.to||0); toast(t('shotMoved')); }

/* 4.23: قص طرف اللقطة مباشرة: قرّب من الحد بين لقطتين والمؤشر يتغيّر، واسحب. ويطلع لك كم بتقص وأنت تسحب */
function edgeNear(x,tg){ if(!ST||(tg&&tg.closest&&tg.closest('.cutbtn,.blk,.clip,#tAu'))) return null; const b=shotBounds(), tol=7/PX;
  for(let i=1;i<b.length;i++){ const v=b[i]; if(Math.abs(v-x)>tol) continue; if(x<v&&i>=1) return {side:'r',s:b[i-1],e:v,i:i-1}; if(i<b.length-1) return {side:'l',s:v,e:b[i+1],i}; if(i>=1) return {side:'r',s:b[i-1],e:v,i:i-1}; }
  if(Math.abs(x)<tol&&b.length>1) return {side:'l',s:b[0],e:b[1],i:0}; return null; }
function trimBadge(cx,cy,d){ let g=$('#trimBadge'); if(!g){ g=document.createElement('div'); g.id='trimBadge'; document.body.appendChild(g); } if(cx==null||d<0.02){ g.style.display='none'; return; } g.style.display='block'; g.textContent='−'+d.toFixed(2)+(LANG==='ar'?' ث':'s'); g.style.left=(cx+14)+'px'; g.style.top=(cy-34)+'px'; }

/* ───── 4.25: تحسين الجودة: تختار المستوى، تقارن قبل وبعد على نفس اللقطة، وتطبّق ───── */
let QLV=null;
/* ═══ 4.44: أدوات احترافية مثل DaVinci وAfter Effects وPremiere: إضاءة موضعية، تلوين دقيق لكل لون، تنعيم البشرة، إزالة عنصر ثابت، واكتشاف القطعات ═══ */
let FIXD=null, FXC='r', ERD=null;
const fixCur=()=>{ if(!FIXD) FIXD=JSON.parse(JSON.stringify(hs().fix||{})); FIXD.warp=FIXD.warp||{}; FIXD.erase=FIXD.erase||[]; return FIXD; };
function proSec(h){ const W=h.win||{}, F=fixCur(), cw=F.warp[FXC]||{}, dirtyFix=JSON.stringify(F)!==JSON.stringify({warp:{},erase:[],...(h.fix||{})});
  let o='<div class="sec pro"><h4>'+t('proT')+'</h4><p class="hint" style="margin-top:0">'+t('proSub')+'</p>';
  o+='<h5>'+t('winT')+'</h5>'+tog('win.on',t('winOn'),t('winSub'),!!W.on);
  if(W.on) o+=tog('win.follow',t('winFollow'),'',!!W.follow)+(W.follow?'':slider(t('posX'),'win.x',0,1,W.x==null?0.5:W.x,0.01)+slider(t('posY'),'win.y',0,1,W.y==null?0.42:W.y,0.01))+slider(t('winSize'),'win.r',0.1,1,W.r==null?0.42:W.r,0.01)+slider(t('winSoft'),'win.f',0.05,0.95,W.f==null?0.45:W.f,0.01)
    +slider(t('winIn'),'win.in',-0.6,0.6,W.in==null?0.12:W.in,0.01)+slider(t('winOut'),'win.out',-0.9,0.6,W.out==null?-0.45:W.out,0.01)+tog('win.warm',t('winWarm'),'',!!W.warm);
  o+='<h5>'+t('warpT')+'</h5><div class="seg wcols">'+[['r','#e5484d'],['y','#e0b43a'],['g','#43b072'],['c','#3aa7a0'],['b','#4c8dff'],['m','#c05fd0']].map(([k,c])=>'<button data-fxc="'+k+'" class="'+(FXC===k?'on':'')+'"><i style="background:'+c+'"></i>'+t('wc_'+k)+((F.warp[k]&&(F.warp[k].h||F.warp[k].s||F.warp[k].l))?' •':'')+'</button>').join('')+'</div>'
    +'<div class="row"><label>'+t('warpHue')+'</label><input type="range" data-fxw="h" min="-60" max="60" step="1" value="'+(cw.h||0)+'"><span class="val">'+(cw.h||0)+'</span></div>'
    +'<div class="row"><label>'+t('warpSat')+'</label><input type="range" data-fxw="s" min="-1" max="1" step="0.05" value="'+(cw.s||0)+'"><span class="val">'+(cw.s||0)+'</span></div>'
    +'<div class="row"><label>'+t('warpLight')+'</label><input type="range" data-fxw="l" min="-0.5" max="0.5" step="0.02" value="'+(cw.l||0)+'"><span class="val">'+(cw.l||0)+'</span></div>';
  o+='<h5>'+t('skinT')+'</h5><div class="seg">'+[['off','qOff'],['light','skinL'],['strong','skinS']].map(([k,l])=>'<button data-fxskin="'+k+'" class="'+((F.skin||'off')===k?'on':'')+'">'+t(l)+'</button>').join('')+'</div>';
  o+='<h5>'+t('eraseT')+'</h5><p class="hint" style="margin-top:0">'+t('eraseHint')+'</p><div id="erBox" style="background-image:url('+frU(Math.max(1,Math.round(vm(T)*FPS)+1))+')">'+F.erase.map((r,i)=>'<i style="left:'+r.x*100+'%;top:'+r.y*100+'%;width:'+r.w*100+'%;height:'+r.h*100+'%"><b data-erdel="'+i+'">×</b></i>').join('')+(ERD?'<i class="new" style="left:'+ERD.x*100+'%;top:'+ERD.y*100+'%;width:'+ERD.w*100+'%;height:'+ERD.h*100+'%"></i>':'')+'</div>';
  o+='<div class="row" style="margin-top:8px;flex-wrap:wrap"><button class="sm" id="fxCmp">'+t('qCompare')+'</button><button class="pri sm" id="fxApply"'+(dirtyFix?'':' disabled')+'>'+t('fxApply')+'</button>'+(h.fix?'<button class="sm ghost" id="fxClear">'+t('fxClear')+'</button>':'')+'</div><div id="fxOut"></div>';
  o+='<h5>'+t('mbT')+'</h5>'+tog('mb.on',t('mbAll'),t('mbAllSub'),!!(h.mb&&h.mb.on));
  o+='<h5>'+t('scnT')+'</h5><div class="row"><button class="sm" id="scnGo">'+t('scnGo')+'</button></div><p class="hint">'+t('scnHint')+'</p></div>';
  return o; }
document.addEventListener('click',async e=>{ const b=e.target.closest('[data-fxc],[data-fxskin],[data-erdel],#fxCmp,#fxApply,#fxClear,#scnGo'); if(!b||!ST) return; const d=b.dataset, F=fixCur();
  if(d.fxc){ FXC=d.fxc; renderRight(); return; }
  if(d.fxskin){ F.skin=d.fxskin==='off'?undefined:d.fxskin; renderRight(); return; }
  if(d.erdel!=null){ e.stopPropagation(); F.erase.splice(+d.erdel,1); renderRight(); return; }
  if(b.id==='fxCmp'){ const out=$('#fxOut'); out.innerHTML='<p class="hint">'+t('qMaking')+'</p>'; const u='/hs/fix_preview?t='+T.toFixed(2)+'&fix='+encodeURIComponent(JSON.stringify(F))+'&v='+Date.now(); const im=new Image(); im.onload=()=>{ out.innerHTML='<p class="hint">'+t('qBeforeAfter')+'</p>'; im.style.width='100%'; im.style.borderRadius='8px'; out.appendChild(im); }; im.onerror=()=>{ out.innerHTML='<p class="hint">'+t('failed')+'</p>'; }; im.src=u; return; }
  if(b.id==='fxApply'||b.id==='fxClear'){ const body=b.id==='fxClear'?{}:F; for(const k in body.warp||{}){ const w=body.warp[k]; if(!w.h&&!w.s&&!w.l) delete body.warp[k]; } if(body.erase&&!body.erase.length) delete body.erase; if(body.warp&&!Object.keys(body.warp).length) delete body.warp;
    if(Object.keys(body).length) hs().fix=body; else delete hs().fix; await save(); const r=await api('/hs/fix',{fix:body}); if(!r.ok){ toast(srvEn(r.msg)||t('busyJob')); return; }
    stLoader('rebuild',t('fxWorking')); pollJob(async p=>{ try{ FIXD=null; await reloadLite(); if(!p.err) toast(t('fxDone')); } finally{ stLoaderHide(); renderRight(); } }); return; }
  if(b.id==='scnGo'){ b.disabled=true; b.textContent=t('scnBusy'); const r=await api('/hs/scenes',{}); b.disabled=false; if(!r||!r.ok){ toast((r&&srvEn(r.msg))||t('failed')); renderRight(); return; }
    snap(); const h=hs(); h.marks=[...new Set([...(h.marks||[]),...r.cuts])].sort((a,b)=>a-b); MARKS=h.marks.filter(m=>m>0.05&&m<total()-0.05); dirty(); buildTL(); renderRight(); toast(t('scnDone',r.cuts.length)); } });
document.addEventListener('input',e=>{ const k=e.target.dataset&&e.target.dataset.fxw; if(!k) return; const F=fixCur(); F.warp[FXC]=F.warp[FXC]||{}; F.warp[FXC][k]=+e.target.value; const v=e.target.parentNode.querySelector('.val'); if(v) v.textContent=e.target.value; const a=$('#fxApply'); if(a) a.disabled=false; });
let _erD=null;
document.addEventListener('pointerdown',e=>{ const b=e.target.closest('#erBox'); if(!b||e.target.dataset.erdel!=null) return; e.preventDefault(); b.setPointerCapture(e.pointerId); const B=b.getBoundingClientRect(); _erD={B,x0:(e.clientX-B.left)/B.width,y0:(e.clientY-B.top)/B.height}; });
document.addEventListener('pointermove',e=>{ if(!_erD) return; const {B,x0,y0}=_erD, x1=Math.max(0,Math.min(1,(e.clientX-B.left)/B.width)), y1=Math.max(0,Math.min(1,(e.clientY-B.top)/B.height)); ERD={x:Math.min(x0,x1),y:Math.min(y0,y1),w:Math.abs(x1-x0),h:Math.abs(y1-y0)};
  const b=$('#erBox'); let n=b&&b.querySelector('i.new'); if(b&&!n){ n=document.createElement('i'); n.className='new'; b.appendChild(n); } if(n) Object.assign(n.style,{left:ERD.x*100+'%',top:ERD.y*100+'%',width:ERD.w*100+'%',height:ERD.h*100+'%'}); });
document.addEventListener('pointerup',()=>{ if(!_erD) return; _erD=null; if(ERD&&ERD.w>0.015&&ERD.h>0.008){ const F=fixCur(); F.erase.push({x:+ERD.x.toFixed(4),y:+ERD.y.toFixed(4),w:+ERD.w.toFixed(4),h:+ERD.h.toFixed(4)}); } ERD=null; renderRight(); });
function qualitySec(h){ const cur=(h.enhance&&h.enhance.level)||'off', sel=QLV||cur;
  return '<div class="sec"><h4>'+t('qTitle')+'</h4><div class="seg" style="margin-bottom:8px">'+[['off',t('qOff')],['light',t('qLight')],['strong',t('qStrong')]].map(([k,l])=>'<button data-qlv="'+k+'" class="'+(sel===k?'on':'')+'">'+l+(cur===k?' ✓':'')+'</button>').join('')+'</div>'
    +'<div class="row"><button class="sm" id="qCmp">'+t('qCompare')+'</button><button class="pri sm" id="qApply"'+(sel===cur?' disabled':'')+'>'+t('qApply')+'</button></div><p class="hint">'+t('qHint')+'</p><div id="qOut"></div></div>'; }
document.addEventListener('click',async e=>{ const b=e.target.closest('[data-qlv],#qCmp,#qApply'); if(!b||!ST) return;
  if(b.dataset.qlv){ QLV=b.dataset.qlv; renderRight(); return; }
  if(b.id==='qCmp'){ const lv=(QLV&&QLV!=='off')?QLV:'light', o=$('#qOut'); if(o) o.innerHTML='<p class="hint">'+t('qWait')+'</p><img alt="" style="width:100%;border-radius:10px;margin-top:6px" src="/hs/quality_preview?t='+T.toFixed(2)+'&level='+lv+'&v='+Date.now()+'"><div class="row" style="justify-content:space-between;font-size:12px;color:var(--mut)"><span>'+t('qBefore')+'</span><span>'+t('qAfter',t(lv==='strong'?'qStrong':'qLight'))+'</span></div>'; return; }
  if(b.id==='qApply'){ const lv=QLV||'off'; hs().enhance={level:lv}; await save(); const r=await api('/hs/quality',{level:lv}); if(!r.ok){ toast(srvEn(r.msg)||t('busyJob')); return; } stLoader('rebuild',t('qWorking')); pollJob(async()=>{ try{ QLV=null; await reloadLite(); toast(t('qDone')); } finally{ stLoaderHide(); } }); } });

/* ───── 4.41: ألوان الآيفون (HDR): فيديو HDR يطلع باهت ورمادي بدون محوّل أبل، يتصلّح على جهازك بجدول ألوان قبل الكابشن والعناصر ───── */
let HLV=null, HINFO=undefined;
function hdrLine(I){ return '<div class="item"><span>'+t(I.washed?'hdrWashed':(I.kind&&I.on?'hdrFixed':(I.kind?'hdrOff':'hdrSdr')),t('hdrKind_'+(I.kind||'hlg')))+'</span>'+(I.washed?'<button class="sm" data-hdfix="1">'+t('hdrFix')+'</button>':'')+'</div>'; }
function hdrSec(h){ const cur=(h.hdr&&h.hdr.level)||'auto', sel=HLV||cur;
  if(HINFO===undefined){ HINFO=null; api('/hs/hdr_info').then(r=>{ HINFO=r||{}; if(RTAB==='proj') renderRight(); }).catch(()=>{}); }
  const I=HINFO&&HINFO.ok?HINFO:null;
  return '<div class="sec"><h4>'+t('hdrTitle')+'</h4>'+(I?hdrLine(I):'')+(I&&I.apple?'<p class="hint">'+t('hdrApple')+'</p>':'')+'<div class="seg" style="margin-bottom:8px">'+[['auto',t('hdrAuto')],['on',t('hdrOn')],['off',t('qOff')]].map(([k,l])=>'<button data-hdlv="'+k+'" class="'+(sel===k?'on':'')+'">'+l+(cur===k?' ✓':'')+'</button>').join('')+'</div>'
    +'<div class="row" style="flex-wrap:wrap"><button class="sm" id="hdCmp">'+t('qCompare')+'</button><button class="pri sm" id="hdApply"'+(sel===cur&&!(I&&I.washed)?' disabled':'')+'>'+t('qApply')+'</button></div><p class="hint">'+t('hdrHint')+'</p><div id="hdOut"></div></div>'; }
function hdrChk(c){ const H=c&&c.hdr; if(!H||!H.washed) return ''; return '<div class="sec"><h4>'+t('hdrTitle')+'</h4>'+hdrLine({washed:true,kind:H.kind})+'<p class="hint">'+t('hdrChkHint')+'</p></div>'; }
async function hdrApply(lv){ if(!ST) return; hs().hdr={level:lv}; await save(); const r=await api('/hs/hdr',{level:lv}); if(!r.ok){ toast(srvEn(r.msg)||t('busyJob')); return; }
  stLoader('rebuild',t('hdrWorking')); pollJob(async p=>{ try{ HLV=null; HINFO=undefined; await reloadLite(); if(!p.err) toast(t(lv==='off'?'hdrOffDone':'hdrDone')); refreshCheck(); } finally{ stLoaderHide(); } }); }
document.addEventListener('click',async e=>{ const b=e.target.closest('[data-hdlv],[data-hdfix],#hdCmp,#hdApply'); if(!b||!ST) return;
  if(b.dataset.hdlv){ HLV=b.dataset.hdlv; renderRight(); return; }
  if(b.dataset.hdfix){ HLV=null; hdrApply('auto'); return; }
  if(b.id==='hdCmp'){ const o=$('#hdOut'); if(!o) return; o.innerHTML='<p class="hint">'+t('hdrWait')+'</p>';
    const im=new Image(); im.style.cssText='width:100%;border-radius:10px;margin-top:6px;display:none';
    im.onload=()=>{ im.style.display=''; const w=o.querySelector('p'); if(w) w.remove(); };
    im.onerror=()=>{ o.innerHTML='<p class="hint">'+t('stbCmpFail')+'</p>'; };
    im.src='/hs/hdr_preview?t='+T.toFixed(2)+'&level=on&v='+Date.now(); o.appendChild(im);
    o.insertAdjacentHTML('beforeend','<div class="row" style="justify-content:space-between;font-size:12px;color:var(--mut);direction:ltr"><span>'+t('qBefore')+'</span><span>'+t('hdrAfter')+'</span></div>'); return; }
  if(b.id==='hdApply'){ hdrApply(HLV||((hs().hdr&&hs().hdr.level)||'auto')); } });
/* ───── 4.40: تثبيت الصورة: يفحص اهتزاز التصوير باليد ويثبّته قبل الكابشن والعناصر (vid.stab على جهازك) ───── */
let SLV=null, SINFO=undefined;
function stabLine(I,cur){ return '<div class="item"><span>'+t('stbShake_'+I.level,(+I.jitter).toFixed(1))+'</span>'+(I.level!=='ok'&&cur==='off'?'<button class="sm" data-stfix="'+I.level+'">'+t('stbFix_'+I.level)+'</button>':'')+'</div>'; }
function stabSec(h){ const cur=(h.stab&&h.stab.level)||'off', sel=SLV||cur;
  if(SINFO===undefined){ SINFO=null; api('/hs/stab_info').then(r=>{ SINFO=r||{}; if(RTAB==='proj') renderRight(); }).catch(()=>{}); }
  const I=SINFO&&SINFO.info, can=!SINFO||SINFO.can!==false;
  return '<div class="sec"><h4>'+t('stbTitle')+'</h4>'+(I?stabLine(I,cur):'')+'<div class="seg" style="margin-bottom:8px">'+[['off',t('qOff')],['light',t('qLight')],['strong',t('qStrong')]].map(([k,l])=>'<button data-stlv="'+k+'" class="'+(sel===k?'on':'')+'">'+l+(cur===k?' ✓':'')+'</button>').join('')+'</div>'
    +'<div class="row" style="flex-wrap:wrap">'+(can?'<button class="sm" id="stChk">'+t(I?'stbRecheck':'stbCheck')+'</button>':'')+'<button class="sm" id="stCmp">'+t('qCompare')+'</button><button class="pri sm" id="stApply"'+(sel===cur?' disabled':'')+'>'+t('qApply')+'</button></div><p class="hint">'+t(can?'stbHint':'stbHintNo')+'</p><div id="stOut"></div></div>'; }
function stabChk(c){ const S=c&&c.shake; if(!S||!S.level||S.level==='ok'||S.on!=='off') return ''; return '<div class="sec"><h4>'+t('stbTitle')+'</h4>'+stabLine(S,'off')+'<p class="hint">'+t('stbChkHint')+'</p></div>'; }
async function stabApply(lv){ if(!ST) return; hs().stab={level:lv}; await save(); const r=await api('/hs/stab',{level:lv}); if(!r.ok){ toast(srvEn(r.msg)||t('busyJob')); return; }
  stLoader('rebuild',t('stbWorking')); pollJob(async p=>{ try{ SLV=null; SINFO=undefined; await reloadLite(); if(!p.err) toast(t(lv==='off'?'stbOffDone':'stbDone')); refreshCheck(); } finally{ stLoaderHide(); } }); }
document.addEventListener('click',async e=>{ const b=e.target.closest('[data-stlv],[data-stfix],#stChk,#stCmp,#stApply'); if(!b||!ST) return;
  if(b.dataset.stlv){ SLV=b.dataset.stlv; renderRight(); return; }
  if(b.dataset.stfix){ SLV=null; stabApply(b.dataset.stfix); return; }
  if(b.id==='stChk'){ const r=await api('/hs/stab_check',{}); if(!r.ok){ toast(srvEn(r.msg)||t('busyJob')); return; } stLoader('rebuild',t('stbChecking'));
    pollJob(async p=>{ try{ const q=await api('/hs/stab_info'); SINFO=q||{}; if(!p.err&&q&&q.info) toast(t('stbShake_'+q.info.level,(+q.info.jitter).toFixed(1))); renderRight(); refreshCheck(); } finally{ stLoaderHide(); } }); return; }
  if(b.id==='stCmp'){ const lv=(SLV&&SLV!=='off')?SLV:((hs().stab&&hs().stab.level!=='off'&&hs().stab.level)||'light'), o=$('#stOut'); if(!o) return;
    o.innerHTML='<p class="hint">'+t('stbWait')+'</p>';
    const v=document.createElement('video'); v.muted=true; v.loop=true; v.autoplay=true; v.playsInline=true; v.style.cssText='width:100%;border-radius:10px;margin-top:6px;display:none';
    v.onloadeddata=()=>{ v.style.display=''; const w=o.querySelector('p'); if(w) w.remove(); v.play().catch(()=>{}); };
    v.onerror=()=>{ o.innerHTML='<p class="hint">'+t('stbCmpFail')+'</p>'; };
    v.src='/hs/stab_preview?t='+T.toFixed(2)+'&level='+lv+'&v='+Date.now(); o.appendChild(v);
    o.insertAdjacentHTML('beforeend','<div class="row" style="justify-content:space-between;font-size:12px;color:var(--mut);direction:ltr"><span>'+t('qBefore')+'</span><span>'+t('qAfter',t(lv==='strong'?'qStrong':'qLight'))+'</span></div>'); return; }
  if(b.id==='stApply'){ stabApply(SLV||'off'); } });

/* ───── 4.35: «ما عجبتني، خلّ Claude يبدّلها»: ملاحظة جاهزة عند وقتها، تزيد عليها ليش وتحفظها ───── */
async function swapNote(t0,label){ if(playing) stop(); seek(Math.max(0,+t0||0)+0.05); await new Promise(r=>setTimeout(r,250)); openNote(); const tx=$('#nTx'); if(tx){ tx.value=t('swapNoteTx',label); tx.focus(); tx.setSelectionRange(tx.value.length,tx.value.length); } }

/* ───── 4.32: الأقسام بأزرار فوق: تشوف قسم واحد بدل ما تنزل وتدوّر ───── */
const ELGROUPS=[['media',['binSearch','binGen','binClips','binImages']],['text',['binIntros','binHooks']],['mg',['binMg']],['viz',['binViz']],['cards',['binSplit']],['chars',['binChars']],['person',['binPerson']],
  ['fx',['binFx']],['trans',['binTrans']],['looks',['binLooks']],['marks',['binAnno','binMarks','binDraw']],['sfx',['binSfx']],['fonts',['binFonts']],['ideas',['binIdeas']]];
let SECG={}; try{ SECG=JSON.parse(localStorage.getItem('hs.secg')||'{}')||{}; }catch(e){}
function secTabs(B,key,groups){ const secs=[...B.children].filter(e=>e.classList&&e.classList.contains('sec')); if(secs.length<4) return;
  const head=e=>{ const h=e.querySelector(':scope>h4'); if(!h) return ''; let s=''; for(const n of h.childNodes){ if(n.nodeType===3) s+=n.textContent; else if(n.tagName==='SPAN'&&!n.classList.contains('st')) s+=n.textContent; else break; } return s.trim(); };
  let G=[];
  if(groups){ const lab={}; groups.forEach(([id,ks])=>ks.forEach(k=>lab[t(k)]=id)); const by={};
    secs.forEach(e=>{ const id=lab[head(e)]||'other'; (by[id]=by[id]||[]).push(e); }); G=[...groups.map(g=>g[0]),'other'].filter(id=>by[id]).map(id=>({id,label:id==='other'?t('sgOther'):t('sg_'+id),els:by[id]})); }
  else { secs.forEach((e,i)=>{ const h=head(e); if(!h) return; G.push({id:'s'+i+':'+h.slice(0,24),label:h,els:[e]}); }); const loose=secs.filter(e=>!head(e)); if(loose.length&&G.length) G[0].els.unshift(...loose); }
  if(G.length<3) return; let cur=SECG[key]; if(!G.some(g=>g.id===cur)) cur=G[0].id;
  G.forEach(g=>g.els.forEach(e=>e.style.display=g.id===cur?'':'none'));
  const bar=document.createElement('div'); bar.className='secbar'; bar.innerHTML=G.map(g=>'<button data-secg="'+esc(g.id)+'" class="'+(g.id===cur?'on':'')+'">'+esc(g.label)+'</button>').join(''); bar.dataset.key=key;
  secs[0].parentNode.insertBefore(bar,secs[0]); const on=bar.querySelector('.on'); if(on) on.scrollIntoView({block:'nearest',inline:'center'});
  bar.addEventListener('wheel',ev=>{ if(Math.abs(ev.deltaY)>Math.abs(ev.deltaX)){ bar.scrollLeft-=ev.deltaY; ev.preventDefault(); } },{passive:false}); }
document.addEventListener('click',e=>{ const b=e.target.closest('[data-secg]'); if(!b) return; const bar=b.closest('.secbar'); SECG[bar.dataset.key]=b.dataset.secg; try{ localStorage.setItem('hs.secg',JSON.stringify(SECG)); }catch(err){}
  if(bar.dataset.key.startsWith('L:')) renderLeft(); else renderRight(); });

/* ───── 4.31: الفيديو نفسه: تحدده بضغطة على المعاينة، تسحبه لأي جهة، والعجلة تكبّر وتصغّر ───── */
function vxfPanel(){ const V=hs().vxf||(hs().vxf={x:0,y:0,s:1});
  return '<div class="sec"><h4>'+t('vxfTitle')+'</h4><p class="hint">'+t('vxfHint')+'</p>'+slider(t('size'),'vxf.s',0.5,3,+V.s||1,0.01)+slider(t('vxfX'),'vxf.x',-1080,1080,+V.x||0,1)+slider(t('vxfY'),'vxf.y',-1920,1920,+V.y||0,1)
    +'<div class="row"><button class="sm" data-vxf="reset">'+t('vxfReset')+'</button></div></div>'; }
document.addEventListener('click',e=>{ const b=e.target.closest('[data-vxf]'); if(!b||!ST) return; snap(); const h=hs();
  h.vxf={x:0,y:0,s:1};
  renderRight(); placeGiz(); live(); });
$('#wrap').addEventListener('wheel',e=>{ if(!ST||!SEL||SEL.kind!=='vxf') return; e.preventDefault(); const V=hs().vxf||(hs().vxf={}); V.s=r3(clamp((+V.s||1)*(e.deltaY<0?1.05:1/1.05),0.5,3)); const w=F.contentWindow; if(w&&w.hsSet) w.hsSet(ST.studio.hs); if(w&&w.draw) w.draw(T); dirty(); clearTimeout(window._vxT); window._vxT=setTimeout(()=>renderRight(),250); },{passive:false});

/* ───── 4.29: ملاحظة «لازم تعدّلها»: «روح لها» يوقفك عند الكلمة ويفتحها للتعديل ───── */
document.addEventListener('click',e=>{ const b=e.target.closest('[data-fixgo]'); if(!b||!ST) return; const n=(NOTES||[]).find(x=>String(x.id)===b.dataset.fixgo); if(!n) return;
  seek(n.t); if(n.card!=null&&ST.caps.cards[n.card]){ select({kind:'cap',id:n.card}); } });

/* ───── 4.29: شريط التقدّم: تطفيه أو تغيّر لونه ومكانه وسماكته ───── */
function barSec(h){ const B=h.bar||(h.bar={}); if(B.on==null) B.on=!(h.pod&&h.pod.on&&!h.pod.bar);
  return '<div class="sec"><h4>'+t('barTitle')+'</h4>'+tog('bar.on',t('barOn'),t('barOnSub'),B.on)
    +(B.on?swatches(t('color'),'bar.color',B.color||lookAccOf(h)||'#D97757')+slider(t('posY'),'bar.y',3,97,B.y==null?77.7:B.y,0.5)+slider(t('barH'),'bar.h',2,24,B.h||7,1)+seg(t('barW'),'bar.full',[[false,t('barInset')],[true,t('barFull')]],!!B.full):'')+'</div>'; }

/* ───── 4.28: صور «صور كثيرة»: تضغط الصورة تدخل أو تطلع ───── */
document.addEventListener('click',e=>{ const b=e.target.closest('[data-mgimg]'); if(!b||!ST) return; const L=selLayer(); if(!L||L.type!=='mg') return; snap();
  const src=b.dataset.mgimg, it=(L.items||[]).filter(x=>x&&x.src); const i=it.findIndex(x=>x.src===src); if(i>=0) it.splice(i,1); else it.push({src}); L.items=it;
  const w=F.contentWindow; Promise.resolve(w&&w.__hsLoadImg?w.__hsLoadImg(src):0).then(()=>{ renderRight(); live(); }); });

/* ───── 4.27: قوالب الكابشن مع الاسم: كل قالب يغيّر شكل الكابشن وصندوق الاسم مع بعض. الاسم طبقة نص عادية تحركها وتعدّلها ───── */
const TPLS={
  talk:{cap:{font:'Cairo',weight:800,size:56,color:'#FFFFFF',active:'#F5A524',bg:'none',shadow:true,stroke:0,hl:'color',lines:2,width:760,y:74,enter:'fade'},name:{bg:'box',bgColor:'#1E1915',bgOpacity:0.88,color:'#FFFFFF',x:0.74,y:0.088,size:44}},
  box:{cap:{font:'Cairo',weight:800,size:52,color:'#FFFFFF',active:'#FFD21F',bg:'box',bgColor:'#000000',bgOpacity:0.7,shadow:false,stroke:0,hl:'color',lines:2,width:760,y:76,enter:'fade'},name:{bg:'box',bgColor:'#F5A524',bgOpacity:1,color:'#141413',x:0.26,y:0.088,size:42}},
  paper:{cap:{font:'Cairo',weight:800,size:50,color:'#141413',active:'#D97757',bg:'box',bgColor:'#FAF9F5',bgOpacity:0.95,shadow:false,stroke:0,hl:'color',lines:2,width:760,y:76,enter:'fade'},name:{bg:'box',bgColor:'#141413',bgOpacity:0.92,color:'#FAF9F5',x:0.5,y:0.088,size:42}},
  bold:{cap:{font:'Cairo',weight:900,size:62,color:'#FFFFFF',active:'#FFD21F',bg:'none',shadow:true,stroke:5,strokeColor:'#000000',hl:'color',lines:2,width:800,y:72,enter:'pop'},name:{bg:'box',bgColor:'#FFD21F',bgOpacity:1,color:'#141413',x:0.74,y:0.088,size:46}},
  soft:{cap:{font:'IBM Plex Sans Arabic',weight:700,size:50,color:'#FFFFFF',active:'#8FD3FF',bg:'none',shadow:true,stroke:0,hl:'color',lines:2,width:760,y:76,enter:'fade'},name:{bg:'glass',color:'#FFFFFF',x:0.5,y:0.09,size:40}},
  low:{cap:{font:'Tajawal',weight:800,size:54,color:'#FFFFFF',active:'#43D17A',bg:'none',shadow:true,stroke:0,hl:'color',lines:2,width:760,y:80,enter:'rise'},name:{bg:'box',bgColor:'#43D17A',bgOpacity:1,color:'#0E1A12',x:0.5,y:0.66,size:40}} };
function tplTile(k){ const T_=TPLS[k], c=T_.cap, n=T_.name, on=(hs().cap.font===c.font&&hs().cap.active===c.active&&+hs().cap.y===c.y);
  const nb=n.bg==='glass'?'background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.45)':'background:'+(n.bgColor||'#000');
  const nx=n.x<0.4?'left:8%':n.x>0.6?'right:8%':'left:50%;transform:translateX(-50%)';
  const cb=c.bg==='box'?'background:'+c.bgColor+';padding:2px 5px;border-radius:4px;':'';
  return '<div class="tile tplt'+(on?' sel':'')+'" data-tpl="'+k+'"><div class="pv" dir="rtl" style="padding:0;background:linear-gradient(160deg,#4a4038,#1d1a17);font-family:\''+c.font+'\';overflow:hidden">'
    +'<i style="font-style:normal;position:absolute;top:'+(n.y*100)+'%;'+nx+';'+nb+';color:'+n.color+';font:800 9px Cairo;padding:2px 5px;border-radius:4px;white-space:nowrap">'+t('nameDef')+'</i>'
    +'<i style="font-style:normal;position:absolute;top:'+(c.y-12)+'%;left:8%;right:8%;text-align:center;font-weight:'+c.weight+';font-size:10px;line-height:1.5;color:'+c.color+';'+(c.shadow&&c.bg!=='box'?'text-shadow:0 1px 3px #000;':'')+'"><b style="font-weight:inherit;'+cb+'">'+(LANG==='en'?'Some <b style="font-weight:inherit;color:'+c.active+'">key</b> words':'كلام <b style="font-weight:inherit;color:'+c.active+'">مهم</b> هنا')+'</b></i></div><span>'+t('tpl_'+k)+'</span></div>'; }
function tplSec(h){ return '<div class="sec"><h4>'+t('tplTitle')+'</h4><div class="grid3">'+Object.keys(TPLS).map(tplTile).join('')+'</div><p class="hint">'+t('tplHint')+'</p></div>'; }
function tplApply(k){ const T_=TPLS[k], h=hs(); snap(); Object.assign(h.cap,{...CAPRESET,...T_.cap,on:true});
  let L=h.layers.find(l=>l.auto==='name');
  if(!L){ const id='L'+(Math.max(0,...h.layers.map(l=>parseInt(String(l.id).replace(/\D/g,''))||0))+1); L={id,type:'text',s:0,e:r3(total()),track:3,anim:'fade',auto:'name',text:(h.pod&&h.pod.speaker)||t('nameDef')}; h.layers.push(L); }
  ['bg','bgColor','bgOpacity','x','y','size'].forEach(f=>delete L[f]); Object.assign(L,{font:'Cairo',weight:800,...T_.name});
  if(h.pod&&h.pod.on) h.pod.titleOn=false;
  select({kind:'layer',id:L.id}); live(); renderRight(); if(L.text===t('nameDef')) toast(t('tplName')); }
document.addEventListener('click',e=>{ const b=e.target.closest('[data-tpl]'); if(!b||!ST) return; tplApply(b.dataset.tpl); });

/* ───── 4.27: مكان الفيديو بالكادر: الصورة الأصلية كاملة ومربع تسحبه وتكبّر، ثم يتقص الفيديو من الأصل على مكانك ───── */
let VPI=null, VPD=null, _vpL=0;
function vpLoad(){ if(Date.now()-_vpL<3000) return; _vpL=Date.now(); api('/hs/vpos_info').then(r=>{ VPI=r; if(RTAB==='proj') renderRight(); }).catch(()=>{}); }
function vpCur(){ const f=VPD||(VPI&&VPI.vpos)||{}, au=VPI&&VPI.auto&&VPI.auto.length?VPI.auto[0]:0.5; return {x:f.x==null?au:f.x, y:f.y==null?0.3:f.y, z:f.z||1, still:!!f.still, auto:f.x==null}; }
function vpRect(){ const I=VPI, c=vpCur(), rw=(I.wide?Math.min(1,(I.sh*9/16)/I.sw):1)/c.z, rh=1/c.z; return {l:Math.max(0,Math.min(1-rw,c.x-rw/2)), t:(1-rh)*c.y, w:rw, h:rh}; }
function vpDraw(){ const r=$('#vpRect'); if(!r) return; const R=vpRect(); Object.assign(r.style,{left:R.l*100+'%',top:R.t*100+'%',width:R.w*100+'%',height:R.h*100+'%'}); const a=$('#vpApply'); if(a) a.disabled=!VPD; }
document.addEventListener('click',async e=>{ const b=e.target.closest('#mfitGo,#mfitOff'); if(!b||!ST) return; if(MUP){ MUP.pause(); MUP=null; }
  if(b.id==='mfitOff'){ await api('/hs/music_fit',{off:true}); delete hs().mix.fit; renderRight(); toast(t('mfitOffDone')); return; }
  b.disabled=true; b.textContent=t('mfitBusy'); await save(); const r=await api('/hs/music_fit',{}); b.disabled=false;
  if(!r||!r.ok){ toast((r&&srvEn(r.msg))||t('failed')); renderRight(); return; } const st=await api('/api/state'); hs().mix.fit=((st.studio||{}).hs||{}).mix&&st.studio.hs.mix.fit||{D:r.target}; renderRight(); toast(t('mfitDone',r.dur)); });
function vposSec(){ vpLoad(); const I=VPI; if(!I||!I.can) return ''; const c=vpCur(), R=vpRect(), box=I.wide?'width:100%':'height:280px;width:'+Math.round(280*I.sw/I.sh)+'px';
  return '<div class="sec"><h4>'+t('vpTitle')+(c.auto&&!VPD?' <span class="st">'+t('vpAutoOn')+'</span>':'')+'</h4>'
    +'<div id="vpBox" style="position:relative;'+box+';aspect-ratio:'+I.sw+'/'+I.sh+';margin:0 auto 8px;border-radius:10px;overflow:hidden;background:#000 url(/hs/vpos_thumb?t='+T.toFixed(1)+') center/100% 100% no-repeat;touch-action:none;cursor:grab">'
    +'<div id="vpRect" style="position:absolute;left:'+R.l*100+'%;top:'+R.t*100+'%;width:'+R.w*100+'%;height:'+R.h*100+'%;border:2px solid #D97757;box-shadow:0 0 0 999px rgba(0,0,0,.55);border-radius:3px;pointer-events:none"></div></div>'
    +'<div class="row"><label>'+t('vpZoom')+'</label><input type="range" id="vpZ" min="100" max="250" value="'+Math.round(c.z*100)+'" style="flex:1"></div>'
    +'<label class="item"><input type="checkbox" id="vpStill"'+(c.still?' checked':'')+'><span>'+t('vpStill')+'</span></label>'
    +'<div class="row"><button class="sm" id="vpAuto">'+t(I.wide?'vpAuto':'vpReset')+'</button>'+(I.wide?'<button class="pri sm" id="vpApply"'+(VPD?'':' disabled')+'>'+t('vpApply')+'</button>':'')+'</div><p class="hint">'+t(I.wide?'vpHint':'vpHintLive')+'</p></div>'; }
let _vpDrag=null;
document.addEventListener('pointerdown',e=>{ const b=e.target.closest('#vpBox'); if(!b||!VPI) return; e.preventDefault(); b.setPointerCapture(e.pointerId); const B=b.getBoundingClientRect(), R=vpRect();
  const px=(e.clientX-B.left)/B.width, py=(e.clientY-B.top)/B.height, inside=px>=R.l&&px<=R.l+R.w&&py>=R.t&&py<=R.t+R.h;
  _vpDrag={B, ox:inside?px-(R.l+R.w/2):0, oy:inside?py-(R.t+R.h/2):0}; vpMove(e); });
function vpMove(e){ if(!_vpDrag) return; const {B,ox,oy}=_vpDrag, c=vpCur(), R=vpRect(); const cx=(e.clientX-B.left)/B.width-ox, cy=(e.clientY-B.top)/B.height-oy;
  const x=Math.max(R.w/2,Math.min(1-R.w/2,cx)), y=(1-R.h)>0.001?Math.max(0,Math.min(1,(cy-R.h/2)/(1-R.h))):c.y; VPD={...c,x:+x.toFixed(4),y:+y.toFixed(4)}; delete VPD.auto; vpDraw(); vpLive(); }
/* 4.44: الفيديو العمودي: المكان والتكبير يتغيّرون فوراً بالمعاينة والتصدير (نفس تحريك الفيديو بالسحب)، بدون إعادة قص */
function vpLive(){ if(!VPI||VPI.wide||!VPD) return; const R=vpRect(), s=1/Math.max(0.05,R.w), cx=R.l+R.w/2, cy=R.t+R.h/2; hs().vxf={x:Math.round(-s*(cx*1080-540)),y:Math.round(-s*(cy*1920-960)),s:+s.toFixed(3)}; const w=F.contentWindow; if(w&&w.hsSet) w.hsSet(ST.studio.hs); if(w&&w.draw) w.draw(T); dirty(); }
document.addEventListener('pointermove',vpMove); document.addEventListener('pointerup',()=>{ _vpDrag=null; });
document.addEventListener('input',e=>{ if(e.target.id!=='vpZ'||!VPI) return; const c=vpCur(); VPD={...c,z:+e.target.value/100}; if(c.auto) delete VPD.x; delete VPD.auto; vpDraw(); vpLive(); });
document.addEventListener('change',e=>{ if(e.target.id!=='vpStill'||!VPI) return; const c=vpCur(); VPD={...c,still:e.target.checked}; if(c.auto) delete VPD.x; delete VPD.auto; vpDraw(); });
async function vpGo(body){ const h=hs(); if(body.reset) delete h.vpos; else h.vpos=body; await save(); const r=await api('/hs/vpos',body); if(!r.ok){ toast(srvEn(r.msg)||t('busyJob')); return; }
  stLoader('rebuild',t('vpWorking')); pollJob(async()=>{ try{ VPD=null; VPI=null; _vpL=0; await reloadLite(); toast(t('vpDone')); } finally{ stLoaderHide(); } }); }
document.addEventListener('click',e=>{ const b=e.target.closest('#vpApply,#vpAuto'); if(!b||!ST) return;
  if(b.id==='vpApply'&&VPD){ const d={...VPD}; delete d.auto; if(!d.still) delete d.still; vpGo(d); }
  if(b.id==='vpAuto'){ if(VPI&&!VPI.wide){ snap(); hs().vxf={x:0,y:0,s:1}; VPD=null; const w=F.contentWindow; if(w&&w.hsSet) w.hsSet(ST.studio.hs); if(w&&w.draw) w.draw(T); dirty(); renderRight(); return; } vpGo({reset:true}); } });

/* ───── 4.29: حركة بالمفاتيح (keyframes): مفتاح عند المؤشر للمكان والحجم والدوران والشفافية، والطبقة تتحرك بينها لحالها ───── */
const KF_T=['text','image','char','lt','mark','draw'], KF_EPS=1/60;
const kfOk=L=>!!L&&KF_T.includes(L.type)&&!(L.type==='image'&&L.fit==='cover');
const KF_EZ={ smooth:k=>k<0.5?4*k*k*k:1-Math.pow(-2*k+2,3)/2, linear:k=>k, back:k=>{ const c1=1.70158, c3=c1+1; return 1+c3*Math.pow(k-1,3)+c1*Math.pow(k-1,2); }, hold:k=>k>=1?1:0 };
const KF_EASE=['smooth','linear','back','hold','curve'], KF_PRE=['across','grow','rise','spin','pulse','sway'];
function kfList(L){ return Array.isArray(L&&L.kf)?L.kf.slice().sort((a,b)=>a.t-b.t):[]; }
function kfVal(K,u){ const n=K.length, D0={dx:0,dy:0,s:1,r:0,o:1}, g=(k,f)=>k[f]==null||!isFinite(+k[f])?D0[f]:+k[f], one=k=>({dx:g(k,'dx'),dy:g(k,'dy'),s:g(k,'s'),r:g(k,'r'),o:g(k,'o')});
  if(!n) return {...D0}; if(u<=+K[0].t) return one(K[0]); if(u>=+K[n-1].t) return one(K[n-1]);
  let i=0; while(i<n-2&&u>=+K[i+1].t) i++; const a=K[i], b=K[i+1], k=(a.e==='curve'&&Array.isArray(a.cb)?bezF(a.cb):(KF_EZ[a.e]||KF_EZ.smooth))(clamp((u-+a.t)/Math.max(1e-6,+b.t-+a.t),0,1));
  const A=one(a), B=one(b), o={}; for(const f in A) o[f]=A[f]+(B[f]-A[f])*k; o.o=clamp(o.o,0,1); o.s=Math.max(0.02,o.s); return o; }
function kfPivot(L){ const T_=L.type, x=L.x, y=L.y;
  if(T_==='char') return [(x==null?0.2:x)*1080,(y==null?0.62:y)*1920];
  if(T_==='image') return [(x==null?0.5:x)*1080,(y==null?(L.fit==='card'?0.28:(L.frame==='browser'||L.frame==='post')?0.36:0.35):y)*1920];
  if(T_==='lt') return [((L.side||'right')==='right'?0.72:0.28)*1080,(y==null?0.7:y)*1920];
  if(T_==='mark') return [(x==null?0.5:x)*1080,(y==null?0.4:y)*1920];
  if(T_==='draw') return [(x==null?0.5:x)*1080,(y==null?0.5:y)*1920];
  return [(x==null?0.5:x)*1080,(y==null?0.3:y)*1920]; }
const kfU=L=>r3(clamp(T-L.s,0,Math.max(0,L.e-L.s)));
function kfHere(L){ const u=T-L.s; return kfList(L).findIndex(k=>Math.abs(k.t-u)<=KF_EPS+1e-6); }
function kfCur(L){ return kfVal(kfList(L),T-L.s); }
function kfSet(L,patch){ const u=kfU(L), K=kfList(L); let i=K.findIndex(k=>Math.abs(k.t-u)<=KF_EPS+1e-6);
  if(i<0){ const v=kfVal(K,u); K.push({t:u,dx:Math.round(v.dx),dy:Math.round(v.dy),s:r3(v.s),r:Math.round(v.r*10)/10,o:r3(v.o),e:'smooth'}); K.sort((a,b)=>a.t-b.t); i=K.findIndex(k=>k.t===u); }
  K[i]={...K[i],...patch}; L.kf=K; return K[i]; }
function kfPreset(L,name){ const D=Math.max(0.3,r3(L.e-L.s)), m=r3(Math.min(0.6,D/2)), P=kfPivot(L);
  const K=name==='across'?[{t:0,dx:Math.round(1080-P[0]+360),e:'linear'},{t:D,dx:Math.round(-P[0]-360)}]
    :name==='grow'?[{t:0,s:1},{t:D,s:1.25}]
    :name==='rise'?[{t:0,dy:180,o:0},{t:m,dy:0,o:1,e:'linear'},{t:D,dy:-60}]
    :name==='spin'?[{t:0,r:-180,s:0.3,e:'back'},{t:m,r:0,s:1}]
    :name==='pulse'?Array.from({length:Math.max(2,Math.floor(D/0.5)+1)},(_,i)=>({t:r3(Math.min(D,i*0.5)),s:i%2?1.12:1}))
    :name==='sway'?Array.from({length:Math.max(2,Math.floor(D/0.8)+1)},(_,i)=>({t:r3(Math.min(D,i*0.8)),r:i%2?6:-6,dy:i%2?-14:0})):[];
  L.kf=K.map(k=>({dx:0,dy:0,s:1,r:0,o:1,e:'smooth',...k})); }
const kfFmt=(f,v)=>f==='s'?(+v).toFixed(2)+'×':f==='o'?Math.round(v*100)+'%':f==='r'?Math.round(v)+'°':String(Math.round(v));
function kfDots(L){ if(!kfOk(L)) return ''; return kfList(L).filter(k=>k.t>=-1e-6&&k.t<=L.e-L.s+1e-6).map(k=>'<b class="kfd" data-l="'+esc(L.id)+'" data-t="'+k.t+'" style="left:'+(k.t*PX)+'px" title="'+esc(fmt(L.s+k.t))+'"></b>').join(''); }
/* 4.45: محرر المنحنيات (Graph Editor): تسحب النقطتين وتحدد سرعة الحركة بين المفتاحين (تبدأ هادية وتسرع، أو ترتد…) */
function bezF(cb){ const w=F&&F.contentWindow; if(w&&w.__hsBez) return w.__hsBez(cb); const [x1,y1,x2,y2]=cb; return k=>{ let u=k; for(let i=0;i<12;i++){ const x=3*(1-u)*(1-u)*u*x1+3*(1-u)*u*u*x2+u*u*u; const dx=3*(1-u)*(1-u)*x1+6*(1-u)*u*(x2-x1)+3*u*u*(1-x2); if(Math.abs(dx)<1e-6) break; u-=(x-k)/dx; u=clamp(u,0,1); } return 3*(1-u)*(1-u)*u*y1+3*(1-u)*u*u*y2+u*u*u; }; }
const CURVES={inOut:[0.42,0,0.58,1],in:[0.55,0,1,0.45],out:[0,0.55,0.45,1],snap:[0.7,0,0.1,1],over:[0.34,1.56,0.64,1],anticip:[0.36,-0.5,0.6,1]};
function curveEd(k){ const cb=Array.isArray(k.cb)?k.cb:CURVES.inOut, S=150, pad=24, X_=x=>pad+x*S, Y_=y=>pad+(1-y)*S, f=bezF(cb); let d='M'+X_(0)+' '+Y_(0);
  for(let i=1;i<=40;i++){ const x=i/40; d+=' L'+X_(x).toFixed(1)+' '+Y_(f(x)).toFixed(1); }
  return '<div class="curve"><svg id="cvEd" viewBox="0 0 '+(S+2*pad)+' '+(S+2*pad)+'" width="'+(S+2*pad)+'" height="'+(S+2*pad)+'"><rect x="'+pad+'" y="'+pad+'" width="'+S+'" height="'+S+'" class="g"/><path d="M'+X_(0)+' '+Y_(0)+' L'+X_(cb[0])+' '+Y_(cb[1])+'M'+X_(1)+' '+Y_(1)+' L'+X_(cb[2])+' '+Y_(cb[3])+'" class="arm"/><path d="'+d+'" class="c"/>'
    +'<circle cx="'+X_(cb[0])+'" cy="'+Y_(cb[1])+'" r="7" data-cvh="0"/><circle cx="'+X_(cb[2])+'" cy="'+Y_(cb[3])+'" r="7" data-cvh="1"/></svg>'
    +'<div class="chips">'+Object.keys(CURVES).map(c=>'<button data-cvp="'+c+'">'+t('cv_'+c)+'</button>').join('')+'</div><p class="hint">'+t('cvHint')+'</p></div>'; }
let _cvD=null;
document.addEventListener('pointerdown',e=>{ const h=e.target.closest('[data-cvh]'); if(!h) return; e.preventDefault(); const sv=$('#cvEd'); sv.setPointerCapture(e.pointerId); _cvD={h:+h.dataset.cvh,sv}; snap(); });
document.addEventListener('pointermove',e=>{ if(!_cvD) return; const L=selLayer(); if(!kfOk(L)) return; const i=kfHere(L); if(i<0) return; const K=kfList(L), k=K[i], R=_cvD.sv.getBoundingClientRect(), sc=R.width/198;
  const x=clamp(((e.clientX-R.left)/sc-24)/150,0,1), y=clamp(1-((e.clientY-R.top)/sc-24)/150,-0.6,1.6); const cb=(Array.isArray(k.cb)?k.cb:CURVES.inOut).slice(); cb[_cvD.h*2]=+x.toFixed(3); cb[_cvD.h*2+1]=+y.toFixed(3);
  kfSet(L,{e:'curve',cb}); live(); const sec=$('#kfSec'); if(sec){ const ed=sec.querySelector('.curve'); const kk=kfList(L)[kfHere(L)]; if(ed&&kk){ const d=document.createElement('div'); d.innerHTML=curveEd(kk); ed.replaceWith(d.firstChild); _cvD.sv=$('#cvEd'); } } });
document.addEventListener('pointerup',()=>{ if(_cvD){ _cvD=null; buildTL(); } });
document.addEventListener('click',e=>{ const b=e.target.closest('[data-cvp]'); if(!b||!ST) return; const L=selLayer(); if(!kfOk(L)||kfHere(L)<0) return; snap(); kfSet(L,{e:'curve',cb:CURVES[b.dataset.cvp].slice()}); live(); renderRight(); });
function kfSec(L){ if(!kfOk(L)) return ''; const K=kfList(L), inR=T>=L.s-1e-6&&T<=L.e+1e-6, i=inR?kfHere(L):-1, k=i>=0?K[i]:null, v=kfCur(L);
  let o='<div class="sec" id="kfSec"><h4>'+t('kfTitle')+(K.length?'<span class="st">'+t('kfCount',K.length)+'</span>':'')+'</h4>';
  if(!inR) return o+'<p class="hint">'+t('kfOut')+'</p></div>';
  o+='<div class="row"><button class="sm'+(k?' on':'')+'" data-kfa="add">'+t(k?'kfOnKey':'kfAdd')+'</button>'+(K.length?'<button class="sm ghost" data-kfa="prev">'+t('kfPrev')+'</button><button class="sm ghost" data-kfa="next">'+t('kfNext')+'</button>':'')+'</div>';
  const R=(lbl,f,mn,mx,st)=>'<div class="row"><label>'+lbl+'</label><input type="range" data-kf="'+f+'" min="'+mn+'" max="'+mx+'" step="'+st+'" value="'+(+v[f]).toFixed(3)+'"><span class="val" dir="ltr" id="kfv_'+f+'">'+kfFmt(f,v[f])+'</span></div>';
  o+=R(t('kfX'),'dx',-1080,1080,1)+R(t('kfY'),'dy',-1920,1920,1)+R(t('size'),'s',0.1,4,0.01)+R(t('rotate'),'r',-360,360,1)+R(t('opacity'),'o',0,1,0.01);
  if(k&&i<K.length-1){ o+='<div class="row"><label>'+t('kfEase')+'</label><div class="seg">'+KF_EASE.map(e=>'<button data-kfe="'+e+'" class="'+((k.e||'smooth')===e?'on':'')+'">'+t('kfe_'+e)+'</button>').join('')+'</div></div>'; if(k.e==='curve') o+=curveEd(k); }
  o+='<p class="hint">'+t(K.length?'kfHint2':'kfHint')+'</p><p class="hint" style="margin:8px 0 6px">'+t('kfReady')+'</p><div class="chips" style="margin-bottom:8px">'+KF_PRE.map(p=>'<button data-kfp="'+p+'">'+t('kfp_'+p)+'</button>').join('')+'</div>';
  if(K.length) o+='<div class="row">'+(k?'<button class="sm ghost" data-kfa="del">'+t('kfDel')+'</button>':'')+'<button class="sm ghost" data-kfa="clear">'+t('kfClear')+'</button></div>';
  return o+'</div>'; }
/* المؤشر يتحرك والقيم تتحدّث: لوحة المفاتيح تعيد نفسها لو تغيّر الوقت (وأنت مو ماسك سلايدر) */
let _kfLT=-1; setInterval(()=>{ const sec=document.getElementById('kfSec'); if(!sec||playing||!ST) return; if(Math.abs(T-_kfLT)<1e-4) return; const a=document.activeElement; if(a&&sec.contains(a)&&a.type==='range'&&a.matches(':active')) return; _kfLT=T; const L=selLayer(); if(!kfOk(L)) return; const d=document.createElement('div'); d.innerHTML=kfSec(L); if(d.firstChild) sec.replaceWith(d.firstChild); },300);
let _kfT=0; function kfDirty(){ clearTimeout(_kfT); _kfT=setTimeout(()=>{ buildTL(); },250); }
document.addEventListener('input',e=>{ const el=e.target; if(!ST||el.dataset.kf==null) return; const L=selLayer(); if(!kfOk(L)) return; const f=el.dataset.kf, v=+el.value; if(!isFinite(v)) return;
  if(!el._sn){ snap(); el._sn=1; setTimeout(()=>el._sn=0,1200); } kfSet(L,{[f]:f==='s'||f==='o'?r3(v):Math.round(v)}); const sp=document.getElementById('kfv_'+f); if(sp) sp.textContent=kfFmt(f,v);
  live(); kfDirty(); });
document.addEventListener('change',e=>{ const el=e.target; if(!ST||el.dataset.kf==null) return; renderRight(); });
document.addEventListener('click',e=>{ const b=e.target.closest('[data-kfa],[data-kfe],[data-kfp]'); if(!b||!ST) return; const L=selLayer(); if(!kfOk(L)) return; const d=b.dataset, K=kfList(L);
  if(d.kfa==='prev'||d.kfa==='next'){ const u=T-L.s, x=d.kfa==='prev'?K.filter(k=>k.t<u-KF_EPS).pop():K.find(k=>k.t>u+KF_EPS); if(!x){ toast(t('kfNone')); return; } seek(r3(L.s+x.t)); renderRight(); placeGiz(); return; }
  if(d.kfa==='add'&&kfHere(L)>=0){ toast(t('kfOnKey')); return; }
  snap();
  if(d.kfa==='add'){ kfSet(L,{}); toast(t('kfAdded',fmt(T))); }
  else if(d.kfa==='del'){ const i=kfHere(L); if(i<0) return; K.splice(i,1); if(K.length) L.kf=K; else delete L.kf; }
  else if(d.kfa==='clear'){ delete L.kf; toast(t('kfCleared')); }
  else if(d.kfe){ const i=kfHere(L); if(i<0) return; kfSet(L,d.kfe==='curve'?{e:'curve',cb:Array.isArray(K[i].cb)?K[i].cb:CURVES.inOut.slice()}:{e:d.kfe}); }
  else if(d.kfp){ kfPreset(L,d.kfp); toast(t('kfPresetDone',t('kfp_'+d.kfp))); }
  live(); buildTL(); renderRight(); placeGiz(); });

/* ───── 4.26: الدبلجة بالاستوديو: حالتها، تشغيل وإطفاء، السكربت بالتوقيت، ورفع ملف دبلجة كامل ───── */
let DUBS=null, _dubL=0;
function dubLoad(){ if(Date.now()-_dubL<4000) return; _dubL=Date.now(); api('/hs/dub_state').then(r=>{ DUBS=r; if(RTAB==='audio') renderRight(); }).catch(()=>{}); }
function dubSec(){ dubLoad(); const D=DUBS; if(!D) return ''; if(!D.has&&!D.want) return '';
  let o='<div class="sec"><h4>'+t('dubTitle')+(D.has?' <span class="st">'+esc(D.name||D.lang||'')+'</span>':'')+'</h4>';
  if(!D.has){ o+='<p class="hint">'+t('dubWant',esc(D.want))+'</p></div>'; return o; }
  o+='<div class="tog"><div>'+t('dubOn')+'<small>'+t('dubOnSub')+'</small></div><div class="sw-t'+(D.on?' on':'')+'" id="dubTog"></div></div>'
    +'<p class="hint">'+t('dubStat',D.n,D.tr,D.aud)+(D.track?' · '+t('dubTrack'):'')+'</p>'
    +'<div class="row"><button class="sm" id="dubCopy">'+t('dubCopy')+'</button><button class="sm" id="dubUp">'+t('dubUp')+'</button></div><p class="hint">'+t('dubHint')+'</p></div>';
  return o; }
document.addEventListener('click',async e=>{ const b=e.target.closest('#dubTog,#dubCopy,#dubUp'); if(!b||!ST) return;
  if(b.id==='dubTog'){ const on=!(DUBS&&DUBS.on); const r=await api('/hs/dub',{on}); if(!r.ok){ toast(srvEn(r.msg)||t('failed')); return; } hs().mix.dub=on; _dubL=0; DUBS=null; dubLoad(); auLoad(true); toast(t(on?'dubOnDone':'dubOffDone')); return; }
  if(b.id==='dubCopy'){ try{ await navigator.clipboard.writeText((DUBS&&DUBS.script)||''); toast(t('copied')); }catch(err){ toast(t('failed')); } return; }
  if(b.id==='dubUp'){ const inp=$('#fileIn'); inp.value=''; inp.accept='audio/*,.mp3,.wav,.m4a,.aac'; inp.multiple=false; inp.onchange=async()=>{ const f=inp.files[0]; if(!f) return; toast(t('uploading')); const r=await api('/hs/dub_track',f,{'X-Name':encodeURIComponent(f.name)}); if(!r.ok){ toast(srvEn(r.msg)||t('failed')); return; } hs().mix.dub=true; _dubL=0; DUBS=null; dubLoad(); auLoad(true); toast(t('dubOnDone')); }; inp.click(); } });

/* ───── النوافذ ───── */
function modal(html,wide){ $('#mbox').className=wide?'wide':''; $('#mbox').dir=LANG==='ar'?'rtl':'ltr'; $('#mbox').innerHTML=html; $('#modal').classList.add('on'); }
function closeModal(){ $('#modal').classList.remove('on'); $('#mbox').innerHTML=''; }
$('#modal').addEventListener('pointerdown',e=>{ if(e.target.id==='modal') closeModal(); });
function editCard(i){ const c=ST.caps.cards[i]; modal('<h3>'+t('editTitle')+'</h3><textarea id="edTx" rows="3" dir="rtl">'+esc(key(c))+'</textarea><p class="hint">'+t('editHint')+'</p><div class="row" style="margin:12px 0 0"><button class="pri" id="edOk">'+t('save')+'</button><button class="ghost" id="edNo">'+t('cancel')+'</button></div>');
  const x=$('#edTx'); x.focus(); $('#edNo').onclick=closeModal;
  $('#edOk').onclick=async()=>{ await save(); snap(); const r=await api('/hs/text',{card:i,text:x.value}); if(!r.ok){ toast(srvEn(r.msg)||t('failed')); return; } ST.caps=r.caps; ST.studio.hs=r.hs; hs(); closeModal(); await initFrame(false); buildTL(); renderAll(); drawT(T); adoptSig=true; $('#saved').textContent=t('saved'); refreshCheck(); }; }
function askRemove(body,what,confirmIt){ if(!confirmIt) return doRemove(body,what); modal('<h3>'+t('removeTitle')+'</h3><p dir="auto" style="line-height:1.9">'+esc(what)+'</p><p class="hint">'+t('removeHint')+'</p><div class="row" style="margin:12px 0 0"><button class="pri" id="dOk">'+t('removeGo')+'</button><button class="ghost" id="dNo">'+t('cancel')+'</button></div>');
  $('#dNo').onclick=closeModal; $('#dOk').onclick=async()=>{ closeModal(); doRemove(body,what); }; }
async function doRemove(body,what){ { await save(); const r=await api('/hs/remove',body); if(r&&r.instant){ MARKS=[]; SEL=null; await reloadLite(); cutUndoMark({}); toast(t('cutInstant',r.gone)); return; } if(!r.ok){ toast(srvEn(r.msg)||t('busyJob')); return; } MARKS=[]; SEL=null; stLoader('rebuild',t('rebuildSub')); pollJob(async(p)=>{ try{ await load(true); cutUndoMark(p); } finally{ stLoaderHide(); } }); }; }
function pollJob(done){ let miss=0; const tk=async()=>{ let p; try{ p=await api('/api/progress'); if(!p||p.running==null) throw 0; miss=0; }catch(e){ if(++miss<60){ setTimeout(tk,1500); return; } p={running:false,err:'',log:''}; }   /* 4.45: السيرفر يعيد تشغيله أحياناً وسط العملية: نكمل نسأل بدل ما يعلق التحميل */ { const cf=$('#cutfx .ln'); if(cf) cf.textContent=srvEn((p.log||'').split('\n').filter(Boolean).slice(-1)[0]||''); } const L=$('#log'); if(L){ L.style.display='block'; L.dir='rtl'; L.textContent=(p.log||'').split('\n').filter(Boolean).slice(-9).join('\n'); L.scrollTop=1e6; }
  $('#saved').textContent=p.running?t('working',p.elapsed):t('saved'); if(p.running){ setTimeout(tk,1200); return; } if(p.err) toast(t('failedWhy',p.err.slice(0,90))); done&&done(p); }; setTimeout(tk,600); }
async function doExport(kind,hooks){ await save(); RTAB='proj'; markTabs(); renderRight(); const r=await api('/hs/export',{kind,hooks:!!hooks}); if(!r.ok){ toast(srvEn(r.msg)||t('busyJob')); return; } toast(t('exportStarted'));
  pollJob(async p=>{ INFO=await api('/hs/info'); if(RTAB==='proj') renderRight(); if(!p.err) toast(t('exportDone')); }); }
$('#bExport').onclick=()=>{ RTAB='proj'; markTabs(); renderRight(); };
let PIN=null;
function grab(){ try{ const w=F.contentWindow, src=w.document.getElementById('cv'), c=document.createElement('canvas'); c.width=432; c.height=768; c.getContext('2d').drawImage(src,0,0,432,768); return c.toDataURL('image/jpeg',0.72); }catch(e){ return ''; } }
function openNote(){ if(!ST) return; if(playing) stop(); PIN=null; const img=grab(), x0=T;
  modal('<h3>'+t('noteAt',fmt(x0))+'</h3><div class="ngrid"><div><div id="pinbox">'+(img?'<img src="'+img+'">':'')+'<div id="pin"></div></div><p class="hint" style="text-align:center">'+t('pinHint')+'</p></div><div><textarea id="nTx" rows="7" dir="auto" placeholder="'+t('notePh')+'"></textarea><div class="row" style="margin:12px 0 0"><button class="pri" id="nOk">'+t('noteSave')+'</button><button class="ghost" id="nNo">'+t('cancel')+'</button></div><p class="hint"><kbd>Ctrl</kbd>+<kbd>Enter</kbd></p></div></div>');
  const tx=$('#nTx'); tx.focus();
  $('#pinbox').onclick=e=>{ const r=$('#pinbox').getBoundingClientRect(); PIN={x:+((e.clientX-r.left)/r.width).toFixed(3),y:+((e.clientY-r.top)/r.height).toFixed(3)}; const p=$('#pin'); p.style.display='block'; p.style.left=(PIN.x*100)+'%'; p.style.top=(PIN.y*100)+'%'; };
  const ok=async()=>{ if(!tx.value.trim()){ toast(t('noteEmpty')); return; } const ci=cardAt(x0); const r=await api('/hs/note',{t:x0,text:tx.value.trim(),pin:PIN,img,card:ci>=0?ci:null}); NOTES=r.notes; buildTL(); if(RTAB==='notes') renderRight(); closeModal(); toast(t('noteSaved')); };
  $('#nOk').onclick=ok; $('#nNo').onclick=closeModal; tx.onkeydown=e=>{ if(e.key==='Enter'&&(e.ctrlKey||e.metaKey)){ e.preventDefault(); ok(); } e.stopPropagation(); }; }
$('#bNote').onclick=askOpen;   // 4.50: الملاحظات صارت المساعد
$('#bQR').onclick=()=>{ if(!INFO) return; let svg=''; try{ const q=qrcode(0,'M'); q.addData(INFO.lanM||INFO.lan); q.make(); svg=q.createSvgTag({cellSize:6,margin:3,scalable:true}); }catch(e){}
  modal('<h3>'+t('qrTitle')+'</h3><div style="display:flex;gap:18px;flex-wrap:wrap;align-items:center"><div style="width:230px;background:#fff;border-radius:10px;padding:6px;line-height:0">'+svg+'</div><div style="flex:1;min-width:220px"><p style="line-height:1.9;margin-top:0">'+t('qrHint')+'</p><div class="copy"><span style="direction:ltr;text-align:left">'+esc(INFO.lanM||INFO.lan)+'</span></div><p class="hint">'+t('qrCode')+' <b style="color:var(--tx);font-size:16px;letter-spacing:2px">'+INFO.token+'</b></p></div></div><div id="ntfBox" class="sec" style="margin-top:14px"></div><div class="row" style="margin:14px 0 0"><button id="qNo">'+t('close')+'</button></div>'); $('#qNo').onclick=closeModal; ntfRender(); };
/* 4.1: إشعارات للجوال (ntfy): Claude يكلّمك ويرسل لك المقطع أول ما يخلص */
async function ntfRender(st){ const box=$('#ntfBox'); if(!box) return; if(!st){ try{ st=await (await fetch('/hs/notify')).json(); }catch(e){ st={on:false}; } }
  let h='<h4>'+t('ntfTitle')+'</h4><p class="hint" style="line-height:1.8">'+t('ntfHint')+'</p>';
  if(st.on&&st.sub){ let svg=''; try{ const q=qrcode(0,'M'); q.addData(st.sub); q.make(); svg=q.createSvgTag({cellSize:4,margin:2,scalable:true}); }catch(e){}
    h+='<div style="display:flex;gap:14px;flex-wrap:wrap;align-items:center"><div style="width:150px;background:#fff;border-radius:8px;padding:4px;line-height:0">'+svg+'</div><div style="flex:1;min-width:200px"><p style="margin:0 0 6px">'+t('ntfSteps')+'</p><div class="copy"><span style="direction:ltr;text-align:left">'+esc(st.topic)+'</span></div><p class="hint">'+t('ntfPrivacy')+'</p></div></div><div class="row"><button class="pri" id="ntfTest">'+t('ntfTest')+'</button><button class="ghost" id="ntfOff">'+t('ntfOff')+'</button></div>'; }
  else h+='<div class="row"><button class="pri" id="ntfOn">'+t('ntfOn')+'</button></div>';
  box.innerHTML=h;
  const call=async a=>{ const r=await api('/hs/notify',{action:a}); return r; };
  if($('#ntfOn')) $('#ntfOn').onclick=async()=>{ const r=await call('setup'); ntfRender(r); };
  if($('#ntfOff')) $('#ntfOff').onclick=async()=>{ await call('off'); ntfRender({on:false}); };
  if($('#ntfTest')) $('#ntfTest').onclick=async()=>{ const r=await call('test'); toast(r&&r.ok?t('ntfSent'):t('ntfFail')+(r&&srvEn(r.msg)?': '+srvEn(r.msg):'')); }; }
function compare(a,b){ modal('<h3>'+t('compareTitle')+'</h3><div class="cmp"><div><video id="cvA" src="/hs/export/'+a+'" playsinline muted></video><p class="hint" style="direction:ltr">'+a+'</p></div><div><video id="cvB" src="/hs/export/'+b+'" playsinline></video><p class="hint" style="direction:ltr">'+b+'</p></div></div><div class="row" style="margin-top:10px"><button class="pri" id="cPlay">'+t('play')+'</button><input type="range" id="cSeek" min="0" max="1000" value="0"><button id="cNo">'+t('close')+'</button></div>',true);
  const A=$('#cvA'), B=$('#cvB'); $('#cNo').onclick=()=>{ A.pause(); B.pause(); closeModal(); };
  $('#cPlay').onclick=()=>{ if(A.paused){ B.currentTime=A.currentTime; A.play(); B.play(); $('#cPlay').textContent=t('pause'); } else { A.pause(); B.pause(); $('#cPlay').textContent=t('play'); } };
  $('#cSeek').oninput=e=>{ const d=Math.max(A.duration||0,B.duration||0), x=d*e.target.value/1000; A.currentTime=Math.min(x,A.duration||x); B.currentTime=Math.min(x,B.duration||x); };
  A.ontimeupdate=()=>{ const d=Math.max(A.duration||0,B.duration||0); if(d) $('#cSeek').value=1000*A.currentTime/d; }; }
$('#bSafe').onclick=()=>$('#safe').classList.toggle('on'); $('#bCover').onclick=coverShot; $('#bUndo').onclick=undo; $('#pp').onclick=play;

/* ───── تحريك الطبقة على الشاشة ───── */
function placeGiz(){ const g=$('#giz'), L=selLayer(); if(!ST){ g.style.display='none'; return; }
  if(SEL&&SEL.kind==='vxf'){ const V=hs().vxf||{}; g.style.display='block'; g.style.left=((0.5+(+V.x||0)/1080)*100)+'%'; g.style.top=((0.5+(+V.y||0)/1920)*100)+'%'; return; }
  if(SEL&&SEL.kind==='hook'){ const H=hs().hooks; if(H&&H.on&&T<(H.dur||2.6)){ g.style.display='block'; g.style.left=((H.x==null?0.5:H.x)*100)+'%'; g.style.top=((H.y==null?0.2:H.y)*100)+'%'; } else g.style.display='none'; return; }
  if(SEL&&SEL.kind==='cap'&&hs().cap.on){ const i=+SEL.id, c=ST.caps.cards[i]; if(c&&T>=c.s&&T<c.e){ const ov=capOvOf(i,false), y=(SCOPE==='one'&&ov&&ov.y!==undefined)?ov.y:hs().cap.y; g.style.display='block'; g.style.left='50%'; g.style.top=y+'%'; return; } }
  if(!L||L.type==='fx'||(L.type==='mg'&&(L.kind==='sting'||L.kind==='compare'))||L.type==='split'||L.type==='cover'||L.type==='bg'||(L.type==='behind'&&L.y==null)||(L.type==='viz'&&L.layout!=='over')||(L.type==='image'&&L.fit==='cover')||L.type==='kinetic'||T<L.s||T>=L.e){ g.style.display='none'; return; } g.style.display='block'; if(kfOk(L)&&kfList(L).length){ const P=kfPivot(L), v=kfCur(L); g.style.left=(clamp((P[0]+v.dx)/1080,0,1)*100)+'%'; g.style.top=(clamp((P[1]+v.dy)/1920,0,1)*100)+'%'; return; } if(L.type==='pip'&&L.pos!=='free'){ const w_=(L.size||0.36), h_=w_*1080*(L.circle?1:(L.ratio||1.25))/1920, p=L.pos||'tr', cx=p==='tl'||p==='bl'?(48/1080+w_/2):p==='tc'||p==='bc'?0.5:1-48/1080-w_/2, cy=p==='bl'||p==='br'||p==='bc'?1-(300/1920)-h_/2:170/1920+h_/2; g.style.left=(cx*100)+'%'; g.style.top=(cy*100)+'%'; return; }   // 4.56
  g.style.left=((L.x==null?(L.type==='desk'?0.3:0.5):L.x)*100)+'%'; if(L.type==='desk'){ const S=dkStageK(); g.style.top=((S.y0+(L.y==null?0.42:L.y)*S.h)*100)+'%'; } else g.style.top=((L.y==null?0.3:L.y)*100)+'%'; }
(function(){ const g=$('#giz'); let on=false; g.addEventListener('pointerdown',e=>{ on=true; snap(); g.setPointerCapture(e.pointerId); e.preventDefault(); });
  g.addEventListener('pointermove',e=>{ if(!on) return; const r=$('#wrap').getBoundingClientRect(); let x=clamp((e.clientX-r.left)/r.width,0,1), y=clamp((e.clientY-r.top)/r.height,0,1); const w=F.contentWindow;
    if(SEL&&SEL.kind==='hook'){ const H=hs().hooks; if(MAG&&Math.abs(x-0.5)<0.02) x=0.5; H.x=r3(x); H.y=r3(clamp(y,0.04,0.95)); if(w&&w.hsSet) w.hsSet(ST.studio.hs); placeGiz(); if(w&&w.draw) w.draw(T); return; }
    if(SEL&&SEL.kind==='vxf'){ const V=hs().vxf||(hs().vxf={}); if(MAG&&Math.abs(x-0.5)<0.02) x=0.5; if(MAG&&Math.abs(y-0.5)<0.012) y=0.5; V.x=Math.round((x-0.5)*1080); V.y=Math.round((y-0.5)*1920); if(w&&w.hsSet) w.hsSet(ST.studio.hs); placeGiz(); if(w&&w.draw) w.draw(T); return; }
    if(SEL&&SEL.kind==='cap'){ const v=Math.round(clamp(y*100,15,92)*2)/2; setK('C.y',v); if(w&&w.hsSet) w.hsSet(ST.studio.hs); placeGiz(); if(w&&w.draw) w.draw(T); return; }
    const L=selLayer(); if(!L) return; if(MAG&&Math.abs(x-0.5)<0.02) x=0.5; if(kfOk(L)&&kfList(L).length&&T>=L.s&&T<L.e){ const P=kfPivot(L); kfSet(L,{dx:Math.round(x*1080-P[0]),dy:Math.round(y*1920-P[1])}); placeGiz(); if(w&&w.hsSet) w.hsSet(ST.studio.hs); if(w&&w.draw) w.draw(T); kfDirty(); return; } if(L.type==='desk'){ const S=dkStageK(); y=clamp((y-S.y0)/S.h,0,1); } if(L.type==='pip'&&L.pos!=='free'){ L.pos='free'; } L.x=r3(x); L.y=r3(y); propagate('L.x',L.x); propagate('L.y',L.y); if(L.type==='pip'&&w&&w.hsSet) w.hsSet(ST.studio.hs); placeGiz(); if(w&&w.draw) w.draw(T); });
  const end=()=>{ if(on){ on=false; live(); renderRight(); } }; g.addEventListener('pointerup',end); g.addEventListener('pointercancel',end); })();

/* ───── الاختصارات ───── */
document.addEventListener('keydown',e=>{ const tg=e.target.tagName, typing=(tg==='INPUT'&&!['range','checkbox','radio'].includes(e.target.type))||tg==='TEXTAREA'||tg==='SELECT';
  if(e.key==='Escape'){ closeModal(); return; }
  const mod=e.ctrlKey||e.metaKey;
  if($('#modal').classList.contains('on')||typing||!ST){ if(mod&&e.code==='KeyF'&&ST&&!$('#modal').classList.contains('on')){ e.preventDefault(); LTAB='text'; markTabs(); renderLeft(); $('#q').focus(); } return; }
  if(e.code==='Space'){ e.preventDefault(); spaceDown(e); }
  else if(mod&&e.code==='KeyZ'){ e.preventDefault(); undo(); }
  else if(mod&&e.code==='KeyF'){ e.preventDefault(); LTAB='text'; markTabs(); renderLeft(); $('#q').focus(); }
  else if(mod&&e.code==='KeyD'){ e.preventDefault(); dupSel(); }
  else if(mod) return;
  else if(e.code==='KeyM'){ e.preventDefault(); askOpen(); }
  else if(e.code==='KeyA'||e.code==='KeyV'){ TOOL='select'; markTabs(); }
  else if(e.code==='KeyB'){ TOOL='blade'; markTabs(); }
  else if(e.code==='KeyN'){ MAG=!MAG; markTabs(); }
  else if(e.code==='KeyL'){ e.preventDefault(); linkToggle(); }
  else if(e.code==='KeyS'){ e.preventDefault(); cutHere(); }
  else if(e.code==='KeyK'){ $('#bSkim').click(); }
  else if(e.key==='ArrowLeft'||e.key==='ArrowRight'){ e.preventDefault(); if(playing) stop(); seek(T+(e.shiftKey?1:1/FPS)*(e.key==='ArrowRight'?1:-1)); placeGiz(); }
  else if(e.key==='Delete'||e.key==='Backspace'){ if(SEL){ e.preventDefault(); delSel(); } } });
window.addEventListener('resize',()=>{ if(ST) buildTL(); });


/* ═══════════ v3: ستايلات جاهزة للكابشن ═══════════ */
const CAPRESET={bg:'none',bgColor:'#000000',bgOpacity:0.62,stroke:0,strokeColor:'#000000',shadow:true,shadowColor:'#000000',hl:'color',chunk:0,actScale:1,fill:'solid',mode:'line',enter:'rise',lines:2};
const CAPPRE={ clean:{font:'Tajawal',weight:800,size:66,color:'#FFFFFF',active:'#F2B33D',bg:'none',stroke:0,shadow:true,enter:'rise'},
  box:{font:'Cairo',weight:800,size:52,color:'#FFFFFF',active:'#FFE14D',bg:'box',bgColor:'#000000',bgOpacity:0.7,stroke:0,enter:'pop'},
  pill:{font:'Tajawal',weight:900,size:58,color:'#FFFFFF',active:'#8F73F5',bg:'pill',stroke:0,shadow:true,enter:'rise'},
  bold:{font:'Cairo',weight:900,size:68,color:'#FFE14D',active:'#FFFFFF',bg:'none',stroke:7,strokeColor:'#000000',shadow:false,enter:'pop'},
  karaoke:{font:'Alexandria',weight:800,size:56,color:'#FFFFFF',active:'#43D17A',bg:'none',stroke:4,strokeColor:'#000000',shadow:true,enter:'words'},
  oneword:{font:'Cairo',weight:900,size:104,color:'#FFFFFF',active:'#F2B33D',bg:'none',stroke:8,strokeColor:'#000000',shadow:false,enter:'pop',chunk:1,lines:1},
  band:{font:'IBM Plex Sans Arabic',weight:700,size:48,color:'#FFFFFF',active:'#FFE14D',bg:'bar',bgColor:'#000000',bgOpacity:0.78,shadow:false,enter:'fade'},
  lines:{font:'Almarai',weight:800,size:50,color:'#111111',active:'#D2558F',bg:'lines',bgColor:'#FFFFFF',bgOpacity:1,shadow:false,enter:'rise'},
  under:{font:'Readex Pro',weight:700,size:56,color:'#FFFFFF',active:'#43D17A',hl:'under',shadow:true,enter:'fade'},
  fill:{font:'Tajawal',weight:900,size:60,color:'#FFFFFF',active:'#FFFFFF',hl:'dim',stroke:5,strokeColor:'#000000',shadow:false,enter:'none'},
  punch:{font:'Cairo',weight:900,size:68,color:'#FFFFFF',active:'#FFE14D',actScale:1.22,stroke:8,strokeColor:'#000000',shadow:false,enter:'pop',chunk:3,lines:1},
  duo:{font:'Lalezar',weight:400,size:92,color:'#FFFFFF',active:'#F2B33D',stroke:8,strokeColor:'#000000',shadow:false,enter:'pop',chunk:2,lines:1},
  hollow:{font:'Changa',weight:800,size:72,color:'#FFFFFF',active:'#FFE14D',fill:'outline',shadow:false,enter:'words'},
  retro:{font:'Baloo Bhaijaan 2',weight:800,size:66,color:'#FFE14D',active:'#FFFFFF',stroke:6,strokeColor:'#1B1B22',shadow:'hard',shadowColor:'#D2558F',enter:'drop'},
  calm:{font:'IBM Plex Sans Arabic',weight:500,size:44,color:'#FFFFFF',active:'#FFFFFF',shadow:true,enter:'fade'},
  kufi:{font:'Reem Kufi',weight:700,size:60,color:'#FFFFFF',active:'#4C8DFF',shadow:true,enter:'slide'},
  naskh:{font:'Amiri',weight:700,size:62,color:'#FFFFFF',active:'#F2B33D',bg:'bar',bgColor:'#101014',bgOpacity:0.55,shadow:false,enter:'fade'},
  naskhword:{font:'Noto Naskh Arabic',weight:700,size:90,color:'#FFFFFF',active:'#FFD21F',shadow:true,enter:'pop',chunk:1,lines:1},
  glass:{font:'Noto Naskh Arabic',weight:700,size:60,color:'#FFFFFF',active:'#FFD21F',bg:'glass',shadow:false,enter:'rise',chunk:3,lines:2},
  fun:{font:'Baloo Bhaijaan 2',weight:700,size:60,color:'#FFFFFF',active:'#FF7A59',bg:'pill',shadow:true,enter:'pop'} };
function preTile(k){ const p={...CAPRESET,...CAPPRE[k]}, dark=p.bg==='lines';
  let base='font-family:\''+p.font+'\';font-weight:'+p.weight+';color:'+p.color+';';
  if(p.stroke) base+='text-shadow:0 0 2px '+p.strokeColor+',0 0 2px '+p.strokeColor+',0 1px 2px '+p.strokeColor+(p.shadow==='hard'?',3px 3px 0 '+p.shadowColor:'')+';';
  if(p.fill==='outline') base+='-webkit-text-stroke:1px '+p.color+';color:transparent;';
  let wrap='all:unset;'; if(p.bg==='box') wrap+='background:rgba(0,0,0,.75);padding:2px 8px;border-radius:6px;'; if(p.bg==='glass') wrap+='background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.45);padding:2px 9px;border-radius:9px;'; if(p.bg==='lines') wrap+='background:'+p.bgColor+';padding:1px 7px;border-radius:4px;';
  if(p.bg==='bar') wrap+='display:block;width:100%;background:rgba(0,0,0,.78);padding:3px 0;text-align:center;';
  let act='all:unset;'; if(p.bg==='pill') act+='background:'+p.active+';color:#fff;padding:0 5px;border-radius:5px;'; else if(p.hl==='under') act+='border-bottom:3px solid '+p.active+';'; else if(p.hl==='dim') act+='opacity:.36;'; else act+='color:'+p.active+';'+(p.fill==='outline'?'-webkit-text-stroke:0;':'');
  if(p.actScale>1) act+='font-size:1.25em;';
  const words=LANG==='en'?(p.chunk===1?['','key']:['Some','key']):p.chunk===1?['','مميّز']:['كلام','مميّز'];
  return '<div class="tile" data-cappre="'+k+'" style="aspect-ratio:16/10"><div class="pv" dir="'+(LANG==='en'?'ltr':'rtl')+'" style="'+base+(dark?'':'')+(p.bg==='bar'?'padding:4px 0;':'')+'"><span style="'+wrap+'">'+(words[0]?words[0]+' ':'')+'<span style="'+act+'">'+words[1]+'</span></span></div><span>'+t('cp_'+k)+'</span></div>'; }
function capStyle(k){ return {...CAPRESET,...CAPPRE[k]}; }

/* ═══════════ v3: نطاق التعديل (هذا فقط / الكل) ═══════════ */
let SCOPE='one';
const NOPROP=new Set(['style','draw','a','b','by','mode','num','kind','values','value','items','from','to','km','time','label','pre','word','post','url','frame','caption','handle','title','ratio','text','s','e','src','char','id','track','type','auto','fx']);
function scopeRow(){ return '<div class="row"><label>'+t('scope')+'</label><div class="seg"><button data-scope="one" class="'+(SCOPE==='one'?'on':'')+'">'+t('scopeOne')+'</button><button data-scope="all" class="'+(SCOPE==='all'?'on':'')+'">'+t('scopeAll')+'</button></div></div>'; }
function capOvOf(i,create){ const h=hs(); h.capOv=h.capOv||{}; const k=key(ST.caps.cards[i]); if(!h.capOv[k]&&create) h.capOv[k]={}; return h.capOv[k]; }
function capVal(i,f){ const o=capOvOf(i,false); return (SCOPE==='one'&&o&&o[f]!==undefined)?o[f]:(o&&o[f]!==undefined&&SCOPE==='one'?o[f]:hs().cap[f]); }
function propagate(k,v){ if(SCOPE!=='all'||!k.startsWith('L.')) return; const f=k.slice(2), L=selLayer(); if(!L||NOPROP.has(f)) return; hs().layers.forEach(x=>{ if(x!==L&&x.type===L.type&&(L.type!=='image'||x.fit===L.fit)) x[f]=v; }); }

/* ═══════════ v3: صفحة الأسئلة قبل المونتاج ═══════════ */
let BR=null, BRD=null;
const PLATS=['tiktok','instagram','x','linkedin'], FRAMES=['9:16','4:5','1:1','16:9'];
const B_OPTS={ goal:['ad','explain','story','news','vlog','tutorial','review','podcast','other'], platform:PLATS, frame:FRAMES, length:['keep','tight','max30','max60'], pace:['calm','normal','fast'],
  pos:['top','mid','bottom'], media:['none','search','ai','mix','mine'], amount:['few','some','many'], sfx:['none','light','rich'] };
const POSY={top:30,mid:56,bottom:76};
function chips(id,opts,val,multi){ return '<div class="chips">'+opts.map(o=>{ const on=multi?(val||[]).includes(o):val===o; return '<button data-b="'+id+'" data-v="'+o+'"'+(multi?' data-m="1"':'')+' class="'+(on?'on':'')+'">'+t('b_'+o)+'</button>'; }).join('')+'</div>'; }
function btog(id,title,sub,val){ const v=BVIS.tog[id]; return '<div class="tog">'+(v?'<span class="tvi">'+v()+'</span>':'')+'<div style="flex:1">'+title+(sub?'<small>'+sub+'</small>':'')+'</div><div class="sw-t'+(val?' on':'')+'" data-bt="'+id+'"></div></div>'; }
/* 4.16: صور توضيحية بصفحة الأسئلة: كل خيار يحتاج شرح له رسمة صغيرة تبيّن وش بيطلع */
const BVC={s:'#0f1014',p1:'#646a78',p2:'#4a4f5c',w:'#F2F2F4',m:'#7d7d8b',a:'#F2B33D',o:'#F28C28',pp:'#ECE4D2',ink:'#2b2620',bd:'#3a3a46',c:'#20222b'};
const bvR=(x,y,w,h,f,r,ex)=>'<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" rx="'+(r==null?1.5:r)+'" fill="'+f+'"'+(ex||'')+'/>';
const bvPhone=(inner,bg)=>'<svg viewBox="0 0 56 100" aria-hidden="true"><defs><clipPath id="bvc"><rect x="1" y="1" width="54" height="98" rx="6.5"/></clipPath></defs><g clip-path="url(#bvc)">'+bvR(0,0,56,100,bg||BVC.s,0)+inner+'</g><rect x=".5" y=".5" width="55" height="99" rx="7" fill="none" stroke="'+BVC.bd+'"/></svg>';
const bvWide=inner=>'<svg viewBox="0 0 120 44" aria-hidden="true">'+bvR(0,0,120,44,BVC.s,6)+inner+'</svg>';
function bvMan(cx,cy,k,c1,c2){ k=k||1; return '<path d="M'+(cx-16*k)+' '+(cy+30*k)+'Q'+(cx-16*k)+' '+(cy+11*k)+' '+cx+' '+(cy+11*k)+'Q'+(cx+16*k)+' '+(cy+11*k)+' '+(cx+16*k)+' '+(cy+30*k)+'Z" fill="'+(c2||BVC.p2)+'"/><circle cx="'+cx+'" cy="'+cy+'" r="'+(7.5*k)+'" fill="'+(c1||BVC.p1)+'"/>'; }
const bvCap=(y,w1,w2,c)=>{ const x=28-(w1+w2+2)/2; return bvR(x,y,w1,4,BVC.w)+bvR(x+w1+2,y,w2,4,c||BVC.a); };
const bvPhoto=(x,y,w,h)=>bvR(x,y,w,h,'#2c3e52',2)+'<circle cx="'+(x+w*0.74)+'" cy="'+(y+h*0.3)+'" r="'+(h*0.12)+'" fill="#F2D27A"/><path d="M'+x+' '+(y+h)+'L'+(x+w*0.35)+' '+(y+h*0.45)+'L'+(x+w*0.6)+' '+(y+h*0.78)+'L'+(x+w*0.75)+' '+(y+h*0.6)+'L'+(x+w)+' '+(y+h)+'Z" fill="#4f7a5b"/>';
const bvAI=(x,y,w,h)=>bvR(x,y,w,h,'#2a2340',2)+'<circle cx="'+(x+w*0.45)+'" cy="'+(y+h*0.55)+'" r="'+(h*0.26)+'" fill="#B98AF0"/><ellipse cx="'+(x+w*0.45)+'" cy="'+(y+h*0.55)+'" rx="'+(w*0.36)+'" ry="'+(h*0.08)+'" fill="none" stroke="#F2D27A" stroke-width="1.2"/>'+bvR(x+w-12,y+2.5,9.5,6,'#0f1014',1.5)+'<text x="'+(x+w-7.25)+'" y="'+(y+7.2)+'" font-size="4.6" font-weight="700" text-anchor="middle" fill="#F2F2F4" font-family="sans-serif">AI</text>';
const BVIS={
  style:{
    normal:()=>bvPhone(bvR(5,6,46,32,BVC.c,3,' stroke="'+BVC.bd+'"')+bvR(10,12,8,8,BVC.a,4)+bvR(21,13,24,2.6,BVC.w)+bvR(21,17.5,16,2.2,BVC.m)+bvR(10,25,35,2.6,BVC.w)+bvR(10,30,26,2.2,BVC.m)+bvMan(28,56,1.15)+bvCap(84,16,9)),
    podcast:()=>bvPhone(bvR(9,12,38,4,BVC.w)+bvR(15,19,26,2.5,BVC.m)+bvR(2,34,52,29,'#2a2d36',1)+bvMan(17,44,0.42)+bvMan(39,44,0.42,'#7a7468','#5a554b')+bvR(10,70,36,3,BVC.w)+bvR(14,75.5,28,2.4,BVC.m)),
    paper:()=>bvPhone(bvR(8,14,36,4,BVC.ink)+bvR(8,22,28,4,BVC.ink)+bvR(8,30,18,4,BVC.o)+bvR(28,30,1.6,4.6,BVC.ink,0)+bvR(11,49,36,26,'rgba(0,0,0,.10)',2.5)+bvR(9,47,36,26,'#FFFFFF',2.5)+bvR(14,62,5,7,BVC.ink,1)+bvR(22,57,5,12,BVC.ink,1)+bvR(30,52,5,17,BVC.o,1)+bvR(8,84,22,3,'#b9b09c'),BVC.pp),
    motion:()=>bvPhone(bvR(6,9,30,7,BVC.a,2)+bvR(9,11.4,18,2.4,'#1b1b22')+'<circle cx="41" cy="31" r="8.5" fill="none" stroke="'+BVC.o+'" stroke-width="1.5" stroke-dasharray="2.2 2"/>'+bvR(37.5,27.5,7,7,BVC.w,3.5)+bvR(7,24,22,4,BVC.w)+bvR(7,30,15,3,BVC.m)+bvR(8,50,6,12,BVC.a,1)+bvR(17,45,6,17,BVC.o,1)+bvR(26,54,6,8,BVC.w,1)+'<path d="M8 47 L19 42 L27 49 L35 39" fill="none" stroke="'+BVC.w+'" stroke-width="1.2"/>'+bvMan(44,62,0.62)+bvR(9,79,30,4,BVC.w)+bvR(13,85,22,3,BVC.a)),
    dahih:()=>bvPhone('<circle cx="10" cy="12" r="5" fill="#9b9b9b"/>'+bvR(18,8.5,28,4,BVC.w)+bvR(18,15,14,3,BVC.o)+bvR(0,24,56,54,BVC.pp,0)+bvMan(40,41,1.05,'#3b3e48','#2e3039')
      +'<g transform="rotate(-7 15 44)">'+bvR(5,36,20,15,'#FFFFFF',1,' stroke="#d4c9b2" stroke-width=".6"')+bvR(12,34,6,4,'#9a9aa6',1)+bvR(8,41,14,2,BVC.ink)+bvR(8,45,10,2,'#b9b09c')+'</g>'
      +'<circle cx="15" cy="64" r="6.5" fill="none" stroke="'+BVC.o+'" stroke-width="1.4"/><text x="15" y="66.3" font-size="6.4" font-weight="800" text-anchor="middle" fill="'+BVC.ink+'" font-family="sans-serif">87</text>'
      +bvR(22,83,12,4,BVC.o)+bvR(36,83,9,4,BVC.w))
  },
  pos:{ top:()=>bvPhone(bvMan(28,52,1.2)+bvCap(28,16,9)), mid:()=>bvPhone(bvMan(28,40,1.2)+bvCap(56,16,9)), bottom:()=>bvPhone(bvMan(28,40,1.2)+bvCap(76,16,9)) },
  media:{
    none:()=>bvPhone(bvMan(28,44,1.2)+bvCap(78,16,9)),
    search:()=>bvPhone(bvPhoto(6,8,44,30)+bvMan(28,56,1.05)+bvCap(84,16,9)),
    ai:()=>bvPhone(bvAI(6,8,44,30)+bvMan(28,56,1.05)+bvCap(84,16,9)),
    mix:()=>bvPhone(bvPhoto(4,7,28,22)+bvAI(22,17,30,22)+bvMan(28,56,1.05)+bvCap(84,16,9)),
    mine:()=>bvPhone(bvR(6,8,44,30,'none',2,' stroke="'+BVC.m+'" stroke-dasharray="2.5 2"')+'<path d="M28 30V16M22 21l6-6 6 6" fill="none" stroke="'+BVC.w+'" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'+bvMan(28,56,1.05)+bvCap(84,16,9))
  },
  length:(()=>{ const segs={keep:[[0,30],[32,42],[44,108]],tight:[[0,24],[34,52],[60,82],[92,108]],max60:[[10,34],[48,66],[80,96]],max30:[[16,34],[70,82]]};
    const f=k=>()=>{ const S=segs[k]; let top=bvR(6,9,108,6,'#2c2c36',3), len=0; S.forEach(s=>{ top+=bvR(6+s[0],9,s[1]-s[0],6,BVC.a,2); len+=s[1]-s[0]; }); return bvWide(top+bvR(6,27,len,6,BVC.a,3)+'<path d="M'+(8+len)+' 30h'+(Math.max(0,104-len))+'" stroke="#3a3a46" stroke-dasharray="2 3"/>'); };
    return {keep:f('keep'),tight:f('tight'),max30:f('max30'),max60:f('max60')}; })(),
  pace:(()=>{ const f=n=>()=>{ let o='', w=(108-(n-1)*2)/n; for(let i=0;i<n;i++) o+=bvR(6+i*(w+2),12,w,20,i%2?'#3a3e4b':'#4a4f5c',2); return bvWide(o+'<path d="M6 38h108" stroke="'+BVC.a+'" stroke-width="1.5" stroke-dasharray="'+(n>6?'2 2':n>3?'5 4':'10 8')+'"/>'); }; return {calm:f(3),normal:f(5),fast:f(9)}; })(),
  amount:(()=>{ const f=n=>()=>{ let o=bvR(6,26,108,3,'#2c2c36',1.5); for(let i=0;i<n;i++){ const x=8+i*(100/Math.max(1,n-1))*((n-1)/n)+50/n-4; o+=bvR(x,12,9,9,'#2c3e52',1.5)+bvR(x+4,21,1,5,BVC.m,0); } return bvWide(o); }; return {few:f(3),some:f(5),many:f(9)}; })(),
  sfx:(()=>{ const f=n=>()=>{ let d='M6 22'; for(let x=6;x<=114;x+=3) d+='L'+x+' '+(22+Math.sin(x*0.5)*((x*7)%11)/2.2); let o='<path d="'+d+'" fill="none" stroke="#4a4f5c" stroke-width="1.4"/>'; for(let i=0;i<n;i++){ const x=14+i*(92/Math.max(1,n-1)); o+='<path d="M'+x+' 8l3.5 3.5L'+x+' 15l-3.5-3.5Z" fill="'+BVC.a+'"/>'+bvR(x-.5,15,1,22,BVC.a,0,' opacity=".35"'); } return bvWide(o); }; return {none:f(0),light:f(2),rich:f(6)}; })(),
  tog:{
    'fx.zoom':()=>bvPhone(bvMan(28,40,1.7)+bvR(9,14,38,58,'none',2,' stroke="'+BVC.a+'" stroke-dasharray="3 2"')+bvCap(80,16,9)),
    'fx.transitions':()=>bvPhone(bvMan(18,44,1)+'<path d="M36 0L20 100H56V0Z" fill="#2c3e52"/><path d="M36 0L20 100" stroke="'+BVC.a+'" stroke-width="1.6"/>'+bvMan(42,44,0.9,'#7a7468','#5a554b')),
    'fx.bg':()=>bvPhone(bvMan(28,40,1.2)+'<path d="M8 80q5-8 10 0t10 0 10 0 10 0" fill="none" stroke="'+BVC.a+'" stroke-width="1.6"/>'),
    'en':()=>bvPhone(bvMan(28,38,1.2)+bvCap(70,16,9)+bvR(15,77,26,2.6,BVC.m)),
    'hook.use':()=>bvPhone(bvR(6,9,44,19,'#D97757',3)+bvR(11,14,34,3.4,BVC.w)+bvR(16,20,24,3.4,BVC.w)+bvMan(28,52,1.1)+bvCap(84,16,9)),
    'outro.use':()=>bvPhone(bvR(7,28,42,38,BVC.c,4,' stroke="'+BVC.bd+'"')+'<circle cx="28" cy="38" r="5" fill="'+BVC.p1+'"/>'+bvR(15,47,26,3,BVC.w)+bvR(13,55,30,6,BVC.a,3)),
    'media.video':()=>bvPhone(bvR(6,8,44,30,'#2c3e52',2)+'<path d="M24 16v14l12-7Z" fill="'+BVC.w+'"/>'+bvMan(28,56,1.05)+bvCap(84,16,9))
  }
};
function vtiles(id,group,opts,val){ const wide=!['style','pos','media'].includes(group);
  return '<div class="vts'+(wide?' wide':'')+'">'+opts.map(o=>'<button data-b="'+id+'" data-v="'+o+'" class="'+(val===o?'on':'')+'"><span class="vi">'+((BVIS[group]||{})[o]?BVIS[group][o]():'')+'</span><b>'+t('b_'+o)+'</b><small>'+t('bv_'+group+'_'+o)+'</small></button>').join('')+'</div>'; }

function frameRec(){ const P=(BRD&&BRD.platforms)||{}; const sets=(BR.platform||[]).map(k=>(P[k]||{}).frames||[]); if(!sets.length) return ['9:16']; const common=FRAMES.filter(f=>sets.every(s=>s.includes(f))); return common.length?common:[sets[0][0]]; }
function bget(p){ return p.split('.').reduce((o,k)=>o==null?undefined:o[k],BR); }
function bset(p,v){ const ks=p.split('.'); let o=BR; for(let i=0;i<ks.length-1;i++){ o[ks[i]]=o[ks[i]]||{}; o=o[ks[i]]; } o[ks[ks.length-1]]=v; }
async function openBrief(){ BRD=await api('/hs/brief'); const L=BRD.last||{}, A=BRD.ask||{};
  BR={ goal:L.goal||'explain', goalText:L.goalText||'', theme:{mode:'auto',bg:'#101014',acc:'#F2B33D',ink:'#FFFFFF',handle:'',...(L.theme||{})}, platform:(L.platform||['tiktok','instagram']).filter(x=>PLATS.includes(x)), frame:FRAMES.includes(L.frame)?L.frame:'9:16', length:L.length||'keep', pace:L.pace||'normal', look:L.look||'clean', pos:L.pos||'bottom', en:!!L.en,
    hook:{use:true,text:(A.hooks||[])[0]||'',variants:A.hooks||[]}, char:{use:'none',side:'left',...(L.char||{}),color:undefined}, media:{mode:'search',amount:'some',video:false,...(L.media||{}),topics:A.topics||[]},
    cards:['none','few','some','many'].includes(L.cards)?L.cards:'some', fx:{zoom:true,transitions:false,sfx:'light',bg:false,...(L.fx||{})}, cut:{fillers:BRD.fillers>0,dupes:(BRD.dupes||[]).length>0,drop:(BRD.dupes||[]).map(d=>d[0])}, brand:L.brand||'', outro:{use:false,text:'',handle:'',...(L.outro||{})}, extra:{}, notes:'', ref:'', style:(BRD.want&&BRD.want.style==='motion')?'motion':['normal','paper','dahih','motion'].includes(L.style)?L.style:'normal' };
  { const ids=BRD.ids||[], w=(BRD.want||{}).identity, has=s=>ids.some(x=>x.slug===s);   // 4.37: هويته المحفوظة مختارة لحالها
    if(BR.theme.mode==='newid') BR.theme.mode='auto';
    if(w==='none'){ if(BR.theme.mode==='identity') BR.theme.mode='auto'; }
    else if(w&&has(w)){ BR.theme.mode='identity'; BR.theme.identity=w; }
    else if(BR.theme.mode==='identity'||(BR.theme.mode==='auto'&&BRD.idDefault)){ const s=has(BR.theme.identity)?BR.theme.identity:BRD.idDefault; if(s&&has(s)){ BR.theme.mode='identity'; BR.theme.identity=s; } else BR.theme.mode='auto'; }
    BR.theme.idFiles=[]; delete BR.theme.idKey; }
  if(!(BRD.sound||[]).some(x=>x.id===BR.fx.src)) BR.fx.src='lib';
  renderBrief(); $('#brief').classList.add('on'); }
/* 4.37: الهوية: وحدة محفوظة (تنطبق على المونتاج والموشن والبودكاست) أو جديدة بملفات ووصف، وClaude يكتب identity.md مرة وحدة */
function idSecHtml(){ const IDS=BRD.ids||[], m=BR.theme.mode;
  if(m==='identity'&&IDS.length){ if(!IDS.some(x=>x.slug===BR.theme.identity)) BR.theme.identity=(IDS.find(x=>x.default)||IDS[0]).slug;
    return '<h4>'+t('idPick')+'</h4><div class="chips">'+IDS.map(x=>'<button data-b="theme.identity" data-v="'+esc(x.slug)+'" data-raw="1" class="'+(BR.theme.identity===x.slug?'on':'')+'"><span class="sw3 sm"><u style="background:'+esc(x.colors.bg)+'"></u><u style="background:'+esc(x.colors.acc)+'"></u></span> '+esc(x.name)+(x.default?' ★':'')+(x.draft?' <span class="tkb">'+t('idDraft')+'</span>':'')+'</button>').join('')+'</div><p class="hint" style="margin:8px 0 0">'+t('idHint')+'</p>'; }
  if(m!=='newid') return '';
  BR.theme.idKey=BR.theme.idKey||('new-'+Date.now().toString(36)); const fs=BR.theme.idFiles||[];
  return '<h4>'+t('idName')+'</h4><input type="text" dir="auto" data-bi="theme.idName" placeholder="'+t('idNamePh')+'" value="'+esc(BR.theme.idName||'')+'">'
    +'<h4>'+t('idText')+'</h4><textarea rows="3" dir="auto" data-bi="theme.idText" placeholder="'+t('idTextPh')+'">'+esc(BR.theme.idText||'')+'</textarea>'
    +'<h4>'+t('idFiles')+'</h4><label class="drop sm" style="display:block;cursor:pointer"><b>'+t('idFiles')+'</b> <small>'+t('idFilesSub')+'</small><input type="file" id="bIdFile" multiple hidden accept="image/*,.pdf,.md,.txt,.ttf,.otf,.woff,.woff2,.svg,.json"></label>'
    +(fs.length?'<div class="chips" style="margin-top:8px">'+fs.map(f=>'<span class="chip on">✓ '+esc(f)+'</span>').join('')+'</div>':'')
    +'<p class="hint" style="margin:8px 0 0">'+t('idNewHint')+'</p>'; }
document.addEventListener('change',async e=>{ if(e.target.id!=='bIdFile') return; const fs=[...e.target.files]; if(!fs.length) return; toast(t('uploading'));
  for(const f of fs){ const r=await api('/hs/identity_file?name='+encodeURIComponent(BR.theme.idKey),f,{'X-Name':encodeURIComponent(f.name)}); if(r.ok) (BR.theme.idFiles=BR.theme.idFiles||[]).push(f.name); else toast(srvEn(r.msg)||t('failed')); }
  renderBrief(); });
/* 4.19: منين الأصوات: المكتبة المجانية، أو خدمة مربوطة بحسابه (تصرف من رصيده) */
function sndSrcHtml(){ const P=BRD.sound||[]; if(BR.fx.sfx==='none') return ''; if(!P.length) return '<p class="hint" style="margin:6px 0 0">'+t('bqSrcNone')+'</p>';
  return '<h4>'+t('bqSrc')+'</h4><div class="chips">'+[['lib',t('bqSrcLib')],...P.map(p=>[p.id,p.name])].map(([k,l])=>'<button data-b="fx.src" data-v="'+esc(k)+'" class="'+(BR.fx.src===k?'on':'')+'">'+esc(l)+(k!=='lib'?' <span class="tkb">'+t('bqSrcCost')+'</span>':'')+'</button>').join('')+'</div>'+(BR.fx.src!=='lib'?'<p class="hint" style="margin:6px 0 0">'+t('bqSrcHint',esc((P.find(p=>p.id===BR.fx.src)||{}).name||''))+'</p>':''); }
function renderBrief(){ const A=BRD.ask||{}; let o='<div class="bin"><h2>'+t('bTitle')+'</h2><p class="hint" style="font-size:13px">'+t('bSub')+'</p>'+(A.note?'<div class="warnbox" dir="auto">'+esc(A.note)+'</div>':'')+(BRD.last?'<p class="hint">'+t('bLast')+'</p>':'');
  let _n=0; const sec=(n,title,body)=>'<div class="bsec"><h3><i>'+(++_n)+'</i>'+title+'</h3>'+body+'</div>';
  o+=sec(1,t('bqGoal'),chips('goal',B_OPTS.goal,BR.goal)+'<p class="hint" style="margin:8px 0 0">'+t('bg_goal_'+BR.goal)+'</p>'+(BR.goal==='other'?'<input type="text" dir="auto" data-bi="goalText" placeholder="'+t('bqGoalOther')+'" value="'+esc(BR.goalText||'')+'" style="margin-top:10px">':'')
    +'<h4>'+t('bqPlatform')+'</h4>'+chips('platform',B_OPTS.platform,BR.platform,true)+BR.platform.map(k=>'<p class="hint" style="margin:8px 0 0"><b>'+t('b_'+k)+'</b>: '+t('pf_'+k)+'</p>').join('')
    +'<h4>'+t('bqFrame')+'</h4><div class="frames">'+FRAMES.map(f=>{ const [a,b]=f.split(':').map(Number), rec=frameRec().includes(f); return '<button data-b="frame" data-v="'+f+'" class="'+(BR.frame===f?'on':'')+'"><i style="aspect-ratio:'+a+'/'+b+';'+(a>b?'width:44px':'height:44px')+'"></i><b>'+t('bf_'+f.replace(':','x'))+'</b><small>'+f+(rec?' · '+t('bfRec'):'')+'</small></button>'; }).join('')+'</div><p class="hint" style="margin-top:8px">'+t('fh_'+BR.frame.replace(':','x'))+'</p>');
  const IDS=BRD.ids||[], idSel=IDS.find(x=>x.slug===BR.theme.identity)||IDS.find(x=>x.default)||IDS[0];
  o+=sec('★',t('bqTheme'),'<div class="frames">'+[...(IDS.length?['identity']:[]),'newid','auto','mono','custom'].map(m=>{ const c=m==='identity'?[idSel.colors.bg,idSel.colors.acc,idSel.colors.ink]:m==='newid'?['transparent','transparent','transparent']:m==='mono'?['#0E0E10','#FFE14D','#FFFFFF']:m==='custom'?[BR.theme.bg,BR.theme.acc,BR.theme.ink]:['#1B2A4A','#F2B33D','#FFFFFF']; return '<button data-b="theme.mode" data-v="'+m+'" class="'+(BR.theme.mode===m?'on':'')+'"><span class="sw3'+(m==='newid'?' dash':'')+'"><u style="background:'+c[0]+'"></u><u style="background:'+c[1]+'"></u><u style="background:'+c[2]+'"></u></span><b>'+t('bt_'+m)+'</b><small>'+t('bts_'+m)+'</small></button>'; }).join('')+'</div>'+idSecHtml()+(BR.theme.mode==='custom'?'<div class="row3"><label>'+t('btBg')+'<input type="color" data-bi="theme.bg" value="'+esc(BR.theme.bg)+'"></label><label>'+t('btAcc')+'<input type="color" data-bi="theme.acc" value="'+esc(BR.theme.acc)+'"></label><label>'+t('btInk')+'<input type="color" data-bi="theme.ink" value="'+esc(BR.theme.ink)+'"></label></div>':'')+'<h4>'+t('btHandle')+'</h4><input type="text" dir="ltr" data-bi="theme.handle" placeholder="@handle" value="'+esc(BR.theme.handle||'')+'">');
  o+=sec('S',t('bqStyle'),vtiles('style','style',['normal','motion','podcast','paper','dahih'],BR.style||'normal')+'<p class="hint">'+t('bqStyleH_'+(BR.style||'normal'))+'</p>');
  o+=sec(2,t('bqLength'),vtiles('length','length',B_OPTS.length,BR.length)+'<h4>'+t('bqPace')+'</h4>'+vtiles('pace','pace',B_OPTS.pace,BR.pace));
  o+=sec(3,t('bqCap'),'<div class="grid3 g6">'+Object.keys(CAPPRE).map(k=>preTile(k).replace('class="tile"','class="tile'+(BR.look===k?' sel':'')+'"')).join('')+'</div><h4>'+t('bqPos')+'</h4>'+vtiles('pos','pos',B_OPTS.pos,BR.pos)+btog('en',t('bqEn'),t('bqEnSub'),BR.en));
  o+=sec(4,t('bqHook'),btog('hook.use',t('bqHookUse'),t('bqHookSub'),BR.hook.use)+(BR.hook.use?(BR.hook.variants||[]).map((h,i)=>'<label class="item"><input type="radio" name="bhk" data-bhk="'+i+'"'+(BR.hook.text===h?' checked':'')+'><span dir="auto">'+esc(h)+'</span></label>').join('')+'<input type="text" dir="auto" data-bi="hook.text" placeholder="'+t('bqHookOwn')+'" value="'+esc(BR.hook.text||'')+'">':''));
  o+=sec(5,t('bqChar'),'<div class="grid3 g6"><div class="tile'+(BR.char.use==='none'?' sel':'')+'" data-bchar="none"><div class="pv">'+t('b_nochar')+'</div><span>'+t('b_none')+'</span></div>'+CHARS.map(c=>'<div class="tile'+(BR.char.use===c?' sel':'')+'" data-bchar="'+c+'"><div class="pv"><canvas data-spr="'+c+'" width="56" height="56"></canvas></div><span>'+t('char_'+c)+'</span></div>').join('')+'</div>'+(BR.char.use!=='none'?'<h4>'+t('bqCharSide')+'</h4><div class="chips"><button data-b="char.side" data-v="left" class="'+(BR.char.side==='left'?'on':'')+'">'+t('b_left')+'</button><button data-b="char.side" data-v="right" class="'+(BR.char.side==='right'?'on':'')+'">'+t('b_right')+'</button></div>':'')+'<p class="hint">'+t('bqCharHint')+'</p>');
  o+=sec(6,t('bqMedia'),vtiles('media.mode','media',B_OPTS.media,BR.media.mode)+(BR.media.mode!=='none'&&BR.media.mode!=='mine'?'<h4>'+t('bqTopics')+'</h4><input type="text" dir="auto" data-bi="media.topicsText" placeholder="'+t('bqTopicsPh')+'" value="'+esc((BR.media.topics||[]).join(LANG==='en'?', ':'، '))+'"><h4>'+t('bqAmount')+'</h4>'+vtiles('media.amount','amount',B_OPTS.amount,BR.media.amount)+(BR.media.mode==='ai'||BR.media.mode==='mix'?btog('media.video',t('bqVideo'),t('bqVideoSub'),BR.media.video):''):'')+'<p class="hint">'+t('bqMediaHint')+'</p>');
  o+=sec('c',t('bqCards'),'<div class="chips">'+['none','few','some','many'].map(v=>'<button data-b="cards" data-v="'+v+'" class="'+(BR.cards===v?'on':'')+'">'+t('cd_'+v)+'</button>').join('')+'</div><div class="grid3 g6" style="margin-top:12px;pointer-events:none;opacity:.85">'+CARDS.slice(0,6).map(k=>'<div class="tile"><div class="pv cdp">'+CARDPV[k]+'</div><span>'+t('cs2_'+k)+'</span></div>').join('')+'</div><p class="hint">'+t('bqCardsHint')+'</p>');
  o+=sec(7,t('bqFx'),btog('fx.zoom',t('bqZoom'),'',BR.fx.zoom)+btog('fx.transitions',t('bqTrans'),'',BR.fx.transitions)+'<h4>'+t('bqSfx')+'</h4>'+vtiles('fx.sfx','sfx',B_OPTS.sfx,BR.fx.sfx)+sndSrcHtml()+btog('fx.bg',t('bqBg'),t('bqBgSub'),BR.fx.bg));
  const cards=BRD.cards||[]; o+=sec(8,t('bqCut'),(BRD.fillers?btog('cut.fillers',t('bqFillers',BRD.fillers),'',BR.cut.fillers):'')+((BRD.dupes||[]).length?btog('cut.dupes',t('bqDupes',BRD.dupes.length),'',BR.cut.dupes):'')+(cards.length?'<h4>'+t('bqDrop')+'</h4><div class="bcards">'+cards.map((c,i)=>'<label class="item"><input type="checkbox" data-bdrop="'+i+'"'+(BR.cut.drop.includes(i)?' checked':'')+'><span dir="rtl">'+esc(c)+'</span></label>').join('')+'</div>':'<p class="hint">'+t('bqNoText')+'</p>'));
  o+=sec(9,t('bqEnd'),btog('outro.use',t('bqOutro'),'',BR.outro.use)+(BR.outro.use?'<input type="text" dir="auto" data-bi="outro.text" placeholder="'+t('bqOutroPh')+'" value="'+esc(BR.outro.text)+'" style="margin-bottom:8px"><input type="text" dir="ltr" data-bi="outro.handle" placeholder="@handle" value="'+esc(BR.outro.handle)+'">':'')+((BRD.brands||[]).length?'<h4>'+t('brand')+'</h4><div class="chips"><button data-b="brand" data-v="" class="'+(!BR.brand?'on':'')+'">'+t('b_none')+'</button>'+BRD.brands.map(b=>'<button data-b="brand" data-v="'+esc(b)+'" data-raw="1" class="'+(BR.brand===b?'on':'')+'">'+esc(b)+'</button>').join('')+'</div>':''));
  if((A.extra||[]).length) o+=sec(10,t('bqExtra'),A.extra.map(q=>'<h4 dir="auto">'+esc(q.q)+'</h4>'+((q.options||[]).length?'<div class="chips">'+q.options.map(x=>'<button data-b="extra.'+esc(q.id)+'" data-v="'+esc(x)+'" data-raw="1" class="'+(BR.extra[q.id]===x?'on':'')+'">'+esc(x)+'</button>').join('')+'</div>':'<input type="text" dir="auto" data-bi="extra.'+esc(q.id)+'" value="'+esc(BR.extra[q.id]||'')+'">')).join(''));
  o+=sec((A.extra||[]).length?11:10,t('bqNotes'),'<textarea rows="3" dir="auto" data-bi="notes" placeholder="'+t('bqNotesPh')+'">'+esc(BR.notes)+'</textarea><input type="text" dir="ltr" data-bi="ref" placeholder="'+t('bqRefPh')+'" value="'+esc(BR.ref)+'" style="margin-top:8px">');
  o+='<div class="bsave"><button class="pri" id="bSave">'+t('bSave')+'</button><span class="hint">'+t('bSaveHint')+'</span></div></div>';
  const el=$('#brief'), y=el.scrollTop; el.dir=LANG==='ar'?'rtl':'ltr'; el.innerHTML=o; el.scrollTop=y; drawSprites(); }
$('#brief').addEventListener('click',async e=>{ const el=e.target.closest('[data-b],[data-bt],[data-cappre],[data-bchar],#bSave'); if(!el) return; const d=el.dataset;
  if(d.b){ const raw=d.raw; if(d.m){ const a=bget(d.b)||[]; bset(d.b,a.includes(d.v)?a.filter(x=>x!==d.v):[...a,d.v]); } else bset(d.b,d.v); renderBrief(); return; }
  if(d.bt){ bset(d.bt,!bget(d.bt)); renderBrief(); return; }
  if(d.cappre){ BR.look=d.cappre; renderBrief(); return; }
  if(d.bchar){ BR.char.use=d.bchar; renderBrief(); return; }
  if(el.id==='bSave'){ if(BR.goal==='other'&&!(BR.goalText||'').trim()){ toast(t('bqGoalNeed')); return; } if(BR.theme.mode==='newid'&&!(BR.theme.idText||'').trim()&&!(BR.theme.idFiles||[]).length){ toast(t('idNeed')); return; } if(!BR.platform.length){ toast(t('bqPlatNeed')); return; } const a=JSON.parse(JSON.stringify(BR)); a.cap={...capStyle(a.look),y:POSY[a.pos]||76,on:true}; if(a.media.topicsText!==undefined){ a.media.topics=a.media.topicsText.split(/[،,]/).map(x=>x.trim()).filter(Boolean); delete a.media.topicsText; }
    if(a.char.use!=='none'&&!a.char.color) a.char.color={robo:'#8F73F5',sprout:'#43B072',star:'#F2B33D',cube:'#4C8DFF'}[a.char.use];
    el.disabled=true; const r=await api('/hs/brief_save',{answers:a}); if(r.ok){ $('#brief').classList.remove('on'); PULSE.brief='saved'; BRW=Date.now(); BRLAST=lastAct; stLoader('brief',t('brWaitSub')); } else { el.disabled=false; toast(srvEn(r.msg)||t('failed')); } } });
$('#brief').addEventListener('input',e=>{ const d=e.target.dataset; if(d.bi) bset(d.bi,e.target.value); });
$('#brief').addEventListener('change',e=>{ if(e.target.type==='color') renderBrief(); });
$('#brief').addEventListener('change',e=>{ const d=e.target.dataset; if(d.bhk!==undefined){ BR.hook.text=BR.hook.variants[+d.bhk]; renderBrief(); } if(d.bdrop!==undefined){ const i=+d.bdrop; BR.cut.drop=e.target.checked?[...new Set([...BR.cut.drop,i])]:BR.cut.drop.filter(x=>x!==i); } });

/* ═══════════ v3: بحث الصور + التوليد ═══════════ */
let MEDIA={q:'',items:[],busy:false,fit:'card',msg:''};
function mediaHtml(){ let o='<div class="sec"><h4>'+t('binSearch')+'</h4><div class="row"><input type="search" id="mq" dir="auto" placeholder="'+t('searchPh')+'" value="'+esc(MEDIA.q)+'"><button class="sm" id="mGo">'+t('search')+'</button></div><div class="seg" style="margin-bottom:8px"><button data-mkind="image" class="'+(MEDIA.kind!=='video'?'on':'')+'">'+t('mkImage')+'</button><button data-mkind="video" class="'+(MEDIA.kind==='video'?'on':'')+'">'+t('mkVideo')+'</button></div><div class="seg" style="margin-bottom:8px;'+(MEDIA.kind==='video'?'display:none':'')+'"><button data-mfit="card" class="'+(MEDIA.fit==='card'?'on':'')+'">'+t('fitCard')+'</button><button data-mfit="cover" class="'+(MEDIA.fit==='cover'?'on':'')+'">'+t('fitCover')+'</button></div>';
  if(MEDIA.busy) o+='<p class="hint">'+t('searching')+'</p>'; else if(MEDIA.msg) o+='<p class="hint">'+esc(MEDIA.msg)+'</p>';
  o+='<div class="grid3">'+MEDIA.items.map((m,i)=>'<div class="tile" data-madd="'+i+'" title="'+esc(m.title+' · '+m.lic+' · '+m.author)+'"><div class="pv" style="background-image:url('+esc(m.thumb)+')"></div><span>'+(m.kind==='video'?esc(m.dur+'s · '):'')+esc(m.lic)+'</span></div>').join('')+'</div><p class="hint">'+t(MEDIA.kind==='video'?'searchHintV':'searchHint')+'</p></div>';
  o+='<div class="sec"><h4>'+t('binGen')+'</h4><textarea id="gTx" rows="2" dir="auto" placeholder="'+t('genPh')+'"></textarea><div class="row" style="margin-top:8px"><button class="sm" data-gen="image">'+t('genImage')+'</button><button class="sm" data-gen="video">'+t('genVideo')+'</button></div>'
    +(INFO.gen||[]).slice().reverse().map(r=>'<div class="greq'+(r.status==='done'?' done':'')+'"><div class="gp" dir="auto"><b>'+t(r.kind==='image'?'genKImg':'genKVid')+'</b> '+esc(r.prompt)+'</div>'+(r.status==='done'?'<small>'+t('genDone')+' · '+esc(r.file||'')+'</small>':'<div class="row" style="margin:6px 0 0;flex-wrap:wrap"><button class="sm" data-gopen="'+r.id+'">'+t(r.kind==='image'?'genOpenImg':'genOpenVid')+'</button><button class="sm" data-gup="'+r.id+'">'+t('genUpload')+'</button><button class="sm ghost" data-gcl="'+r.id+'">'+t('genViaClaude')+'</button><button class="sm ghost" data-grm="'+r.id+'">'+t('delete')+'</button></div>')+'</div>').join('')
    +'<p class="hint">'+t('genHint')+'</p></div>';
  return o; }
async function mediaSearch(){ const q=$('#mq').value.trim(); if(!q) return; MEDIA.q=q; MEDIA.busy=true; MEDIA.msg=''; renderLeft(); const r=await api('/hs/media_search?q='+encodeURIComponent(q)+(MEDIA.kind==='video'?'&kind=video':'')); MEDIA.busy=false; MEDIA.items=r.items||[]; MEDIA.msg=r.ok?(MEDIA.items.length?'':t('searchNone')):(srvEn(r.msg)||t('failed')); renderLeft(); }
async function genAsk(kind){ const p=$('#gTx').value.trim(); if(!p){ toast(t('genEmpty')); return; } const r=await api('/hs/gen',{kind,prompt:p,at:T,fit:MEDIA.fit});
  if(!r.ok){ toast(srvEn(r.msg)||t('failed')); return; } INFO.gen=r.gen; renderLeft(); toast(t('genSaved')); }
function genReq(id){ return (INFO.gen||[]).find(r=>String(r.id)===String(id)); }
async function genOpen(id){ const r=genReq(id); if(!r) return; try{ await navigator.clipboard.writeText(r.text); toast(t('genCopied')); }catch(e){ modal('<h3>'+t('genCopyTitle')+'</h3><div class="copy"><span dir="ltr" style="text-align:left;user-select:all">'+esc(r.text)+'</span></div><div class="row" style="margin:14px 0 0"><button id="qNo">'+t('close')+'</button></div>'); $('#qNo').onclick=closeModal; }
  window.open(r.kind==='image'?r.site+'?q='+encodeURIComponent(r.text):r.site,'_blank','noopener'); }
function genUpload(id){ const i=document.createElement('input'); i.type='file'; i.accept='image/png,image/jpeg,image/webp,video/mp4,video/quicktime,video/webm'; i.onchange=async()=>{ const f=i.files[0]; if(!f) return; toast(t('uploading')); await save();
    const res=await fetch('/hs/gen_import',{method:'POST',headers:{'X-Name':encodeURIComponent(f.name),'X-Id':String(id)},body:f}); const r=await res.json().catch(()=>({ok:false})); if(!r.ok){ toast(srvEn(r.msg)||t('failed')); return; } await load(true); toast(t('genAdded')); }; i.click(); }
async function genRm(id){ const r=await api('/hs/gen_rm',{id}); if(r.ok){ INFO.gen=r.gen; renderLeft(); } }
function genClaude(id){ const r=genReq(id); if(r) runAgent(t('reqGen',r.id,r.kind==='image'?'ChatGPT (chatgpt.com)':'Gemini (gemini.google.com)'),true); }
/* ═══════════ 3.4: واجهة الجوال (/m) ═══════════ */
const MOBILE=document.body.classList.contains('m');
const MVIEWS=[['notes','panel','notes'],['sel','panel','sel'],['takes','bin','takes'],['text','bin','text'],['cap','panel','cap'],['plan','panel','plan'],['tr','panel','tr'],['audio','panel','audio'],['files','bin','files'],['proj','panel','proj'],['check','panel','check'],['pub','panel','pub'],['claude','panel','claude']];
let _mS={}; const _mSet=(id,v,html)=>{ if(_mS[id]===v) return; _mS[id]=v; const e=$('#'+id); if(e){ if(html) e.innerHTML=v; else e.textContent=v; } };
function mSync(){ const sc=$('#mScrub'); if(!sc||!ST) return; _mSet('mNow',fmt(T).replace(/\.\d+$/,'')); _mSet('mDur',fmt(dur()).replace(/\.\d+$/,'')); _mSet('mPlay2',playing?'<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16" rx="1"/><rect x="14" y="4" width="4" height="16" rx="1"/></svg>':'<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M7 4l13 8-13 8z"/></svg>',1); if(document.activeElement!==sc){ const mx=String(dur()||1); if(sc.max!==mx) sc.max=mx; sc.value=T; } _mSet('mTime',fmt(T)+' / '+fmt(dur())); _mSet('mPlay',t(playing?'pause':'play')); }
function mView(k){ const v=MVIEWS.find(x=>x[0]===k)||MVIEWS[0]; document.body.dataset.mv=v[1]; if(v[1]==='bin') LTAB=v[2]; else RTAB=v[2]; if(LTAB==='takes'&&v[1]==='bin') loadTakes(); $$('#mnav button,#mtabs button').forEach(b=>b.classList.toggle('on',b.dataset.mv===k)); if(ST){ markTabs(); renderLeft(); renderRight(); } mSync(); const sc=$('#mid'); if(sc) sc.scrollTop=0; }
if(MOBILE){ $('#mnav').innerHTML=MVIEWS.map(v=>'<button data-mv="'+v[0]+'" data-t="mv_'+v[0]+'"></button>').join('');
  $('#mtabs').innerHTML=MVIEWS.map(v=>'<button data-mv="'+v[0]+'"></button>').join('');
  $('#mshBody').appendChild($('#bin')); $('#mshBody').appendChild($('#panel'));
  $('#mtabs').addEventListener('click',e=>{ const b=e.target.closest('[data-mv]'); if(b) mView(b.dataset.mv); });
  $('#mnav').addEventListener('click',e=>{ const b=e.target.closest('[data-mv]'); if(b) mView(b.dataset.mv); });
  $('#mPlay').onclick=()=>play(); $('#mScrub').addEventListener('input',e=>{ if(playing) stop(); seek(+e.target.value); });
  $('#mBack').onclick=()=>seek(Math.max(0,T-2)); $('#mFwd').onclick=()=>seek(Math.min(dur(),T+2));
  const close=()=>{ document.body.dataset.mv=''; };
  $('#mshClose').onclick=close; $('#msh').addEventListener('click',e=>{ if(e.target.id==='msh') close(); });
  $('#mList').onclick=()=>mView('notes'); $('#mKb').onclick=()=>openNote(); $('#mExport').onclick=()=>{ close(); $('#bExport').click(); };
  document.body.dataset.mv=''; setTimeout(()=>{ applyLang(); mTabs(); },0); }
function mTabs(){ if(!MOBILE) return; $$('#mtabs button').forEach(b=>{ const k=b.dataset.mv; b.textContent=k==='notes'?t('mv_notes'):k==='text'?t('tabText'):k==='files'?t('tabFiles'):k==='takes'?t('tabTakes'):t('tab_'+k); }); }
/* 4.3: أدوات الشريط (للجوال والكمبيوتر) */
if(!MOBILE){ const st=$('#stage'), mt=$('#mtools'); if(st&&mt) st.insertBefore(mt,$('#stageBtns')); }
$('#mPlay2').onclick=()=>play(); $('#mUndo').onclick=undo; $('#mRedo').onclick=redo;
$('#mMark').onclick=async()=>{ if(!ST) return; await save(); const r=await api('/hs/ver_save',{name:t('markName',fmt(T))}); if(r.ok){ INFO.versions=r.versions; toast(t('markSaved')); } };
$('#mCut').onclick=()=>{ buzz(10); splitAt(T); };
function splitAt(x){ if(!ST) return; let k=SEL;
  if(k&&(k.kind==='audio'||k.kind==='video')){ const m=r3(x); if(m<=k.s+0.1||m>=k.e-0.1){ toast(t('auSplitOut')); return; } if(!MARKS.some(q=>Math.abs(q-m)<0.05)){ MARKS.push(m); MARKS.sort((a,b)=>a-b); marksSave(); } select({kind:k.kind,s:k.s,e:m,id:k.id,solo:k.solo}); toast(t('splitDone')); return; }
  if(k&&k.kind==='sfx'){ blade({dataset:{kind:'sfx',id:String(k.id)}},x); return; }
  if(!k||!['layer','cap','broll'].includes(k.kind)){ const ci=cardAt(x); if(ci<0){ toast(t('cutNothing')); return; } k={kind:'cap',id:ci}; }
  const was=TOOL; blade({dataset:{kind:k.kind,id:String(k.id)}},x); TOOL=was; }
$('#wrap').addEventListener('pointerdown',e=>{ if(!PICK) return; e.preventDefault(); e.stopPropagation(); const r=$('#wrap').getBoundingClientRect(); pickAt(clamp((e.clientX-r.left)/r.width,0,1),clamp((e.clientY-r.top)/r.height,0,1)); },true);
document.addEventListener('keydown',e=>{ if(PICK&&e.key==='Escape'){ pickEnd(); toast(t('akPickOff')); } });
$('#bFull').onclick=()=>{ const w=$('#wrap'); try{ if(document.fullscreenElement) document.exitFullscreen(); else (w.requestFullscreen||w.webkitRequestFullscreen).call(w); }catch(e){} };
$('#bPen').onclick=()=>openNote();
let HUBU=null;
function hubBack(){ const ck=document.cookie.includes('hs_hub=1'); const local=['127.0.0.1','localhost'].includes(location.hostname); const u=ck?'/library':(INFO&&INFO.hub&&local?INFO.hub:null); HUBU=u; const b=$('#bBack'); b.hidden=!u; b.title=t('backLib'); b.dataset.l=t('back_lib'); if(u) b.onclick=async()=>{ b.disabled=true; await saveNow(); location.href=u; }; }
/* 4.53: وقت ما Claude يشتغل: بطاقة بالمساحة الفاضية بين المقطع واللوحة اليمين، ما تغطي المقطع ولا اللوحات. لو المساحة ضيقة ترجع الشارة الصغيرة فوق */
function workCard(p){ const run=!!(p&&p.agent&&p.agent.running), st=$('#stage'), wr=$('#wrap'), tl=$('#sideTools'); let c=$('#workc');
  if(!run||!ST||!st||!wr||MOBILE||document.body.classList.contains('full')){ if(c) c.remove(); document.body.classList.remove('wcard'); return false; }
  const S=st.getBoundingClientRect(), W=wr.getBoundingClientRect(), K=tl?tl.getBoundingClientRect():null; let x0, x1;
  if(document.dir==='rtl'||document.documentElement.dir==='rtl'){ x0=W.right; x1=K&&K.width&&K.left>W.right?K.left:S.right; } else { x0=K&&K.width&&K.right<W.left?K.right:S.left; x1=W.left; }
  const gw=x1-x0-28; if(gw<150){ if(c) c.remove(); document.body.classList.remove('wcard'); return false; }
  if(!c){ c=document.createElement('div'); c.id='workc'; c.innerHTML='<div class="wc-logo">'+clLogo(30)+'</div><b>'+esc(t('wbClaude'))+'</b><span class="wc-t" dir="ltr"></span><p class="wc-live" dir="auto"></p><button class="sm ghost" id="agStop">'+t('stop')+'</button>'; st.appendChild(c); requestAnimationFrame(()=>c.classList.add('on')); }
  const w=Math.min(230,gw); c.style.width=w+'px'; c.style.left=Math.round(x0-S.left+(x1-x0-w)/2)+'px'; c.style.top=Math.round(W.top-S.top+W.height/2)+'px'; document.body.classList.add('wcard');
  const el=p.agent.elapsed||0, t0=Date.now()-el*1000-3000, last=[...ACT].reverse().find(a=>(a.kind==='tool'||a.kind==='claude')&&a.t*1000>=t0);
  c.querySelector('.wc-t').textContent=fmtm(el); const lv=c.querySelector('.wc-live'), tx=last?srvEn(String(last.text)).replace(/\s+/g,' ').slice(0,90):''; if(lv.textContent!==tx) lv.textContent=tx; return true; }
function workBadge(p){ if(workCard(p)){ const ow=$('#workb'); if(ow) ow.remove(); return; } let w=$('#workb'); const run=!!(p&&p.agent&&p.agent.running), nr=!!(p&&!p.ready&&READY&&ST);
  if(!run&&!nr){ if(w) w.remove(); return; }
  if(!w){ w=document.createElement('div'); w.id='workb'; $('#stage').appendChild(w); }
  const el=run?(p.agent.elapsed||0):0; w.innerHTML='<i></i><span>'+esc(t(run?'wbClaude':'wbPrep'))+(run?' · <bdi dir="ltr">'+fmtm(el)+'</bdi>':'')+'</span>'+(run?'<button class="sm ghost" id="agStop">'+t('stop')+'</button>':''); }
function pillSync(){ const el=$('#pill'); if(!el||!INFO) return; const p=PULSE||{}; let k='', s='';
  if(p.agent&&p.agent.running){ k='work'; s=t('pillClaude'); } else if(p.job&&p.job.running){ k='work'; s=t('pillExport'); }
  else if(!(INFO.exports||[]).length){ k='dirty'; s=t('pillNoExport'); } else if((LASTSAVE||0)/1000>(INFO.exportMt||0)+2||(INFO.studioMt||0)>(INFO.exportMt||0)+2){ k='dirty'; s=t('pillDirty'); } else { k='ready'; s=t('pillReady'); }
  el.className='pill '+k; el.querySelector('span').textContent=s; }
let LASTSAVE=0;
/* 4.3: ملاحظة بالصوت: اضغط مطوّل وتكلّم */
const REC={mr:null,chunks:[],t0:0,at:0,short:false,tm:null};
async function recStart(btn){ if(!ST||REC.mr&&REC.mr.state==='recording') return; if(!(window.isSecureContext&&navigator.mediaDevices&&window.MediaRecorder)){ toast(t('micNeedHttps')); openNote(); return; }
  let st; try{ st=await navigator.mediaDevices.getUserMedia({audio:true}); }catch(e){ toast(t('micDenied')); return; }
  if(playing) stop(); REC.at=T; REC.chunks=[]; REC.short=false; const mr=new MediaRecorder(st); REC.mr=mr; REC.btn=btn;
  mr.ondataavailable=e=>{ if(e.data&&e.data.size) REC.chunks.push(e.data); }; mr.onstop=()=>{ st.getTracks().forEach(x=>x.stop()); recSend(); };
  mr.start(); buzz(20); REC.t0=Date.now(); btn.classList.add('rec'); $('#rec').classList.add('on'); const up=()=>{ $('#recTx').textContent=t('micRec',Math.round((Date.now()-REC.t0)/1000)); }; up(); REC.tm=setInterval(up,500);
  if(REC.pending){ REC.pending=false; recStop(); } }
function recStop(){ if(!REC.mr||REC.mr.state!=='recording'){ REC.pending=true; setTimeout(()=>REC.pending=false,1500); return; } REC.short=Date.now()-REC.t0<700; REC.mr.stop(); clearInterval(REC.tm); $('#rec').classList.remove('on'); if(REC.btn) REC.btn.classList.remove('rec'); }
async function recSend(){ if(REC.short||!REC.chunks.length){ toast(t('micHold')); return; } const b=new Blob(REC.chunks,{type:(REC.mr&&REC.mr.mimeType)||'audio/webm'}); const ci=cardAt(REC.at);
  let r; try{ r=await fetch('/hs/voice_note?t='+REC.at+'&card='+(ci>=0?ci:''),{method:'POST',headers:{'Content-Type':b.type},body:b}).then(x=>x.json()); }catch(e){ r={ok:false}; }
  if(r&&r.ok){ NOTES=r.notes; buildTL(); if(RTAB==='notes') renderRight(); toast(t('micSaved')); setTimeout(async()=>{ NOTES=await api('/hs/notes'); buildTL(); if(RTAB==='notes') renderRight(); },20000); } else toast((r&&srvEn(r.msg))||t('failed')); }
for(const id of ['#bMic','#mMic']){ const b=$(id); if(!b) continue; b.addEventListener('pointerdown',e=>{ e.preventDefault(); recStart(b); }); ['pointerup','pointercancel','pointerleave'].forEach(ev=>b.addEventListener(ev,()=>{ if(REC.mr&&REC.mr.state==='recording'||REC.btn===b) recStop(); })); b.addEventListener('contextmenu',e=>e.preventDefault()); }

/* ═══════════ 4.3: لمستنا ═══════════ */
const buzz=n=>{ try{ navigator.vibrate&&navigator.vibrate(n||12); }catch(e){} };
/* يكمل من وين وقفت */
let _posT=0; function posSave(){ if(!INFO||!ST) return; clearTimeout(_posT); _posT=setTimeout(()=>{ try{ localStorage.setItem('hsPos:'+INFO.work,String(r3(T))); }catch(e){} },400); }
let _posDone=false; function posRestore(){ if(_posDone||!INFO) return; _posDone=true; try{ const v=+localStorage.getItem('hsPos:'+INFO.work); if(v>0.5&&v<dur()-0.5){ seek(v); toast(t('resumed',fmt(v).replace(/\.\d+$/,''))); } }catch(e){} }
/* شريط Claude الحي فوق المعاينة */
function tickerSync(p){ const el=$('#ticker'); if(!el) return; const on=!!(p&&p.agent&&p.agent.running); el.classList.toggle('on',on);
  if(on){ const last=[...ACT].reverse().find(a=>a.kind==='claude'||a.kind==='tool'||a.kind==='ask'); $('#tickTx').textContent=t('tickWorking')+(last?' · '+String(last.text).replace(/\s+/g,' ').slice(0,90):''); } }
$('#ticker').onclick=()=>{ if(MOBILE) mView('claude'); else { RTAB='claude'; markTabs(); renderRight(); } };
/* طلبات بضغطة */
const QUICK=['qkFillers','qk30','qkCards','qkHook','qkCaps','qkEn'];
function quickHtml(){ return '<div class="sec"><h4>'+t('qkTitle')+'</h4><div class="quick">'+QUICK.map(k=>'<button class="sm" data-quick="'+k+'">'+t(k)+'</button>').join('')+'</div></div>'; }
document.addEventListener('click',e=>{ const b=e.target.closest('[data-quick]'); if(!b) return; buzz(); runAgent(t(b.dataset.quick+'_task')); toast(t('qkSent')); });
/* إيماءات المعاينة: ضغطتين = تشغيل/إيقاف · سحب يمين/يسار = الجملة اللي قبل/بعد */
(function(){ const st=$('#stage'); let x0=0,y0=0,t0=0,lastTap=0;
  const GI={prev:'<svg width="44" height="44" viewBox="0 0 24 24" fill="#fff"><path d="M6 5h2v14H6zM20 5v14L9 12z"/></svg>',next:'<svg width="44" height="44" viewBox="0 0 24 24" fill="#fff"><path d="M16 5h2v14h-2zM4 5v14l11-7z"/></svg>',play:'<svg width="44" height="44" viewBox="0 0 24 24" fill="#fff"><path d="M7 4l13 8-13 8z"/></svg>',pause:'<svg width="44" height="44" viewBox="0 0 24 24" fill="#fff"><rect x="6" y="4" width="4" height="16" rx="1"/><rect x="14" y="4" width="4" height="16" rx="1"/></svg>'};
  const hint=s=>{ const h=$('#gestHint'); h.innerHTML=GI[s]||''; h.classList.add('on'); clearTimeout(hint._t); hint._t=setTimeout(()=>h.classList.remove('on'),500); };
  st.addEventListener('touchstart',e=>{ if(e.target.closest('button,#giz')||e.touches.length>1) return; x0=e.touches[0].clientX; y0=e.touches[0].clientY; t0=Date.now(); },{passive:true});
  st.addEventListener('touchend',e=>{ if(!ST||e.target.closest('button,#giz')||!t0) return; const dx=e.changedTouches[0].clientX-x0, dy=e.changedTouches[0].clientY-y0, dt=Date.now()-t0; t0=0;
    if(Math.abs(dx)>60&&Math.abs(dy)<50&&dt<600){ const cs=ST.caps.cards;
      const back=document.documentElement.dir==='rtl'?dx<0:dx>0; let tgt=null;
      if(!back){ const n=cs.find(c=>c.s>T+0.05); tgt=n?n.s:null; } else { const prev=[...cs].reverse().find(c=>c.s<T-0.3); tgt=prev?prev.s:0; }
      if(tgt!=null){ if(playing) stop(); seek(tgt); buzz(8); hint(back?'prev':'next'); } return; }
    if(Math.abs(dx)<10&&Math.abs(dy)<10&&dt<300){ const now=Date.now(); if(now-lastTap<320){ lastTap=0; play(); hint(playing?'play':'pause'); buzz(8); } else lastTap=now; } },{passive:true});
  st.addEventListener('dblclick',e=>{ if(!ST||e.target.closest('button')) return; play(); });
})();
/* قرصة على التايم لاين = زوم */
(function(){ const sc=$('#scroller'); let d0=0,p0=0;
  const dist=e=>Math.hypot(e.touches[0].clientX-e.touches[1].clientX,e.touches[0].clientY-e.touches[1].clientY);
  sc.addEventListener('touchstart',e=>{ if(e.touches.length===2){ d0=dist(e); p0=PX; } },{passive:true});
  sc.addEventListener('touchmove',e=>{ if(e.touches.length===2&&d0){ e.preventDefault(); setZoom(Math.round(p0*dist(e)/d0)); } },{passive:false});
  sc.addEventListener('touchend',()=>{ d0=0; },{passive:true});
  sc.addEventListener('wheel',e=>{ if(e.ctrlKey){ e.preventDefault(); setZoom(Math.round(PX*(e.deltaY<0?1.12:0.89))); } },{passive:false});
})();
/* ═══════════ 3.3: أمثلة المؤثرات + انتقال عند القص ═══════════ */
const TRANS=['curve','push','pull','rack','whip','spin','iris','flash','zoom','glitch'];
function thumbAt(x){ return '/hs/th/'+(Math.max(0,Math.floor(vm(x)))+1)+'.jpg'; }
function fxTile(f,attr,on,x){ return '<div class="tile fxt'+(on?' sel':'')+'" '+attr+' title="'+esc(t('fx_'+f))+'"><div class="pv"><i class="fxp fxp-'+f+'" style="background-image:url('+thumbAt(x==null?T:x)+')"></i></div><span>'+t('fx_'+f)+'</span></div>'; }
function seamFx(sm){ return hs().layers.find(l=>l.type==='fx'&&(l.auto==='transitions'||l.auto==='trans')&&(l.seam!=null?Math.abs(l.seam-sm)<0.02:Math.abs(l.s+0.02-sm)<0.12)); }
function seamPick(sm){ seek(Math.max(0,sm-0.4)); const cur=seamFx(sm);
  modal('<h3>'+t('cutTitle')+'</h3><p class="hint" style="margin-top:0">'+t('cutHint',fmt(sm))+'</p><div class="grid3 g6">'+'<div class="tile fxt'+(!cur?' sel':'')+'" data-tr=""><div class="pv"><i class="fxp" style="background-image:url('+thumbAt(sm)+')"></i></div><span>'+t('cutNone')+'</span></div>'+TRANS.map(f=>fxTile(f,'data-tr="'+f+'"',cur&&cur.fx===f,sm)).join('')+'</div><div class="row" style="margin:14px 0 0"><button id="trAll">'+t('cutAll')+'</button><button id="qNo">'+t('close')+'</button></div>',true);
  $('#qNo').onclick=closeModal; let pick=cur?cur.fx:'';
  $('#mbox').querySelectorAll('[data-tr]').forEach(el=>el.onclick=()=>{ pick=el.dataset.tr; seamSet(sm,pick); closeModal(); seek(Math.max(0,sm-0.5)); });
  $('#trAll').onclick=()=>{ const f=pick||'flash'; snap(); (INFO.seams||[]).forEach(q=>seamSet(q,f,true)); buildTL(); live(); closeModal(); toast(t('cutAllDone',(INFO.seams||[]).length)); }; }
function seamSet(sm,f,quiet){ if(!quiet) snap(); const h=hs(), old=seamFx(sm); if(old) h.layers=h.layers.filter(l=>l!==old);
  if(f&&sm>0.2&&sm<total()-0.2){ const id='L'+(Math.max(0,...h.layers.map(l=>parseInt(String(l.id).replace(/\D/g,''))||0))+1), long=f==='zoom'||f==='blur';
    if(TRS.includes(f)) h.layers.push({id,...trAdd(f,sm),s:r3(sm-0.3),e:r3(sm+0.35)}); else h.layers.push({id,type:'fx',fx:f,auto:'trans',seam:r3(sm),s:r3(sm-(long?0.12:0.02)),e:r3(sm+(long?0.38:0.3)),amount:f==='flash'?0.35:0.55,track:2}); }
  if(!quiet){ buildTL(); live(); } }
/* ═══════════ 3.1: المقاس ومناطق الأمان ═══════════ */
async function frameSync(){ const h=hs(), f=h.frame||{}; const r=await api('/hs/frame',{ar:f.ar||'9:16',cy:f.cy,platforms:h.platforms||[]}); if(r.ok) INFO.safe=r.safe; dirty(); drawSafe(); $('#safe').classList.add('on'); if(RTAB==='proj'||RTAB==='cap') renderRight(); }
function drawSafe(){ const el=$('#safe'), z=INFO&&INFO.safe; if(!el||!z) return; const c=z.crop||[0,100], hh=c[1]-c[0], Z=z.zone; let o='';
  if(z.crop) o+='<div class="mask" style="top:0;left:0;right:0;height:'+c[0]+'%"></div><div class="mask" style="bottom:0;left:0;right:0;height:'+(100-c[1])+'%"></div>';
  o+='<div style="top:'+c[0]+'%;left:0;right:0;height:'+(Z[0]*hh/100)+'%"></div><div style="top:'+(c[1]-Z[1]*hh/100)+'%;left:0;right:0;height:'+(Z[1]*hh/100)+'%"></div>';
  o+='<div style="left:0;top:'+(c[0]+Z[0]*hh/100)+'%;height:'+(hh*(100-Z[0]-Z[1])/100)+'%;width:'+Z[2]+'%"></div><div style="right:0;top:'+(c[0]+hh*0.45)+'%;height:'+(hh*(55-Z[1])/100)+'%;width:'+Z[3]+'%"></div>';
  if(z.ar==='16:9') o+='<span class="tag">'+t('fh_16x9')+'</span>'; el.innerHTML=o; }
let SFXLIB=[], _sfxNow=null, MYDIR='', SFXCAT='all', SFXQ='';
function sfxSet(items){ SFXLIB=items||[]; SFXLIB.forEach(x=>{ I18N['sfx_'+x.id]=[x.ar,x.en]; }); }
async function sfxLibLoad(){ try{ const r=await api('/hs/sfxlib'); MYDIR=r.myDir||''; sfxSet(r.items); }catch(e){} }
function sfxLibHtml(){ const mine=SFXLIB.filter(x=>x.mine), lib=SFXLIB.filter(x=>!x.mine), miss=lib.filter(x=>!x.have).length;
  let o='<h4 style="margin-top:14px">'+t('mySounds')+'<span><button class="sm" data-up="sound">'+t('upload')+'</button>'+(INFO&&INFO.local?' <button class="sm ghost" id="myOpen">'+t('myOpen')+'</button>':'')+'</span></h4>';
  o+=mine.length?'<div class="sfxlist">'+mine.map(x=>'<div class="sfxrow"><button class="sm ghost" data-sfxplay="'+x.id+'" title="'+esc(t('listen'))+'">'+(_sfxNow&&_sfxNow._id===x.id?IC_PAUSE:IC_PLAY)+'</button><span dir="auto" data-myedit="'+x.id+'" title="'+esc(x.note||t('myEdit'))+'" style="cursor:pointer">'+esc(x.ar)+(x.long?' <small>'+t('myLong')+'</small>':'')+'</span><small>'+esc(x.dur)+'</small><button class="sm" data-sfxlib="'+x.id+'">'+t('add')+'</button></div>').join('')+'</div>':'';
  o+='<p class="hint">'+t(mine.length?'myHint':'myEmpty')+'</p>';
  if(lib.length){ const cats=[...new Set(lib.map(x=>x.cat||'mixkit'))];
    o+='<h4 style="margin-top:14px">'+t('sfxLib')+'</h4><div class="chips sfxcats"><button data-sfxcat="all"'+(SFXCAT==='all'?' class="on"':'')+'>'+t('sfxCatAll')+'</button>'+cats.map(c=>'<button data-sfxcat="'+c+'"'+(SFXCAT===c?' class="on"':'')+'>'+t('sfxc_'+c)+'</button>').join('')+'</div>'
      +'<input type="search" id="sfxQ" dir="auto" value="'+esc(SFXQ)+'" placeholder="'+esc(t('sfxQPh'))+'" style="margin:6px 0"><div id="sfxBox">'+sfxBoxHtml()+'</div><p class="hint">'+t('sfxLibHint')+'</p>'; }
  return o; }
function sfxShown(){ const q=SFXQ.toLowerCase(); return SFXLIB.filter(x=>!x.mine&&(SFXCAT==='all'||(x.cat||'mixkit')===SFXCAT)&&(!q||(x.ar+' '+x.en+' '+(x.use||'')+' '+x.id).toLowerCase().includes(q))); }
function sfxBoxHtml(){ const L=sfxShown(), miss=L.filter(x=>!x.have).length;
  return (miss?'<div class="row" style="margin:0 0 6px"><button class="sm" id="sfxAll">'+t('sfxAll',miss)+'</button></div>':'')+(SFXCAT==='all'&&!SFXQ&&L.length?sfxGroups(L):'<div class="sfxlist">'+(L.length?L.map(x=>'<div class="sfxrow" title="'+esc(x.use||'')+'"><button class="sm ghost" data-sfxplay="'+x.id+'" title="'+esc(t('listen'))+'">'+(_sfxNow&&_sfxNow._id===x.id?IC_PAUSE:IC_PLAY)+'</button><span dir="auto">'+esc(LANG==='ar'?x.ar:x.en)+(x.long?' <small>'+t('myLong')+'</small>':'')+'</span><small>'+esc(x.dur)+'</small><button class="sm" data-sfxlib="'+x.id+'">'+t('add')+'</button></div>').join(''):'<p class="hint">'+t('sfxNone')+'</p>')+'</div>'); }
function sfxRow(x){ return '<div class="sfxrow" title="'+esc(x.use||'')+'"><button class="sm ghost" data-sfxplay="'+x.id+'" title="'+esc(t('listen'))+'">'+(_sfxNow&&_sfxNow._id===x.id?IC_PAUSE:IC_PLAY)+'</button><span dir="auto">'+esc(LANG==='ar'?x.ar:x.en)+(x.long?' <small>'+t('myLong')+'</small>':'')+'</span><small>'+esc(x.dur)+'</small><button class="sm" data-sfxlib="'+x.id+'">'+t('add')+'</button></div>'; }
function sfxGroups(L){ const cats=[...new Set(L.map(x=>x.cat||'mixkit'))]; return cats.map(c=>{ const g=L.filter(x=>(x.cat||'mixkit')===c); return '<div class="sfxgrp">'+esc(t('sfxc_'+c))+' <small>'+g.length+'</small></div><div class="sfxlist">'+g.map(sfxRow).join('')+'</div>'; }).join(''); }
function myEdit(id){ const it=SFXLIB.find(x=>x.id===id); if(!it) return; modal('<h3>'+t('myEdit')+'</h3><input type="text" id="myN" dir="auto" value="'+esc(it.ar)+'" placeholder="'+esc(t('myNamePh'))+'" style="margin-bottom:8px"><input type="text" id="myT" dir="auto" value="'+esc(it.note||'')+'" placeholder="'+esc(t('myNotePh'))+'"><p class="hint">'+t('myNoteHint')+'</p><div class="row" style="margin:12px 0 0"><button class="pri" id="myOk">'+t('save')+'</button><button class="ghost" id="myDel">'+t('delete')+'</button><button class="ghost" id="qNo">'+t('cancel')+'</button></div>');
  $('#qNo').onclick=closeModal; $('#myOk').onclick=async()=>{ const r=await api('/hs/mysfx_edit',{id,name:$('#myN').value,note:$('#myT').value}); sfxSet(r.items); closeModal(); renderLeft(); buildTL(); };
  $('#myDel').onclick=async()=>{ const r=await api('/hs/mysfx_edit',{id,delete:true}); sfxSet(r.items); if(ST.studio.sfx&&ST.studio.sfx[id]){ snap(); delete ST.studio.sfx[id]; dirty(); } closeModal(); renderLeft(); buildTL(); }; }
/* 4.21: زر السماع يصير خطين وهو شغّال، ويرجع مثلث لما يوقف */
const IC_PLAY='<svg class="pp-ic" viewBox="0 0 12 12"><path d="M3 1.5v9l7.5-4.5z" fill="currentColor"/></svg>', IC_PAUSE='<svg class="pp-ic" viewBox="0 0 12 12"><rect x="2.2" y="1.5" width="2.6" height="9" rx=".6" fill="currentColor"/><rect x="7.2" y="1.5" width="2.6" height="9" rx=".6" fill="currentColor"/></svg>';
function sfxBtns(){ $$('[data-sfxplay]').forEach(b=>{ const on=!!(_sfxNow&&_sfxNow._id===b.dataset.sfxplay); b.classList.toggle('playing',on); b.innerHTML=on?IC_PAUSE:IC_PLAY; }); }
function sfxPlay(id){ const it=SFXLIB.find(x=>x.id===id); if(!it) return; if(_sfxNow){ _sfxNow.pause(); const same=_sfxNow._id===id; _sfxNow=null; sfxBtns(); if(same) return; } const au=new Audio(it.have?'/sfx_prev/'+id+'.wav':it.prev); au._id=id; _sfxNow=au; sfxBtns(); au.play().catch(()=>{ toast(t('sfxNoNet')); if(_sfxNow===au){ _sfxNow=null; sfxBtns(); } }); au.onended=()=>{ if(_sfxNow===au){ _sfxNow=null; sfxBtns(); } }; }
function sfxAdd(k){ snap(); ST.studio.sfx=ST.studio.sfx||{}; const it=SFXLIB.find(x=>x.id===k), long=it&&it.long; (ST.studio.sfx[k]=ST.studio.sfx[k]||[]).push(long?[r3(T),0.6,r3(Math.min(parseFloat(it.dur)||10,total()-T))]:r3(T)); ST.studio.sfx[k].sort((a,b)=>(Array.isArray(a)?a[0]:a)-(Array.isArray(b)?b[0]:b)); buildTL(); dirty(); try{ new Audio('/sfx_prev/'+k+'.wav').play().catch(()=>{}); }catch(e){} }
async function autoFx(kind,on){ await save(); const r=await api('/hs/auto',{kind,on}); await load(true); toast(on?t('autoAdded',r.n):t('autoCleared')); }
function coverShot(){ try{ const w=F.contentWindow, a=document.createElement('a'); a.href=w.document.getElementById('cv').toDataURL('image/png'); a.download=(INFO.name||'cover')+'-'+T.toFixed(2)+'.png'; a.click(); }catch(e){ toast(t('failed')); } }
function phoneFile(f){ let svg=''; const u=INFO.lan.replace('/?k=','/'+f+'?k='); try{ const q=qrcode(0,'M'); q.addData(u); q.make(); svg=q.createSvgTag({cellSize:6,margin:3,scalable:true}); }catch(e){}
  modal('<h3>'+t('phoneFileTitle')+'</h3><div style="display:flex;gap:18px;flex-wrap:wrap;align-items:center"><div style="width:230px;background:#fff;border-radius:10px;padding:6px;line-height:0">'+svg+'</div><div style="flex:1;min-width:220px"><p style="line-height:1.9;margin-top:0">'+t('phoneFileHint')+'</p><div class="copy"><span style="direction:ltr;text-align:left">'+esc(u)+'</span></div></div></div><div class="row" style="margin:14px 0 0"><button id="qNo">'+t('close')+'</button></div>'); $('#qNo').onclick=closeModal; }

/* ───── النبض: بث حي + إعادة تحميل لما Claude يعدّل ───── */
async function pulse(){ let p; const pt0=Date.now(); try{ p=await api('/hs/pulse?since='+lastAct); }catch(e){ return; } if(!p||!p.sig) return; PULSE=p;
  if(TKAG&&!(p.agent&&p.agent.running)){ TKAG=false; loadTakes(); }
  if((RTAB==='notes'||RTAB==='claude')&&ST){ const was=!!(window._chatRun), now=!!(p.agent&&p.agent.running); window._chatRun=now; if(was&&!now){ api('/hs/notes').then(n=>{ NOTES=n; chatFeed(); agFeed(); buildTL(); }); } else if((p.act&&p.act.length)||was!==now){ chatFeed(); agFeed(); } }
  if(CAPRAG&&!(p.agent&&p.agent.running)){ CAPRAG=false; CAPRI=-1; CAPRDONE=true; caprFollow(); caprLoad(); } else if(CAPRAG) caprFollow();
  if(BUILDAG&&!(p.agent&&p.agent.running)){ BUILDAG=false; loadSteps(); setTimeout(async()=>{ if(BV){ BVDONE=Math.max(0,(hs().layers||[]).length-BV0); try{ PLAN=await api('/hs/plan'); }catch(e){} bvDraw(); } },1500); } else if(BV) bvDraw();
  if(PVAG){ if(!(p.agent&&p.agent.running)){ PVAG=''; PLAN=await api('/hs/plan'); if(PV2&&PV2.sub===1&&PLAN&&PLAN.ok&&(PLAN.items||[]).length) PV2.sub=2; loadSteps(); } pvDraw(); }
  if(BRW&&((p.act||[]).some(e=>e.kind&&e.kind!=='ask'&&e.kind!=='done'&&e.id>BRLAST)||(p.agent&&p.agent.running)||Date.now()-BRW>600000)){ BRW=0; stLoaderHide(); RTAB='claude'; markTabs(); renderRight(); toast(t('brStarted')); }
  if((p.act||[]).some(e=>e.id>lastAct)){ ACT.push(...p.act.filter(e=>e.id>lastAct)); if(ACT.length>300) ACT=ACT.slice(-300); lastAct=ACT[ACT.length-1].id; if(RTAB==='claude'&&ST) renderFeed(); }   // 4.50: نبضتين مع بعض بأول التحميل كانت تكرر السجل
  else if(RTAB==='claude'&&ST){ const st=$('#pStages'); if(st) st.innerHTML=stagesHtml(); }
  const busy=p.agent.running?t('claudeWorking',p.agent.elapsed):p.job.running?t('jobWorking'):(p.vis&&p.vis.busy)?t(p.vis.what==='face'?'visFace':'visMask'):''; $('#busy').classList.toggle('on',!!busy); $('#busyTx').textContent=busy;
  if(RTAB==='claude'&&ST){ const g=$('#agGo'); if(g) g.disabled=p.agent.running; agFeed(); if(!!$('#agStop')!==p.agent.running&&document.activeElement!==$('#agTx')) renderRight(); }
  if(p.brief==='pending'){ if(!$('#brief').classList.contains('on')&&!BR_OPENING){ BR_OPENING=true; openBrief().finally(()=>BR_OPENING=false); } } else $('#brief').classList.remove('on');
  if(p.vis&&p.vis.busy&&!VISB) toast(t(p.vis.what==='face'?'visFace':'visMask')); VISB=!!(p.vis&&p.vis.busy);
  if(p.aux!==undefined&&p.aux!==AUXS){ const first=AUXS===null; AUXS=p.aux; const w=F.contentWindow; if(!first&&READY&&w&&w.hsAux){ w.hsAux().then(()=>{ lastFrame=-1; drawT(T); if(RTAB==='sel') renderRight(); }).catch(()=>{}); } }
  pillSync(); tickerSync(p);
  document.body.classList.toggle('nr',!p.ready); if(!READY||!ST) applyMode();
  workBadge(p);
  if(!p.ready&&READY&&ST){ return; }   // 4.46: Claude يعيد بناء شي وسط الشغل: الاستوديو يبقى، وفوق المعاينة شارة صغيرة لين يخلص
  if(!p.ready){ READY=false; $('#live').classList.add('on'); renderLive(); SIG=p.sig; if(_ldK==='boot') stLoaderHide(); return; }
  if(!READY){ READY=true; $('#live').classList.remove('on'); SIG=p.sig; try{ await load(false); } finally{ if(_ldK==='boot') stLoaderHide(); } return; }
  if(pt0<=LOCALW) return;   // النبضة بدت قبل ما يخلص حفظك: لا تحسبه تعديل من برّا
  if(SIG===null||adoptSig){ SIG=p.sig; adoptSig=false; return; }
  if(p.sig!==SIG&&!dragging&&!p.job.running&&!$('#modal').classList.contains('on')&&!_saveT_pending()){ SIG=p.sig; await load(true); toast(t('externalChange')); } }
let BR_OPENING=false, VISB=false, AUXS=null;
function _saveT_pending(){ return $('#saved').textContent===t('saving'); }
applyLang(); let _pAct=Date.now(); ['pointerdown','keydown','wheel'].forEach(k=>addEventListener(k,()=>{ _pAct=Date.now(); },{passive:true,capture:true}));
// 4.4.1: النبضة تهدى لما ما فيه شغل: كل ثانية ونص وقت Claude أو التصدير، 4 ثواني عادي، و15 لما الصفحة مخفية
(async function pLoop(){ try{ await pulse(); }catch(e){} const p=PULSE||{}, busy=(p.agent&&p.agent.running)||(p.job&&p.job.running)||(p.vis&&p.vis.busy)||p.brief==='pending';
  setTimeout(pLoop, document.hidden?15000:(busy||Date.now()-_pAct<8000)?1500:4000); })();
document.addEventListener('visibilitychange',()=>{ if(!document.hidden) pulse(); });
(function(){ const d=document.createElement('datalist'); d.id='hsCities'; d.innerHTML=Object.keys(CITIES).map(c=>'<option value="'+c+'">').join(''); document.body.appendChild(d); })();

/* ───── 4.4: رسم حر على الفيديو (بيدك، بالماوس أو بإصبعك) ───── */
let DRW=null; const DRC=['#FFFFFF','#FFD21F','#FF4D6D','#4C8DFF','#2FBF9B','#15151C'], DRW_W=[6,12,22];
function drawStart(edit){ if(!ST||DRW) return; if(playing) stop(); const w=$('#wrap'); let c0='#FFD21F', w0=12; try{ c0=localStorage.getItem('hsDrawC')||c0; w0=+localStorage.getItem('hsDrawW')||w0; }catch(e){}
  DRW={pts:edit?(edit.pts||[]).slice():[],color:edit?(edit.color||c0):c0,lw:edit?(edit.lw||w0):w0,edit:edit?edit.id:null,hist:[],down:false};
  const cv=document.createElement('canvas'); cv.id='drawCv'; w.appendChild(cv); const bar=document.createElement('div'); bar.id='drawBar'; $('#stage').appendChild(bar); document.body.classList.add('drawing');
  const fit=()=>{ const R=w.getBoundingClientRect(), d=devicePixelRatio||1; cv.width=Math.round(R.width*d); cv.height=Math.round(R.height*d); drawPaint(); }; fit(); DRW.fit=fit; addEventListener('resize',fit);
  const at=e=>{ const R=cv.getBoundingClientRect(); return [+clamp((e.clientX-R.left)/R.width,0,1).toFixed(4),+clamp((e.clientY-R.top)/R.height,0,1).toFixed(4)]; };
  cv.addEventListener('pointerdown',e=>{ e.preventDefault(); e.stopPropagation(); cv.setPointerCapture(e.pointerId); DRW.hist.push(DRW.pts.length); if(DRW.pts.length) DRW.pts.push(null); DRW.pts.push(at(e)); DRW.down=true; drawPaint(); });
  cv.addEventListener('pointermove',e=>{ if(!DRW||!DRW.down) return; e.preventDefault(); const p=at(e), q=DRW.pts[DRW.pts.length-1]; if(q&&Math.hypot((p[0]-q[0])*1080,(p[1]-q[1])*1920)<4) return; DRW.pts.push(p); drawPaint(); });
  const up=e=>{ if(DRW) DRW.down=false; }; cv.addEventListener('pointerup',up); cv.addEventListener('pointercancel',up);
  ['touchstart','touchmove','touchend','click','dblclick'].forEach(k=>cv.addEventListener(k,e=>e.stopPropagation()));
  drawBar(); }
function drawBar(){ const b=$('#drawBar'); if(!b||!DRW) return;
  b.innerHTML='<div class="dsw">'+DRC.map(c=>'<i data-dc="'+c+'" class="'+(DRW.color===c?'on':'')+'" style="background:'+c+'"></i>').join('')+'<input type="color" id="dcI" value="'+esc(DRW.color)+'"></div>'
   +'<div class="dw">'+DRW_W.map(v=>'<button data-dw="'+v+'" class="'+(DRW.lw===v?'on':'')+'"><i style="width:'+(v/2+3)+'px;height:'+(v/2+3)+'px"></i></button>').join('')+'</div>'
   +'<span class="sp"></span><button class="ic" id="dUndo" title="'+esc(t('undo'))+'"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 14L4 9l5-5"/><path d="M4 9h10a6 6 0 0 1 0 12h-3"/></svg></button><button class="sm ghost" id="dClear">'+t('drawClear')+'</button><button class="sm" id="dNo">'+t('cancel')+'</button><button class="sm pri" id="dOk">'+t('done')+'</button>';
  b.querySelectorAll('[data-dc]').forEach(x=>x.onclick=()=>{ DRW.color=x.dataset.dc; try{ localStorage.setItem('hsDrawC',DRW.color); }catch(e){} drawBar(); drawPaint(); });
  $('#dcI').oninput=e=>{ DRW.color=e.target.value; drawPaint(); }; $('#dcI').onchange=()=>drawBar();
  b.querySelectorAll('[data-dw]').forEach(x=>x.onclick=()=>{ DRW.lw=+x.dataset.dw; try{ localStorage.setItem('hsDrawW',DRW.lw); }catch(e){} drawBar(); drawPaint(); });
  $('#dUndo').onclick=()=>{ if(!DRW.hist.length) return; DRW.pts.length=DRW.hist.pop(); while(DRW.pts.length&&DRW.pts[DRW.pts.length-1]===null) DRW.pts.pop(); drawPaint(); };
  $('#dClear').onclick=()=>{ DRW.hist.push(DRW.pts.length); DRW.pts=[]; DRW.hist=[]; drawPaint(); };
  $('#dNo').onclick=()=>drawEnd(false); $('#dOk').onclick=()=>drawEnd(true); }
function drawPaint(){ const cv=$('#drawCv'); if(!cv||!DRW) return; const x=cv.getContext('2d'), W=cv.width, H=cv.height; x.clearRect(0,0,W,H); x.lineCap='round'; x.lineJoin='round'; x.strokeStyle=DRW.color; x.lineWidth=DRW.lw*W/1080; x.shadowColor='rgba(0,0,0,.35)'; x.shadowBlur=8*W/1080;
  x.beginPath(); let pen=false; for(const p of DRW.pts){ if(!p){ pen=false; continue; } if(!pen){ x.moveTo(p[0]*W,p[1]*H); x.lineTo(p[0]*W+0.01,p[1]*H); pen=true; } else x.lineTo(p[0]*W,p[1]*H); } x.stroke(); }
function drawEnd(ok){ const d=DRW; if(!d) return; DRW=null; removeEventListener('resize',d.fit); ['#drawCv','#drawBar'].forEach(s=>{ const e=$(s); if(e) e.remove(); }); document.body.classList.remove('drawing');
  while(d.pts.length&&d.pts[d.pts.length-1]===null) d.pts.pop(); if(!ok) return; if(d.pts.filter(Boolean).length<2){ toast(t('drawEmpty')); return; }
  if(d.edit){ const L=hs().layers.find(l=>l.id===d.edit); if(L){ snap(); L.pts=d.pts; L.color=d.color; L.lw=d.lw; live(); renderAll(); return; } }
  addLayer({type:'draw',pts:d.pts,color:d.color,lw:d.lw,reveal:0.9,glow:'shadow',anim:'fade',x:0.5,y:0.5,track:1}); renderAll(); toast(t('drawAdded')); }
document.addEventListener('keydown',e=>{ if(!DRW) return; e.stopImmediatePropagation(); if(e.key==='Escape') drawEnd(false); else if(e.key==='Enter') drawEnd(true); else if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='z'){ e.preventDefault(); $('#dUndo')&&$('#dUndo').click(); } },true);
(function(){ const b=$('#bDraw'); if(b){ b.title=t('drawTool'); b.onclick=()=>DRW?drawEnd(true):drawStart(); } })();

/* ───── 4.4: احفظ قبل ما تطلع (زر المكتبة، إغلاق الصفحة) ───── */
async function saveNow(){ if(!ST) return; if(_saveT||_saveT_pending()){ clearTimeout(_saveT); _saveT=null; try{ await save(); }catch(e){} } }
/* 4.46: زر الرجوع بالمتصفح ما يخرّب المقطع: أول ضغطة تقفل اللي فاتح (نافذة، الخطة، قائمة)، وبعدها يحفظ ويرجع للمكتبة.
   ولو رجعت للاستوديو من ذاكرة المتصفح (نسخة قديمة) يتحمّل من جديد عشان ما يحفظ القديم فوق شغلك */
addEventListener('pageshow',e=>{ if(e.persisted) location.reload(); });
try{ if(!history.state||history.state.hs!=='top'){ history.replaceState({hs:'base'},''); history.pushState({hs:'top'},''); } }catch(e){}
addEventListener('popstate',async ()=>{ const keep=()=>{ try{ history.pushState({hs:'top'},''); }catch(e){} };
  if($('#modal').classList.contains('on')){ closeModal(); keep(); return; }
  if($('#planv')){ pvClose(); keep(); return; }
  if($('#ctx').classList.contains('on')){ ctxClose(); keep(); return; }
  if($('#brief')&&$('#brief').classList.contains('on')){ keep(); return; }
  if(HUBU){ try{ await saveNow(); }catch(e){} location.replace(HUBU); return; }
  keep(); });
addEventListener('pagehide',()=>{ if(!ST||!_saveT_pending()) return; try{ navigator.sendBeacon('/api/save',new Blob([JSON.stringify({caps:ST.caps,theme:ST.theme,studio:ST.studio,outro:ST.outro||0})],{type:'application/json'})); }catch(e){} });
document.addEventListener('visibilitychange',()=>{ if(document.hidden) saveNow(); });
document.addEventListener('click',e=>{ const b=e.target.closest('#drawAgain,[data-drawbin]'); if(!b) return; if(b.id==='drawAgain'){ const L=selLayer(); if(L&&L.type==='draw') drawStart(L); } else { if(document.body.classList.contains('m')) document.body.dataset.mv=''; drawStart(); } });
/* ───── 4.4: اسم المشروع ينعدّل من فوق ───── */
$('#proj').addEventListener('click',()=>{ if(!ST||document.body.classList.contains('m')) return; const el=$('#proj'); if(el.isContentEditable) return; el.contentEditable='true'; el.focus(); try{ const r=document.createRange(); r.selectNodeContents(el); const s=getSelection(); s.removeAllRanges(); s.addRange(r); }catch(e){}
  const fin=ok=>{ el.contentEditable='false'; const v=el.textContent.trim().slice(0,80); if(ok&&v&&v!==(INFO.title||INFO.name)){ hs().title=v; INFO.title=v; dirty(); } el.textContent=INFO.title||INFO.name; };
  el.onkeydown=e=>{ if(e.key==='Enter'){ e.preventDefault(); el.blur(); } else if(e.key==='Escape'){ el.onblur=null; fin(false); } e.stopPropagation(); }; el.onblur=()=>fin(true); });
$('#proj').title=t('renameP');

/* ───── 4.4: شاشة التحميل بعبارات تتبدّل ───── */
const LDS={ boot:[['أفتح الاستوديو','Opening the studio'],['أجيب الفيديو','Loading the video'],['أرسم أول فريم','Drawing the first frame'],['أرتّب الكابشن والطبقات','Placing captions and layers'],['أضبط الأصوات','Tuning the sound'],['أجهّز التايم لاين','Building the timeline'],['تقريباً جاهز','Almost there']],
  brief:[['وصلت إجاباتك','Got your answers'],['Claude يقرأها','Claude is reading them'],['يختار الكابشن والألوان','Picking captions and colors'],['يرسم خطة المونتاج','Planning the edit'],['يجهّز أول مشهد','Preparing the first scene'],['ثواني ويبدأ','Starting in a moment']],
  rebuild:[['أقص الفيديو','Cutting the video'],['أعيد ترتيب اللقطات','Re-stitching the shots'],['أزحّف الكابشن مع الصوت','Shifting captions with the audio'],['أضبط الطبقات على الوقت الجديد','Re-timing the layers'],['أرسم الفريمات من جديد','Redrawing frames'],['قربنا','Nearly done']] };
const HJS_WM='<svg viewBox="0 0 307.2 264.75" fill="currentColor" aria-hidden="true"><rect width="33.5" height="185.1"/><rect x="33.5" y="75.8" width="81.25" height="33.5"/><path d="M114.75 0H148.25V211A53.75 53.75 0 0 1 40.75 211H74.25A20.25 20.25 0 0 0 114.75 211Z"/><path d="M285.14 34.87A49.04 37.75 0 1 0 243.49 92.55L241.51 92.55A49.04 37.75 0 1 1 199.86 150.23" fill="none" stroke="currentColor" stroke-width="33.2"/></svg>';
function hjsMark(lock){ const s='<div class="hjs" aria-hidden="true"><i></i><i></i><i></i></div>'; return lock?'<div class="hjs-lk">'+s+'<span class="hjs-wm">'+HJS_WM+'</span></div>':s; }
let _ldK=null, _ldI=0, _ldT0=0, BRW=0, BRLAST=0;
function stLoader(k,sub){ const b=$('#boot'); if(!b) return; _ldK=k; _ldI=0; _ldT0=Date.now(); const x=LDS[k][0]; bootScope(k!=='boot'&&!MOBILE&&!!ST);
  b.innerHTML='<div>'+hjsMark(k==='boot')+'<div class="tx">'+esc(LANG==='en'?x[1]:x[0])+'</div>'+(sub?'<div class="sub" dir="auto">'+esc(sub)+'</div>':'')+'<div class="line"><i></i></div><div class="slow"></div></div>'; b.classList.add('on'); }
function stLoaderHide(){ const b=$('#boot'); if(b) b.classList.remove('on'); _ldK=null; bootScope(false); }
/* 4.46: التحميل وقت العمليات (القص، الحركة البطيئة، الألوان…) فوق المعاينة بس، مو الشاشة كلها: الأقسام اللي جنب تبقى تشتغل */
function bootScope(on){ const b=$('#boot'); if(!b) return; document.body.classList.toggle('jobbusy',!!on); b.classList.toggle('scoped',!!on); if(!on){ b.style.cssText=''; return; } const r=$('#stage').getBoundingClientRect(); Object.assign(b.style,{top:r.top+'px',left:r.left+'px',width:r.width+'px',height:r.height+'px',right:'auto',bottom:'auto'}); }
addEventListener('resize',()=>{ if(document.body.classList.contains('jobbusy')) bootScope(true); });
setInterval(()=>{ if(!_ldK) return; const b=$('#boot'), tx=b&&b.querySelector('.tx'); if(!tx) return; _ldI++; const L=LDS[_ldK], x=L[_ldI%L.length]; tx.classList.add('out'); setTimeout(()=>{ tx.textContent=LANG==='en'?x[1]:x[0]; tx.classList.remove('out'); },320);
  const sl=b.querySelector('.slow'); if(sl&&!sl.textContent&&Date.now()-_ldT0>(_ldK==='boot'?15000:_ldK==='brief'?75000:90000)){ sl.innerHTML=esc(t(_ldK==='boot'?'ldSlowSt':_ldK==='brief'?'brSlow':'ldSlowRb'))+(_ldK==='brief'?' <button class="sm" id="brHide">'+t('brHide')+'</button>':''); } },2400);
document.addEventListener('click',e=>{ if(e.target.id==='brHide'){ BRW=0; stLoaderHide(); RTAB='claude'; markTabs(); renderRight(); } });
stLoader('boot');

/* ═══ 4.5: فحص الاحتفاظ · الإعادات · انشر (أغلفة، كاروسيل، ثريد، يوتيوب، أرقامك) · حارس الاستهلاك ═══ */
let RET=null, PUB={cov:null,rp:null,perf:null,ci:0,lay:'top',ctitle:null};
function tokenGo(kind,size){ return new Promise(res=>{ if(INFO&&INFO.tokenAsk===false) return res(true); try{ if(localStorage.getItem('hsTok_'+kind)==='1') return res(true); }catch(e){}
  modal('<h3>'+t('tokT')+'</h3><p style="line-height:1.9">'+t('tok_'+kind)+'</p><div class="warnbox">'+t('tokSize_'+(size||'mid'))+'</div><label class="item" style="margin-top:8px"><input type="checkbox" id="tkS"><span>'+t('tokSkip')+'</span></label><div class="row" style="margin:12px 0 0"><button class="pri" id="tkY">'+t('tokYes')+'</button><button class="ghost" id="tkN">'+t('cancel')+'</button></div>');
  $('#tkY').onclick=()=>{ try{ if($('#tkS').checked) localStorage.setItem('hsTok_'+kind,'1'); }catch(e){} closeModal(); res(true); }; $('#tkN').onclick=()=>{ closeModal(); res(false); }; }); }
const TKB=()=>' <span class="tkb">'+t('tokBadge')+'</span>';
async function refreshRet(){ if(!READY) return; try{ RET=await api('/hs/retention'); }catch(e){ RET=null; } drawCheck(); if(RTAB==='check') renderRight(); }
function retHtml(){ const R=RET; if(!R||!R.ok) return '';
  const col=v=>v>=80?'var(--au)':v>=55?'var(--warn)':'var(--bad)', W=300, H=64, n=R.curve.length;
  const pts=R.curve.map((v,i)=>(i/(Math.max(1,n-1))*W).toFixed(1)+','+(H-v/100*H).toFixed(1)).join(' ');
  const zones=(R.zones||[]).map(z=>'<rect x="'+(z.s/R.total*W).toFixed(1)+'" y="0" width="'+Math.max(2,(z.e-z.s)/R.total*W).toFixed(1)+'" height="'+H+'" fill="'+(z.lvl==='red'?'rgba(239,106,90,.22)':'rgba(242,179,61,.16)')+'"/>').join('');
  let o='<div class="sec ret"><h4>'+t('retT')+'</h4><div style="display:flex;align-items:flex-end;gap:12px"><div class="score" style="color:'+col(R.score)+'">'+R.score+'</div><div class="hint" style="margin:0">'+t('retEnd',Math.round(R.end))+'</div></div>'
    +'<svg class="rcv" viewBox="0 0 '+W+' '+H+'" preserveAspectRatio="none">'+zones+'<polyline points="'+pts+'" fill="none" stroke="#6aa2ff" stroke-width="2" vector-effect="non-scaling-stroke"/></svg>'
    +'<div class="dims">'+['hook','pace','visual','clarity','payoff','length'].map(k=>'<div class="dm"><span>'+t('rd_'+k)+'</span><i><b style="width:'+R.dims[k]+'%;background:'+col(R.dims[k])+'"></b></i><em>'+R.dims[k]+'</em></div>').join('')+'</div>';
  if(R.fixes.length){ o+='<h4 style="margin-top:14px">'+t('retFix')+'</h4>'+R.fixes.map((f,i)=>'<div class="item rfx" style="align-items:flex-start;cursor:default"><span style="flex:1;min-width:0;line-height:1.75" dir="auto">'+esc(srvEn(f.msg))+'</span><span class="row" style="flex:none;gap:6px;margin:0"><button class="sm ghost" data-seek="'+f.t+'" style="direction:ltr">'+fmt(f.t).slice(0,5)+'</button>'+(f.fix?'<button class="sm'+(f.fix==='claude'?' ghost':'')+'" data-rfx="'+i+'">'+t('rfx_'+f.fix)+(f.fix==='claude'?TKB():'')+'</button>':'')+'</span></div>').join('');
    const cl=R.fixes.filter(f=>f.fix!==null); if(INFO.claude&&cl.length) o+='<button class="ghost" id="retClaude" style="width:100%;margin-top:8px">'+t('retAllClaude')+TKB()+'</button>'; }
  else o+='<p class="hint">'+t('retClean')+'</p>';
  return o+'<p class="hint" style="margin-top:8px">'+t('retNote')+'</p></div>'; }
async function retFix(i){ const f=RET&&RET.fixes[i]; if(!f) return; const h=hs();
  if(f.fix==='hook'){ snap(); h.hooks={...h.hooks,on:true,active:0,items:[{text:f.arg}]}; live(); renderRight(); toast(t('retHookDone')); setTimeout(refreshRet,900); return; }
  if(f.fix==='zoom'){ addLayer({type:'fx',fx:'zoom',s:r3(f.arg[0]),e:r3(f.arg[1]),amount:0.5,auto:'retention'}); toast(t('retZoomDone')); setTimeout(refreshRet,900); return; }
  if(f.fix==='cut'){ const sec=f.arg.reduce((a,r)=>a+(r[1]-r[0]),0); askRemove({ranges:f.arg},t('retCutWhat',f.arg.length,sec.toFixed(1))); return; }
  if(f.fix==='takes'||f.fix==='fillers'){ const el=$(f.fix==='takes'?'#chkTakes':'#chkFil'); if(el) el.scrollIntoView({behavior:'smooth',block:'start'}); return; }
  if(f.fix==='claude') return retClaude([f.msg]); }
async function retClaude(items){ if(!INFO.claude){ toast(t('askNoCli')); return; } if(!(await tokenGo('fix','mid'))) return; await save(); const r=await api('/hs/claude_fix',{what:'retention',items}); if(r.ok){ RTAB='claude'; markTabs(); renderRight(); toast(t('claudeStarted')); } else toast(srvEn(r.msg)||t('failed')); }
/* الإعادات: كل مجموعة تختار أي محاولة تبقى */
function takesHtml(c){ const G={}; (c.dupes||[]).forEach(d=>{ const k=(d.group||[d.a,d.b]).join(','); if(!G[k]) G[k]={cards:d.group||[d.a,d.b],keep:d.b,why:d.why||[]}; });
  const gs=Object.values(G); let o='<div class="sec" id="chkTakes"><h4>'+t('takesT')+'</h4>';
  if(!gs.length) return o+'<p class="hint">'+t('chkNoDupes')+'</p></div>';
  o+='<p class="hint">'+t('takesHint')+'</p>'+gs.map((g,gi)=>'<div class="tkg"><label class="item" style="cursor:default"><input type="checkbox" data-tkon="'+gi+'" checked><b style="flex:1">'+t('takesN',g.cards.length)+'</b>'+(g.why.length?'<small style="color:var(--mut)">'+esc(g.why.map(srvEn).join(' · '))+'</small>':'')+'</label>'
    +g.cards.map((ci,j)=>{ const cd=ST.caps.cards[ci]; return '<label class="item tk'+(ci===g.keep?' keep':'')+'"><input type="radio" name="tk'+gi+'" data-tkg="'+gi+'" data-tkc="'+ci+'"'+(ci===g.keep?' checked':'')+'><span dir="auto" style="flex:1;min-width:0">'+t('takeN',j+1)+' · '+esc(key(cd))+'</span><button class="sm ghost" data-tkp="'+ci+'">'+t('play')+'</button></label>'; }).join('')+'</div>').join('');
  TAKES=gs; return o+'</div>'; }
let TAKES=[];
function takesDrop(){ const drop=[]; TAKES.forEach((g,gi)=>{ const on=$('[data-tkon="'+gi+'"]'); if(on&&!on.checked) return; const k=$('[data-tkg="'+gi+'"]:checked'); const keep=k?+k.dataset.tkc:g.keep; g.cards.forEach(ci=>{ if(ci!==keep) drop.push(ci); }); }); return drop; }
function playRange(s,e){ stop(); seek(Math.max(0,s-0.05)); play(); clearTimeout(playRange._t); playRange._t=setTimeout(()=>{ if(playing) stop(); },(e-s)*1000+250); }
/* انشر */
function pubHtml(){ let o='';
  const C=PUB.cov; o+='<div class="sec"><h4>'+t('covT')+'</h4>';
  if(!C) o+='<p class="hint">…</p>'; else if(!C.ok) o+='<p class="hint">'+esc(srvEn(C.msg)||'')+'</p>'; else {
    o+='<div class="covs">'+C.frames.map((f,i)=>'<canvas class="cov'+(PUB.ci===i?' on':'')+'" data-cov="'+i+'" width="270" height="480"></canvas>').join('')+'</div>'
      +'<input type="text" id="covTx" dir="auto" value="'+esc(PUB.ctitle!=null?PUB.ctitle:C.title)+'" placeholder="'+t('covPh')+'" style="margin-top:8px">'
      +'<div class="seg" style="margin-top:8px">'+['top','center','bottom','big'].map(k=>'<button data-clay="'+k+'" class="'+(PUB.lay===k?'on':'')+'">'+t('cl_'+k)+'</button>').join('')+'</div>'+covCtl()
      +'<div class="row" style="margin-top:8px"><button class="pri" id="covSave" style="flex:1">'+t('covSave')+'</button></div>'
      +((C.have||[]).length?'<div class="hint" style="margin-top:6px">'+C.have.map(f=>'<a href="/'+f+'?v='+Date.now()+'" download>'+esc(f)+'</a>').join(' · ')+'</div>':''); }
  o+='</div>';
  const R=PUB.rp; o+='<div class="sec"><h4>'+t('rpT')+'</h4>';
  if(!R) o+='<p class="hint">…</p>'; else if(!R.ok&&R.msg) o+='<p class="hint">'+esc(srvEn(R.msg))+'</p>'; else {
    o+='<p class="hint">'+t(R.by==='claude'?'rpByC':'rpByL')+'</p><label class="lbl2">'+t('rpTitle')+'</label><input type="text" id="rpTitle" dir="auto" value="'+esc(R.title)+'">'
      +'<label class="lbl2">'+t('rpPts')+'</label><textarea id="rpPts" rows="5" dir="auto">'+esc((R.points||[]).join('\n'))+'</textarea>'
      +'<label class="item"><input type="checkbox" id="rpCtaOn"'+(R.ctaOn?' checked':'')+'><span>'+t('rpCtaOn')+'</span></label>'+(R.ctaOn?'<input type="text" id="rpCta" dir="auto" value="'+esc(R.cta||'')+'" placeholder="'+esc(t('rpCta'))+'">':'')
      +'<div class="covs car">'+[0,...(R.points||[]).map((_,i)=>i+1),...(R.ctaOn?[(R.points||[]).length+1]:[])].map(i=>'<canvas class="cs" data-cs="'+i+'" width="216" height="270"></canvas>').join('')+'</div>'
      +'<div class="row" style="margin-top:8px"><button class="pri" id="carSave" style="flex:1">'+t('carSave')+'</button><button id="rpRe">'+t('rpRe')+'</button></div><div id="carOut"></div>'
      +(INFO.claude?'<button class="ghost" id="rpClaude" style="width:100%;margin-top:10px">'+t('rpClaude')+TKB()+'</button>':''); }
  o+='</div>';
  return o; }
async function loadPub(){ const [c,r]=await Promise.all([api('/hs/covers'),api('/hs/repurpose')]); PUB.cov=c; PUB.rp=r; if(RTAB==='pub'){ renderRight(); drawPub(); } }
function fw(){ return F&&F.contentWindow; }
function fval(n,d){ try{ return fw().eval('typeof '+n+'!=="undefined"?'+n+':null')||d; }catch(e){ return d; } }
async function fontReady(fam){ try{ await fw().document.fonts.load('900 80px "'+fam+'"'); }catch(e){} }
function loadImg(src){ return new Promise(r=>{ const im=new (fw().Image)(); im.onload=()=>r(im); im.onerror=()=>r(null); im.src=src; }); }
function wrapLines(X,txt,maxW){ const out=[]; for(const para of String(txt||'').split('\n')){ let line=''; for(const w of para.split(/\s+/).filter(Boolean)){ const tt=line?line+' '+w:w; if(X.measureText(tt).width>maxW&&line){ out.push(line); line=w; } else line=tt; } if(line) out.push(line); } return out; }
/* 4.44: الغلاف تتحكم فيه كامل: الخط، الحجم، لون النص، الصندوق ولونه، الظل، والتعتيم */
function covS(){ const h=hs(); h.coverStyle=h.coverStyle||{}; return Object.assign({font:h.cap.font||'',size:0,color:'#FFFFFF',box:true,boxColor:'',shadow:true,dim:0.35,weight:900},h.coverStyle); }
function covCtl(){ const c=covS(), fonts=allFonts();
  return '<div class="covctl"><div class="row"><label>'+t('covFont')+'</label><select id="cvFont">'+fonts.map(f=>'<option'+(f===(c.font||fonts[0])?' selected':'')+'>'+esc(f)+'</option>').join('')+'</select></div>'
    +'<div class="row"><label>'+t('covSize')+'</label><input type="range" id="cvSize" min="70" max="210" step="2" value="'+(c.size||(PUB.lay==='big'?150:112))+'"><span class="val">'+(c.size||t('auto'))+'</span></div>'
    +'<div class="row"><label>'+t('covWeight')+'</label><div class="seg">'+[[600,'covW6'],[800,'covW8'],[900,'covW9']].map(([w,l])=>'<button data-cvw="'+w+'" class="'+(c.weight===w?'on':'')+'">'+t(l)+'</button>').join('')+'</div></div>'
    +'<div class="row"><label>'+t('covColor')+'</label><input type="color" id="cvColor" value="'+esc(c.color)+'"><label class="item" style="margin:0"><input type="checkbox" id="cvBox"'+(c.box?' checked':'')+'><span>'+t('covBox')+'</span></label><input type="color" id="cvBoxC" value="'+esc(c.boxColor||fval('ACC','#4C8DFF'))+'"></div>'
    +'<div class="row"><label class="item" style="margin:0"><input type="checkbox" id="cvShadow"'+(c.shadow?' checked':'')+'><span>'+t('covShadow')+'</span></label></div>'
    +'<div class="row"><label>'+t('covDim')+'</label><input type="range" id="cvDim" min="0" max="0.8" step="0.05" value="'+c.dim+'"></div></div>'; }
document.addEventListener('input',e=>{ const id=e.target.id; if(!['cvFont','cvSize','cvColor','cvBox','cvBoxC','cvShadow','cvDim'].includes(id)) return; const h=hs(); h.coverStyle=covS();
  const C=h.coverStyle; if(id==='cvFont') C.font=e.target.value; if(id==='cvSize'){ C.size=+e.target.value; const v=e.target.parentNode.querySelector('.val'); if(v) v.textContent=C.size; } if(id==='cvColor') C.color=e.target.value; if(id==='cvBox') C.box=e.target.checked; if(id==='cvBoxC') C.boxColor=e.target.value; if(id==='cvShadow') C.shadow=e.target.checked; if(id==='cvDim') C.dim=+e.target.value;
  dirty(); clearTimeout(PUB._t); PUB._t=setTimeout(drawPub,120); });
document.addEventListener('change',e=>{ if(['cvFont','cvBox','cvShadow'].includes(e.target.id)) e.target.dispatchEvent(new Event('input',{bubbles:true})); if(e.target.id==='rpCtaOn'&&PUB.rp){ pubSync(); PUB.rp.ctaOn=e.target.checked; api('/hs/repurpose',{save:PUB.rp}); renderRight(); drawPub(); } });
document.addEventListener('click',e=>{ const b=e.target.closest('[data-cvw]'); if(!b) return; const h=hs(); h.coverStyle=covS(); h.coverStyle.weight=+b.dataset.cvw; $$('[data-cvw]').forEach(x=>x.classList.toggle('on',x===b)); dirty(); drawPub(); });
async function drawCover(cv,frame,title,lay,full){ const w=fw(); if(!w) return null; const S=full?1:cv.width/1080, c=w.document.createElement('canvas'); c.width=Math.round(1080*S); c.height=Math.round(1920*S);
  const CS=covS(), X=c.getContext('2d'), fam=CS.font||hs().cap.font||fval('FONT','Cairo'), acc=CS.boxColor||fval('ACC','#4C8DFF'); await fontReady(fam); const im=await loadImg('/vfr/'+String(frame).padStart(5,'0')+'.jpg');
  X.setTransform(S,0,0,S,0,0); X.fillStyle='#000'; X.fillRect(0,0,1080,1920); if(im) X.drawImage(im,0,0,1080,1920);
  const big=lay==='big', fs=CS.size||(big?150:112); X.font=(CS.weight||900)+' '+fs+'px "'+fam+'", "Cairo", sans-serif'; X.textAlign='center'; X.direction='rtl';
  if(CS.dim>0){ X.fillStyle='rgba(0,0,0,'+CS.dim+')'; X.fillRect(0,0,1080,1920); }
  const L=wrapLines(X,title,big?940:900).slice(0,big?4:3), lh=fs*1.18, bh=L.length*lh+70, y0=lay==='bottom'?1920-bh-260:(lay==='big'||lay==='center')?(1920-bh)/2:230;
  if(!big&&CS.box!==false){ X.fillStyle=acc; const bw=Math.min(1000,Math.max(...L.map(l=>X.measureText(l).width))+90); X.beginPath(); (X.roundRect?X.roundRect((1080-bw)/2,y0,bw,bh,36):X.rect((1080-bw)/2,y0,bw,bh)); X.fill(); }
  X.fillStyle=CS.color||'#fff'; if(CS.shadow!==false){ X.shadowColor='rgba(0,0,0,'+(big||CS.box===false?.6:.25)+')'; X.shadowBlur=big||CS.box===false?24:8; } L.forEach((l,i)=>X.fillText(l,540,y0+35+fs*0.92+i*lh)); X.shadowBlur=0;
  if(!full){ cv.getContext('2d').drawImage(c,0,0); return null; } return c.toDataURL('image/jpeg',0.92); }
async function drawSlide(cv,i,full){ const w=fw(); if(!w) return null; const R=PUB.rp, n=(R.points||[]).length, S=full?1:cv.width/1080, c=w.document.createElement('canvas'); c.width=Math.round(1080*S); c.height=Math.round(1350*S);
  const X=c.getContext('2d'), fam=hs().cap.font||fval('FONT','Cairo'), acc=fval('ACC','#4C8DFF'); await fontReady(fam); X.setTransform(S,0,0,S,0,0);
  X.fillStyle='#0E1118'; X.fillRect(0,0,1080,1350); X.fillStyle=acc; X.fillRect(0,0,1080,14); X.textAlign='center'; X.direction='rtl';
  if(i===0){ if(PUB.cov&&PUB.cov.ok&&PUB.cov.frames[0]){ const im=await loadImg('/vfr/'+String(PUB.cov.frames[PUB.ci||0].f).padStart(5,'0')+'.jpg'); if(im){ X.globalAlpha=.42; X.drawImage(im,0,(1350-1920)/2,1080,1920); X.globalAlpha=1; } }
    X.font='900 104px "'+fam+'", "Cairo", sans-serif'; X.fillStyle='#fff'; const L=wrapLines(X,R.title,900).slice(0,5); L.forEach((l,j)=>X.fillText(l,540,(1350-L.length*124)/2+100+j*124)); X.font='600 40px "'+fam+'", sans-serif'; X.fillStyle=acc; X.fillText(t('carSwipe'),540,1250); }
  else if(i<=n){ X.font='900 84px "'+fam+'", "Cairo", sans-serif'; X.fillStyle=acc; X.direction='ltr'; X.fillText(String(i),540,250); X.direction='rtl'; X.font='800 74px "'+fam+'", "Cairo", sans-serif'; X.fillStyle='#fff'; const L=wrapLines(X,R.points[i-1],880).slice(0,8); L.forEach((l,j)=>X.fillText(l,540,(1350-L.length*100)/2+110+j*100)); X.font='500 34px sans-serif'; X.fillStyle='rgba(255,255,255,.4)'; X.direction='ltr'; X.fillText(i+' / '+n,540,1290); X.direction='rtl'; }
  else { X.font='900 92px "'+fam+'", "Cairo", sans-serif'; X.fillStyle='#fff'; const L=wrapLines(X,R.cta||'',880).slice(0,5); L.forEach((l,j)=>X.fillText(l,540,(1350-L.length*112)/2+90+j*112)); }
  if(!full){ cv.getContext('2d').drawImage(c,0,0); return null; } return c.toDataURL('image/png'); }
function pubSync(){ const R=PUB.rp; if(!R||!$('#rpTitle')) return; R.title=$('#rpTitle').value; R.points=$('#rpPts').value.split('\n').map(x=>x.trim()).filter(Boolean); if($('#rpCta')) R.cta=$('#rpCta').value; }
async function drawPub(){ if(RTAB!=='pub') return; const C=PUB.cov; if(C&&C.ok){ const tt=$('#covTx')?$('#covTx').value:C.title; for(const cv of $$('[data-cov]')) await drawCover(cv,C.frames[+cv.dataset.cov].f,tt,PUB.lay,false); }
  if(PUB.rp&&PUB.rp.title!=null) for(const cv of $$('[data-cs]')) await drawSlide(cv,+cv.dataset.cs,false); }
async function pubClick(el){ const d=el.dataset;
  if(d.cov!=null){ PUB.ci=+d.cov; $$('[data-cov]').forEach(x=>x.classList.toggle('on',x===el)); return true; }
  if(d.clay){ PUB.lay=d.clay; $$('[data-clay]').forEach(x=>x.classList.toggle('on',x===el)); drawPub(); return true; }
  if(el.id==='covSave'){ el.disabled=true; try{ const C=PUB.cov, url=await drawCover(null,C.frames[PUB.ci].f,$('#covTx').value,PUB.lay,true); const r=await api('/hs/cover_save',{i:PUB.ci+1,data:url}); if(r.ok){ toast(t('covDone')); PUB.cov=await api('/hs/covers'); renderRight(); drawPub(); } } finally{ el.disabled=false; } return true; }
  if(el.id==='carSave'){ pubSync(); el.disabled=true; try{ await api('/hs/repurpose',{save:PUB.rp}); const n=(PUB.rp.points||[]).length+(PUB.rp.ctaOn?2:1); for(let i=0;i<n;i++){ const url=await drawSlide(null,i,true); await api('/hs/carousel_save',{i:i+1,data:url,clear:i===0}); } $('#carOut').innerHTML='<p class="hint"><a href="/hs/carousel.zip?v='+Date.now()+'" download>'+t('carDl',n)+'</a></p>'; toast(t('carDone')); } finally{ el.disabled=false; } return true; }
  if(el.id==='rpRe'){ PUB.rp=await api('/hs/repurpose',{}); renderRight(); drawPub(); return true; }
  if(el.id==='rpClaude'){ if(!(await tokenGo('rp','small'))) return true; pubSync(); await api('/hs/repurpose',{save:PUB.rp}); const r=await api('/hs/claude_fix',{what:'repurpose'}); if(r.ok){ toast(t('rpClaudeGo')); } else toast(srvEn(r.msg)||t('failed')); return true; }
  if(d.copy){ const x=$('#'+d.copy); try{ await navigator.clipboard.writeText(x.value); toast(t('copied')); }catch(e){ x.select(); document.execCommand('copy'); toast(t('copied')); } return true; }
  if(d.pfp){ PUB.plat=d.pfp; $$('[data-pfp]').forEach(x=>x.classList.toggle('on',x===el)); return true; }
  if(el.id==='pfSave'){ const b={plat:PUB.plat||'tiktok'}; $$('[data-pf]').forEach(x=>b[x.dataset.pf]=x.value.trim()); PUB.perf=await api('/hs/perf',b); toast(t('pfDone')); return true; }
  return false; }

document.addEventListener('click',async e=>{ const el=e.target.closest('[data-rfx],#retClaude,[data-tkp],[data-cov],[data-clay],#covSave,#carSave,#rpRe,#rpClaude,[data-copy],[data-pfp],#pfSave'); if(!el) return; const d=el.dataset;
  if(d.rfx!=null){ e.preventDefault(); retFix(+d.rfx); return; }
  if(el.id==='retClaude'){ retClaude((RET.fixes||[]).map(f=>f.msg)); return; }
  if(d.tkp!=null){ e.preventDefault(); const c=ST.caps.cards[+d.tkp]; if(c) playRange(c.s,c.e); return; }
  await pubClick(el); });
document.addEventListener('input',e=>{ if(e.target.id==='covTx'){ PUB.ctitle=e.target.value; clearTimeout(PUB._t); PUB._t=setTimeout(drawPub,250); } else if(['rpTitle','rpPts','rpCta'].includes(e.target.id)){ pubSync(); clearTimeout(PUB._t); PUB._t=setTimeout(drawPub,350); } });
