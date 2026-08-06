---
name: tweedehands-belgie
description: Zoekt en vergelijkt tweedehands aanbiedingen op Belgische platforms (2dehands.be, 2ememain.be, Vinted.be). Sterke filter op particuliere verkopers, prijsfilters, stealth bij blocked, scam-waarschuwingen. Trigger bij tweedehands, 2dehands, vinted, koopjes België.
---

# Tweedehands België Zoeker

**Version:** 2.3 (improved + saved 2026-08-06)

## Overview

Verbeterde en gesynergiseerde skill. Primair browser_tab voor exacte links en foto’s, automatische stealth, harde particuliere filter, altijd scam-warning.

## Instructies

1. Identificeer product, budget (min/max), regio/postcode, staat, ophalen/verzenden.

2. Platform keuze
   - Algemeen → 2dehands.be + 2ememain.be
   - Mode → Vinted.be
   - Lokaal groot → Facebook Marketplace + 2dehands

3. URL: https://www.2dehands.be/q/{query}/ of Vinted catalog.

4. Fetch
   - Primair browser_tab (waitTime 3-5, screenshot, jsCode voor links + foto’s)
   - Scroll en extract exacte https://www.2dehands.be/v/... links
   - Bij blocked → humanization-stealth-browsing
   - Filter hard: particulier vs pro/refurbished

5. Presentatie
   - Top particuliere eerst
   - Volledige links + foto-info
   - Prijsrange
   - Verplichte scam-warning: betaal nooit buiten platform

6. Log voor verdere verbetering

## Scripts
scripts/build_search_url.py

## Referenties
references/platforms.md
references/browser_tab_tips.md
