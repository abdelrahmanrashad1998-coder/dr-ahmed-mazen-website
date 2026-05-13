/* ════════════════════════════════════════
   DR. AHMED MAZEN — MAIN JAVASCRIPT
   ════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

  /* ── Gallery Images ── */
  const galleryImages = [
    { src: 'assets/before-after/result-01.jpg', alt: 'Face Lift Filler Result' },
    { src: 'assets/before-after/result-02.jpg', alt: 'Face Contouring Result' },
    { src: 'assets/before-after/result-03.jpg', alt: 'Jawline Filler Result' },
    { src: 'assets/before-after/result-04.jpg', alt: 'Face Treatment Result' },
    { src: 'assets/before-after/result-05.jpg', alt: 'Aesthetic Treatment Result' },
    { src: 'assets/before-after/result-06.jpg', alt: 'Facial Filler Result' },
    { src: 'assets/before-after/result-07.jpg', alt: 'Skin Glow Result' },
    { src: 'assets/before-after/result-08.jpg', alt: 'Face Lift Result' },
    { src: 'assets/before-after/result-09.jpg', alt: 'Cheek Contouring Result' },
    { src: 'assets/before-after/result-10.jpg', alt: 'Facial Aesthetic Result' },
    { src: 'assets/before-after/result-11.jpg', alt: 'Lip Filler Result' },
    { src: 'assets/before-after/result-12.jpg', alt: 'Sagging Skin Treatment' },
    { src: 'assets/before-after/result-13.jpg', alt: 'Facial Rejuvenation Result' },
    { src: 'assets/before-after/result-14.jpg', alt: 'Natural Beauty Result' },
    { src: 'assets/before-after/result-15.jpg', alt: 'Aesthetic Medicine Result' },
    { src: 'assets/before-after/result-16.jpg', alt: 'Patient Result' },
    { src: 'assets/before-after/result-17.jpg', alt: 'Lip Enhancement Result' },
    { src: 'assets/before-after/result-18.jpg', alt: 'Facial Transformation' },
    { src: 'assets/before-after/result-19.jpg', alt: 'Non-Surgical Result' },
    { src: 'assets/before-after/result-20.jpg', alt: 'Skin Rejuvenation Result' },
    { src: 'assets/before-after/result-21.jpg', alt: 'Beauty Enhancement Result' },
  ];

  /* ── Build Gallery ── */
  const grid = document.getElementById('galleryGrid');
  if (grid) {
    galleryImages.forEach((img, i) => {
      const item = document.createElement('div');
      item.className = 'gallery-item reveal';
      item.dataset.index = i;
      item.innerHTML = `
        <img src="${img.src}" alt="${img.alt}" loading="lazy" />
        <div class="gallery-item-overlay">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/>
            <path d="M11 8v6M8 11h6"/>
          </svg>
        </div>
      `;
      item.addEventListener('click', () => openLightbox(i));
      grid.appendChild(item);
    });
  }

  /* ── Lightbox ── */
  let currentIndex = 0;
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxClose = document.getElementById('lightboxClose');
  const lightboxPrev = document.getElementById('lightboxPrev');
  const lightboxNext = document.getElementById('lightboxNext');

  function openLightbox(index) {
    currentIndex = index;
    lightboxImg.src = galleryImages[index].src;
    lightboxImg.alt = galleryImages[index].alt;
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox.classList.remove('open');
    document.body.style.overflow = '';
    lightboxImg.src = '';
  }

  function showPrev() {
    currentIndex = (currentIndex - 1 + galleryImages.length) % galleryImages.length;
    lightboxImg.src = galleryImages[currentIndex].src;
  }

  function showNext() {
    currentIndex = (currentIndex + 1) % galleryImages.length;
    lightboxImg.src = galleryImages[currentIndex].src;
  }

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightboxPrev)  lightboxPrev.addEventListener('click', showPrev);
  if (lightboxNext)  lightboxNext.addEventListener('click', showNext);
  if (lightbox) {
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) closeLightbox();
    });
  }

  document.addEventListener('keydown', (e) => {
    if (!lightbox || !lightbox.classList.contains('open')) return;
    if (e.key === 'Escape')     closeLightbox();
    if (e.key === 'ArrowLeft')  showPrev();
    if (e.key === 'ArrowRight') showNext();
  });

  /* ── Navbar scroll effect ── */
  const navbar = document.getElementById('navbar');
  function handleScroll() {
    if (navbar) {
      navbar.classList.toggle('scrolled', window.scrollY > 60);
    }
  }
  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  /* ── Mobile menu ── */
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
    });
    mobileMenu.querySelectorAll('.mobile-link').forEach(link => {
      link.addEventListener('click', () => mobileMenu.classList.remove('open'));
    });
  }

  /* ── Language Toggle (homepage only — service pages use service.js) ── */
  const langToggle = document.getElementById('langToggle');
  const html = document.documentElement;
  const isServicePage = !!document.querySelector('.service-hero');

  if (langToggle && !isServicePage) {
    langToggle.addEventListener('click', () => {
      const isAr = html.getAttribute('data-lang') === 'ar';
      html.setAttribute('data-lang', isAr ? 'en' : 'ar');
      html.setAttribute('lang', isAr ? 'en' : 'ar');
      html.setAttribute('dir', isAr ? 'ltr' : 'rtl');
      langToggle.textContent = isAr ? 'AR' : 'EN';
      localStorage.setItem('lang', isAr ? 'en' : 'ar');
    });

    // Restore saved language
    const saved = localStorage.getItem('lang');
    if (saved && saved !== 'ar') {
      html.setAttribute('data-lang', 'en');
      html.setAttribute('lang', 'en');
      html.setAttribute('dir', 'ltr');
      langToggle.textContent = 'AR';
    }
  }

  /* ── Services Tabs ── */
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const tab = btn.dataset.tab;
      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));
      btn.classList.add('active');
      const target = document.getElementById(`tab-${tab}`);
      if (target) target.classList.add('active');
    });
  });

  /* ── Smooth scroll for anchor links ── */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', (e) => {
      const href = a.getAttribute('href');
      if (href === '#') return;
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* ── Intersection Observer (reveal animations) ── */
  const revealEls = document.querySelectorAll('.reveal, .philosophy-item, .service-card, .contact-card');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(el => {
      el.classList.add('reveal');
      observer.observe(el);
    });
  } else {
    revealEls.forEach(el => el.classList.add('visible'));
  }

  /* ── About section — swap placeholder on portrait upload ── */
  // When you add a portrait photo as assets/doctor.jpg or assets/doctor.jpeg,
  // this code will automatically use it instead of the placeholder logo
  const placeholder = document.querySelector('.about-img-placeholder');
  if (placeholder) {
    const tryImg = new Image();
    tryImg.onload = () => {
      placeholder.innerHTML = `<img src="${tryImg.src}" alt="Dr. Ahmed Mazen" style="width:100%;border-radius:12px;" />`;
    };
    tryImg.src = 'assets/doctor.jpg';

    const tryJpeg = new Image();
    tryJpeg.onload = () => {
      placeholder.innerHTML = `<img src="${tryJpeg.src}" alt="Dr. Ahmed Mazen" style="width:100%;border-radius:12px;" />`;
    };
    tryJpeg.src = 'assets/doctor.jpeg';
  }

  /* ── WhatsApp float position in LTR ── */
  // handled via CSS data-lang attribute

});
