# Copilot Instructions — Dr. Ahmed Mazen Website

## Project Overview
Bilingual (Arabic RTL / English LTR) website for Dr. Ahmed Mazen, an Egyptian aesthetic medicine consultant. Non-surgical cosmetic treatments only. Luxury black & gold brand.

## Always read CLAUDE.md first
The full project brief, design system, services list, SEO strategy, coding conventions, and TODO list are in `/CLAUDE.md`. Load it before generating any code for this project.

## Quick Rules

**Colors — never hardcode, always use CSS variables:**
- Background: `var(--black)` = `#0A0A0A`
- Gold accent: `var(--gold)` = `#C9A84C`
- Text: `var(--off-white)` = `#F5F0E8`

**Bilingual text — every visible string needs both:**
```html
<span class="ar-text">النص العربي</span>
<span class="en-text">English text</span>
```

**Primary CTA is always WhatsApp:**
```html
<a href="https://wa.me/201274477111" target="_blank" rel="noopener">...</a>
```

**No frameworks — vanilla HTML/CSS/JS only.**

**Arabic is the primary language (RTL). English is secondary (LTR toggle).**

## Key Files
- `index.html` — homepage, complete
- `css/style.css` — full design system, complete
- `js/main.js` — all interactivity, complete
- `assets/logo.jpeg` — brand logo (gold on black)
- `assets/before-after/result-01.jpg` … `result-21.jpg` — patient images

## Next Tasks (priority order)
1. Create individual service pages in `/services/[slug]/index.html`
2. Create Arabic SEO blog articles in `/blog/[slug]/index.html`
3. Add Google Analytics snippet to all pages
4. Convert images to WebP format

See `CLAUDE.md` for complete service list with Arabic names, slugs, and page template structure.
