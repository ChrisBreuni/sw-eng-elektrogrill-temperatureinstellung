# Design Sprint 2 – GUI

## Layoutstruktur
- **HeaderFrame**: Titel des Systems
- **TemperatureFrame**: Anzeige aktuelle Temperatur, Wunschtemperatur, Buttons + / –
- **StatusFrame**: Zieltemperaturstatus, Resttemperaturstatus
- **PowerFrame**: An-/Aus-Button, Statusanzeige

## Zentrale Widgets
- **Label**: Temperaturanzeigen
- **Button**: Benutzerinteraktion
- **Frame**: Strukturierung der GUI
- Optional: **Canvas** für Statusindikatoren

## GUI-Methoden
- **update_display()**: Aktualisiert alle Anzeigen regelmäßig
- **increase_target_temperature()**, **decrease_target_temperature()**
- **toggle_power()**
- **refresh_status_indicators()**

## Hinweise
- GUI bleibt lose gekoppelt an **GrillController**.
- Keine Berechnung oder Validierung in der GUI.
