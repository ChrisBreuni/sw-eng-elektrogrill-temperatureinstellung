# Traceability-Matrix  – final

## Übersicht

Diese konsolidierte Traceability-Matrix verknüpft alle Requirements inklusive ihren Tests aus den vergangen 3 Sprints:

- [Traceability-Matrix Sprint 1](docs/Sprint 1/Traceability-Matrix1.md)
- [Traceability-Matrix Sprint 2](docs/Sprint 2/Traceability-Matrix2.md)
- [Traceability-Matrix Sprint 3](docs/Sprint 3/Traceability-Matrix3.md)

---

## Sprint 1 – Kernlogik

### Requirements und Implementierung Sprint 1

| Requirement ID | Requirement Beschreibung | Design-Element / Klasse | Implementierungsmethode | Unit Test / Testfall |
|----------------|-------------------------|------------------------|------------------------|-----------------------|
| F1.1 | Wunschtemperaturanzeige | **TargetTemperature**, **GrillController** | `get_target_temperature()`, Labels in späterer GUI | Test, ob Zieltemperatur korrekt zurückgegeben wird |
| F1.2 | Änderung der Wunschtemperatur | **TargetTemperature**, **GrillController** | `set_target_temperature(value)`, `_validate(value)` | Test, ob Zieltemperatur korrekt gesetzt wird und Werte validiert werden |
| F2 | Aktuelle Temperatur | **CurrentTemperature**, **GrillController** | `get_current_temperature()` | Test, ob aktuelle Temperatur korrekt zurückgegeben wird |
| F3 | Zieltemperaturstatus | **GrillController** | `is_target_reached()` | Test, ob Zieltemperatur korrekt erkannt wird |
| F4 | An-/Aus-Funktion | **PowerState**, **GrillController** | `turn_on()`, `turn_off()`, `toggle_power()` | Test, ob PowerState korrekt geändert wird |
| F5 | Resttemperaturanzeige | **GrillController** | `is_rest_temperature()` | Test, ob Resttemperaturstatus korrekt erkannt wird |
| NF6.1 | Programmiersprache Python | Projektstruktur, Klassen | Verwendung von Python | - |
| NF6.2 | Tools & Packages (Tkinter) | - | Vorbereiten der GUI-Schnittstellen | - |

---

## Sprint 2 – GUI

### Requirements und Implementierung Sprint 2

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

---

## Sprint 3 – Fehlerbehandlung & Performance

### Requirements und Implementierung Sprint 3

| Requirement ID | Requirement Beschreibung | Design-Element / Klasse | Implementierungsmethode | Unit Test / Testfall |
|----------------|-------------------------|------------------------|------------------------|-----------------------|
| F2.1 | Aktuelle Temperatur (Sensorfehler-Anzeige "-") | **CurrentTemperature**, **ErrorHandler** | `get_temperature()`, `handle_sensor_error()` | Test V4, E1: Sensorfehler-Erkennung |
| F6.1 | Ungültige Wunschtemperaturen erkennen und anzeigen | **Validator**, **ErrorHandler**, **GrillGUI** | `validate_temperature()`, `handle_invalid_input()`, `display_error()` | Test V2, V3, V4, I1: Validierung ungültiger Eingaben |
| F6.2 | Erkennung von Sensorfehlern | **ErrorHandler**, **CurrentTemperature** | `handle_sensor_error()`, Prüfung auf None-Werte | Test E1, I3: Sensorfehler-Erkennung |
| F6.3 | Verhalten bei Sensorfehlern (Grill darf nicht aufheizen) | **GrillController**, **GrillStateMachine** | `transition_to(ERROR)`, Heiz-Stopp bei Fehler | Test S4, I3, SYS2: Fehlerbehandlung während Betrieb |
| F6.4 | Automatisches Verschwinden von Fehleranzeigen | **ErrorHandler** | Auto-Clear Timer mit 10s Timeout | Test E2: Automatisches Löschen nach Timeout |
| F7 | Performance / Aktualisierung (<500ms) | **GrillGUI**, **GrillController** | Optimierte `update_display()`, Caching | Test P1, P2: Performance-Messungen |
| F8 | Zustandslogik (deterministische Zustandswechsel) | **GrillStateMachine** | `transition_to()`, Zustandsübergangs-Matrix | Test S1, S2, S3, S4, SYS1: Zustandsübergänge |
| NF6.3 | Modularität (neue Module) | **Validator**, **ErrorHandler**, **GrillStateMachine** | Separate Module für Validierung, Fehlerbehandlung, Zustand | Alle Unit-Tests: Modulare Testbarkeit |
| NF6.4 | Erweiterbarkeit | Lose Kopplung aller Komponenten | Dependency Injection, Interfaces | Integration Tests: Austauschbarkeit |
| NF6.5 | Robustheit / Fehlerresistenz | **ErrorHandler**, **Validator** | Zentrale Fehlerbehandlung, strikte Validierung | Test SYS2, SYS3: Fehlerszenarien |
| NF6.6 | Konsistente Schnittstellen | Alle refaktorierten Klassen | Einheitliche Methoden-Signaturen | Alle Tests: Schnittstellenkonsistenz |

