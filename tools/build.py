# Generates the static HTML pages for Bincoo MENA from one shared template.
# Usage (from the repo root):  python tools/build.py [asset-version]
# Edit texts, products or contact details here, then re-run to regenerate every page.
import json, os, sys

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://bincoo-mena.com"
WA = "97470510002"
PHONE = "+974 7051 0002"
EMAIL = "bincoo@kuvani.com"
IG = "https://www.instagram.com/bincoo.mena/"
IG_KUVANI = "https://www.instagram.com/kuvani.co/"
V = sys.argv[1] if len(sys.argv) > 1 else "6"

# ---------------------------------------------------------------- icons
I = {
 "arrow": '<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "arrow_ur": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>',
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.08-.3-.15-1.26-.47-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.07c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.41-.08-.13-.27-.2-.57-.35m-5.42 7.4h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.82 9.82 0 0 1 2.89 6.99c0 5.45-4.44 9.88-9.88 9.88m8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.16-3.48-8.41z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m4 7 8 6 8-6"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h3.5l1.7 4.3-2.2 1.5a11 11 0 0 0 6.2 6.2l1.5-2.2L20 15.5V19a1.5 1.5 0 0 1-1.6 1.5A16.5 16.5 0 0 1 3.5 5.6 1.5 1.5 0 0 1 5 4z"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1" fill="currentColor" stroke="none"/></svg>',
 "sun": '<svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
 "moon": '<svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/></svg>',
 "tick": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.2 4.2L19 7"/></svg>',
 "star": '<svg class="marquee__star" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 0c.6 6.4 5.6 11.4 12 12-6.4.6-11.4 5.6-12 12-.6-6.4-5.6-11.4-12-12C6.4 11.4 11.4 6.4 12 0z"/></svg>',
 "cup": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9h13v5a6 6 0 0 1-6 6h-1a6 6 0 0 1-6-6V9z"/><path d="M17 11h1.5a2.5 2.5 0 0 1 0 5H17M8 2.5c-.8 1 .8 2 0 3.5M12 2.5c-.8 1 .8 2 0 3.5"/></svg>',
 "bell": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 18h18M5 18a7 7 0 0 1 14 0M12 8V6M10 6h4"/></svg>',
 "office": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="1.5"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2M8 15h2M14 15h2M10 21v-3h4v3"/></svg>',
 "store": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 9 5 4h14l1.5 5M3.5 9h17M3.5 9a2.8 2.8 0 0 0 5.7 0 2.8 2.8 0 0 0 5.6 0 2.8 2.8 0 0 0 5.7 0M5 12v8h14v-8M10 20v-5h4v5"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.4 7.5 9.5 4.3-1.1 7.5-4.9 7.5-9.5V6L12 3z"/><path d="m8.8 12 2.2 2.2 4.3-4.4"/></svg>',
 "tag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12.2V4.5A1.5 1.5 0 0 1 4.5 3h7.7l8.3 8.3a1.5 1.5 0 0 1 0 2.1l-7.1 7.1a1.5 1.5 0 0 1-2.1 0L3 12.2z"/><circle cx="7.8" cy="7.8" r="1.4"/></svg>',
 "briefcase": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8.5 7V5.5A1.5 1.5 0 0 1 10 4h4a1.5 1.5 0 0 1 1.5 1.5V7M3 12.5h18"/></svg>',
 "zoom": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg>',
 "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
 "prev": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 5-7 7 7 7"/></svg>',
 "next": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>',
 "info": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v5.5M12 7.6v.1"/></svg>',
 "screen": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="5" y="3" width="14" height="18" rx="3"/><path d="M10 17.5h4" stroke-linecap="round"/></svg>',
 "gauge": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M4 16a8 8 0 1 1 16 0"/><path d="m12 16 4-5"/></svg>',
}

def bincoo(cls="logo-bincoo", p=""):
    return f'<svg class="{cls}" viewBox="0 0 1720 910" role="img" aria-label="Bincoo"><use href="{p}assets/img/brand/bincoo.svg#logo"/></svg>'

def kuvani(cls="logo-kuvani", p=""):
    return f'<svg class="{cls}" viewBox="0 0 1620 209" role="img" aria-label="KUVANI"><use href="{p}assets/img/brand/kuvani.svg#logo"/></svg>'

# ---------------------------------------------------------------- products
PRODUCTS = [
 dict(slug="s2-pro-trailblazer", value="s2-pro", name="S2 Pro Trailblazer", title_html="S2 Pro <em>Trailblazer</em>",
      full="Bincoo S2 Pro Trailblazer Smart Espresso Machine", cat="Smart Espresso Machine", tag="Flagship",
      card_desc="Dual-boiler espresso with a 3.4&Prime; touch screen, Bluetooth app control and 3&ndash;12 bar pressure profiling.",
      price="$2,200", main="s2-black", alt="s2-white"),
 dict(slug="automatic-pour-over", value="pour-over", name="Automatic Pour-Over", title_html="Automatic <em>Pour-Over</em>",
      full="Bincoo Fully Automatic Smart Pour-Over Coffee Machine", cat="Grind &amp; Brew Pour-Over", tag="Grind &amp; Brew",
      card_desc="Grinds, blooms and pours on its own &mdash; barista-quality pour-over in about three minutes.",
      price="$1,100", main="po-black", alt="po-white"),
 dict(slug="composer-po01", value="composer-po01", name="Composer PO01", title_html="Composer <em>PO01</em>",
      full="Bincoo Composer PO01 Automatic Pour-Over Coffee Maker", cat="Automatic Pour-Over Brewer", tag="Compact",
      card_desc="Pro pour techniques, automated &mdash; PID heating from 40&ndash;95&nbsp;&deg;C and six brewing modes.",
      price="$650", main="cp-black", alt=None),
]
BY_SLUG = {p["slug"]: p for p in PRODUCTS}

HERO = [
 dict(slug="s2-pro-trailblazer", name="S2 Pro Trailblazer", image="s2-black", alt="Bincoo S2 Pro Trailblazer smart espresso machine in black",
      chips=[(I["screen"], "3.4&Prime; touch screen + app"), (I["gauge"], "3&ndash;12 bar profiling"), ("58", "mm professional group head")]),
 dict(slug="automatic-pour-over", name="Automatic Pour-Over", image="po-black", alt="Bincoo Automatic Pour-Over grind and brew machine in black",
      chips=[(I["screen"], "4.3&Prime; HD touch screen"), ("80", "step burr grinder"), ("3&prime;", "Bean to cup in ~3 min")]),
 dict(slug="composer-po01", name="Composer PO01", image="cp-black", alt="Bincoo Composer PO01 automatic pour-over brewer in black",
      chips=[(I["screen"], "6 preset brewing modes"), (I["gauge"], "PID 40&ndash;95 &deg;C"), ("H&#8322;O", "Automatic water supply")]),
]

FAQS = [("Can individuals buy from Bincoo MENA?", "No. Bincoo MENA operates exclusively through authorized distributors. We do not sell directly to individuals or end customers. All purchases should be made through our official distributors in each market."),
        ("How do I get pricing?", "Prices on this site are retail references in USD. Final pricing is set by the authorized distributor in your market &mdash; contact us and we&rsquo;ll connect you."),
        ("Which countries do you cover?", "Bincoo MENA covers the Middle East &amp; North Africa. Tell us your country and we&rsquo;ll point you to the authorized distributor there, or talk about distribution if there isn&rsquo;t one yet."),
        ("How can I become an authorized distributor?", "Contact us with your company details and the market you cover. Distributor terms, including minimum orders, depend on the product and the market, and our team will walk you through them."),
        ("Are there shipping fees?", "There is no online checkout on this site, so no shipping fees are charged here. Delivery is arranged by the authorized distributor in your market."),
        ("Which versions are available?", "S2 Pro Trailblazer comes in black or white, or as a bundle with the DM02 electric grinder. The Automatic Pour-Over and Composer PO01 come in black or white."),
        ("What power supply do the machines use?", "The S2 Pro Trailblazer and Automatic Pour-Over run on 220&nbsp;V / 50&nbsp;Hz. Your distributor can confirm the requirements for your market.")]

