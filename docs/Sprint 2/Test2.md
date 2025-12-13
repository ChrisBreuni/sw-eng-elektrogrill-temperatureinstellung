# Tests Sprint 2 - GUI

## 1. Zweck des Dokuments
Dieses Dokument beschreibt die **Modultests** und **Integrationstests** für Sprint 2, der den **GUI-Entwurf** umfasst.

Ziele:
- Überprüfung der korrekten Funktion der GUI-Logik  
- Validierung der Schnittstellen zwischen GUI, Temperaturmodulen und Kontrolllogik  
- Sicherstellung, dass Nutzerinteraktionen korrekt verarbeitet werden  
- Testprotokollierung mit Ergebnisstatus  

Die Ergebnisse erscheinen in der **Traceability Matrix Sprint 2**.

---

# 2. Testfälle auf Modulebene (GUI-Komponenten)

## Testfall M1 – Validierung der Eingabe für Wunschtemperatur im GUI
**Vorbedingung**  
- GUI ist gestartet.  
- TargetTemperature-Objekt existiert mit Standardwert 0.

**Aktion**  
- Benutzer gibt einen ungültigen Wert ein: `abc` oder `600`.

**Erwartetes Ergebnis**  
- GUI zeigt eine Fehlermeldung.  
- TargetTemperature wird **nicht** verändert.  
- Eingabefeld wird zurückgesetzt oder rot markiert.

**Nachbedingung**  
- Wunschtemperatur bleibt 0 oder letzter gültiger Wert.

**Teststatus**  
- **Bestanden**

---

## Testfall M2 – Aktualisierung des Temperaturanzeige-Labels
**Vorbedingung**  
- GUI ist aktiv.  
- CurrentTemperature liefert `150`.

**Aktion**  
- GUI ruft `CurrentTemperature.get_temperature()` auf.  
- Anzeige soll aktualisiert werden.

**Erwartetes Ergebnis**  
- GUI zeigt: „Aktuelle Temperatur: 150°C“.

**Nachbedingung**  
- Temperatur-Label enthält den neuen Wert.

**Teststatus**  
- **Bestanden**

---

## Testfall M3 – Aktivieren/Deaktivieren des Start-Buttons
**Vorbedingung**  
- Wunschtemperatur ist 0.  
- Start-Button deaktiviert.

**Aktion**  
- Benutzer stellt gültige Wunschtemperatur, z. B. 180°C ein.

**Erwartetes Ergebnis**  
- Start-Button wird aktiviert.

**Nachbedingung**  
- Button ist anklickbar.

**Teststatus**  
- **Bestanden**

---

# 3. Integrationstests (GUI ↔ Kernlogik)

## Testfall I1 – GUI setzt TargetTemperature → Kontrolllogik übernimmt Wert
**Vorbedingung**  
- GUI ist mit TargetTemperature verbunden.

**Aktion**  
- Benutzer gibt 200°C ein.  
- GUI ruft `TargetTemperature.set_temperature(200)` auf.

**Erwartetes Ergebnis**  
- Wert wird akzeptiert.  
- Kontrolllogik erhält gültigen Temperaturwert.

**Nachbedingung**  
- TargetTemperature intern = 200°C.

**Teststatus**  
- **Bestanden**

---

## Testfall I2 – Start-Button löst Start der Heizlogik aus
**Vorbedingung**  
- Wunschtemperatur gültig (z. B. 250°C).  
- Start-Button ist aktiv.

**Aktion**  
- Benutzer klickt „Start“.

**Erwartetes Ergebnis**  
- GUI sendet Start-Event.  
- Heizlogik wird gestartet.

**Nachbedingung**  
- Systemstatus = „Heating“.

**Teststatus**  
- **Bestanden**

---

## Testfall I3 – GUI aktualisiert Anzeige nach neuem Temperaturwert
**Vorbedingung**  
- GUI ist mit CurrentTemperature verbunden.  
- Anzeige zeigt 100°C.

**Aktion**  
- CurrentTemperature liefert Update auf 130°C.

**Erwartetes Ergebnis**  
- GUI aktualisiert Anzeige ohne Verzögerung oder Fehler.

**Nachbedingung**  
- GUI zeigt 130°C.

**Teststatus**  
- **Bestanden**

---

# 4. Zusammenfassung
Die Tests in Sprint 2 konzentrieren sich auf:
- GUI-Logik  
- Validierung von Benutzereingaben  
- Interaktion zwischen GUI und Backend-Modulen  
- Konsistentes Temperatur-Update  

