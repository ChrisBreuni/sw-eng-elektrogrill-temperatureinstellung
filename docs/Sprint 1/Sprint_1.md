# Sprint 1 - Kernlogik

### Schritt 1: Sprint Planning

Zu Beginn des ersten Sprints habe ich die relevanten Anforderungen (Requirements) ausgewählt. 
Der Fokus lag dabei auf der Implementierung grundlegender Teilfunktionalitäten, die für den weiteren
Projektverlauf essenziell sind. Konkret wurden folgende Kernfunktionen identifiziert und berücksichtigt:

- Wunschtemperaturanzeige
- Wunschtemperaturänderung
- Aktuelle Temperatur

Bei der Auswahl der Anforderungen wurde bewusst auf eine realistische und zielgerichtete Planung geachtet. Der Fokus lag auf der Implementierung der absoluten Grundfunktionen, die für die weitere Entwicklung des Elektrogrills wesentlich sind.

**Requirements:**

- Req. F1.1: Wunschtemperaturanzeige
- Req. F1.2: Wunschtemperaturänderung
- Req. F2.1: Aktuelle Temperatur

**Sprint-Zeitraum:** 03.11.2025 - 30.11.2025

**Sprintziel:**

1. Erstellung einer übersichtlichen Grundstruktur
2. Evaluierung und finale Auswahl der geeigneten Programmiersprache
3. Definition der grundlegenden Anforderungen und Architektur für den Projektstart

---

### Schritt 2: Architektur

Nach der Anforderungsanalyse beschäftigte ich mich mit der Softwarearchitektur des Projekts. 
Ziel war es, eine geeignete strukturelle Grundlage für die spätere Implementierung zu schaffen.

Basierend auf den funktionalen Anforderungen und den nicht-funktionalen Anforderungen wie 
Wartbarkeit und Erweiterbarkeit fiel die Wahl auf eine **modulare Schichtenarchitektur** 
mit klarer Trennung der Verantwortlichkeiten.


**A1. Modularer Aufbau:** Trennung der Kernlogik in einzelne Python-Module (`current_temperature.py`, `target_temperature.py`, `grill_controller.py`). Jede Komponente übernimmt klar abgegrenzte Verantwortlichkeiten (Single Responsibility Principle).

**A2. Model-Schicht vorbereiten (MVC-Vorbereitung):** Aufbau einer Model-Schicht für alle temperaturbezogenen Berechnungen und Validierungen. GUI-Schicht (Tkinter) wird im Sprint 1 nicht implementiert, aber durch klare Schnittstellen vorbereitet.

