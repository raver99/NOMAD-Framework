# 📋 App Store Publishing Checklist – Fillable Metadata & Assets Worksheet

## Purpose of This Document

A fill-out worksheet that collects every piece of metadata, every asset, and every declaration needed to publish an app on the Apple App Store and Google Play Store. Copy this file per app (or per release), fill in the **Value** columns, and tick the checkboxes as items are completed. For limits, exact specifications, and the reasoning behind each item, see the [App Store Metadata Requirements Reference](app-store-metadata-reference.md).

> **How to use:** Duplicate this file into your app's project (e.g. `store-listing-<appname>.md`). Fill it out once per app, then re-review sections 1, 6, and 7 on every release.

---

## 1. Pre-Submission Gates

These block submission entirely — clear them before working on the listing.

### 1.1 Apple

- [ ] Age-rating questionnaire answered in App Store Connect (App Information) — new 2026 questionnaire with 13+/16+/18+ tiers
- [ ] `ITSAppUsesNonExemptEncryption` set in iOS `Info.plist` — value: `false` (HTTPS only) / `true` (custom crypto): `______`
- [ ] If `true`: annual U.S. BIS self-classification report planned (due Feb 1)
- [ ] App Privacy "nutrition labels" completed (see section 4.3)
- [ ] Contact information for App Review filled in

### 1.2 Google

- [ ] Build targets **API level 35+** (Wear OS/Automotive/TV: 34+)
- [ ] Native `.so` libraries are **16 KB page-aligned** — verified in App bundle explorer (`PAGE_ALIGNMENT_16K`)
- [ ] Play Billing Library **7+** (if using in-app purchases)
- [ ] Financial features declaration completed (mandatory for every app)
- [ ] Data safety form completed (see section 5.3)
- [ ] IARC content rating questionnaire completed
- [ ] Target audience & content declared
- [ ] Ads declaration completed
- [ ] App access instructions provided (test credentials if functionality is restricted)
- [ ] Health apps declaration completed (mandatory to answer, even if N/A)
- [ ] Developer identity verification done (account-level)

---

## 2. App Identity (Both Stores)

| Item | Value |
|---|---|
| App name (working title) | |
| Bundle ID (iOS) | |
| Package name (Android) | |
| Primary language/locale | |
| Category — Apple primary | |
| Category — Apple secondary (optional) | |
| Category — Google (single) | |
| Google tags (up to 5) | |
| Copyright holder (Apple) | |
| Developer name (Google) | |

---

## 3. Text Copy Worksheet

### 3.1 Apple (indexed budget: 160 chars — never repeat a word across name/subtitle/keywords)

| Field | Limit | Value |
|---|---|---|
| App name | 30 | |
| Subtitle | 30 | |
| Keywords (comma-separated, no spaces after commas, no plurals) | 100 | |
| Promotional text (editable anytime) | 170 | |
| Description | 4,000 | *(link or paste)* |
| What's New / release notes | 4,000 | |
| Notes for App Review (demo credentials, test setup) | 4,000 | |

- [ ] No word repeated across name / subtitle / keywords
- [ ] No trademarks or competitor names in keywords
- [ ] No "free/best" or misleading claims in name

### 3.2 Google (title + short + full description are all indexed)

| Field | Limit | Value |
|---|---|---|
| App title | 30 | |
| Short description | 80 | |
| Full description | 4,000 | *(link or paste)* |
| Release notes ("What's new") | 500 per language | |

- [ ] Keywords woven naturally into title, short, and full description (no stuffing/word lists)
- [ ] No emojis, ALL CAPS, "Free/No Ads/#1/Best", or ranking text in title

---

## 4. Apple — Assets, Declarations & URLs

### 4.1 Assets

- [ ] App icon **1024×1024 PNG, sRGB, no alpha, no pre-rounded corners** — file: `______`
- [ ] Screenshots **6.9" iPhone (1320×2868)** — count (1–10): `______`
- [ ] Screenshots **13" iPad (2064×2752)** — required if app runs on iPad — count: `______`
- [ ] Screenshots for other supported platforms (Mac / TV / Vision / Watch): `______`
- [ ] First 2–3 screenshots carry the core message (visible in search results)
- [ ] App preview video(s) — optional, max 3 per localization, **15–30 s, ≤500 MB, 30 fps, in-app footage only**, iPhone 886×1920 — file(s): `______`
- [ ] Poster frame set deliberately after upload

