# Jimmy Youngjae Sim — personal website

A small, academic-style website made with plain HTML, CSS, and JavaScript. There are no dependencies or build steps. The layout takes inspiration from Matteo Santamaria’s personal site: a compact masthead, narrow reading column, restrained typography, and separate pages.

## Future edits

Start with [EDITING.md](EDITING.md) for GitHub editing, local previews, common changes, publishing, and recovery. `AGENTS.md` provides maintenance guidance for future Codex tasks. The optional `scripts/publish.sh` helper publishes only named files using Jimmy’s Git identity.

## Pages and files

- `index.html` — home, a brief introduction, and selected work.
- `about.html` — biography, technical interests, activities, and résumé PDF link.
- `education.html` — schools, degree plans, and coursework.
- `projects.html` — research and technical projects.
- `retinal-imaging.html` and `pothole-detection.html` — research notes with paper-reported results.
- `assets/papers/` — original CVD JSR paper and pothole CJSJ submission PDFs.
- `stock-prediction.html` — a short research note linked from Projects.
- `assets/stock-prediction/` — original AAPL plots and archived Python/notebook source.
- `resume.pdf` — the latest uploaded résumé.
- `headshot.png` — portrait on the home page.
- `outdoor.jpg` — personal photo on the About page.
- `styles.css` — shared layout, typography, mobile, and print styles.
- `script.js` — optional automatic copyright year. All navigation works without JavaScript.

## Preview

Open `index.html` directly in a browser, or run a local server from the repository directory:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

On your computer, visit `http://localhost:8000`. Stop the server with **Ctrl+C**. In a cloud terminal, use local HTTP requests for checks; the loopback address is not a public preview URL.

## Content sources

Current Berkeley information and the downloadable résumé come from the more recent résumé and Jimmy’s direct updates. Additional high-school activities and project details come from the older, detailed high-school résumé. Historical “Present” labels are not carried forward as current roles. High-school activities are summarized briefly; detailed awards and activities are left to the résumé. The source résumés disagree on USACO division, so confirm it before adding that distinction. The older document is not published as a second résumé.

## Maintain the site

1. Open the HTML file for the page you want to change and edit the content inside `<main>`.
2. To add a project, copy an entire project `<article>` in `projects.html`. Give it a unique `id` if you want to link directly to it. Selected projects on the home page link to these IDs.
3. Add public code or paper URLs when available; none are invented for projects without supplied links.
4. Replace `resume.pdf` to update the downloadable document and refresh the `?v=` value on its links in Home and About to avoid cached older copies. The expected graduation date is May 2029, reflecting Jimmy’s confirmed three-year plan using high-school credits.
5. Replace `headshot.png` or `outdoor.jpg` to change the photos. Keep the HTML image dimensions and descriptive `alt` text up to date if a replacement differs. Photos keep their original proportions and stack with the text on mobile.
6. Change colors and typography in `styles.css`; they apply to every page.
7. The header and footer are deliberately repeated in the HTML files to avoid a build system. If you change a navigation link, name, or footer, update every page. Each page marks its own navigation link with `aria-current="page"`.

Use relative file links such as `education.html` and `resume.pdf` so the site works both locally and on GitHub Pages. Filenames and link capitalization must match.

## Publish with GitHub Pages

Commit and push the files to `main` in `jimmy-sim/jimmy-sim.github.io`. In **Settings → Pages**, select **Deploy from a branch → main → / (root)** and save. No custom Actions workflow or framework is required.

After deployment succeeds, the site should be available at `https://jimmy-sim.github.io/`. Future pushes to `main` trigger updates. Use the repository’s Actions tab to check deployment status if an update does not appear.

## Before publishing changes

- Open each page directly and follow its navigation links.
- Check narrow mobile and desktop widths for readable text and overflow.
- Use Tab to check visible keyboard focus and the “Skip to content” link.
- Open and download the résumé PDF.
- Review dates, descriptions, contact details, and all public links.

There is no compilation step or committed test suite. The site uses no external fonts, analytics, or JavaScript libraries.

## Project notes

The stock-prediction note is a curated summary inspired by the article format of the reference site. Its two plots are original image assets extracted unchanged from the supplied Keynote, not regenerated results. The Keynote and converted slide deck are not published. The note distinguishes visual observations from reproducible benchmark claims. Keep new notes concise and link them from their project entries.

The stock note also includes the supplied Colab code as a Python export and a notebook reconstructed from its three model sections. Executable logic is unchanged; only the generated Colab header was replaced with setup/provenance notes. Neither file contains executed outputs. The dataset and pinned dependency versions were not supplied; model training has not been revalidated in this website environment.

The retinal-imaging note follows the supplied JSR paper’s exact title and coauthor list. The pothole note links the CJSJ semifinalist submission, clearly distinguished from publication. Both PDFs are preserved unchanged. Research-note tables transcribe reported results; no research experiments were rerun. The CVD PDF is the authoritative linked paper; the older résumé DOI was not verified against its title and is not used in its place.
