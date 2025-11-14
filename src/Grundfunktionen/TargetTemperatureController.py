"""
TargetTemperatureController.py
Controller-Klasse zur Steuerung der Zieltemperatur-Logik.
Verknüpft CurrentTemperature und TargetTemperature und liefert klare Aktionen
für Regelung, Logging oder UI-Logik.
"""

from TargetTemperature import TargetTemperature
from CurrentTemperature import CurrentTemperature


class TargetTemperatureController:
    """
    Steuert die Zieltemperatur relativ zur aktuellen Temperatur.
    Verantwortlichkeiten:
    - Solltemperatur setzen, erhöhen, senken
    - Überwachung, ob Zieltemperatur erreicht / überschritten wird
    - Bereitstellen klarer Statusinformationen für Regelung/Heizelement
    """

    def __init__(self,
                 current_temp: CurrentTemperature,
                 target_temp: TargetTemperature,
                 tolerance: float = 2.0):
        """
        current_temp: Instanz von CurrentTemperature
        target_temp: Instanz von TargetTemperature
        tolerance: Temperaturband, ab dem "erreicht" gilt
        """
        self.current_temp = current_temp
        self.target_temp = target_temp
        self.tolerance = max(0.2, float(tolerance))


    def set_target(self, value: float) -> None:
        """Setzt eine neue Solltemperatur."""
        self.target_temp.set(value)

    def increase(self, step: float = 5.0) -> None:
        """Erhöht die Solltemperatur um einen Schritt."""
        if not self.target_temp.is_active():
            self.target_temp.set(step)
            return
        new_value = self.target_temp.get() + step
        self.target_temp.set(new_value)

    def decrease(self, step: float = 5.0) -> None:
        """Verringert die Solltemperatur um einen Schritt."""
        if not self.target_temp.is_active():
            return
        new_value = max(0, self.target_temp.get() - step)
        self.target_temp.set(new_value)

    def turn_off(self) -> None:
        """Deaktiviert die Zieltemperatur."""
        self.target_temp.set(0)

    def is_reached(self) -> bool:
        """
        Prüft, ob die aktuelle Temperatur nahe genug an der Solltemperatur ist.
        """
        if not self.target_temp.is_active():
            return False
        return abs(self.current_temp.get() - self.target_temp.get()) <= self.tolerance

    def needs_heating(self) -> bool:
        """
        Liefert True, wenn der Grill heizen sollte.
        """
        if not self.target_temp.is_active():
            return False
        return self.current_temp.get() < self.target_temp.get() - self.tolerance

    def needs_cooling(self) -> bool:
        """
        Liefert True, wenn der Grill eher zu heiß ist.
        """
        if not self.target_temp.is_active():
            return False
        return self.current_temp.get() > self.target_temp.get() + self.tolerance

    def get_status(self) -> str:
        """
        Kompakter Statusstring für UI, Logging etc.
        """
        if not self.target_temp.is_active():
            return "Status: Solltemperatur AUS"

        ct = self.current_temp.get()
        tt = self.target_temp.get()

        if self.is_reached():
            return f"Status: Ziel erreicht ({ct:.1f}/{tt:.1f} °C)"
        if self.needs_heating():
            return f"Status: Heizen ({ct:.1f} → {tt:.1f} °C)"
        if self.needs_cooling():
            return f"Status: Zu heiß ({ct:.1f} > {tt:.1f} °C)"

        return f"Status: Stabil ({ct:.1f}/{tt:.1f} °C)"

    def __repr__(self):
        return f"TargetTemperatureController(target={self.target_temp}, tolerance={self.tolerance})"
