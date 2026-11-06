# Battery Passport Network — Redesign

A responsive, high-fidelity redesign of the [Battery Passport Network](https://battery-passport-network-e1d6.vercel.app) platform built with an industrial design aesthetic inspired by materials inside a battery pack (brushed graphite, pale ceramic surfaces, fine etched lines, layered battery cell SVG illustration, and a quiet circuit trace pulse background animation).

## Project Structure

```
.
├── battery-passport-redesign/   # The redesigned website (Production)
│   ├── index.html               # Semantic HTML5 with all 11 pages and SVG artwork
│   ├── styles.css               # Brushed graphite & pale ceramic design system
│   └── app.js                  # Routing, deep linking, interactive states & Chart.js
├── original/                    # Preserved original deployment files
│   └── index.html
├── verify.py                    # Programmatic text & route fidelity audit
├── test_interactions.mjs        # Automated browser test suite (CDP)
└── README.md
```

## Visual Direction Highlights

- **Palette:** Brushed Graphite (`#080D0B`, `#0D1411`) for the dark immersive hero, Pale Ceramic (`#F8FAF9`, `#FFFFFF`) for high-contrast reading sections (>7:1 WCAG AAA), with battery emerald (`#14D97D`), mint (`#3CF2C4`), and cobalt (`#2E8FE0`) accents.
- **Hero Artwork:** Layered isometric battery cells (graphite anode, ceramic separator, cathode foils, current collector tabs, and diagonal light beam) integrated with the live BPN Dashboard snapshot.
- **Background Animation:** Lightweight SVG circuit trace energy pulses on a calm 10s cycle, with `IntersectionObserver` pause and reduced motion support.
- **Typography:** Barlow Semi Condensed 600 for headings; Inter 400–600 for body copy; IBM Plex Mono for technical telemetry.
- **Content Fidelity:** 100% exact text, wording, punctuation, routes, and anchor destinations preserved across all 11 pages.

## Running Locally

To preview the redesigned website locally:

```bash
# Serve the redesign folder directly
npx serve battery-passport-redesign
# or using Python
python -m http.server 3000 --directory battery-passport-redesign
```

Then open `http://localhost:3000` in your browser.
