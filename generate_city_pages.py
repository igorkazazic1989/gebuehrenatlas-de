# -*- coding: utf-8 -*-
"""
GebührenAtlas – Generator für die Stadt-Dimension (Stadt x Projekttyp).

WICHTIGER HINWEIS ZUR SEO-STRATEGIE:
Diese Seiten sind bewusst SCHLANK gehalten und verzichten auf erfundene
lokale Gebühren, weil solche Zahlen ohne echte Quelle (Gebührenordnung
der jeweiligen Kommune) Falschinformation wären. Jede Seite enthält
nur: (1) die bereits verifizierten Bundesland-Regeln, (2) einen Verweis
auf die zuständige Behörde ohne erfundene Kontaktdaten, (3) einen Link
zurück zur ausführlichen Projekttyp-Seite.

Das bedeutet: viele dieser Seiten werden sich inhaltlich stark ähneln
(nur der Bundesland-Absatz und der Stadtname ändern sich). Das ist ein
reales Risiko für Google als "Near-Duplicate-/Doorway-Content" und kann
dem ganzen Projekt schaden statt zu helfen, wenn es in dieser Form ohne
weitere Anreicherung live geht. Vor der Veröffentlichung in großer Zahl
sollten pro Stadt mindestens 1-2 wirklich einzigartige Fakten ergänzt
werden (z. B. echte Gebührenordnung der Kommune, lokale Bearbeitungs-
zeiten, Besonderheiten aus dem Bebauungsplan).

Verwendung:
    python3 generate_city_pages.py
"""

import os

OUTDIR = "pages"

CITY_META = {
    "muenchen":    ("München", "Bayern", "Lokalbaukommission München"),
    "berlin":      ("Berlin", "Berlin", "Bau- und Wohnungsaufsicht Berlin"),
    "koeln":       ("Köln", "Nordrhein-Westfalen", "Bauaufsichtsamt Köln"),
    "duesseldorf": ("Düsseldorf", "Nordrhein-Westfalen", "Bauaufsichtsamt Düsseldorf"),
    "nuernberg":   ("Nürnberg", "Bayern", "Bauordnungsbehörde Nürnberg"),
    "essen":       ("Essen", "Nordrhein-Westfalen", "Bauordnungsamt Essen"),
}

