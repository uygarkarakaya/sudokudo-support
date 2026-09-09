# sudokudo website

A standalone static website for sudokudo: `/`, `/privacy`, `/support`, and a custom 404. The source is plain HTML/CSS with local SVG branding, system fonts, native accessible FAQ disclosures, and no JavaScript or dependencies. The iOS project is separate and unchanged.

## Preview locally

From this project directory, run:

```sh
python3 scripts/preview.py
```

Open http://127.0.0.1:4173. Stop with Ctrl+C. Python 3 is needed only for this local preview; Vercel serves the files directly. The preview supports the extension-free privacy and support URLs.

## Before publication — owner review required

The website is a completed local draft. Do not treat its privacy wording as a verified legal determination.

- Confirm the public email and operator/contact name. The supplied email `uygarkarakaya@gmail/com` needs correction/confirmation; `uygarkarakaya@gmail.com` has been proposed. The operator name is still pending.
- Replace every `[PUBLIC EMAIL — to be confirmed]` and `[OPERATOR NAME — to be confirmed]` in `dist/privacy.html` and `dist/support.html`. Make the support email a real `mailto:` link after confirmation. No form or fake email is included.
- Set the privacy effective date in `dist/privacy.html`, and confirm your support correspondence retention practices and email service provider. Add applicable operator address/jurisdiction details if needed; none have been invented.
- Review the actual release SDK versions, AdMob settings, mediation partners (if any), regional privacy messages, intended audience/age treatment, purchase availability, and App Store privacy disclosures. The draft is based on the provided app audit, not a new inspection of the iOS repository.
- Confirm the hosting provider and associated processing. If deploying to Vercel, review its hosting privacy terms/logging practices and update the website paragraph as necessary. Analytics and tracking are not included in this site's code; enabling them later requires another review.
- Remove both `.notice` draft banners and pending wording after review. Remove `<meta name="robots" content="noindex, nofollow">` from the three public pages when ready for indexing. Keep it on the 404. Noindex is not access control; use private previews before publication.
- Add canonical URLs only after your public domain is known. No invented App Store URL, purchase packs, or social preview image is included.

Find publication fields with `rg 'pending|confirmed|TO BE|Draft|noindex' dist`.

## GitHub → Vercel

1. Create a new GitHub repository for this website and add this directory's `dist/`, `scripts/`, `README.md`, `vercel.json`, and `.gitignore`. Include the authored `dist/` files; they are the source, not generated build output. Keep `work/` and `outputs/` out of the repository. Do not add this site to the iOS repository.
2. In Vercel, import that GitHub repository. Use the repository root, framework preset **Other**, no install/build command, and output directory **dist**. The included `vercel.json` sets the output directory and clean URLs.
3. Review the deployment, then connect your domain if desired. Git pushes to the connected production branch trigger deployments according to your Vercel project settings.
4. Check `/`, `/privacy`, `/support`, and an unknown path. Use your final `/privacy` and `/support` URLs in App Store Connect when the owner review is complete.

Official deployment references: [Vercel project configuration](https://vercel.com/docs/project-configuration) and [Git deployments](https://vercel.com/docs/git).

## Editing

Edit `dist/index.html`, `dist/privacy.html`, and `dist/support.html` directly. Shared CSS and SVGs are in `dist/assets/`. Navigation/footer markup is repeated in the static HTML; keep those elements consistent when changing them. `.openai/hosting.json` only records the static folder for Sites tooling; it is not used by Vercel, contains no project registration, and may be omitted from GitHub.

## Privacy drafting sources

Checked 9 September 2026:

- [Google Mobile Ads iOS data disclosure](https://developers.google.com/admob/ios/privacy/data-disclosure): SDK data categories and uses.
- [Google UMP for iOS](https://developers.google.com/admob/ios/privacy): privacy choices entry point requirements.
- [Google Privacy Policy](https://policies.google.com/privacy): Google's handling, retention, and user controls.
- [Apple App Store & Privacy](https://www.apple.com/legal/privacy/data/en/app-store/): Apple's purchase processing and data practices.

These sources describe provider practices. They do not independently establish the exact behavior or legal obligations of your configured app.

## Verification

Checked in the browser at desktop (1440 px) and mobile (390 px), with an additional 320 px overflow check on all three pages. Navigation, privacy section anchors, FAQ expansion and Enter-key collapse passed. Local links/assets/fragment targets, image alt text, unique IDs, one main heading per page, configuration JSON, and the custom HTTP 404 response were checked. This was a focused accessibility check, not a formal accessibility audit.

No site was registered, pushed, or published.
