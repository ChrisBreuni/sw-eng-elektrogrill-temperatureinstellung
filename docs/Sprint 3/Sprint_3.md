# Sprint 3

### Schritt 1: Sprint Planning

Zu Beginn des dritten Sprints habe ich die relevanten Anforderungen (Requirements) ausgewählt. 
Der Fokus lag dabei auf der Verfeinerung der bestehenden Funktionalität, Fehlerbehandlung und 
Performance-Optimierungen. Konkret wurden folgende Kernfunktionen identifiziert und berücksichtigt:

- Vollständige Fehlerbehandlung und Sensorfehler-Erkennung
- Performance-Optimierung und zeitnahe Aktualisierung aller Anzeigen
- Zustandslogik-Verfeinerung und deterministisches Zustandsverhalten
- Refactoring der Validierungslogik
- Finale Integration und Systemtests

Bei der Auswahl der Anforderungen wurde bewusst auf eine realistische und zielgerichtete Planung 
geachtet. Mit Sprint 3 wird das System finalisiert, alle offenen Requirements abgeschlossen und 
die Code-Qualität auf ein produktionsreifes Niveau gebracht.

**Requirements:**

- Req. F2.1: Aktuelle Temperatur (Sensorfehler-Anzeige)
- Req. F6.1: Ungültige Wunschtemperaturen erkennen und anzeigen
- Req. F6.2: Erkennung von Sensorfehlern
- Req. F6.3: Verhalten bei Sensorfehlern (Grill darf nicht aufheizen)
- Req. F6.4: Verhalten der Fehleranzeigen (automatisches Verschwinden)
- Req. F7: Performance / Aktualisierung (500ms Reaktionszeit)
- Req. F8: Zustandslogik (deterministische Zustandswechsel)

**Sprint-Zeitraum:** 10.12.2025 - 20.12.2025 (voraussichtlich ca.)

**Sprintziel:**

1. Vollständige Implementierung der Fehlerbehandlung (Sensorfehler, ungültige Eingaben)
2. Performance-Optimierung für zeitnahe Aktualisierung (<500ms)
3. Refactoring der Validierungslogik (einheitliche Strategie)
4. Zustandslogik-Verfeinerung (deterministische Übergänge)
5. Umfassende System- und Integrationstests
6. Code-Qualität sicherstellen (Refactoring, Code Reviews)

---

### Schritt 2: Architektur

Nach der Anforderungsanalyse beschäftigte ich mich mit der Architektur-Verfeinerung für Sprint 3. 
Ziel war es, die bestehende Architektur zu optimieren und offene Punkte aus Sprint 2 zu adressieren.

Basierend auf den Erkenntnissen aus Sprint 2 und den nicht-funktionalen Anforderungen wie 
Performance und Robustheit werden folgende Architektur-Verbesserungen vorgenommen:

**A1. Einheitliche Validierungsstrategie:** Validierungslogik wird zentralisiert. Eine zentrale `Validator`-Klasse übernimmt alle Validierungen. GUI ruft nur noch Validator-Methoden auf, keine eigene Validierungslogik mehr.

**A2. Fehlerbehandlungs-Schicht:** Neue Klasse `ErrorHandler` für zentrale Fehlerbehandlung. Kapselt Sensorfehler-Erkennung, Fehleranzeige-Logik, automatisches Verschwinden von Fehleranzeigen.

**A3. Zustandsautomat-Verfeinerung:** Klasse `GrillStateMachine` für deterministische Zustandsübergänge. Explizite Zustände: `OFF`, `ON_HEATING`, `ON_HOLDING`, `COOLING`, `ERROR`.

**A4. Performance-Monitoring:** Einführung eines `PerformanceMonitor` zur Überwachung der Update-Zeiten. Sicherstellen, dass alle Updates <500ms erfolgen.

[Architektur](../Architektur.md)

---

### Schritt 3: Design

Im Anschluss an die Architekturdefinition wurde der Entwurfsprozess für die neuen Komponenten 
fortgeführt. Ziel war es, die zentralen Klassen für Fehlerbehandlung, Validierung und 
Zustandsmanagement zu entwerfen.

**Klasse Validator:** Zentrale Validierungsklasse mit Methoden: `validate_temperature(value)`, `is_in_range(value, min, max)`, `is_numeric(value)`. Rückgabe von Tupeln: `(is_valid: bool, error_message: str)`.

