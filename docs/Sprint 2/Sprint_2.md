# Sprint 2

### Schritt 1: Sprint Planning

Zu Beginn des zweiten Sprints habe ich die relevanten Anforderungen (Requirements) ausgewählt. 
Der Fokus lag dabei auf der Implementierung der grafischen Benutzeroberfläche, die für die 
Interaktion mit dem Elektrogrill essenziell ist. Konkret wurden folgende Kernfunktionen 
identifiziert und berücksichtigt:

- Strukturierte Darstellung der Temperaturen
- Änderung der Wunschtemperatur über GUI-Elemente
- Anzeige des Grillstatus
- Nutzerinteraktionen (Buttons, Eingabefelder)
- Live-Aktualisierung der Anzeigen

Bei der Auswahl der Anforderungen wurde bewusst auf eine realistische und zielgerichtete Planung 
geachtet. Mit dem GUI-Entwurf wird die Basis für die Benutzerinteraktion geschaffen und die 
bisherige reine Logik-Schicht mit der Präsentationsschicht verbunden. Sprint 3 kann dann für 
weitere Funktionen und zur Verfeinerung genutzt werden.

**Requirements:**

- Req. F1.3: Validierung der Eingabewerte
- Req. F6: GUI-Interaktion
- Req. F7: Fehleranzeigen im GUI
- Req. NF6.2: Tools & Packages (Tkinter)
- Req. NF6.3: Modularität (gui_main.py)
- Req. NF6.4: Erweiterbarkeit
- Req. NF6.5: Robustheit / Fehlerresistenz
- Req. NF6.6: Konsistente Schnittstellen

**Sprint-Zeitraum:** 01.12.2025 - 15.12.2025

**Sprintziel:**

1. Entwurf der Benutzeroberfläche für die Temperatursteuerung des Elektrogrills mittels **Tkinter**
2. Definition der GUI-Struktur (Layouts, Widgets, Interaktionslogik)
3. Verbindung der GUI-Schicht mit der Kernlogik aus Sprint 1
4. Sicherstellen, dass alle UI-Elemente den funktionalen Anforderungen entsprechen

---

### Schritt 2: Architektur

Nach der Anforderungsanalyse beschäftigte ich mich mit der Softwarearchitektur für die GUI-Integration. 
Ziel war es, eine geeignete strukturelle Grundlage für die Benutzeroberfläche zu schaffen und diese 
sauber mit der bestehenden Logik-Schicht zu verbinden.

Basierend auf den funktionalen Anforderungen und den nicht-funktionalen Anforderungen wie 
Übersichtlichkeit und Responsivität fiel die Wahl auf eine **Drei-Schicht-Struktur (MVC)** 
mit klarer Separation of Concerns.

**A1. Drei-Schicht-Struktur:** Model (fertig aus Sprint 1), Controller (Teil von GrillController, Erweiterung für UI-Interaktionen), View (GUI) – wird in Sprint 2 erstellt.

**A2. GUI-Schicht als eigene Klasse:** Neue Klasse `GrillGUI` mit Verantwortlichkeiten: Aufbau des Tkinter-Fensters, Layout-Management (Frames, Grid), visuelle Darstellung der Model-Daten, Weiterleitung von Benutzeraktionen an den Controller.

**A3. Lose Kopplung:** Die GUI fragt nur über den Controller nach Daten ab. Keine direkte Änderung der Model-Schicht durch die GUI.

**A4. Ereignissteuerung:** Periodische Aktualisierung mit Tkinter: `root.after(interval, callback)`. Keine while-Schleifen → GUI bleibt reaktionsfähig.

[Architektur](../Architektur.md)

---

### Schritt 3: Design

Im Anschluss an die Architekturdefinition wurde der Entwurfsprozess auf GUI-Ebene fortgeführt. 
Ziel war es, die zentralen GUI-Komponenten und deren Layout zu identifizieren sowie die 
Interaktionslogik anhand geeigneter Strukturen zu modellieren.

**Layoutstruktur:** HeaderFrame (Titel des Systems), TemperatureFrame (Anzeige aktuelle Temperatur, Wunschtemperatur, Buttons + / –), StatusFrame (Zieltemperaturstatus, Resttemperaturstatus), PowerFrame (An-/Aus-Button, Statusanzeige).

**Zentrale Widgets:** Label für Temperaturanzeigen, Button für Interaktion, Frame zur Strukturierung, Optional Canvas oder farbige Labels für Statusindikatoren.

**GUI-Methoden:** `update_display()` aktualisiert alle Anzeigen regelmäßig über `.after()`. Weitere Methoden: `increase_target_temperature()`, `decrease_target_temperature()`, `toggle_power()`, `refresh_status_indicators()`.

**Keine Business-Logik in der GUI:** GUI darf keine Temperaturen berechnen. Validierungen und Statuslogik bleiben vollständig in der Model-Schicht.

[Design](Design2.md)

---

### Schritt 4: Implementierung

Nach Abschluss der Designphase begann die Umsetzung der Benutzeroberfläche gemäß der zuvor 
definierten Architektur- und Entwurfsdokumente. Dabei wurde iterativ und testgetrieben vorgegangen, 
um frühzeitig funktionale Korrektheit und Konsistenz sicherzustellen.

