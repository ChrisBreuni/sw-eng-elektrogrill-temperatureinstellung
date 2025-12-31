# Test Sprint 1 – Kernlogik

## 1. Ziel der Tests

Das Ziel der Tests in Sprint 1 ist die Verifikation und Validierung der Kernlogik des Elektrogrills hinsichtlich funktionaler Korrektheit, robuster Temperaturverarbeitung und sauber definierter Schnittstellen für spätere Sprints. Die Tests stellen sicher, dass:

- Temperaturwerte innerhalb des spezifierten Bereichs (50–500 °C, sowie 0 als „nicht gesetzt") korrekt verarbeitet werden.
- Die Wunschtemperatur korrekt gesetzt, gelesen und validiert wird.
- Die aktuelle Temperatur korrekt gelesen und zur weiteren Logik bereitgestellt wird.
- Der Grillzustand (ein/aus, Zieltemperatur erreicht, Resthitze) konsistent aus Kernlogik abgeleitet wird.

---

## 2. Testarten und Abdeckung

### 2.1 Unit-Tests

Ziel: Prüfung der kleinstmöglichen Testeinheiten (z. B. Methoden in `CurrentTemperature`, `TargetTemperature`, `GrillController`, `PowerState`), um fehlerhafte Logik frühzeitig zu erkennen.

Beispielsweise getestet:
- Temperaturvalidierung in `TargetTemperature` (gültige/ungültige Werte, Bereich 50–500 °C, Sonderfall 0)
- Berechnung und Rückgabe der aktuellen Temperatur in `CurrentTemperature`
- Bestimmung, ob die Zieltemperatur erreicht ist (`is_target_reached()` im `GrillController`)
- Power-State-Logik (ein/aus) im Modul `PowerState`

### 2.2 Integrationstests (Modellschicht)

Ziel: Sicherstellen, dass die einzelnen Logik-Klassen korrekt zusammenspielen, insbesondere:
- Zusammenspiel von `CurrentTemperature` und `TargetTemperature` im `GrillController` zur Berechnung des Zieltemperaturstatus
- Korrekte Ansteuerung des `PowerState` durch den `GrillController` in Abhängigkeit der Wunschtemperatur
- Konsistentes Verhalten der Resttemperaturlogik (Grill aus, aber Temperatur > 50 °C)

### 2.3 Black-Box/Systemtests (Kernlogik ohne GUI)

Ziel: Prüfung des sichtbaren Systemverhaltens auf Ebene der öffentlichen API der Kernlogik (ohne GUI), um sicherzustellen, dass die Anforderungen aus Lasten- und Pflichtenheft erfüllt werden.

---

## 3. Teststrategie

Die Teststrategie kombiniert **automatisierte Unit-Tests** mit **manuellen Integrationstests**, um folgende Ziele zu erreichen:

- **Automatisierte Tests** für alle testbaren Codeeinheiten (insbesondere `TargetTemperature`, `CurrentTemperature`, `GrillController`, `PowerState`)
- **Manuelle Tests** für Integrations- und Systemtests zur Validierung des Gesamtverhaltens
- **Iterative Tests** nach jeder Änderung an der Kernlogik
- **Regressionstests** nach Anpassungen an Validierungslogik oder Statusbestimmung

### Testumgebung:

- Python 3.x mit unittest oder pytest
- Simulierte Temperaturwerte für Systemtests
- Mock-Objekte für isolierte Unit-Tests
- Logging für Debugging und Nachvollziehbarkeit

---

## 4. Testumfang

### In-Scope:

- Validierung von Temperaturwerten (Bereich 50–500 °C, Sonderfall 0)
- Berechnung des Zieltemperaturstatus
- Power-State-Management (ein/aus)
- Resttemperaturlogik (Grill aus, aber noch heiß)
- Öffentliche Schnittstellen aller Kernklassen

### Out-of-Scope:

- GUI-Komponenten (erst in Sprint 2)
- Benutzerinteraktionen (erst in Sprint 2)
- Performance-Tests (erst in Sprint 3)
- Fehlerbehandlung mit Fehlerdialogen (erst in Sprint 3)

---

## Definition Testfälle inkl. betroffener Requirements

Alle Testfälle für Sprint 1 sind dokumentiert in:

[Testfälle](../referenziert/Tests/Testfaelle.md) (Sektion: Sprint 1 – Kernlogik)

---

## Dokumentation der Ergebnisse

Alle Testergebnisse für Sprint 1 sind dokumentiert in:

[Testergebnisse](../referenziert/Tests/Testergebnisse.md) (Sektion: Sprint 1 – Kernlogik)

---

## Zusammenfassung Sprint 1 Tests

Die Tests in Sprint 1 konzentrieren sich auf:
- **Kernlogik**: Alle Basisklassen wurden erfolgreich getestet
- **Validierung**: Temperaturbereichsprüfung funktioniert korrekt
- **Statusbestimmung**: Zieltemperaturerkennung und Resttemperaturlogik arbeiten fehlerfrei
- **Schnittstellen**: Alle öffentlichen Methoden sind konsistent und gut testbar

Alle kritischen Testfälle wurden erfolgreich abgeschlossen.
