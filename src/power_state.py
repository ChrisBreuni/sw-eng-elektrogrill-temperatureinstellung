"""
PowerState - Modell für Stromstatus des Grills

Verantwortlichkeiten:
- Speichert den Stromstatus (AN/AUS)
- Toggle-Funktion
"""


class PowerState:
    """
    Modelliert den Stromstatus des Elektrogrills.
    
    Attributes:
        _is_on (bool): Ist der Grill eingeschaltet?
    """
    
    def __init__(self):
        """Initialisiert den Stromstatus (AUS)."""
        self._is_on = False
    
    def is_on(self) -> bool:
        """
        Prüft ob der Grill eingeschaltet ist.
        
        Returns:
            bool: True wenn eingeschaltet
        """
        return self._is_on
    
    def turn_on(self) -> None:
        """Schaltet den Grill ein."""
        self._is_on = True
    
    def turn_off(self) -> None:
        """Schaltet den Grill aus."""
        self._is_on = False
    
    def toggle_power(self) -> None:
        """Toggled den Stromstatus (AN ↔ AUS)."""
        self._is_on = not self._is_on
    
    def reset(self) -> None:
        """Setzt auf Initialzustand (AUS) zurück."""
        self._is_on = False
