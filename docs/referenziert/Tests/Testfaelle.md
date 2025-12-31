# Testfälle – Elektrogrill Temperatursteuerung
## Sprint 1 – Kernlogik

### Unit-Tests (UT)

#### UT1 – Validierung gültiger Zieltemperatur
**Requirement:** F1.2  
**Vorbedingung:** TargetTemperature-Objekt existiert  
**Aktion:** `set_temperature(200)` aufrufen  
**Erwartetes Ergebnis:** Wert wird akzeptiert, `get_temperature()` liefert 200  
**Nachbedingung:** Zieltemperatur = 200°C  

#### UT2 – Validierung ungültiger Zieltemperatur (zu niedrig)
**Requirement:** F1.2  
**Vorbedingung:** TargetTemperature-Objekt existiert  
**Aktion:** `set_temperature(30)` aufrufen  
**Erwartetes Ergebnis:** ValueError wird geworfen, Temperatur bleibt unverändert  
**Nachbedingung:** Zieltemperatur = vorheriger Wert  

#### UT3 – Validierung ungültiger Zieltemperatur (zu hoch)
**Requirement:** F1.2  
**Vorbedingung:** TargetTemperature-Objekt existiert  
**Aktion:** `set_temperature(600)` aufrufen  
**Erwartetes Ergebnis:** ValueError wird geworfen, Temperatur bleibt unverändert  
**Nachbedingung:** Zieltemperatur = vorheriger Wert  

#### UT4 – Validierung Sonderfall Zieltemperatur = 0
**Requirement:** F1.2, F4  
**Vorbedingung:** TargetTemperature-Objekt existiert  
**Aktion:** `set_temperature(0)` aufrufen  
**Erwartetes Ergebnis:** Wert wird akzeptiert (Grill aus)  
**Nachbedingung:** Zieltemperatur = 0°C  

#### UT5 – Aktuelle Temperatur abrufen
**Requirement:** F2  
**Vorbedingung:** CurrentTemperature-Objekt mit Wert 150°C  
**Aktion:** `get_temperature()` aufrufen  
**Erwartetes Ergebnis:** Rückgabe = 150  
**Nachbedingung:** Keine Änderung  

#### UT6 – Zieltemperatur erreicht (aktuelle >= Ziel)
**Requirement:** F3  
**Vorbedingung:** Aktuelle Temp = 200°C, Ziel = 180°C  
**Aktion:** `is_target_reached()` aufrufen  
**Erwartetes Ergebnis:** Rückgabe = True  
**Nachbedingung:** Keine Änderung  

#### UT7 – Zieltemperatur nicht erreicht (aktuelle < Ziel)
**Requirement:** F3  
**Vorbedingung:** Aktuelle Temp = 120°C, Ziel = 180°C  
**Aktion:** `is_target_reached()` aufrufen  
**Erwartetes Ergebnis:** Rückgabe = False  
**Nachbedingung:** Keine Änderung  

#### UT8 – Power State einschalten
**Requirement:** F4  
**Vorbedingung:** PowerState = OFF  
**Aktion:** `turn_on()` aufrufen  
**Erwartetes Ergebnis:** PowerState wechselt zu ON  
**Nachbedingung:** `is_on()` liefert True  

#### UT9 – Power State ausschalten
**Requirement:** F4  
**Vorbedingung:** PowerState = ON  
**Aktion:** `turn_off()` aufrufen  
**Erwartetes Ergebnis:** PowerState wechselt zu OFF  
**Nachbedingung:** `is_on()` liefert False  

#### UT10 – Resttemperatur erkennen
**Requirement:** F5  
**Vorbedingung:** Grill aus, aktuelle Temp = 120°C  
**Aktion:** `is_rest_temperature()` aufrufen  
**Erwartetes Ergebnis:** Rückgabe = True (noch heiß)  
**Nachbedingung:** Keine Änderung  

---

### Integrationstests (IT)

#### IT1 – Controller setzt Zieltemperatur korrekt
**Requirement:** F1.2  
**Vorbedingung:** GrillController mit TargetTemperature verbunden  
**Aktion:** `controller.set_target_temperature(250)` aufrufen  
**Erwartetes Ergebnis:** TargetTemperature intern = 250°C  
**Nachbedingung:** `get_target_temperature()` liefert 250  

#### IT2 – Controller erkennt Zieltemperatur erreicht
**Requirement:** F3  
**Vorbedingung:** Aktuelle = 200°C, Ziel = 200°C  
**Aktion:** `controller.is_target_reached()` aufrufen  
**Erwartetes Ergebnis:** Rückgabe = True  
**Nachbedingung:** Keine Änderung  

