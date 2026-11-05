(() => {
  // القائمة على الجوال
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    nav.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => { nav.classList.remove('is-open'); toggle.setAttribute('aria-expanded', 'false'); }));
  }

  // موجة الصوت في التايم لاين التوضيحي (زخرفية)
  document.querySelectorAll('.wave[data-bars]').forEach((el) => {
    const count = Number(el.dataset.bars) || 48;
    for (let i = 0; i < count; i++) {
      const bar = document.createElement('i');
      const h = 22 + Math.abs(Math.sin(i * 1.3) * 60 * (0.55 + 0.45 * Math.cos(i * 0.37)));
      bar.style.height = Math.min(100, Math.round(h)) + '%';
      el.appendChild(bar);
    }
  });

  // إعلان التحديث: يطلع مرة وحدة لكل نسخة جديدة، وما يرجع بعد ما تقفله
  const ver = document.documentElement.dataset.ver;
  let seen = null; try { seen = localStorage.getItem('hs-seen-ver'); } catch (e) {}
  if (ver && seen !== ver) {
    const d = document.createElement('div'); d.className = 'upd'; d.setAttribute('role', 'dialog'); d.setAttribute('aria-modal', 'true'); d.setAttribute('aria-labelledby', 'upd-t');
    d.innerHTML = '<div class="upd-card"><button class="upd-x" type="button" aria-label="إغلاق">×</button>'
      + '<img src="/assets/img/board.jpg" width="1600" height="800" alt="">'
      + '<div class="upd-body"><p class="upd-k">نزّلنا تحديث جديد · ' + ver + '</p><h2 id="upd-t">السبورة: شرح متحرك يرسمه Claude على كلامك</h2>'
      + '<p>تكلم عن فكرة، وClaude يرسمها بالطباشير فوق مقطعك: النص ينكتب لحظة ما تقوله، والرسم ينرسم، وشخصيات وصور توضحها. والتفريغ صار حرفي.</p>'
      + '<div class="upd-acts"><a class="btn btn-primary" href="/#new">شوف الجديد</a><a class="btn btn-ghost" href="/downloads/hojas-studio.zip" download>حمّل التحديث</a></div>'
      + '<p class="upd-note">بلقن Claude Code يتحدّث لحاله.</p></div></div>';
    const close = () => { try { localStorage.setItem('hs-seen-ver', ver); } catch (e) {} d.remove(); document.removeEventListener('keydown', esc); };
    const esc = (e) => { if (e.key === 'Escape') close(); };
    d.addEventListener('click', (e) => { if (e.target === d || e.target.closest('.upd-x') || e.target.closest('.upd-acts a')) close(); });
    document.addEventListener('keydown', esc);
    document.body.appendChild(d); setTimeout(() => { const x = d.querySelector('.upd-x'); if (x) x.focus(); }, 50);
  }

  // نسخ أمر التثبيت
  document.querySelectorAll('.copy[data-copy]').forEach((b) => {
    b.addEventListener('click', async () => {
      const text = document.getElementById(b.dataset.copy).textContent.trim();
      try { await navigator.clipboard.writeText(text); }
      catch (e) { const r = document.createRange(); r.selectNodeContents(document.getElementById(b.dataset.copy)); const s = getSelection(); s.removeAllRanges(); s.addRange(r); }
      const old = b.textContent; b.textContent = 'انتسخ'; b.classList.add('done');
      setTimeout(() => { b.textContent = old; b.classList.remove('done'); }, 1800);
    });
  });
})();