**A3. Temperature-Management-Kern:** Zentrale Klasse/Modul für die Verwaltung der aktuellen und gewünschten Temperatur. Implementierung von Validierungslogiken für Temperaturbereiche (50–500 °C, sowie 0 für „noch nicht gesetzt" bei Zieltemperaturen). Definition von Statuszuständen: Heating, Target Reached, Cooling Down.

**A4. Power-State-Management:** Architektur für die An-/Ausfunktion vorbereiten. Separates Modul für den Betriebsstatus des Grills.

[Architektur](../Architektur.md)

---

### Schritt 3: Design

Im Anschluss an die Architekturdefinition wurde der Entwurfsprozess auf Klassenebene
fortgeführt. Ziel war es, zentrale Klassen und deren Interaktionen zu identifizieren 
sowie die Systemlogik anhand geeigneter UML-Diagramme zu modellieren.

**Design-Highlights:**

- **Klare Klassen- und Methodensignaturen:** Entwurf der Klassen: `CurrentTemperature`, `TargetTemperature`, `GrillController`. Wichtige öffentliche Methoden: `set_temperature()`, `get_temperature()`, `is_valid()`, `is_target_reached()`, `turn_on()`, `turn_off()`.

- **Defensive Design:** Ungültige Temperaturwerte (<50 oder >500 °C) werden sofort abgefangen. Nutzung privater Hilfsmethoden wie `_validate()`.

- **Erweiterbarkeit:** Design so aufgebaut, dass die GUI mittels Tkinter später ohne größere Änderungen ergänzt werden kann. Klare Abgrenzung zwischen Logik (Model) und Benutzeroberfläche (View/Controller).

- **Zustandsorientiertes Design:** Einführung einfacher Statuswerte: `ON`, `OFF`, `TARGET_REACHED`, `COOLING_DOWN`.

[Design](Design1.md)

---

### Schritt 4: Implementierung

Nach Abschluss der Designphase begann die Umsetzung der Anwendung gemäß der zuvor definierten Architektur- und Entwurfsdokumente. Dabei wurde iterativ und testgetrieben vorgegangen, um frühzeitig funktionale Korrektheit und Konsistenz sicherzustellen.

Zunächst wurden die in der Designphase entworfenen Klassen und Schnittstellen gemäß dem Klassendiagramm implementiert. Der Fokus lag auf der sauberen Umsetzung der öffentlichen Schnittstellen und der klaren Trennung zwischen interner Logik und extern zugänglichen Funktionen.

**Implementierungs-Schwerpunkte:**

- **Grundlegende Logik-Klassen:** Umsetzung in den Klassen: `CurrentTemperature`, `TargetTemperature`, `GrillController`, `PowerState`.

- **Validierungslogik:** Implementierung der Temperaturbereiche: gültig 50–500 °C, Zieltemperatur zusätzlich 0 = nicht gesetzt. Ungültige Werte lösen ValueError aus.

- **Statusbestimmung:** Implementierung der Logik: `target_reached = current >= target`. Rückgabe als Boolean für spätere UI-Nutzung.

- **Resttemperaturlogik:** Erkennung, ob der Grill ausgeschaltet, aber noch über 50 °C ist. Noch keine Anzeige, nur interne Methoden für die spätere GUI.

- **Unit Tests:** Schreiben von Unit Tests für Temperaturvalidierung, Zieltemperaturstatus und Power-State-Logik.

[Implementierung](Implementierung1.md)

---

### Schritt 5: Test

Nach Abschluss der Implementierung wurden alle durchgeführten Tests als formale Testfälle dokumentiert. Darauf aufbauend wurden das übergeordnete Ziel des Testens, die geplanten Testarten sowie deren Abdeckung definiert und eine Teststrategie festgelegt.

Um die interne Codequalität sicherzustellen, wurde eine Checkliste für das Codereview erstellt. Anschließend wurden gezielt weitere Testfälle ergänzt, um die vollständige Abdeckung aller Hauptanforderungen sicherzustellen. Abschließend wurden die Testergebnisse übersichtlich dokumentiert und mit den definierten Requirements in der Traceability Matrix verknüpft.

[Test](Test1.md)

---

### Schritt 6: Retrospektive

**Was lief gut?**

- Alle Requirements wurden umgesetzt.
- Fokus lag klar auf der Kernfunktionalität
- Gute Grundstruktur für spätere Erweiterungen geschaffen
- Tests wurden erfolgreich durchgeführt

**Was lief nicht so gut?**

- Die Tools waren noch nicht optimal eingerichtet
- Nicht konsequent direkt die Requirements, Lasten- und Pflichtenheft aktualisiert
- teils unübersichtliche Struktur der Dokumente 

**Was werde ich im nächsten Sprint anders machen?**

- Requirements-Doku auf dem aktuellen Stand halten
- sauberer Arbeiten, Struktur gleich und übersichtlich halten

**Lessons Learned:**

- Ich habe gelernt, dass ich mich nicht von der Vielzahl an Anforderungen überfordern lassen sollte
- Die richtige Architektur früh zu definieren vereinfacht die spätere Implementierung erheblich
- Klare Schnittstellen sind essentiell für wartbaren Code und spätere Hinzufügung von Features

---

## Abweichungen

**Vergleich von Software-Architektur und -Design mit der tatsächlichen Implementierung:**

| Bereich               | Geplant | Implementiert | Abweichung | Status |
|-----------------------|---------|--------------|-----------|--------|
| **Modularer Aufbau**  | Separate Module: `current_temperature.py`, `target_temperature.py`, `grill_controller.py` | Alle drei Module erfolgreich implementiert und getestet | ✅ Keine Abweichung | ✅ Umgesetzt |
| **Validierungslogik** | Temperaturbereich 50–500 °C, Zieltemperatur zusätzlich 0 | Vollständig implementiert mit ValueError-Handling | ✅ Keine Abweichung | ✅ Umgesetzt |
| **Statusmanagement**  | Zustände: Heating, Target Reached, Cooling Down | Zustände als interne Logik implementiert | ✅ Keine Abweichung | ✅ Umgesetzt |
| **GUI in Sprint 1**   | Nicht geplant – nur Logik-Kern | Nicht implementiert – Fokus auf Model-Schicht | ✅ Keine Abweichung | ✅ Korrekt |
| **MVC-Vorbereitung**  | Klare Schnittstellen für spätere GUI | Definierte Methoden wie `set_target_temperature()`, `get_current_temperature()` | ✅ Keine Abweichung | ✅ Umgesetzt |