#### IT3 – Controller verwaltet Power State korrekt
**Requirement:** F4  
**Vorbedingung:** Zieltemperatur = 0  
**Aktion:** Zieltemperatur auf 180°C setzen  
**Erwartetes Ergebnis:** PowerState wechselt zu ON  
**Nachbedingung:** Grill ist eingeschaltet  

#### IT4 – Resttemperaturlogik im Controller
**Requirement:** F5  
**Vorbedingung:** Grill ein, aktuelle Temp = 300°C  
**Aktion:** Zieltemperatur auf 0 setzen (Grill aus)  
**Erwartetes Ergebnis:** PowerState = OFF, aber `is_cooling_down()` = True  
**Nachbedingung:** Restwärme wird erkannt  

---

### Systemtests (ST)

#### ST1 – Kompletter Heizzyklus (ohne GUI)
**Requirement:** F1.1, F1.2, F2, F3, F4  
**Vorbedingung:** System initialisiert, Grill aus  
**Aktion:**  
1. Zieltemperatur auf 200°C setzen  
2. Aktuelle Temperatur simuliert steigt von 20°C auf 200°C  
3. Zieltemperatur auf 0 setzen  

**Erwartetes Ergebnis:**  
- Grill schaltet ein bei Schritt 1  
- `is_target_reached()` liefert True bei Schritt 2  
- Grill schaltet aus bei Schritt 3  

**Nachbedingung:** System konsistent  

#### ST2 – Fehlerhafte Eingaben werden abgefangen
**Requirement:** F1.2, NF6.5  
**Vorbedingung:** System läuft  
**Aktion:** Versuche ungültige Werte zu setzen (10°C, 700°C, "abc")  
**Erwartetes Ergebnis:** Alle Eingaben werden abgefangen (ValueError), System bleibt stabil  
**Nachbedingung:** Zieltemperatur unverändert  

---

## Sprint 2 – GUI

### Unit-Tests (UT)

#### UT11 – GUI: Validierung ungültiger Eingabe (Text)
**Requirement:** F1.3, F7  
**Vorbedingung:** GUI gestartet, Zieltemperatur = 0  
**Aktion:** Benutzer gibt "abc" ein  
**Erwartetes Ergebnis:** Fehlermeldung wird angezeigt, Zieltemperatur bleibt 0  
**Nachbedingung:** Eingabefeld zurückgesetzt oder rot markiert  

#### UT12 – GUI: Validierung ungültiger Eingabe (Zahl außerhalb Bereich)
**Requirement:** F1.3, F7  
**Vorbedingung:** GUI gestartet, Zieltemperatur = 0  
**Aktion:** Benutzer gibt "600" ein  
**Erwartetes Ergebnis:** Fehlermeldung wird angezeigt, Zieltemperatur bleibt 0  
**Nachbedingung:** Eingabefeld zurückgesetzt oder rot markiert  

#### UT13 – GUI: Aktualisierung Temperaturanzeige-Label
**Requirement:** F-GUI1, F-GUI5  
**Vorbedingung:** GUI aktiv, CurrentTemperature = 150°C  
**Aktion:** GUI ruft `get_temperature()` auf  
**Erwartetes Ergebnis:** Label zeigt "Aktuelle Temperatur: 150°C"  
**Nachbedingung:** Label korrekt aktualisiert  

#### UT14 – GUI: Aktivieren Start-Button
**Requirement:** F-GUI4, F6  
**Vorbedingung:** Zieltemperatur = 0, Start-Button deaktiviert  
**Aktion:** Benutzer setzt Zieltemperatur auf 180°C  
**Erwartetes Ergebnis:** Start-Button wird aktiviert  
**Nachbedingung:** Button ist anklickbar  

---

### Integrationstests (IT)

#### IT5 – GUI setzt Zieltemperatur → Controller übernimmt
**Requirement:** F-GUI2, NF6.6  
**Vorbedingung:** GUI mit Controller verbunden  
**Aktion:** Benutzer gibt 200°C ein, GUI ruft `set_target_temperature(200)` auf  
**Erwartetes Ergebnis:** Controller-Zieltemperatur = 200°C  
**Nachbedingung:** Wert konsistent zwischen GUI und Controller  

#### IT6 – Start-Button löst Heizlogik aus
**Requirement:** F-GUI4, F6  
**Vorbedingung:** Zieltemperatur gültig (250°C), Start-Button aktiv  
**Aktion:** Benutzer klickt "Start"  
**Erwartetes Ergebnis:** GUI sendet Start-Event, Heizlogik startet  
**Nachbedingung:** Systemstatus = "Heating"  

#### IT7 – GUI aktualisiert bei neuem Temperaturwert
**Requirement:** F-GUI5  
**Vorbedingung:** GUI verbunden, Anzeige zeigt 100°C  
**Aktion:** CurrentTemperature liefert Update auf 130°C  
**Erwartetes Ergebnis:** GUI aktualisiert Anzeige ohne Verzögerung  
**Nachbedingung:** GUI zeigt 130°C  

