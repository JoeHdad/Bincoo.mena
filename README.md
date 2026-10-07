# Bincoo MENA — Exclusive by KUVANI

The official Bincoo website for the Middle East & North Africa, at **https://bincoo-mena.com**.
It is a B2B site: businesses only, no online checkout. Quote requests go out by WhatsApp or email.

موقع Bincoo الرسمي لمنطقة الشرق الأوسط وشمال أفريقيا، حصرياً عن طريق KUVANI. الموقع B2B، يعني للشركات فقط وما فيه دفع أونلاين. طلبات عروض الأسعار بتوصل على الواتساب أو الإيميل.

---

## محتوى الموقع

| الصفحة | الملف |
|---|---|
| الرئيسية (المنتجات، For Business، About، FAQ، نموذج طلب عرض السعر) | `index.html` |
| S2 Pro Trailblazer | `products/s2-pro-trailblazer.html` |
| Automatic Pour-Over | `products/automatic-pour-over.html` |
| Composer PO01 | `products/composer-po01.html` |
| صفحة الخطأ 404 | `404.html` |

- **التصميم:** `assets/css/style.css` (فيه الوضعين الفاتح والداكن، والأنيميشن، والتصميم المتجاوب للموبايل)
- **السكربت:** `assets/js/main.js` (زر الثيم، الأنيميشن عند السكرول، معرض الصور، ونموذج الطلب). ما بيعتمد على أي مكتبة خارجية.
- **الصور:** `assets/img/products/*.webp` (مأخوذة من موقع bincoo.com الرسمي)
- **اللوجوهات:** `assets/img/brand/` (Bincoo و KUVANI بصيغة SVG، ولونهم بيتغير تلقائياً مع الثيم)

الموقع **HTML ثابت** بدون قاعدة بيانات وبدون PHP، فبيشتغل على أي استضافة cPanel مباشرة.

---

## تعديل المعلومات

### رقم الواتساب والإيميل وإظهار الأسعار
بأول ملف `assets/js/main.js`:

```js
const CONFIG = {
  whatsapp: "97470510002",       // الرقم بالصيغة الدولية، أرقام فقط
  phoneDisplay: "+974 7051 0002",
  email: "bincoo@kuvani.com",
  showPrices: true               // false = بيخفي كل الأسعار من الموقع
};
```

### النصوص والمنتجات والمواصفات
كل الصفحات بتتولّد من ملف واحد: `tools/build.py`. عدّل النص فيه وبعدين شغّل:

```bash
python tools/build.py 7
```

الرقم (7) هو رقم نسخة الملفات. كبّره كل مرة بتعدّل فيها الـ CSS أو الـ JS، لحتى المتصفحات تحمّل النسخة الجديدة بدل النسخة المخزنة عندها.

> إذا بدك تغيّر رقم التواصل، غيّره بمكانين: `CONFIG` بملف `main.js`، والثوابت `WA` و `PHONE` و `EMAIL` بأول ملف `tools/build.py`. بعدين أعد توليد الصفحات.

---

## الرفع على cPanel

### ⭐ الطريقة المعتمدة: رفع تلقائي من GitHub
كل push على فرع `main` بيخلّي GitHub يعطي cPanel أمر يسحب آخر نسخة من الـ repo ويرفعها على `public_html`، خلال دقيقة تقريباً. الإعداد موجود بملف `.github/workflows/deploy.yml`، والنسخ على `public_html` بيصير حسب ملف `.cpanel.yml`.

> الـ FTP مسكّر على السيرفر، فهالطريقة بتستعمل cPanel API على البورت 2083 بداله.

**الإعداد لأول مرة بس:**
1. **اربط الـ repo بـ cPanel:** cPanel ← **Git™ Version Control** ← **Create**
   - **Clone a Repository:** خليه مفعّل
   - **Clone URL:** `https://github.com/JoeHdad/Bincoo.mena.git`
   - **Repository Path:** `repositories/Bincoo.mena`
   - **Repository Name:** `Bincoo.mena`
   - اضغط **Create**
2. **اعمل API Token:** cPanel ← **Manage API Tokens** ← **Create**
   - Name: `github-deploy`
   - Expiration: **The API Token will not expire**
   - اضغط **Create**، و**انسخ التوكن فوراً** لأنه ما بيظهر غير مرة وحدة.
3. **حطّه بـ GitHub:** الـ repo ← **Settings** ← **Secrets and variables** ← **Actions** ← **New repository secret**
   - Name: `CPANEL_TOKEN`
   - Secret: التوكن اللي نسخته
4. اعمل push على `main`، وتابع الرفع من تبويب **Actions**. لازم تطلع ✅ خضرا.

> إذا ضفت ملف أو مجلد جديد بجذر الموقع، ضيفه لسطور `/bin/cp` بملف `.cpanel.yml`، وإلا ما رح ينرفع.
> بتقدر تشغّل الرفع يدوياً من **Actions** ← **Deploy to bincoo-mena.com** ← **Run workflow**.

### الطريقة 1: ملف ZIP (احتياطية)
1. ادخل على cPanel ← **File Manager** ← افتح مجلد `public_html`.
2. فعّل خيار إظهار الملفات المخفية: **Settings** ← **Show Hidden Files**، لأن ملف `.htaccess` مخفي.
3. اضغط **Upload** وارفع ملف `bincoo-mena-cpanel.zip`.
4. اضغط على الملف بكليك يمين ← **Extract** جوّا `public_html`.
5. احذف ملف الـ ZIP بعد ما يخلص الاستخراج.

### الطريقة 2: من GitHub مباشرة (Git Version Control)
1. بملف `.cpanel.yml` غيّر `CPANEL_USERNAME` لاسم مستخدم حساب cPanel تبعك، واعمل commit و push.
2. cPanel ← **Git™ Version Control** ← **Create**، وحط رابط الـ repo:
   `https://github.com/JoeHdad/Bincoo.mena.git`
3. بعد ما يخلص الـ clone: **Manage** ← **Pull or Deploy** ← **Update from Remote** وبعدها **Deploy HEAD Commit**.
4. كل تعديل جديد: اعمل push على GitHub، وبعدين اضغط نفس الزرين.

> إذا الـ repo خاص (private)، cPanel بيحتاج SSH key مضاف بإعدادات GitHub ← Deploy keys.

### بعد الرفع
- **SSL:** cPanel ← **SSL/TLS Status** ← **Run AutoSSL**. ملف `.htaccess` بيحوّل كل الزوار لـ `https://bincoo-mena.com` تلقائياً، فلازم الشهادة تكون شغالة.
- جرّب: الرئيسية، صفحات المنتجات التلاتة، زر الثيم، نموذج الطلب، ورابط غلط (مثلاً `/test`) لازم يفتح صفحة 404.
- (اختياري) سجّل الموقع بـ Google Search Console، والـ sitemap موجود على `https://bincoo-mena.com/sitemap.xml`.

---

## التشغيل على جهازك

```bash
python -m http.server 8000
```

بعدها افتح `http://localhost:8000`. لازم تشغّله من سيرفر وما تفتح الملف مباشرة، لأن اللوجوهات (SVG) ما بتظهر من `file://`.