# Nur Projekttypen, für die ein klarer, verifizierter Bundeslandwert vorliegt.
# state_rule ist bewusst kurz gehalten und identisch mit den Werten aus
# generate_pages.py (Single Source of Truth wäre in einer echten Codebase
# ein gemeinsames Datenmodul statt Duplikation - hier vereinfacht).
PROJECT_TYPES = {
    "garage": dict(
        label="Garage",
        parent_slug="garage-baugenehmigung-groesse",
        parent_title="Garage genehmigungsfrei: Größe, Grenzbebauung & Kosten",
        state_rule={
            "Bayern": "In Bayern sind Garagen bis 50 m² Grundfläche und 3 m mittlerer Wandhöhe genehmigungsfrei.",
            "Berlin": "In Berlin gilt für Garagen im Regelfall eine Grenze von rund 30 m² – lassen Sie den Einzelfall vom Bauamt bestätigen.",
            "Nordrhein-Westfalen": "In NRW sind Garagen bis 30 m² Grundfläche und 3 m Wandhöhe genehmigungsfrei (§ 62 BauO NRW).",
        },
    ),
    "pool": dict(
        label="Pool",
        parent_slug="pool-baugenehmigung-ab-wann",
        parent_title="Pool Baugenehmigung: Ab wann ist ein Schwimmbecken genehmigungspflichtig?",
        state_rule={
            "Bayern": "In Bayern sind Pools bis 50 m³ im Außenbereich bzw. bis 100 m³ im Innenbereich genehmigungsfrei.",
            "Berlin": "In Berlin sind Schwimmbecken bis 100 m³ genehmigungsfrei.",
            "Nordrhein-Westfalen": "In NRW sind Schwimmbecken bis 100 m³ genehmigungsfrei (§ 62 BauO NRW), außer im Außenbereich.",
        },
    ),
    "terrasse": dict(
        label="Terrassenüberdachung",
        parent_slug="terrasse-baugenehmigung-groesse",
        parent_title="Terrassenüberdachung Baugenehmigung: Größe & Tiefe je Bundesland",
        state_rule={
            "Bayern": "In Bayern sind Terrassenüberdachungen bis 30 m² und 3 m Tiefe genehmigungsfrei.",
            "Berlin": "In Berlin sind Terrassenüberdachungen bis 30 m² und 3 m Tiefe genehmigungsfrei.",
            "Nordrhein-Westfalen": "In NRW sind Terrassenüberdachungen bis 30 m² und bis zu 4,5 m Tiefe genehmigungsfrei.",
        },
    ),
    "carport": dict(
        label="Carport",
        parent_slug="carport-baugenehmigung-nrw-bayern",
        parent_title="Carport Baugenehmigung: Größe, Kosten & Regeln",
        state_rule={
            "Bayern": "In Bayern sind Carports bis 50 m² Grundfläche genehmigungsfrei (Art. 57 Abs. 1 Nr. 1b BayBO).",
            "Berlin": "In Berlin sind Carports bis 30 m² Grundfläche und 3 m Wandhöhe genehmigungsfrei (§ 61 BauOBln).",
            "Nordrhein-Westfalen": "In NRW sind Carports bis 30 m² Grundfläche und 3 m Wandhöhe genehmigungsfrei (§ 62 BauO NRW).",
        },
    ),
    "gartenhaus": dict(
        label="Gartenhaus",
        parent_slug="gartenhaus-genehmigungsfrei-modelle",
        parent_title="Gartenhaus genehmigungsfrei: Diese Modelle & Größen sind erlaubt",
        state_rule={
            "Bayern": "In Bayern sind Gartenhäuser bis 75 m³ Brutto-Rauminhalt genehmigungsfrei (Art. 57 BayBO).",
            "Berlin": "In Berlin gilt bundesweit meist die 10-m³-Faustregel für Gartenhäuser – im Zweifel beim Bauamt nachfragen.",
            "Nordrhein-Westfalen": "In NRW wird häufig eine Grenze von bis zu 75 m³ genannt, kommunale Satzungen können jedoch abweichen (z. B. teils nur 30 m³).",
        },
    ),
}

