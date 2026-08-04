# ArtefyCraft mājaslapa — kā labot

Dzīvā lapa: https://artefycraft.com (GitHub Pages no šī repo `master`/`main` zara).

## Failu izkārtojums

| Fails | Kas tas ir |
|---|---|
| `index.html` | GATAVAIS fails, ko rāda pārlūks. **Nelabot ar roku** — to ģenerē `build.py`. |
| `src/site_core.html` | ĪSTAIS pirmkods: viss HTML, CSS un JS. Šeit veic izmaiņas. |
| `src/fonts_embed.css` | Iegultie fonti (base64). Parasti nav jāaiztiek. |
| `src/logo_mark.svg` | Logo zīme (pilšu "A"). |
| `src/page_wrapper.html` | Lapas galvenes apvalks (meta, favicon). Figūriekavas tajā ir dubultotas ({{ }}) — tā jāpaliek. |
| `build.py` | Saliek `src/` failus vienā `index.html` (galvene, meta, favicon). |
| `CNAME` | Domēna piesaiste `artefycraft.com`. **Nekad nedzēst un nemainīt.** |

## Darba gaita

1. Labo `src/site_core.html`.
2. Uzbūvē gatavo failu: `python build.py` (vajadzīgs Python 3, nekādas bibliotēkas nav jāinstalē).
3. Pārbaudi lokāli: atver `index.html` pārlūkā.
4. Publicē: `git add -A && git commit -m "apraksts" && git push`.
5. GitHub Pages automātiski izliek jauno versiju ~1–2 minūtēs (pārlūkā Ctrl+F5, ja rāda veco).

## Piezīmes

- Lapa ir viens pašpietiekams fails: fonti, attēli un logo ir iegulti, ārējo pieprasījumu nav.
- Pieteikuma forma sūta e-pastu caur FormSubmit uz arturs@artefycraft.com.
- Fontu licences un attēlu avoti aprakstīti `README.md`.
