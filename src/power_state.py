class PowerState:
    """
    Ein/Aus-Zustand des Grills.
    """

    def __init__(self) -> None:
        self._is_on: bool = False

    def turn_on(self) -> None:
        self._is_on = True

    def turn_off(self) -> None:
        self._is_on = False

    def toggle_power(self) -> None:
        self._is_on = not self._is_on

    def is_on(self) -> bool:
        return self._is_on