CITY_TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{project_label} Baugenehmigung {city}: Regeln & zuständiges Amt (2026)</title>
<meta name="description" content="{project_label} in {city} genehmigungsfrei bauen? Die {bundesland}-Regeln im Überblick, plus zuständige Behörde vor Ort.">
<link rel="canonical" href="https://gebuehrenatlas.de/{city_slug}/baugenehmigung-{project_slug}.html">
<style>
  :root{{--blue:#0b4f8a;--blue-dark:#083a66;--bg:#f7f9fb;--border:#e2e8ef;--text:#1f2933;--muted:#5b6670;--accent:#e8f1fa;}}
  *{{box-sizing:border-box;}}
  body{{font-family:"Segoe UI",Arial,sans-serif;margin:0;color:var(--text);background:#fff;line-height:1.55;}}
  header{{background:var(--blue-dark);padding:14px 24px;}}
  header a{{color:#fff;text-decoration:none;font-weight:700;font-size:1.1rem;}}
  .breadcrumb{{font-size:.85rem;color:var(--muted);margin:16px 24px 0;}}
  .breadcrumb a{{color:var(--blue);text-decoration:none;}}
  main{{max-width:820px;margin:0 auto;padding:0 24px 60px;}}
  h1{{font-size:1.5rem;color:var(--blue-dark);margin-top:18px;}}
  h2{{font-size:1.15rem;color:var(--blue-dark);border-bottom:2px solid var(--accent);padding-bottom:6px;margin-top:34px;}}
  .facts-box{{background:var(--accent);border:1px solid var(--border);border-radius:8px;padding:16px 20px;margin:20px 0;}}
  .cta-box{{background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:18px 20px;margin:24px 0;font-size:.95rem;}}
  .cta-box a.btn{{display:inline-block;background:var(--blue);color:#fff;text-decoration:none;padding:10px 18px;border-radius:6px;font-weight:600;margin-top:8px;font-size:.9rem;}}
  .disclaimer{{font-size:.8rem;color:var(--muted);margin-top:8px;}}
  footer{{border-top:1px solid var(--border);margin-top:44px;padding:22px;text-align:center;font-size:.8rem;color:var(--muted);}}
  footer a{{color:var(--muted);}}
</style>
</head>
<body>

<header><a href="../index.html">GebührenAtlas</a></header>
<p class="breadcrumb"><a href="../index.html">GebührenAtlas</a> &gt; <a href="../{parent_slug}.html">{project_label}</a> &gt; {city}</p>

<main>
  <h1>{project_label} Baugenehmigung in {city}: Was gilt in {bundesland}?</h1>
  <p>{intro}</p>

  <div class="facts-box">
    <p>{state_rule}</p>
    <p class="disclaimer">Dies ist die allgemeine {bundesland}-Regel. Der Bebauungsplan von {city} oder eine kommunale Satzung können abweichende, strengere Vorgaben enthalten.</p>
  </div>

  <h2>Zuständige Behörde in {city}</h2>
  <p>Zuständig für Baugenehmigungen und Bauvoranfragen in {city} ist die <strong>{amt}</strong>. Die genauen Kontaktdaten, Formulare und Online-Antragswege finden Sie auf der offiziellen Website der Stadtverwaltung {city}.</p>

  <div class="cta-box">
    <strong>Ausführliche Informationen zu {project_label}</strong>
    <p>Alle Bundesländer im Vergleich, Checkliste und kostenloser Vermittlungsservice für Fachbetriebe:</p>
    <a class="btn" href="../{parent_slug}.html">Zur vollständigen {project_label}-Übersicht →</a>
  </div>

  <p class="disclaimer">Zuletzt geprüft: September 2026 von Igor Kazazic, keine Rechtsberatung. Bei Unsicherheit empfiehlt sich eine Bauvoranfrage bei der {amt}.</p>
</main>

<footer>
  © 2026 GebührenAtlas.de – Ihr unabhängiges Bau- und Genehmigungsportal.<br>
  <a href="../impressum.html">Impressum</a> | <a href="../datenschutz.html">Datenschutz</a> | <a href="../agb.html">AGB</a>
</footer>

</body>
</html>
"""


def main():
    count = 0
    for city_slug, (city, bundesland, amt) in CITY_META.items():
        city_dir = os.path.join(OUTDIR, city_slug)
        os.makedirs(city_dir, exist_ok=True)
        for proj_slug, proj in PROJECT_TYPES.items():
            rule = proj["state_rule"].get(bundesland)
            if not rule:
                continue  # nur Städte mit verifizierter Bundeslandregel erzeugen
            html = CITY_TEMPLATE.format(
                project_label=proj["label"],
                project_slug=proj_slug,
                parent_slug=proj["parent_slug"],
                city=city,
                city_slug=city_slug,
                bundesland=bundesland,
                amt=amt,
                state_rule=rule,
                intro=f"Wer in {city} ein Vorhaben der Kategorie \"{proj['label']}\" plant, muss zunächst prüfen, ob es nach den Regeln von {bundesland} genehmigungsfrei ist.",
            )
            path = os.path.join(city_dir, f"baugenehmigung-{proj_slug}.html")
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            count += 1
    print(f"{count} Stadt-Seiten geschrieben in {OUTDIR}/<stadt>/")


if __name__ == "__main__":
    main()
