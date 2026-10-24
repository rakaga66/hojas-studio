/* لقطة لصفحة موقع (للعرض داخل إطار متصفح بالمونتاج).
   node 20_shot.js <url> <out.png> [--full] [--width 1200]
   --full = الصفحة كاملة بطولها (عشان تتحرك لتحت داخل الإطار) · بدونها = أول شاشة فقط */
const path=require('path');
function resolvePuppeteer(){ for(const p of [process.env.PUPPETEER_PATH,'puppeteer-core','puppeteer',path.join(__dirname,'..','node_modules/puppeteer-core'),path.join(process.cwd(),'node_modules/puppeteer-core'),path.join(require('os').homedir(),'.hojas-studio','node_modules','puppeteer-core')]){ if(!p) continue; try{ return require(p); }catch(e){} } throw new Error('ما لقيت puppeteer-core'); }
function findChrome(){ if(process.env.CHROME_PATH) return process.env.CHROME_PATH; const fs=require('fs'), LA=process.env.LOCALAPPDATA||'', PF=process.env.ProgramFiles||'C:/Program Files', P86=process.env['ProgramFiles(x86)']||'C:/Program Files (x86)';
  for(const c of ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',PF+'/Google/Chrome/Application/chrome.exe',P86+'/Google/Chrome/Application/chrome.exe',LA+'/Google/Chrome/Application/chrome.exe',PF+'/Microsoft/Edge/Application/msedge.exe',P86+'/Microsoft/Edge/Application/msedge.exe','/usr/bin/google-chrome','/usr/bin/chromium','/usr/bin/chromium-browser']) if(c&&fs.existsSync(c)) return c; throw new Error('ما لقيت Chrome'); }
(async()=>{ const a=process.argv.slice(2), url=a[0], out=a[1], full=a.includes('--full'), wi=a.indexOf('--width'), W=wi>=0?+a[wi+1]:1200;
  if(!url||!out){ console.error('usage: 20_shot.js <url> <out.png> [--full] [--width 1200]'); process.exit(2); }
  const pp=resolvePuppeteer(), b=await pp.launch({executablePath:findChrome(),headless:'new',args:['--no-sandbox','--hide-scrollbars']});
  try{ const p=await b.newPage(); await p.setViewport({width:W,height:Math.round(W*1.25),deviceScaleFactor:1.5});
    await p.goto(url,{waitUntil:'networkidle2',timeout:45000}).catch(async()=>{ await p.goto(url,{waitUntil:'domcontentloaded',timeout:45000}); });
    await new Promise(r=>setTimeout(r,1200));
    if(full){ const h=await p.evaluate(()=>Math.min(document.documentElement.scrollHeight,6000)); await p.screenshot({path:out,clip:{x:0,y:0,width:W,height:Math.max(600,h)}}); }
    else await p.screenshot({path:out});
    console.log('shot ok '+out); }
  finally{ await b.close(); } })().catch(e=>{ console.error('shot failed: '+e.message); process.exit(1); });
