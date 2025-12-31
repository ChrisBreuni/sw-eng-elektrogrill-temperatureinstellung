# Testergebnisse – Elektrogrill Temperatursteuerung

## Sprint 1 – Kernlogik

### Unit-Tests (UT)

| Test-ID  | Testname                                        | Requirement  | Status       | Bemerkungen                           |
|----------|-------------------------------------------------|--------------|--------------|---------------------------------------|
| UT1      | Validierung gültiger Zieltemperatur             | F1.2         | ✅ Bestanden  | Wert 200°C korrekt akzeptiert         |
| UT2      | Validierung ungültige Zieltemp. (zu niedrig)    | F1.2         | ✅ Bestanden  | ValueError korrekt geworfen bei 30°C  |
| UT3      | Validierung ungültige Zieltemp. (zu hoch)       | F1.2         | ✅ Bestanden  | ValueError korrekt geworfen bei 600°C |
| UT4      | Validierung Sonderfall Zieltemperatur = 0       | F1.2, F4     | ✅ Bestanden  | Wert 0°C für "Grill aus" akzeptiert   |
| UT5      | Aktuelle Temperatur abrufen                     | F2           | ✅ Bestanden  | Rückgabe 150°C korrekt                |
| UT6      | Zieltemperatur erreicht (aktuelle >= Ziel)      | F3           | ✅ Bestanden  | Status True bei 200°C >= 180°C        |
| UT7      | Zieltemperatur nicht erreicht (aktuelle < Ziel) | F3           | ✅ Bestanden  | Status False bei 120°C < 180°C        |
| UT8      | Power State einschalten                         | F4           | ✅ Bestanden  | Zustand wechselt korrekt zu ON        |
| UT9      | Power State ausschalten                         | F4           | ✅ Bestanden  | Zustand wechselt korrekt zu OFF       |
| UT10     | Resttemperatur erkennen                         | F5           | ✅ Bestanden  | Status True bei Grill aus + 120°C     |

**Zusammenfassung Unit-Tests Sprint 1:** 10/10 bestanden (100%)

---

### Integrationstests (IT)

| Test-ID   | Testname                                   | Requirement   | Status     | Bemerkungen                         |
|-----------|--------------------------------------------|---------------|------------|-------------------------------------|
| IT1       | Controller setzt Zieltemperatur korrekt    | F1.2          | ✅ Bestanden| Wert 250°C korrekt übernommen       |
| IT2       | Controller erkennt Zieltemperatur erreicht | F3            | ✅ Bestanden| Status korrekt berechnet            |
| IT3       | Controller verwaltet Power State korrekt   | F4            | ✅ Bestanden| PowerState bei Zieltemp. > 0 auf ON |
| IT4       | Resttemperaturlogik im Controller          | F5            | ✅ Bestanden| Cooling-Status korrekt erkannt      |

**Zusammenfassung Integrationstests Sprint 1:** 4/4 bestanden (100%)

---

### Systemtests (ST)

| Test-ID | Testname | Requirement | Status | Datum | Bemerkungen |
|---------|----------|-------------|--------|-------|-------------|
| ST1 | Kompletter Heizzyklus (ohne GUI) | F1.1-F5 | ✅ Bestanden | 30.11.2025 | Alle Zustandswechsel korrekt |
| ST2 | Fehlerhafte Eingaben werden abgefangen | F1.2, NF6.5 | ✅ Bestanden | 30.11.2025 | Ungültige Werte korrekt abgefangen |

**Zusammenfassung Systemtests Sprint 1:** 2/2 bestanden (100%)

---

**Gesamtzusammenfassung Sprint 1:** 16/16 Tests bestanden (100%)

---

## Sprint 2 – GUI

### Unit-Tests (UT)

| Test-ID   | Testname                                    | Requirement    | Status      | Bemerkungen                          |
|-----------|---------------------------------------------|----------------|-------------|--------------------------------------|
| UT11      | GUI: Validierung ungültiger Eingabe (Text)  | F1.3, F7       | ✅ Bestanden | Fehlermeldung bei "abc" angezeigt    |
| UT12      | GUI: Validierung ungültig (Zahl außerhalb)  | F1.3, F7       | ✅ Bestanden | Fehlermeldung bei "600" angezeigt    |
| UT13      | GUI: Aktualisierung Temperaturanzeige-Label | F-GUI1, F-GUI5 | ✅ Bestanden | Label zeigt 150°C korrekt            |
| UT14      | GUI: Aktivieren Start-Button                | F-GUI4, F6     | ✅ Bestanden | Button aktiviert bei Zieltemp. 180°C |

**Zusammenfassung Unit-Tests Sprint 2:** 4/4 bestanden (100%)

---

### Integrationstests (IT)

