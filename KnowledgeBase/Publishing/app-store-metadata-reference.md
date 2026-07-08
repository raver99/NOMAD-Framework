# 🚀 App Store Metadata Requirements – Apple App Store & Google Play Reference (2026)

## Purpose of This Document

This document is the canonical reference for all metadata required to publish a mobile app on the Apple App Store (App Store Connect) and Google Play Store (Play Console). It covers text fields with exact character limits, graphic asset specifications with exact pixel dimensions, mandatory declarations and questionnaires, and required URLs — current as of July 2026, sourced from Apple's and Google's official documentation. Use it together with the fillable [App Store Publishing Checklist](app-store-publishing-checklist.md) when preparing a release.

> Figures are drawn from Apple's App Store Connect Help / developer.apple.com and Google's Play Console Help / developer.android.com. Store requirements change frequently — always re-verify limits at upload time.

---

## 1. How the Two Stores Differ

Both stores separate listing metadata into (1) text fields, (2) graphic/visual assets, (3) declarations/questionnaires, and (4) URLs. Two structural differences shape everything else:

| Aspect | Apple App Store | Google Play Store |
|--------|-----------------|-------------------|
| Keyword indexing | Private 100-char keyword field; description NOT indexed | No keyword field; short + full description fully indexed |
| Total indexed text | 160 chars (name 30 + subtitle 30 + keywords 100) | ~4,000+ chars (title 30 + short 80 + full 4,000) |
| Screenshot validation | Exact pixel dimensions per device class — off-by-one = rejection | Range: 320–3840 px per side, aspect-ratio cap 2:1 |
| Extra required graphic | — | Feature graphic 1024×500 |
| Icon transparency | Forbidden (no alpha channel) | Required format is 32-bit PNG **with** alpha |
| Preview video | Direct upload, 15–30 s, exact specs | YouTube URL only |

> **Apple has a private keyword field and does not index the description; Google has no keyword field but fully indexes the short and full description. Write your copy differently for each store.**

✅ Apple: concentrate keywords in name + subtitle + keyword field, never repeating a word across them.
✅ Google: weave keywords naturally into title, short description, and full description.
❌ Don't reuse the same copy strategy across both stores.

---

## 2. Apple App Store (App Store Connect)

### 2.1 Text Fields (all localizable, per App Store language)

| Field | Limit | Indexed? | Editable without new build? | Notes |
|---|---|---|---|---|
| **App name / title** | 30 characters | Yes (strongest weight) | No | Reviewed before going live. Must not be misleading or use "free/best" claims. |
| **Subtitle** | 30 characters | Yes (2nd-strongest weight) | No | Appears under the name throughout the App Store. Don't duplicate name keywords. |
| **Keywords** | 100 characters | Yes | No | Private (not user-visible). Comma-separated, **no spaces after commas** (spaces consume characters). Skip plurals (Apple matches automatically); don't repeat words already in name/subtitle; avoid trademarks/competitor names. |
| **Promotional text** | 170 characters | **No** | **Yes — anytime, no review wait** | Appears at top of description on iOS 11+/macOS 10.13+. Ideal for time-sensitive messaging. |
| **Description** | 4,000 characters | No | No (new version only) | Feature/benefit copy. Don't keyword-stuff or list prices. |
| **What's New (release notes)** | 4,000 characters | No | No | Required for all versions after the first. Not for promotional use. |
| **Notes for App Review** | 4,000 characters | — | — | Optional. Include demo credentials, test settings; attachments allowed (.pdf, .mp4, etc.). |
| **In-app purchase display name** | 30 characters | — | — | Up to 20 IAPs/subscriptions shown across the two product-page sections. |
| **In-app purchase name (internal)** | 35 characters | — | — | — |
| **In-app purchase description** | 55 characters | — | — | — |
| **Copyright** | — | — | — | E.g. "2026 Company Name LLC" — the person/entity owning rights. |

> **Total indexed iOS space = 160 characters** (30 name + 30 subtitle + 100 keywords). Apple auto-combines individual words across these three fields into multi-word search phrases, so never repeat a word across them.

### 2.2 Graphics & Visual Assets

**App icon**
- Exactly **1024×1024 px**, **PNG**, **sRGB** (Display P3 wide-gamut also supported with sRGB fallback), **72 DPI**.
- **Fully opaque — no alpha channel / no transparency.** A transparent pixel is an automatic rejection.
- **Do not pre-round corners or add shadows/gloss** — iOS applies its "squircle" mask automatically. Baking in your own corners produces a broken double-radius look.
- Upload the single 1024×1024 master; smaller sizes are derived automatically.