def img(name, p="", alt="", cls="", lazy=True, extra=""):
    c = f' class="{cls}"' if cls else ""
    l = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img src="{p}assets/img/products/{name}.webp" alt="{alt}"{c}{l}{extra}>'

def card(pr, i, p=""):
    href = f'{p}products/{pr["slug"]}.html'
    alt_img = img(pr["alt"], p, f'{pr["name"]} in white', "alt") if pr["alt"] else ""
    return f'''
      <article class="p-card" data-reveal>
        <a class="p-card__link" href="{href}" aria-label="View {pr['name']}"></a>
        <div class="p-card__media">
          <span class="p-card__index">0{i}</span>
          <span class="p-card__tag">{pr['tag']}</span>
          {img(pr["main"], p, pr["full"], "main")}
          {alt_img}
        </div>
        <div class="p-card__body">
          <span class="p-card__cat">{pr['cat']}</span>
          <h3 class="p-card__name">{pr['name']}</h3>
          <p class="p-card__desc">{pr['card_desc']}</p>
          <div class="p-card__foot">
            <div class="price"><small>Retail ref. (USD)</small><strong>{pr['price']}</strong></div>
            <div class="swatches" aria-label="Available in black and white"><span class="swatch swatch--black"></span><span class="swatch swatch--white"></span></div>
          </div>
          <div class="p-card__actions">
            <a class="btn btn--sm" href="{href}">View details {I['arrow']}</a>
            <a class="btn btn--sm btn--ghost" href="#" data-wa="{pr['full']}">{I['wa']} Find a distributor</a>
          </div>
        </div>
      </article>'''

# ---------------------------------------------------------------- layout
def head(title, desc, path, p="", og="assets/img/og.jpg", jsonld=None):
    url = DOMAIN + "/" + path
    ld = f'\n  <script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>' if jsonld else ""
    return f'''<!doctype html>
<html lang="en" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#F5F2EC">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Bincoo MENA">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{DOMAIN}/{og}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
  <link rel="icon" href="{p}favicon-32.png" sizes="32x32" type="image/png">
  <link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
  <link rel="manifest" href="{p}site.webmanifest">
  <script>(function(){{var d=document.documentElement;d.classList.add('js');try{{var t=localStorage.getItem('bm-theme');if(!t)t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';d.setAttribute('data-theme',t);if(sessionStorage.getItem('bm-visited'))d.classList.add('skip-preloader');}}catch(e){{}}}})();</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..500&family=Manrope:wght@400;500;600;700;800&display=swap">
  <link rel="stylesheet" href="{p}assets/css/style.css?v={V}">{ld}
</head>'''

NAV = [("Collection", "#collection"), ("Distributors", "#business"), ("About", "#about"), ("FAQ", "#faq"), ("Contact", "#inquiry")]

def header(p="", home=True):
    base = "" if home else f"{p}"
    nav = "".join(f'<a href="{base}{h}">{t}</a>' for t, h in NAV)
    home_href = "#top" if home else p
    return f'''
<body id="top">
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="preloader" aria-hidden="true">
    <div class="preloader__inner">
      {bincoo(p=p)}
      <div class="preloader__bar"><span></span></div>
      <div class="preloader__by">Exclusive by {kuvani(p=p)}</div>
    </div>
  </div>
  <div class="progress" aria-hidden="true"><span></span></div>

  <div class="topbar">
    <div class="container">
      <span class="topbar__dot"></span>
      <span>Official Bincoo in MENA <span class="topbar__long">&middot; Sold through authorized distributors</span></span>
      <span aria-hidden="true">&middot;</span>
      <span style="display:inline-flex;align-items:center;gap:8px">Exclusive by {kuvani(p=p)}</span>
    </div>
  </div>

  <header class="header">
    <div class="container">
      <a class="brand" href="{home_href}" aria-label="Bincoo MENA home">
        {bincoo(p=p)}
        <span class="brand__divider" aria-hidden="true"></span>
        <span class="brand__meta"><span class="brand__mena">MENA</span></span>
      </a>
      <nav class="nav" aria-label="Primary">{nav}</nav>
      <div class="header__actions">
        <button class="theme-toggle" type="button" data-theme-toggle aria-label="Toggle dark theme" aria-pressed="false">
          <span class="theme-toggle__knob"></span>{I['sun']}{I['moon']}
        </button>
        <a class="btn btn--sm" href="{base}#inquiry">Find a distributor</a>
        <button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span></button>
      </div>
    </div>
  </header>

  <div class="mobile-menu" id="mobile-menu">
    <nav aria-label="Mobile">{nav}<a href="{base}#inquiry">Find a distributor</a></nav>
    <div class="mobile-menu__foot">
      <a href="https://wa.me/{WA}">WhatsApp &middot; {PHONE}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <span>Exclusive by KUVANI &middot; Authorized distributors</span>
    </div>
  </div>
'''

def footer(p="", home=True):
    base = "" if home else p
    cols = "".join(f'<li><a href="{p}products/{x["slug"]}.html">{x["name"]}</a></li>' for x in PRODUCTS)
    return f'''
  <footer class="footer">
    <div class="container">
      <div class="footer__cta">
        <h2 data-split>Bring Bincoo to <em>your business.</em></h2>
        <div class="footer__cta-actions" data-reveal>
          <a class="btn" href="{base}#inquiry">Find a distributor {I['arrow']}</a>
          <a class="btn btn--wa" href="#" data-wa="">{I['wa']} WhatsApp us</a>
        </div>
      </div>
      <div class="footer__grid">
        <div class="footer__brand">
          {bincoo(p=p)}
          <p>The official home of Bincoo in the Middle East &amp; North Africa. Sold through authorized distributors.</p>
          <div class="social">
            <a href="{IG}" target="_blank" rel="noopener" aria-label="Bincoo MENA on Instagram">{I['ig']}</a>
            <a href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{I['wa']}</a>
            <a href="mailto:{EMAIL}" aria-label="Email">{I['mail']}</a>
          </div>
        </div>
        <div><h4>Collection</h4><ul>{cols}</ul></div>
        <div><h4>Company</h4><ul>
          <li><a href="{base}#about">About us</a></li>
          <li><a href="{base}#business">Become a distributor</a></li>
          <li><a href="{base}#process">How it works</a></li>
          <li><a href="{base}#faq">FAQ</a></li>
        </ul></div>
        <div><h4>Contact</h4><ul>
          <li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{IG}" target="_blank" rel="noopener">@bincoo.mena</a></li>
          <li><a href="{IG_KUVANI}" target="_blank" rel="noopener">@kuvani.co</a></li>
        </ul></div>
      </div>
      <div class="footer__bottom">
        <span>&copy; <span data-year>2026</span> Bincoo MENA. All rights reserved.</span>
        <span>Bincoo is a trademark of its respective owner. Prices are retail references in USD.</span>
      </div>
    </div>
    <div class="footer__giant" aria-hidden="true">Bincoo MENA</div>
  </footer>

  <script src="{p}assets/js/main.js?v={V}" defer></script>
  <script src="{p}assets/js/chat.js?v={V}" defer></script>
</body>
</html>
'''

