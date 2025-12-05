# Sprint 1


__Zeitraum: 03.11.2025 - 30.11.2025__
## Planung

Im Rahmen des ersten Sprints sollen die folgenden Requirements implementiert werden:
- Req. F1.1: Wunschtemperaturanzeige
- Req. F1.2: Wunschtemperaturänderung
- Req. F2.1: Aktuelle Temperatur
Der Fokus hierbei liegt auf der Implementierung der absoluten Grundfunktionen, welche wichtig für
die weitere Entwicklung des Elektrogrills sind.

## Ziel des Sprints
1. Erstellung einer übersichtlichen Grundstruktur.
2. Evaluierung und finale Auswahl der geigneten Programmiersprache.
3. Definition der grundlegenden Anforderungen und Architektur für den Projektstart.

## Software-Architektur
### A1. Modularer Aufbau

- Trennung der Kernlogik in einzelne Python-Module (z. B. current_temperature.py, target_temperature.py, grill_controller.py).

- Jede Komponente übernimmt klar abgegrenzte Verantwortlichkeiten (Single Responsibility Principle).

### A2. Model-Schicht vorbereiten (MVC-Vorbereitung)

- Aufbau einer Model-Schicht für alle temperaturbezogenen Berechnungen und Validierungen.

- GUI-Schicht (Tkinter) wird im Sprint 1 nicht implementiert, aber durch klare Schnittstellen vorbereitet.

- Definierte Methoden, die später von der GUI aufgerufen werden können (z. B. set_target_temperature(), get_current_temperature()).

### A3. Temperature-Management-Kern

- Zentrale Klasse/Modul für die Verwaltung der aktuellen und gewünschten Temperatur.

- Implementierung von Validierungslogiken für Temperaturbereiche (50–500 °C, sowie 0 für „noch nicht gesetzt“ bei Zieltemperaturen).

- Definition von Statuszuständen: Heating, Target Reached, Cooling Down.

### A4. Power-State-Management

- Architektur für die An-/Ausfunktion vorbereiten.

- Separates Modul power_state.py, das den Betriebsstatus des Grills kapselt.

- Einheitliche Schnittstelle, durch die später GUI und Logik kommunizieren.

## Design
### Klare Klassen- und Methodensignaturen

- Entwurf der Klassen:

  - CurrentTemperature

  - TargetTemperature

  - GrillController

  - PowerState

- Wichtige öffentliche Methoden:

  - set_temperature(value)
  - get_temperature()
  - is_valid(value)
  - is_target_reached()
  - turn_on() / turn_off()

### Defensive Design

- Ungültige Temperaturwerte (<50 oder >500 °C) werden sofort abgefangen.
- Nutzung privater Hilfsmethoden wie:
  - _validate(value)

### Erweiterbarkeit

- Design so aufgebaut, dass die GUI mittels Tkinter später ohne größere Änderungen ergänzt werden kann.

- Klare Abgrenzung zwischen Logik (Model) und Benutzeroberfläche (View/Controller).

### Zustandsorientiertes Design

- Einführung einfacher Statuswerte:
  - ON
  - OFF
  - TARGET_REACHED 
  - COOLING_DOWN


## Implementierung
### Grundlegende Logik-Klassen

- Umsetzung der Grundlogik in diesen Klassen:
  - CurrentTemperature 
  - TargetTemperature
  - GrillController
  - PowerState

### Validierungslogik

- Implementieren der Temperaturbereiche:

  - gültig: 50–500 °C

  - Zieltemperatur zusätzlich: 0 = nicht gesetzt

- Ungültige Werte lösen ValueError aus.

### Statusbestimmung der Zieltemperatur

- Implementierung der Logik:
target_reached = current >= target

- Rückgabe als Boolean, später als UI-Anzeige nutzbar.

### Resttemperaturlogik

- Erkennen, ob der Grill ausgeschaltet, aber noch über 50 °C ist.

- Noch keine Anzeige, nur interne Methoden für die spätere GUI.

### Keine UI in Sprint 1

- Tkinter wird nicht implementiert.

- Keine grafischen Komponenten wie Buttons, Labels oder Displays.

- Fokus liegt ausschließlich auf der Kernlogik.

### Unit Tests
- Schreiben von Unit Tests für:
  - Temperaturvalidierung
  - Zieltemperaturstatus
  - Power-State-Logik
- Sicherstellen, dass alle Logikmodule zuverlässig funktionieren.
