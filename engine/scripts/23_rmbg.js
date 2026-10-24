/* 4.11: شيل الخلفية من صورة فيها شخص (موديل فصل الشخص اللي بالسكل، MediaPipe · Apache 2.0). كل شي على الجهاز.
   node 23_rmbg.js <صورة> <ناتج.png>   ← يطبع {"person":0.42} (نسبة الشخص من الصورة) */
const http=require('http'), fs=require('fs'), path=require('path');
const IN=path.resolve(process.argv[2]||''), OUT=path.resolve(process.argv[3]||''), VIS=path.join(__dirname,'..','vision');
if(!fs.existsSync(IN)||!process.argv[3]){ console.error('23_rmbg.js <صورة> <ناتج.png>'); process.exit(2); }
for(const f of ['vision_bundle.mjs','wasm/vision_wasm_internal.wasm','selfie_segmentation.tflite']) if(!fs.existsSync(path.join(VIS,f))){ console.error('ملف ناقص: engine/vision/'+f); process.exit(3); }
function resolvePuppeteer(){ for(const p of [process.env.PUPPETEER_PATH,'puppeteer-core','puppeteer',path.join(__dirname,'..','node_modules/puppeteer-core'),path.join(process.cwd(),'node_modules/puppeteer-core'),path.join(require('os').homedir(),'.hojas-studio','node_modules','puppeteer-core')]){ if(!p) continue; try{ return require(p); }catch(e){} } throw new Error('ما لقيت puppeteer-core'); }
function findChrome(){ if(process.env.CHROME_PATH) return process.env.CHROME_PATH; const LA=process.env.LOCALAPPDATA||'', PF=process.env.ProgramFiles||'C:/Program Files', P86=process.env['ProgramFiles(x86)']||'C:/Program Files (x86)';
  for(const c of ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',PF+'/Google/Chrome/Application/chrome.exe',P86+'/Google/Chrome/Application/chrome.exe',LA+'/Google/Chrome/Application/chrome.exe',PF+'/Microsoft/Edge/Application/msedge.exe',P86+'/Microsoft/Edge/Application/msedge.exe','/usr/bin/google-chrome','/usr/bin/chromium','/usr/bin/chromium-browser']){ try{ if(c&&fs.existsSync(c)) return c; }catch(e){} } throw new Error('ما لقيت كروم — حدّد CHROME_PATH'); }
const MIME={'.mjs':'text/javascript','.js':'text/javascript','.wasm':'application/wasm','.tflite':'application/octet-stream','.jpg':'image/jpeg','.jpeg':'image/jpeg','.png':'image/png','.webp':'image/webp'};
const srv=http.createServer((q,r)=>{ const u=decodeURIComponent(q.url.split('?')[0]);
  if(u==='/'){ r.writeHead(200,{'content-type':'text/html'}); return r.end('<!doctype html><meta charset=utf-8><body>'); }
  const f=u.startsWith('/vision/')?path.join(VIS,path.normalize(u.slice(8))):u==='/in'?IN:null;
  if(!f||f.includes('..')||!fs.existsSync(f)){ r.writeHead(404); return r.end(); }
  r.writeHead(200,{'content-type':MIME[path.extname(f).toLowerCase()]||'application/octet-stream','cache-control':'no-store'}); fs.createReadStream(f).pipe(r); });
srv.listen(0,'127.0.0.1',async()=>{ const port=srv.address().port; let b;
  try{ b=await resolvePuppeteer().launch({executablePath:findChrome(),headless:'new',args:['--no-sandbox','--disable-dev-shm-usage']}); const p=await b.newPage();
    await p.goto('http://127.0.0.1:'+port+'/');
    const res=await p.evaluate(async()=>{ const m=await import('/vision/vision_bundle.mjs'), fsr=await m.FilesetResolver.forVisionTasks('/vision/wasm');
      const sg=await m.ImageSegmenter.createFromOptions(fsr,{baseOptions:{modelAssetPath:'/vision/selfie_segmentation.tflite',delegate:'CPU'},runningMode:'IMAGE',outputConfidenceMasks:true,outputCategoryMask:false});
      const im=new Image(); im.src='/in'; await im.decode(); const W=im.naturalWidth, H=im.naturalHeight, r=sg.segment(im), k=r.confidenceMasks[r.confidenceMasks.length-1], w=k.width, h=k.height, a=k.getAsFloat32Array().slice(); if(r.close) r.close();
      const tmp=document.createElement('canvas'); tmp.width=w; tmp.height=h; const tx=tmp.getContext('2d'), id=tx.createImageData(w,h), d=id.data; let on=0;
      for(let i=0;i<a.length;i++){ let v=(a[i]-0.3)/0.4; v=v<0?0:v>1?1:v; v=v*v*(3-2*v); if(v>0.5) on++; const o=i*4; d[o]=d[o+1]=d[o+2]=255; d[o+3]=Math.round(v*255); } tx.putImageData(id,0,0);
      const out=document.createElement('canvas'); out.width=W; out.height=H; const ox=out.getContext('2d'); ox.drawImage(im,0,0); ox.globalCompositeOperation='destination-in'; ox.filter='blur(1.2px)'; ox.drawImage(tmp,0,0,W,H); ox.filter='none';
      return {url:out.toDataURL('image/png'), person:+(on/a.length).toFixed(3)}; });
    if(res.person<0.02){ console.error('ما لقيت شخص بالصورة'); process.exitCode=4; }
    else { fs.writeFileSync(OUT,Buffer.from(res.url.split(',')[1],'base64')); console.log(JSON.stringify({person:res.person})); }
  }catch(e){ console.error('rmbg failed: '+e.message); process.exitCode=1; }
  finally{ try{ if(b) await b.close(); }catch(e){} srv.close(); } });
