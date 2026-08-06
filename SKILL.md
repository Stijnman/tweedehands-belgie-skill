---
name: tweedehands-belgie
description: Zoekt en vergelijkt tweedehands aanbiedingen op Belgische platforms (2dehands.be, 2ememain.be, Vinted.be). Sterke filter op particuliere verkopers, prijsfilters, stealth bij blocked, scam-waarschuwingen. Trigger bij tweedehands, 2dehands, vinted, koopjes België.
---

# Tweedehands België Zoeker

**Version:** 1.6 (final after loops + review 2026-08-06)

## Overview

Geharde, production-ready skill voor Belgische tweedehands. Na meerdere test/improve loops: prioriteit particuliere verkopers, betere extractie, prijsstats, Vinted voor mode, humanization-stealth fallback, duidelijke scam-guardrails.

## Instructies

1. Identificeer product, budget (min/max), regio/postcode, staat, ophalen/verzenden, sort voorkeur.

2. Platform keuze
   - Algemeen / electronica / meubels → 2dehands.be + 2ememain.be
   - Mode, schoenen, accessoires → Vinted.be eerst
   - Lokaal groot → Facebook Marketplace + 2dehands
   - Auto → 2dehands + AutoScout24

3. URL bouw
   - 2dehands: https://www.2dehands.be/q/{query}/
   - Vinted: https://www.vinted.be/catalog?search_text={query}&order=price_low_to_high of newest_first
   - Voeg price_from / price_to toe als budget gegeven

4. Fetch
   - browse_page met strakke extract: titel, prijs, locatie, staat, verkoper-type (particulier vs pro), link
   - Filter actief: markeer of skip professioneel / refurbished / shop listings
   - Bij blocked of leeg → humanization-stealth-browsing
   - Backup: web_search site:2dehands.be of site:vinted.be

5. Presentatie
   - Top 5-8 particuliere listings eerst
   - Prijsrange + mediaan
   - Directe links
   - Altijd: "Betaal nooit buiten het platform. Check verkopersprofiel. Meet af bij ophalen."

6. Extra
   - Lokale query met stad versterken
   - Kringwinkel / GIFT groepen voor ultra-goedkoop
   - Log patterns

## Scripts
scripts/build_search_url.py

## Referenties
references/platforms.md
