import React from 'react';
import { Metadata } from 'next';
import Link from 'next/link';
export const metadata: Metadata = {
title: 'AGB | GebührenAtlas',
description: 'Allgemeine Geschäftsbedingungen für die Nutzung von gebuehrenatlas.de und
den Erwerb digitaler Produkte',
};
export default function AGBPage() {
return (
<main className="max-w-4xl mx-auto px-6 py-16 text-gray-800 leading-relaxed">
<div className="mb-8">
<Link href="/" className="text-sm font-semibold text-zinc-600 hover:text-black
inline-flex items-center gap-1">
← Zurück zur Startseite
</Link>

</div>
<h1 className="text-3xl font-bold mb-10">Allgemeine Geschäftsbedingungen (AGB)</h1>
<div className="space-y-8">
<section>
<h2 className="text-xl font-semibold mb-3">§ 1 Geltungsbereich und
Vertragsgegenstand</h2>
<p className="mb-2">(1) Diese Allgemeinen Geschäftsbedingungen (AGB) gelten für
alle Verträge über die Nutzung der Website <strong>gebuehrenatlas.de</strong> und den
Erwerb digitaler Produkte (z. B. Planungs- und Antrag-Templates), die zwischen <strong>Igor
Kazazic</strong>, <strong>Segeparksgatan 18, 212 50 Malmö, Sverige</strong>,
<strong>igorkazazic1989@gmail.com</strong> (im Folgenden &quot;Anbieter&quot;) und dem
Kunden geschlossen werden.</p>
<p className="mb-2">(2) Gegenstand des Vertrages ist die Bereitstellung von
digitalen Inhalten (PDFs, Checklisten und Excel- bzw. Dokumentvorlagen) zum Download nach
erfolgreichem Kauf.</p>
</section>
<section>
<h2 className="text-xl font-semibold mb-3">§ 2 Vertragsschluss</h2>
<p className="mb-2">(1) Die Darstellung der digitalen Produkte auf der Website
stellt kein rechtlich bindendes Angebot, sondern einen unverbindlichen Online-Katalog dar.
</p>
<p>(2) Durch den Abschluss des Bezahlvorgangs über unseren Zahlungsdienstleister
gibt der Kunde ein verbindliches Angebot zum Kauf des jeweiligen digitalen Produkts ab. Der
Vertrag kommt mit der Bereitstellung und dem Download-Zugang des Produkts zustande.</p>
</section>
<section>
<h2 className="text-xl font-semibold mb-3">§ 3 Preise und
Zahlungsbedingungen</h2>
<p className="mb-2">(1) Alle Preise sind Endpreise in EUR. Da der Anbieter
Kleinunternehmer im Sinne des UStG bzw. eine Privatperson mit Sitz in Schweden ist, wird
keine deutsche Umsatzsteuer gesondert ausgewiesen (sofern anwendbar).</p>
<p>(2) Die Bezahlung erfolgt über die auf der Website angebotenen Zahlungsarten
unmittelbar bei Vertragsschluss.</p>
</section>
<section>
<h2 className="text-xl font-semibold mb-3">§ 4 Bereitstellung und
Nutzungsrecht</h2>
<p className="mb-2">(1) Die Bereitstellung der digital erworbenen Inhalte erfolgt
unmittelbar nach Zahlungsabwicklung als Download.</p>
<p>(2) Dem Kunden wird ein einfaches, nicht übertragbares und zeitlich
unbeschränktes Nutzungsrecht zur privaten bzw. geschäftlichen Eigenverwendung eingeräumt.
Eine Weitergabe, Veröffentlichung oder kommerzielle Weiterverarbeitung der Templates ist
untersagt.</p>
</section>
<section>
<h2 className="text-xl font-semibold mb-3">§ 5 Haftungsausschluss</h2>
<p className="mb-2">(1) Alle bereitgestellten Informationen, Kostenübersichten
und Templates auf gebuehrenatlas.de werden sorgfältig recherchiert, erfolgen jedoch ohne
Gewähr. Eine offizielle Rechtsberatung oder verbindliche Auskunft der zuständigen Behörden
wird ausdrücklich nicht ersetzt.</p>
<p>(2) Der Anbieter haftet unbeschränkt nur für Vorsatz und grobe Fahrlässigkeit.
</p>
</section>
<section>
<h2 className="text-xl font-semibold mb-3">§ 6 Schlussbestimmungen</h2>
<p className="mb-2">(1) Es gilt das Recht Schwedens unter Ausschluss des UNKaufrechts.</p>
<p>(2) Gerichtsstand für alle Streitigkeiten aus diesem Vertrag ist der Sitz des
Anbieters, sofern gesetzlich zulässig.</p>
</section>
</div>
<div className="mt-12 pt-6 border-t">

<Link href="/" className="text-sm font-semibold text-zinc-600 hover:text-black">
← Zurück zur Startseite
</Link>
</div>
</main>
);
}
==============================
