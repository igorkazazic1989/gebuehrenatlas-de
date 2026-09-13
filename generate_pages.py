# -*- coding: utf-8 -*-
"""
GebührenAtlas – Seitengenerator für projekttyp-basierte Long-Tail-Seiten.

Verwendung:
    python3 generate_pages.py

Jede Seite wird aus PAGE_TEMPLATE + den Daten in PAGES[...] gebaut.
Neue Projekttypen hinzufügen = neuen Eintrag in PAGES ergänzen, Skript
erneut laufen lassen. Für die Stadt-Dimension siehe generate_city_pages.py.

WICHTIG: Alle Zahlenwerte in PAGES stammen aus recherchierten Quellen
(Landesbauordnungen bzw. seriöse Fachportale, Stand September 2026) und
sind als Richtwerte gekennzeichnet – keine erfundenen Werte. Bei neuen
Projekttypen: erst recherchieren, dann eintragen.
"""

import os

OUTDIR = "pages"
os.makedirs(OUTDIR, exist_ok=True)

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta_description}">
<link rel="canonical" href="https://gebuehrenatlas.de/{slug}.html">
<style>
  :root{{
    --blue:#0b4f8a; --blue-dark:#083a66; --bg:#f7f9fb; --border:#e2e8ef;
    --text:#1f2933; --muted:#5b6670; --accent:#e8f1fa;
  }}
  *{{box-sizing:border-box;}}
  body{{font-family:"Segoe UI",Arial,sans-serif;margin:0;color:var(--text);background:#fff;line-height:1.55;}}
  header{{background:var(--blue-dark);padding:14px 24px;}}
  header a{{color:#fff;text-decoration:none;font-weight:700;font-size:1.1rem;}}
  .breadcrumb{{font-size:.85rem;color:var(--muted);margin:16px 24px 0;}}
  .breadcrumb a{{color:var(--blue);text-decoration:none;}}
  main{{max-width:880px;margin:0 auto;padding:0 24px 60px;}}
  h1{{font-size:1.7rem;color:var(--blue-dark);margin-top:18px;}}
  h2{{font-size:1.25rem;color:var(--blue-dark);border-bottom:2px solid var(--accent);padding-bottom:6px;margin-top:38px;}}
  .lead{{font-size:1.05rem;color:var(--muted);}}
  .facts-box{{background:var(--accent);border:1px solid var(--border);border-radius:8px;padding:18px 22px;margin:22px 0;}}
  .facts-box h3{{margin-top:0;color:var(--blue-dark);font-size:1.05rem;}}
  .facts-box ul{{margin:8px 0 0;padding-left:20px;}}
  .form-box{{background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:22px;margin:30px 0;}}
  .form-box .tag{{display:inline-block;background:var(--blue);color:#fff;font-size:.75rem;padding:3px 10px;border-radius:20px;margin-bottom:10px;}}
  .form-box h3{{margin:4px 0 4px;color:var(--blue-dark);}}
  .form-box p{{margin-top:0;color:var(--muted);font-size:.95rem;}}
  form label{{display:block;font-size:.85rem;font-weight:600;margin:12px 0 4px;}}
  form select, form input{{width:100%;padding:9px 10px;border:1px solid var(--border);border-radius:6px;font-size:.95rem;}}
  .consent{{font-size:.75rem;color:var(--muted);margin-top:14px;}}
  .consent a{{color:var(--blue);}}
  .cta{{display:inline-block;background:var(--blue);color:#fff;border:none;padding:12px 22px;border-radius:6px;font-weight:600;margin-top:16px;cursor:pointer;font-size:.95rem;}}
  .cta-note{{font-size:.75rem;color:var(--muted);margin-top:8px;}}
  table{{width:100%;border-collapse:collapse;margin-top:14px;font-size:.9rem;}}
  th, td{{border:1px solid var(--border);padding:10px 12px;text-align:left;vertical-align:top;}}
  th{{background:var(--accent);color:var(--blue-dark);}}
  .disclaimer{{font-size:.8rem;color:var(--muted);margin-top:8px;}}
  ol, ul.checklist{{padding-left:22px;}}
  .city-links{{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px;}}
  .city-links a{{background:var(--accent);color:var(--blue-dark);text-decoration:none;font-size:.85rem;padding:8px 14px;border-radius:6px;border:1px solid var(--border);}}
  footer{{border-top:1px solid var(--border);margin-top:50px;padding:24px;text-align:center;font-size:.8rem;color:var(--muted);}}
  footer a{{color:var(--muted);}}
</style>
</head>
<body>

<header><a href="index.html">GebührenAtlas</a></header>
<p class="breadcrumb"><a href="index.html">GebührenAtlas</a> &gt; <a href="index.html#baugenehmigungen">Baugenehmigungen</a> &gt; {breadcrumb}</p>

<main>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>

  <div class="facts-box">
    <h3>⚡ Die wichtigsten Vorgaben auf einen Blick (2026)</h3>
    <ul>
      {facts}
    </ul>
  </div>

  <div class="form-box">
    <span class="tag">Kostenloser Vermittlungsservice</span>
    <h3>Angebote regionaler Fachbetriebe & Architekten anfragen</h3>
    <p>Unsicher, ob Ihr Vorhaben genehmigungsfrei ist? Lassen Sie es von geprüften Partnern in Ihrer Region kostenlos prüfen und vergleichen Sie bis zu 3 unverbindliche Angebote.</p>
    <form onsubmit="return false;">
      <label>Ihr Bauvorhaben *</label>
      <select>
        <option>Bitte wählen...</option>
        <option selected>{project_option}</option>
        <option>Wohnraumanbau / Gebäudeerweiterung</option>
        <option>Bauantrag / Architektenleistung (§ Bauvorlageberechtigung)</option>
      </select>
      <label>Postleitzahl & Ort *</label>
      <input type="text" placeholder="z. B. 50667 Köln">
      <label>Telefonnummer (für Rückfragen) *</label>
      <input type="tel">
      <label>Vor- und Nachname *</label>
      <input type="text">
      <label>E-Mail-Adresse *</label>
      <input type="email">
      <label>Kurze Projektbeschreibung (optional)</label>
      <input type="text" placeholder="{project_placeholder}">
      <p class="consent"><strong>Datenschutz-Einwilligung:</strong> Ich willige ein, dass GebührenAtlas meine angegebenen Daten zur Erstellung passender Angebote an bis zu 3 verifizierte regionale Partnerbetriebe und Fachplaner übermittelt. Diese Einwilligung kann ich jederzeit mit Wirkung für die Zukunft per E-Mail widerrufen. Es gelten die Hinweise der <a href="datenschutz.html">Datenschutzerklärung</a>.</p>
      <button class="cta" type="submit">Kostenlose Fachangebote anfordern →</button>
      <p class="cta-note">100% kostenlos & unverbindlich. Ihre Daten werden vertraulich behandelt.</p>
    </form>
  </div>

  <h2>{table_heading}</h2>
  <p>{table_intro}</p>
  <table>
    <tr><th>Bundesland</th><th>Rechtsgrundlage</th><th>Genehmigungsfrei / Regelung</th></tr>
    {table_rows}
  </table>
  <p class="disclaimer">{table_disclaimer}</p>

  {extra_section}

  <h2>{checklist_heading}</h2>
  <ul class="checklist">
    {checklist_items}
  </ul>

  <h2>Lokale Vorschriften in den Großstädten prüfen</h2>
  <p>Wählen Sie Ihre Stadt für detaillierte Vorgaben des örtlichen Bauamts:</p>
  <div class="city-links">
    {city_links}
  </div>
  <p class="disclaimer">Letzte Prüfung: 13.09.2026 von Igor Kazazic, keine Rechtsberatung.</p>
</main>

<footer>
  © 2026 GebührenAtlas.de – Ihr unabhängiges Bau- und Genehmigungsportal.<br>
  <a href="impressum.html">Impressum</a> | <a href="datenschutz.html">Datenschutz</a> | <a href="agb.html">AGB</a>
</footer>

</body>
</html>
"""

CITIES = ["muenchen", "berlin", "koeln", "duesseldorf", "nuernberg", "essen"]
CITY_LABELS = {
    "muenchen": "München Lokalbaukommission",
    "berlin": "Berlin Bau- und Wohnungsaufsicht",
    "koeln": "Köln Bauaufsichtsamt",
    "duesseldorf": "Düsseldorf Bauaufsichtsamt",
    "nuernberg": "Nürnberg Bauordnungsbehörde",
    "essen": "Essen Bauordnungsamt",
}


def render_city_links(slug_suffix):
    links = []
    for c in CITIES:
        links.append(f'<a href="{c}/baugenehmigung-{slug_suffix}.html">{CITY_LABELS[c]}</a>')
    return "\n    ".join(links)


def render_list(items):
    return "\n      ".join(f"<li>{i}</li>" for i in items)


def render_rows(rows):
    out = []
    for land, grundlage, regel in rows:
        out.append(f"<tr><td>{land}</td><td>{grundlage}</td><td>{regel}</td></tr>")
    return "\n    ".join(out)


PAGES = {

    "garage-baugenehmigung-groesse": dict(
        title="Garage genehmigungsfrei: Größe, Grenzbebauung & Kosten (2026)",
        meta_description="Bis zu welcher Größe ist eine Garage ohne Baugenehmigung erlaubt? Regeln zu Grenzbebauung, Wandhöhe und Bundesländer-Unterschieden.",
        breadcrumb="Garage",
        h1="Garage genehmigungsfrei: Größe, Grenzbebauung & Kosten (2026)",
        lead="In den meisten Bundesländern sind Garagen bis zu einer bestimmten Grundfläche verfahrensfrei. Entscheidend sind Fläche, Wandhöhe und die Länge an der Grundstücksgrenze.",
        facts=render_list([
            "Bundesweite Faustregel: Garagen bis <strong>50 m² Grundfläche</strong> und <strong>3 m mittlere Wandhöhe</strong> sind in den meisten Bundesländern genehmigungsfrei.",
            "<strong>Grenzbebauung</strong> ist ohne Zustimmung des Nachbarn oft möglich, wenn die Wandlänge an einer Grenze 9 m nicht überschreitet und insgesamt max. 15 m der Grundstücksgrenze bebaut werden.",
            "In <strong>Nordrhein-Westfalen</strong> gilt für Garagen die gleiche 30-m²-Grenze wie für Carports (§ 62 BauO NRW) – abweichend von der bundesweiten 50-m²-Faustregel.",
            "Ein Mindestabstand von ca. 3 m zur Grundstücksgrenze ist Standard, sofern keine Grenzbebauung vorliegt.",
        ]),
        project_option="Garage / Nebengebäude",
        project_placeholder="z. B. Garage für 1 Fahrzeug, ca. 24 m²",
        table_heading="Genehmigungsfreie Garagengrößen im Bundesländer-Vergleich",
        table_intro="Datenbank 2026 – Richtwerte auf Basis der jeweiligen Landesbauordnung (LBO).",
        table_rows=render_rows([
            ("Bayern, Hessen, Sachsen, Thüringen u.a.", "jeweilige LBO", "bis 50 m², Wandhöhe bis 3 m"),
            ("Nordrhein-Westfalen", "§ 62 BauO NRW", "bis 30 m², Wandhöhe bis 3 m"),
            ("Mecklenburg-Vorpommern", "LBauO M-V", "bis 30 m²"),
            ("Grenzbebauung (bundesweit üblich)", "jeweilige LBO", "bis 9 m Länge je Grenze, insgesamt max. 15 m"),
        ]),
        table_disclaimer="Zuletzt geprüft: September 2026 von Igor Kazazic, geprüft nach den Landesbauordnungen, keine Rechtsberatung. Kommunale Satzungen und Bebauungspläne können abweichende Regeln vorsehen.",
        extra_section="",
        checklist_heading="Wann wird aus einer Garage ein genehmigungspflichtiges Vorhaben?",
        checklist_items=render_list([
            "Überschreitung der Flächen- oder Höhengrenze des jeweiligen Bundeslandes",
            "Nutzung als Aufenthaltsraum, Werkstatt oder Lagerraum statt reiner Fahrzeugunterstellung",
            "Überschreitung der zulässigen Grenzbebauungslänge",
            "Errichtung im planungsrechtlichen Außenbereich",
            "Widerspruch zu den Festsetzungen des örtlichen Bebauungsplans",
        ]),
        city_links=render_city_links("garage"),
    ),

    "pool-baugenehmigung-ab-wann": dict(
        title="Pool Baugenehmigung: Ab wann ist ein Schwimmbecken genehmigungspflichtig? (2026)",
        meta_description="Ab welchem Volumen braucht ein Pool im Garten eine Baugenehmigung? Übersicht der Grenzwerte nach Bundesland, Tiefe und Überdachung.",
        breadcrumb="Pool",
        h1="Pool Baugenehmigung: Ab wann ist ein Schwimmbecken genehmigungspflichtig? (2026)",
        lead="Nach der Musterbauordnung (MBO) sind private Schwimmbecken bis 100 m³ meist verfahrensfrei – einige Bundesländer setzen jedoch niedrigere Grenzen, besonders im Außenbereich.",
        facts=render_list([
            "Bundesweite Regel (§ 61 Nr. 10a MBO): Schwimmbecken bis <strong>100 m³ Beckeninhalt</strong> sind im Innenbereich meist genehmigungsfrei.",
            "<strong>Bayern:</strong> im Außenbereich nur bis 50 m³ genehmigungsfrei, im Innenbereich bis 100 m³.",
            "<strong>Baden-Württemberg:</strong> im Außenbereich bereits ab 10 m³ genehmigungspflichtig.",
            "<strong>Hessen:</strong> Grenze bezieht sich auf Grundfläche (bis 50 m²) und Tiefe (1,5–1,8 m), nicht auf Volumen.",
            "Eine <strong>feste Überdachung</strong> (Glas/Wände) macht den Pool baurechtlich zu einem Gebäude – dann gilt meist ein Mindestabstand von 3 m zur Grundstücksgrenze.",
        ]),
        project_option="Pool / Schwimmbecken",
        project_placeholder="z. B. Einbaupool 4x8m, ca. 48 m³",
        table_heading="Genehmigungsfreie Poolgrößen im Bundesländer-Vergleich",
        table_intro="Datenbank 2026 – Richtwerte auf Basis der jeweiligen Landesbauordnung (LBO).",
        table_rows=render_rows([
            ("Bayern", "Art. 57 BayBO", "bis 50 m³ (Außenbereich) / 100 m³ (Innenbereich)"),
            ("Baden-Württemberg", "LBO", "bis 10 m³ (Außenbereich) / 100 m³ (Innenbereich)"),
            ("Hessen", "HBO", "bis 50 m² Grundfläche, 1,5–1,8 m Tiefe"),
            ("Berlin, Brandenburg, NRW u. a.", "jeweilige LBO / MBO", "bis 100 m³ im Innenbereich"),
        ]),
        table_disclaimer="Zuletzt geprüft: September 2026 von Igor Kazazic, geprüft nach den Landesbauordnungen, keine Rechtsberatung. Wasserschutzgebiete und Bebauungspläne können zusätzliche Auflagen enthalten.",
        extra_section="""
  <h2>Wichtig unabhängig von der Genehmigungspflicht</h2>
  <p>Auch ein genehmigungsfreier Pool muss Abstandsflächen zur Grundstücksgrenze einhalten und braucht ab 1,20 m Wassertiefe eine bauordnungsrechtlich vorgeschriebene Absturzsicherung (z. B. Zaun oder Abdeckung). Bei Berührung des Grundwassers oder Einleitung von Wasser in den Boden kann zusätzlich eine wasserrechtliche Prüfung nötig sein.</p>
""",
        checklist_heading="Wann wird aus einem Pool ein genehmigungspflichtiges Vorhaben?",
        checklist_items=render_list([
            "Überschreitung des zulässigen Volumens bzw. der Grundfläche im jeweiligen Bundesland",
            "Feste Überdachung mit Wänden (baurechtlich ein Gebäude)",
            "Lage im planungsrechtlichen Außenbereich",
            "Anschluss an das Abwassernetz oder Grundwassereingriff ohne wasserrechtliche Prüfung",
            "Unterschreitung der vorgeschriebenen Abstandsfläche zum Nachbargrundstück",
        ]),
        city_links=render_city_links("pool"),
    ),

    "terrasse-baugenehmigung-groesse": dict(
        title="Terrassenüberdachung Baugenehmigung: Größe & Tiefe je Bundesland (2026)",
        meta_description="Wann ist eine Terrassenüberdachung genehmigungsfrei? Grenzwerte für Fläche und Tiefe im Bundesländer-Vergleich.",
        breadcrumb="Terrasse",
        h1="Terrassenüberdachung Baugenehmigung: Größe & Tiefe je Bundesland (2026)",
        lead="Terrassenüberdachungen sind in fast allen Bundesländern bis zu einer bestimmten Fläche und Tiefe verfahrensfrei – die genauen Grenzwerte unterscheiden sich aber deutlich.",
        facts=render_list([
            "Häufigste Regel: Überdachungen bis <strong>30 m² Fläche</strong> und <strong>3 m Tiefe</strong> sind genehmigungsfrei.",
            "<strong>Nordrhein-Westfalen:</strong> großzügigere Tiefe von bis zu 4,5 m erlaubt.",
            "<strong>Rheinland-Pfalz:</strong> Grenzwert bezieht sich auf einen Rauminhalt von max. 50 m³ statt auf die Fläche.",
            "<strong>Saarland:</strong> bis 36 m² genehmigungsfrei.",
            "<strong>Hessen:</strong> keine feste Größengrenze in der Landesbauordnung genannt – Einzelfallprüfung beim Bauamt empfohlen.",
        ]),
        project_option="Terrasse / Terrassenüberdachung",
        project_placeholder="z. B. Terrassenüberdachung 25 m², Tiefe 3,5 m",
        table_heading="Genehmigungsfreie Terrassenüberdachungen im Bundesländer-Vergleich",
        table_intro="Datenbank 2026 – Richtwerte auf Basis der jeweiligen Landesbauordnung (LBO).",
        table_rows=render_rows([
            ("Baden-Württemberg", "LBO", "bis 30 m²"),
            ("Bayern", "BayBO", "bis 30 m², Tiefe bis 3 m"),
            ("Berlin", "BauO Bln", "bis 30 m², Tiefe bis 3 m"),
            ("Brandenburg", "BbgBO", "bis 20 m², Tiefe bis 4 m"),
            ("Nordrhein-Westfalen", "BauO NRW", "bis 30 m², Tiefe bis 4,5 m"),
            ("Rheinland-Pfalz", "LBauO", "bis 50 m³ Rauminhalt"),
            ("Saarland", "LBO", "bis 36 m², Tiefe bis 3 m"),
            ("Sachsen", "SächsBO", "bis 50 m², Tiefe bis 3 m"),
            ("Hessen", "HBO", "keine feste Größengrenze genannt – Bauamt kontaktieren"),
        ]),
        table_disclaimer="Zuletzt geprüft: September 2026 von Igor Kazazic, geprüft nach den Landesbauordnungen, keine Rechtsberatung. Zusätzlich gilt meist ein Mindestabstand von 3 m zur Grundstücksgrenze.",
        extra_section="",
        checklist_heading="Wann wird aus einer Terrassenüberdachung ein genehmigungspflichtiges Vorhaben?",
        checklist_items=render_list([
            "Überschreitung der Flächen- oder Tiefengrenze des jeweiligen Bundeslandes",
            "Geschlossene Seitenwände, die einen Wintergarten oder Aufenthaltsraum entstehen lassen",
            "Unterschreitung des Grenzabstands (meist 3 m) ohne Zustimmung des Nachbarn",
            "Zusätzliche Einfriedungen (Zäune/Mauern) über 2 m Höhe",
            "Widerspruch zu Festsetzungen im Bebauungsplan",
        ]),
        city_links=render_city_links("terrasse"),
    ),

    "tiny-house-baugenehmigung": dict(
        title="Tiny House Baugenehmigung: Regeln für Dauerwohnen & Aufstellort (2026)",
        meta_description="Braucht ein Tiny House eine Baugenehmigung? Unterschiede zwischen mobilen und stationären Tiny Houses, Dauerwohnen und Campingplätzen.",
        breadcrumb="Tiny House",
        h1="Tiny House Baugenehmigung: Regeln für Dauerwohnen & Aufstellort (2026)",
        lead="Anders als bei Gartenhaus oder Carport gibt es für Tiny Houses keine pauschale Genehmigungsfreiheit – entscheidend sind Bauweise (mobil/stationär), Nutzungsdauer und der Bebauungsplan des Standorts.",
        facts=render_list([
            "Ein <strong>stationäres Tiny House</strong> auf festem Fundament unterliegt denselben Regeln wie ein normales Wohngebäude – Bauantrag, Statik, Brandschutz und GEG-Anforderungen inklusive.",
            "Ein <strong>mobiles Tiny House auf Rädern</strong> gilt ähnlich wie ein Wohnwagen: für dauerhaftes Stehen auf einem Grundstück wird i. d. R. trotzdem eine Genehmigung benötigt.",
            "<strong>Dauerwohnen</strong> ist nur zulässig, wenn der Bebauungsplan der Gemeinde Wohnnutzung an diesem Standort vorsieht.",
            "Auf <strong>Campingplätzen</strong> gelten bis zu einer Standdauer von häufig 3 Monaten die Camping- und Wochenendplatzverordnungen statt des vollen Baurechts – darüber hinaus greift meist das reguläre Baurecht.",
            "Unter 50 m² Wohnfläche ist in der Regel kein Energieausweis erforderlich.",
        ]),
        project_option="Tiny House",
        project_placeholder="z. B. Tiny House 25 m², stationär, Dauerwohnen geplant",
        table_heading="Tiny House: Was gilt je nach Standort und Nutzung?",
        table_intro="Datenbank 2026 – allgemeine Einordnung nach Standortart. Die tatsächliche Zulässigkeit hängt immer vom konkreten Bebauungsplan ab.",
        table_rows=render_rows([
            ("Privates Baugrundstück, stationär", "jeweilige LBO", "Bauantrag erforderlich, volle bauordnungsrechtliche Anforderungen"),
            ("Privates Grundstück, mobil (Räder)", "jeweilige LBO / StVZO", "Genehmigung für dauerhaftes Aufstellen i. d. R. erforderlich"),
            ("Campingplatz, Kurzaufenthalt", "Camping-/Wochenendplatzverordnung", "Baurecht meist nicht anwendbar bis zur Höchstdauer"),
            ("Campingplatz, Dauerwohnen", "jeweilige LBO", "Baurecht greift, Bebauungsplan muss Wohnnutzung zulassen"),
        ]),
        table_disclaimer="Zuletzt geprüft: September 2026 von Igor Kazazic, keine Rechtsberatung. Empfehlung: vor dem Kauf eines Grundstücks oder Stellplatzes eine Bauvoranfrage beim zuständigen Bauamt stellen.",
        extra_section="",
        checklist_heading="Checkliste vor dem Tiny-House-Kauf",
        checklist_items=render_list([
            "Klären, ob der Bebauungsplan am geplanten Standort Wohnnutzung zulässt",
            "Prüfen, ob Anschluss an Straße, Strom, Wasser und Kanalisation möglich ist",
            "Bei Rädern: Straßenzulassung (max. 4 m Höhe, 2,55 m Breite, 3.500 kg) beachten",
            "Bauvoranfrage bei der zuständigen Bauaufsichtsbehörde stellen",
            "Bei Campingplätzen: Vertrag auf Dauerwohn-Erlaubnis und Höchstaufenthaltsdauer prüfen",
        ]),
        city_links=render_city_links("tiny-house"),
    ),

    "einliegerwohnung-baugenehmigung": dict(
        title="Einliegerwohnung Baugenehmigung: Nutzungsänderung & Voraussetzungen (2026)",
        meta_description="Wann braucht eine Einliegerwohnung eine Baugenehmigung oder Nutzungsänderung? Voraussetzungen wie Deckenhöhe, Rettungswege und Stellplätze.",
        breadcrumb="Einliegerwohnung",
        h1="Einliegerwohnung Baugenehmigung: Nutzungsänderung & Voraussetzungen (2026)",
        lead="Eine Einliegerwohnung entsteht meist durch eine Nutzungsänderung bestehender Räume (z. B. Keller oder Dachgeschoss) – und die ist praktisch immer genehmigungspflichtig.",
        facts=render_list([
            "Die Umwandlung von z. B. Keller, Hobbyraum oder Dachgeschoss in Wohnraum ist eine <strong>genehmigungsbedürftige Nutzungsänderung</strong>, auch wenn keine baulichen Veränderungen erfolgen.",
            "Zentrale Voraussetzungen: ausreichende <strong>Aufenthaltsraumhöhe</strong>, Belichtung/Belüftung, ein zweiter <strong>Rettungsweg</strong> und ggf. zusätzliche <strong>Stellplätze</strong>.",
            "Der <strong>Bebauungsplan</strong> muss eine zweite Wohneinheit auf dem Grundstück zulassen (z. B. keine Beschränkung auf 'Einzelhaus').",
            "Eine bereits genehmigte Nutzung (z. B. als Fitnessraum) gibt <strong>keine Rechtsgrundlage</strong> für eine spätere Wohnnutzung – der Wechsel muss separat beantragt werden.",
            "Ohne Genehmigung drohen Bußgelder und im schlimmsten Fall eine Nutzungsuntersagung durch die Bauaufsichtsbehörde.",
        ]),
        project_option="Einliegerwohnung / Dachausbau",
        project_placeholder="z. B. Kellergeschoss zu Einliegerwohnung, ca. 45 m²",
        table_heading="Voraussetzungen für eine genehmigte Einliegerwohnung",
        table_intro="Die folgenden Punkte werden von der Bauaufsichtsbehörde im Rahmen der Nutzungsänderung geprüft – unabhängig vom Bundesland.",
        table_rows=render_rows([
            ("Aufenthaltsraumhöhe", "jeweilige LBO", "Mindestdeckenhöhe muss eingehalten werden (häufig ca. 2,2–2,4 m)"),
            ("Rettungswege", "jeweilige LBO", "Zweiter Rettungsweg (z. B. Fenster ausreichender Größe) erforderlich"),
            ("Stellplätze", "kommunale Stellplatzsatzung", "Zusätzlicher Stellplatz je Wohneinheit oft vorgeschrieben"),
            ("Bebauungsplan", "BauGB / kommunaler B-Plan", "Muss zweite Wohneinheit zulassen (z. B. keine reine Einzelhausfestsetzung)"),
        ]),
        table_disclaimer="Zuletzt geprüft: September 2026 von Igor Kazazic, geprüft nach den Landesbauordnungen, keine Rechtsberatung. Der Ablauf (Kenntnisgabeverfahren, vereinfachtes oder umfassendes Verfahren) unterscheidet sich je nach Bundesland und Gemeinde.",
        extra_section="",
        checklist_heading="Unterlagen für den Antrag auf Nutzungsänderung",
        checklist_items=render_list([
            "Bauantrag mit Angabe der bisherigen und der geplanten Nutzung",
            "Grundriss mit Kennzeichnung der neuen Raumaufteilung (eigener Zugang, Sanitär, Küche)",
            "Nachweis ausreichender Belichtung/Belüftung und Rettungswege",
            "Ggf. statischer Nachweis bei baulichen Änderungen",
            "Prüfung der Stellplatzpflicht nach kommunaler Satzung",
        ]),
        city_links=render_city_links("einliegerwohnung"),
    ),
}


def main():
    for slug, data in PAGES.items():
        html = PAGE_TEMPLATE.format(slug=slug, **data)
        path = os.path.join(OUTDIR, f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"geschrieben: {path}")


if __name__ == "__main__":
    main()
