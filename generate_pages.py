#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dr. Ahmed Mazen — Static Site Generator
Generates all service pages and blog pages
"""

import os, json

BASE = os.path.dirname(os.path.abspath(__file__))

# ──────────────────────────────────────────────────────
# SHARED NAV HTML (same across all pages)
# ──────────────────────────────────────────────────────
def navbar(root="../.."):
    return f"""  <nav class="navbar" id="navbar">
    <div class="nav-inner">
      <a href="{root}/index.html" class="nav-logo">
        <img src="{root}/assets/logo.jpeg" alt="Dr. Ahmed Mazen Logo" />
      </a>
      <div class="nav-right">
        <button class="lang-toggle" id="langToggle" aria-label="Switch Language">EN</button>
        <a href="https://wa.me/201274477111" target="_blank" rel="noopener" class="btn btn-gold nav-cta">
          <span class="ar-text">احجز موعدك</span>
          <span class="en-text">Book Now</span>
        </a>
        <button class="hamburger" id="hamburger" aria-label="Menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <div class="mobile-menu" id="mobileMenu">
      <a href="{root}/index.html" class="mobile-link"><span class="ar-text">الرئيسية</span><span class="en-text">Home</span></a>
      <a href="{root}/index.html#services" class="mobile-link"><span class="ar-text">الخدمات</span><span class="en-text">Services</span></a>
      <a href="{root}/index.html#results" class="mobile-link"><span class="ar-text">نتائجنا</span><span class="en-text">Results</span></a>
      <a href="{root}/index.html#about" class="mobile-link"><span class="ar-text">عن الدكتور</span><span class="en-text">About</span></a>
      <a href="{root}/index.html#contact" class="mobile-link"><span class="ar-text">تواصل معنا</span><span class="en-text">Contact</span></a>
    </div>
  </nav>"""

def footer(root="../.."):
    return f"""  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="{root}/assets/logo.jpeg" alt="Dr. Ahmed Mazen" class="footer-logo" />
          <p>
            <span class="ar-text">جمالك الطبيعي بلا جراحة</span>
            <span class="en-text">Your Natural Beauty, No Surgery</span>
          </p>
        </div>
        <div class="footer-links">
          <h4><span class="ar-text">روابط سريعة</span><span class="en-text">Quick Links</span></h4>
          <a href="{root}/index.html#services"><span class="ar-text">الخدمات</span><span class="en-text">Services</span></a>
          <a href="{root}/index.html#results"><span class="ar-text">نتائجنا</span><span class="en-text">Results</span></a>
          <a href="{root}/index.html#about"><span class="ar-text">عن الدكتور</span><span class="en-text">About</span></a>
          <a href="{root}/index.html#contact"><span class="ar-text">تواصل معنا</span><span class="en-text">Contact</span></a>
        </div>
        <div class="footer-social">
          <h4><span class="ar-text">تابعنا</span><span class="en-text">Follow Us</span></h4>
          <div class="social-icons">
            <a href="https://www.facebook.com/drahmedmazen.1" target="_blank" rel="noopener" aria-label="Facebook">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
            </a>
            <a href="https://www.instagram.com/drahmedmazen" target="_blank" rel="noopener" aria-label="Instagram">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
            </a>
            <a href="https://vm.tiktok.com/ZS9F9Q1wosPrP-Talxs/" target="_blank" rel="noopener" aria-label="TikTok">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>
            </a>
            <a href="https://youtube.com/@ahmedmazen1" target="_blank" rel="noopener" aria-label="YouTube">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
            </a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>
          <span class="ar-text">© 2025 دكتور أحمد مازن. جميع الحقوق محفوظة.</span>
          <span class="en-text">© 2025 Dr. Ahmed Mazen. All rights reserved.</span>
        </p>
      </div>
    </div>
  </footer>
  <a href="https://wa.me/201274477111" target="_blank" rel="noopener" class="whatsapp-float" aria-label="Book on WhatsApp">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
  </a>"""

# ──────────────────────────────────────────────────────
# SERVICE DATA
# ──────────────────────────────────────────────────────
SERVICES = [
  {
    "slug": "filler-shad-alwajh",
    "ar_name": "فيلر شد الوجه",
    "en_name": "Face Lift Filler",
    "ar_tagline": "شباب ونضارة فورية — بدون جراحة ولا تعافٍ",
    "en_tagline": "Instant Youth & Radiance — No Surgery, No Downtime",
    "keyword": "فيلر شد الوجه",
    "meta_ar": "فيلر شد الوجه مع دكتور أحمد مازن في مصر — نتائج فورية وطبيعية بدون جراحة أو تخدير. احجز موعدك الآن.",
    "ar_desc": "فيلر شد الوجه هو أحد أبرز تقنيات طب التجميل الحديثة التي تتيح رفع ملامح الوجه وإعادة شبابه دون اللجوء إلى الجراحة. يعتمد الدكتور أحمد مازن على حقن الهيالورونيك أسيد بدقة في المناطق المستهدفة لاستعادة الحجم الطبيعي، وشد الترهل، وإعادة التناسق لملامح الوجه. النتيجة فورية وطبيعية تمامًا تدوم من 12 إلى 18 شهرًا.",
    "en_desc": "Face Lift Filler is one of the most advanced non-surgical rejuvenation techniques available today. Dr. Ahmed Mazen precisely injects hyaluronic acid into targeted areas to restore natural volume, lift sagging skin, and rebalance facial proportions. Results are immediate, completely natural-looking, and last 12–18 months.",
    "steps": [
      {"ar": "استشارة شخصية لتقييم الوجه وتحديد المناطق المحتاجة للعلاج", "en": "Personal consultation to assess the face and identify target areas"},
      {"ar": "تطبيق كريم تخدير موضعي لضمان أقصى راحة", "en": "Application of topical anesthetic cream for maximum comfort"},
      {"ar": "حقن دقيق للفيلر في المناطق المستهدفة بتقنية متخصصة", "en": "Precise filler injection into target areas using specialized technique"},
      {"ar": "مراجعة النتائج الفورية والخروج بوجه مشدود ومنتعش", "en": "Review of immediate results — leave with a lifted, refreshed face"},
    ],
    "faqs": [
      {"q_ar": "كم تدوم نتيجة فيلر شد الوجه؟", "q_en": "How long do Face Lift Filler results last?",
       "a_ar": "تدوم النتائج عادةً من 12 إلى 18 شهرًا حسب نوع الفيلر المستخدم وطبيعة الجلد.", "a_en": "Results typically last 12–18 months depending on the filler type and skin characteristics."},
      {"q_ar": "هل العملية مؤلمة؟", "q_en": "Is the procedure painful?",
       "a_ar": "لا. يُستخدم كريم تخدير موضعي قبل الجلسة، وقد يشعر المريض بضغط خفيف فقط.", "a_en": "No. A topical anesthetic is applied beforehand. Patients typically feel only slight pressure."},
      {"q_ar": "هل أحتاج إلى فترة نقاهة؟", "q_en": "Is there recovery time needed?",
       "a_ar": "لا. يمكنك مغادرة العيادة ومواصلة يومك الطبيعي مباشرة بعد الجلسة.", "a_en": "No. You can leave the clinic and continue your normal day immediately after the session."},
    ],
    "images": ["result-02.jpg", "result-03.jpg", "result-10.jpg"],
    "related": ["jawline", "kontur-alkhdud", "raf-altarahal"],
    "category": "face",
  },
  {
    "slug": "jawline",
    "ar_name": "جولاين الفك",
    "en_name": "Jawline Filler",
    "ar_tagline": "تحديد خط الفك وإبراز الملامح بدقة فائقة",
    "en_tagline": "Define & Sharpen Your Jawline with Precision",
    "keyword": "جولاين الفك",
    "meta_ar": "جولاين الفك مع دكتور أحمد مازن — تحديد وتجميل خط الفك بدون جراحة. نتائج فورية وطبيعية في القاهرة.",
    "ar_desc": "يُعدّ تحديد الفك (الجولاين) من أكثر إجراءات تجميل الوجه طلبًا لدى الرجال والنساء على حدٍّ سواء. يقوم الدكتور أحمد مازن بحقن فيلر متخصص على طول خط الفك لمنحه تعريفًا وحدةً أكثر، مع إزالة الترهل تحت الذقن وتحسين التناسق العام للوجه. الإجراء سريع، بدون جراحة، والنتيجة فورية.",
    "en_desc": "Jawline definition is one of the most sought-after facial aesthetic procedures for both men and women. Dr. Ahmed Mazen injects specialized filler along the jawline to create sharper definition, reduce jowling, and improve overall facial harmony. Quick, non-surgical, with immediate results.",
    "steps": [
      {"ar": "تحليل خط الفك وتحديد نقاط الحقن المثلى", "en": "Analysis of the jawline and mapping optimal injection points"},
      {"ar": "تخدير موضعي للراحة التامة خلال الجلسة", "en": "Topical anesthesia for complete comfort during the session"},
      {"ar": "حقن الفيلر بدقة على طول خط الفك", "en": "Precise filler injection along the jawline"},
      {"ar": "مراجعة النتيجة الفورية وتعديل دقيق إذا لزم", "en": "Review of immediate result with fine-tuning if needed"},
    ],
    "faqs": [
      {"q_ar": "من يستفيد من حقن الجولاين؟", "q_en": "Who benefits from Jawline Filler?",
       "a_ar": "كل من يعاني من ترهل الفك أو ضعف تحديده أو عدم التناسق، سواء للرجال أو النساء.", "a_en": "Anyone experiencing a soft or undefined jawline, jowling, or asymmetry — suitable for both men and women."},
      {"q_ar": "هل النتيجة طبيعية المظهر؟", "q_en": "Are the results natural-looking?",
       "a_ar": "نعم. فلسفة الدكتور أحمد مازن تقوم على إبراز الجمال الطبيعي بدون مبالغة.", "a_en": "Yes. Dr. Ahmed Mazen's philosophy is to enhance natural beauty without exaggeration."},
      {"q_ar": "كم مدة الجلسة؟", "q_en": "How long does the session take?",
       "a_ar": "تستغرق الجلسة عادةً بين 30 و45 دقيقة فقط.", "a_en": "The session typically takes between 30 and 45 minutes."},
    ],
    "images": ["result-03.jpg", "result-05.jpg", "result-16.jpg"],
    "related": ["filler-shad-alwajh", "kontur-alkhdud", "filler-alsadghein"],
    "category": "face",
  },
  {
    "slug": "kontur-alkhdud",
    "ar_name": "كونتور الخدود",
    "en_name": "Cheek Contouring",
    "ar_tagline": "امتلاء طبيعي وتوازن مثالي لملامح وجهك",
    "en_tagline": "Natural Volume & Perfect Balance for Your Face",
    "keyword": "كونتور الخدود",
    "meta_ar": "كونتور الخدود بالفيلر مع دكتور أحمد مازن — امتلاء طبيعي وتناسق مثالي بدون جراحة. احجز في القاهرة.",
    "ar_desc": "تُمثّل الخدود الممتلئة والمرتفعة علامةً على الشباب والصحة. مع مرور الوقت، تفقد الخدود حجمها الطبيعي مما يجعل الوجه يبدو مسنًّا أو متعبًا. يستعيد الدكتور أحمد مازن هذا الحجم من خلال حقن دقيقة للفيلر في المنطقة الوجنية، مما يمنح الوجه انتعاشًا وتوازنًا طبيعيًا تمامًا.",
    "en_desc": "Full, lifted cheeks are a hallmark of youth and vitality. Over time, cheeks lose their natural volume making the face appear tired or aged. Dr. Ahmed Mazen restores this volume through precise filler injections in the zygomatic area, giving the face natural-looking freshness and balance.",
    "steps": [
      {"ar": "تقييم بنية الوجه وتحديد مستوى الحجم المطلوب", "en": "Assessment of facial structure and required volume level"},
      {"ar": "تطبيق مخدر موضعي لضمان الراحة", "en": "Application of topical anesthetic for comfort"},
      {"ar": "حقن الفيلر بدقة في منطقة عظام الخد", "en": "Precise injection of filler into the cheekbone area"},
      {"ar": "تشكيل النتيجة وضبط التناسق", "en": "Shaping the result and adjusting symmetry"},
    ],
    "faqs": [
      {"q_ar": "ما الفرق بين كونتور الخدود وشد الوجه؟", "q_en": "What's the difference between cheek contouring and face lifting?",
       "a_ar": "كونتور الخدود يركز على إعادة الحجم والامتلاء للمنطقة الوجنية، بينما شد الوجه يستهدف رفع الترهل العام.", "a_en": "Cheek contouring focuses on restoring volume to the cheekbone area, while face lifting targets overall sagging."},
      {"q_ar": "هل تبدو الخدود طبيعية بعد الحقن؟", "q_en": "Do the cheeks look natural after injection?",
       "a_ar": "بالتأكيد. الدكتور أحمد مازن يحرص على الامتلاء الطبيعي دون مبالغة.", "a_en": "Absolutely. Dr. Ahmed Mazen ensures natural fullness without exaggeration."},
      {"q_ar": "متى تظهر النتائج؟", "q_en": "When do results appear?",
       "a_ar": "النتائج فورية من اللحظة الأولى وتستمر في التحسن خلال 2-4 أسابيع.", "a_en": "Results are immediate and continue to improve over 2–4 weeks."},
    ],
    "images": ["result-04.jpg", "result-06.jpg", "result-10.jpg"],
    "related": ["filler-shad-alwajh", "jawline", "filler-alsadghein"],
    "category": "face",
  },
  {
    "slug": "filler-alsadghein",
    "ar_name": "فيلر الصدغين",
    "en_name": "Temple Filler",
    "ar_tagline": "استعادة شباب الصدغين لمظهر أكثر نضارة وشبابًا",
    "en_tagline": "Restore Temple Volume for a Youthful Appearance",
    "keyword": "فيلر الصدغين",
    "meta_ar": "فيلر الصدغين مع دكتور أحمد مازن — استعادة الحجم وشباب منطقة الصدغين بدون جراحة في مصر.",
    "ar_desc": "يُعدّ فقدان حجم الصدغين من أولى علامات الشيخوخة التي يغفل عنها كثيرون. الصدغ الغائر يجعل الوجه يبدو هزيلًا ويبرز عظام الجمجمة بشكل غير جمالي. يعالج الدكتور أحمد مازن هذه المنطقة بدقة بالغة لإعادة التناسق الطبيعي للوجه وإخفاء آثار التقدم في السن.",
    "en_desc": "Temple volume loss is one of the earliest signs of aging that many overlook. Hollow temples make the face appear gaunt and accentuate the skull bones unaesthetically. Dr. Ahmed Mazen treats this area with great precision to restore natural facial harmony and conceal signs of aging.",
    "steps": [
      {"ar": "فحص وتقييم منطقة الصدغين", "en": "Examination and assessment of the temple area"},
      {"ar": "تحديد الكمية المثلى من الفيلر لكل صدغ", "en": "Determining the optimal filler volume for each temple"},
      {"ar": "حقن دقيق ومحترف لإعادة الحجم", "en": "Precise professional injection to restore volume"},
      {"ar": "مراجعة التماثل ومظهر الوجه الإجمالي", "en": "Review of symmetry and overall facial appearance"},
    ],
    "faqs": [
      {"q_ar": "لماذا تغور الصدغين مع التقدم بالسن؟", "q_en": "Why do temples hollow with age?",
       "a_ar": "بسبب فقدان الدهون العميقة في هذه المنطقة تدريجيًا مع مرور الوقت.", "a_en": "Due to gradual loss of deep fat in this area over time."},
      {"q_ar": "هل الحقن في منطقة الصدغ آمن؟", "q_en": "Is injection in the temple area safe?",
       "a_ar": "نعم، بيد طبيب متخصص خبير. الدكتور أحمد مازن لديه خبرة واسعة في هذه المنطقة الحساسة.", "a_en": "Yes, in the hands of an experienced specialist. Dr. Ahmed Mazen has extensive expertise in this sensitive area."},
      {"q_ar": "كم تدوم النتائج؟", "q_en": "How long do results last?",
       "a_ar": "من 12 إلى 24 شهرًا حسب نوع الفيلر المستخدم.", "a_en": "12–24 months depending on the filler type used."},
    ],
    "images": ["result-07.jpg", "result-09.jpg"],
    "related": ["filler-shad-alwajh", "kontur-alkhdud", "nadara"],
    "category": "face",
  },
  {
    "slug": "filler-alshfayef",
    "ar_name": "فيلر الشفايف",
    "en_name": "Lip Filler",
    "ar_tagline": "شفاه ممتلئة وطبيعية — بلمسة فنية دقيقة",
    "en_tagline": "Fuller, Natural Lips — With an Artistic Precise Touch",
    "keyword": "فيلر الشفايف",
    "meta_ar": "فيلر الشفايف مع دكتور أحمد مازن في مصر — تجميل الشفاه بشكل طبيعي وبدون مبالغة. نتائج فورية.",
    "ar_desc": "فيلر الشفايف من أكثر إجراءات التجميل شيوعًا وطلبًا. فلسفة الدكتور أحمد مازن في هذا الإجراء قائمة على إبراز جمال الشفاه الطبيعي دون المبالغة أو التشوه. يستخدم فيلر هيالورونيك أسيد عالي الجودة لمنح الشفاه امتلاءً ونضارةً طبيعيًا يناسب ملامح كل مريضة.",
    "en_desc": "Lip filler is one of the most popular cosmetic procedures today. Dr. Ahmed Mazen's philosophy is to enhance the natural beauty of the lips without exaggeration or distortion. He uses premium hyaluronic acid filler to give lips a natural fullness and freshness that suits each patient's unique features.",
    "steps": [
      {"ar": "تحليل شكل الشفاه وتحديد النتيجة المرغوبة", "en": "Analysis of lip shape and determining desired outcome"},
      {"ar": "تطبيق كريم تخدير موضعي أو حقن تخدير محلي", "en": "Application of topical or local anesthetic"},
      {"ar": "حقن الفيلر بدقة فائقة في مناطق مختارة", "en": "Highly precise filler injection into selected areas"},
      {"ar": "تشكيل وضبط التناسق للحصول على النتيجة المثالية", "en": "Shaping and symmetry adjustment for the ideal result"},
    ],
    "faqs": [
      {"q_ar": "هل يبدو فيلر الشفايف طبيعيًا؟", "q_en": "Does lip filler look natural?",
       "a_ar": "نعم عند الطبيب المناسب. الدكتور أحمد مازن يتفادى تمامًا الشكل المبالغ فيه.", "a_en": "Yes, with the right doctor. Dr. Ahmed Mazen completely avoids the overfilled look."},
      {"q_ar": "هل الألم شديد؟", "q_en": "Is there significant pain?",
       "a_ar": "منطقة الشفاه حساسة لكن مع التخدير الموضعي تكون التجربة مريحة جدًا.", "a_en": "The lip area is sensitive but with topical anesthetic the experience is very comfortable."},
      {"q_ar": "هل يمكن إزالة الفيلر إذا أردت؟", "q_en": "Can the filler be dissolved if I want?",
       "a_ar": "نعم. فيلر الهيالورونيك أسيد قابل للإذابة الكاملة باستخدام الهيالورونيداز عند الحاجة.", "a_en": "Yes. Hyaluronic acid filler can be fully dissolved using hyaluronidase if needed."},
    ],
    "images": ["result-01.jpg", "result-17.jpg", "result-18.jpg", "result-19.jpg"],
    "related": ["filler-shad-alwajh", "filler-alanf", "kontur-alkhdud"],
    "category": "face",
  },
  {
    "slug": "filler-alanf",
    "ar_name": "فيلر الأنف",
    "en_name": "Non-Surgical Rhinoplasty",
    "ar_tagline": "تجميل الأنف بدون جراحة لحالات مختارة",
    "en_tagline": "Reshape Your Nose Without Surgery — For Select Cases",
    "keyword": "فيلر الأنف بدون جراحة",
    "meta_ar": "فيلر الأنف وتجميل الأنف بدون جراحة مع دكتور أحمد مازن في مصر — لحالات مختارة. نتائج فورية.",
    "ar_desc": "فيلر الأنف (رينوبلاستي غير جراحي) يُتيح تعديل شكل الأنف وإخفاء بعض العيوب البسيطة بدون أي جراحة أو تخدير عام. يستخدم الدكتور أحمد مازن هذه التقنية لحالات مختارة بعناية، مثل تعديل زاوية الطرف أو تنعيم انحناء الظهر أو رفع طرف الأنف. الإجراء دقيق للغاية ويتطلب خبرة عالية.",
    "en_desc": "Non-Surgical Rhinoplasty allows reshaping of the nose and correcting minor imperfections without any surgery or general anesthesia. Dr. Ahmed Mazen applies this technique to carefully selected cases — such as adjusting the tip angle, smoothing a dorsal hump, or lifting the tip. The procedure is highly precise and requires great expertise.",
    "steps": [
      {"ar": "تقييم دقيق للحالة لتحديد مدى الاستفادة من الفيلر", "en": "Precise case assessment to determine suitability for filler"},
      {"ar": "تخدير موضعي للمنطقة المستهدفة", "en": "Topical anesthesia of the target area"},
      {"ar": "حقن دقيق جدًا في النقاط المحددة", "en": "Very precise injection at the mapped points"},
      {"ar": "مراجعة النتيجة من زوايا مختلفة", "en": "Review of results from multiple angles"},
    ],
    "faqs": [
      {"q_ar": "هل كل الحالات مناسبة لفيلر الأنف؟", "q_en": "Is every case suitable for nose filler?",
       "a_ar": "لا. الدكتور أحمد مازن يقبل حالات مختارة فقط حيث يمكن تحقيق نتيجة جمالية حقيقية.", "a_en": "No. Dr. Ahmed Mazen accepts only select cases where a genuine aesthetic result can be achieved."},
      {"q_ar": "هل يمكن تكرار الإجراء؟", "q_en": "Can the procedure be repeated?",
       "a_ar": "نعم بعد امتصاص الفيلر السابق أو تقليله عند الحاجة.", "a_en": "Yes, after the previous filler is absorbed or reduced as needed."},
      {"q_ar": "هل النتائج دائمة؟", "q_en": "Are results permanent?",
       "a_ar": "لا، الفيلر مؤقت ويدوم من 9 إلى 18 شهرًا.", "a_en": "No, filler is temporary and lasts 9–18 months."},
    ],
    "images": ["result-08.jpg", "result-11.jpg"],
    "related": ["filler-shad-alwajh", "botox-anf", "jawline"],
    "category": "face",
  },
  {
    "slug": "raf-altarahal",
    "ar_name": "رفع الترهل",
    "en_name": "Sagging Skin Lift",
    "ar_tagline": "شد الترهل وإعادة التوتر لبشرتك بدون جراحة",
    "en_tagline": "Lift Sagging Skin & Restore Firmness Without Surgery",
    "keyword": "رفع ترهل الوجه بدون جراحة",
    "meta_ar": "رفع الترهل وشد الوجه بدون جراحة مع دكتور أحمد مازن — نتائج فورية وطبيعية في القاهرة. احجز الآن.",
    "ar_desc": "يُعدّ ترهل الجلد من أبرز علامات التقدم في السن. يقدم الدكتور أحمد مازن تقنيات متطورة لرفع الترهل بدون جراحة، من خلال حقن الفيلر في المناطق الداعمة لهيكل الوجه لإعادة الشد الطبيعي وتحسين التوتر الجلدي. النتيجة وجه أكثر شبابًا ونضارةً دون أي تدخل جراحي.",
    "en_desc": "Skin sagging is one of the most prominent signs of aging. Dr. Ahmed Mazen offers advanced non-surgical lifting techniques, injecting filler into supportive facial structure areas to restore natural firmness and improve skin tension. The result is a younger, fresher face without any surgical intervention.",
    "steps": [
      {"ar": "تقييم شامل لدرجة الترهل وتحديد المناطق المحتاجة", "en": "Comprehensive evaluation of sagging degree and target areas"},
      {"ar": "تخدير موضعي للراحة التامة", "en": "Topical anesthesia for complete comfort"},
      {"ar": "حقن استراتيجي للفيلر في نقاط الدعم الهيكلي", "en": "Strategic filler injection at structural support points"},
      {"ar": "تقييم النتيجة وضبط الشد", "en": "Result evaluation and tension adjustment"},
    ],
    "faqs": [
      {"q_ar": "ما مدى فاعلية رفع الترهل بالفيلر؟", "q_en": "How effective is lifting sagging skin with filler?",
       "a_ar": "فعّال جدًا في الحالات المتوسطة. للحالات الشديدة قد يُقترح خيارات إضافية.", "a_en": "Very effective in moderate cases. For severe cases, additional options may be suggested."},
      {"q_ar": "هل تحتاج نتائجه إلى صيانة؟", "q_en": "Does the result require maintenance?",
       "a_ar": "نعم، جلسة صيانة كل 12-18 شهرًا للحفاظ على النتيجة.", "a_en": "Yes, a maintenance session every 12–18 months to preserve results."},
      {"q_ar": "ما الفرق بين رفع الترهل وشد الوجه الجراحي؟", "q_en": "What's the difference from surgical facelift?",
       "a_ar": "لا جراحة ولا تعافٍ ولا مخاطر تخدير. النتيجة أكثر طبيعية وتناسب الحالات غير الشديدة.", "a_en": "No surgery, no recovery, no anesthesia risk. Results are more natural and suit non-severe cases."},
    ],
    "images": ["result-09.jpg", "result-10.jpg", "result-12.jpg"],
    "related": ["filler-shad-alwajh", "kontur-alkhdud", "botox-jabha"],
    "category": "face",
  },
  {
    "slug": "nadara",
    "ar_name": "نضارة البشرة",
    "en_name": "Skin Glow Treatment",
    "ar_tagline": "إشراقة وحيوية فورية لبشرتك",
    "en_tagline": "Instant Radiance & Vitality for Your Skin",
    "keyword": "حقن نضارة البشرة",
    "meta_ar": "حقن نضارة البشرة مع دكتور أحمد مازن في القاهرة — بشرة مشرقة وحيوية من أول جلسة. احجز الآن.",
    "ar_desc": "حقن نضارة البشرة (Skin Boosters) هي إجراء تجميلي غير جراحي يُعيد الترطيب العميق والإشراقة لبشرتك. يستخدم الدكتور أحمد مازن تركيبات متخصصة من الهيالورونيك أسيد والفيتامينات والمعادن لإعادة الحيوية للبشرة المتعبة أو الجافة أو الباهتة، مع تحسين ملمسها وتوحيد لونها.",
    "en_desc": "Skin Boosters are a non-surgical cosmetic procedure that restores deep hydration and radiance to your skin. Dr. Ahmed Mazen uses specialized formulations of hyaluronic acid, vitamins, and minerals to revitalize tired, dry, or dull skin, improving texture and evening skin tone.",
    "steps": [
      {"ar": "تقييم نوع البشرة واحتياجاتها", "en": "Assessment of skin type and its specific needs"},
      {"ar": "تنظيف البشرة وتطبيق التخدير الموضعي", "en": "Skin cleansing and topical anesthetic application"},
      {"ar": "حقن دقيق للتركيبة المختارة في طبقات الجلد", "en": "Precise injection of the chosen formulation into skin layers"},
      {"ar": "مراجعة النتيجة والإرشادات بعد الجلسة", "en": "Result review and post-session care instructions"},
    ],
    "faqs": [
      {"q_ar": "كم جلسة أحتاج للحصول على نتيجة مثالية؟", "q_en": "How many sessions do I need for optimal results?",
       "a_ar": "عادةً 2-3 جلسات بفاصل 3-4 أسابيع ثم جلسة صيانة كل 6 أشهر.", "a_en": "Usually 2–3 sessions spaced 3–4 weeks apart, then a maintenance session every 6 months."},
      {"q_ar": "هل تناسب جميع أنواع البشرة؟", "q_en": "Is it suitable for all skin types?",
       "a_ar": "نعم، الإجراء مناسب لجميع أنواع البشرة وجميع الأعمار.", "a_en": "Yes, the procedure is suitable for all skin types and ages."},
      {"q_ar": "متى أرى النتيجة؟", "q_en": "When will I see results?",
       "a_ar": "تبدأ الإشراقة في الظهور خلال أيام قليلة وتتحسن باستمرار.", "a_en": "Radiance begins to appear within a few days and continues to improve."},
    ],
    "images": ["result-11.jpg", "result-12.jpg", "result-20.jpg"],
    "related": ["filler-shad-alwajh", "raf-altarahal", "filler-alsadghein"],
    "category": "face",
  },
  # ── BOTOX ──
  {
    "slug": "botox-jabha",
    "ar_name": "بوتكس الجبهة",
    "en_name": "Forehead Botox",
    "ar_tagline": "تنعيم خطوط الجبهة لمظهر أكثر شبابًا",
    "en_tagline": "Smooth Forehead Lines for a More Youthful Look",
    "keyword": "بوتكس الجبهة",
    "meta_ar": "بوتكس الجبهة مع دكتور أحمد مازن في مصر — تنعيم التجاعيد وخطوط الجبهة بنتائج طبيعية وفورية.",
    "ar_desc": "البوتكس هو أكثر الإجراءات التجميلية انتشارًا في العالم لعلاج تجاعيد الجبهة والخطوط التعبيرية. يحقن الدكتور أحمد مازن البوتوكس بكميات دقيقة ومحسوبة في عضلات الجبهة لإرخائها وتنعيم الخطوط الناتجة عنها، مع الحفاظ على تعبيرات الوجه الطبيعية تمامًا.",
    "en_desc": "Botox is the world's most popular cosmetic procedure for treating forehead wrinkles and expression lines. Dr. Ahmed Mazen injects precisely calculated Botox doses into forehead muscles to relax them and smooth the resulting lines, while fully preserving natural facial expressions.",
    "steps": [
      {"ar": "تحليل حركة عضلات الجبهة وتحديد نقاط الحقن", "en": "Analysis of forehead muscle movement and mapping injection points"},
      {"ar": "تنظيف المنطقة وتطبيق مخدر موضعي اختياري", "en": "Area cleansing and optional topical anesthetic"},
      {"ar": "حقن البوتوكس بدقة فائقة في النقاط المحددة", "en": "Highly precise Botox injection at the mapped points"},
      {"ar": "الخروج فوراً ومتابعة النتيجة بعد أسبوعين", "en": "Immediate departure with a follow-up after two weeks"},
    ],
    "faqs": [
      {"q_ar": "متى تظهر نتيجة البوتكس؟", "q_en": "When do Botox results appear?",
       "a_ar": "تبدأ النتيجة في الظهور خلال 3-5 أيام وتصل لذروتها بعد أسبوعين.", "a_en": "Results begin to appear within 3–5 days and reach their peak after two weeks."},
      {"q_ar": "كم تدوم نتيجة البوتكس؟", "q_en": "How long do Botox results last?",
       "a_ar": "عادةً من 3 إلى 6 أشهر، وتطول مع الاستخدام المتكرر.", "a_en": "Usually 3–6 months, lasting longer with repeated treatments."},
      {"q_ar": "هل يُجمّد البوتكس تعبيرات الوجه؟", "q_en": "Does Botox freeze facial expressions?",
       "a_ar": "لا عند الطبيب الخبير. الدكتور أحمد مازن يحرص على الحفاظ على تعبيرية الوجه الطبيعية.", "a_en": "No with an expert doctor. Dr. Ahmed Mazen ensures natural facial expressiveness is preserved."},
    ],
    "images": ["result-13.jpg", "result-15.jpg"],
    "related": ["botox-soda3", "botox-ragaba", "filler-shad-alwajh"],
    "category": "botox",
  },
  {
    "slug": "botox-soda3",
    "ar_name": "بوتكس الجز والصداع",
    "en_name": "Bruxism & Headache Botox",
    "ar_tagline": "علاج صرير الأسنان والصداع المزمن بشكل دائم",
    "en_tagline": "Permanent Relief from Teeth Grinding & Chronic Headaches",
    "keyword": "بوتكس الجز والصداع",
    "meta_ar": "بوتكس لعلاج صرير الأسنان والصداع المزمن مع دكتور أحمد مازن في مصر — نتائج طويلة الأمد.",
    "ar_desc": "صرير الأسنان (Bruxism) والصداع المزمن من المشكلات المزعجة التي تؤثر على جودة الحياة. البوتوكس في عضلة الماضغ (Masseter) يُرخيها ويقلل من قوة الضغط اللاإرادي على الأسنان، مما يُريح الصداع ويحمي الأسنان ويُنحّف مظهر الوجه. حل فعّال جدًا ومجرَّب.",
    "en_desc": "Teeth grinding (Bruxism) and chronic headaches are troublesome conditions that affect quality of life. Botox in the masseter muscle relaxes it and reduces involuntary jaw pressure, relieving headaches, protecting teeth, and slimming the facial appearance. A highly effective and proven solution.",
    "steps": [
      {"ar": "تقييم حجم عضلة الماضغ ودرجة الجز", "en": "Assessment of masseter size and grinding severity"},
      {"ar": "تحديد الجرعة المناسبة لكل حالة", "en": "Determining appropriate dose for each case"},
      {"ar": "حقن البوتوكس في عضلة الماضغ من كلا الجانبين", "en": "Botox injection into the masseter muscle bilaterally"},
      {"ar": "إرشادات ما بعد الجلسة ومتابعة النتائج", "en": "Post-session instructions and result follow-up"},
    ],
    "faqs": [
      {"q_ar": "هل بوتكس الجز يُنحّف الوجه؟", "q_en": "Does bruxism Botox slim the face?",
       "a_ar": "نعم، من الآثار الجانبية الإيجابية تقليل ضخامة عضلة الماضغ مما يُعطي الوجه شكلًا أكثر نحافةً.", "a_en": "Yes, a positive side effect is reducing masseter bulk, giving the face a slimmer appearance."},
      {"q_ar": "متى يتوقف ألم الرأس؟", "q_en": "When does the headache pain stop?",
       "a_ar": "خلال أسبوعين من الحقن يلاحظ معظم المرضى تحسنًا ملحوظًا في الصداع.", "a_en": "Within two weeks of injection, most patients notice significant improvement in headaches."},
      {"q_ar": "هل أحتاج لإعادة الحقن؟", "q_en": "Do I need repeat injections?",
       "a_ar": "نعم كل 4-6 أشهر للحفاظ على النتيجة العلاجية.", "a_en": "Yes, every 4–6 months to maintain the therapeutic result."},
    ],
    "images": ["result-14.jpg", "result-16.jpg"],
    "related": ["botox-jabha", "botox-ragaba", "botox-anf"],
    "category": "botox",
  },
  {
    "slug": "botox-ragaba",
    "ar_name": "بوتكس الرقبة",
    "en_name": "Neck Botox",
    "ar_tagline": "شد وتنعيم بشرة الرقبة بدون جراحة",
    "en_tagline": "Lift & Smooth Neck Skin Without Surgery",
    "keyword": "بوتكس الرقبة",
    "meta_ar": "بوتكس الرقبة مع دكتور أحمد مازن — شد وتنعيم بشرة الرقبة وإزالة خطوطها بدون جراحة في القاهرة.",
    "ar_desc": "بوتكس الرقبة (Nefertiti Lift) تقنية حديثة تُرخي عضلات الرقبة المشدودة لأسفل، مما يُتيح رفع خط الفك والرقبة بشكل طبيعي. يُعالج كذلك الخطوط الأفقية للرقبة (حلقات فينوس) ويحسن مظهر البشرة في هذه المنطقة المهملة كثيرًا.",
    "en_desc": "Neck Botox (Nefertiti Lift) is a modern technique that relaxes downward-pulling neck muscles, allowing natural lifting of the jawline and neck. It also treats horizontal neck lines (Venus rings) and improves the appearance of this often-neglected area.",
    "steps": [
      {"ar": "تقييم عضلات الرقبة وخطوطها", "en": "Assessment of neck muscles and lines"},
      {"ar": "تحديد نقاط الحقن على طول الرقبة والفك", "en": "Mapping injection points along the neck and jaw"},
      {"ar": "حقن البوتوكس في العضلات المستهدفة", "en": "Botox injection into target muscles"},
      {"ar": "تقييم النتيجة والإرشادات", "en": "Result evaluation and instructions"},
    ],
    "faqs": [
      {"q_ar": "هل بوتكس الرقبة مؤلم؟", "q_en": "Is neck Botox painful?",
       "a_ar": "الإبر رفيعة جدًا والانزعاج يسير. الجلسة سريعة ومريحة.", "a_en": "The needles are very fine and discomfort is minimal. The session is quick and comfortable."},
      {"q_ar": "هل تختفي خطوط الرقبة تمامًا؟", "q_en": "Do neck lines disappear completely?",
       "a_ar": "تتحسن بشكل ملحوظ وتُخفف لكن العمق يتحكم في مدى الاستجابة.", "a_en": "They improve noticeably and are reduced, but depth determines the extent of response."},
      {"q_ar": "كم مدة النتيجة؟", "q_en": "How long do results last?",
       "a_ar": "من 3 إلى 5 أشهر.", "a_en": "3 to 5 months."},
    ],
    "images": ["result-15.jpg", "result-20.jpg"],
    "related": ["botox-jabha", "filler-shad-alwajh", "raf-altarahal"],
    "category": "botox",
  },
  {
    "slug": "botox-anf",
    "ar_name": "بوتكس الأنف",
    "en_name": "Nose Botox",
    "ar_tagline": "تحسين شكل طرف الأنف بلمسة بوتكس دقيقة",
    "en_tagline": "Refine Your Nose Tip With a Precise Botox Touch",
    "keyword": "بوتكس الأنف",
    "meta_ar": "بوتكس الأنف مع دكتور أحمد مازن — رفع طرف الأنف وتحسين شكله بدون جراحة. نتائج فورية في مصر.",
    "ar_desc": "بوتكس الأنف إجراء دقيق يهدف إلى رفع طرف الأنف وتحسين مظهره عند الابتسام. بعض الأشخاص يلاحظون أن طرف أنفهم ينخفض عند الابتسام — حقنة بوتوكس واحدة دقيقة تُعالج هذه المشكلة بشكل فعال وفوري.",
    "en_desc": "Nose Botox is a precise procedure aimed at lifting the nose tip and improving its appearance when smiling. Some people notice their nose tip drops when smiling — a single precise Botox injection effectively and immediately addresses this concern.",
    "steps": [
      {"ar": "فحص حركة طرف الأنف عند الابتسام وأثناء الراحة", "en": "Examination of nose tip movement during smiling and at rest"},
      {"ar": "تحديد نقطة الحقن الدقيقة", "en": "Identifying the precise injection point"},
      {"ar": "حقن كمية ميكروسكوبية من البوتوكس", "en": "Injection of a microscopic Botox dose"},
      {"ar": "متابعة النتيجة بعد أسبوعين", "en": "Follow-up after two weeks"},
    ],
    "faqs": [
      {"q_ar": "هل إجراء بوتكس الأنف آمن؟", "q_en": "Is nose Botox safe?",
       "a_ar": "نعم، بيد طبيب متخصص بكميات دقيقة جدًا.", "a_en": "Yes, in the hands of a specialist using very precise amounts."},
      {"q_ar": "هل الإجراء مؤلم؟", "q_en": "Is the procedure painful?",
       "a_ar": "لا يكاد يُشعر به. حقنة واحدة خفيفة فقط.", "a_en": "Barely noticeable. Just one light injection."},
      {"q_ar": "ما الفرق بينه وبين فيلر الأنف؟", "q_en": "What's the difference from nose filler?",
       "a_ar": "البوتكس يُرخي العضلة لرفع الطرف، بينما الفيلر يُضيف حجمًا ويُعيد تشكيل الأنف.", "a_en": "Botox relaxes the muscle to lift the tip, while filler adds volume and reshapes the nose."},
    ],
    "images": ["result-08.jpg", "result-11.jpg"],
    "related": ["filler-alanf", "botox-jabha", "filler-shad-alwajh"],
    "category": "botox",
  },
  {
    "slug": "botox-ta3arroq",
    "ar_name": "بوتكس التعرق",
    "en_name": "Hyperhidrosis Botox",
    "ar_tagline": "تخلص من التعرق المفرط نهائيًا",
    "en_tagline": "Eliminate Excessive Sweating for Good",
    "keyword": "علاج التعرق المفرط بالبوتكس",
    "meta_ar": "بوتكس لعلاج التعرق المفرط في اليدين والإبطين والرجلين مع دكتور أحمد مازن — نتائج طويلة الأمد.",
    "ar_desc": "التعرق المفرط (Hyperhidrosis) مشكلة مزعجة تُؤثر على الثقة بالنفس والحياة اليومية. البوتكس يمنع إفراز العرق بشكل آمن وفعّال من خلال حجب الإشارات العصبية التي تُحفز الغدد العرقية. يُعالج الدكتور أحمد مازن هذه المشكلة في اليدين والإبطين والرجلين بنتائج تدوم 6-12 شهرًا.",
    "en_desc": "Excessive sweating (Hyperhidrosis) is a distressing condition affecting confidence and daily life. Botox safely and effectively prevents sweat production by blocking the nerve signals that stimulate sweat glands. Dr. Ahmed Mazen treats this condition in the hands, underarms, and feet with results lasting 6–12 months.",
    "steps": [
      {"ar": "تحديد المناطق المتأثرة بالتعرق الزائد", "en": "Identification of affected excessive sweating areas"},
      {"ar": "تطبيق مخدر موضعي للراحة التامة", "en": "Topical anesthetic for complete comfort"},
      {"ar": "حقن متعدد دقيق للبوتوكس في المنطقة المستهدفة", "en": "Multiple precise Botox injections in the target area"},
      {"ar": "إرشادات ما بعد الجلسة", "en": "Post-session care instructions"},
    ],
    "faqs": [
      {"q_ar": "هل البوتكس يعالج التعرق نهائيًا؟", "q_en": "Does Botox permanently treat sweating?",
       "a_ar": "يوقفه من 6 إلى 12 شهرًا ثم يمكن تكرار الجلسة للاستمرار.", "a_en": "It stops sweating for 6–12 months, then the session can be repeated to continue."},
      {"q_ar": "هل العلاج مؤلم؟", "q_en": "Is the treatment painful?",
       "a_ar": "يُطبَّق مخدر موضعي وتكون الجلسة مريحة جدًا.", "a_en": "Topical anesthetic is applied and the session is very comfortable."},
      {"q_ar": "هل يؤثر على وظائف الجسم الأخرى؟", "q_en": "Does it affect other body functions?",
       "a_ar": "لا على الإطلاق، الجسم يواصل التعرق الطبيعي في مناطق أخرى.", "a_en": "Not at all. The body continues normal sweating in other areas."},
    ],
    "images": ["result-20.jpg", "result-21.jpg"],
    "related": ["botox-jabha", "botox-dahr", "botox-soda3"],
    "category": "botox",
  },
  {
    "slug": "botox-dahr",
    "ar_name": "بوتكس فقرات الظهر",
    "en_name": "Back Botox",
    "ar_tagline": "حرية الحركة وراحة الظهر بدون علاجات تقليدية",
    "en_tagline": "Freedom of Movement & Back Comfort Without Traditional Treatments",
    "keyword": "بوتكس فقرات الظهر",
    "meta_ar": "بوتكس فقرات الظهر مع دكتور أحمد مازن — لتخفيف توتر عضلات الظهر والتعرق. نتائج سريعة.",
    "ar_desc": "بوتكس الظهر يُستخدم لتخفيف توتر العضلات المزمن في منطقة الظهر والعمود الفقري، مما يُريح الألم الناجم عن التشنج العضلي. يُفيد كذلك في علاج التعرق المفرط في منطقة الظهر. إجراء سريع وفعال يوفر راحة ملموسة.",
    "en_desc": "Back Botox is used to relieve chronic muscle tension in the back and spine area, relieving pain caused by muscle spasm. It is also useful in treating excessive sweating in the back area. A quick and effective procedure that provides tangible relief.",
    "steps": [
      {"ar": "تقييم المنطقة المستهدفة من الظهر", "en": "Assessment of the target back area"},
      {"ar": "تحديد العضلات المتشنجة أو الغدد العرقية المتأثرة", "en": "Identifying spasmed muscles or affected sweat glands"},
      {"ar": "حقن البوتوكس بدقة في النقاط المحددة", "en": "Precise Botox injection at mapped points"},
      {"ar": "الراحة قليلًا ثم مواصلة الحياة الطبيعية", "en": "Brief rest then resuming normal activities"},
    ],
    "faqs": [
      {"q_ar": "من يستفيد من بوتكس الظهر؟", "q_en": "Who benefits from Back Botox?",
       "a_ar": "المرضى الذين يعانون من تشنج عضلي مزمن في الظهر أو التعرق الزائد في هذه المنطقة.", "a_en": "Patients with chronic back muscle spasm or excessive sweating in this area."},
      {"q_ar": "هل الإجراء آمن على العمود الفقري؟", "q_en": "Is the procedure safe for the spine?",
       "a_ar": "نعم تمامًا. يتم الحقن في العضلات السطحية وليس القناة الشوكية.", "a_en": "Absolutely. Injection is into superficial muscles, not the spinal canal."},
      {"q_ar": "كم تدوم النتيجة؟", "q_en": "How long do results last?",
       "a_ar": "من 4 إلى 6 أشهر للشد العضلي، ومن 6 إلى 9 أشهر للتعرق.", "a_en": "4–6 months for muscle tension, and 6–9 months for sweating."},
    ],
    "images": ["result-21.jpg", "result-14.jpg"],
    "related": ["botox-ta3arroq", "botox-ragaba", "botox-jabha"],
    "category": "botox",
  },
  # ── BODY ──
  {
    "slug": "filler-aydi",
    "ar_name": "فيلر الأيدي",
    "en_name": "Hand Filler",
    "ar_tagline": "يدان شابتان ناعمتان — بدون جراحة",
    "en_tagline": "Youthful, Smooth Hands — Without Surgery",
    "keyword": "فيلر تجميل اليدين",
    "meta_ar": "فيلر اليدين مع دكتور أحمد مازن — استعادة شباب اليدين وإخفاء الأوردة والعروق البارزة. القاهرة.",
    "ar_desc": "اليدان أول ما يُكشف عمره من الجسم. فقدان الحجم في ظهر اليد يجعل الأوردة والأوتار بارزة ومُقبّحة. يُعالج الدكتور أحمد مازن هذه المنطقة بفيلر هيالورونيك أسيد لإعادة الحجم الطبيعي وإخفاء الأوردة البارزة، مما يمنح اليدين مظهرًا أكثر شبابًا ونعومةً.",
    "en_desc": "Hands are the first part of the body to reveal age. Volume loss in the back of the hand makes veins and tendons prominent and unattractive. Dr. Ahmed Mazen treats this area with hyaluronic acid filler to restore natural volume and conceal protruding veins, giving hands a younger, smoother appearance.",
    "steps": [
      {"ar": "تقييم حجم اليد ودرجة ظهور الأوردة", "en": "Assessment of hand volume and vein prominence"},
      {"ar": "تطبيق مخدر موضعي على ظهر اليد", "en": "Topical anesthetic on the back of the hand"},
      {"ar": "حقن الفيلر بالكنولا أو الإبرة في المنطقة المستهدفة", "en": "Cannula or needle filler injection in the target area"},
      {"ar": "تدليك لطيف لتوزيع الفيلر بشكل متساوٍ", "en": "Gentle massage to distribute the filler evenly"},
    ],
    "faqs": [
      {"q_ar": "هل فيلر اليد مؤلم؟", "q_en": "Is hand filler painful?",
       "a_ar": "مع التخدير الموضعي يكون الانزعاج بسيطًا جدًا.", "a_en": "With topical anesthetic, discomfort is very minimal."},
      {"q_ar": "كم تدوم نتائج فيلر اليد؟", "q_en": "How long do hand filler results last?",
       "a_ar": "عادةً من 9 إلى 18 شهرًا.", "a_en": "Usually 9–18 months."},
      {"q_ar": "هل يمكن رؤية النتيجة فورًا؟", "q_en": "Can results be seen immediately?",
       "a_ar": "نعم، النتيجة مرئية فور الجلسة.", "a_en": "Yes, results are visible immediately after the session."},
    ],
    "images": ["result-06.jpg", "result-07.jpg"],
    "related": ["filler-ardaf", "filler-reglen", "filler-gesm"],
    "category": "body",
  },
  {
    "slug": "filler-ardaf",
    "ar_name": "فيلر الأرداف",
    "en_name": "Buttocks Filler",
    "ar_tagline": "قوام متناسق ومنحنيات طبيعية بدون جراحة",
    "en_tagline": "Balanced Figure & Natural Curves Without Surgery",
    "keyword": "فيلر الأرداف",
    "meta_ar": "فيلر الأرداف مع دكتور أحمد مازن في مصر — تحسين شكل الأرداف بشكل طبيعي وآمن بدون جراحة.",
    "ar_desc": "فيلر الأرداف بديل آمن وغير جراحي لعمليات تكبير الأرداف. يستخدم الدكتور أحمد مازن الفيلر لتحسين شكل وحجم منطقة الأرداف بشكل طبيعي متناسق مع قوام الجسم، مع تجنب مخاطر الجراحة والتخدير العام وفترات التعافي الطويلة.",
    "en_desc": "Buttocks filler is a safe, non-surgical alternative to buttock augmentation surgery. Dr. Ahmed Mazen uses filler to improve the shape and volume of the buttocks area naturally and in harmony with body proportions, avoiding surgical risks, general anesthesia, and long recovery periods.",
    "steps": [
      {"ar": "مناقشة النتيجة المطلوبة وتحديد الحجم والشكل", "en": "Discussion of desired outcome, volume, and shape"},
      {"ar": "تطبيق التخدير الموضعي اللازم", "en": "Application of required local anesthesia"},
      {"ar": "حقن الفيلر بالكنولا بدقة في المنطقة المستهدفة", "en": "Precise cannula filler injection in the target area"},
      {"ar": "تشكيل وضبط التناسق", "en": "Shaping and symmetry adjustment"},
    ],
    "faqs": [
      {"q_ar": "هل فيلر الأرداف آمن؟", "q_en": "Is buttocks filler safe?",
       "a_ar": "نعم، بيد طبيب متخصص خبير يستخدم مواد معتمدة.", "a_en": "Yes, with an experienced specialist using approved materials."},
      {"q_ar": "كم تدوم النتائج؟", "q_en": "How long do results last?",
       "a_ar": "من 12 إلى 24 شهرًا حسب نوع الفيلر المستخدم.", "a_en": "12–24 months depending on the filler type used."},
      {"q_ar": "هل هناك فترة تعافٍ؟", "q_en": "Is there a recovery period?",
       "a_ar": "لا تعافٍ. يمكن ممارسة النشاطات الاعتيادية الخفيفة بعد الجلسة مباشرةً.", "a_en": "No recovery. Light daily activities can be resumed immediately after the session."},
    ],
    "images": ["result-05.jpg", "result-09.jpg"],
    "related": ["filler-reglen", "filler-gesm", "filler-aydi"],
    "category": "body",
  },
  {
    "slug": "filler-reglen",
    "ar_name": "فيلر الرجلين",
    "en_name": "Leg Filler",
    "ar_tagline": "ساقان أكثر تناسقًا وجمالًا — بدون جراحة",
    "en_tagline": "More Contoured, Beautiful Legs — Without Surgery",
    "keyword": "فيلر الرجل",
    "meta_ar": "فيلر الرجلين مع دكتور أحمد مازن — تناسق وتجميل الساقين بدون جراحة أو تعافٍ في مصر.",
    "ar_desc": "فيلر الرجلين يُستخدم لتحسين تناسق وشكل الساقين من خلال ملء المناطق الغائرة وتصحيح عدم الاستواء. مناسب لمن يعانون من تقوس الساقين الخفيف أو عدم التناسق أو الغمازات. الإجراء سريع وبدون جراحة.",
    "en_desc": "Leg filler is used to improve the contour and shape of the legs by filling sunken areas and correcting unevenness. Suitable for those with mild bow legs, asymmetry, or dimpling. Quick procedure, no surgery.",
    "steps": [
      {"ar": "تقييم شكل الساقين وتحديد المناطق المستهدفة", "en": "Leg shape assessment and target area identification"},
      {"ar": "تخدير موضعي للراحة", "en": "Topical anesthetic for comfort"},
      {"ar": "حقن الفيلر بالكنولا في المناطق المحددة", "en": "Cannula filler injection in mapped areas"},
      {"ar": "تشكيل وضبط التماثل", "en": "Shaping and symmetry adjustment"},
    ],
    "faqs": [
      {"q_ar": "هل يمكن الوقوف والمشي بعد الجلسة مباشرةً؟", "q_en": "Can I stand and walk immediately after the session?",
       "a_ar": "نعم، مع تجنب الجهد الشديد ليوم أو يومين.", "a_en": "Yes, while avoiding strenuous activity for a day or two."},
      {"q_ar": "لمن يناسب هذا الإجراء؟", "q_en": "Who is this procedure suitable for?",
       "a_ar": "من يعاني من تقوس خفيف أو عدم تناسق أو منطقة غائرة في الساق.", "a_en": "Those with mild bow legs, asymmetry, or a sunken area in the leg."},
      {"q_ar": "كم تدوم النتائج؟", "q_en": "How long do results last?",
       "a_ar": "من 12 إلى 18 شهرًا.", "a_en": "12–18 months."},
    ],
    "images": ["result-04.jpg", "result-08.jpg"],
    "related": ["filler-ardaf", "filler-gesm", "filler-aydi"],
    "category": "body",
  },
  {
    "slug": "filler-gesm",
    "ar_name": "فيلر الجسم",
    "en_name": "Body Filler",
    "ar_tagline": "تحسين تناسق القوام العام بتقنية الفيلر المتخصصة",
    "en_tagline": "Improve Overall Body Contour with Specialized Filler",
    "keyword": "فيلر الجسم",
    "meta_ar": "فيلر الجسم مع دكتور أحمد مازن — تحسين القوام وتناسق الجسم بدون جراحة في القاهرة مصر.",
    "ar_desc": "فيلر الجسم تقنية شاملة لمعالجة مناطق متعددة من الجسم في جلسة واحدة أو جلسات متتالية. يُستخدم لإعادة الحجم للمناطق الغائرة، تحسين التناسق، وتصحيح الندبات أو المناطق غير المتساوية بدون جراحة.",
    "en_desc": "Body filler is a comprehensive technique for treating multiple body areas in one or consecutive sessions. Used to restore volume to sunken areas, improve contour, and correct scars or uneven areas without surgery.",
    "steps": [
      {"ar": "استشارة شاملة لتحديد المناطق المستهدفة وخطة العلاج", "en": "Comprehensive consultation to identify target areas and treatment plan"},
      {"ar": "تخدير موضعي مناسب لكل منطقة", "en": "Appropriate local anesthesia for each area"},
      {"ar": "حقن الفيلر بدقة في المناطق المحددة", "en": "Precise filler injection in mapped areas"},
      {"ar": "تقييم شامل للنتيجة وضبط التناسق", "en": "Comprehensive result evaluation and contour adjustment"},
    ],
    "faqs": [
      {"q_ar": "ما المناطق التي يمكن علاجها بفيلر الجسم؟", "q_en": "What areas can body filler treat?",
       "a_ar": "الأرداف، الرجلان، اليدان، ومناطق الندبات أو الغمازات في أي مكان بالجسم.", "a_en": "Buttocks, legs, hands, and areas of scars or dimpling anywhere on the body."},
      {"q_ar": "هل الإجراء آمن؟", "q_en": "Is the procedure safe?",
       "a_ar": "نعم، بيد طبيب متخصص وبمواد معتمدة صحيًا.", "a_en": "Yes, with a specialist using medically approved materials."},
      {"q_ar": "كم جلسة أحتاج؟", "q_en": "How many sessions do I need?",
       "a_ar": "يعتمد على المنطقة والحجم المطلوب، يتم تحديده بعد الاستشارة.", "a_en": "Depends on the area and required volume, determined after consultation."},
    ],
    "images": ["result-05.jpg", "result-06.jpg", "result-09.jpg"],
    "related": ["filler-ardaf", "filler-reglen", "filler-aydi"],
    "category": "body",
  },
]

# Related slug → name mapping
SLUG_TO_NAMES = {s["slug"]: (s["ar_name"], s["en_name"]) for s in SERVICES}

# ──────────────────────────────────────────────────────
# PAGE GENERATOR
# ──────────────────────────────────────────────────────
def make_steps(steps):
    html = '<div class="steps-grid">\n'
    for i, s in enumerate(steps, 1):
        html += f'''      <div class="step-item reveal">
        <div class="step-num">{i:02d}</div>
        <div class="step-text">
          <span class="ar-text">{s["ar"]}</span>
          <span class="en-text">{s["en"]}</span>
        </div>
      </div>\n'''
    html += '    </div>'
    return html

def make_faqs(faqs):
    html = '<div class="faq-list">\n'
    for f in faqs:
        html += f'''      <div class="faq-item">
        <button class="faq-q">
          <span class="ar-text">{f["q_ar"]}</span>
          <span class="en-text">{f["q_en"]}</span>
          <svg class="faq-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-a">
          <p><span class="ar-text">{f["a_ar"]}</span><span class="en-text">{f["a_en"]}</span></p>
        </div>
      </div>\n'''
    html += '    </div>'
    return html

def make_images(imgs, root):
    """Build a slideshow banner for a service page."""
    if not imgs:
        return ''
    # All 21 result images cycle in the slideshow, but service-specific ones come first
    all_imgs = [f'result-{i:02d}.jpg' for i in range(1, 22)]
    # Put service images first, then the rest
    ordered = imgs + [x for x in all_imgs if x not in imgs]
    imgs_js = ', '.join(
        f'{{ src: "{root}/assets/before-after/{img}", alt: "\u0646\u062a\u064a\u062c\u0629 \u062d\u0642\u064a\u0642\u064a\u0629" }}'
        for img in ordered
    )
    # unique id based on slug (caller must pass slug or we use a counter)
    uid = 'svc'
    return f'''<div class="slideshow-section service-slideshow-section">
      <div class="slideshow-banner" id="{uid}SlideshowBanner">
        <div class="slide-track" id="{uid}SlideshowTrack"></div>
        <button class="slide-arrow slide-arrow-prev" id="{uid}SlideArrowPrev" aria-label="Previous">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
        </button>
        <button class="slide-arrow slide-arrow-next" id="{uid}SlideArrowNext" aria-label="Next">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
        </button>
      </div>
      <div class="slide-dots" id="{uid}SlideDots"></div>
      <div class="ss-lightbox" id="{uid}Lightbox" role="dialog" aria-modal="true">
        <div class="ss-lightbox-img-wrap">
          <button class="ss-lb-btn ss-lb-close" id="{uid}LbClose" aria-label="Close">&#x2715;</button>
          <button class="ss-lb-btn ss-lb-prev" id="{uid}LbPrev" aria-label="Previous">&#x2039;</button>
          <button class="ss-lb-btn ss-lb-next" id="{uid}LbNext" aria-label="Next">&#x203A;</button>
          <img src="" alt="" id="{uid}LbImg" />
        </div>
      </div>
    </div>
    <script>
      document.addEventListener('DOMContentLoaded', function() {{
        if (typeof initSlideshow === 'function') {{
          initSlideshow({{
            containerId: '{uid}SlideshowBanner',
            trackId:     '{uid}SlideshowTrack',
            prevId:      '{uid}SlideArrowPrev',
            nextId:      '{uid}SlideArrowNext',
            dotsId:      '{uid}SlideDots',
            lightboxId:  '{uid}Lightbox',
            lbImgId:     '{uid}LbImg',
            lbCloseId:   '{uid}LbClose',
            lbPrevId:    '{uid}LbPrev',
            lbNextId:    '{uid}LbNext',
            interval:    4500,
            images: [{imgs_js}]
          }});
        }}
      }});
    </script>'''

def make_related(slugs, root):
    html = '<div class="related-grid">\n'
    for slug in slugs[:3]:
        if slug in SLUG_TO_NAMES:
            ar, en = SLUG_TO_NAMES[slug]
            html += f'''      <a href="{root}/services/{slug}/index.html" class="related-card">
        <span class="ar-text">{ar}</span>
        <span class="en-text">{en}</span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>\n'''
    html += '    </div>'
    return html

def schema_service(svc):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "MedicalProcedure",
        "name": svc["en_name"],
        "alternateName": svc["ar_name"],
        "description": svc["en_desc"],
        "procedureType": "Noninvasive",
        "followup": "Immediate results, no downtime",
        "preparation": "Topical anesthesia applied before procedure",
        "provider": {
            "@type": "Physician",
            "name": "Dr. Ahmed Mazen",
            "telephone": "+201274477111",
            "url": "https://drahmedmazen.com"
        }
    }, ensure_ascii=False, indent=2)

def generate_service_page(svc):
    root = "../.."
    slug = svc["slug"]

    page = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl" data-lang="ar">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{svc["ar_name"]} | دكتور أحمد مازن | Dr. Ahmed Mazen</title>
  <meta name="description" content="{svc["meta_ar"]}"/>
  <meta name="keywords" content="{svc["keyword"]}, دكتور أحمد مازن, طب التجميل مصر, تجميل بدون جراحة"/>
  <link rel="canonical" href="https://drahmedmazen.com/services/{slug}/"/>
  <meta property="og:title" content="{svc["ar_name"]} | دكتور أحمد مازن"/>
  <meta property="og:description" content="{svc["meta_ar"]}"/>
  <meta property="og:type" content="website"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Cairo:wght@300;400;500;600;700&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet"/>
  <script type="application/ld+json">{schema_service(svc)}</script>
  <link rel="stylesheet" href="{root}/css/style.css"/>
  <link rel="stylesheet" href="{root}/css/service.css"/>
  <link rel="stylesheet" href="{root}/css/slideshow.css"/>
</head>
<body>

{navbar(root)}

  <!-- SERVICE HERO -->
  <section class="service-hero">
    <div class="service-hero-bg"></div>
    <div class="container">
      <div class="breadcrumb">
        <a href="{root}/index.html"><span class="ar-text">الرئيسية</span><span class="en-text">Home</span></a>
        <span class="sep">›</span>
        <a href="{root}/index.html#services"><span class="ar-text">الخدمات</span><span class="en-text">Services</span></a>
        <span class="sep">›</span>
        <span class="ar-text">{svc["ar_name"]}</span><span class="en-text">{svc["en_name"]}</span>
      </div>
      <h1>
        <span class="ar-text">{svc["ar_name"]}</span>
        <span class="en-text">{svc["en_name"]}</span>
      </h1>
      <p class="service-hero-tagline">
        <span class="ar-text">{svc["ar_tagline"]}</span>
        <span class="en-text">{svc["en_tagline"]}</span>
      </p>
      <div class="service-hero-ctas">
        <a href="https://wa.me/201274477111" target="_blank" rel="noopener" class="btn btn-gold btn-lg">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
          <span class="ar-text">احجز الآن</span>
          <span class="en-text">Book Now</span>
        </a>
        <a href="{root}/index.html#results" class="btn btn-outline btn-lg">
          <span class="ar-text">شاهد النتائج</span>
          <span class="en-text">See Results</span>
        </a>
      </div>
    </div>
  </section>

  <!-- WHAT IS IT -->
  <section class="service-desc">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">
          <span class="ar-text">ما هو؟</span>
          <span class="en-text">What Is It?</span>
        </span>
        <h2>
          <span class="ar-text">{svc["ar_name"]}</span>
          <span class="en-text">{svc["en_name"]}</span>
        </h2>
      </div>
      <p class="service-desc-text reveal">
        <span class="ar-text">{svc["ar_desc"]}</span>
        <span class="en-text">{svc["en_desc"]}</span>
      </p>
    </div>
  </section>

  <!-- HOW IT WORKS -->
  <section class="service-steps">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">
          <span class="ar-text">كيف يتم؟</span>
          <span class="en-text">How It Works</span>
        </span>
        <h2>
          <span class="ar-text">خطوات الجلسة</span>
          <span class="en-text">Session Steps</span>
        </h2>
      </div>
      {make_steps(svc["steps"])}
    </div>
  </section>

  <!-- BEFORE & AFTER -->
  <section class="service-results">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">
          <span class="ar-text">نتائج حقيقية</span>
          <span class="en-text">Real Results</span>
        </span>
        <h2>
          <span class="ar-text">قبل وبعد</span>
          <span class="en-text">Before &amp; After</span>
        </h2>
      </div>
      {make_images(svc["images"], root)}
    </div>
  </section>

  <!-- FAQ -->
  <section class="service-faq">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">FAQ</span>
        <h2>
          <span class="ar-text">أسئلة شائعة</span>
          <span class="en-text">Frequently Asked Questions</span>
        </h2>
      </div>
      {make_faqs(svc["faqs"])}
    </div>
  </section>

  <!-- CTA BANNER -->
  <section class="cta-banner">
    <div class="container">
      <h2>
        <span class="ar-text">مستعد للبدء؟ احجز استشارتك الآن</span>
        <span class="en-text">Ready to Start? Book Your Consultation Now</span>
      </h2>
      <p>
        <span class="ar-text">تواصل معنا عبر واتساب للحجز أو الاستفسار</span>
        <span class="en-text">Contact us via WhatsApp to book or inquire</span>
      </p>
      <a href="https://wa.me/201274477111" target="_blank" rel="noopener" class="btn btn-gold btn-lg">
        <span class="ar-text">تواصل الآن على واتساب</span>
        <span class="en-text">Chat on WhatsApp Now</span>
      </a>
    </div>
  </section>

  <!-- RELATED SERVICES -->
  <section class="related-services">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">
          <span class="ar-text">اكتشف أيضًا</span>
          <span class="en-text">Explore Also</span>
        </span>
        <h2>
          <span class="ar-text">خدمات ذات صلة</span>
          <span class="en-text">Related Services</span>
        </h2>
      </div>
      {make_related(svc["related"], root)}
    </div>
  </section>

{footer(root)}

  <script src="{root}/js/slideshow.js"></script>
  <script src="{root}/js/main.js"></script>
  <script src="{root}/js/service.js"></script>
</body>
</html>"""
    return page

# ──────────────────────────────────────────────────────
# WRITE ALL SERVICE PAGES
# ──────────────────────────────────────────────────────
def write_pages():
    services_dir = os.path.join(BASE, 'services')
    os.makedirs(services_dir, exist_ok=True)
    count = 0
    for svc in SERVICES:
        slug_dir = os.path.join(services_dir, svc["slug"])
        os.makedirs(slug_dir, exist_ok=True)
        page_path = os.path.join(slug_dir, 'index.html')
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(generate_service_page(svc))
        count += 1
        print(f"  ✓ services/{svc['slug']}/index.html — {svc['ar_name']}")
    print(f"\n✅ Generated {count} service pages")

if __name__ == "__main__":
    print("🚀 Generating Dr. Ahmed Mazen service pages...\n")
    write_pages()
