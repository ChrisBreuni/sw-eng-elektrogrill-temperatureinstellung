# Test Sprint 2 – GUI

## 1. Ziel der Tests

Das Ziel der Tests in Sprint 2 ist die Verifikation und Validierung der GUI-Komponenten des Elektrogrills hinsichtlich Benutzerfreundlichkeit, korrekter Interaktion mit der Kernlogik und robuster Fehlerbehandlung bei Eingaben. Die Tests stellen sicher, dass:

- Die GUI alle Temperaturwerte korrekt anzeigt
- Benutzerinteraktionen (Buttons, Eingabefelder) korrekt verarbeitet werden
- Ungültige Eingaben abgefangen und dem Benutzer angezeigt werden
- Die GUI mit der Kernlogik konsistent kommuniziert
- Alle Statusanzeigen (Zieltemperatur erreicht, Restwärme) korrekt aktualisiert werden

---

## 2. Testarten und Abdeckung

### 2.1 Unit-Tests (GUI-Komponenten)

Ziel: Prüfung der GUI-Logik auf Komponentenebene, z.B. Validierung von Eingaben, Aktivierung/Deaktivierung von Buttons, Aktualisierung von Labels.

Beispielsweise getestet:
- Validierung der Eingabe für Wunschtemperatur im GUI
- Aktualisierung des Temperaturanzeige-Labels
- Aktivieren/Deaktivieren des Start-Buttons

### 2.2 Integrationstests (GUI ↔ Kernlogik)

Ziel: Sicherstellen, dass GUI und Kernlogik korrekt zusammenarbeiten, insbesondere:
- GUI setzt TargetTemperature → Controller übernimmt Wert
- Start-Button löst Start der Heizlogik aus
- GUI aktualisiert Anzeige nach neuem Temperaturwert

---

## 3. Teststrategie

Die Teststrategie kombiniert **automatisierte Unit-Tests** mit **manuellen Integrationstests**, um folgende Ziele zu erreichen:

- **Automatisierte Tests** für GUI-Validierungslogik
- **Manuelle Tests** für Usability-Aspekte und visuelle Darstellung
- **Iterative Tests** nach jeder Änderung an GUI-Komponenten
- **Regressionstests** nach Anpassungen an der Schnittstelle zwischen GUI und Kernlogik

### Testumgebung:

- Python 3.x mit tkinter
- Mock-Objekte für Controller-Simulation
- Simulierte Benutzerinteraktionen für GUI-Tests
- Logging für Debugging und Nachvollziehbarkeit

---

## 4. Testumfang

### In-Scope:

- GUI-Validierungslogik für Temperatureingaben
- Anzeige von aktueller und Zieltemperatur
- Button-Interaktionen (Start, Stop, +, –)
- Fehleranzeigen bei ungültigen Eingaben
- Statusanzeigen (Zieltemperatur erreicht, Restwärme)

### Out-of-Scope:

- Detaillierte Fehlerbehandlung mit Auto-Clear (erst in Sprint 3)
- Performance-Tests (<500ms) (erst in Sprint 3)
- Zustandsautomat-Verfeinerung (erst in Sprint 3)

---

## Definition Testfälle inkl. betroffener Requirements

Alle Testfälle für Sprint 2 sind dokumentiert in:

[Testfälle](../referenziert/Tests/Testfaelle.md) (Sektion: Sprint 2 – GUI)

---

## Dokumentation der Ergebnisse

Alle Testergebnisse für Sprint 2 sind dokumentiert in:

[Testergebnisse](../referenziert/Tests/Testergebnisse.md) (Sektion: Sprint 2 – GUI)

---

## Zusammenfassung Sprint 2 Tests

Die Tests in Sprint 2 konzentrieren sich auf:
- **GUI-Logik**: Alle Validierungen und Button-Interaktionen funktionieren korrekt
- **Validierung von Benutzereingaben**: Ungültige Werte werden abgefangen
- **Interaktion zwischen GUI und Backend-Modulen**: Schnittstellen funktionieren fehlerfrei
- **Konsistentes Temperatur-Update**: Anzeigen werden korrekt aktualisiert

Alle kritischen Testfälle wurden erfolgreich abgeschlossen.