---

## Sprint 3 – Fehlerbehandlung & Performance

### Unit-Tests (UT)

#### UT15 – Validator: Gültige Temperatur
**Requirement:** F6.1  
**Vorbedingung:** Validator-Instanz existiert  
**Aktion:** `validate_temperature(200)` aufrufen  
**Erwartetes Ergebnis:** Rückgabe = (True, "")  
**Nachbedingung:** Keine Änderung  

#### UT16 – Validator: Ungültige Temperatur (zu niedrig)
**Requirement:** F6.1  
**Vorbedingung:** Validator-Instanz existiert  
**Aktion:** `validate_temperature(30)` aufrufen  
**Erwartetes Ergebnis:** Rückgabe = (False, "Temperatur muss zwischen 50 und 500°C liegen")  
**Nachbedingung:** Keine Änderung  

#### UT17 – Validator: Ungültige Temperatur (zu hoch)
**Requirement:** F6.1  
**Vorbedingung:** Validator-Instanz existiert  
**Aktion:** `validate_temperature(600)` aufrufen  
**Erwartetes Ergebnis:** Rückgabe = (False, "Temperatur muss zwischen 50 und 500°C liegen")  
**Nachbedingung:** Keine Änderung  

#### UT18 – Validator: Nicht-numerischer Wert
**Requirement:** F6.1  
**Vorbedingung:** Validator-Instanz existiert  
**Aktion:** `validate_temperature("abc")` aufrufen  
**Erwartetes Ergebnis:** Rückgabe = (False, "Bitte eine gültige Zahl eingeben")  
**Nachbedingung:** Keine Änderung  

#### UT19 – ErrorHandler: Sensorfehler behandeln
**Requirement:** F6.2, F6.3  
**Vorbedingung:** ErrorHandler-Instanz, kein aktiver Fehler  
**Aktion:** `handle_sensor_error()` aufrufen  
**Erwartetes Ergebnis:** `has_error()` = True, `get_current_error()` = "Err"  
**Nachbedingung:** Fehler aktiv  

#### UT20 – ErrorHandler: Automatisches Löschen nach Timeout
**Requirement:** F6.4  
**Vorbedingung:** ErrorHandler mit aktivem Fehler  
**Aktion:** 11 Sekunden warten  
**Erwartetes Ergebnis:** `has_error()` = False  
**Nachbedingung:** Fehler automatisch gelöscht  

#### UT21 – ErrorHandler: Manuelles Löschen
**Requirement:** F6.4  
**Vorbedingung:** ErrorHandler mit aktivem Fehler  
**Aktion:** `clear_error()` aufrufen  
**Erwartetes Ergebnis:** `has_error()` = False  
**Nachbedingung:** Fehler gelöscht  

#### UT22 – StateMachine: Gültiger Übergang OFF → ON_HEATING
**Requirement:** F8  
**Vorbedingung:** StateMachine im Zustand OFF, Zieltemperatur = 200°C  
**Aktion:** `transition_to(ON_HEATING)` aufrufen  
**Erwartetes Ergebnis:** Zustand wechselt zu ON_HEATING  
**Nachbedingung:** `get_current_state()` = ON_HEATING  

#### UT23 – StateMachine: Ungültiger Übergang OFF → ON_HOLDING
**Requirement:** F8  
**Vorbedingung:** StateMachine im Zustand OFF  
**Aktion:** `transition_to(ON_HOLDING)` aufrufen  
**Erwartetes Ergebnis:** Exception "Ungültiger Zustandsübergang", Zustand bleibt OFF  
**Nachbedingung:** Zustand = OFF  

#### UT24 – StateMachine: Übergang ON_HEATING → ON_HOLDING
**Requirement:** F8  
**Vorbedingung:** StateMachine = ON_HEATING, aktuelle Temp >= Ziel  
**Aktion:** `transition_to(ON_HOLDING)` aufrufen  
**Erwartetes Ergebnis:** Zustand wechselt zu ON_HOLDING  
**Nachbedingung:** `get_current_state()` = ON_HOLDING  

#### UT25 – StateMachine: Übergang bei Sensorfehler
**Requirement:** F8, F6.3  
**Vorbedingung:** StateMachine in beliebigem Zustand, Sensorfehler tritt auf  
**Aktion:** `transition_to(ERROR)` aufrufen  
**Erwartetes Ergebnis:** Zustand wechselt zu ERROR (von jedem Zustand aus möglich)  
**Nachbedingung:** `get_current_state()` = ERROR  

---

### Integrationstests (IT)

