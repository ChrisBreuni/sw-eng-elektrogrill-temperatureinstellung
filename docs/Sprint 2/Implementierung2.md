# Implementierung Sprint 2 – GUI

## Klasse GrillGUI
- Aufbau eines Tkinter-Fensters
- Frames: TemperatureFrame, StatusFrame, PowerFrame
- Widgets: Labels, Buttons, optional Canvas

## GUI–Controller-Verbindung
- Instanz von **GrillController** übergeben
- GUI-Ereignisse delegieren an Controller-Methoden

## Aktualisierungslogik
- **update_display()** wird periodisch mit `root.after()` aufgerufen
- Aktualisiert:
  - aktuelle Temperatur
  - Zieltemperatur
  - An/Aus-Status
  - Ziel- und Resttemperaturstatus

## Eingabevalidierung
- Buttons / Eingaben validieren Werte
- Ungültige Eingaben lösen Fehlermeldung oder Popup aus

## Keine Business-Logik in GUI
- Berechnungen und Statuslogik bleiben in Model/Controller
