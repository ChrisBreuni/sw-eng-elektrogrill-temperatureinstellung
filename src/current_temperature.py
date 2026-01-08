class CurrentTemperature:
    """
    Hält die aktuelle Temperatur (z. B. simuliert).
    -1.0 bedeutet: Sensorfehler / kein gültiger Messwert.
    """

    def __init__(self, initial: float = 20.0) -> None:
        self._temperature: float = float(initial)

    def set_temperature(self, value: float) -> None:
        self._temperature = float(value)

    def get_temperature(self) -> float:
        return self._temperature

    def is_sensor_ok(self) -> bool:
        return self._temperature >= 0.0
