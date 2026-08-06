---
name: tweedehands-belgie
description: Zoekt en vergelijkt tweedehands aanbiedingen op Belgische platforms (2dehands.be, 2ememain.be, Vinted.be). Sterke filter op particuliere verkopers, prijsfilters, stealth bij blocked, scam-waarschuwingen. Trigger bij tweedehands, 2dehands, vinted, koopjes België.
---

# Tweedehands België Zoeker

**Version:** 1.8 (saved 2026-08-06)

## Overview

Geharde skill voor Belgische tweedehands. Prioriteit particuliere verkopers, parallel fetch, prijsstats, stealth fallback, scam-guardrails, en altijd links + foto's waar mogelijk.

## Instructies

1. Identificeer product, budget, regio, staat, ophalen/verzenden.

2. Platform keuze
   - Algemeen → 2dehands.be + 2ememain.be
   - Mode → Vinted.be
   - Lokaal groot → Facebook Marketplace + 2dehands

3. URL bouw
   - 2dehands: https://www.2dehands.be/q/{query}/
   - Vinted: https://www.vinted.be/catalog?search_text={query}

4. Fetch
   - browse_page of browser_tab voor exacte links en foto's
   - Filter pro / refurbished
   - Blocked → humanization-stealth-browsing

5. Presentatie
   - Altijd directe links
   - Foto-beschrijving of screenshot indien mogelijk
   - Prijsrange
   - Scam warning: betaal nooit buiten platform

6. Extra
   - Lokale query versterken
   - Kringwinkel / GIFT groepen

## Scripts
scripts/build_search_url.py

## Referenties
references/platforms.md