**Screenshots** — 1–10 per device type, .jpeg/.jpg/.png, no transparency. Must match Apple's exact pixel dimensions per display class — an off-by-one export triggers "The dimensions of one or more screenshots are wrong."

iPhone display classes (portrait; landscape is the reverse):

| Display | Representative devices | Screenshot size (portrait) |
|---|---|---|
| **6.9"** (lead size for 2026) | iPhone 17 Pro Max, 16 Pro Max, 16 Plus, 15 Pro Max, 15 Plus, 14 Pro Max | **1320×2868** (also 1290×2796; iPhone Air uses **1260×2736**) |
| **6.5"** | iPhone 14 Plus, 13/12/11 Pro Max, 11, XS Max, XR | 1284×2778 or 1242×2688 — *required if 6.9" screenshots aren't provided* |
| **6.3"** | iPhone 17/17 Pro, 16/16 Pro, 15/15 Pro, 14 Pro | 1179×2556 or 1206×2622 (falls back to scaled 6.5") |
| **6.1"** | iPhone 16e, 14, 13 series, 12 series, 11 Pro, XS, X | 1170×2532 / 1125×2436 / 1080×2340 |
| **5.5"** | iPhone 8/7/6s/6 Plus | 1242×2208 |
| 4.7" / 4" / 3.5" | Older iPhone SE / 8 / 7 / 5 / 4 series | 750×1334 / 640×1136 / 640×960 |

iPad display classes:

| Display | Representative devices | Screenshot size (portrait) |
|---|---|---|
| **13"** (lead size for iPad) | iPad Pro (M5/M4), iPad Pro 3rd–6th gen, iPad Air (M2/M3/M4) | **2064×2752** or 2048×2732 — **required if app runs on iPad** |
| 12.9" | iPad Pro 2nd gen | 2048×2732 (falls back to scaled 13") |
| 11" | iPad Pro/Air variants, iPad (A16/10th gen), iPad mini | 1488×2266 / 1668×2420 / 1668×2388 / 1640×2360 |
| 10.5" / 9.7" | Older iPad Pro/Air/mini | 1668×2224 / 1536×2048 etc. |

Other platforms: **Mac** 1280×800, 1440×900, 2560×1600, or 2880×1800 (16:10); **Apple TV** 1920×1080 or 3840×2160; **Apple Vision Pro** 3840×2160; **Apple Watch** device-specific (e.g. 416×496 Series 11/10, 410×502 Ultra 2/Ultra) — same Watch size across all localizations.

- The first 2–3 screenshots are what most users see in search results. Text overlays/captions are permitted and standard practice, but must accurately represent the app (guideline 2.3.1); no misleading mockups.
- **Auto-scaling:** If you provide only the largest size (6.9" iPhone, 13" iPad), Apple scales down for smaller devices — but native uploads render sharpest.

**App previews (video)**
- Up to **3 per localization**, per device type. Portrait or landscape.
- **15–30 seconds** (anything outside this range is rejected, measured to the second).
- **≤500 MB**, **30 fps max.** Formats: H.264 (.mov/.m4v/.mp4) or ProRes 422 HQ (.mov). Audio: stereo 256 kbps AAC or PCM, 44.1/48 kHz.
- **Preview video resolutions are standardized lower resolutions, NOT screenshot sizes** — e.g. **iPhone 886×1920 / 1920×886**; **iPad 1200×1600 / 1600×1200**. Poster frame defaults to 5 seconds; set it deliberately after upload.
- Content must be **in-app footage only** (no live-action, no hands, no unrelated marketing). Each portrait video occupies one screenshot slot in the gallery.

### 2.3 Declarations & Questionnaires

**Age rating (MAJOR 2025–2026 CHANGE):** The updated age rating system adds **13+, 16+, and 18+** to the existing 4+ and 9+ tiers (the old 12+ and 17+ tiers are removed), with new required questions covering **In-app controls, Capabilities, Medical or wellness topics, and Violent themes**. You don't set a rating directly — Apple calculates it from your questionnaire answers, per country/region. **Deadline: responses were required by January 31, 2026 — missing answers block update submissions.** Complete this in the **App Information** section.

**App Privacy ("nutrition labels"):** Required to submit any new app or update. **Can be updated anytime without an app submission.** You declare — across **Data Used to Track You, Data Linked to You, Data Not Linked to You** — which of **14 data-type categories** you *and any third-party SDKs* collect: Contact Info, Health & Fitness, Financial Info, Location, Sensitive Info, Contacts, User Content, Browsing History, Search History, Identifiers, Purchases, Usage Data, Diagnostics, Other Data. A **Privacy Policy URL is required**; a Privacy Choices URL is optional.

