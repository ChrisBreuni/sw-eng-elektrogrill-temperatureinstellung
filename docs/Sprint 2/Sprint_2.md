# Sprint 2 – GUI-Entwurf (Tkinter)

## Ziel des Sprints
1. Entwurf der Benutzeroberfläche für die Temperatursteuerung des Elektrogrills mittels **Tkinter**.  
2. Definition der GUI-Struktur (Layouts, Widgets, Interaktionslogik).  
3. Verbindung der GUI-Schicht mit der Kernlogik aus Sprint 1 (ohne vollständige Funktionalität).  
4. Sicherstellen, dass alle UI-Elemente den funktionalen Anforderungen entsprechen.

---

# Erweiterte funktionale Requirements für die GUI

## F-GUI1: Strukturierte Darstellung der Temperaturen
- Die GUI zeigt klar getrennt:
  - **Aktuelle Temperatur**
  - **Wunschtemperatur (Zieltemperatur)**
  - **Zieltemperaturstatus**
- Beide Anzeigen müssen optisch voneinander unterscheidbar sein.

## F-GUI2: Änderung der Wunschtemperatur
- Die GUI enthält Steuerelemente zur Änderung der Zieltemperatur:
  - Buttons (*+* / *–*)
  - oder alternativ ein Eingabefeld mit *Set*-Button.
- Werte außerhalb von **50–500 °C** sind nicht zulässig.

## F-GUI3: Anzeige des Grillstatus
- Die GUI zeigt klar sichtbar:
  - **An/Aus-Status**
  - **Resttemperaturstatus** (Grill aus, aber > 50 °C)

## F-GUI4: Nutzerinteraktionen
- Benutzer*innen müssen folgende Aktionen durchführen können:
  - Grill ein-/ausschalten
  - Wunschtemperatur setzen/ändern
  - Systemzustände visuell erkennen

## F-GUI5: Live-Anzeige
- Die GUI aktualisiert alle Anzeigen in Intervallen (z. B. alle 200–500 ms).
- Die Aktualisierung blockiert die GUI nicht (Tkinter `.after()`).

---

# Nicht-funktionale Requirements (GUI-bezogen)

## NF-GUI1: Übersichtlichkeit
- Die Benutzeroberfläche muss klar gegliedert und intuitiv verständlich sein.

## NF-GUI2: Responsives Verhalten
- GUI-Elemente passen sich bei Größenänderung des Fensters an.

## NF-GUI3: Fehlertoleranz
- Ungültige Benutzereingaben (z. B. außerhalb des Temperaturbereichs) müssen abgefangen werden.

---

# Architektur (Sprint 2)

## A1. Drei-Schicht-Struktur
- **Model** (fertig aus Sprint 1)  
- **Controller** (Teil von GrillController, Erweiterung für UI-Interaktionen)  
- **View (GUI)** – wird in Sprint 2 erstellt

## A2. GUI-Schicht als eigene Klasse
- Neue Klasse:
  - **`GrillGUI`**  
- Verantwortlichkeiten:
  - Aufbau des Tkinter-Fensters
  - Layout-Management (Frames, Grid)
  - visuelle Darstellung der Model-Daten
  - Weiterleitung von Benutzeraktionen an den Controller

## A3. Lose Kopplung
- Das GUI fragt nur über den **Controller** nach Daten ab.
- Keine direkte Änderung der Model-Schicht durch die GUI.

## A4. Ereignissteuerung
- Periodische Aktualisierung mit Tkinter:
  - **`root.after(interval, callback)`**
- Keine while-Schleifen → GUI bleibt reaktionsfähig.

---

# Design (Sprint 2)

## D1. Layoutstruktur
Voraussichtliche Struktur (Frames):

- **HeaderFrame**  
  - Titel des Systems

- **TemperatureFrame**  
  - Anzeige: aktuelle Temperatur  
  - Anzeige: Wunschtemperatur  
  - Buttons: + / – für Wunschtemperatur  

- **StatusFrame**  
  - Zieltemperaturstatus (*Erreicht / Nicht erreicht*)  
  - Resttemperaturstatus (*Grill heiß*)  

- **PowerFrame**  
  - Button: *An / Aus*  
  - Statusanzeige  

## D2. Zentrale Widgets
- **`Label`** für Temperaturanzeigen  
- **`Button`** für Interaktion  
- **`Frame`** zur Strukturierung  
- Optional: **`Canvas`** oder farbige Labels für Statusindikatoren  

## D3. GUI-Methoden
- **`update_display()`**  
  Aktualisiert alle Anzeigen, wird regelmäßig über `.after()` aufgerufen.

- **`increase_target_temperature()`**  
- **`decrease_target_temperature()`**  
- **`toggle_power()`**  
- **`refresh_status_indicators()`**

---

# Implementierung (Sprint 2)

## I1. Klasse GrillGUI
- Implementieren eines Tkinter-Fensters mit:
  - Temperaturanzeigen
  - Buttons
  - Statusanzeigen
  - Power-Toggle

## I2. GUI–Controller-Verbindung
- GrillGUI erhält eine Instanz von **`GrillController`**.
- Alle GUI-Ereignisse delegieren an Controller-Methoden.

