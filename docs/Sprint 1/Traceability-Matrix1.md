# Traceability-Matrix Sprint 1 – Kernlogik

| Requirement ID | Requirement Beschreibung | Design-Element / Klasse | Implementierungsmethode | Unit Test / Testfall |
|----------------|-------------------------|------------------------|------------------------|--------------------|
| F1.1 | Wunschtemperaturanzeige | **TargetTemperature**, **GrillController** | `get_target_temperature()`, Labels in späterer GUI | Test, ob Zieltemperatur korrekt zurückgegeben wird |
| F1.2 | Änderung der Wunschtemperatur | **TargetTemperature**, **GrillController** | `set_target_temperature(value)`, `_validate(value)` | Test, ob Zieltemperatur korrekt gesetzt wird und Werte validiert werden |
| F2 | Aktuelle Temperatur | **CurrentTemperature**, **GrillController** | `get_current_temperature()` | Test, ob aktuelle Temperatur korrekt zurückgegeben wird |
| F3 | Zieltemperaturstatus | **GrillController** | `is_target_reached()` | Test, ob Zieltemperatur korrekt erkannt wird |
| F4 | An-/Aus-Funktion | **PowerState**, **GrillController** | `turn_on()`, `turn_off()`, `toggle_power()` | Test, ob PowerState korrekt geändert wird |
| F5 | Resttemperaturanzeige | **GrillController** | `is_rest_temperature()` | Test, ob Resttemperaturstatus korrekt erkannt wird |
| NF6.1 | Programmiersprache Python | Projektstruktur, Klassen | Verwendung von Python | - |
| NF6.2 | Tools & Packages (Tkinter) | - | Vorbereiten der GUI-Schnittstellen (`get_target_temperature()`, `get_current_temperature()`) | - |

---

### Hinweise
- **Requirement ID:** entspricht den Sprint 1 Requirements.  
- **Design-Element / Klasse:** welche Klassen oder Module für das Requirement relevant sind.  
- **Implementierungsmethode:** konkrete Methoden, die das Requirement erfüllen.  
- **Unit Test / Testfall:** mögliche Testfälle oder Testmethoden zur Verifikation.