| Test-ID   | Testname                                        | Requirement   | Status      | Bemerkungen                          |
|-----------|-------------------------------------------------|---------------|-------------|--------------------------------------|
| IT5       | GUI setzt Zieltemperatur → Controller übernimmt | F-GUI2, NF6.6 | ✅ Bestanden | Wert 200°C korrekt übertragen        |
| IT6       | Start-Button löst Heizlogik aus                 | F-GUI4, F6    | ✅ Bestanden | Heizlogik startet bei Button-Klick   |
| IT7       | GUI aktualisiert bei neuem Temperaturwert       | F-GUI5        | ✅ Bestanden | Anzeige wechselt von 100°C auf 130°C |

**Zusammenfassung Integrationstests Sprint 2:** 3/3 bestanden (100%)


**Gesamtzusammenfassung Sprint 2:** 7/7 Tests bestanden (100%)

---

## Sprint 3 – Fehlerbehandlung & Performance

### Unit-Tests (UT)

| Test-ID   | Testname                                           | Requirement   | Status      | Bemerkungen                               |
|-----------|----------------------------------------------------|---------------|-------------|-------------------------------------------|
| UT15      | Validator: Gültige Temperatur                      | F6.1          | ✅ Bestanden | Rückgabe (True, "") bei 200°C             |
| UT16      | Validator: Ungültig (zu niedrig)                   | F6.1          | ✅ Bestanden | Rückgabe (False, Fehlermeldung) bei 30°C  |
| UT17      | Validator: Ungültig (zu hoch)                      | F6.1          | ✅ Bestanden | Rückgabe (False, Fehlermeldung) bei 600°C |
| UT18      | Validator: Nicht-numerischer Wert                  | F6.1          | ✅ Bestanden | Rückgabe (False, Fehlermeldung) bei "abc" |
| UT19      | ErrorHandler: Sensorfehler behandeln               | F6.2, F6.3    | ✅ Bestanden | Fehler aktiv, Anzeige "Err"               |
| UT20      | ErrorHandler: Auto-Löschen nach Timeout            | F6.4          | ✅ Bestanden | Fehler nach 11s automatisch gelöscht      |
| UT21      | ErrorHandler: Manuelles Löschen                    | F6.4          | ✅ Bestanden | Fehler via clear_error() gelöscht         |
| UT22      | StateMachine: Gültiger Übergang OFF → ON_HEATING   | F8            | ✅ Bestanden | Zustand wechselt korrekt                  |
| UT23      | StateMachine: Ungültiger Übergang OFF → ON_HOLDING | F8            | ✅ Bestanden | Exception geworfen, Zustand bleibt        |
| UT24      | StateMachine: Übergang ON_HEATING → ON_HOLDING     | F8            | ✅ Bestanden | Zustand wechselt bei Temp. erreicht       |
| UT25      | StateMachine: Übergang bei Sensorfehler            | F8, F6.3      | ✅ Bestanden | Zustand zu ERROR von überall möglich      |

**Zusammenfassung Unit-Tests Sprint 3:** 11/11 bestanden (100%)

---

### Integrationstests (IT)

| Test-ID   | Testname                                      | Requirement   | Status      | Bemerkungen                          |
|-----------|-----------------------------------------------|---------------|-------------|--------------------------------------|
| IT8       | GUI → Validator → Controller Integration      | F6.1, NF6.6   | ✅ Bestanden | Fehler "abc" korrekt behandelt       |
| IT9       | Controller → StateMachine → GUI Integration   | F8            | ✅ Bestanden | Status "Heating" korrekt angezeigt   |
| IT10      | Sensorfehler → ErrorHandler → GUI Integration | F6.2, F6.3    | ✅ Bestanden | "Err" angezeigt, Grill stoppt Heizen |

**Zusammenfassung Integrationstests Sprint 3:** 3/3 bestanden (100%)

---

### Performance-Tests (PT)

| Test-ID  | Testname                          | Requirement  | Status      | Bemerkungen                                  |
|----------|-----------------------------------|--------------|-------------|----------------------------------------------|
| PT1      | GUI-Update-Zeit bei normaler Last | F7           | ✅ Bestanden | Durchschnitt: 287ms, Max: 412ms, 95% < 500ms |
| PT2      | GUI-Update-Zeit bei hoher Last    | F7           | ✅ Bestanden | 90% < 500ms, Max: 489ms                      |

**Zusammenfassung Performance-Tests Sprint 3:** 2/2 bestanden (100%)

#### Performance-Metriken (F7)

| Messung                       | Ziel   | Erreicht  | Status      |
|-------------------------------|--------|-----------|-------------|
| Durchschnittliche Update-Zeit | <300ms | 287ms     | ✅ Bestanden |
| 95% Perzentil                 | <500ms | 412ms     | ✅ Bestanden |
| Maximum (normale Last)        | <500ms | 412ms     | ✅ Bestanden |
| Maximum (hohe Last)           | <500ms | 489ms     | ✅ Bestanden |

