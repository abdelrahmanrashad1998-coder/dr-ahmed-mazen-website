/* ============================================================
   service.js — Dr. Ahmed Mazen
   Interactivity for individual service pages
   ============================================================ */

(function () {
  'use strict';

  /* ── Language toggle ──────────────────────────────────────── */
  const html = document.documentElement;
  const savedLang = localStorage.getItem('lang') || 'ar';
  html.setAttribute('data-lang', savedLang);
  html.setAttribute('dir', savedLang === 'ar' ? 'rtl' : 'ltr');
  html.setAttribute('lang', savedLang);

  const langToggle = document.getElementById('langToggle');
  if (langToggle) {
    // Sync button label on load
    langToggle.textContent = savedLang === 'ar' ? 'EN' : 'AR';

    langToggle.addEventListener('click', () => {
      const next = html.getAttribute('data-lang') === 'ar' ? 'en' : 'ar';
      html.setAttribute('data-lang', next);
      html.setAttribute('dir', next === 'ar' ? 'rtl' : 'ltr');
      html.setAttribute('lang', next);
      localStorage.setItem('lang', next);
      langToggle.textContent = next === 'ar' ? 'EN' : 'AR';
    });
  }

  /* ── Mobile nav toggle ────────────────────────────────────── */
  const navToggle = document.getElementById('navToggle');
  const navMenu   = document.getElementById('navMenu');
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
      navMenu.classList.toggle('open');
      navToggle.setAttribute('aria-expanded',
        navMenu.classList.contains('open') ? 'true' : 'false');
    });
  }

  /* ── Navbar scroll shrink ─────────────────────────────────── */
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 60);
    }, { passive: true });
  }

  /* ── FAQ Accordion ────────────────────────────────────────── */
  function initFAQ() {
    const items = document.querySelectorAll('.faq-item');
    items.forEach(item => {
      // Support both .faq-question (service.css) and .faq-q (generate_pages.py)
      const btn = item.querySelector('.faq-question, .faq-q');
      if (!btn) return;
      btn.addEventListener('click', () => {
        const isOpen = item.classList.contains('open');
        // Close all
        items.forEach(i => i.classList.remove('open'));
        // Open clicked (toggle)
        if (!isOpen) item.classList.add('open');
      });
    });
  }
  initFAQ();

  /* ── Service gallery lightbox ─────────────────────────────── */
  function initGalleryLightbox() {
    const galleryItems = document.querySelectorAll('.service-gallery-item');
    const lightbox = document.getElementById('svcLightbox');
    const lightboxImg = document.getElementById('svcLightboxImg');
    const closeBtn = document.getElementById('svcLightboxClose');

    if (!lightbox || !lightboxImg) return;

    let currentIndex = 0;
    const images = Array.from(galleryItems).map(el => el.querySelector('img'));

    function open(index) {
      currentIndex = index;
      const img = images[index];
      if (img) {
        lightboxImg.src = img.src;
        lightboxImg.alt = img.alt || '';
      }
      lightbox.classList.add('open');
      document.body.style.overflow = 'hidden';
    }

    function close() {
      lightbox.classList.remove('open');
      document.body.style.overflow = '';
    }

    galleryItems.forEach((item, i) => {
      item.addEventListener('click', () => open(i));
      item.setAttribute('role', 'button');
      item.setAttribute('tabindex', '0');
      item.addEventListener('keydown', e => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(i); }
      });
    });

    if (closeBtn) closeBtn.addEventListener('click', close);
    lightbox.addEventListener('click', e => { if (e.target === lightbox) close(); });

    document.addEventListener('keydown', e => {
      if (!lightbox.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
        const dir = e.key === 'ArrowRight' ? 1 : -1;
        // Flip direction for RTL
        const rtlDir = html.getAttribute('dir') === 'rtl' ? -dir : dir;
        const next = (currentIndex + rtlDir + images.length) % images.length;
        open(next);
      }
    });
  }
  initGalleryLightbox();

  /* ── IntersectionObserver reveal ─────────────────────────── */
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('visible'));
  }

  /* ── Smooth anchor scroll ─────────────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

})();
