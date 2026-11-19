# JLM JAM 2026

Bilingual registration landing page for MakeGamesJLM's Hanukkah Game Jam. The default page is Hebrew. The English page is at `en/`.

## Edit and preview

- Update the Hebrew and English copy in `content.json`.
- Update the signup URL in `build.py` if the registration form changes.
- Run `python3 build.py` to regenerate both HTML pages.
- Run `python3 -m http.server 8000 --directory docs` to preview the site.

The game-device illustrations, title lettering, icons, and Jerusalem skyline came from the event's original graphics layers.

## Hosting

GitHub Pages can publish directly from the `main` branch and the `/docs` folder. Commit the regenerated pages along with changes to their source. The public Pages URL is the destination to use for the Cloudflare redirect.
