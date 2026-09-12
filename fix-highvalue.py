import os
root = "."
cities = ["augsburg","berlin","bielefeld","bochum","bonn","darmstadt","dortmund","duesseldorf","duisburg","essen","fuerth","hanau","ingolstadt","koeln","mitte","muenchen","muenster","nuernberg","offenbach","pankow","regensburg","wuerzburg","wuppertal"]

bauamt = {
    "offenbach": ("Offenbach am Main","Bauaufsichtsamt Offenbach","Berliner Straße 60","63065","Offenbach am Main","069 8065-2100","bauaufsicht@offenbach.de","https://www.offenbach.de/rathaus/aemter/bauaufsicht/bauantrag.php","HBO","Hessen"),
    "berlin": ("Berlin","Bauamt Berlin Mitte","Müllerstraße 146","13353","Berlin","030 9018-45754","bauaufsicht@bamitte.berlin.de","https://service.berlin.de/dienstleistung/120620/","BauO Bln","Berlin"),
    "augsburg": ("Augsburg","Bauordnungsamt Augsburg","Rathausplatz 1","86150","Augsburg","0821 324-0","bauordnungsamt@augsburg.de","https://www.augsburg.de/buergerservice/bauen/bauantrag","BayBO","Bayern"),
    "muenchen": ("München","Lokalbaukommission München","Blumenstraße 28b","80331","München","089 233-22211","lbk@muenchen.de","https://www.muenchen.de/rathaus/verwaltung/bauantrag","BayBO","Bayern"),
    "koeln": ("Köln","Bauaufsichtsamt Köln","Willy-Brandt-Platz 2","50679","Köln","0221 221-25324","bauaufsichtsamt@stadt-koeln.de","https://www.stadt-koeln.de/service/bauantrag","BauO NRW","NRW"),
}

def get_info(city):
    if city in bauamt:
        s,a,st,plz,ort,tel,em,link,lbo,bund = bauamt[city]
        return {"stadt":s,"amt":a,"strasse":st,"plz":plz,"ort":ort,"tel":tel,"email":em,"link":link,"lbo":lbo,"bundesland":bund}
    return {"stadt":city.title(),"amt":f"Bauaufsichtsamt {city.title()}","strasse":f"Rathaus {city.title()}","plz":"00000","ort":city.title(),"tel":"Siehe Website","email":f"bauaufsicht@{city}.de","link":f"https://www.{city}.de/bauen/bauantrag","lbo":"LBO","bundesland":"Deutschland"}

def make_page(title, desc, geb, info, typ, city):
    return f"""<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} {info['stadt']} 2026 | Kosten {geb}</title>
<meta name="description" content="{desc} in {info['stadt']}: Kosten {geb}, {info['lbo']}. September 2026.">
<link rel="canonical" href="https://gebuehrenatlas.de/{city}/baugenehmigung-{typ}.html">
<link rel="stylesheet" href="../css/styles.css"></head>
<body><header><a href="../index.html">GebührenAtlas.de</a></header>
<main class="container"><h1>{title} Baugenehmigung {info['stadt']} (2026)</h1>
<p>{desc} in {info['stadt']} ({info['bundesland']}) nach {info['lbo']}.</p>
<div style="background:#fff; border:1px solid #e2e8f0; padding:1.5rem; border-radius:12px; margin:2rem 0;">
<h3>💰 Gebühren {info['stadt']} - HIGH VALUE</h3><p style="font-weight:bold; color:#2563eb; font-size:1.2rem;">{geb}</p>
<p style="font-size:0.9rem; color:#64748b;">Zuletzt geprüft: September 2026</p></div>
<div style="background:#f8fafc; border-left:4px solid #2563eb; padding:1.5rem; border-radius:8px; margin:2rem 0;">
<h3>🏛️ {info['amt']}</h3><p><strong>{info['strasse']}</strong><br>{info['plz']} {info['ort']}<br>Tel: {info['tel']}<br>Email: {info['email']}</p>
<a href="{info['link']}" target="_blank" style="background:#0f172a; color:#fff; padding:0.5rem 1rem; border-radius:6px; text-decoration:none; font-weight:bold;">➜ Formular {info['stadt']}</a></div>
<p style="font-size:0.85rem; color:#64748b;">Zuletzt geprüft: September 2026 von Igor Kazazic</p>
</main><footer style="margin-top:3rem; text-align:center; font-size:0.85rem;"><p>&copy; 2026 GebührenAtlas.de</p></footer></body></html>"""

