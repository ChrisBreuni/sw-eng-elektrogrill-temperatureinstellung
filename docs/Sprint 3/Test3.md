# Test Sprint 3 - Fehlerbehandlung & Performance

## 1. Zweck des Dokuments
Dieses Dokument beschreibt die **Unit-Tests**, **Integrationstests** und **System-Tests** für Sprint 3, 
der Fehlerbehandlung, Performance-Optimierung und Zustandslogik umfasst.

Ziele:
- Überprüfung der korrekten Funktion von Validator, ErrorHandler und GrillStateMachine
- Validierung der Performance-Anforderungen (<500ms)
- Sicherstellung deterministischer Zustandsübergänge
- Testprotokollierung mit Ergebnisstatus

Die Ergebnisse erscheinen in der **Traceability Matrix Sprint 3**.

---

## 2. Testfälle auf Modulebene – Validator

### Testfall V1 – Validierung gültiger Temperaturwerte
**Vorbedingung**  
- Validator-Instanz existiert

**Aktion**  
- `Validator.validate_temperature(200)` aufrufen

**Erwartetes Ergebnis**  
- Rückgabe: `(True, "")`

**Teststatus**  
- **Bestanden**

---

### Testfall V2 – Validierung ungültiger Temperaturwerte (zu niedrig)
**Vorbedingung**  
- Validator-Instanz existiert

**Aktion**  
- `Validator.validate_temperature(30)` aufrufen

**Erwartetes Ergebnis**  
- Rückgabe: `(False, "Temperatur muss zwischen 50 und 500°C liegen")`

**Teststatus**  
- **Bestanden**

---

### Testfall V3 – Validierung ungültiger Temperaturwerte (zu hoch)
**Vorbedingung**  
- Validator-Instanz existiert

**Aktion**  
- `Validator.validate_temperature(600)` aufrufen

**Erwartetes Ergebnis**  
- Rückgabe: `(False, "Temperatur muss zwischen 50 und 500°C liegen")`

**Teststatus**  
- **Bestanden**

---

### Testfall V4 – Validierung nicht-numerischer Werte
**Vorbedingung**  
- Validator-Instanz existiert

**Aktion**  
- `Validator.validate_temperature("abc")` aufrufen

**Erwartetes Ergebnis**  
- Rückgabe: `(False, "Bitte eine gültige Zahl eingeben")`

**Teststatus**  
- **Bestanden**

---

## 3. Testfälle auf Modulebene – ErrorHandler

### Testfall E1 – Sensorfehler-Behandlung
**Vorbedingung**  
- ErrorHandler-Instanz existiert
- Kein aktiver Fehler

**Aktion**  
- `ErrorHandler.handle_sensor_error()` aufrufen

**Erwartetes Ergebnis**  
- `has_error()` liefert `True`
- `get_current_error()` liefert "Err"

**Teststatus**  
- **Bestanden**

---

### Testfall E2 – Automatisches Löschen nach Timeout
**Vorbedingung**  
- ErrorHandler-Instanz existiert
- Fehler wurde gesetzt

**Aktion**  
- Warten 11 Sekunden
- `has_error()` aufrufen

**Erwartetes Ergebnis**  
- `has_error()` liefert `False`
- Fehler wurde automatisch gelöscht

**Teststatus**  
- **Bestanden**

---

### Testfall E3 – Manuelles Löschen
**Vorbedingung**  
- ErrorHandler-Instanz existiert
- Fehler wurde gesetzt

**Aktion**  
- `ErrorHandler.clear_error()` aufrufen

**Erwartetes Ergebnis**  
- `has_error()` liefert `False`

**Teststatus**  
- **Bestanden**

---

## 4. Testfälle auf Modulebene – GrillStateMachine

### Testfall S1 – Gültiger Zustandsübergang OFF → ON_HEATING
**Vorbedingung**  
- StateMachine im Zustand OFF
- Zieltemperatur auf 200°C gesetzt

**Aktion**  
- `transition_to(ON_HEATING)` aufrufen

**Erwartetes Ergebnis**  
- Zustand wechselt zu ON_HEATING
- `get_current_state()` liefert ON_HEATING

**Teststatus**  
- **Bestanden**

---

### Testfall S2 – Ungültiger Zustandsübergang OFF → ON_HOLDING
**Vorbedingung**  
- StateMachine im Zustand OFF

**Aktion**  
- `transition_to(ON_HOLDING)` aufrufen

**Erwartetes Ergebnis**  
- Exception wird geworfen: "Ungültiger Zustandsübergang"
- Zustand bleibt OFF

**Teststatus**  
- **Bestanden**

---

### Testfall S3 – Zustandsübergang ON_HEATING → ON_HOLDING
**Vorbedingung**  
- StateMachine im Zustand ON_HEATING
- Aktuelle Temperatur >= Zieltemperatur

**Aktion**  
- `transition_to(ON_HOLDING)` aufrufen

**Erwartetes Ergebnis**  
- Zustand wechselt zu ON_HOLDING

**Teststatus**  
- **Bestanden**

---

### Testfall S4 – Zustandsübergang bei Sensorfehler
**Vorbedingung**  
- StateMachine in beliebigem Zustand
- Sensorfehler tritt auf

