# 11ty Build Setup

This folder contains the 11ty setup to centralize shared layout (header/footer) and reduce duplication.

## Build
1. Install dependencies:
   ```bash
   npm install
   ```
2. Build to `docs/`:
   ```bash
   npx @11ty/eleventy
   ```

## Notes
- Source templates live in `site/src/pages/`.
- Shared partials live in `site/src/_includes/`.
- `docs/` is the publish output (GitHub Pages should point to `/docs`).