# ---------------------------------------------------------------- home
def home():
    p = ""
    marquee_items = ["Coffee, <em>reimagined</em>", "Smart machines", "Exceptional brewing", "Exclusive by KUVANI", "Middle East &amp; North Africa", "For business <em>only</em>"]
    group = "".join(f'<span class="marquee__item">{t}</span>{I["star"]}' for t in marquee_items)
    cards = "".join(card(pr, i + 1) for i, pr in enumerate(PRODUCTS))
    countries = ["Algeria", "Bahrain", "Egypt", "Iraq", "Jordan", "Kuwait", "Lebanon", "Libya", "Morocco", "Oman", "Palestine", "Qatar", "Saudi Arabia", "Sudan", "Syria", "Tunisia", "United Arab Emirates", "Yemen", "Other"]
    copts = "".join(f"<option>{c}</option>" for c in countries)

    # Hero slider: one slide per machine, each with its own three spec chips
    slides = "".join(
        img(h["image"], p, h["alt"], "hero__slide" + (" is-active" if k == 0 else ""), lazy=False).replace(' fetchpriority="high"', ' fetchpriority="high"' if k == 0 else ' decoding="async"')
        for k, h in enumerate(HERO))
    chips = "".join(
        f'<div class="hero__chips{" is-active" if k == 0 else ""}" aria-hidden="{"false" if k == 0 else "true"}">'
        + "".join(f'<span class="chip chip--{n + 1}"><i{" class=\"red\"" if n == 1 else ""}>{icon}</i>{text}</span>' for n, (icon, text) in enumerate(h["chips"]))
        + "</div>" for k, h in enumerate(HERO))
    dots = "".join(
        f'<button class="hero__dot{" is-active" if k == 0 else ""}" type="button" data-slide="{k}" data-href="products/{h["slug"]}.html" data-name="{h["name"]}" aria-label="Show {h["name"]}" aria-current="{"true" if k == 0 else "false"}">'
        f'<span class="hero__dot-bar"><i></i></span><span class="hero__dot-label">{h["name"]}</span></button>'
        for k, h in enumerate(HERO))

    def chapter(n, flip, photo, photo_alt, tile, tile_alt, eyebrow, title, text, stats, ticks, slug, full):
        st = "".join(f'<div class="stat"><strong>{a}</strong><span>{b}</span></div>' for a, b in stats)
        return f'''
      <article class="chapter{' chapter--flip' if flip else ''}">
        <div class="chapter__media">
          <div class="chapter__photo" data-reveal="clip">{img(photo, p, photo_alt, extra=' data-parallax="0.14"')}</div>
          <div class="chapter__tile" data-reveal="scale" style="--d:.25s">{img(tile, p, tile_alt)}</div>
        </div>
        <div class="chapter__body">
          <span class="chapter__num" aria-hidden="true">{n}</span>
          <span class="eyebrow eyebrow--accent" data-reveal>{eyebrow}</span>
          <h2 class="h2" data-split>{title}</h2>
          <p class="lead" data-reveal>{text}</p>
          <ul class="ticks" data-stagger=".08">{''.join(f'<li data-reveal>{I["tick"]}<span>{t}</span></li>' for t in ticks)}</ul>
          <div class="chapter__stats" data-reveal>{st}</div>
          <div class="chapter__ctas" data-reveal>
            <a class="btn" href="products/{slug}.html">Explore the machine {I['arrow']}</a>
            <a class="btn btn--ghost" href="#" data-wa="{full}">{I['wa']} Find a distributor</a>
          </div>
        </div>
      </article>'''

    chapters = (
        chapter("01", False, "s2-life-white", "Bincoo S2 Pro Trailblazer in white pulling an espresso shot", "s2-black", "S2 Pro Trailblazer in black",
                "S2 Pro Trailblazer &middot; Espresso", "Espresso with <em>true intelligence.</em>",
                "Two ways to control every shot: a 3.4-inch HD touch screen on the machine, or the Bincoo app over Bluetooth. Pressure, temperature, pre-infusion and volume are all yours to tune.",
                [("3&ndash;12<small>bar</small>", "Adjustable extraction pressure"), ("58<small>mm</small>", "Professional thermal group head"), ("88&ndash;96<small>&deg;C</small>", "Extraction temperature")],
                ["Triple pumps and dual instant boilers &mdash; brew and steam at the same time", "4 NTC sensors with PID for rock-steady temperature", "One-touch puck clearing and automatic water supply"],
                "s2-pro-trailblazer", PRODUCTS[0]["full"]) +
        chapter("02", True, "po-life-touch", "Bincoo Automatic Pour-Over machine being operated on a kitchen counter", "po-white", "Automatic Pour-Over in white",
                "Automatic Pour-Over &middot; Grind &amp; Brew", "The pour-over ritual, <em>perfected by machine.</em>",
                "It grinds fresh with a 38&nbsp;mm six-star steel burr, then blooms, pours and drips in precise stages. Build recipes in the Bincoo mini-program and sync them straight to the 4.3-inch screen.",
                [("80", "Grind adjustment steps"), ("4.3<small>&Prime;</small>", "HD IPS touch screen"), ("~3<small>min</small>", "Bean to cup")],
                ["Adjustable 60&ndash;120 RPM grinding with plasma static elimination", "Coffee, tea and hot water from one machine", "All-metal body, food-grade glass dripper and carafe"],
                "automatic-pour-over", PRODUCTS[1]["full"]) +
        chapter("03", False, "cp-life-dark", "Bincoo Composer PO01 brewing pour-over coffee beside an iced coffee", "cp-black", "Composer PO01 in black",
                "Composer PO01 &middot; Automatic Pour-Over", "Hand-pour craft, <em>on repeat.</em>",
                "Composer PO01 automates the techniques baristas pour by hand &mdash; one-pour, three-stage and the four-to-six method &mdash; with PID heating that holds temperature from the first drop to the last.",
                [("40&ndash;95<small>&deg;C</small>", "PID heating range"), ("6", "Preset brewing modes"), ("1:16", "Default brew ratio")],
                ["Automatic water supply &mdash; connect a water line for non-stop service", "Touch panel plus Bluetooth mini-program control", "Magnetic drip tray and conical filter cup for easy cleaning"],
                "composer-po01", PRODUCTS[2]["full"])
    )

    gallery = [("s2-life-espresso", "S2 Pro Trailblazer", "Espresso"), ("po-life-kitchen", "Automatic Pour-Over", "Home office"),
               ("cp-duo", "Composer PO01", "Duo service"), ("s2-life-steam", "S2 Pro Trailblazer", "Steam"),
               ("po-life-counter", "Automatic Pour-Over", "Counter"), ("cp-life-white", "Composer PO01", "Café bar"),
               ("s2-life-portafilter", "S2 Pro Trailblazer", "58 mm"), ("po-life-beans", "Automatic Pour-Over", "Fresh ground")]
    hitems = "".join(f'<figure class="hscroll__item">{img(n, p, f"{a} — {b}")}<figcaption>{a}<span>{b}</span></figcaption></figure>' for n, a, b in gallery)

    segs = [("cup", "Caf&eacute;s &amp; roasteries", "Consistent espresso and pour-over that keep pace with a busy bar, shift after shift."),
            ("bell", "Hotels &amp; restaurants", "Barista-quality coffee for lobbies, suites, breakfast service and fine dining."),
            ("office", "Offices &amp; workspaces", "Smart, intuitive machines that make great coffee an everyday perk for your team."),
            ("store", "Retailers &amp; distributors", "Stock official Bincoo machines with direct support from the regional distributor.")]
    segments = "".join(f'<article class="segment" data-reveal><span class="segment__icon">{I[i]}</span><h3>{t}</h3><p>{d}</p></article>' for i, t, d in segs)

    bens = [("Exclusive regional partner", "KUVANI is Bincoo&rsquo;s exclusive partner for the Middle East &amp; North Africa &mdash; you&rsquo;re buying from the source."),
            ("Partner pricing", "Distributor terms shaped around your market, product mix and volumes &mdash; not a one-size retail price."),
            ("A direct line to our team", "Talk to real people on WhatsApp or email. Fast answers, clear terms, no call centres."),
            ("Regional focus", "Dedicated to the Middle East &amp; North Africa, from the Gulf and the Levant to North Africa."),
            ("Genuine Bincoo products", "Official machines exactly as the brand designed them, supplied through the authorised channel."),
            ("Distributor-led, by design", "No direct sales to end customers &mdash; every purchase goes through an authorized distributor in your market.")]
    benefits = "".join(f'<div class="benefit" data-reveal><b>0{k+1}</b><h3>{t}</h3><p>{d}</p></div>' for k, (t, d) in enumerate(bens))

    steps_data = [("Get in touch", "Tell us your country and what you&rsquo;re looking for &mdash; buying, or becoming a distributor."),
                  ("Meet your distributor", "We connect you with the authorized Bincoo distributor for your market."),
                  ("Get pricing &amp; availability", "Your distributor shares final pricing, availability and delivery for your order."),
                  ("Start brewing", "Set up with support from your distributor, backed by our regional team.")]
    steps = "".join(f'<div class="step" data-reveal><span class="step__n">0{k+1}</span><h3>{t}</h3><p>{d}</p></div>' for k, (t, d) in enumerate(steps_data))

    faqs = FAQS
    faq_html = "".join(f'<details data-reveal><summary>{q}<i aria-hidden="true"></i></summary><div class="faq__a"><p>{a}</p></div></details>' for q, a in faqs)

    checks = "".join(f'''<div class="check"><input type="checkbox" id="pr-{x["value"]}" name="products" value="{x["value"]}" data-label="{x["name"]}"><label for="pr-{x["value"]}">{x["name"]}<small>{x["cat"]}</small></label></div>''' for x in PRODUCTS)

    jsonld = {"@context": "https://schema.org", "@type": "Organization", "name": "Bincoo MENA", "url": DOMAIN + "/",
              "logo": DOMAIN + "/assets/img/brand/bincoo-color.svg", "email": EMAIL, "telephone": PHONE,
              "description": "Official Bincoo distributor for the Middle East & North Africa, exclusive by KUVANI. Sold through authorized distributors.",
              "sameAs": [IG], "areaServed": "Middle East and North Africa",
              "parentOrganization": {"@type": "Organization", "name": "KUVANI"}}

    html = head("Bincoo MENA — Official Bincoo Smart Coffee Machines | Exclusive by KUVANI",
                "The official home of Bincoo in the Middle East & North Africa, exclusive by KUVANI. Smart espresso and pour-over machines, available through authorized distributors.",
                "", p, jsonld=jsonld)
    html += header(p, True)
    html += f'''
  <main id="main">
    <!-- Hero -->
    <section class="hero">
      <div class="container hero__grid">
        <div class="hero__copy">
          <span class="eyebrow eyebrow--accent" data-intro style="--d:.1s">Official Bincoo &middot; Middle East &amp; North Africa</span>
          <h1 class="hero__title" data-split>Coffee, <em>reimagined</em><br>for the region.</h1>
          <p class="lead" data-intro style="--d:.55s">Bincoo&rsquo;s smart espresso and pour-over machines are now available across the Middle East &amp; North Africa &mdash; exclusively through KUVANI and a network of authorized distributors in each market.</p>
          <div class="hero__ctas" data-intro style="--d:.7s">
            <a class="btn" href="#collection">Explore the collection {I['arrow']}</a>
            <a class="btn btn--ghost" href="#inquiry">Find a distributor</a>
          </div>
          <div class="hero__meta" data-intro style="--d:.85s">
            <div><strong>3</strong><span>Flagship machines</span></div>
            <div><strong>Official</strong><span>Authorized distributors</span></div>
            <div><strong>MENA</strong><span>Regional coverage</span></div>
          </div>
        </div>
        <div class="hero__visual" data-intro style="--d:.2s">
          <span class="hero__watermark" aria-hidden="true">Bincoo</span>
          <div class="hero__tile">
            <div class="hero__slides" data-parallax="0.06">{slides}</div>
            <a class="hero__tile-link" href="products/{HERO[0]['slug']}.html" aria-label="View {HERO[0]['name']}"></a>
          </div>
          {chips}
          <div class="hero__nav" aria-label="Featured machines">{dots}</div>
          <div class="hero__badge" aria-label="Exclusive by KUVANI">
            <svg class="ring" viewBox="0 0 100 100" aria-hidden="true"><defs><path id="ring-path" d="M50 50m-38 0a38 38 0 1 1 76 0a38 38 0 1 1-76 0"/></defs><text><textPath href="#ring-path" textLength="236" lengthAdjust="spacing">Exclusive by Kuvani &middot; Official Bincoo &middot;</textPath></text></svg>
            {kuvani(p=p)}
          </div>
        </div>
      </div>
      <div class="container"><a class="scroll-cue" href="#collection" data-intro style="--d:1s"><span></span>Scroll to discover</a></div>
    </section>

    <div class="marquee" aria-hidden="true"><div class="marquee__track"><div class="marquee__group">{group}</div><div class="marquee__group">{group}</div></div></div>

    <!-- Collection -->
    <section class="section" id="collection">
      <div class="container">
        <div class="section-head section-head--split">
          <div style="display:grid;gap:22px">
            <span class="eyebrow" data-reveal>The collection</span>
            <h2 data-split>Three machines. <em>One standard</em> of precision.</h2>
          </div>
          <p class="lead" data-reveal>Our launch line-up brings Bincoo&rsquo;s most advanced brewers to the region &mdash; from dual-boiler espresso to fully automatic pour-over. Prices are retail references; final pricing is set by the authorized distributor in each market.</p>
        </div>
        <div class="products-grid" data-stagger=".12">{cards}
        </div>
      </div>
    </section>

    <!-- Chapters -->
    <section class="section section--alt" id="machines">
      <div class="container">
        <div class="section-head section-head--center">
          <span class="eyebrow" data-reveal>Inside the machines</span>
          <h2 data-split>Engineered for the <em>perfect cup.</em></h2>
        </div>
        {chapters}
      </div>
    </section>

    <!-- Spec band -->
    <section class="section--tight">
      <div class="container">
        <div class="specband" data-stagger=".1">
          <div class="specband__item" data-reveal><em>S2 Pro</em><strong><span data-count="58">58</span><small>mm</small></strong><span>Professional thermal group head</span></div>
          <div class="specband__item" data-reveal><em>S2 Pro</em><strong><span data-count="12">12</span><small>bar</small></strong><span>Maximum adjustable extraction pressure</span></div>
          <div class="specband__item" data-reveal><em>Pour-Over</em><strong><span data-count="80">80</span><small>steps</small></strong><span>Grind adjustment with a 38&nbsp;mm burr</span></div>
          <div class="specband__item" data-reveal><em>Composer</em><strong><span data-count="95">95</span><small>&deg;C</small></strong><span>Instant PID heating, from 40&nbsp;&deg;C</span></div>
        </div>
      </div>
    </section>

    <!-- Horizontal gallery -->
    <section class="hscroll" aria-label="Gallery">
      <div class="hscroll__sticky">
        <div class="container"><div class="section-head" style="margin-bottom:0">
          <span class="eyebrow" data-reveal>In the wild</span>
          <h2 data-split>Made for <em>every counter.</em></h2>
        </div></div>
        <div class="hscroll__track">{hitems}</div>
      </div>
    </section>

    <!-- Business -->
    <section class="section" id="business">
      <div class="container">
        <div class="b2b-banner" data-reveal="scale">
          <div style="display:grid;gap:22px">
            <span class="eyebrow">Become a distributor</span>
            <h2 data-split>Grow with Bincoo in <em>your market.</em></h2>
          </div>
          <div style="display:grid;gap:26px">
            <p>Bincoo MENA appoints authorized distributors across the Middle East &amp; North Africa. If you&rsquo;re a distributor, retailer or equipment supplier, talk to us about representing Bincoo in your country.</p>
            <div style="display:flex;flex-wrap:wrap;gap:12px">
              <a class="btn" href="#inquiry">Become a distributor {I['arrow']}</a>
              <a class="btn btn--ghost" href="#" data-mail="">{I['mail']} Email our team</a>
            </div>
          </div>
        </div>
        <div class="segments" data-stagger=".1">{segments}</div>

        <div class="section-head section-head--split" style="margin-top:clamp(90px,12vw,150px)">
          <div style="display:grid;gap:22px">
            <span class="eyebrow" data-reveal>Why Bincoo MENA</span>
            <h2 data-split>A partner, <em>not a checkout.</em></h2>
          </div>
          <p class="lead" data-reveal>Every account is handled personally by our team &mdash; from the first inquiry to delivery and beyond.</p>
        </div>
        <div class="benefits" data-stagger=".08">{benefits}</div>
      </div>
    </section>

    <!-- About -->
    <section class="section section--alt" id="about">
      <div class="container about">
        <div class="about__media">
          <div class="photo" data-reveal="clip">{img("s2-life-pitcher", p, "Barista steaming milk beside the Bincoo S2 Pro Trailblazer", extra=' data-parallax="0.1"')}</div>
          <div class="about__card" data-reveal style="--d:.3s">
            {kuvani(p=p)}
            <p>Exclusive partner of Bincoo for the Middle East &amp; North Africa.</p>
          </div>
        </div>
        <div class="about__body">
          <span class="eyebrow" data-reveal>About us</span>
          <h2 data-split>The official home of Bincoo <em>in the region.</em></h2>
          <p class="lead" data-reveal>Bincoo designs smart coffee machines and brewing tools that let everyone who loves coffee become their own barista. Bincoo MENA brings that range to the Middle East &amp; North Africa &mdash; operated exclusively by KUVANI.</p>
          <p class="lead" data-reveal>We don&rsquo;t sell directly to end customers. Bincoo MENA works through authorized distributors in each market, backing them with genuine Bincoo machines, partner pricing and hands-on support.</p>
          <div class="notice" data-reveal>{I['briefcase']}<div><strong>Sold through authorized distributors</strong><p>Bincoo MENA does not sell directly to individuals or end customers. Contact us to find the authorized distributor in your market, or to become one.</p></div></div>
          <blockquote class="quote" data-reveal>&ldquo;Coffee, reimagined. Smart machines. Exceptional brewing.&rdquo;<cite>Bincoo MENA</cite></blockquote>
        </div>
      </div>
    </section>

    <!-- Process -->
    <section class="section" id="process">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow" data-reveal>How it works</span>
          <h2 data-split>From inquiry to <em>first pour.</em></h2>
        </div>
        <div class="steps" data-stagger=".12">{steps}</div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="section section--alt" id="faq">
      <div class="container faq">
        <div class="section-head" style="margin-bottom:0">
          <span class="eyebrow" data-reveal>FAQ</span>
          <h2 data-split>Good to <em>know.</em></h2>
          <p class="lead" data-reveal>Can&rsquo;t find what you&rsquo;re looking for? Message us on WhatsApp and we&rsquo;ll get back to you.</p>
          <div data-reveal><a class="btn btn--wa" href="#" data-wa="">{I['wa']} Ask on WhatsApp</a></div>
        </div>
        <div class="faq__list" data-stagger=".06">{faq_html}</div>
      </div>
    </section>

    <!-- Inquiry -->
    <section class="section" id="inquiry">
      <div class="container inquiry">
        <aside class="inquiry__aside">
          <span class="eyebrow" data-reveal>Contact</span>
          <h2 data-split>Let&rsquo;s get <em>in touch.</em></h2>
          <p class="lead" data-reveal>Looking for Bincoo in your country, or want to become an authorized distributor? Tell us a little about you and our team will get back to you.</p>
          <div class="contact-list" data-stagger=".08">
            <a class="contact-item" data-reveal href="https://wa.me/{WA}" target="_blank" rel="noopener"><span class="contact-item__icon" style="color:#1f8f4e">{I['wa']}</span><span><small>WhatsApp</small><strong>{PHONE}</strong></span>{I['arrow_ur']}</a>
            <a class="contact-item" data-reveal href="tel:+{WA}"><span class="contact-item__icon">{I['phone']}</span><span><small>Call us</small><strong>{PHONE}</strong></span>{I['arrow_ur']}</a>
            <a class="contact-item" data-reveal href="mailto:{EMAIL}"><span class="contact-item__icon">{I['mail']}</span><span><small>Email</small><strong>{EMAIL}</strong></span>{I['arrow_ur']}</a>
            <a class="contact-item" data-reveal href="{IG}" target="_blank" rel="noopener"><span class="contact-item__icon">{I['ig']}</span><span><small>Instagram</small><strong>@bincoo.mena</strong></span>{I['arrow_ur']}</a>
          </div>
        </aside>

        <form class="form" id="inquiry-form" novalidate data-reveal="scale">
          <div class="form__head">
            <h3>Contact our team</h3>
            <p class="muted">Fill in your details, then send via WhatsApp or email &mdash; your message is prepared automatically.</p>
          </div>
          <div class="form__grid">
            <div class="field"><label for="f-company">Company</label><input class="input" id="f-company" name="company" autocomplete="organization" placeholder="Your company (optional)"></div>
            <div class="field"><label for="f-name">Your name <span class="req">*</span></label><input class="input" id="f-name" name="name" autocomplete="name" required placeholder="Full name"><span class="field__error">Please enter your name.</span></div>
            <div class="field"><label for="f-type">I&rsquo;m interested in</label><select class="select" id="f-type" name="type"><option value="">Select&hellip;</option><option>Finding where to buy in my country</option><option>Becoming an authorized distributor</option><option>Something else</option></select></div>
            <div class="field"><label for="f-country">Country <span class="req">*</span></label><select class="select" id="f-country" name="country" required><option value="">Select&hellip;</option>{copts}</select><span class="field__error">Please choose your country.</span></div>
            <div class="field"><label for="f-email">Email <span class="req">*</span></label><input class="input" id="f-email" name="email" type="email" autocomplete="email" required placeholder="name@company.com"><span class="field__error">Please enter a valid email.</span></div>
            <div class="field"><label for="f-phone">Phone / WhatsApp <span class="req">*</span></label><input class="input" id="f-phone" name="phone" type="tel" autocomplete="tel" required placeholder="+974 ..."><span class="field__error">Please enter a phone number.</span></div>
            <fieldset class="field field--full"><legend>Machines of interest</legend><div class="checks" style="margin-top:8px">{checks}</div></fieldset>
            <div class="field field--full"><label for="f-qty">Estimated quantity</label><input class="input" id="f-qty" name="quantity" placeholder="e.g. 6 &times; S2 Pro (black), 2 &times; Composer PO01"></div>
            <div class="field field--full"><label for="f-msg">Message</label><textarea class="textarea" id="f-msg" name="message" placeholder="Tell us about your venue, timeline or any questions."></textarea></div>
          </div>
          <div class="form__actions">
            <button class="btn btn--wa" type="submit">{I['wa']} Send via WhatsApp</button>
            <button class="btn btn--ghost" type="button" data-send-email>{I['mail']} Send via email</button>
          </div>
          <p class="form__status" role="status" aria-live="polite"></p>
          <p class="form__note">We&rsquo;ll connect you with the authorized distributor in your market. Your details are used solely to reply to your request.</p>
        </form>
      </div>
    </section>
  </main>
'''
    html += footer(p, True)
    return html

