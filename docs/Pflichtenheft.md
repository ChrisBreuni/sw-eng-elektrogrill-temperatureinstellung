# Pflichtenheft
## F1. Wunschtemperatur
## F1.1 Wunschtemperaturanzeige
- Die eingestellte Wunschtemperatur wird auf einem Panel angezeigt und kann die Werte 0 °C oder 50 bis 
500 °C annehmen.

## F1.2 Wunschtemperaturänderung
- Die Wunschtemperatur kann geändert werden und die Werte 0 °C oder 50 bis 500 °C annehmen.
- Durch die Änderung der Wunschtemperatur wird das Panel der Wunschtemperatur in Echtzeit
innerhalb von maximal 500 ms aktualisiert.
- Bei einer Einstellung von weniger als 50 °C wird der Grill nicht eingeschaltet.

## F2.1 Aktuelle Temperatur
- Die aktuelle Temperatur des Elektrogrills wird mir eindeutig auf einem extra Panel angezeigt.
- Die Anzeige der aktuelle Temperatur kann Werte im Messbereich von 50 bis 500 °C annehmen.
- Ist die aktuelle Temperatur unterhalb des Messbereichs, so zeigt das Panel einen Trennstrich "-" an.

## F3. Zieltemperaturstatus
- Ein Lämpchen leuchtet, solange die aktuelle Temperatur des Elektrogrills
die Wunschtemperatur noch nicht erreicht hat.
- Das Lämpchen erlischt, wenn die aktuelle Temperatur die Wunschtemperatur erreicht hat.

## F4. An-Aus-Funktion
- Der Elektrogrill ist angeschaltet, wenn die Wunschtemperatur im Messbereich von 50 bis 500 °C liegt
und ist ausgeschaltet, wenn sich die Wunschtemperatur darunter befindet.
- Ist der Elektrogrill angeschaltet, so zeigt eine Anzeige "On" an.
- Ist der Elektrogrill ausgeschaltet, so zeigt die selbe Anzeige "Off" an und erlischt nach 10 Sekunden,
wenn nicht der Resttemperaturmodus einsetzt.

## F5. Resttemperaturmodus
- Wenn der Grill nach dem Ausschalten noch eine aktuelle Temperatur im Messbereich von 50 bis 500 °C hat,
geht die Anzeige der An-Aus-Funktion auf "H", um vor noch bestehender Hitze zu warnen.
- Sinkt die aktuelle Temperatur auf eine Temperatur unterhalb des genannten Messbereiches, so schaltet
sich die Anzeige nach 10 Sekunden ab.

## F6. Fehlerbehandlung
## F6.1 Ungültige Wunschtemperaturen 
- invalide Wunschtemperaturen (z. B. 10 °C, 600 °C, Textwerte) werden blockiert und als „Err“ angezeigt.

## F6.2 Erkennung von Sensonfehlern
- Sensorfehler werden erkannt und als „Err“ auf dem Panel der aktuellen Temperatur ausgegeben.

## F6.3 Verhalten bei Sensorfehlern
- Bei Sensorfehlern darf der Grill nicht aufheizen.

## F6.4 Verhalten der Fehleranzeigen
- Fehleranzeigen müssen automatisch verschwinden, sobald die Eingabe oder der Sensor wieder gültig ist.

## F7. Performance / Aktualisierung

- Alle Statusanzeigen (Temperatur, Wunschtemperatur, Betriebsmodus, Heißstatus) müssen innerhalb von 500 ms nach relevanter Änderung aktualisiert werden.
- Die Temperaturabfrage erfolgt mindestens 2× pro Sekunde.

## F8. Zustandslogik
Zur Vermeidung von Inkonsistenzen:
- Der Grill kann sich nur in genau einem der folgenden Zustände befinden:
  - Off
  - On / Heating
  - On / Holding Temperature
  - Cooling (Hot / H)
- Zustandswechsel erfolgen deterministisch nach folgenden Regeln:
  - Wunschtemperatur 0 → Off
  - Wunschtemperatur 50–500 → On
  - Aktuelle Temperatur < Wunschtemperatur → Heating (Lämpchen an)
  - Aktuelle Temperatur >= Wunschtemperatur → Holding (Lämpchen aus)
  - Off + aktuelle Temperatur >= 50 → Cooling (H)
  - Off + aktuelle Temperatur < 50 → Anzeige erlischt nach 10s