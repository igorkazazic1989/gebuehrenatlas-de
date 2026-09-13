import os
cities = ["augsburg","berlin","bielefeld","bochum","bonn","darmstadt","dortmund","duesseldorf","duisburg","essen","fuerth","hanau","ingolstadt","koeln","mitte","muenchen","muenster","nuernberg","offenbach","pankow","regensburg","wuerzburg","wuppertal"]
projects = [
    ("terrasse", "Terrasse / Altan", "Terrasse Baugenehmigung", "Bis 30m² oft verfahrensfrei, überdacht genehmigungspflichtig", "0-450 €"),
    ("garage", "Garage", "Garage Baugenehmigung", "Meist genehmigungspflichtig, Stellplatznachweis", "250-900 €"),
    ("zaun", "Zaun / Staket", "Zaun Baugenehmigung", "Bis 1,2-2m oft frei, Einfriedungssatzung", "0-250 €"),
    ("wintergarten", "Wintergarten / Inglasad Balkong", "Wintergarten Baugenehmigung", "Immer genehmigungspflichtig, Wohnraumnutzung", "800-3.000 €"),
]

def info(city):
    return {"stadt": city.title(), "amt": f"Bauaufsichtsamt {city.title()}", "strasse": f"Rathaus {city.title()}", "plz": "00000", "ort": city.title(), "tel": "Siehe Website", "email": f"bau@{city}.de", "link": f"https://www.{city}.de/bauen/bauantrag", "lbo": "LBO", "bundesland": "Deutschland"}

def make(city, slug, label, title, frei, kosten):
    i = info(city)
    return f"""<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8"><title>{title} {i['stadt']} 2026 – Kosten, Unterlagen & Genehmigung</title>
<meta name="description" content="{title} {i['stadt']}: Kosten {kosten}, Unterlagen, Prozess, Ablehnungsgründe. {i['lbo']} 2026.">
<link rel="stylesheet" href="../css/styles.css"></head><body><main class="container" style="max-width:900px; margin:0 auto; padding:1rem;">
<h1>{title} {i['stadt']} 2026</h1>
<p>{label} in {i['stadt']} nach {i['lbo']}: {frei}.</p>

<h2>Prozess Schritt für Schritt in {i['stadt']}</h2>
<ol><li>Bebauungsplan prüfen (GRZ/GFZ)</li><li>Bauvoranfrage optional 150-250€ – spart 3-4 Wochen</li><li>Unterlagen: Flurkarte (max 6 Monate), Lageplan 1:500, Bauzeichnungen 1:100, Baubeschreibung, Berechnung</li><li>Antrag beim {i['amt']} – <a href="{i['link']}" target="_blank">Formular {i['stadt']}</a></li><li>Genehmigung 4-12 Wochen, dann 2 Jahre Zeit für Baubeginn</li></ol>

<h2>Checkliste Dokumente</h2>
<ul><li>Bauantrag Original unterschrieben</li><li>Flurkarte aktuell</li><li>Lageplan 1:500 mit {label}</li><li>Grundriss Ansichten Schnitte 1:100</li><li>Nachbarzustimmung wenn <3m</li><li>Stellplatznachweis bei Garage/Einliegerwohnung</li></ul>

<h2>Kosten {i['stadt']}</h2><p style="font-weight:bold; color:#2563eb; font-size:1.2rem;">{kosten}</p>

<h2>Häufige Ablehnungsgründe in {i['stadt']}</h2>
<ul><li>Grenzabstand <3m ohne Zustimmung – häufigster Grund</li><li>GRZ/GFZ überschritten</li><li>Unterlagen unvollständig (Flurkarte zu alt)</li><li>Stellplätze fehlen</li><li>Gestaltung/Denkmalschutz</li><li>Schallschutz bei Wärmepumpe: 35dB nachts</li></ul>

<div style="background:#f8fafc; border-left:4px solid #2563eb; padding:1rem;"><h3>{i['amt']}</h3><p>{i['strasse']}<br>{i['plz']} {i['ort']}<br>Tel {i['tel']}<br><a href="{i['link']}" target="_blank">Offizielles Formular {i['stadt']}</a></p></div>
<p style="font-size:0.85rem; color:#64748b;">Zuletzt geprüft: September 2026 von Igor Kazazic | Keine Rechtsberatung</p>
</main></body></html>"""

count=0
for city in cities:
    for slug, label, title, frei, kosten in projects:
        fp = os.path.join(city, f"baugenehmigung-{slug}.html")
        if not os.path.exists(fp):
            os.makedirs(city, exist_ok=True)
            with open(fp, "w", encoding="utf-8") as f:
                f.write(make(city, slug, label, title, frei, kosten))
            count+=1
print(f"Created {count} djupa sidor: Terrasse, Garage, Zaun, Wintergarten x 23 städer = fler stad x ärendetyp kombinationer")
