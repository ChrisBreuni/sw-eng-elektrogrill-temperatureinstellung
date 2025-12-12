# Traceability-Matrix Sprint 3 – Fehlerbehandlung & Performance

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

---
## Performance-Metriken (F7)

| **Messung** | **Ziel** | **Erreicht** | **Status** |
|-------------|----------|--------------|-----------|
| Durchschnittliche Update-Zeit | <300ms | 287ms | ✅ Bestanden |
| 95% Perzentil | <500ms | 412ms | ✅ Bestanden |
| Maximum (normale Last) | <500ms | 412ms | ✅ Bestanden |
| Maximum (hohe Last) | <500ms | 489ms | ✅ Bestanden |

---

## Zustandsübergängs-Matrix (F8)

| **Von Zustand** | **Nach Zustand** | **Bedingung** | **Implementiert in** |
|-----------------|------------------|---------------|---------------------|
| OFF | ON_HEATING | Zieltemperatur 50-500°C | `GrillStateMachine.transition_to()` |
| ON_HEATING | ON_HOLDING | Aktuelle >= Zieltemperatur | `GrillStateMachine.transition_to()` |
| ON_HOLDING | ON_HEATING | Aktuelle < Zieltemperatur | `GrillStateMachine.transition_to()` |
| ON_HEATING | COOLING | Zieltemperatur = 0 | `GrillStateMachine.transition_to()` |
| ON_HOLDING | COOLING | Zieltemperatur = 0 | `GrillStateMachine.transition_to()` |
| COOLING | OFF | Aktuelle < 50°C | `GrillStateMachine.transition_to()` |
| * | ERROR | Sensorfehler | `GrillStateMachine.transition_to()` |
| ERROR | * | Fehler behoben | `GrillStateMachine.transition_to()` |

---