#### IT8 – GUI → Validator → Controller Integration
**Requirement:** F6.1, NF6.6  
**Vorbedingung:** GUI, Validator, Controller verbunden  
**Aktion:** Benutzer gibt "abc" ein, GUI ruft Validator auf  
**Erwartetes Ergebnis:** Validator gibt Fehler zurück, GUI zeigt Fehler an, Controller unverändert  
**Nachbedingung:** System konsistent  

#### IT9 – Controller → StateMachine → GUI Integration
**Requirement:** F8  
**Vorbedingung:** Controller nutzt StateMachine, GUI verbunden  
**Aktion:** Zieltemperatur auf 250°C setzen, Controller wechselt zu ON_HEATING  
**Erwartetes Ergebnis:** GUI zeigt Status "Heating", Lämpchen leuchtet  
**Nachbedingung:** Anzeigen konsistent  

#### IT10 – Sensorfehler → ErrorHandler → GUI Integration
**Requirement:** F6.2, F6.3  
**Vorbedingung:** System läuft normal  
**Aktion:** Sensorfehler simulieren (None-Wert), ErrorHandler benachrichtigt  
**Erwartetes Ergebnis:** GUI zeigt "Err", Grill heizt nicht auf, StateMachine = ERROR  
**Nachbedingung:** System in Fehlerzustand, sicher  

---

### Performance-Tests (PT)

#### PT1 – GUI-Update-Zeit bei normaler Last
**Requirement:** F7  
**Vorbedingung:** GUI läuft, normale Last  
**Aktion:** 100 Update-Zyklen durchführen, Zeit messen  
**Erwartetes Ergebnis:** 95% aller Updates <500ms, Durchschnitt <300ms  
**Nachbedingung:** Performance-Ziel erfüllt  

#### PT2 – GUI-Update-Zeit bei hoher Last
**Requirement:** F7  
**Vorbedingung:** GUI läuft, hohe Last (viele parallele Operationen)  
**Aktion:** 100 Update-Zyklen unter Last, Zeit messen  
**Erwartetes Ergebnis:** 90% aller Updates <500ms  
**Nachbedingung:** Performance-Ziel erfüllt  

---

### System-Tests (ST)

#### ST3 – Kompletter Grillzyklus mit GUI
**Requirement:** F1.1-F8  
**Vorbedingung:** System gestartet, Grill aus, kalt  
**Aktion:**  
1. Zieltemperatur auf 200°C setzen  
2. Grill startet Heizen  
3. Temperatur erreicht 200°C  
4. Status wechselt zu "Holding"  
5. Zieltemperatur auf 0 setzen  
6. Grill schaltet ab  
7. Cooling-Status angezeigt  
8. Temperatur sinkt unter 50°C  
9. Status wechselt zu OFF  

**Erwartetes Ergebnis:** Alle Zustandswechsel korrekt, alle Anzeigen aktualisiert, keine Fehler  
**Nachbedingung:** System zurück im Ausgangszustand  

#### ST4 – Fehlerfall während Betrieb
**Requirement:** F6.2, F6.3, F8  
**Vorbedingung:** Grill heizt, Zieltemperatur = 250°C  
**Aktion:**  
1. Sensorfehler simulieren  
2. System erkennt Fehler  
3. Fehleranzeige "Err"  
4. Grill stoppt Heizen  
5. Fehler behoben  
6. System wechselt zurück zu normalem Betrieb  

**Erwartetes Ergebnis:** Fehler sofort erkannt, Grill heizt nicht während Fehler, nach Behebung normaler Betrieb  
**Nachbedingung:** System stabil und betriebsbereit  

#### ST5 – Ungültige Eingabe während Betrieb
**Requirement:** F6.1, NF6.5  
**Vorbedingung:** Grill läuft, Zieltemperatur = 200°C  
**Aktion:** Benutzer gibt ungültigen Wert "999" ein  
**Erwartetes Ergebnis:** Fehlermeldung erscheint, Zieltemperatur bleibt 200°C, Betrieb läuft normal weiter  
**Nachbedingung:** System stabil, kein Zustandswechsel  

---

## Testabdeckung

| Sprint | Unit-Tests | Integrationstests | System-Tests | Performance-Tests | Gesamt |
|--------|-----------|------------------|--------------|------------------|--------|
| Sprint 1 | 10 (UT1-UT10) | 4 (IT1-IT4) | 2 (ST1-ST2) | 0 | 16 |
| Sprint 2 | 4 (UT11-UT14) | 3 (IT5-IT7) | 0 | 0 | 7 |
| Sprint 3 | 11 (UT15-UT25) | 3 (IT8-IT10) | 3 (ST3-ST5) | 2 (PT1-PT2) | 19 |
| **Gesamt** | **25** | **10** | **5** | **2** | **42** |
