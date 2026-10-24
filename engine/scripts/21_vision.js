/* عين السكل: مكان الوجه + قناع الشخص. يشتغل على ويندوز وماك ولينكس داخل كروم (بلا نت وبلا تثبيت إضافي).
   node 21_vision.js <work> face                  ← يكتب face.json + hs-face.js (مكان الوجه كل ثلث ثانية)
   node 21_vision.js <work> mask 3.2-6.8 [12-15]  ← يكتب mk/NNNNN.png لفريمات المدى + hs-mask.js
   node 21_vision.js <work> mask all              ← كل المقطع (أبطأ)
   node 21_vision.js <work> clear                 ← يحذف الأقنعة
   الموديلات داخل engine/vision (MediaPipe · Apache 2.0). كل شي محلي: الفريمات ما تطلع من الجهاز. */
const http=require('http'), fs=require('fs'), path=require('path');
const W=path.resolve(process.argv[2]||'.')+path.sep, MODE=process.argv[3]||'face', ARGS=process.argv.slice(4);
const VIS=path.join(__dirname,'..','vision'), FPS=30, STEP=10;
function resolvePuppeteer(){ for(const p of [process.env.PUPPETEER_PATH,'puppeteer-core','puppeteer',path.join(__dirname,'..','node_modules/puppeteer-core'),path.join(process.cwd(),'node_modules/puppeteer-core'),path.join(require('os').homedir(),'.hojas-studio','node_modules','puppeteer-core')]){ if(!p) continue; try{ return require(p); }catch(e){} } throw new Error('ما لقيت puppeteer-core'); }
function findChrome(){ if(process.env.CHROME_PATH) return process.env.CHROME_PATH; const LA=process.env.LOCALAPPDATA||'', PF=process.env.ProgramFiles||'C:/Program Files', P86=process.env['ProgramFiles(x86)']||'C:/Program Files (x86)';
  for(const c of ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',PF+'/Google/Chrome/Application/chrome.exe',P86+'/Google/Chrome/Application/chrome.exe',LA+'/Google/Chrome/Application/chrome.exe',PF+'/Microsoft/Edge/Application/msedge.exe',P86+'/Microsoft/Edge/Application/msedge.exe','/usr/bin/google-chrome','/usr/bin/chromium','/usr/bin/chromium-browser']){ try{ if(c&&fs.existsSync(c)) return c; }catch(e){} } throw new Error('ما لقيت كروم — حدّد CHROME_PATH'); }
const pad=n=>String(n).padStart(5,'0');
const frames=()=>fs.existsSync(W+'vfr')?fs.readdirSync(W+'vfr').filter(f=>/^\d{5}\.jpg$/.test(f)).length:0;
function maskIndex(){ const d=W+'mk'; const have=fs.existsSync(d)?fs.readdirSync(d).filter(f=>/^\d{5}\.png$/.test(f)).map(f=>+f.slice(0,5)).sort((a,b)=>a-b):[]; const r=[]; for(const n of have){ const l=r[r.length-1]; if(l&&n===l[1]+1) l[1]=n; else r.push([n,n]); }
  fs.writeFileSync(W+'hs-mask.js','window.__hsMask='+JSON.stringify({v:Date.now(),ranges:r})+';'); return r; }
if(MODE==='clear'){ try{ fs.rmSync(W+'mk',{recursive:true,force:true}); }catch(e){} maskIndex(); console.log('انحذفت الأقنعة.'); process.exit(0); }
const N=frames(); if(!N){ console.error('ما فيه فريمات (vfr/) — جهّز الفيديو أول.'); process.exit(3); }
for(const f of ['vision_bundle.mjs','wasm/vision_wasm_internal.wasm','selfie_segmentation.tflite','face_detection_short_range.tflite']) if(!fs.existsSync(path.join(VIS,f))){ console.error('ملف ناقص من السكل: engine/vision/'+f); process.exit(4); }
let want=[];
if(MODE==='face'){ for(let n=1;n<=N;n+=STEP) want.push(n); }
else if(MODE==='mask'){ const set=new Set(); for(const a of (ARGS.length?ARGS:['all'])){ if(a==='all'){ for(let n=1;n<=N;n++) set.add(n); continue; } const m=String(a).match(/^([\d.]+)-([\d.]+)$/); if(!m){ console.error('المدى بالثواني بشكل 3.2-6.8'); process.exit(2); }
    const f0=Math.max(1,Math.floor((+m[1]-0.5)*FPS)+1), f1=Math.min(N,Math.ceil((+m[2]+0.7)*FPS)+1); for(let n=f0;n<=f1;n++) set.add(n); }
  fs.mkdirSync(W+'mk',{recursive:true}); want=[...set].sort((a,b)=>a-b).filter(n=>!fs.existsSync(W+'mk/'+pad(n)+'.png')||ARGS.includes('--force'));
  if(!want.length){ maskIndex(); console.log('الأقنعة جاهزة من قبل.'); process.exit(0); } }
else { console.error('21_vision.js <work> face | mask <ث-ث> … | clear'); process.exit(2); }
const MIME={'.mjs':'text/javascript','.js':'text/javascript','.wasm':'application/wasm','.tflite':'application/octet-stream','.jpg':'image/jpeg'};
const srv=http.createServer((q,r)=>{ const u=decodeURIComponent(q.url.split('?')[0]);
  if(u==='/'){ r.writeHead(200,{'content-type':'text/html'}); return r.end('<!doctype html><meta charset=utf-8><body>'); }
  const f=u.startsWith('/vision/')?path.join(VIS,path.normalize(u.slice(8))):/^\/vfr\/\d{5}\.jpg$/.test(u)?path.join(W,'vfr',u.slice(5)):null;
  if(!f||f.includes('..')||!fs.existsSync(f)){ r.writeHead(404); return r.end(); }
  r.writeHead(200,{'content-type':MIME[path.extname(f)]||'application/octet-stream','cache-control':'no-store'}); fs.createReadStream(f).pipe(r); });
srv.listen(0,'127.0.0.1',async()=>{ const port=srv.address().port; let b;
  try{ b=await resolvePuppeteer().launch({executablePath:findChrome(),headless:'new',args:['--no-sandbox','--disable-dev-shm-usage']}); const p=await b.newPage(); p.on('pageerror',e=>console.error('page: '+e.message));
    await p.goto('http://127.0.0.1:'+port+'/');
    await p.evaluate(async(mode)=>{ const m=await import('/vision/vision_bundle.mjs'), fsr=await m.FilesetResolver.forVisionTasks('/vision/wasm'); window.__load=async n=>{ const im=new Image(); im.src='/vfr/'+String(n).padStart(5,'0')+'.jpg'; await im.decode(); return im; };
      if(mode==='face'){ const fd=await m.FaceDetector.createFromOptions(fsr,{baseOptions:{modelAssetPath:'/vision/face_detection_short_range.tflite',delegate:'CPU'},runningMode:'IMAGE',minDetectionConfidence:0.5});
        window.__run=async n=>{ const im=await window.__load(n), r=fd.detect(im), W=im.naturalWidth, H=im.naturalHeight; let best=null; for(const d of r.detections){ const b=d.boundingBox; if(!best||b.width*b.height>best.width*best.height) best=b; }
          return best?[+((best.originX+best.width/2)/W).toFixed(4),+((best.originY+best.height/2)/H).toFixed(4),+(best.width/W).toFixed(4),+(best.height/H).toFixed(4)]:null; }; }
      else { const sg=await m.ImageSegmenter.createFromOptions(fsr,{baseOptions:{modelAssetPath:'/vision/selfie_segmentation.tflite',delegate:'CPU'},runningMode:'IMAGE',outputConfidenceMasks:true,outputCategoryMask:false});
        let prev=null, prevN=0; const tmp=document.createElement('canvas'), out=document.createElement('canvas');
        window.__run=async n=>{ const im=await window.__load(n), r=sg.segment(im), k=r.confidenceMasks[r.confidenceMasks.length-1], w=k.width, h=k.height, a=k.getAsFloat32Array().slice(); if(r.close) r.close();
          if(prev&&prev.length===a.length&&n===prevN+1){ for(let i=0;i<a.length;i++) a[i]=a[i]*0.72+prev[i]*0.28; } prev=a; prevN=n;       /* تنعيم بين الفريمات: يخفف رجفة الحواف */
          tmp.width=w; tmp.height=h; const tx=tmp.getContext('2d'), id=tx.createImageData(w,h), d=id.data; for(let i=0;i<a.length;i++){ let v=(a[i]-0.32)/0.36; v=v<0?0:v>1?1:v; v=v*v*(3-2*v); const o=i*4; d[o]=255; d[o+1]=255; d[o+2]=255; d[o+3]=Math.round(v*255); } tx.putImageData(id,0,0);
          out.width=Math.round(im.naturalWidth/2); out.height=Math.round(im.naturalHeight/2); const ox=out.getContext('2d'); ox.clearRect(0,0,out.width,out.height); ox.filter='blur(1.6px)'; ox.imageSmoothingQuality='high'; ox.drawImage(tmp,0,0,out.width,out.height); ox.filter='none';
          return out.toDataURL('image/png'); }; } },MODE);
    const t0=Date.now(); let done=0;
    if(MODE==='face'){ const raw=[]; for(const n of want){ raw.push([n,await p.evaluate(n=>window.__run(n),n)]); if(++done%40===0) console.log('وجه: '+done+'/'+want.length); }
      const hit=raw.filter(x=>x[1]); if(hit.length<Math.max(2,raw.length*0.15)){ fs.writeFileSync(W+'face.json',JSON.stringify({v:1,found:false,n:N})); fs.writeFileSync(W+'hs-face.js','window.__hsFace=null;'); console.log('ما لقيت وجه واضح بالمقطع (لقيته بـ'+hit.length+' من '+raw.length+' لقطة). المكان الافتراضي يبقى.'); }
      else { /* تعبئة الناقص بأقرب قيمة ثم وسيط متحرك: الكادر يتحرك بهدوء وما يرجف */
        const full=raw.map((x,i)=>{ if(x[1]) return x[1]; let j=1; while(i-j>=0||i+j<raw.length){ if(i-j>=0&&raw[i-j][1]) return raw[i-j][1]; if(i+j<raw.length&&raw[i+j][1]) return raw[i+j][1]; j++; } return hit[0][1]; });
        const med=a=>{ const s=a.slice().sort((x,y)=>x-y); return s[Math.floor(s.length/2)]; }, R=6;
        const pts=raw.map((x,i)=>{ const win=full.slice(Math.max(0,i-R),i+R+1); return [+(((x[0]-1)/FPS).toFixed(2)),...[0,1,2,3].map(k=>+med(win.map(v=>v[k])).toFixed(4))]; });
        const all=k=>med(full.map(v=>v[k])); const o={v:1,found:true,n:N,step:STEP,avg:[0,1,2,3].map(k=>+all(k).toFixed(4)),pts:pts};
        fs.writeFileSync(W+'face.json',JSON.stringify(o)); fs.writeFileSync(W+'hs-face.js','window.__hsFace='+JSON.stringify(o)+';');
        console.log('الوجه: وسط الكادر عند '+Math.round(o.avg[0]*100)+'% عرض و'+Math.round(o.avg[1]*100)+'% ارتفاع · حجمه '+Math.round(o.avg[3]*100)+'% من الارتفاع ('+hit.length+'/'+raw.length+' لقطة)'); } }
    else { for(const n of want){ const u=await p.evaluate(n=>window.__run(n),n); fs.writeFileSync(W+'mk/'+pad(n)+'.png',Buffer.from(u.split(',')[1],'base64')); if(++done%30===0) console.log('قناع: '+done+'/'+want.length); }
      const r=maskIndex(); console.log('قناع الشخص جاهز: '+want.length+' فريم ('+((Date.now()-t0)/1000).toFixed(1)+' ث) · المدى: '+r.map(x=>((x[0]-1)/FPS).toFixed(1)+'-'+((x[1]-1)/FPS).toFixed(1)).join(' · ')); }
  }catch(e){ console.error('vision failed: '+e.message); process.exitCode=1; }
  finally{ try{ if(b) await b.close(); }catch(e){} srv.close(); } });