# ---------------------------------------------------------------- product pages
PDP = {
 "s2-pro-trailblazer": dict(
    desc="Bincoo S2 Pro Trailblazer smart espresso machine: 3.4\" touch screen and Bluetooth app control, triple pumps with dual instant boilers, 58 mm group head and 3–12 bar pressure profiling. Available through authorized distributors in MENA.",
    lead="A dual-control espresso machine with a 3.4-inch HD touch screen and Bluetooth app, triple pumps and dual instant boilers, a 58&nbsp;mm professional group head and fully adjustable pressure, temperature and flow.",
    thumbs=[("s2-black", "contain", "S2 Pro Trailblazer in black"), ("s2-white", "contain", "S2 Pro Trailblazer in white"),
            ("s2-bundle-black", "contain", "S2 Pro with DM02 grinder, black"), ("s2-bundle-white", "contain", "S2 Pro with DM02 grinder, white"),
            ("s2-life-espresso", "cover", "S2 Pro pulling a shot on a bar counter"), ("s2-life-white", "cover", "S2 Pro in white with steam"),
            ("s2-life-pitcher", "cover", "Steaming milk with the S2 Pro"), ("s2-life-portafilter", "cover", "58 mm portafilter detail"),
            ("s2-life-steam", "cover", "S2 Pro steam in action"), ("s2-app", "cover", "Touch screen and mobile app control"),
            ("s2-cutaway", "cover", "Thermal group head cutaway"), ("s2-life-grinder", "cover", "S2 Pro with grinder at home")],
    colors=[("Black", "s2-black"), ("White", "s2-white")],
    configs=[("Machine only", "$2,200", None), ("Machine + DM02 grinder", "On request", "s2-bundle-{color}")],
    keyfacts=[("Control", "3.4&Prime; touch screen + app"), ("Pressure", "3&ndash;12 bar, adjustable"), ("Group head", "58 mm thermal"), ("Boilers", "Triple pumps, dual instant")],
    features=[
      ("s2-app", "Dual control. <em>True intelligence.</em>", "A 3.4-inch HD touch screen plus a direct Bluetooth connection to the Bincoo app. Set mode, temperature, water volume and pressure with a slide of the finger &mdash; every parameter at a glance.",
       ["Screen settings on the machine or in the app", "Save and reuse your favourite recipes"]),
      ("s2-life-pitcher", "Five functions, <em>every drink.</em>", "Hot extraction, variable-pressure extraction, cold extraction, automatic puck clearing and steam. Hot coffee in the morning, iced drinks in summer and every milk-based favourite in between.",
       ["Cold extraction for iced menus", "Variable-pressure profiles for specialty beans"]),
      ("s2-life-portafilter", "58 mm professional <em>group head.</em>", "A self-developed thermal group head with constant-temperature balance pushes an even column of water through the puck &mdash; richer oils and caf&eacute;-grade espresso, shot after shot.",
       ["4 NTC sensors + PID temperature control", "88&ndash;96 &deg;C extraction temperature"]),
      ("s2-life-steam", "Brew and steam <em>at the same time.</em>", "Three pumps and two instant boilers run independently, so extraction and milk frothing happen simultaneously &mdash; no waiting between steps, even at peak hours.",
       ["Live steering lever, adjustable as you wish", "Faster service for milk-based drinks"]),
      ("s2-life-grinder", "Automatic water, <em>effortless service.</em>", "Connect bottled water or an external supply and skip manual refilling &mdash; built for high-frequency use. One-touch puck clearing keeps hands and counter clean.",
       ["External water inlet supported", "One-touch puck clearing after every shot"]),
    ],
    specs=[("Functions", "Hot extraction &middot; Variable-pressure extraction &middot; Cold extraction &middot; Automatic puck clearing &middot; Steam"),
           ("Control", "3.4&Prime; HD touch screen + Bluetooth app (dual control)"),
           ("Temperature control", "4 NTC sensors + PID"),
           ("Pumps / boilers", "Triple pumps &middot; dual instant (tankless) boilers"),
           ("Extraction pressure", "3&ndash;12 bar, adjustable"),
           ("Extraction temperature", "88&ndash;96 &deg;C"),
           ("Pre-infusion time", "1&ndash;10 s"),
           ("Extraction volume", "10&ndash;150 ml"),
           ("Group head", "58 mm thermal group head"),
           ("Water supply", "Automatic &mdash; external water inlet supported"),
           ("Rated power", "2600 W"),
           ("Voltage", "220 V ~ 50 Hz"),
           ("Dimensions (L &times; W &times; H)", "300 &times; 340 &times; 339 mm"),
           ("Net weight", "11 kg"),
           ("Materials", "304 stainless steel, plastic, silicone"),
           ("Colours", "Black &middot; White"),
           ("Bundle option", "With DM02 electric bean grinder")],
    recipes=None),
 "automatic-pour-over": dict(
    desc="Bincoo Fully Automatic Smart Pour-Over Coffee Machine: built-in 38 mm burr grinder with 80 settings, 4.3\" HD touch screen, custom recipes and multi-stage pouring. Available through authorized distributors in MENA.",
    lead="A fully automatic grind-and-brew pour-over machine. A 38&nbsp;mm six-star steel burr grinds fresh, then multi-stage water flow blooms, pours and drips with barista precision &mdash; controlled from a 4.3-inch HD touch screen.",
    thumbs=[("po-black", "contain", "Automatic Pour-Over in black"), ("po-white", "contain", "Automatic Pour-Over in white"),
            ("po-life-touch", "cover", "Selecting a recipe on the touch screen"), ("po-life-beans", "cover", "Adding beans to the hopper"),
            ("po-life-counter", "cover", "Automatic Pour-Over on a wooden counter"), ("po-life-kitchen", "cover", "Automatic Pour-Over in a home kitchen")],
    colors=[("Black", "po-black"), ("White", "po-white")],
    configs=None,
    keyfacts=[("Grinder", "38 mm six-star steel burr"), ("Grind settings", "80 steps, 60&ndash;120 RPM"), ("Display", "4.3&Prime; HD IPS touch screen"), ("Drinks", "Coffee &middot; Tea &middot; Hot water")],
    features=[
      ("po-life-touch", "Barista precision, <em>without the guesswork.</em>", "Multi-stage water flow control replicates professional pour-over technique, ensuring even saturation and optimal extraction every time. One touch, and the machine handles blooming, pouring and dripping.",
       ["Adjust water temperature, flow rate and brew time", "Preset recipes for different bean profiles"]),
      ("po-life-beans", "Fresh-ground, <em>every single cup.</em>", "A professional grinding system with a 38&nbsp;mm six-star steel core, 80 grind settings and adjustable 60&ndash;120 RPM speed. Plasma static elimination keeps grounds clean and the chamber tidy.",
       ["80-step grind adjustability", "Plasma static elimination technology"]),
      ("po-life-counter", "Your recipe, <em>synced.</em>", "Create a recipe in the Bincoo mini-program, set your parameters and sync it to the machine. Rinse the filter, add beans, choose the recipe and start &mdash; great coffee in about three minutes.",
       ["Recipe management in the Bincoo mini-program", "50 fps responsive, lag-free touch screen"]),
      ("po-life-kitchen", "Coffee, tea, hot water &mdash; <em>one machine.</em>", "A full barista station in one compact, all-metal body: no separate grinders, kettles or pour-over tools needed. Stainless steel base, food-grade glass dripper and carafe.",
       ["All-metal, anti-deformation construction", "Compact 22 &times; 16 cm footprint"]),
    ],
    specs=[("Brewing", "Fully automatic grind &amp; brew pour-over &mdash; blooming, pouring, dripping"),
           ("Display", "4.3&Prime; HD IPS touch screen, 50 fps"),
           ("Grinder", "38 mm six-star steel burr core"),
           ("Grind adjustment", "80 steps"),
           ("Grinder speed", "60&ndash;120 RPM, adjustable"),
           ("Anti-static", "Plasma static elimination"),
           ("Drinks", "Coffee &middot; Tea &middot; Hot water"),
           ("Adjustable parameters", "Water temperature, flow rate, brew time, volume, strength"),
           ("Recipes", "Presets + custom recipes via Bincoo mini-program"),
           ("Construction", "All-metal body &middot; stainless steel base &middot; food-grade glass dripper and carafe"),
           ("Voltage", "220 V ~ 50 Hz"),
           ("Heating power", "1130 W"),
           ("Grinding power", "30 W"),
           ("Dimensions (L &times; W &times; H)", "22 &times; 16 &times; 36 cm"),
           ("Net weight", "11.7 kg"),
           ("Package", "32 &times; 26 &times; 46 cm &middot; 12 kg"),
           ("Colours", "Black &middot; White")],
    recipes=None),
 "composer-po01": dict(
    desc="Bincoo Composer PO01 automatic pour-over coffee maker: PID heating 40–95 °C, six brewing modes, three professional pour techniques and automatic water supply. Available through authorized distributors in MENA.",
    lead="An automatic pour-over brewer that reproduces professional hand-pour techniques. PID heating from 40&ndash;95&nbsp;&deg;C, six preset brewing modes, a dynamic brewing system and automatic water supply for non-stop service.",
    thumbs=[("cp-black", "contain", "Composer PO01 in black"), ("cp-life-dark", "cover", "Composer PO01 in black on a café counter"),
            ("cp-life-white", "cover", "Composer PO01 in white on a café counter"), ("cp-duo", "cover", "Composer PO01 in black and white")],
    colors=[("Black", "cp-black"), ("White", "cp-life-white")],
    configs=None,
    keyfacts=[("Heating", "PID, 40&ndash;95 &deg;C"), ("Brewing modes", "6 presets"), ("Techniques", "One-pour &middot; Three-stage &middot; 4:6"), ("Water", "Automatic supply")],
    features=[
      ("cp-life-dark", "Precise temperature, <em>every moment.</em>", "A PID intelligent algorithm adjusts in milliseconds, holding water temperature constant from 40 to 95&nbsp;&deg;C. Stable output makes every extraction just right.",
       ["Instant heating &mdash; no waiting", "Dynamic brewing system for even extraction"]),
      ("cp-duo", "Three pour techniques, <em>endless flavour.</em>", "One-pour, three-stage and the four-to-six method &mdash; each controls water rhythm and extraction time differently, adapting to every bean for a rich, full-bodied cup.",
       ["Six preset modes on the touch panel", "Dual control via Bluetooth mini-program"]),
      ("cp-life-white", "Free-flowing, <em>non-stop coffee.</em>", "Connect an external pressureless water line and say goodbye to frequent refills &mdash; ideal for studios, offices and busy service. A magnetic drip tray and conical filter cup keep cleaning simple.",
       ["Automatic water supply", "Magnetic, easy-to-clean water tray"]),
    ],
    specs=[("Type", "Automatic pour-over (drip) coffee machine"),
           ("Temperature control", "PID, 40&ndash;95 &deg;C instant heating"),
           ("Brewing modes", "6 presets on the touch panel"),
           ("Pour techniques", "One-pour &middot; Three-stage &middot; Four-to-six method"),
           ("Default recipe", "15 g coffee &middot; 92 &deg;C &middot; 1:16 ratio &middot; 240 ml"),
           ("Control", "Sensitive touch panel + Bluetooth mini-program"),
           ("Brewing system", "Dynamic brewing system"),
           ("Water supply", "Automatic, via external pressureless water line"),
           ("Details", "Conical filter cup &middot; Magnetic water tray"),
           ("Colours", "Black &middot; White")],
    recipes=[("One-pour", "15 g &middot; 92 &deg;C &middot; 1:16 &middot; 240 ml", "After blooming, the remaining water is poured in one go.", "Clean, clear and balanced &mdash; for medium to dark roasts."),
             ("Three-stage", "15 g &middot; 92 &deg;C &middot; 1:16 &middot; 240 ml", "After blooming, water is poured in three stages.", "More layered cup &mdash; for light to medium roasts."),
             ("Four-to-six", "15 g &middot; 92 &deg;C &middot; 1:16 &middot; 240 ml", "After blooming, the remaining water is divided into four pours.", "High sweetness and body &mdash; for advanced brewers, light to medium roasts.")]),
}

