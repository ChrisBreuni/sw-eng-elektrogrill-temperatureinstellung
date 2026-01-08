class TargetTemperature:
    """
    Speichert und verwaltet die Wunschtemperatur des Grills.
    Validierung: 50–500 °C, 0 = „nicht gesetzt / aus“.
    """

    def __init__(self, initial: float = 0.0) -> None:
        self._temperature: float = float(initial)

    def _validate(self, value: float) -> None:
        v = float(value)
        if v == 0.0:
            return
        if v < 50.0 or v > 500.0:
            raise ValueError("Zieltemperatur muss zwischen 50 und 500 °C liegen oder 0 sein.")

    def set_temperature(self, value: float) -> None:
        self._validate(value)
        self._temperature = float(value)

    def get_temperature(self) -> float:
        return self._temperature