> **Audit every dependency (analytics, crash reporting, ads SDKs) — their data collection must be declared even if you never see the data yourself.**

**Export compliance / encryption:** Every new version prompts encryption questions. Set the **`ITSAppUsesNonExemptEncryption`** key in your iOS `Info.plist`: **`false`** if the app only uses exempt encryption such as HTTPS via the OS (the vast majority of apps), **`true`** if it ships proprietary/non-standard cryptography. Setting it avoids the repeated "Missing Compliance" prompt. If `true`, you may owe an annual self-classification report to the U.S. BIS (due Feb 1 for the prior year) and possibly a CCATS; a separate **French encryption declaration** applies only if distributing in France.

**Other declarations/fields:** Category (**one primary + one optional secondary**); Content rights (third-party content); Regulated medical device status; EU Digital Services Act trader information; region-specific compliance for Mainland China, South Korea, and Vietnam. Contact information for App Review is mandatory.

### 2.4 URLs

| URL | Required? |
|---|---|
| Support URL | ✅ Mandatory — visible on the product page |
| Privacy Policy URL | ✅ Required — localizable per language |
| Marketing URL | Optional |
| Privacy Choices URL | Optional |

### 2.5 Localization

- App Store Connect supports localized metadata in **50 languages/locales** (11 Indian-market languages added March 31, 2026).
- Localizable fields: name, subtitle, keywords, description, promotional text, What's New, screenshots, app previews, support/marketing URLs, Privacy Policy URL. When you add a language, most properties default to the primary language **except description and keywords**. A new primary language requires App Review approval and matching screenshots.
- **Cross-localization tip:** in a given storefront Apple indexes keywords from up to two locales (e.g. en-US + es-MX in the U.S.), effectively extending your keyword reach.

---

## 3. Google Play Store (Play Console)

### 3.1 Text Fields (localizable per language; "Main store listing")

| Field | Limit | Indexed? | Editable without new build? | Notes |
|---|---|---|---|---|
| **App title** | 30 characters | Yes (highest weight) | Yes | No "Free/No Ads/#1/Best," no emojis, no ALL CAPS (unless brand), no promotional/ranking text. |
| **Short description** | 80 characters | Yes (2nd) | Yes | Shown in search results and above the fold. Second-most-important ranking field. |
| **Full description** | 4,000 characters | **Yes** (unlike Apple) | Yes | Fully indexed — use natural, keyword-relevant prose; avoid stuffing/word lists. |
| **Release notes ("What's new")** | 500 Unicode characters per language | No | With release | Not for promotional use. |
| **Developer name** | — | — | — | Must not be misleading. |

> **No dedicated keyword field** — Google extracts keywords from title, short, and full description. Density/relevance discipline matters more than character conservation.

### 3.2 Graphics & Visual Assets

(Managed under Grow users → Store presence → Main store listing → Graphics)

**App icon (required to publish)**
- **512×512 px**, **32-bit PNG with alpha**, **≤1024 KB (1 MB)**.
- Perfect square with **no rounded corners applied by you** — Google dynamically applies rounded corners and shadows. (As of March 31, 2026, Play renders icons with a ~30% corner radius; keep key elements within ~15–18% internal padding.) No badges/ranking/price text.

**Feature graphic (required to publish)**
- **1024×500 px**, **JPEG or 24-bit PNG, no alpha/transparency.** Used as the cover for the preview video and in promotional placements. Keep key content away from edges; no store badges, no device frames.

**Screenshots**
- **Minimum to publish:** two screenshots across different device types.
- **Maximum:** up to **8 per supported device type** (phones; 7" and 10" tablets; Chromebooks; Android TV; Wear OS; Android Automotive OS; Android XR).
- **Format:** JPEG or **24-bit PNG (no alpha).** Solid background — transparency is rejected.
- **Dimensions:** **min 320 px, max 3840 px** per side; the maximum dimension can't be more than twice the minimum (effective aspect-ratio cap, keeping assets within the 16:9 ↔ 9:16 family). Community standard for phones is 1080×1920 portrait.
- **Large-screen recommendation eligibility:** at least 4 screenshots at ≥1080 px, 16:9 landscape (≥1920×1080) or 9:16 portrait (≥1080×1920).
- **Device-specific:** Wear OS ≥1 screenshot at 1:1, min 384×384, no frames/transparency; Android TV requires ≥1 TV screenshot plus a **TV banner (1280×720, JPEG/24-bit PNG no alpha)**; Android XR 4–8 screenshots, 8:5, ≤8 MB each.
- Text overlays allowed; keep key content centered (Google may crop). Add **alt text (≤140 chars)** per asset for accessibility.

