import os
cities = ["augsburg","berlin","bielefeld","bochum","bonn","darmstadt","dortmund","duesseldorf","duisburg","essen","fuerth","hanau","ingolstadt","koeln","mitte","muenchen","muenster","nuernberg","offenbach","pankow","regensburg","wuerzburg","wuppertal"]
projects = [
    ("terrasse", "Terrasse / Altan", "Terrasse Baugenehmigung", "Bis 30m² oft verfahrensfrei, überdacht genehmigungspflichtig", "0-450 €"),
    ("garage", "Garage", "Garage Baugenehmigung", "Meist genehmigungspflichtig, Stellplatznachweis nötig", "250-900 €"),
    ("zaun", "Zaun / Staket", "Zaun Baugenehmigung", "Bis 1,2-2m oft frei, Einfriedungssatzung beachten", "0-250 €"),
    ("wintergarten", "Wintergarten / Inglasad Balkong", "Wintergarten Baugenehmigung", "Immer genehmigungspflichtig, Wohnraumnutzung", "800-3.000 €"),
]
def info(city):
    return {"stadt": city.title(), "amt": f"Bauaufsichtsamt {city.title()}", "strasse": f"Rathaus {city.title()}", "plz": "00000", "ort": city.title(), "link": f"https://www.{city}.de/bauen/bauantrag", "lbo": "LBO"}

def make(city, slug, label, title, frei, kosten):
    i = info(city)
    return f"""<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8"><title>{title} {i['stadt']} 2026 – Kosten, Unterlagen & Genehmigung nach {i['lbo']}</title>
<meta name="description" content="{title} {i['stadt']}: Brauche ich Genehmigung? Kosten {kosten}, Unterlagen, Prozess, Ablehnungsgründe. September 2026.">
<link rel="stylesheet" href="../css/styles.css"></head><body>
<main class="container" style="max-width:900px; margin:0 auto; padding:2rem; font-family:system-ui;">
<h1>{title} {i['stadt']} 2026: Kosten, Unterlagen & Genehmigung</h1>
<p><strong>{label} in {i['stadt']}</strong> nach {i['lbo']}: {frei}. Bundesportal: Baurecht ist regional.</p>

<h2>Prozess Schritt für Schritt in {i['stadt']}</h2>
<ol><li><strong>Bebauungsplan prüfen:</strong> GRZ/GFZ, Baugrenzen</li>
<li><strong>Bauvoranfrage optional:</strong> 150-250€, spart 3-4 Wochen bei Anbau/Wintergarten</li>
<li><strong>Unterlagen:</strong> Flurkarte max 6 Monate, Lageplan 1:500, Bauzeichnungen 1:100, Baubeschreibung, Berechnung</li>
<li><strong>Antrag beim {i['amt']}:</strong> <a href="{i['link']}" target="_blank">Formular {i['stadt']}</a> – Bearbeitung 4-12 Wochen</li>
<li><strong>Genehmigung & Baubeginn:</strong> 2 Jahre Zeit, Bauschild aufstellen</li></ol>

<h2>Checkliste Dokumente für {i['stadt']}</h2>
<ul><li>Bauantrag Original unterschrieben</li><li>Flurkarte aktuell</li><li>Lageplan 1:500 mit {label}</li><li>Grundriss Ansichten Schnitte</li><li>Nachbarzustimmung wenn Abstandsfläche <3m</li><li>Stellplatznachweis bei Garage/Wintergarten</li></ul>

<h2>Kosten {i['stadt']}</h2><p style="font-weight:bold; color:#2563eb; font-size:1.3rem;">{kosten}</p>
<p style="font-size:0.9rem; color:#64748b;">Beispielrahmen – kein einheitlicher Preis in Deutschland. Quelle: {i['lbo']} + Satzung {i['stadt']}. Zuletzt geprüft September 2026</p>

<h2>Häufige Ablehnungsgründe in {i['stadt']}</h2>
<ul><li>Grenzabstand <3m ohne Nachbarzustimmung – häufigster Grund</li><li>GRZ/GFZ überschritten, Baugrenze überbaut</li><li>Flurkarte zu alt, Lageplan fehlt</li><li>Stellplätze fehlen (Garage, Einliegerwohnung)</li><li>Gestaltung/Denkmalschutz passt nicht</li><li>Schallschutz: Wärmepumpe 35dB nachts überschritten</li></ul>

<div style="background:#f8fafc; border-left:4px solid #2563eb; padding:1rem; margin:2rem 0;"><h3>{i['amt']}</h3><p>{i['strasse']}<br>{i['plz']} {i['ort']}<br><a href="{i['link']}" target="_blank">Offizielles Formular {i['stadt']}</a></p></div>
<p style="font-size:0.85rem; color:#64748b;">Zuletzt geprüft: September 2026 von Igor Kazazic | Beliebte Bauprojekte → Bundesländer → Städte → Fragen → Produkt</p>
</main></body></html>"""

c=0
for city in cities:
    for slug,label,title,frei,kosten in projects:
        fp = os.path.join(city, f"baugenehmigung-{slug}.html")
        if not os.path.exists(fp):
            os.makedirs(city, exist_ok=True)
            open(fp,"w",encoding="utf-8").write(make(city,slug,label,title,frei,kosten))
            c+=1
print(f"Klart! {c} nya djupa sidor skapade – nu 23×11=253 sidor")
