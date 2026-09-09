# sudokudo website

A standalone static website for sudokudo: `/`, `/privacy`, `/support`, and a custom 404. The source is plain HTML/CSS with local SVG branding, system fonts, native accessible FAQ disclosures, and no JavaScript or dependencies. The iOS project is separate and unchanged.

## Preview locally

From this project directory, run:

```sh
python3 scripts/preview.py
```

Open http://127.0.0.1:4173. Stop with Ctrl+C. Python 3 is needed only for this local preview; GitHub Pages serves the prepared files directly. The preview supports the extension-free privacy and support URLs.

## Before publication — owner review required

The website is a completed local draft. Do not treat its privacy wording as a verified legal determination.

- The confirmed public support and privacy email is `uygarkarakaya@gmail.com`. The operator/contact name is still pending.
- Replace every `[OPERATOR NAME — to be confirmed]` in `dist/privacy.html` and `dist/support.html`. The confirmed email is already linked with `mailto:` on both pages.
- Set the privacy effective date in `dist/privacy.html`, and confirm your support correspondence retention practices and email service provider. Add applicable operator address/jurisdiction details if needed; none have been invented.
- Review the actual release SDK versions, AdMob settings, mediation partners (if any), regional privacy messages, intended audience/age treatment, purchase availability, and App Store privacy disclosures. The draft is based on the provided app audit, not a new inspection of the iOS repository.
- Confirm the hosting provider and associated processing. For GitHub Pages, review GitHub’s hosting privacy terms/logging practices and update the website paragraph as necessary. Analytics and tracking are not included in this site's code; enabling them later requires another review.
- Remove both `.notice` draft banners and pending wording after review. Remove `<meta name="robots" content="noindex, nofollow">` from the three public pages when ready for indexing. Keep it on the 404. Noindex is not access control; use private previews before publication.
- Add canonical URLs only after your public domain is known. No invented App Store URL, purchase packs, or social preview image is included.

Find publication fields with `rg 'pending|confirmed|TO BE|Draft|noindex' dist`.

## Deploy with GitHub Pages

1. Create a GitHub repository (for example `sudokudo-website`). A public repository works with GitHub Free. Upload this project's contents to its `main` branch, including `dist/`, `scripts/`, and **`.github/workflows/pages.yml`**. The `.github` folder is hidden in some file browsers; make sure it is included. Keep `work/`, `outputs/`, and `_site/` out of Git.
2. Open the repository's **Settings → Pages → Build and deployment → Source**, and select **GitHub Actions**. You do not need to select a template: the workflow is already included.
3. Open **Actions → Deploy GitHub Pages → Run workflow**, choose `main`, and run it. Future pushes to `main` redeploy automatically. If your branch has another name, change `branches: [main]` in the workflow first.
4. Wait for the workflow to succeed, then open the URL shown in **Settings → Pages**. A project site normally uses `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/`. Your policy and support URLs end in `/privacy/` and `/support/`.

The workflow prepares `_site/` from the authored `dist/` files. It automatically prefixes links/assets with the repository path and converts privacy/support to directory index pages because GitHub Pages does not use Vercel's clean-URL rules. User sites and configured custom domains also work without hardcoding a repository name. `vercel.json` is an optional leftover for Vercel and is ignored by GitHub Pages.

To inspect the generated files locally:

```sh
python3 scripts/build_pages.py
python3 -m http.server 4173 --directory _site
```

Open http://localhost:4173. Use `PAGES_BASE_PATH=/example-repo python3 scripts/build_pages.py` to check project-path generation. A server serving `_site` directly will not mount that prefix automatically.

Finish the publication checklist above before publishing. GitHub Pages is a public website in this setup; a private repository does not by itself make its Pages site private.

Official instructions: [Configure a publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) and [custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Editing

Edit `dist/index.html`, `dist/privacy.html`, and `dist/support.html` directly. Shared CSS and SVGs are in `dist/assets/`. Navigation/footer markup is repeated in the static HTML; keep those elements consistent when changing them. `.openai/hosting.json` only records the static folder for Sites tooling; it is not used by GitHub Pages or Vercel, contains no project registration, and may be omitted from GitHub.

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

GitHub Pages adaptation: generated and checked both domain-root and repository-prefix output, including privacy/support directory routes, assets, and 404 navigation. Deployment itself has not been run.