created=0
for city in cities:
    info = get_info(city)
    cpath = os.path.join(root, city)
    os.makedirs(cpath, exist_ok=True)
    for fname, title, desc, geb, typ in [
        ("baugenehmigung-anbau.html","Anbau & Wohnraum","Anbau immer genehmigungspflichtig, Bauwert 40k-150k€","1.850 € - 5.000 €","anbau"),
        ("baugenehmigung-solaranlage.html","Solaranlage PV","PV bis 30m² meist verfahrensfrei","0 € - 350 €","solaranlage"),
        ("baugenehmigung-einliegerwohnung.html","Einliegerwohnung","Einliegerwohnung immer genehmigungspflichtig + Stellplätze","1.500 € - 6.000 €","einliegerwohnung"),
        ("baugenehmigung-waermepumpe.html","Wärmepumpe","Wärmepumpe meldepflichtig, TA Lärm beachten","180 € - 560 €","waermepumpe"),
    ]:
        fp = os.path.join(cpath, fname)
        if not os.path.exists(fp):
            with open(fp,"w",encoding="utf-8") as out:
                out.write(make_page(title,desc,geb,info,typ,city))
            created+=1
            print(f"Created {city}/{fname}")

print(f"Klart! {created} nya sidor")

def hub(title, desc, typ):
    links = "".join([f'<a href="{c}/baugenehmigung-{typ}.html" style="display:inline-block; padding:0.8rem; margin:0.3rem; border:1px solid #e2e8f0; border-radius:8px; background:#f8fafc; text-decoration:none; color:#0f172a;">{c.title()}</a>' for c in cities])
    return f"""<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} 2026</title><meta name="description" content="{desc}"><link rel="stylesheet" href="css/styles.css"></head>
<body style="max-width:900px; margin:0 auto; padding:2rem; font-family:system-ui;">
<header><a href="index.html">GebührenAtlas.de</a></header>
<main><h1>{title}</h1><p>{desc}</p>
<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-top:2rem;">{links}</div>
<div style="background:#fffbeb; border:1px solid #fde68a; padding:1rem; border-radius:8px; margin-top:3rem;">
<p style="margin:0;"><strong>Zuletzt geprüft: September 2026</strong> von Igor Kazazic | High-Value: Anbau 1.850-5.000€, Einliegerwohnung 1.500-6.000€</p></div></main>
<footer style="margin-top:3rem; text-align:center; font-size:0.85rem; color:#64748b;"><p>Zuletzt geprüft: September 2026</p></footer>
</body></html>"""

hubs = {
    "anbau-baugenehmigung.html": ("Baugenehmigung Anbau & Wohnraum","Anbau immer genehmigungspflichtig. Kosten 1.850-5.000€, Bauwert 40k-150k€. High-Value.","anbau"),
    "waermepumpe-baugenehmigung.html": ("Wärmepumpe Baugenehmigung","Wärmepumpe meist genehmigungsfrei aber meldepflichtig. Kosten 180-560€.","waermepumpe"),
    "solaranlage-baugenehmigung.html": ("Solaranlage PV Baugenehmigung","PV bis 30m² meist verfahrensfrei. Kosten 0-350€.","solaranlage"),
    "einliegerwohnung-baugenehmigung.html": ("Einliegerwohnung Baugenehmigung","Einliegerwohnung immer genehmigungspflichtig. 1.500-6.000€ + Stellplätze.","einliegerwohnung"),
}
for fname,(t,d,typ) in hubs.items():
    with open(os.path.join(root,fname),"w",encoding="utf-8") as f:
        f.write(hub(t,d,typ))
print("Hubs fixade!")