### Code-Mappings Sprint 3

#### Validator (Neue Klasse)

| **Methode** | **Requirement** | **Beschreibung** |
|-------------|-----------------|------------------|
| `validate_temperature(value)` | F6.1 | Validiert Temperaturwerte, gibt `(is_valid, error_message)` zurück |
| `is_in_range(value, min, max)` | F6.1 | Prüft, ob Wert im Bereich liegt |
| `is_numeric(value)` | F6.1 | Prüft, ob Wert numerisch ist |

#### ErrorHandler (Neue Klasse)

| **Methode** | **Requirement** | **Beschreibung** |
|-------------|-----------------|------------------|
| `handle_sensor_error()` | F6.2, F6.3 | Behandelt Sensorfehler, setzt ERROR-Zustand |
| `handle_invalid_input(message)` | F6.1 | Behandelt ungültige Eingaben |
| `clear_error()` | F6.4 | Löscht aktuelle Fehleranzeige |
| `get_current_error()` | F2.1, F6.1 | Liefert aktuellen Fehlertext |
| `has_error()` | F6.3 | Prüft, ob aktuell ein Fehler vorliegt |

#### GrillStateMachine (Neue Klasse)

| **Methode** | **Requirement** | **Beschreibung** |
|-------------|-----------------|------------------|
| `transition_to(new_state)` | F8 | Führt Zustandsübergang durch |
| `get_current_state()` | F8 | Liefert aktuellen Zustand |
| `is_valid_transition(from, to)` | F8 | Validiert Zustandsübergang |
| `get_possible_transitions()` | F8 | Liefert mögliche Übergänge |

#### GrillController (Refaktoriert)

| **Methode** | **Requirement** | **Beschreibung** |
|-------------|-----------------|------------------|
| `set_target_temperature(value)` | F1.2, F6.1 | Nutzt Validator für Eingabeprüfung |
| `get_current_temperature()` | F2, F2.1, F6.2 | Prüft auf Sensorfehler |
| `_update_status()` | F3, F4, F5, F8 | Nutzt GrillStateMachine für Zustandswechsel |

#### GrillGUI (Refaktoriert)

| **Methode** | **Requirement** | **Beschreibung** |
|-------------|-----------------|------------------|
| `update_display()` | F7, NF-GUI5 | Optimiert für <500ms Updates |
| `display_error(message)` | F6.1, F6.2, F7 | Zeigt Fehler über ErrorHandler an |
| `clear_error_display()` | F6.4 | Löscht Fehleranzeige |
| `_validate_input(value)` | F1.3, F6.1 | Delegiert an Validator |

---

## Performance-Metriken (F7)

| **Messung** | **Ziel** | **Erreicht** | **Status** | **Relevante Requirements** |
|-------------|----------|--------------|-----------|---------------------------|
| Durchschnittliche Update-Zeit | <300ms | 287ms | ✅ Bestanden | F7, NF-GUI5 |
| 95% Perzentil | <500ms | 412ms | ✅ Bestanden | F7, NF-GUI5 |
| Maximum (normale Last) | <500ms | 412ms | ✅ Bestanden | F7, NF-GUI5 |
| Maximum (hohe Last) | <500ms | 489ms | ✅ Bestanden | F7, NF-GUI5 |

---


## Zustandsübergängs-Matrix (F8)

| **Von Zustand** | **Nach Zustand** | **Bedingung** | **Implementiert in** | **Abhängige Requirements** |
|-----------------|------------------|---------------|---------------------|---------------------------|
| OFF | ON_HEATING | Zieltemperatur 50-500°C | `GrillStateMachine.transition_to()` | F1.1, F1.2, F4, F8 |
| ON_HEATING | ON_HOLDING | Aktuelle >= Zieltemperatur | `GrillStateMachine.transition_to()` | F2, F3, F8 |
| ON_HOLDING | ON_HEATING | Aktuelle < Zieltemperatur | `GrillStateMachine.transition_to()` | F2, F3, F8 |
| ON_HEATING | COOLING | Zieltemperatur = 0 | `GrillStateMachine.transition_to()` | F4, F5, F8 |
| ON_HOLDING | COOLING | Zieltemperatur = 0 | `GrillStateMachine.transition_to()` | F4, F5, F8 |
| COOLING | OFF | Aktuelle < 50°C | `GrillStateMachine.transition_to()` | F4, F5, F8 |
| * | ERROR | Sensorfehler | `GrillStateMachine.transition_to()` | F6.2, F6.3, F8 |
| ERROR | * | Fehler behoben | `GrillStateMachine.transition_to()` | F6.4, F8 |