**Preview video**
- A **single YouTube URL only** — no direct file upload. Video URL (not playlist/channel), no extra parameters/timecodes.
- Requirements: ads/monetization **off**, privacy **public or unlisted** (not private), **not age-restricted**, and **embeddable**. Only the first ~30 seconds autoplays (muted). Games effectively need one to appear on certain surfaces.

### 3.3 Declarations & Questionnaires

(Play Console → Policy and programs → App content)

**Content rating (IARC questionnaire):** Free questionnaire generating ratings from multiple regional authorities simultaneously — ESRB (Americas), PEGI (Europe), USK (Germany), ClassInd (Brazil), ACB (Australia), GRAC (South Korea), plus IARC generic ratings elsewhere. Apps without a completed questionnaire are marked Unrated and may be blocked in certain territories. **Retake the questionnaire whenever content/features change.**

**Data safety form (mandatory for every app, including those collecting no data):** Appears as the "Data safety" section on the listing. You disclose data collection and sharing across categories, encryption in transit, deletion requests, Families policy compliance, independent security review status, and (India) UPI usage. **Must include data collected by all libraries/SDKs and webviews.** The April 10, 2025 policy update reclassified **Android ID** as a device identifier that must be declared under "Device or other IDs" — relevant if any SDK reads `Settings.Secure.ANDROID_ID`. Apps active *only* on internal testing tracks are exempt.

**Target audience & content:** Declare target age group(s); apps including children must comply with the **Families policy** (COPPA/GDPR, family-compliant ad SDKs, neutral age screens). Adult-only apps can enable **Restrict Minor Access** ("18 and over" as the only target group). Must be completed *after* the Ads and App access declarations.

**Ads declaration:** Declare whether the app contains ads (including third-party ad SDKs); apps with ads get a "Contains ads" label.

**Financial features declaration (mandatory for ALL apps since October 30, 2025):** Must be completed for every app on your account, even with no financial features — updates are blocked until it's done. Either declare financial feature categories (banking/loans, payments, trading, etc.) or select "My app doesn't provide any financial features." System services and private apps are exempt.

**Other App content declarations, as applicable:** App access instructions (test credentials for restricted functionality); News app declaration; COVID-19 contact-tracing/status; Health apps declaration (mandatory to complete on the App content page); Government apps; Advertising ID declaration (`AD_ID` permission use and purposes).

**Category & tags:** Application type (App vs Game) and a **single category**, plus up to **5 tags** to refine discovery. (No secondary-category concept; tags fill that role.)

### 3.4 URLs & Contact

| Item | Required? |
|---|---|
| Privacy policy URL | ✅ Required for apps handling sensitive data — active, publicly accessible, non-geofenced, non-editable URL (no PDFs); also link it within the app |
| Support email | ✅ Required (developer contact) |
| Website / phone | Optional |

### 3.5 Platform/SDK Requirements That Gate Publishing

These are binary/technical requirements, but they block store submission, so they belong in the release checklist:

- **Target API level 35 (Android 15):** Since **August 31, 2025**, all new apps and updates must target **API level 35 or higher** (Wear OS/Android Automotive/Android TV: API 34+). Non-compliant apps cannot publish updates and are hidden from new users on newer OS versions.
- **16 KB page-size requirement:** Since **November 1, 2025**, all new apps and updates targeting Android 15 (API 35)+ must support 16 KB page sizes. **This applies to any cross-platform framework that ships native `.so` libraries** (e.g. .NET MAUI's `libmonodroid.so` and runtime libraries, Flutter, React Native) — "apps with no native code" exemption does not apply. Build with an SDK version that produces 16 KB-aligned `.so` files and verify in Play Console's App bundle explorer (look for `PAGE_ALIGNMENT_16K`).
- **Play Billing Library 7+** required for new apps/updates using in-app purchases (since Aug 31, 2025).
- **Developer identity verification** (government ID) required for accounts; **Play Integrity API** replaced the deprecated SafetyNet.

### 3.6 Localization

Metadata (title, short/full description, release notes, screenshots, feature graphic, video) is localizable per language. Category, contact details, and privacy policy remain constant across custom store listings. Up to 50 custom store listings. The Metadata policy applies to **all** translations.

---

## 4. Recommended Publishing Workflow

**Stage 1 — Before you build the listing (these gate submission):**
1. **Apple:** Answer the updated **age-rating questionnaire** (blocks update submissions if missing). Set **`ITSAppUsesNonExemptEncryption`** in `Info.plist` (almost always `false` for a standard app using HTTPS) to bypass the repeated compliance prompt.
2. **Google:** Confirm the Android build **targets API level 35** and produces **16 KB-aligned native libraries**; verify in the App bundle explorer. Complete the **Financial features declaration**, **Data safety form**, **IARC content rating**, **Target audience**, **Ads**, and **App access** declarations, and add a valid **privacy policy URL**.

**Stage 2 — Produce assets once, size per store:**
3. Design **one 1024×1024 icon master with a solid (opaque) background**. Apple: export with **no alpha**. Google: export 512×512 **32-bit PNG with alpha** (≤1 MB). Never round corners yourself on either store.
4. Capture screenshots at the **lead sizes**: Apple **6.9" iPhone (1320×2868)** + **13" iPad (2064×2752)** if iPad-supported; Google phone **1080×1920** (min 2, up to 8). Build Google's mandatory **1024×500 feature graphic**.
5. If producing video: Apple app preview **15–30 s, ≤500 MB, in-app footage, 886×1920 (iPhone)**; Google a **public/unlisted, ads-off YouTube URL**.

**Stage 3 — Write copy to each store's indexing model:**
6. Apple: best keywords in **name (30) + subtitle (30) + keyword field (100)**; no repeated words; use promotional text (170) for evergreen, updatable messaging. Google: weave keywords naturally into **title (30) + short description (80) + full description (4,000)**.
7. Localize metadata for your top markets. Localized listings measurably lift conversion; start with description and (Apple) promotional text since those don't require a new build.

**Thresholds that should change your plan:**
- Any SDK that reads Android ID, advertising ID, or transmits data off-device → expand both the Google Data safety form and the Apple privacy labels. **Re-audit dependencies before every release.**
- Adding social features, user-generated content, or unrestricted web access → expect a **higher age rating on both stores**; re-run both questionnaires.
- Distributing in France, Mainland China, South Korea, or Vietnam → additional Apple compliance fields activate.

---

## 5. Caveats

- **Official vs. secondary sources:** Character limits, questionnaire content, declaration deadlines, and Google's screenshot ranges are taken from Apple's and Google's own documentation. Apple adds device classes with each iPhone/iPad generation — always re-verify screenshot dimensions in App Store Connect at upload time.
- **16 KB extension date:** Community reports mention a Play Console-level extension to ~May 2026 for existing-app updates, but this is not officially confirmed — verify in your own Play Console. The Nov 1, 2025 baseline for apps targeting Android 15+ is official.
- **File-size caps:** Apple publishes no hard per-screenshot file-size cap (practical guidance <8 MB); Google's official 8 MB per-file cap is stated explicitly only for Android XR — treat a universal 8 MB rule as a safe convention, not a documented limit.
- **Self-reported declarations:** Both Apple's privacy labels and Google's Data safety form are self-declared but enforced on discrepancy (Google reported blocking 1.75M+ policy-violating apps and banning 80,000+ developer accounts in 2025). Declare accurately.
- This reference covers **metadata and store-listing requirements** only — not the full App Review Guidelines / Play Developer Program Policies, binary technical requirements beyond §3.5, or pricing/tax setup.

---

## 6. Summary

1. **Apple indexes only 160 characters** (name + subtitle + hidden keyword field) and ignores the description; **Google indexes everything** (title + short + full description) and has no keyword field — write copy per store.
2. **Apple validates screenshots to the exact pixel**; lead with 6.9" iPhone (1320×2868) and 13" iPad (2064×2752). **Google accepts ranges** but additionally requires a 1024×500 feature graphic.
3. **Icons:** one opaque 1024×1024 master; Apple gets no-alpha PNG, Google gets 512×512 PNG *with* alpha. Never round corners yourself.
4. **Declarations gate submission:** Apple's new age-rating questionnaire (deadline Jan 31, 2026) and privacy labels; Google's Data safety form, IARC rating, target audience, ads, app access, and the Financial features declaration (mandatory for every app since Oct 30, 2025).
5. **Cross-platform frameworks shipping native libraries** (MAUI, Flutter, React Native) must meet Google's target API 35 and 16 KB page-size requirements or updates are blocked.
6. **Audit third-party SDKs before every release** — their data collection must be declared in both stores' privacy disclosures.
7. Use the fillable [App Store Publishing Checklist](app-store-publishing-checklist.md) to track all of the above per release.