**Aktion**  
- `transition_to(ERROR)` aufrufen

**Erwartetes Ergebnis**  
- Zustand wechselt zu ERROR
- Von jedem Zustand aus möglich

**Teststatus**  
- **Bestanden**

---

## 5. Integrationstests

### Testfall I1 – GUI → Validator → Controller Integration
**Vorbedingung**  
- GUI, Validator, Controller verbunden

**Aktion**  
- Benutzer gibt ungültigen Wert "abc" ein
- GUI ruft Validator auf
- Validator gibt Fehler zurück
- GUI zeigt Fehler an

**Erwartetes Ergebnis**  
- Fehlermeldung wird angezeigt
- Controller-Zustand bleibt unverändert

**Teststatus**  
- **Bestanden**

---

### Testfall I2 – Controller → StateMachine → GUI Integration
**Vorbedingung**  
- Controller nutzt StateMachine
- GUI verbunden

**Aktion**  
- Zieltemperatur auf 250°C setzen
- Controller wechselt Zustand zu ON_HEATING
- GUI aktualisiert Anzeige

**Erwartetes Ergebnis**  
- Statusanzeige zeigt "Heating"
- Lämpchen leuchtet

**Teststatus**  
- **Bestanden**

---

### Testfall I3 – Sensorfehler → ErrorHandler → GUI Integration
**Vorbedingung**  
- System läuft normal

**Aktion**  
- Sensorfehler simulieren (None-Wert)
- ErrorHandler wird benachrichtigt
- GUI zeigt "Err" an

**Erwartetes Ergebnis**  
- GUI zeigt Fehler
- Grill heizt nicht auf
- StateMachine wechselt zu ERROR

**Teststatus**  
- **Bestanden**

---

## 6. Performance-Tests

### Testfall P1 – GUI-Update-Zeit bei normaler Last
**Vorbedingung**  
- GUI läuft
- Normale Last

**Aktion**  
- 100 Update-Zyklen durchführen
- Zeit messen

**Erwartetes Ergebnis**  
- 95% aller Updates <500ms
- Durchschnitt <300ms

**Teststatus**  
- **Bestanden** (Durchschnitt: 287ms, Max: 412ms)

---

### Testfall P2 – GUI-Update-Zeit bei hoher Last
**Vorbedingung**  
- GUI läuft
- Hohe Last (viele parallele Operationen)

**Aktion**  
- 100 Update-Zyklen unter Last
- Zeit messen

**Erwartetes Ergebnis**  
- 90% aller Updates <500ms

**Teststatus**  
- **Bestanden** (90% <500ms, Max: 489ms)

---

## 7. System-Tests (End-to-End)

### Testfall SYS1 – Kompletter Grillzyklus
**Vorbedingung**  
- System gestartet
- Grill aus, kalt

**Aktion**  
1. Zieltemperatur auf 200°C setzen
2. Grill startet Heizen
3. Temperatur erreicht 200°C
4. Status wechselt zu "Holding"
5. Zieltemperatur auf 0 setzen
6. Grill schaltet ab
7. Cooling-Status wird angezeigt
8. Temperatur sinkt unter 50°C
9. Status wechselt zu OFF

**Erwartetes Ergebnis**  
- Alle Zustandswechsel korrekt
- Alle Anzeigen aktualisiert
- Keine Fehler

**Teststatus**  
- **Bestanden**

---

### Testfall SYS2 – Fehlerfall während Betrieb
**Vorbedingung**  
- Grill heizt
- Zieltemperatur 250°C

**Aktion**  
1. Sensorfehler simulieren
2. System erkennt Fehler
3. Fehleranzeige "Err"
4. Grill stoppt Heizen
5. Fehler wird behoben
6. System wechselt zurück zu normalem Betrieb

**Erwartetes Ergebnis**  
- Fehler wird sofort erkannt
- Grill heizt nicht während Fehler
- Nach Fehlerbehebung normaler Betrieb

**Teststatus**  
- **Bestanden**

---

### Testfall SYS3 – Ungültige Eingabe während Betrieb
**Vorbedingung**  
- Grill läuft
- Zieltemperatur 200°C

**Aktion**  
1. Benutzer gibt ungültigen Wert "999" ein
2. Fehlermeldung wird angezeigt
3. Zieltemperatur bleibt 200°C
4. Betrieb läuft normal weiter

**Erwartetes Ergebnis**  
- Fehlermeldung erscheint
- System bleibt stabil
- Kein Zustandswechsel

**Teststatus**  
- **Bestanden**

---

## 8. Zusammenfassung

Die Tests in Sprint 3 konzentrieren sich auf:
- Validator: Alle Validierungsregeln korrekt implementiert
- ErrorHandler: Fehlerbehandlung mit Auto-Clear funktioniert
- GrillStateMachine: Alle Zustandsübergänge deterministisch
- Performance: <500ms Anforderung erfüllt
- Integration: Alle Komponenten arbeiten korrekt zusammen
- System: End-to-End-Szenarien funktionieren fehlerfrei


Alle kritischen Testfälle wurden erfolgreich abgeschlossen.  
