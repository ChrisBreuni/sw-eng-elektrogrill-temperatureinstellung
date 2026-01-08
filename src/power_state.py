"""
PowerState - Modell für Ein-/Aus-Status des Grills

Verantwortlichkeiten:
- Speichert Stromstatus (an/aus)
- Bietet Toggle-Funktion
"""


class PowerState:
    """
    Modelliert den Stromstatus des Elektrogrills.
    
    Der Grill kann entweder eingeschaltet (True) oder ausgeschaltet (False) sein.
    
    Attributes:
        _is_on (bool): True wenn Grill eingeschaltet, False wenn aus
    """
    
    def __init__(self):
        """Initialisiert den Grill im ausgeschalteten Zustand."""
        self._is_on = False
    
    def turn_on(self) -> None:
        """Schaltet den Grill ein."""
        self._is_on = True
    
    def turn_off(self) -> None:
        """Schaltet den Grill aus."""
        self._is_on = False
    
    def toggle_power(self) -> None:
        """Schaltet den Grill um (an → aus oder aus → an)."""
        self._is_on = not self._is_on
    
    def is_on(self) -> bool:
        """
        Prüft ob Grill eingeschaltet ist.
        
        Returns:
            bool: True wenn Grill an, False wenn aus
        """
        return self._is_on
    
    def reset(self) -> None:
        """Setzt Stromstatus auf aus."""
        self._is_on = False
