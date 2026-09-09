# sudokudo website

A standalone static website for sudokudo: `/`, `/privacy`, `/support`, and a custom 404. The source is plain HTML/CSS with local SVG branding, system fonts, native accessible FAQ disclosures, and no JavaScript or dependencies. The iOS project is separate and unchanged.

## Preview locally

From this project directory, run:

```sh
python3 scripts/preview.py
```

Open http://127.0.0.1:4173. Stop with Ctrl+C. Python 3 is needed only for this local preview. The preview supports the extension-free privacy and support URLs.

## Public URLs

Vercel is the canonical deployment used for App Store and AdMob metadata:

- Website and Marketing URL: `https://sudokudo-support.vercel.app/`
- Privacy Policy URL: `https://sudokudo-support.vercel.app/privacy`
- Support URL: `https://sudokudo-support.vercel.app/support`
- AdMob seller file: `https://sudokudo-support.vercel.app/app-ads.txt`

`dist/app-ads.txt` contains the AdMob publisher entry and must remain available at the Vercel domain root. GitHub Pages remains a supported mirror, but its project-path URL should not be used as the App Store Marketing URL because AdMob looks for `/app-ads.txt` at the hostname root.

The privacy policy identifies Uygar Karakaya as the operator, uses 9 September 2026 as its effective date, describes the enabled StoreKit consumables, and identifies Vercel and GitHub Pages as hosting providers. Re-review the policy if SDKs, ad partners, analytics, purchases, contact details, or data handling change.

## Deploy with GitHub Pages

1. Create a GitHub repository (for example `sudokudo-website`). A public repository works with GitHub Free. Upload this project's contents to its `main` branch, including `dist/`, `scripts/`, and **`.github/workflows/pages.yml`**. The `.github` folder is hidden in some file browsers; make sure it is included. Keep `work/`, `outputs/`, and `_site/` out of Git.
2. Open the repository's **Settings → Pages → Build and deployment → Source**, and select **GitHub Actions**. You do not need to select a template: the workflow is already included.
3. Open **Actions → Deploy GitHub Pages → Run workflow**, choose `main`, and run it. Future pushes to `main` redeploy automatically. If your branch has another name, change `branches: [main]` in the workflow first.
4. Wait for the workflow to succeed, then open the URL shown in **Settings → Pages**. A project site normally uses `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/`. Your policy and support URLs end in `/privacy/` and `/support/`.

The workflow prepares `_site/` from the authored `dist/` files. It automatically prefixes links/assets with the repository path and converts privacy/support to directory index pages because GitHub Pages does not use Vercel's clean-URL rules. User sites and configured custom domains also work without hardcoding a repository name. `vercel.json` configures the canonical Vercel deployment and is ignored by GitHub Pages.

To inspect the generated files locally:

```sh
python3 scripts/build_pages.py
python3 -m http.server 4173 --directory _site
```

Open http://localhost:4173. Use `PAGES_BASE_PATH=/example-repo python3 scripts/build_pages.py` to check project-path generation. A server serving `_site` directly will not mount that prefix automatically.

GitHub Pages is a public mirror in this setup; a private repository does not by itself make its Pages site private.

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

The canonical site is deployed at `https://sudokudo-support.vercel.app/`. GitHub Pages adaptation has been checked for both domain-root and repository-prefix output, including privacy/support directory routes, assets, and 404 navigation.
