# Traceability-Matrix Sprint 2 – GUI

| Requirement ID | Requirement Beschreibung | Design-Element / Klasse | Implementierungsmethode | Unit Test / Testfall |
|----------------|-------------------------|------------------------|------------------------|--------------------|
| F-GUI1 | Strukturierte Darstellung der Temperaturen (aktuell, Wunsch, Zielstatus) | **GrillGUI**, **TemperatureFrame**, Labels | `update_display()`, Labels aktualisieren | Test, ob Labels die richtigen Werte anzeigen |
| F-GUI2 | Änderung der Wunschtemperatur über Buttons oder Eingabefeld | **GrillGUI**, Buttons (+ / –), Eingabefeld | `increase_target_temperature()`, `decrease_target_temperature()`, `set_target_temperature()` | Test, ob Zieltemperatur korrekt verändert wird und validiert wird |
| F-GUI3 | Anzeige des Grillstatus (An/Aus, Resttemperatur) | **GrillGUI**, **PowerFrame**, **StatusFrame**, Labels | `toggle_power()`, `refresh_status_indicators()` | Test, ob An/Aus-Status korrekt angezeigt wird, Restwärme korrekt erkannt |
| F-GUI4 | Nutzerinteraktionen (Buttons, Toggle, Eingaben) | **GrillGUI**, Buttons, Event-Handler | Event-Handler Methoden für Buttons | Test der Button-Events, Simulation von Klicks |
| F-GUI5 | Live-Anzeige / regelmäßige Aktualisierung | **GrillGUI**, `update_display()` mit `root.after()` | `update_display()` wird periodisch aufgerufen | Test, dass GUI nach Interval korrekt aktualisiert wird |
| NF-GUI1 | Übersichtlichkeit / Layout | **GrillGUI**, Frames, Grid Layout | `build_layout()` | Visuelle Inspektion / Layout-Test |
| NF-GUI2 | Responsives Verhalten | **GrillGUI**, Grid / Pack Layout | Layout so gesetzt, dass Widgets skalieren | Fenstergröße ändern, prüfen ob GUI korrekt skaliert |
| NF-GUI3 | Fehlertoleranz bei Eingaben | **GrillGUI**, Input-Validation | Validierung in `increase_target_temperature()`, `decrease_target_temperature()` | Testen von Eingaben außerhalb 50–500°C, Fehlermeldung vorhanden |

---

### Hinweise
- **Requirement ID:** entspricht den Sprint 2 Requirements.  
- **Design-Element / Klasse:** welche Klassen, Frames oder Widgets für das Requirement relevant sind.  
- **Implementierungsmethode:** konkrete Methoden oder Event-Handler, die das Requirement erfüllen.  
- **Unit Test / Testfall:** mögliche Testfälle oder Testmethoden zur Verifikation.

