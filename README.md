# Jimmy Youngjae Sim

My personal website: [jimmy-sim.github.io](https://jimmy-sim.github.io/).

Built with plain HTML, CSS, and JavaScript. No dependencies or build step.

## Editing

- `index.html` — Home and biography
- `education.html` — Education and coursework
- `projects.html` — Project listing; individual projects have their own HTML pages
- `resume.pdf` — Downloadable résumé
- `styles.css` — Shared appearance and mobile layout
- `assets/` — Project figures, papers, and code

See [EDITING.md](EDITING.md) for detailed editing instructions and [CONTENT-SOURCES.md](CONTENT-SOURCES.md) for source notes.

## Preview

Open `index.html` in your browser, or run:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Then visit `http://localhost:8000` on your computer.

## Publish

Commit and push to `main`. GitHub Pages publishes from `main` → `/ (root)`. Check the repository’s **Actions** tab for deployment status.
