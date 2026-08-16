# Back-fill sources for the App Store metadata reference
**Depth:** deep — the document carries dated compliance claims that gate releases, and its own Caveats
section flags two of them as unconfirmed.

**Date:** 2026-08-16

## Sources

| # | Source | Tier | Retrieved | How |
|---|--------|------|-----------|-----|
| 1 | https://developer.android.com/google/play/requirements/target-sdk | primary | 2026-08-16 | direct fetch (page last updated 2026-08-14) |
| 2 | https://developer.android.com/guide/practices/page-sizes | primary | 2026-08-16 | direct fetch (page last updated 2026-08-05) |
| 3 | https://support.google.com/googleplay/android-developer/answer/9866151 | primary | 2026-08-16 | direct fetch |
| 4 | https://developer.apple.com/help/app-store-connect/reference/screenshot-specifications/ | primary | 2026-08-16 | direct fetch |
| 5 | https://developer.apple.com/news/upcoming-requirements/ | primary | 2026-08-16 | direct fetch |
| 6 | https://support.google.com/googleplay/android-developer/answer/13849271 | primary | 2026-08-16 | direct fetch after the topic-level page [7] carried only a link |

## Not retrieved

| Claim in the document | Why not retrieved |
|---|---|
| Apple text field limits — name 30, subtitle 30, keyword field 100, promotional text 170 | Not fetched in this pass. Still unsourced. |
| Google title 30 and full description 4,000 characters | Google's asset specification page [3] states the 80-character short description limit but does not state these two. Source not located. |
| Play Billing Library 7+ required since Aug 31, 2025 | Not fetched in this pass. Still unsourced. |
| Apple app preview video specs (15–30 s, ≤500 MB, 886×1920) | Not fetched in this pass. Still unsourced. |
| Google's claim of 1.75M+ apps blocked and 80,000+ accounts banned in 2025 | Secondary in the document; primary source not located. |

[7] https://support.google.com/googleplay/android-developer/answer/13327111 — topic page, contained only a
link to [6] rather than the declaration content.

## Raw extracts

### [1] Google Play target API level requirements
> Starting August 31, 2026: New apps and app updates must target Android 16 (API level 36) or higher.
> Exceptions: Wear OS and Android Automotive OS apps: Android 15 (API level 35) or higher; Android TV
> and Android XR apps: Android 14 (API level 34) or higher.
>
> Starting August 31, 2026: Existing apps must target Android 15 (API level 35) or higher to remain
> available to new users on devices running Android OS higher than the app's target API level.
>
> Developers can request an extension to November 1, 2026 through extension forms in Play Console.

Page last updated 2026-08-14 UTC.

### [2] 16 KB page sizes
> To ensure your app works correctly on the latest versions of Android, all apps targeting Android 15
> (API level 35) and higher must support 16 KB memory page sizes on 64-bit devices on Google Play.
> Starting February 1, 2027, if your app updates don't support 16 KB memory page sizes, you won't be
> able to release these updates.

Page last updated 2026-08-05 UTC. No other extension or deadline appears on the page.

### [3] Google Play asset specifications
> Short description: 80 character limit
> App icon: 32-bit PNG (with alpha). Dimensions: 512px by 512px. Maximum file size: 1024KB.
> Feature graphic: JPEG or 24-bit PNG (no alpha). Dimensions: 1024px by 500px.
> Screenshots: JPEG or 24-bit PNG (no alpha). Minimum dimension: 320px. Maximum dimension: 3840px.
> The maximum dimension of your screenshot can't be more than twice as long as the minimum dimension.

### [4] Apple screenshot specifications
> 1 to 10 screenshots in .jpeg, .jpg, and .png formats. Images can't include alpha channels or
> transparencies.
>
> 6.9" Display — Required if app runs on iPhone: 1320 x 2868 portrait (also 1290 x 2796, 1260 x 2736).
> 6.5" Display — Required if app runs on iPhone and screenshots for 6.9" display aren't provided.
> 13" Display — Required if app runs on iPad: 2064 x 2752 portrait (also 2048 x 2732).

