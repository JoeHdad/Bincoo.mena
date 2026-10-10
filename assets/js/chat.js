/* ==========================================================================
   Bincoo MENA — chat assistant widget
   Talks to /api/chat.php (AI replies) and /api/lead.php (contact requests).
   ========================================================================== */
(() => {
  "use strict";

  const API = "/api/";
  const WA = (typeof CONFIG !== "undefined" && CONFIG.whatsapp) || "97470510002";
  const STORE = "bm-chat-v1";
  const COUNTRIES = ["Algeria", "Bahrain", "Egypt", "Iraq", "Jordan", "Kuwait", "Lebanon", "Libya", "Morocco", "Oman", "Palestine", "Qatar", "Saudi Arabia", "Sudan", "Syria", "Tunisia", "United Arab Emirates", "Yemen", "Other"];
  const GREETING = "Hi! I'm the Bincoo MENA assistant. Ask me about our machines, their specs, or how to buy in your market.\n\nمرحباً! اسألني عن ماكينات Bincoo ومواصفاتها وطريقة الشراء في بلدك.";
  const CHIPS = ["Compare the 3 machines", "Which machine suits a café?", "How can I buy?", "Become a distributor", "ما الفرق بين الماكينات؟"];

  const ICONS = {
    chat: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 12a8 8 0 0 1-11.6 7.1L4 20l1-4.1A8 8 0 1 1 20 12z"/><path d="M8.5 11h.01M12 11h.01M15.5 11h.01" stroke-width="2.4"/></svg>',
    close: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
    send: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    user: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
    wa: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.08-.3-.15-1.26-.47-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.07c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.41-.08-.13-.27-.2-.57-.35m-5.42 7.4h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.82 9.82 0 0 1 2.89 6.99c0 5.45-4.44 9.88-9.88 9.88m8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.16-3.48-8.41z"/></svg>'
  };

  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const waLink = (text) => `https://wa.me/${WA}?text=${encodeURIComponent(text)}`;

  /** Minimal, safe Markdown: escape first, then bold, links, bare URLs and simple lists. */
  const render = (text) => {
    const inline = (s) => esc(s)
      .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
      .replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
      .replace(/(^|[\s(])(https?:\/\/[^\s<)]+)/g, '$1<a href="$2" target="_blank" rel="noopener">$2</a>');
    const blocks = [];
    let list = null;
    String(text).split(/\n/).forEach((line) => {
      const item = line.match(/^\s*(?:[-•*]|\d+[.)])\s+(.*)$/);
      if (item) {
        if (!list) { list = []; blocks.push(list); }
        list.push(`<li dir="auto">${inline(item[1])}</li>`);
      } else {
        list = null;
        if (line.trim()) blocks.push(`<p dir="auto">${inline(line)}</p>`);
      }
    });
    return blocks.map((b) => (Array.isArray(b) ? `<ul dir="auto">${b.join("")}</ul>` : b)).join("");
  };

  let state = { messages: [] };
  try { state = JSON.parse(sessionStorage.getItem(STORE)) || state; } catch (e) {}
  const save = () => { try { sessionStorage.setItem(STORE, JSON.stringify(state)); } catch (e) {} };

  /* ---------- Markup ---------- */
  const root = document.createElement("div");
  root.className = "bmc";
  root.innerHTML = `
    <button class="bmc-launcher" type="button" aria-label="Open chat" aria-expanded="false" aria-controls="bmc-panel">
      <span class="bmc-launcher__icon bmc-launcher__icon--chat">${ICONS.chat}</span>
      <span class="bmc-launcher__icon bmc-launcher__icon--close">${ICONS.close}</span>
    </button>
    <div class="bmc-nudge" role="status">Questions about our machines? <strong>Ask us</strong></div>
    <section class="bmc-panel" id="bmc-panel" role="dialog" aria-modal="false" aria-label="Bincoo MENA chat assistant" hidden>
      <header class="bmc-head">
        <span class="bmc-avatar" aria-hidden="true">B</span>
        <div class="bmc-head__text"><strong>Bincoo MENA Assistant</strong><span><i></i>Online · replies in seconds</span></div>
        <button class="bmc-iconbtn" type="button" data-bmc-contact aria-label="Talk to our team" title="Talk to our team">${ICONS.user}</button>
        <a class="bmc-iconbtn bmc-iconbtn--wa" href="${waLink("Hello Bincoo MENA team,")}" target="_blank" rel="noopener" aria-label="WhatsApp us" title="WhatsApp us">${ICONS.wa}</a>
        <button class="bmc-iconbtn" type="button" data-bmc-close aria-label="Close chat">${ICONS.close}</button>
      </header>
      <div class="bmc-log" role="log" aria-live="polite"></div>
      <div class="bmc-chips"></div>
      <form class="bmc-input" autocomplete="off">
        <textarea rows="1" maxlength="1000" placeholder="Type your question…" aria-label="Your message" dir="auto"></textarea>
        <button type="submit" aria-label="Send">${ICONS.send}</button>
      </form>
      <p class="bmc-note">AI assistant · answers may contain mistakes. Please don't share sensitive information.</p>
    </section>`;
  document.body.appendChild(root);

  const $ = (s) => root.querySelector(s);
  const launcher = $(".bmc-launcher");
  const panel = $(".bmc-panel");
  const log = $(".bmc-log");
  const chips = $(".bmc-chips");
  const form = $(".bmc-input");
  const input = $(".bmc-input textarea");
  let busy = false;

  /* ---------- Rendering ---------- */
  const scroll = () => { log.scrollTop = log.scrollHeight; };

  const bubble = (role, text, extraClass) => {
    const el = document.createElement("div");
    el.className = `bmc-msg bmc-msg--${role}${extraClass ? " " + extraClass : ""}`;
    el.setAttribute("dir", "auto");
    el.innerHTML = role === "user" ? `<p dir="auto">${esc(text)}</p>` : render(text);
    log.appendChild(el);
    scroll();
    return el;
  };

  const actions = (html) => {
    const el = document.createElement("div");
    el.className = "bmc-actions";
    el.innerHTML = html;
    log.appendChild(el);
    scroll();
    return el;
  };

  const renderChips = () => {
    chips.innerHTML = state.messages.length ? "" : CHIPS.map((c) => `<button type="button" dir="auto">${esc(c)}</button>`).join("");
  };

  const restore = () => {
    log.innerHTML = "";
    bubble("assistant", GREETING);
    state.messages.forEach((m) => bubble(m.role, m.content));
    renderChips();
  };

  /* ---------- Sending ---------- */
  const typing = () => {
    const el = document.createElement("div");
    el.className = "bmc-msg bmc-msg--assistant bmc-typing";
    el.innerHTML = "<span></span><span></span><span></span>";
    log.appendChild(el);
    scroll();
    return el;
  };

  const errorText = {
    not_configured: "The assistant isn't available right now. Our team is happy to help on WhatsApp.",
    busy: "We're receiving a lot of messages right now. Please try again in a minute, or reach us on WhatsApp.",
    rate_limited: "You've reached the message limit for now. Please continue with our team on WhatsApp.",
    default: "Sorry, something went wrong. Please try again, or reach us on WhatsApp."
  };

  const send = async (text) => {
    text = text.trim();
    if (!text || busy) return;
    busy = true;
    form.classList.add("is-busy");
    state.messages.push({ role: "user", content: text });
    save();
    bubble("user", text);
    renderChips();
    const dots = typing();
    try {
      const res = await fetch(API + "chat.php", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: state.messages.slice(-12) })
      });
      const data = await res.json().catch(() => ({}));
      dots.remove();
      if (!res.ok || !data.reply) {
        state.messages.pop(); // let the visitor resend the same question
        save();
        bubble("assistant", errorText[data.error] || errorText.default, "bmc-msg--error");
        actions(`<a class="bmc-btn bmc-btn--wa" href="${waLink("Hello Bincoo MENA team, " + text)}" target="_blank" rel="noopener">${ICONS.wa} WhatsApp us</a>`);
      } else {
        state.messages.push({ role: "assistant", content: data.reply });
        save();
        bubble("assistant", data.reply);
        if (data.contact) offerContact();
      }
    } catch (e) {
      dots.remove();
      state.messages.pop();
      save();
      bubble("assistant", errorText.default, "bmc-msg--error");
    } finally {
      busy = false;
      form.classList.remove("is-busy");
      input.focus();
    }
  };

  /* ---------- Contact form ---------- */
  const offerContact = () => {
    const el = actions(`<button class="bmc-btn" type="button">${ICONS.user} Contact our team</button>
      <a class="bmc-btn bmc-btn--wa" href="${waLink(summary())}" target="_blank" rel="noopener">${ICONS.wa} WhatsApp</a>`);
    el.querySelector("button").addEventListener("click", showForm);
  };

  const summary = () => {
    const asked = state.messages.filter((m) => m.role === "user").slice(-3).map((m) => `• ${m.content}`).join("\n");
    return `Hello Bincoo MENA team,\n\nI was chatting with your website assistant:\n${asked}\n\nName: \nCompany: \nCountry: `;
  };

  const showForm = () => {
    if (log.querySelector(".bmc-form")) { log.querySelector(".bmc-form").scrollIntoView({ block: "nearest" }); return; }
    const wrap = document.createElement("form");
    wrap.className = "bmc-form";
    wrap.noValidate = true;
    wrap.innerHTML = `
      <strong>Talk to our team</strong>
      <p>Leave your details and we'll get back to you, or connect you with the authorized distributor for your market.</p>
      <label>Name *<input name="name" required maxlength="120" autocomplete="name"></label>
      <label>Company<input name="company" maxlength="160" autocomplete="organization"></label>
      <label>Country *<select name="country" required><option value="">Select…</option>${COUNTRIES.map((c) => `<option>${c}</option>`).join("")}</select></label>
      <label>Phone / WhatsApp<input name="phone" type="tel" maxlength="40" autocomplete="tel" placeholder="+974 …"></label>
      <label>Email<input name="email" type="email" maxlength="160" autocomplete="email" placeholder="name@company.com"></label>
      <label>I'm interested in<select name="interest">
        <option>Finding where to buy in my country</option>
        <option>Becoming an authorized distributor</option>
        <option>Something else</option>
      </select></label>
      <label>Message<textarea name="message" rows="2" maxlength="1500" dir="auto"></textarea></label>
      <input class="bmc-hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
      <p class="bmc-form__err" role="alert"></p>
      <button class="bmc-btn bmc-btn--solid" type="submit">Send</button>`;
    log.appendChild(wrap);
    wrap.scrollIntoView({ block: "nearest" });
    wrap.querySelector("input[name=name]").focus();

    wrap.addEventListener("submit", async (e) => {
      e.preventDefault();
      const f = Object.fromEntries(new FormData(wrap).entries());
      const err = wrap.querySelector(".bmc-form__err");
      if (!f.name.trim() || !f.country) { err.textContent = "Please add your name and country."; return; }
      if (!f.phone.trim() && !/^\S+@\S+\.\S+$/.test(f.email.trim())) { err.textContent = "Please add a phone number or a valid email."; return; }
      err.textContent = "";
      const btn = wrap.querySelector("button[type=submit]");
      btn.disabled = true;
      btn.textContent = "Sending…";
      try {
        const res = await fetch(API + "lead.php", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(Object.assign(f, { transcript: state.messages.slice(-10) }))
        });
        if (!res.ok) throw new Error(String(res.status));
        wrap.remove();
        bubble("assistant", `Thank you, ${f.name.trim()}! Our team has your details and will be in touch soon.`);
      } catch (ex) {
        btn.disabled = false;
        btn.textContent = "Send";
        err.innerHTML = `We couldn't send your request. Please <a href="${waLink(summary())}" target="_blank" rel="noopener">message us on WhatsApp</a>.`;
      }
    });
  };

  /* ---------- Open / close ---------- */
  const open = () => {
    panel.hidden = false;
    requestAnimationFrame(() => root.classList.add("is-open"));
    launcher.setAttribute("aria-expanded", "true");
    launcher.setAttribute("aria-label", "Close chat");
    root.classList.remove("has-nudge");
    if (!log.childElementCount) restore();
    setTimeout(() => input.focus(), 250);
  };
  const close = () => {
    root.classList.remove("is-open");
    launcher.setAttribute("aria-expanded", "false");
    launcher.setAttribute("aria-label", "Open chat");
    setTimeout(() => { if (!root.classList.contains("is-open")) panel.hidden = true; }, 350);
  };

  launcher.addEventListener("click", () => (root.classList.contains("is-open") ? close() : open()));
  $("[data-bmc-close]").addEventListener("click", close);
  $("[data-bmc-contact]").addEventListener("click", showForm);
  document.addEventListener("keydown", (e) => { if (e.key === "Escape" && root.classList.contains("is-open")) close(); });
  chips.addEventListener("click", (e) => { const b = e.target.closest("button"); if (b) send(b.textContent); });
  form.addEventListener("submit", (e) => { e.preventDefault(); const t = input.value; input.value = ""; input.style.height = ""; send(t); });
  input.addEventListener("keydown", (e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); form.requestSubmit(); } });
  input.addEventListener("input", () => { input.style.height = ""; input.style.height = Math.min(input.scrollHeight, 120) + "px"; });

  // A small one-time nudge after a few seconds on the first visit of the session
  try {
    if (!sessionStorage.getItem("bm-chat-nudged")) {
      setTimeout(() => {
        if (!root.classList.contains("is-open")) root.classList.add("has-nudge");
        sessionStorage.setItem("bm-chat-nudged", "1");
        setTimeout(() => root.classList.remove("has-nudge"), 7000);
      }, 6000);
    }
  } catch (e) {}
})();
