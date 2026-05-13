# Dr. Ahmed Mazen — Website Project

## Who is the client?
Dr. Ahmed Mazen is one of Egypt's top aesthetic medicine specialists. He does **non-surgical only** cosmetic treatments — fillers, Botox, body contouring. No surgery, no anesthesia, immediate results. Patients come from Egypt, the Gulf, and North Africa.

**Credentials:**
- Ain Shams University (Cairo)
- Member, American Society of Aesthetic Medicine
- Member, Afro-Asian Society of Aesthetic Medicine
- Featured in Al-Gomhuria and Al-Masry Al-Youm newspapers

**Core philosophy (use in all copy):**
> الحفاظ على الملامح الطبيعية وتعبيرات الوجه — بدون تدخل جراحي — تجنب مخاطر التخدير — النتيجة فورية
> Preserve natural features and facial expressions — no surgery — no anesthesia risk — immediate results

---

## Design System

### Colors (strict — never deviate)
```css
--black:      #0A0A0A   /* primary background */
--dark:       #111111
--dark-2:     #1A1A1A   /* section alternates */
--dark-3:     #222222   /* card backgrounds */
--gold:       #C9A84C   /* primary accent, CTAs, icons */
--gold-light: #E8C97A   /* hover states */
--gold-dim:   #8A6F2E   /* borders, subtle accents */
--off-white:  #F5F0E8   /* body text */
--gray:       #888888   /* secondary text */
--gray-light: #BBBBBB   /* descriptions */
```

### Fonts (loaded via Google Fonts in index.html)
- **Arabic headings:** Cairo, font-weight 700
- **English headings:** Playfair Display, serif
- **Body (both):** Cairo (AR) / Montserrat (EN)
- **Always** use `html[data-lang="ar"]` and `html[data-lang="en"]` selectors for bilingual styles

### Language / Directionality
- Default: Arabic RTL (`dir="rtl"`, `lang="ar"`)
- Toggle: user switches to English LTR via `#langToggle` button
- Every piece of text needs BOTH:
  ```html
  <span class="ar-text">النص العربي</span>
  <span class="en-text">English text</span>
  ```
- CSS hides the inactive language:
  ```css
  html[data-lang="ar"] .en-text { display: none; }
  html[data-lang="en"] .ar-text { display: none; }
  ```

---

## File Structure
```
/
├── index.html              ← Main homepage (complete)
├── css/style.css           ← All styles (complete)
├── js/main.js              ← Gallery, tabs, lightbox, lang toggle (complete)
├── assets/
│   ├── logo.jpeg           ← Gold "AM" monogram on black background
│   ├── doctor.jpg          ← PLACEHOLDER — add Dr. Ahmed's portrait here
│   └── before-after/
│       └── result-01.jpg … result-21.jpg  ← All patient before/after images
├── images/                 ← Original source images (keep, don't delete)
├── blog/                   ← TODO: Arabic SEO blog articles
│   └── index.html          ← Blog listing page
├── services/               ← TODO: Individual service pages
│   ├── filler-wajh.html
│   ├── botox.html
│   └── ...
└── CLAUDE.md               ← This file
```

---

## Services (complete list — use exact Arabic/English)

### Face Fillers (فيلر الوجه)
| Arabic | English | Slug |
|---|---|---|
| فيلر شد الوجه | Face Lift Filler | filler-shad-alwajh |
| جولاين الفك | Jawline Filler | jawline |
| كونتور الخدود | Cheek Contouring | kontur-alkhdud |
| فيلر الصدغين | Temple Filler | filler-alsadghein |
| فيلر الشفايف | Lip Filler | filler-alshfayef |
| فيلر الأنف | Non-Surgical Rhinoplasty | filler-alanf |
| رفع الترهل | Sagging Skin Lift | raf-altarahal |
| نضارة البشرة | Skin Glow Treatment | nadara |

### Botox (بوتكس)
| Arabic | English | Slug |
|---|---|---|
| بوتكس الجبهة | Forehead Botox | botox-jabha |
| بوتكس الجز والصداع | Bruxism & Headache Botox | botox-soda3 |
| بوتكس الرقبة | Neck Botox | botox-ragaba |
| بوتكس الأنف | Nose Botox | botox-anf |
| بوتكس التعرق | Hyperhidrosis Botox | botox-ta3arroq |
| بوتكس فقرات الظهر | Back Botox | botox-dahr |

### Body Fillers (فيلر الجسم)
| Arabic | English | Slug |
|---|---|---|
| فيلر الأيدي | Hand Filler | filler-aydi |
| فيلر الأرداف | Buttocks Filler | filler-ardaf |
| فيلر الرجلين | Leg Filler | filler-reglen |
| فيلر الجسم | Body Filler | filler-gesm |

---

