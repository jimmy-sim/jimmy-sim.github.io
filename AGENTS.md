# Website maintenance

This is Jimmy Youngjae Sim’s plain HTML/CSS/JavaScript academic website, published from `main` in `jimmy-sim/jimmy-sim.github.io`. Read README.md and EDITING.md for file mapping and the beginner workflow.

- Use this existing isolated checkout; do not create a worktree unless requested.
- Preserve the minimal academic design, separate pages, content, photos, and résumé unless the user requests changes. Do not introduce frameworks, package dependencies, external fonts, or a build step for routine edits.
- Keep high-school activities and awards minimal. Prefer a short background summary; reserve detailed activity lists, competition results, and minor internships for the résumé. Keep substantive research contributions and publication links.
- Keep the shared navigation and footer consistent in all six pages. Preserve `aria-current`, skip links, descriptive image alt text, natural image proportions, and responsive layouts.
- Prefer the user’s latest statements and recent résumé over older documents. Current education: UC Berkeley Applied Mathematics, intended Computer Science double major, August 2026–May 2030 expected. Do not invent publications, project links, credentials, dates, or honors. Historical high-school “Present” labels do not establish current activity.
- Review the working tree and fetch before publishing. Preserve user edits and uploads. This repository was recreated with fresh history; do not merge or push history from its deleted predecessor or local backups.
- Use commit author and committer `Jimmy Sim <77947780+jimmy-sim@users.noreply.github.com>`. Verify actual commit metadata before pushing. Do not use the Codex account owner’s default Git identity.
- For an explicitly requested publication, use a normal push to `origin HEAD:main`. Do not force-push, rewrite history, delete repositories, or change Pages settings for routine edits. If the user only requests advice or a draft, do not publish.
- Check `git diff --check`. For JavaScript changes use `node --check script.js` when Node is available. For layout/navigation changes, check affected pages in a browser at mobile and desktop widths, local links and anchors, image loading/proportions, and the PDF if affected. Keep any temporary browser tooling outside the repository. Do not add tests that merely mirror content edits.
- No installation is required. Open index.html directly, or use Python’s local HTTP server for internal validation. Do not present loopback links as public cloud previews. Live processes do not persist between cloud tasks.
- Keep the user informed about what was changed, verified, committed, and pushed. A successful push is not proof that GitHub Pages deployed. GitHub API access may be blocked even when Git reads and pushes work; do not claim settings or contributor lists were changed without evidence.