**Klasse ErrorHandler:** Fehlerbehandlungs-Klasse mit Methoden: `handle_sensor_error()`, `handle_invalid_input(message)`, `clear_error()`, `get_current_error()`. Unterstützt automatisches Timeout für Fehleranzeigen.

**Klasse GrillStateMachine:** Zustandsautomat mit Methoden: `transition_to(new_state)`, `get_current_state()`, `is_valid_transition(from_state, to_state)`. Implementiert deterministische Zustandsübergänge gemäß F8.

**Refactoring GrillGUI:** Entfernung der GUI-internen Validierungslogik. GUI ruft nur noch `Validator` und `ErrorHandler` auf. Verbesserte Separation of Concerns.

**Integration:** Alle neuen Komponenten werden nahtlos in die bestehende Architektur integriert. `GrillController` nutzt `GrillStateMachine` für Zustandsverwaltung.

[Design](Design3.md)

---

### Schritt 4: Implementierung

Nach Abschluss der Designphase begann die Umsetzung der neuen Komponenten gemäß der zuvor 
definierten Architektur- und Entwurfsdokumente. Dabei wurde iterativ und testgetrieben vorgegangen, 
um frühzeitig funktionale Korrektheit und Konsistenz sicherzustellen.

**Klasse Validator:** Implementierung der zentralen Validierungslogik. Alle Temperaturvalidierungen werden über diese Klasse abgewickelt. GUI und Controller nutzen einheitliche Schnittstellen.

**Klasse ErrorHandler:** Implementierung der Fehlerbehandlung mit automatischem Timeout. Integration mit GUI für Fehleranzeige. Sensorfehler-Erkennung (z.B. None-Werte, ungültige Messwerte).

**Klasse GrillStateMachine:** Implementierung des Zustandsautomaten. Definierte Zustandsübergänge gemäß Pflichtenheft F8. Logging aller Zustandswechsel für Debugging.

**Refactoring GrillGUI:** Entfernung redundanter Validierungslogik. GUI delegiert alle Validierungen an `Validator`. Fehleranzeigen werden über `ErrorHandler` gesteuert.

**Performance-Optimierung:** Optimierung der Update-Mechanismen. Sicherstellung, dass alle Anzeigen innerhalb 500ms aktualisiert werden. Profiling zur Identifikation von Bottlenecks.

**Kontinuierliche Tests:** Unit-Tests für alle neuen Klassen. Integrationstests für das Zusammenspiel. System-Tests für End-to-End-Szenarien.

[Implementierung](Implementierung3.md)

---

### Schritt 5: Test

Nach Abschluss der Implementierung wurden alle während der Entwicklung durchgeführten Tests als 
formale Testfälle dokumentiert. Darauf aufbauend wurden das übergeordnete Ziel des Testens, die 
geplanten Testarten sowie deren Abdeckung definiert und eine Teststrategie festgelegt.

Um die interne Codequalität sicherzustellen, wurde ein umfassendes Codereview durchgeführt. 
Der Code wurde basierend auf den Ergebnissen überarbeitet. Anschließend wurden gezielt weitere 
Testfälle ergänzt, um die vollständige Abdeckung aller Hauptanforderungen sicherzustellen.

**Testarten:**
- Unit-Tests für Validator, ErrorHandler, GrillStateMachine
- Integrationstests für das Zusammenspiel aller Komponenten
- System-Tests für End-to-End-Szenarien
- Performance-Tests zur Validierung der <500ms Anforderung
- Fehlerfall-Tests für Sensorfehler und ungültige Eingaben

[Test](Test3.md)

---

### Schritt 6: Retrospektive

**Was lief gut?**

- Alle Requirements wurden vollständig umgesetzt
- Einheitliche Validierungsstrategie erfolgreich etabliert
- Performance-Anforderungen (<500ms) erfüllt
- Deterministisches Zustandsverhalten implementiert
- Umfassende Testabdeckung erreicht
- Code-Qualität deutlich verbessert durch Refactoring

**Was lief nicht so gut?**

- Refactoring dauerte länger als geplant
- Einige Legacy-Abhängigkeiten waren schwieriger zu entfernen als erwartet
- Performance-Optimierung erforderte mehr Iteration als ursprünglich gedacht

**Was habe ich für zukünftige Projekte gelernt?**

- Einheitliche Validierungsstrategie von Anfang an etablieren spart viel Refactoring-Aufwand
- Zustandsautomaten früh explizit modellieren erleichtert spätere Erweiterungen
- Performance-Anforderungen sollten bereits in Sprint 1 berücksichtigt werden
- Umfassende Tests von Beginn an zahlen sich aus

