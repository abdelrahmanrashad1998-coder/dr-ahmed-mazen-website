/* ============================================================
   slideshow.js — Dr. Ahmed Mazen
   Reusable auto-advancing before/after slider
   Call: initSlideshow(options) after DOM ready
   ============================================================ */

(function(global) {
  'use strict';

  /**
   * @param {Object} opts
   *   containerId  {string}   - id of .slideshow-banner
   *   trackId      {string}   - id of .slide-track
   *   prevId       {string}   - id of prev arrow button
   *   nextId       {string}   - id of next arrow button
   *   dotsId       {string}   - id of .slide-dots container
   *   lightboxId   {string}   - id of .ss-lightbox overlay
   *   lbImgId      {string}   - id of lightbox <img>
   *   lbCloseId    {string}   - id of close button
   *   lbPrevId     {string}   - id of lightbox prev button
   *   lbNextId     {string}   - id of lightbox next button
   *   images       {Array}    - [{src, alt}]
   *   interval     {number}   - ms between slides (default 4000)
   *   visibleCount {number}   - slides visible at once (calculated via CSS, 1|2|3)
   */
  function initSlideshow(opts) {
    const container  = document.getElementById(opts.containerId);
    const track      = document.getElementById(opts.trackId);
    const dotsWrap   = document.getElementById(opts.dotsId);
    const prevBtn    = document.getElementById(opts.prevId);
    const nextBtn    = document.getElementById(opts.nextId);
    const lightbox   = document.getElementById(opts.lightboxId);
    const lbImg      = document.getElementById(opts.lbImgId);
    const lbClose    = document.getElementById(opts.lbCloseId);
    const lbPrev     = document.getElementById(opts.lbPrevId);
    const lbNext     = document.getElementById(opts.lbNextId);

    if (!container || !track) return;

    const images   = opts.images || [];
    const interval = opts.interval || 4000;
    let current    = 0;
    let autoTimer  = null;
    let lbIndex    = 0;
    let touchStartX = 0;
    let isDragging  = false;
    let dragStartX  = 0;
    let dragOffset  = 0;

    // ── Build slides ────────────────────────────────────────
    track.innerHTML = '';
    images.forEach((img, i) => {
      const slide = document.createElement('div');
      slide.className = 'slide';
      slide.innerHTML = `
        <div class="slide-inner" data-index="${i}" role="button" tabindex="0" aria-label="View result ${i+1}">
          <img src="${img.src}" alt="${img.alt}" loading="lazy" />
          <div class="slide-overlay">
            <div class="slide-overlay-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/><path d="M11 8v6M8 11h6"/>
              </svg>
            </div>
          </div>
        </div>`;
      track.appendChild(slide);
    });

    // ── Build dots ──────────────────────────────────────────
    function getVisibleCount() {
      const w = window.innerWidth;
      if (w <= 540) return 1;
      if (w <= 900) return 2;
      return 3;
    }

    function buildDots() {
      if (!dotsWrap) return;
      const vis = getVisibleCount();
      const total = Math.ceil(images.length / vis);
      dotsWrap.innerHTML = '';
      for (let i = 0; i < total; i++) {
        const dot = document.createElement('button');
        dot.className = 'slide-dot' + (i === 0 ? ' active' : '');
        dot.setAttribute('aria-label', `Go to slide group ${i+1}`);
        dot.addEventListener('click', () => goTo(i * vis));
        dotsWrap.appendChild(dot);
      }
    }

    function updateDots() {
      if (!dotsWrap) return;
      const vis = getVisibleCount();
      const dotIndex = Math.floor(current / vis);
      dotsWrap.querySelectorAll('.slide-dot').forEach((d, i) => {
        d.classList.toggle('active', i === dotIndex);
      });
    }

    // ── Navigate ────────────────────────────────────────────
    function getSlideWidth() {
      const slides = track.querySelectorAll('.slide');
      if (!slides.length) return 0;
      return slides[0].getBoundingClientRect().width;
    }

    function isRTL() {
      return document.documentElement.getAttribute('dir') === 'rtl';
    }

    function goTo(index) {
      const vis = getVisibleCount();
      const max = images.length - vis;
      current = Math.max(0, Math.min(index, max));
      // Always use positive offset; track is forced LTR via CSS
      const slideW = container.getBoundingClientRect().width / vis;
      const offset = -(current * slideW);
      track.style.transform = `translateX(${offset}px)`;
      updateDots();
    }

    function goNext() {
      const vis = getVisibleCount();
      const max = images.length - vis;
      goTo(current + vis >= max ? 0 : current + vis);
    }

    function goPrev() {
      const vis = getVisibleCount();
      const max = images.length - vis;
      goTo(current <= 0 ? max : current - vis);
    }

    // ── Autoplay ────────────────────────────────────────────
    function startAuto() {
      stopAuto();
      autoTimer = setInterval(goNext, interval);
    }

    function stopAuto() {
      if (autoTimer) { clearInterval(autoTimer); autoTimer = null; }
    }

    // ── Touch / drag ────────────────────────────────────────
    container.addEventListener('mousedown', e => {
      isDragging = true;
      dragStartX = e.clientX;
      container.style.cursor = 'grabbing';
      stopAuto();
    });

    document.addEventListener('mousemove', e => {
      if (!isDragging) return;
      dragOffset = e.clientX - dragStartX;
    });

    document.addEventListener('mouseup', () => {
      if (!isDragging) return;
      isDragging = false;
      container.style.cursor = 'grab';
      if (Math.abs(dragOffset) > 60) {
        dragOffset > 0 ? goPrev() : goNext();
      }
      dragOffset = 0;
      startAuto();
    });

    container.addEventListener('touchstart', e => {
      touchStartX = e.touches[0].clientX;
      stopAuto();
    }, { passive: true });

    container.addEventListener('touchend', e => {
      const diff = e.changedTouches[0].clientX - touchStartX;
      if (Math.abs(diff) > 50) { diff > 0 ? goPrev() : goNext(); }
      startAuto();
    }, { passive: true });

    // ── Pause on hover ──────────────────────────────────────
    container.addEventListener('mouseenter', stopAuto);
    container.addEventListener('mouseleave', startAuto);

    // ── Arrow buttons (aware of RTL visual swap) ─────────────
    // In RTL the CSS swaps arrow positions, so the LEFT arrow is "next"
    // and the RIGHT arrow is "prev" visually — but we wire by logical function
    if (prevBtn) prevBtn.addEventListener('click', () => { goPrev(); startAuto(); });
    if (nextBtn) nextBtn.addEventListener('click', () => { goNext(); startAuto(); });

    // ── Slide click → lightbox ──────────────────────────────
    track.addEventListener('click', e => {
      const inner = e.target.closest('.slide-inner');
      if (!inner) return;
      const idx = parseInt(inner.dataset.index, 10);
      openLightbox(idx);
    });
    track.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') {
        const inner = e.target.closest('.slide-inner');
        if (inner) openLightbox(parseInt(inner.dataset.index, 10));
      }
    });

    // ── Lightbox ────────────────────────────────────────────
    function openLightbox(idx) {
      lbIndex = idx;
      if (lbImg) {
        lbImg.src = images[lbIndex].src;
        lbImg.alt = images[lbIndex].alt;
      }
      if (lightbox) {
        lightbox.classList.add('open');
        document.body.style.overflow = 'hidden';
      }
    }

    function closeLightbox() {
      if (lightbox) {
        lightbox.classList.remove('open');
        document.body.style.overflow = '';
      }
    }

    function lbGoNext() {
      lbIndex = (lbIndex + 1) % images.length;
      if (lbImg) { lbImg.src = images[lbIndex].src; lbImg.alt = images[lbIndex].alt; }
    }

    function lbGoPrev() {
      lbIndex = (lbIndex - 1 + images.length) % images.length;
      if (lbImg) { lbImg.src = images[lbIndex].src; lbImg.alt = images[lbIndex].alt; }
    }

    if (lbClose) lbClose.addEventListener('click', closeLightbox);
    if (lbPrev)  lbPrev.addEventListener('click', lbGoPrev);
    if (lbNext)  lbNext.addEventListener('click', lbGoNext);
    if (lightbox) {
      lightbox.addEventListener('click', e => { if (e.target === lightbox) closeLightbox(); });
    }

    document.addEventListener('keydown', e => {
      if (lightbox && lightbox.classList.contains('open')) {
        if (e.key === 'Escape')    closeLightbox();
        if (e.key === 'ArrowLeft')  lbGoPrev();
        if (e.key === 'ArrowRight') lbGoNext();
      }
    });

    // ── Resize: recalculate ──────────────────────────────────
    let resizeTimer;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => {
        buildDots();
        goTo(0); // reset on resize
      }, 200);
    });

    // ── Init ─────────────────────────────────────────────────
    buildDots();
    goTo(0);
    startAuto();
  }

  // Expose globally
  global.initSlideshow = initSlideshow;

})(window);
