# ArtefyCraft mājaslapa: kā labot

Dzīvā lapa: https://artefycraft.com (GitHub Pages no šī repo `master`/`main` zara).

## Failu izkārtojums

| Fails | Kas tas ir |
|---|---|
| `index.html` | GATAVAIS fails, ko rāda pārlūks. **Nelabot ar roku**: to ģenerē `build.py`. |
| `src/site_core.html` | ĪSTAIS pirmkods: viss HTML, CSS un JS. Šeit veic izmaiņas. |
| `src/fonts_embed.css` | Fontu @font-face noteikumi; paši fonti ir mapē `fonti/` (licence `fonti/OFL.txt`). Parasti nav jāaiztiek. |
| `src/logo_mark.svg` | Logo zīme (pilšu "A"). |
| `src/page_wrapper.html` | Lapas galvenes apvalks (meta, favicon). Figūriekavas tajā ir dubultotas ({{ }}), tā jāpaliek. |
| `build.py` | Saliek `src/` failus vienā `index.html` (galvene, meta, favicon). |
| `CNAME` | Domēna piesaiste `artefycraft.com`. **Nekad nedzēst un nemainīt.** |

## Darba gaita

1. Labo `src/site_core.html`.
2. Uzbūvē gatavo failu: `python build.py` (vajadzīgs Python 3, nekādas bibliotēkas nav jāinstalē).
3. Pārbaudi lokāli caur serveri: `python -m http.server`, tad http://localhost:8000 (no file:// pārlūks fontus bloķē).
4. Publicē: `git add -A && git commit -m "apraksts" && git push`.
5. GitHub Pages automātiski izliek jauno versiju 1 līdz 2 minūtēs (pārlūkā Ctrl+F5, ja rāda veco).

## Piezīmes

- Lapa neielādē neko no citiem domēniem: fonti ir mapē `fonti/`, logo ir iegults.
- Pieteikuma forma sūta pieteikumu uz https://zcbwdbcfalwhapwgzswj.supabase.co/functions/v1/site-lead?forceFunctionRegion=eu-central-1 (mūsu platforma), kur tas tiek saglabāts; īpašnieks saņem paziņojumu bez personas datiem. Kļūdas gadījumā lapa piedāvā e-pastu un WhatsApp ar aizpildītu tekstu.
- Fontu licences aprakstītas `README.md`.
