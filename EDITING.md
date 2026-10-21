# Editing your website

Your live site is **https://jimmy-sim.github.io/**. Its files live in **jimmy-sim/jimmy-sim.github.io**. Editing a file changes the site only after you commit, push to `main`, and GitHub Pages finishes deploying.

## Three ways to make changes

### Ask Codex

Open a task using this repository and describe the result you want. For example:

> In projects.html, add the following project below the optimization entry: [title, dates, description, link]. Keep the current design, check mobile layouts, and publish to main using my Jimmy Sim Git identity.

For a draft, add “Do not commit or push yet.” Attach a new résumé or supply project links when needed. If a photo attachment cannot be read in the cloud workspace, upload it directly to the repository through GitHub.

### Edit on GitHub — easiest for small text changes

1. Open the repository’s **Code** tab and select the file from the table below.
2. Click the pencil (**Edit this file**).
3. Edit the words between the HTML tags, keeping the surrounding tags in place.
4. Choose **Commit changes**, write a short description, and commit to `main`.
5. Check the **Actions** tab for a successful Pages deployment, then refresh the live page.

Use your own `jimmy-sim` account when editing. GitHub’s editor does not provide a rendered preview of an HTML page; for layout changes, preview locally first.

### Edit on your Mac — best for layout or several files

Install Git and a text editor such as VS Code. Clone the **new** repository into a new folder; do not reuse a clone containing the deleted repository’s history:

```sh
git clone https://github.com/jimmy-sim/jimmy-sim.github.io.git
cd jimmy-sim.github.io
git config --local user.name "Jimmy Sim"
git config --local user.email "77947780+jimmy-sim@users.noreply.github.com"
```

Before each editing session, run `git pull --ff-only` from this folder. If Git reports local changes or a conflict, stop and resolve it rather than discarding work.

Open `index.html` in your browser and follow its links. No installation or build is needed. Optionally, if Python 3 is installed, run `python3 -m http.server 8000 --bind 127.0.0.1` and visit `http://localhost:8000` on your Mac. Stop with Ctrl+C. This local address is not a public preview.

## Which file to edit

| Change | File |
| --- | --- |
| Home introduction and selected work | `index.html` |
| Biography, activities, honors | `about.html` |
| Schools, coursework, graduation date | `education.html` |
| Project descriptions and paper/code links | `projects.html` |
| Stock-prediction project note and selected plots | `stock-prediction.html` and `assets/stock-prediction/` |
| Résumé summary | `resume.html` |
| Downloadable résumé | Replace `resume.pdf` |
| Email and profile links | Footer links in all HTML pages |
| Headshot | Replace `headshot.png`; update its width, height, and alt text in `index.html` |
| Outdoor photo | Replace `outdoor.jpg`; update its dimensions and alt text in `about.html` |
| Fonts, spacing, colors, mobile layout | `styles.css` |
| Automatic copyright year | `script.js` |

The HTML pages each include their own header and footer. Changes to navigation, your displayed name, or footer links must be repeated across every page. The active navigation link uses `aria-current="page"`.

## Common edits

**Add a project:** copy an entire `<article class="entry" ...>...</article>` in `projects.html`, then replace its title, dates, and paragraph. Give it a unique ID such as `id="new-project"`. Link to it from Home using `projects.html#new-project` if you want it featured.

**Add a link:** use `<a href="https://example.com">Descriptive link text</a>`. For local files use `resume.pdf` or `education.html`. Match capitalization exactly.

**Stylesheet caching:** each page’s stylesheet URL includes a `?v=` version. After changing `styles.css`, change that version to the same new value in every page pages so visitors receive the new styles. Footer SVGs also have explicit dimensions so they remain visible with older styles.

**Write special characters:** write `&amp;` for an ampersand in HTML text and `&lt;` for a literal less-than sign. Keep attribute values inside quotes.

**Replace a photo or PDF:** keep the existing filename so links continue working. Use a JPEG or PNG for photos and check that the résumé is a real PDF. Update the HTML dimensions to match a new image’s pixel dimensions; CSS displays it at a smaller size without distortion. Do not put private information in public files.

## Check and publish from your Mac

1. Preview every page you changed. Check a narrow phone-sized window and a desktop window.
2. Follow links, view the photos, and open the résumé. Tab through links to check keyboard focus.
3. Review your changes with `git diff`. If Node.js is available and you edited JavaScript, run `node --check script.js`.
4. Run the helper with a description and **only the files you edited**:

   ```sh
   bash scripts/publish.sh "Update my biography" about.html
   ```

   Or, for a résumé update:

   ```sh
   bash scripts/publish.sh "Update my resume" resume.pdf resume.html
   ```

The helper checks whitespace, stages the named files, commits using your Jimmy Sim identity, and pushes to `main`. It does not check the visual layout or external links. It refuses to proceed if other changes are already staged. A rejected push leaves your commit safe locally; do not force-push. Ask Codex to help reconcile remote updates.

You can also publish manually:

```sh
git diff --check
git add about.html
git commit -m "Update my biography"
git push origin HEAD:main
```

GitHub may prompt you to authenticate on your Mac. Use your own account. The commit identity controls attribution; the connected account controls the push. Never paste a password or token into a source file or chat.

## Fix a mistake

For a published text mistake, edit it and commit the correction. For a whole bad commit, ask Codex to revert that specific commit; a revert preserves history and is safer than resetting or force-pushing. On GitHub, the file’s **History** view lets you inspect previous versions and copy back text.

If a change is missing online, check **Actions** first, then refresh the browser cache. For a 404, check the exact filename and **Settings → Pages → main → / (root)**. Keep the current layout unless you deliberately want a redesign.

## Known content items

- The web pages correctly use **May 2030** for expected graduation, but the current résumé PDF still says **May 2029**. Replace the PDF when ready.
- The recent résumé says **USACO Gold**; the older high-school résumé says **Platinum**. The site omits that distinction; confirm it before adding it back.