---

### Systemtests (ST)

| Test-ID   | Testname                          | Requirement    | Status      | Bemerkungen                                     |
|-----------|-----------------------------------|----------------|-------------|-------------------------------------------------|
| ST3       | Kompletter Grillzyklus mit GUI    | F1.1-F8        | ✅ Bestanden | Alle 9 Schritte erfolgreich, keine Fehler       |
| ST4       | Fehlerfall während Betrieb        | F6.2, F6.3, F8 | ✅ Bestanden | Sensorfehler erkannt, Grill stoppt, Recovery OK |
| ST5       | Ungültige Eingabe während Betrieb | F6.1, NF6.5    | ✅ Bestanden | Fehlermeldung, System stabil, Betrieb läuft     |

**Zusammenfassung Systemtests Sprint 3:** 3/3 bestanden (100%)

**Gesamtzusammenfassung Sprint 3:** 19/19 Tests bestanden (100%)

---

## Gesamtübersicht aller Sprints

### Testabdeckung nach Testarten

| Testart | Sprint 1 | Sprint 2 | Sprint 3 | Gesamt | Bestanden | Quote |
|---------|----------|----------|----------|--------|-----------|-------|
| **Unit-Tests (UT)** | 10 | 4 | 11 | 25 | 25 | 100% |
| **Integrationstests (IT)** | 4 | 3 | 3 | 10 | 10 | 100% |
| **Systemtests (ST)** | 2 | 0 | 3 | 5 | 5 | 100% |
| **Performance-Tests (PT)** | 0 | 0 | 2 | 2 | 2 | 100% |
| **Gesamt** | **16** | **7** | **19** | **42** | **42** | **100%** |

---

### Testabdeckung nach Requirements

| Requirement | Anzahl Tests | Status | Bemerkungen |
|-------------|--------------|--------|-------------|
| F1.1 | 2 | ✅ Vollständig getestet | Wunschtemperaturanzeige |
| F1.2 | 5 | ✅ Vollständig getestet | Wunschtemperaturänderung |
| F1.3 | 2 | ✅ Vollständig getestet | Validierung der Eingabewerte |
| F2 | 2 | ✅ Vollständig getestet | Aktuelle Temperatur |
| F2.1 | 1 | ✅ Vollständig getestet | Sensorfehler-Anzeige |
| F3 | 4 | ✅ Vollständig getestet | Zieltemperaturstatus |
| F4 | 5 | ✅ Vollständig getestet | An-/Aus-Funktion |
| F5 | 3 | ✅ Vollständig getestet | Resttemperaturanzeige |
| F6 | 3 | ✅ Vollständig getestet | GUI-Interaktion |
| F6.1 | 6 | ✅ Vollständig getestet | Ungültige Wunschtemperaturen |
| F6.2 | 3 | ✅ Vollständig getestet | Erkennung Sensorfehler |
| F6.3 | 3 | ✅ Vollständig getestet | Verhalten bei Sensorfehlern |
| F6.4 | 2 | ✅ Vollständig getestet | Auto-Verschwinden Fehleranzeigen |
| F7 | 4 | ✅ Vollständig getestet | Performance (<500ms) |
| F8 | 6 | ✅ Vollständig getestet | Zustandslogik |
| F-GUI1 | 2 | ✅ Vollständig getestet | Strukturierte Darstellung |
| F-GUI2 | 2 | ✅ Vollständig getestet | Änderung Wunschtemperatur (GUI) |
| F-GUI4 | 3 | ✅ Vollständig getestet | Nutzerinteraktionen |
| F-GUI5 | 3 | ✅ Vollständig getestet | Live-Anzeige |
| NF6.5 | 2 | ✅ Vollständig getestet | Robustheit/Fehlerresistenz |
| NF6.6 | 3 | ✅ Vollständig getestet | Konsistente Schnittstellen |

**Gesamt:** 21 Requirements vollständig getestet durch 42 Testfälle

---

## Fazit

✅ **Alle 42 Testfälle erfolgreich bestanden (100% Erfolgsquote)**

✅ **Alle funktionalen Requirements (F1.1-F8) vollständig getestet**

✅ **Alle nötigen nicht-funktionalen Requirements validiert**

✅ **Performance-Anforderungen (<500ms) erfüllt und nachgewiesen**


---

## Testhistorie

| Sprint   | Testdatum   |  Anzahl Tests  | Erfolgsquote  | Bemerkungen                       |
|----------|-------------|----------------|---------------|-----------------------------------|
| Sprint 1 | 30.11.2025  |  16            | 100%           | Kernlogik vollständig getestet    |
| Sprint 2 | 10.12.2025  |  7             | 100%           | GUI-Integration erfolgreich       |
| Sprint 3 | 18.12.2025  |  19            | 100%           | Fehlerbehandlung & Performance OK |
