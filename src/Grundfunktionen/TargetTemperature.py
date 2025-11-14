"""
TargetTemperature.py
Basisklasse zur Verwaltung, Validierung und Anzeige der Wunschtemperatur.
Zieltemperatur darf 0 sein oder im Bereich 50–500 °C liegen.
"""

class TargetTemperature:
    def __init__(self, initial_target_temp: float = 0.0, min_target_temp: float = 50.0, max_target_temp: float = 500.0):
        """
        initial_target_temp: Start-Wunschtemperatur (0 = deaktiviert)
        min_target_temp: minimale erlaubte Zieltemperatur (außer 0)
        max_target_temp: maximale erlaubte Zieltemperatur
        """
        self._min_target_temp = min_target_temp
        self._max_target_temp = max_target_temp
        self._target_temp = 0.0
        self.set(initial_target_temp)

    def set(self, new_target_temp: float):
        """
        Setzt eine neue Zieltemperatur.
        Valid: 0 oder min_target_temp <= value <= max_target_temp.
        """
        if not self._is_valid(new_target_temp):
            raise ValueError(
                f"Ungültige Zieltemperatur: {new_target_temp} °C "
                f"(erlaubt: 0 oder {self._min_target_temp}–{self._max_target_temp})"
            )
        self._target_temp = new_target_temp

    def _is_valid(self, value: float) -> bool:
        """Interne Prüfung der zulässigen Zieltemperatur."""
        if value == 0:
            return True
        return self._min_target_temp <= value <= self._max_target_temp

    def get(self) -> float:
        """Gibt die aktuelle Zieltemperatur zurück."""
        return self._target_temp

    def is_active(self) -> bool:
        """Gibt zurück, ob eine Zieltemperatur gesetzt ist (≠ 0)."""
        return self._target_temp != 0

    def format_display(self) -> str:
        """Aufbereitete Darstellung für spätere Anzeige."""
        if self._target_temp == 0:
            return "Wunschtemperatur: AUS"
        return f"Wunschtemperatur: {self._target_temp:.1f} °C"

    def __repr__(self):
        return f"TargetTemperature({self._target_temp} °C)"
