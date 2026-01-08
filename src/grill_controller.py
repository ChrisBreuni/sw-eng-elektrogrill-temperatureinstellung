from src.current_temperature import CurrentTemperature
from src.target_temperature import TargetTemperature
from src.power_state import PowerState


class GrillController:
    """
    Kernlogik des Elektrogrills für Sprint 1:
    - Wunschtemperatur verwalten
    - aktuelle Temperatur halten
    - einfachen Status bestimmen
    - Sensorfehler als -1.0 codieren
    """

    def __init__(self) -> None:
        self.target_temp = TargetTemperature()
        self.current_temp = CurrentTemperature()
        self.power_state = PowerState()

    # --- Temperatur-API ---

    def set_target_temperature(self, value: float) -> None:
        """
        Setzt die Zieltemperatur.
        0 => Grill aus.
        """
        self.target_temp.set_temperature(value)
        if value == 0.0:
            self.power_state.turn_off()
        else:
            self.power_state.turn_on()

    def get_target_temperature(self) -> float:
        return self.target_temp.get_temperature()

    def set_current_temperature(self, value: float) -> None:
        """
        Setzt die aktuelle Temperatur.
        -1.0 => Sensorfehler.
        """
        self.current_temp.set_temperature(value)

    def get_current_temperature(self) -> float:
        return self.current_temp.get_temperature()

    # --- Status-Logik ---

    def is_target_reached(self) -> bool:
        """
        Ziel erreicht, wenn aktuelle Temperatur >= Zieltemperatur
        und Zieltemperatur > 0 und Sensor ok.
        """
        if not self.current_temp.is_sensor_ok():
            return False

        tgt = self.target_temp.get_temperature()
        cur = self.current_temp.get_temperature()
        return tgt > 0 and cur >= tgt

    def is_cooling_down(self) -> bool:
        """
        Grill kühlt ab, wenn ausgeschaltet und noch Resttemperatur > 50 °C
        (Sensor muss ok sein).
        """
        if not self.current_temp.is_sensor_ok():
            return False
        return (not self.power_state.is_on()) and self.current_temp.get_temperature() > 50.0

    def get_status(self) -> str:
        """
        Einfache Statusstrings für Sprint 1.
        """
        if not self.current_temp.is_sensor_ok():
            return "SENSOR_ERROR"

        if not self.power_state.is_on():
            if self.is_cooling_down():
                return "COOLING_DOWN"
            return "OFF"

        if self.is_target_reached():
            return "TARGET_REACHED"
        return "HEATING"