## I3. Aktualisierungslogik
- Implementieren der Methode:
  - **`update_display()`**, Aufruf alle 200–500 ms
- Aktualisiert:
  - Temperaturen
  - An/Aus-Status
  - Zieltemperaturstatus
  - Restwärmestatus

## I4. Eingabevalidierung
- Nur gültige Temperaturwerte werden übernommen.
- Ungültige Werte lösen Popup oder Fehlermeldung in der GUI aus.

## I5. Keine Business-Logik in der GUI
- GUI darf keine Temperaturen berechnen.
- Validierungen und Statuslogik bleiben vollständig in der Model-Schicht.

# Vergleich Architektur & Design vs. Implementierung

In Sprint 2 wurde der **GUI-Entwurf** mit Tkinter als Zielvorbereitung umgesetzt. Verglichen wurden:
- Entwurfsziele (Layout, Komponenten, Schnittstellen)
- Architekturziele (Trennung Model – GUI, klare Zugriffspunkte)
- Implementierte Strukturen  
- Durchgeführte Tests

## Festgestellte Abweichungen

### **A1 – GUI-Komponentenstruktur musste erweitert werden**
**Geplant:**  
- Nur grundlegende GUI-Komponenten als Entwurf  
- Einfaches Layouting

**Implementiert:**  
- Erweiterte Struktur für Temperaturfelder  
- Dynamische Aktivierung/Deaktivierung von Buttons  
- Frühe Entscheidung für Grid-Layout

**Abweichung:**  
GUI-Komplexität wurde leicht erhöht, um Testbarkeit und Klarheit zu verbessern.

---

### **A2 – Schnittstellen zu Model-Modulen präziser umgesetzt**
**Geplant:**  
- Nutzung einfacher Getter/Setter

**Implementiert:**  
- Zusätzliche Validierungslogik direkt im GUI-Eingabefeld  
- Fehlerbehandlung über Messagebox

**Abweichung:**  
GUI übernimmt mehr Verantwortung für Validierung als ursprünglich geplant.

---

### **A3 – Statuslogik stärker in GUI integriert**
**Geplant:**  
- Statusanzeigen werden erst in Sprint 3 vollständig UI-basiert umgesetzt

**Implementiert:**  
- Anzeige aktualisiert sich bereits auf Temperaturänderungen  
- Start-Button abhängig vom Zieltemperatur-Status

**Abweichung:**  
Vorverlagerung von Anzeige-Logik von Sprint 3 → Sprint 2.

---

# Dokumentation der Abweichungen

Abweichungen wurden in den Design- und Testabschnitten markiert:
- GUI übernimmt nun zusätzliche Validierungsschritte  
- GUI enthält bereits fundamental logische Statusdarstellungen  
- Button-Zustandslogik wurde erweitert

Diese Punkte wurden zusätzlich in der [Tracability-Matrix2.md](../Traceability-Matrix2.md) ergänzt.

---

# Sicherstellung der Konsistenz aller Dokumente

Folgende Sprint-2-Dokumente wurden vollständig synchronisiert:
- **Design2.md**  
- **Implementierung2.md**  
- **Traceability-Matrix2.md**  
- **Test2.md**  
- Die Architekturabbildung inkl. PlantUML-Klassendiagramm  

Alle enthalten jetzt identische Klassennamen, identische GUI-Komponentenbezeichnungen und konsistente Schnittstellen.

---

# Erkenntnisse für Sprint 3 / spätere Änderungen

## **E1 – GUI benötigt klarere MVC/Model-View-Schnittstellen**
Die Interaktion zwischen GUI und Modell könnte modularer werden.  
Sprint 3 sollte daher:
- ein Controller-Modul einführen  
- Events statt direkter Funktionsaufrufe verwenden  

## **E2 – Temperatur-Updates sollten event-basiert erfolgen**
Bisher: GUI ruft Werte aktiv ab  
Geplant für Sprint 3: automatisches Update durch Timer/Callback

## **E3 – Statusanzeigen sollten in eigenes GUI-Widget ausgelagert werden**
Die Zustandsanzeige ist aktuell Teil der Hauptoberfläche.  
Später sinnvoll:
- eigenes Status-Panel für "Heating", "Target Reached", "Cooling Down"

## **E4 – Separation von Validierungslogik**
Derzeit existiert Validierung in Model **und** GUI.  
Sprint 3 sollte eine einheitliche Validierungsstrategie implementieren.


# Baseline

## Baseline Stand Sprint 2

### Code abgeschlossen für Sprint 2
- GUI-Prototyp erstellt (ohne vollständige Funktionalität)  
- Buttons, Labels, Frames und Eingabefelder gestaltet  
- Verbindung zu Temperature-Modellen strukturell vorbereitet  

### Tests bestanden
- Alle 6 Testfälle aus Sprint 2 erfolgreich  
- Keine kritischen Fehler  

### Architektur konsistent
- GUI-Schicht klar vom Models-Schicht getrennt  
- Controller-Logik für Sprint 3 vorgesehen