**Lessons Learned:**

- Refactoring ist essentiell für langfristige Code-Qualität
- Zentrale Fehlerbehandlung vereinfacht Wartung und Erweiterung erheblich
- Explizite Zustandsautomaten machen Systemverhalten transparent und testbar
- Performance-Monitoring sollte kontinuierlich erfolgen, nicht erst am Ende
- Separation of Concerns ist der Schlüssel zu wartbarem Code

---

## Abweichungen

**Vergleich von Software-Architektur und -Design mit der tatsächlichen Implementierung:**

| Bereich | Geplant | Implementiert | Abweichung | Grund | Status |
|---------|---------|--------------|-----------|-------|--------|
| **Validator-Klasse** | Zentrale Validierungslogik für alle Eingaben | Validator vollständig implementiert mit einheitlichen Schnittstellen | ✅ Keine Abweichung | Wie geplant umgesetzt | ✅ Umgesetzt |
| **ErrorHandler-Klasse** | Zentrale Fehlerbehandlung mit automatischem Timeout | ErrorHandler implementiert, Timeout-Mechanismus funktioniert | ✅ Keine Abweichung | Wie geplant umgesetzt | ✅ Umgesetzt |
| **GrillStateMachine** | Deterministischer Zustandsautomat gemäß F8 | Zustandsautomat vollständig implementiert, alle Übergänge validiert | ✅ Keine Abweichung | Wie geplant umgesetzt | ✅ Umgesetzt |
| **Performance (<500ms)** | Alle Updates innerhalb 500ms | Nach Optimierung: 90% der Updates <300ms, 99% <450ms | ✅ Keine Abweichung | Performance-Ziel übertroffen | ✅ Umgesetzt |
| **GUI Refactoring** | Vollständige Entfernung der GUI-Validierungslogik | GUI-Validierung vollständig entfernt, delegiert an Validator | ✅ Keine Abweichung | Wie geplant umgesetzt | ✅ Umgesetzt |
| **Sensorfehler-Erkennung** | Erkennung von None-Werten und ungültigen Messwerten | Vollständig implementiert, inkl. Fehleranzeige "Err" | ✅ Keine Abweichung | Wie geplant umgesetzt | ✅ Umgesetzt |
| **Zustandslogik-Konsistenz** | Deterministische Zustandsübergänge ohne Race Conditions | Nach Tests: Keine Race Conditions festgestellt | ✅ Keine Abweichung | Zustandsautomat funktioniert stabil | ✅ Umgesetzt |

---

## Finales System-Review

### Code-Metriken

| Metrik | Wert |
|--------|------|
| **Anzahl Klassen** | 8 (CurrentTemperature, TargetTemperature, GrillController, PowerState, GrillGUI, Validator, ErrorHandler, GrillStateMachine) |
| **Lines of Code** | ~1200 (inkl. Kommentare) |
| **Test Coverage** | 85% |
| **Komplexität** | Durchschnittlich (zyklomatische Komplexität: 3.2) |

### Requirements-Abdeckung

Alle funktionalen Requirements (F1.1 - F7) vollständig implementiert und getestet.
Alle nicht-funktionalen Requirements (NF6.1 - NF6.6) erfüllt.

### Baseline Stand Sprint 3

**Code abgeschlossen:**
- Alle Klassen vollständig implementiert
- GUI vollständig funktional
- Fehlerbehandlung vollständig integriert
- Performance-Optimierungen abgeschlossen

**Tests bestanden:**
- Alle Unit-Tests erfolgreich
- Alle Integrationstests erfolgreich
- Alle System-Tests erfolgreich
- Performance-Tests bestätigen <500ms Anforderung

**Architektur konsistent:**
- Drei-Schicht-Architektur sauber implementiert
- Alle Komponenten lose gekoppelt
- Klare Schnittstellen zwischen allen Schichten
- Zustandsautomat deterministisch und testbar

---

## Nächste Schritte
Falls ich das Projekt noch mehr erweitern will, habe ich mir folgende Erweiterungen überlegt:
- PID-Controller für präzisere Temperaturregelung
- Datenlogging und Temperaturverlauf-Visualisierung
- Mehrere Temperaturzonen
- Timer-Funktion
- Vorheizen-Alarm
- Temperatur-Presets
