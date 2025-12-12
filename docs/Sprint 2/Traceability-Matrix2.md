# Traceability-Matrix Sprint 2 – GUI

## Übersicht

Diese Traceability-Matrix verknüpft alle Requirements von Sprint 2 mit ihren Design-Elementen, Implementierungsmethoden und Tests.

---

## Requirements und Implementierung Sprint 2

| Requirement ID | Requirement Beschreibung | Design-Element / Klasse | Implementierungsmethode | Unit Test / Testfall |
|----------------|-------------------------|------------------------|------------------------|-----------------------|
| F1.3 | Validierung der Eingabewerte | **GrillGUI** | Eingabevalidierung in `increase_target_temperature()`, `decrease_target_temperature()` | Test M1: Validierung der Eingabe für Wunschtemperatur |
| F6 | GUI-Interaktion | **GrillGUI** | Tkinter-Fenster mit Frames, Buttons, Labels | Test M2, M3: Temperaturanzeige-Update, Button-Aktivierung |
| F7 | Fehleranzeigen im GUI | **GrillGUI** | Messagebox oder visuelle Markierungen für Fehler | Test I1, I2: Fehlertoleranz und -anzeige |
| NF6.2 | Tools & Packages (Tkinter) | **GrillGUI** | Implementierung mit tkinter | Test: GUI startet ohne Fehler |
| NF6.3 | Modularität (gui_main.py) | **GrillGUI** | Separate Klasse `GrillGUI` in eigener Datei | Test: Modulare Struktur verifikativ |
| NF6.4 | Erweiterbarkeit | **GrillGUI**, **GrillController** | Klare Schnittstellen zwischen GUI und Controller | Integration Tests: Austauschbarkeit |
| NF6.5 | Robustheit / Fehlerresistenz | **GrillGUI**, **GrillController** | Fehlerbehandlung für ungültige Eingaben | Test M1: Ungültige Eingaben werden abgefangen |
| NF6.6 | Konsistente Schnittstellen | Alle Klassen | Einheitliche Methoden-Signaturen | Test: Schnittstellenkonsistenz |

---

## Detaillierte Requirements Sprint 2

| Requirement ID | Requirement Beschreibung | Design-Element / Klasse | Implementierungsmethode | Unit Test / Testfall |
|----------------|-------------------------|------------------------|------------------------|-----------------------|
| F-GUI1 | Strukturierte Darstellung der Temperaturen (aktuell, Wunsch, Zielstatus) | **GrillGUI**, **TemperatureFrame**, Labels | `update_display()`, Labels aktualisieren | Test M2: Labels zeigen richtige Werte |
| F-GUI2 | Änderung der Wunschtemperatur über Buttons oder Eingabefeld | **GrillGUI**, Buttons (+ / –), Eingabefeld | `increase_target_temperature()`, `decrease_target_temperature()`, `set_target_temperature()` | Test M1, I1: Zieltemperatur verändert sich korrekt |
| F-GUI3 | Anzeige des Grillstatus (An/Aus, Resttemperatur) | **GrillGUI**, **PowerFrame**, **StatusFrame**, Labels | `toggle_power()`, `refresh_status_indicators()` | Test M3, I2: An/Aus-Status und Restwärme korrekt |
| F-GUI4 | Nutzerinteraktionen (Buttons, Toggle, Eingaben) | **GrillGUI**, Buttons, Event-Handler | Event-Handler Methoden für Buttons | Test: Button-Events funktionieren |
| F-GUI5 | Live-Anzeige / regelmäßige Aktualisierung | **GrillGUI**, `update_display()` mit `root.after()` | `update_display()` wird periodisch aufgerufen | Test I3: GUI aktualisiert nach neuem Temperaturwert |
| NF-GUI1 | Übersichtlichkeit / Layout | **GrillGUI**, Frames, Grid Layout | `setup_gui()` | Visuelle Inspektion / Layout-Test |
| NF-GUI2 | Responsives Verhalten | **GrillGUI**, Grid / Pack Layout | Layout so gesetzt, dass Widgets skalieren | Fenstergröße ändern, prüfen ob GUI skaliert |
| NF-GUI3 | Fehlertoleranz bei Eingaben | **GrillGUI**, Input-Validation | Validierung in Input-Methoden | Test M1: Eingaben außerhalb 50–500°C, Fehlermeldung |