### 4.2 Declarations

- [ ] Age-rating questionnaire (see 1.1) — resulting rating: `______`
- [ ] Content rights (third-party content) declared
- [ ] Regulated medical device status (if applicable)
- [ ] EU Digital Services Act trader information
- [ ] Region-specific compliance (France crypto / China / South Korea / Vietnam) — applicable: `______`

### 4.3 Privacy Labels

- [ ] All third-party SDKs audited for data collection (analytics, crash reporting, ads)
- [ ] Data Used to Track You — categories: `______`
- [ ] Data Linked to You — categories: `______`
- [ ] Data Not Linked to You — categories: `______`

### 4.4 URLs

| URL | Required | Value |
|---|---|---|
| Support URL | ✅ | |
| Privacy Policy URL | ✅ | |
| Marketing URL | optional | |
| Privacy Choices URL | optional | |

---

## 5. Google — Assets, Declarations & URLs

### 5.1 Assets

- [ ] App icon **512×512, 32-bit PNG with alpha, ≤1 MB, no rounded corners** — file: `______`
- [ ] Feature graphic **1024×500, JPEG/24-bit PNG, no alpha** — file: `______`
- [ ] Phone screenshots (min 2, max 8) — recommended 1080×1920, JPEG/24-bit PNG no alpha — count: `______`
- [ ] ≥4 screenshots at ≥1080 px for large-screen recommendation eligibility (7"/10" tablet sets)
- [ ] Alt text (≤140 chars) added per asset
- [ ] Device-specific assets if applicable: Wear OS (1:1, ≥384×384) / TV screenshot + banner 1280×720 / Android XR (4–8, 8:5, ≤8 MB): `______`
- [ ] Preview video — YouTube URL, **public/unlisted, ads off, embeddable, not age-restricted**: `______`

### 5.2 Declarations

- [ ] IARC content rating — resulting rating(s): `______`
- [ ] Financial features declaration — selection: `______`
- [ ] Target audience age group(s): `______`
- [ ] Families policy compliance (if children included)
- [ ] Ads declaration — contains ads: yes / no: `______`
- [ ] Advertising ID (`AD_ID`) declaration (if used) — purposes: `______`
- [ ] Other applicable: News / COVID-19 / Government apps: `______`

### 5.3 Data Safety Form

- [ ] All SDKs, libraries, and webviews audited for data collection
- [ ] Android ID usage checked (`Settings.Secure.ANDROID_ID` — declare under "Device or other IDs" if any SDK reads it)
- [ ] Data collected/shared — categories: `______`
- [ ] Encrypted in transit: yes / no
- [ ] Users can request deletion: yes / no

### 5.4 URLs & Contact

| Item | Required | Value |
|---|---|---|
| Privacy policy URL (public, no PDF, also linked in-app) | ✅ | |
| Support email | ✅ | |
| Website | optional | |
| Phone | optional | |

---

## 6. Localization

| Language/locale | Apple copy | Apple screenshots | Google copy | Google screenshots |
|---|---|---|---|---|
| *(primary)* | ☐ | ☐ | ☐ | ☐ |
| | ☐ | ☐ | ☐ | ☐ |
| | ☐ | ☐ | ☐ | ☐ |

- [ ] Description + keywords translated per locale (these do NOT inherit from the primary language on Apple)
- [ ] Apple two-locale keyword indexing exploited for key storefronts (e.g. en-US + es-MX in the U.S.)

---

## 7. Every-Release Re-Check

Run through this list for **each** update, not just the first release:

- [ ] Release notes written (Apple ≤4,000 / Google ≤500 per language, non-promotional)
- [ ] New SDKs/dependencies audited → Apple privacy labels and Google Data safety form still accurate
- [ ] Content/feature changes reviewed → age-rating questionnaires re-run if social features, UGC, or web access were added
- [ ] Screenshots still match current UI (and current device-class requirements — Apple adds classes with each hardware generation)
- [ ] Google: target API level still meets the current Play requirement
- [ ] Apple: encryption answer still correct for this version

---

## 8. Summary

1. **Section 1 gates everything** — clear the declarations and technical requirements before polishing copy or assets.
2. **Fill sections 2–5 once per app**, keeping this file as the single source of truth for the listing.
3. **Sections 6–7 recur** — localization grows over time, and the every-release re-check catches the silent blockers (SDK audits, API levels, re-triggered questionnaires).
