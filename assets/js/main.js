/* ==========================================================================
   Bincoo MENA — site behaviour
   No dependencies. Every feature degrades gracefully without JS.
   ========================================================================== */

/* ---------- Site settings: edit here ---------- */
const CONFIG = {
  whatsapp: "97470510002",          // international format, digits only
  phoneDisplay: "+974 7051 0002",
  email: "bincoo@kuvani.com",
  showPrices: true                  // false hides every retail reference price
};

(() => {
  "use strict";

  const root = document.documentElement;
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Prices toggle ---------- */
  if (!CONFIG.showPrices) $$(".price, [data-price]").forEach((el) => el.remove());

  /* ---------- Preloader ---------- */
  const finishLoading = () => {
    if (root.classList.contains("is-loaded")) return;
    root.classList.add("is-loaded");
    try { sessionStorage.setItem("bm-visited", "1"); } catch (e) {}
    setTimeout(() => { const p = $(".preloader"); if (p) p.remove(); }, 1000);
  };
  if (root.classList.contains("skip-preloader")) {
    finishLoading();
  } else {
    window.addEventListener("load", () => setTimeout(finishLoading, 450));
    setTimeout(finishLoading, 2600); // never block on a slow asset
  }

  /* ---------- Theme toggle ---------- */
  const setTheme = (t) => {
    root.setAttribute("data-theme", t);
    try { localStorage.setItem("bm-theme", t); } catch (e) {}
    $$("[data-theme-toggle]").forEach((b) => {
      b.setAttribute("aria-pressed", String(t === "dark"));
      b.setAttribute("aria-label", t === "dark" ? "Switch to light theme" : "Switch to dark theme");
    });
    const meta = $('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", t === "dark" ? "#0B0A09" : "#F5F2EC");
  };
  setTheme(root.getAttribute("data-theme") || "light");
  $$("[data-theme-toggle]").forEach((btn) =>
    btn.addEventListener("click", () => setTheme(root.getAttribute("data-theme") === "dark" ? "light" : "dark"))
  );

  /* ---------- Header, progress bar, floating button ---------- */
  const header = $(".header");
  const bar = $(".progress span");
  const fab = $(".fab");
  let lastY = window.scrollY;
  let ticking = false;

  const onScroll = () => {
    const y = window.scrollY;
    const max = document.documentElement.scrollHeight - window.innerHeight;
    if (header) {
      header.classList.toggle("is-scrolled", y > 10);
      const menuOpen = root.classList.contains("menu-open");
      header.classList.toggle("is-hidden", !menuOpen && y > 400 && y > lastY + 4);
      if (y < lastY - 4) header.classList.remove("is-hidden");
    }
    if (bar) bar.style.transform = `scaleX(${max > 0 ? y / max : 0})`;
    if (fab) fab.classList.toggle("is-visible", y > 600);
    lastY = y;
    parallax();
    hscroll();
    ticking = false;
  };
  window.addEventListener("scroll", () => {
    if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });

  /* ---------- Mobile menu ---------- */
  const burger = $(".burger");
  const closeMenu = () => {
    root.classList.remove("menu-open");
    if (burger) burger.setAttribute("aria-expanded", "false");
  };
  if (burger) {
    burger.addEventListener("click", () => {
      const open = !root.classList.contains("menu-open");
      root.classList.toggle("menu-open", open);
      burger.setAttribute("aria-expanded", String(open));
    });
    $$(".mobile-menu a").forEach((a) => a.addEventListener("click", closeMenu));
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeMenu(); });
  }

  /* ---------- Hero slider: one machine every 5 s ---------- */
  const heroVisual = $(".hero__visual");
  if (heroVisual && $$(".hero__slide", heroVisual).length > 1) {
    const slides = $$(".hero__slide", heroVisual);
    const chipSets = $$(".hero__chips", heroVisual);
    const dots = $$(".hero__dot", heroVisual);
    const link = $(".hero__tile-link", heroVisual);
    let index = 0;

    const go = (next) => {
      if (next === index) return;
      const prev = index;
      index = (next + slides.length) % slides.length;
      slides[prev].classList.remove("is-active");
      slides[prev].classList.add("is-leaving");
      setTimeout(() => slides[prev].classList.remove("is-leaving"), 1300);
      slides[index].classList.add("is-active");
      chipSets.forEach((c, i) => {
        c.classList.toggle("is-active", i === index);
        c.setAttribute("aria-hidden", String(i !== index));
      });
      dots.forEach((d, i) => {
        d.classList.remove("is-active");
        d.classList.toggle("is-done", i < index);
        d.setAttribute("aria-current", String(i === index));
      });
      void dots[index].offsetWidth; // restart the progress animation
      dots[index].classList.add("is-active");
      if (link) {
        link.href = dots[index].dataset.href;
        link.setAttribute("aria-label", `View ${dots[index].dataset.name}`);
      }
    };

    dots.forEach((d, i) => d.addEventListener("click", () => go(i)));
    // Autoplay follows the progress bar, so hovering (which pauses the bar) also pauses the slider
    if (!reduceMotion) {
      dots.forEach((d) => $(".hero__dot-bar i", d).addEventListener("animationend", () => go(index + 1)));
    }
    // Pause while the hero is off screen or the tab is hidden
    const setPaused = (paused) => heroVisual.classList.toggle("is-paused", paused);
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(([e]) => setPaused(!e.isIntersecting)).observe(heroVisual);
    }
    document.addEventListener("visibilitychange", () => setPaused(document.hidden));
    // Swipe on touch screens
    let x0 = null;
    heroVisual.addEventListener("touchstart", (e) => { x0 = e.touches[0].clientX; }, { passive: true });
    heroVisual.addEventListener("touchend", (e) => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 40) go(index + (dx < 0 ? 1 : -1));
      x0 = null;
    });
  }

  /* ---------- Split headings into words for the reveal ---------- */
  const splitWords = (el) => {
    const walk = (node) => {
      Array.from(node.childNodes).forEach((child) => {
        if (child.nodeType === 3) {
          const parts = child.textContent.split(/(\s+)/);
          const frag = document.createDocumentFragment();
          parts.forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(" ")); return; }
            const w = document.createElement("span");
            w.className = "w";
            const inner = document.createElement("span");
            inner.textContent = part;
            w.appendChild(inner);
            frag.appendChild(w);
          });
          node.replaceChild(frag, child);
        } else if (child.nodeType === 1 && child.tagName !== "BR") {
          walk(child);
        }
      });
    };
    walk(el);
    $$(".w > span", el).forEach((s, i) => s.style.setProperty("--d", `${(i * 0.045).toFixed(3)}s`));
  };
  $$("[data-split]").forEach(splitWords);

  /* ---------- Reveal on scroll ---------- */
  $$("[data-stagger]").forEach((group) => {
    const step = parseFloat(group.dataset.stagger) || 0.08;
    $$("[data-reveal]", group).forEach((el, i) => el.style.setProperty("--d", `${(i * step).toFixed(2)}s`));
  });
  const revealTargets = $$("[data-reveal], [data-split]");
  // The hero animates on page load, not on scroll
  $$(".hero [data-split]").forEach((el) => el.classList.add("is-in"));
  if ("IntersectionObserver" in window && !reduceMotion) {
    // A fully clipped element never reports as intersecting, so clip reveals watch their parent
    const watched = new Map();
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          (watched.get(entry.target) || []).forEach((el) => el.classList.add("is-in"));
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.12 });
    revealTargets.forEach((el) => {
      if (el.classList.contains("is-in")) return;
      const target = el.dataset.reveal === "clip" ? el.parentElement : el;
      if (!watched.has(target)) watched.set(target, []);
      watched.get(target).push(el);
      io.observe(target);
    });
  } else {
    revealTargets.forEach((el) => el.classList.add("is-in"));
  }

  /* ---------- Counters ---------- */
  const counters = $$("[data-count]");
  const runCounter = (el) => {
    const target = parseFloat(el.dataset.count);
    const decimals = (el.dataset.count.split(".")[1] || "").length;
    const dur = 1600;
    const t0 = performance.now();
    const tick = (now) => {
      const p = Math.min(1, (now - t0) / dur);
      const eased = 1 - Math.pow(1 - p, 4);
      el.textContent = (target * eased).toFixed(decimals);
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  if (counters.length && "IntersectionObserver" in window && !reduceMotion) {
    const cio = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { runCounter(e.target); cio.unobserve(e.target); } });
    }, { threshold: 0.6 });
    counters.forEach((c) => cio.observe(c));
  }

  /* ---------- Parallax ---------- */
  const parallaxEls = reduceMotion ? [] : $$("[data-parallax]");
  function parallax() {
    const vh = window.innerHeight;
    parallaxEls.forEach((el) => {
      const r = el.parentElement.getBoundingClientRect();
      if (r.bottom < -100 || r.top > vh + 100) return;
      const speed = parseFloat(el.dataset.parallax) || 0.12;
      const progress = (r.top + r.height / 2 - vh / 2) / vh; // -1..1 around centre
      el.style.transform = `translate3d(0, ${(-progress * speed * 100).toFixed(2)}%, 0)`;
    });
  }

  /* ---------- Pinned horizontal gallery ---------- */
  const hs = $(".hscroll");
  const hsTrack = hs ? $(".hscroll__track", hs) : null;
  let hsActive = false;
  const setupHscroll = () => {
    if (!hs || !hsTrack) return;
    hsActive = !reduceMotion && window.innerWidth > 900;
    hs.classList.toggle("hscroll--static", !hsActive);
    if (!hsActive) { hs.style.height = ""; hsTrack.style.transform = ""; return; }
    const distance = hsTrack.scrollWidth - window.innerWidth;
    hs.style.height = `${window.innerHeight + Math.max(0, distance)}px`;
    hscroll();
  };
  function hscroll() {
    if (!hsActive) return;
    const r = hs.getBoundingClientRect();
    const distance = hsTrack.scrollWidth - window.innerWidth;
    const p = Math.min(1, Math.max(0, -r.top / (r.height - window.innerHeight)));
    hsTrack.style.transform = `translate3d(${(-p * distance).toFixed(1)}px, 0, 0)`;
  }
  setupHscroll();
  let resizeTimer;
  window.addEventListener("resize", () => { clearTimeout(resizeTimer); resizeTimer = setTimeout(() => { setupHscroll(); parallax(); }, 150); });
  window.addEventListener("load", setupHscroll);

  /* ---------- FAQ: smooth accordion ---------- */
  $$(".faq details").forEach((d) => {
    const summary = $("summary", d);
    const body = $(".faq__a", d);
    summary.addEventListener("click", (e) => {
      if (reduceMotion || !body.animate) return;
      e.preventDefault();
      if (d.open) {
        const h = body.offsetHeight;
        body.animate([{ height: `${h}px`, opacity: 1 }, { height: "0px", opacity: 0 }], { duration: 420, easing: "cubic-bezier(.22,.61,.36,1)" })
          .onfinish = () => { d.open = false; };
      } else {
        d.open = true;
        const h = body.offsetHeight;
        body.animate([{ height: "0px", opacity: 0 }, { height: `${h}px`, opacity: 1 }], { duration: 520, easing: "cubic-bezier(.16,1,.3,1)" });
      }
    });
  });

  /* ---------- WhatsApp / email helpers ---------- */
  const waLink = (text) => `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(text)}`;
  const mailLink = (subject, body) => `mailto:${CONFIG.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  const quoteText = (product) =>
    `Hello Bincoo MENA team,\n\nWe are a business interested in a trade quotation for:\n• ${product}\n\nPlease share pricing, availability and lead times.\n\nCompany: \nCountry: \nEstimated quantity: `;

  // Generic "quote" links (product cards, CTAs)
  $$("[data-wa]").forEach((a) => {
    const product = a.dataset.wa;
    a.href = waLink(product ? quoteText(product) : "Hello Bincoo MENA team, we are a business and would like to discuss a trade account.");
    a.target = "_blank";
    a.rel = "noopener";
  });
  $$("[data-mail]").forEach((a) => {
    const product = a.dataset.mail;
    a.href = product
      ? mailLink(`Trade quotation request — ${product}`, quoteText(product))
      : mailLink("Trade enquiry — Bincoo MENA", "Hello Bincoo MENA team,\n\nWe are a business and would like to discuss a trade account.\n\nCompany: \nCountry: ");
  });

  /* ---------- Product page: gallery, options, lightbox ---------- */
  const pdp = $("[data-pdp]");
  if (pdp) {
    const mainWrap = $(".gallery__main", pdp);
    const thumbs = $$(".thumb", pdp);
    const productName = pdp.dataset.pdp;
    const state = { color: null, config: null };
    let current = 0;

    const show = (i) => {
      const t = thumbs[i];
      if (!t) return;
      current = i;
      thumbs.forEach((x) => x.classList.toggle("is-active", x === t));
      const img = $("img", mainWrap);
      const src = t.dataset.full;
      if (img.getAttribute("src") === src) return;
      img.classList.add("is-leaving");
      const pre = new Image();
      pre.onload = () => {
        img.src = src;
        img.alt = t.dataset.alt || "";
        img.classList.toggle("is-cover", t.dataset.fit === "cover");
        requestAnimationFrame(() => img.classList.remove("is-leaving"));
      };
      pre.src = src;
    };
    thumbs.forEach((t, i) => t.addEventListener("click", () => show(i)));

    // Option pills (colour / configuration)
    $$("[data-option]", pdp).forEach((group) => {
      const key = group.dataset.option;
      const pills = $$(".pill", group);
      const label = $(`[data-option-value="${key}"]`, pdp);
      const select = (pill) => {
        pills.forEach((p) => p.setAttribute("aria-pressed", String(p === pill)));
        state[key] = pill.dataset.value;
        if (label) label.textContent = pill.dataset.value;
        if (pill.dataset.price) { const pr = $("[data-price-value]", pdp); if (pr) pr.textContent = pill.dataset.price; }
        // A configuration may carry its own image per colour, e.g. the grinder bundle
        const cfg = $('[data-option="config"] .pill[aria-pressed="true"]', pdp);
        const tpl = cfg && cfg.dataset.imageTemplate;
        const target = tpl && state.color ? tpl.replace("{color}", state.color.toLowerCase()) : null;
        const colorPill = $('[data-option="color"] .pill[aria-pressed="true"]', pdp);
        const src = target || (key === "color" ? pill.dataset.image : colorPill && colorPill.dataset.image);
        if (src) {
          const idx = thumbs.findIndex((t) => t.dataset.full === src);
          if (idx > -1) show(idx);
        }
        updateQuote();
      };
      pills.forEach((p) => p.addEventListener("click", () => select(p)));
      const initial = pills.find((p) => p.getAttribute("aria-pressed") === "true") || pills[0];
      if (initial) { state[key] = initial.dataset.value; if (label) label.textContent = initial.dataset.value; }
    });

    function updateQuote() {
      const parts = [state.color, state.config].filter(Boolean).join(", ");
      const full = parts ? `${productName} (${parts})` : productName;
      $$("[data-quote-wa]", pdp).forEach((a) => { a.href = waLink(quoteText(full)); a.target = "_blank"; a.rel = "noopener"; });
      $$("[data-quote-mail]", pdp).forEach((a) => { a.href = mailLink(`Trade quotation request — ${full}`, quoteText(full)); });
    }
    updateQuote();

    // Lightbox
    const lb = $(".lightbox");
    if (lb) {
      const lbImg = $("img", lb);
      const open = () => {
        const t = thumbs[current];
        lbImg.src = t.dataset.full; lbImg.alt = t.dataset.alt || "";
        lb.classList.add("is-open"); lb.setAttribute("aria-hidden", "false");
        $(".lightbox__close", lb).focus();
      };
      const close = () => { lb.classList.remove("is-open"); lb.setAttribute("aria-hidden", "true"); };
      const step = (d) => { show((current + d + thumbs.length) % thumbs.length); lbImg.src = thumbs[current].dataset.full; };
      $(".gallery__zoom", pdp)?.addEventListener("click", open);
      $(".lightbox__close", lb).addEventListener("click", close);
      $(".lightbox__nav--prev", lb).addEventListener("click", () => step(-1));
      $(".lightbox__nav--next", lb).addEventListener("click", () => step(1));
      lb.addEventListener("click", (e) => { if (e.target === lb) close(); });
      document.addEventListener("keydown", (e) => {
        if (!lb.classList.contains("is-open")) return;
        if (e.key === "Escape") close();
        if (e.key === "ArrowRight") step(1);
        if (e.key === "ArrowLeft") step(-1);
      });
    }
  }

  /* ---------- B2B inquiry form ---------- */
  const form = $("#inquiry-form");
  if (form) {
    // Pre-select a product from ?product=slug (links from product pages and cards)
    const params = new URLSearchParams(location.search);
    const pre = params.get("product");
    if (pre) {
      const box = form.querySelector(`input[name="products"][value="${CSS.escape(pre)}"]`);
      if (box) box.checked = true;
    }
    $$("[data-preselect]").forEach((a) => a.addEventListener("click", () => {
      const box = form.querySelector(`input[name="products"][value="${a.dataset.preselect}"]`);
      if (box) box.checked = true;
    }));

    const status = $(".form__status", form);
    const required = $$("[required]", form);
    const validate = () => {
      let ok = true;
      required.forEach((input) => {
        const field = input.closest(".field");
        const valid = input.checkValidity() && input.value.trim() !== "";
        field.classList.toggle("is-invalid", !valid);
        if (!valid && ok) { input.focus(); ok = false; }
      });
      return ok;
    };
    required.forEach((input) => input.addEventListener("input", () => {
      const field = input.closest(".field");
      if (field.classList.contains("is-invalid") && input.checkValidity()) field.classList.remove("is-invalid");
    }));

    const compose = () => {
      const f = new FormData(form);
      const products = f.getAll("products").map((v) => form.querySelector(`input[value="${v}"]`).dataset.label);
      const lines = [
        "New B2B inquiry — Bincoo MENA",
        "",
        `Company: ${f.get("company")}`,
        `Contact person: ${f.get("name")}`,
        `Business type: ${f.get("type") || "—"}`,
        `Country: ${f.get("country")}`,
        `Email: ${f.get("email")}`,
        `Phone: ${f.get("phone")}`,
        "",
        `Products of interest: ${products.length ? products.join(", ") : "Not specified"}`,
        `Estimated quantity: ${f.get("quantity") || "—"}`,
        "",
        `Message: ${f.get("message") || "—"}`
      ];
      return { text: lines.join("\n"), company: f.get("company") };
    };

    form.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!validate()) return;
      const { text } = compose();
      window.open(waLink(text), "_blank", "noopener");
      if (status) status.textContent = "Opening WhatsApp… your inquiry is ready to send.";
    });
    $("[data-send-email]", form)?.addEventListener("click", () => {
      if (!validate()) return;
      const { text, company } = compose();
      window.location.href = mailLink(`B2B inquiry — ${company}`, text);
      if (status) status.textContent = "Opening your email app… your inquiry is ready to send.";
    });
  }

  /* ---------- Misc ---------- */
  $$("[data-year]").forEach((el) => { el.textContent = new Date().getFullYear(); });
  onScroll();
})();