def product_page(slug):
    pr = BY_SLUG[slug]; d = PDP[slug]; p = "../"
    thumbs = "".join(
        f'<button class="thumb{" is-active" if k == 0 else ""}" type="button" data-full="{p}assets/img/products/{n}.webp" data-fit="{fit}" data-alt="{alt}" aria-label="Show image: {alt}">'
        f'<img src="{p}assets/img/products/{n}.webp" alt="" loading="lazy" decoding="async"{" class=\"contain\"" if fit == "contain" else ""}></button>'
        for k, (n, fit, alt) in enumerate(d["thumbs"]))
    first = d["thumbs"][0]
    colors = "".join(f'<button class="pill" type="button" data-value="{c}" data-image="{p}assets/img/products/{im}.webp" aria-pressed="{"true" if k == 0 else "false"}"><span class="swatch swatch--{c.lower()}"></span>{c}</button>' for k, (c, im) in enumerate(d["colors"]))
    configs = ""
    if d["configs"]:
        pills = "".join(f'<button class="pill pill--text" type="button" data-value="{c}" data-price="{pz}"{f' data-image-template="{p}assets/img/products/{tpl}.webp"' if tpl else ''} aria-pressed="{"true" if k == 0 else "false"}">{c} <small data-price>{pz}</small></button>' for k, (c, pz, tpl) in enumerate(d["configs"]))
        configs = f'<div class="opt" data-option="config"><span class="opt__label">Configuration <span data-option-value="config"></span></span><div class="opt__row">{pills}</div></div>'
    keyfacts = "".join(f'<div><small>{a}</small><strong>{b}</strong></div>' for a, b in d["keyfacts"])
    feats = "".join(f'''
        <article class="feature">
          <div class="feature__media{' feature__media--portrait' if k % 2 else ''}" data-reveal="clip">{img(im, p, '', extra=' data-parallax="0.1"')}</div>
          <div class="feature__body">
            <span class="feature__n" data-reveal>0{k+1}</span>
            <h2 class="h2" data-split>{t}</h2>
            <p class="lead" data-reveal>{txt}</p>
            <ul class="ticks" data-stagger=".08">{''.join(f'<li data-reveal>{I["tick"]}<span>{x}</span></li>' for x in ticks)}</ul>
          </div>
        </article>''' for k, (im, t, txt, ticks) in enumerate(d["features"]))
    specs = "".join(f"<tr><th scope=\"row\">{a}</th><td>{b}</td></tr>" for a, b in d["specs"])
    recipes = ""
    if d["recipes"]:
        rows = "".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td>{e}</td></tr>' for a, b, c, e in d["recipes"])
        recipes = f'''
    <section class="section--tight">
      <div class="container">
        <div class="section-head"><span class="eyebrow" data-reveal>Brewing methods</span><h2 data-split>Three techniques, <em>built in.</em></h2></div>
        <div class="table-wrap" data-reveal><table class="recipes"><thead><tr><th>Method</th><th>Default parameters</th><th>How it brews</th><th>Best for</th></tr></thead><tbody>{rows}</tbody></table></div>
      </div>
    </section>'''
    others = [x for x in PRODUCTS if x["slug"] != slug]
    related = "".join(card(x, PRODUCTS.index(x) + 1, p) for x in others)
    price_val = d["configs"][0][1] if d["configs"] else pr["price"]

    jsonld = {"@context": "https://schema.org", "@type": "Product", "name": pr["full"], "brand": {"@type": "Brand", "name": "Bincoo"},
              "image": [f"{DOMAIN}/assets/img/products/{n}.webp" for n, _, _ in d["thumbs"][:4]],
              "description": d["desc"], "category": pr["cat"].replace("&amp;", "&"),
              "url": f"{DOMAIN}/products/{slug}.html"}

    html = head(f"{pr['full']} | Bincoo MENA", d["desc"], f"products/{slug}.html", p,
                og=f"assets/img/products/{pr['main']}.webp", jsonld=jsonld)
    html += header(p, False)
    html += f'''
  <main id="main">
    <div class="container">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a><span aria-hidden="true">/</span><a href="../#collection">Collection</a><span aria-hidden="true">/</span><span aria-current="page">{pr['name']}</span></nav>
      <section class="pdp" data-pdp="{pr['full']}">
        <div class="gallery" data-reveal="fade">
          <div class="gallery__main">
            <img src="{p}assets/img/products/{first[0]}.webp" alt="{first[2]}" fetchpriority="high"{' class="is-cover"' if first[1] == 'cover' else ''}>
            <button class="gallery__zoom" type="button" aria-label="View full screen">{I['zoom']}</button>
          </div>
          <div class="gallery__thumbs">{thumbs}</div>
        </div>
        <div class="pdp__info">
          <span class="eyebrow eyebrow--accent" data-reveal>{pr['cat']}</span>
          <h1 class="pdp__title" data-split>{pr['title_html']}</h1>
          <p class="lead" data-reveal>{d['lead']}</p>
          <div class="pdp__price" data-reveal>
            <small data-price>Retail reference (USD)</small>
            <strong data-price data-price-value>{price_val}</strong>
            <span class="trade">Final pricing from the authorized distributor in your market</span>
          </div>
          <div class="opt" data-option="color" data-reveal><span class="opt__label">Colour <span data-option-value="color"></span></span><div class="opt__row">{colors}</div></div>
          {configs}
          <div class="pdp__ctas" data-reveal>
            <a class="btn btn--wa" href="https://wa.me/{WA}" data-quote-wa>{I['wa']} Find a distributor on WhatsApp</a>
            <a class="btn btn--ghost" href="mailto:{EMAIL}" data-quote-mail>{I['mail']} Email us</a>
            <a class="btn btn--ghost" href="../?product={pr['value']}#inquiry">Contact form</a>
          </div>
          <div class="assure" data-reveal>
            <div>{I['shield']}<strong>Official Bincoo</strong>Genuine product via the exclusive MENA partner.</div>
            <div>{I['tag']}<strong>Authorized distributors</strong>Buy through the official distributor in your market.</div>
            <div>{I['briefcase']}<strong>Direct line</strong>Questions? Our team answers on WhatsApp.</div>
          </div>
          <div class="keyfacts" data-reveal>{keyfacts}</div>
        </div>
      </section>
    </div>

    <section class="section section--alt">
      <div class="container">
        <div class="section-head section-head--center"><span class="eyebrow" data-reveal>Highlights</span><h2 data-split>Designed to <em>impress.</em> Built to <em>perform.</em></h2></div>
        <div class="features">{feats}
        </div>
      </div>
    </section>
    {recipes}
    <section class="section" id="specs">
      <div class="container specs">
        <div class="section-head" style="margin-bottom:0">
          <span class="eyebrow" data-reveal>Specifications</span>
          <h2 data-split>Every <em>detail.</em></h2>
          <p class="lead" data-reveal>Technical data as published by Bincoo. Your distributor can confirm the requirements for your market.</p>
          <div data-reveal><a class="btn" href="#" data-wa="{pr['full']}">{I['wa']} Ask about this machine</a></div>
        </div>
        <div class="table-wrap" data-reveal><table class="spec-table"><tbody>{specs}</tbody></table></div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="section-head"><span class="eyebrow" data-reveal>Also in the collection</span><h2 data-split>Complete your <em>line-up.</em></h2></div>
        <div class="products-grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr))" data-stagger=".12">{related}</div>
      </div>
    </section>
  </main>

  <div class="lightbox" role="dialog" aria-modal="true" aria-label="Image viewer" aria-hidden="true">
    <img src="data:," alt="">
    <button class="lightbox__close" type="button" aria-label="Close">{I['close']}</button>
    <button class="lightbox__nav lightbox__nav--prev" type="button" aria-label="Previous image">{I['prev']}</button>
    <button class="lightbox__nav lightbox__nav--next" type="button" aria-label="Next image">{I['next']}</button>
  </div>
'''
    html += footer(p, False)
    return html