## Contact & Social
- **WhatsApp / Phone 1:** +201274477111
- **Phone 2:** +201200066601
- **WhatsApp link:** `https://wa.me/201274477111`
- **Location map:** `https://maps.app.goo.gl/wDUqDdbH6VUvGsd98`
- **Facebook:** https://www.facebook.com/drahmedmazen.1
- **Instagram:** https://www.instagram.com/drahmedmazen
- **TikTok:** https://vm.tiktok.com/ZS9F9Q1wosPrP-Talxs/
- **YouTube:** https://youtube.com/@ahmedmazen1

---

## SEO Strategy

### Target keywords (primary — Arabic)
- دكتور تجميل مصر
- دكتور أحمد مازن
- فيلر الوجه في مصر
- بوتكس في مصر
- شد الوجه بدون جراحة
- حقن الفيلر القاهرة
- طب التجميل غير جراحي

### Target keywords (secondary — English)
- aesthetic medicine egypt
- non surgical facelift cairo
- filler botox egypt
- dr ahmed mazen

### Rules for every page:
1. `<title>` format: `[Service Name] | دكتور أحمد مازن | Dr. Ahmed Mazen`
2. `<meta name="description">` must be 150-160 chars, include Arabic keyword
3. Every page needs Schema.org JSON-LD (Physician + MedicalProcedure for service pages)
4. Every service page URL format: `/services/[slug]/` (e.g., `/services/filler-shad-alwajh/`)
5. Internal links: every service page links back to homepage + related services

### Blog article titles (high-priority — write these first)
- "أفضل دكتور فيلر في مصر" → targets main search term
- "فيلر الوجه: كل ما تحتاج معرفته" → informational
- "الفرق بين الفيلر والبوتكس" → FAQ content
- "شد الوجه بدون جراحة — هل هو آمن؟" → trust-building
- "نتائج فيلر الشفايف — تجارب حقيقية" → social proof

---

## Competitor References

### Epione Beverly Hills (epionebh.com) — International luxury standard
- Structure: Hero → Philosophy → Services (mega-menu by body area) → Before/After → Reviews → CTA
- Key lesson: Organize services by body zone, not just a flat list
- Key lesson: Celebrity/social proof section converts well

### Dr. Emad Farag (dr-emadfarag.com) — Egyptian market benchmark
- Structure: WordPress, Arabic RTL, services dropdown, before/after, videos, blog
- Key lesson: WhatsApp is the primary booking CTA in Egypt
- Key lesson: 94 pages of Arabic SEO blog content = strong organic traffic
- Key lesson: Each service has its own dedicated page with keyword in URL

---

## Coding Conventions

### HTML
- Always include both `.ar-text` and `.en-text` spans for every visible string
- Section pattern: `<section class="[name]" id="[name]">`
- Use `loading="lazy"` on all images below the fold
- All external links: `target="_blank" rel="noopener"`

### CSS
- Use CSS variables for ALL colors — never hardcode hex values
- Mobile-first: base styles for mobile, `@media (min-width: 768px)` for desktop
- Hover animations: always use `transform: translateY(-4px)` + box-shadow
- Gold glow: `box-shadow: 0 0 30px rgba(201,168,76,0.15)`
- Transitions: always `0.3s ease`

### JavaScript
- No frameworks — vanilla JS only (the site is already framework-free)
- Use IntersectionObserver for reveal animations (already set up in main.js)
- Preserve language toggle logic — it uses `localStorage.setItem('lang', ...)`

### New service page template
Each service page should follow this structure:
1. Same navbar as index.html
2. Hero: service name + tagline (AR/EN)
3. What is it? section (description)
4. How it works (steps)
5. Before/After section (show relevant images from assets/before-after/)
6. FAQ section (good for SEO)
7. CTA: WhatsApp booking
8. Related services grid
9. Same footer as index.html

---

## What's Done ✅
- [x] Homepage (index.html) — all sections complete
- [x] CSS design system (css/style.css)
- [x] JavaScript: gallery, lightbox, tabs, language toggle, scroll effects (js/main.js)
- [x] 21 before/after images normalized and ready
- [x] Logo asset
- [x] Git repo initialized and pushed to GitHub
- [x] `/services/` — 18 individual service pages generated (generate_pages.py)
- [x] Homepage service cards linked to service pages
- [x] CSS for generated service pages (css/service.css extended)
- [x] service.js FAQ accordion supports both .faq-question and .faq-q selectors

## What's TODO 🔲
- [ ] Add `assets/doctor.jpg` — portrait photo (JS auto-detects it)
- [ ] `/blog/` — Arabic SEO blog articles (5 high-priority titles in CLAUDE.md)
- [ ] Update canonical URL in `<head>` when real domain is confirmed
- [ ] Add Google Analytics / Google Tag Manager
- [ ] Add Google Maps embed in contact section
- [ ] Connect a booking/inquiry form (or Calendly embed)
- [ ] Add patient video testimonials section (YouTube embeds)
- [ ] Performance: convert JPEGs to WebP for faster load