### [5] Apple upcoming requirements
> Since April 28, 2026 — Apps uploaded to App Store Connect must be built with Xcode 26 or later using
> an SDK for iOS 26, iPadOS 26, tvOS 26, visionOS 26, or watchOS 26.
>
> Since January 31, 2026 — Ratings for all apps have been automatically updated to align with the new
> age rating system. Provide responses to updated age rating questions for each app to avoid
> interruption when submitting app updates.

### [6] Financial features declaration
> All developers that have an app published on Google Play must complete the Financial features
> declaration, including apps on closed testing, open testing, or production tracks.

The page states the declaration became mandatory by August 31, 2023. The document under review states
October 30, 2025.

## Findings

1. **The target API claim is out of date and understates the requirement.** The document states API
   level 35 has been required since August 31, 2025. As of 2026-08-16 the requirement is **API level 36
   for new apps and updates from August 31, 2026**, with API 35 the floor for existing apps to stay
   available to new users, and an extension available to November 1, 2026. The deadline is 15 days
   away at time of writing. Source: [1].

2. **The 16 KB enforcement date moved, and the document's own open question is now settled.** The
   document states enforcement from November 1, 2025, and its Caveats section records an unconfirmed
   community report of an extension to around May 2026. The primary source now gives a single
   enforcement date of **February 1, 2027** for blocking non-compliant updates. The community report
   was directionally right and wrong on the date; the caveat can be replaced with a sourced fact.
   Source: [2].

3. **A publishing gate is missing entirely.** Apple has required builds made with **Xcode 26 and the
   iOS 26 SDK since April 28, 2026**. The document's §3.5 covers Google's gating requirements but has
   no Apple equivalent, so a reader following it would miss this. Source: [5].

4. **The Apple age-rating claim is correct but written in the future tense.** The document calls
   January 31, 2026 a deadline; it has passed. The requirement stands and unanswered questionnaires
   interrupt update submission. Source: [5].

5. **Apple screenshot and Google asset claims check out.** 6.9" iPhone at 1320×2868 and 13" iPad at
   2064×2752 are the required lead sizes, alpha channels are rejected, and the range is 1–10
   screenshots [4]. Google's 512×512 32-bit PNG icon with alpha at ≤1024 KB, the 1024×500 feature
   graphic as JPEG or 24-bit PNG without alpha, and the 80-character short description all match [3].

6. **The Google screenshot specification in §3.2 is already stated correctly** — min 320px, max 3840px,
   maximum side no more than twice the minimum, with 1080×1920 named as a community standard [3]. The
   §4 workflow step drops that qualifier and presents 1080×1920 as the target; harmless in practice,
   but the two sections should agree.

7. **The Financial features declaration date conflicts and is unresolved.** The document says mandatory
   for every app since October 30, 2025; the primary page says August 31, 2023 [6]. Both may be true of
   different phases of the rollout, and the page fetched did not separate them. Neither date should be
   stated as fact without a Play Console check.

8. **Roughly a third of the document's checkable claims remain unsourced**, listed under Not retrieved
   above. The Apple text-field limits in particular carry the document's core §2 guidance and were not
   verified in this pass.

## What was done with this record

The corrections in findings 1–3 were **not** copied into the reference document. On review, dated
compliance values were judged to be the wrong thing for a knowledge base to hold at all — they go
wrong invisibly. §4 of the reference now lists the gates and points at the vendor pages, carrying no
numbers or dates. The general rule is in
[Knowledge Management with AI](../../KnowledgeBase/WorkingWithAI/knowledge-management-with-ai.md) §5.

Findings 5 and 6 (asset specifications) were captured with references, because there the value is the
knowledge. The unsourced claims listed above remain unsourced and are marked as such in the document.
