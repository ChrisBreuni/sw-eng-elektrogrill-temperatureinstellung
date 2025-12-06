# 1. Funktionale Requirements
## F1.1 Wunschtemperaturanzeige
- Die gewünschte Temperatur des Elektrogrills wird angezeigt und befindet sich in einem Messbereich von 50 bis 500 °C.
- Es sollte dem Benutzer klar sein, auf welcher Anzeige die Wunschtemperatur zu sehen ist.

## F1.2 Wunschtemperaturänderung
- Die Wunschtemperatur kann im Messbereich von 50 bis 500 °C geändert werden.
- Die Eingabe ungültiger Werte (z. B. Zahlen außerhalb des Bereichs, leere Felder, Textwerte) muss abgefangen werden.
- Bei ungültigen Eingaben wird die GUI eine Fehlermeldung anzeigen.

## F1.3 Validierung der Eingabewerte
- Die GUI prüft, ob der Benutzer gültige Werte eingibt.
- Ungültige Werte dürfen den Systemzustand nicht verändern.
- Fehlermeldungen müssen eindeutig und verständlich sein.

## F2 Aktuelle Temperatur
- Die aktuelle Temperatur des Elektrogrills wird angezeigt und befindet sich im Messbereich von 50 bis 500 °C.
- Es sollte dem Benutzer klar sein, durch welches Element diese Temperatur dargestellt wird.
- Die Anzeige soll automatisch aktualisiert werden.

## F3 Zieltemperaturstatus
- Der Elektrogrill hat eine Anzeige, die dem Benutzer zeigt, ob die Zieltemperatur erreicht wurde.
- Die Anzeige des Zieltemperaturstatus soll leicht verständlich sein.
- Der Status soll automatisch aktualisiert werden, sobald sich die aktuelle Temperatur ändert.

## F4 An-/Aus-Funktion
- Der Elektrogrill besitzt eine Funktion zum Ein- und Ausschalten.
- Der Benutzer sieht eindeutig, ob der Grill an- oder ausgeschaltet ist.
- Beim Ausschalten wird die Resttemperatur weiterhin überwacht.

## F5 Resttemperaturanzeige
- Wenn der Grill ausgeschaltet ist, zeigt das Gerät an, dass es noch nicht vollständig abgekühlt ist.
- Die Anzeige verschwindet, sobald die Temperatur unter 50 °C fällt.

## F6 GUI-Interaktion
- Das Interface basiert auf dem Python-Paket tkinter.
- Die GUI muss mindestens folgende Elemente enthalten:
  - Eingabefeld für Wunschtemperatur
  - Anzeige der aktuellen Temperatur
  - Anzeige der Zieltemperatur
  - Anzeige des Status
  - Start-/Stop-/Power-Schaltflächen
- Buttons werden automatisch aktiviert/deaktiviert, abhängig vom Systemzustand.

## F7 Fehleranzeigen im GUI
- Die GUI zeigt Fehlermeldungen mittels Dialogen oder sichtbaren Markierungen an.
- Fehleranzeigen müssen eindeutig sein, z. B.:
  - „Ungültiger Temperaturwert“
  - „Bitte eine Zahl eingeben“

# 2. Nicht-funktionale Requirements
## NF6.1 Programmiersprache
- Die Programmiersprache Python wird verwendet.

## NF6.2 Tools & Packages
- Die Benutzeroberfläche wird mit tkinter realisiert.

## NF6.3 Modularität
- Die Software muss in logisch getrennte Module gegliedert sein:
  - current_temperature.py
  - target_temperature.py
  - power_state.py
  - grill_controller.py
  - gui_main.py (ab Sprint 2)

## NF6.4 Erweiterbarkeit
- Die Architektur muss erweiterbar sein, sodass zukünftige Sprints (z. B. Sprint 3) problemlos zusätzliche UI-Elemente oder Features integrieren können.

## NF6.5 Robustheit / Fehlerresistenz
- Das System darf bei ungültigen Nutzereingaben nicht abstürzen.
- Fehler müssen abgefangen und kommuniziert werden.

## NF6.6 Konsistente Schnittstellen

- Die GUI kommuniziert ausschließlich über definierte Methoden mit der Logik, z. B.:
  - set_target_temperature(value)
  - get_current_temperature()
  - turn_on() / turn_off()

# Lastenheft
[Lastenheft](Lastenheft.md)

# Pflichtenheft
[Pflichtenheft](Pflichtenheft.md)