Zunächst wurde die neue Klasse `GrillGUI` implementiert mit allen geplanten Frames und Widgets. 
Der Fokus lag auf der sauberen Umsetzung der GUI-Struktur und der klaren Trennung zwischen 
Präsentation und Logik.

**Klasse GrillGUI:** Implementierung eines Tkinter-Fensters mit Temperaturanzeigen, Buttons, Statusanzeigen, Power-Toggle.

**GUI–Controller-Verbindung:** GrillGUI erhält eine Instanz von `GrillController`. Alle GUI-Ereignisse delegieren an Controller-Methoden.

**Aktualisierungslogik:** Implementierung der Methode `update_display()`, Aufruf alle 200–500 ms. Aktualisiert: Temperaturen, An/Aus-Status, Zieltemperaturstatus, Restwärmestatus.

**Eingabevalidierung:** Nur gültige Temperaturwerte werden übernommen. Ungültige Werte lösen Popup oder Fehlermeldung aus.

**Kontinuierliche Tests:** Bereits während der Implementierung wurden manuelle Tests durchgeführt – sowohl über die GUI als auch über die Kommandozeile.

[Implementierung](Implementierung2.md)

---

### Schritt 5: Test

Nach Abschluss der Implementierung wurden alle während der Entwicklung durchgeführten Tests als 
formale Testfälle dokumentiert. Darauf aufbauend wurden das übergeordnete Ziel des Testens, die 
geplanten Testarten sowie deren Abdeckung definiert und eine Teststrategie festgelegt.

Um die interne Codequalität sicherzustellen, wurde ein Codereview durchgeführt. Der Code wurde 
basierend auf den Ergebnissen überarbeitet. Anschließend wurden gezielt weitere Testfälle ergänzt, 
um die vollständige Abdeckung aller Hauptanforderungen sicherzustellen.

[Test](Test2.md)

---

### Schritt 6: Retrospektive

**Was lief gut?**

- Alle Requirements wurden umgesetzt
- Klare Fokussierung auf GUI-Integration
- Gute Integration mit bestehender Logik-Schicht aus Sprint 1
- Tests wurden bereits während der Implementierung durchgeführt, was die Qualität verbesserte
- Die Dokumentation wurde konsequent aktualisiert

**Was lief nicht so gut?**

- Aus der Design-Phase wurden nicht alle Aspekte 1:1 in der Implementierung umgesetzt
- Einige GUI-Komponenten erwiesen sich als komplexer als ursprünglich geplant
- Validierungslogik teilweise doppelt vorhanden (GUI und Model)

**Was werde ich im nächsten Sprint anders machen?**

- Die Design-Phase noch gründlicher durchführen, um spätere Anpassungen zu vermeiden
- Einheitliche Validierungsstrategie etablieren
- Früher mit Prototyping beginnen

**Lessons Learned:**

- Funktionierende Abläufe und klare Strukturen erleichtern die Arbeit erheblich
- Die kontinuierliche Dokumentation und Aktualisierung während des Sprints ist entscheidend
- Die frühzeitige Identifikation von Fehlern während der Implementierung spart Zeit
- GUI-Tests sollten strukturierter angegangen werden
- Lose Kopplung zwischen GUI und Controller zahlt sich aus

---

## Abweichungen

**Vergleich von Software-Architektur und -Design mit der tatsächlichen Implementierung:**

| Bereich | Geplant | Implementiert | Abweichung | Grund | Status |
|---------|---------|--------------|-----------|-------|--------|
| **Schichtenmodell (GUI - Controller - Model)** | Strikte 3-Schichten-Struktur: GUI ↔ Controller ↔ Model mit definierten Schnittstellen | GUI ↔ Controller ↔ Model korrekt implementiert; Schnittstellen als Callbacks realisiert | ✅ Keine Abweichung | Saubere Architektur war erfolgreich | ✅ Umgesetzt |
| **GUI-Komponentenstruktur** | Grundlegende GUI-Komponenten als Entwurf mit einfachem Layouting | Erweiterte Struktur mit dynamischer Aktivierung/Deaktivierung von Buttons, Grid-Layout | ⚠️ Umsetzung erweitert | Testbarkeit und Klarheit verbessern | ✅ Ausreichend |
| **Update-Mechanismus** | Periodische Aktualisierung mit `.after()` | `update_display()` wird regelmäßig mit `root.after()` aufgerufen | ✅ Keine Abweichung | Ereignissteuerung funktioniert wie geplant | ✅ Umgesetzt |
| **Validierungslogik** | Nur gültige Temperaturwerte werden übernommen | Zusätzliche Validierungslogik direkt in GUI-Eingabefeld neben Model-Validierung | ⚠️ GUI übernimmt mehr als geplant | Vereinfachung und schnellere Fehlertoleranz | ⚠️ Zu refaktorisieren in Sprint 3 |
| **Statusanzeigen** | Erst vollständig in Sprint 3 | Bereits funktionale Statusdarstellungen implementiert | ⚠️ Vorverlagerung von Sprint 3 | Technisch sinnvoll und zeiteffizient | ✅ Ausreichend |
| **Button-Zustandslogik** | Einfache Enable/Disable-Logik | Erweitert mit kontextabhängigen Zustandsübergängen | ⚠️ Umsetzung erweitert | Bessere Benutzerführung | ✅ Ausreichend |
