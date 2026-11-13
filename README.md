# jimmy-sim.github.io

My personal website: [jimmy-sim.github.io](https://jimmy-sim.github.io/).

Built with plain HTML, CSS, and JavaScript. No dependencies or build step.

## Editing

- `index.html` — Home and biography
- `education.html` — Education and coursework
- `projects.html` — Project listing
- `projects/` — Detailed project articles
- `resume.pdf` — Downloadable résumé
- `assets/css/` and `assets/js/` — Shared styles and scripts
- `assets/images/` — Home-page portrait
- Other `assets/` folders — Project figures, papers, and code
- `docs/` — Editing guides and content sources

See [the editing guide](docs/EDITING.md) for instructions and [content sources](docs/CONTENT-SOURCES.md) for source notes.

## Preview

Open `index.html` in your browser, or run:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Then visit `http://localhost:8000` on your computer.

## Publish

Commit and push to `main`. GitHub Pages publishes from `main` → `/ (root)`. Check the repository’s **Actions** tab for deployment status.