def notfound():
    p = "/"
    html = head("Page not found | Bincoo MENA", "The page you are looking for could not be found.", "404.html", p)
    html = html.replace('<meta name="description"', '<meta name="robots" content="noindex">\n  <meta name="description"')
    html += header(p, False)
    html += f'''
  <main id="main">
    <section class="container notfound">
      <div style="display:grid;gap:24px;justify-items:center">
        <span class="giant" aria-hidden="true">404</span>
        <h1 class="h2">This page has <em>brewed away.</em></h1>
        <p class="lead">The page you&rsquo;re looking for doesn&rsquo;t exist or has moved.</p>
        <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center"><a class="btn" href="/">Back to home {I['arrow']}</a><a class="btn btn--ghost" href="/#collection">View the collection</a></div>
      </div>
    </section>
  </main>
'''
    html += footer(p, False)
    return html

def knowledge():
    """Plain-text knowledge base for the site chatbot, built from the same data as the pages."""
    import html as _html, re as _re
    t = lambda s: _re.sub(r"\s+", " ", _html.unescape(_re.sub(r"<[^>]+>", "", s))).strip()
    out = ["# Bincoo MENA — knowledge base",
           "",
           "## Company",
           "- Bincoo MENA is the official home of Bincoo smart coffee machines in the Middle East & North Africa, operated exclusively by KUVANI.",
           "- Sales model: Bincoo MENA sells only through authorized distributors. It does not sell directly to individuals or end customers.",
           "- Businesses that want to become an authorized distributor, and anyone looking for where to buy in their market, should contact the team.",
           "- There is no online checkout and no shipping fees on the website.",
           f"- Website: {DOMAIN}",
           f"- WhatsApp / phone: {PHONE}",
           f"- Email: {EMAIL}",
           "- Instagram: @bincoo.mena (KUVANI: @kuvani.co)",
           "",
           "## Prices",
           "- Prices are retail reference prices in US dollars, for information only. Final pricing is set by the authorized distributor in each market.",
           ""]
    for pr in PRODUCTS:
        d = PDP[pr["slug"]]
        out += [f"## {pr['name']} — {t(pr['cat'])}",
                f"- Full name: {pr['full']}",
                f"- Retail reference price: {pr['price']}",
                f"- Page: {DOMAIN}/products/{pr['slug']}.html",
                f"- Summary: {t(d['lead'])}",
                f"- Colours: {', '.join(c for c, _ in d['colors'])}"]
        if d["configs"]:
            out.append("- Configurations: " + "; ".join(f"{c} ({t(pz)})" for c, pz, _ in d["configs"]))
        out.append("- Highlights:")
        out += [f"  - {t(title)}: {t(txt)}" for _, title, txt, _ in d["features"]]
        out.append("- Specifications:")
        out += [f"  - {t(a)}: {t(b)}" for a, b in d["specs"]]
        if d["recipes"]:
            out.append("- Built-in brewing methods:")
            out += [f"  - {t(a)} ({t(b)}): {t(c)} Best for: {t(e)}" for a, b, c, e in d["recipes"]]
        out.append("")
    out.append("## Frequently asked questions")
    for q, a in FAQS:
        out += [f"- Q: {t(q)}", f"  A: {t(a)}"]
    return "\n".join(out) + "\n"

def write(rel, s):
    path = os.path.join(SITE, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(s)
    print("wrote", rel, len(s))

write("index.html", home())
for pr in PRODUCTS:
    write(f"products/{pr['slug']}.html", product_page(pr["slug"]))
write("404.html", notfound())
write("api/knowledge.md", knowledge())
