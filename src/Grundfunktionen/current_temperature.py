"""
current_temperature.py
Basisklasse zur Erfassung, Validierung und Anzeige der aktuellen Temperatur.
"""

class CurrentTemperature:
    def __init__(self, initial_temp: float = 20.0, min_temp: float = 0.0, max_temp: float = 500.0):
        """
        initial_temp: Starttemperatur
        min_temp: minimal erwarteter Sensorwert
        max_temp: maximal erwarteter Sensorwert
        """
        self._temperature = initial_temp
        self._min_temp = min_temp
        self._max_temp = max_temp

    def update(self, new_value: float):
        """
        Aktualisiert die aktuelle Temperatur (z. B. vom Sensor).
        Führt eine Grundvalidierung durch.
        """
        if not self._is_valid(new_value):
            raise ValueError(f"Ungültige Temperatur: {new_value} °C")
        self._temperature = new_value

    def _is_valid(self, value: float) -> bool:
        """Interne Plausibilitätsprüfung."""
        return self._min_temp <= value <= self._max_temp

    def get(self) -> float:
        """Gibt die aktuelle Temperatur zurück."""
        return self._temperature

    def is_overheated(self, limit: float) -> bool:
        """
        Prüft, ob eine Temperaturgrenze überschritten wurde.
        Beispiel: limit = 500 °C.
        """
        return self._temperature > limit

    def format_display(self) -> str:
        """Bereitet die Temperatur für die Anzeige auf einem Display/UI auf."""
        return f"Aktuelle Temperatur: {self._temperature:.1f} °C"

    def __repr__(self):
        """Technical string representation für Debug-Ausgaben."""
        return f"CurrentTemperature({self._temperature} °C)"
