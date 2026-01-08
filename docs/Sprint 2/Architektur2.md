# Architektur Sprint 2

## Architekturmuster festlegen

**Schichtenarchitektur (MVC)**:

- Trennung der Verantwortlichkeiten (Benutzeroberfläche, Steuerungslogik und Datenmodell)
- Jede Schicht ist unabhängig testbar und austauschbar
- Komponenten nach funktionaler Rolle gruppiert → Kapselung und Entkopplung
- Jede Schicht darf nur die direkt darunterliegende Schicht ansprechen
- GUI-Schicht kommuniziert über Controller mit Datenmodell

## Komponentendiagramm

![Komponentendiagramm Sprint 2](../referenziert/Architektur/Komponentendiagramm_Sprint2.png)

| **Komponente**       | **Requirements**                      |
|----------------------|---------------------------------------|
| Benutzeroberfläche   | F1.3, F6, F7, NF6.2, NF6.5, NF6.6     |
| Grillsteuerung       | F1.1, F1.2, F2, F3, F4, F5, NF6.3     |
| Temperaturmodell     | F1.1, F1.2, F2, F4                    |

**Verantwortlichkeiten der Komponenten:**

| **Komponente**       | **Rolle**              | **Verantwortlichkeiten**                                                    |
|----------------------|------------------------|-----------------------------------------------------------------------------|
| Benutzeroberfläche   | Präsentationsschicht   | Anzeige von Temperaturen und Status, Nutzerinteraktion, Live-Updates       |
| Grillsteuerung       | Business-Logik         | Statusberechnung, Koordination, Vermittlung zwischen GUI und Modell        |
| Temperaturmodell     | Datenmodell            | Speicherung von Ziel- und aktueller Temperatur, Verwaltung Power-State     |

## Schnittstellendefinition

| **Ziel**             | **Quelle**           | **Schnittstellen**                                                                          |
|----------------------|----------------------|---------------------------------------------------------------------------------------------|
| Benutzeroberfläche   | Grillsteuerung       | `get_current_temperature()`, `get_target_temperature()`, `set_target_temperature()`, `is_target_reached()`, `is_cooling_down()`, `turn_on()`, `turn_off()` |
| Grillsteuerung       | Temperaturmodell     | `set_target_temperature()`, `get_target_temperature()`, `get_current_temperature()`, `turn_on()`, `turn_off()`, `is_on()` |

## Technologiestack

| Kategorie                | Technologie / Tool   | Begründung                                                               |
|--------------------------|----------------------|--------------------------------------------------------------------------|
| Sprache                  | Python 3.x           | Requirements-Vorgabe                                                     |
| GUI-Framework            | Tkinter              | Requirements-Vorgabe (NF6.2), Standard-GUI für Python                    |
| Versionskontrolle        | Git + GitHub         | Standard                                                                 |
| IDE                      | VS Code / PyCharm    | Python-Support, Tkinter-Vorschau                                         |
| Test-Framework           | unittest / pytest    | Standard für Python, GUI-Tests mit Mock-Objekten                         |
| Dokumentation            | Markdown + PlantUML  | Für Anforderungen & Architektur, einfache Modellierung                   |
