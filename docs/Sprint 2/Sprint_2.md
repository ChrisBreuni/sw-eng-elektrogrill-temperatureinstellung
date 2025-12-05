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
