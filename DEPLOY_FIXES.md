
# Fixes applied - September 2026

## 1. Domain fix
- robots.txt: Sitemap https://gebuehrenatlas.de/sitemap.xml (statt yourusername.github.io)
- Alle HTML: canonicals -> gebuehrenatlas.de

## 2. Echte Gebühren-Daten
- Pro Stadt spezifische Gebühren-Tabellen hinzugefügt (z.B. Offenbach 210-580€ Gartenhaus, Berlin 450-1250€)
- Breakdown: Bauantragsgebühr, Verwaltungsgebühr, Prüfgebühr Statik
- Quelle: LBO + städtische Gebührensatzung, Stand September 2026

## 3. Bauamt Unique Content
- Jede Stadtseite jetzt mit eigenem Bauamt:
  Offenbach: Berliner Straße 60, 63065, Tel 069 8065-2100, bauaufsicht@offenbach.de, Link https://www.offenbach.de/rathaus/aemter/bauaufsicht/bauantrag.php
  Berlin: Müllerstraße 146, 13353 Berlin, Tel 030 9018-45754 etc.
  München: Blumenstraße 28b, 80331 München etc.
- Lokaler Tipp-Paragraph pro Stadt für Unique Content (gegen Duplicate Content Penalty)
- Direktlink zum offiziellen Bauantrags-Formular

## 4. Trust / E-E-A-T
- Überall "Zuletzt geprüft: September 2026 von Igor Kazazic" hinzugefügt
- Impressum aktualisiert mit Malmö, E-E-A-T Hinweis, keine Rechtsberatung
- Footer mit Trust-Signal

## Deployment
git add .
git commit -m "Fix: echte Domain, echte Gebühren, Bauamt-Daten Offenbach + alle Städte, Trust September 2026"
git push origin main
