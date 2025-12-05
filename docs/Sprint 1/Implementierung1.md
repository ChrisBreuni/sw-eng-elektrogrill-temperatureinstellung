# Implementierung Sprint 1 – Kernlogik

## Grundlegende Logik-Klassen
- **CurrentTemperature**
- **TargetTemperature**
- **GrillController**
- **PowerState**

## Validierungslogik
- Temperaturbereiche: **50–500 °C**
- Zieltemperatur zusätzlich: **0 = nicht gesetzt**
- Ungültige Werte lösen **ValueError** aus.

## Statusbestimmung Zieltemperatur
- **target_reached = current >= target**
- Rückgabe als **Boolean**

## Resttemperaturlogik
- Prüft, ob Grill aus ist, aber noch über 50 °C
- Interne Methoden für spätere GUI

## Keine UI
- Tkinter wird nicht implementiert
- Fokus auf Kernlogik

## Unit Tests
- Testen von:
  - Temperaturvalidierung
  - Zieltemperaturstatus
  - Power-State-Logik
