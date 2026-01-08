"""
TargetTemperature - Modell für Zieltemperatur des Grills

Verantwortlichkeiten:
- Speichert die gewünschte Zieltemperatur
- Validiert Eingabewerte (50-500°C oder 0)
- Liefert Zieltemperatur an Controller
"""


class TargetTemperature:
    """
    Modelliert die Zieltemperatur des Elektrogrills.
    
    Der Benutzer kann eine Zieltemperatur zwischen 50 und 500°C setzen.
    0 bedeutet: Grill soll ausschalten.
    
    Attributes:
        _target_temp (float): Zieltemperatur in °C
    """
    
    # Konstanten
    MIN_OPERATING_TEMP = 50.0      # Minimale Betriebstemperatur
    MAX_OPERATING_TEMP = 500.0     # Maximale Betriebstemperatur
    SHUTDOWN_TEMP = 0.0            # Aus-Temperatur
    
    def __init__(self):
        """Initialisiert die Zieltemperatur auf 0 (Grill aus)."""
        self._target_temp = self.SHUTDOWN_TEMP
    
    def set_target_temperature(self, value: float) -> None:
        """
        Setzt die Zieltemperatur.
        
        Gültige Werte:
        - 0: Grill ausschalten
        - 50-500: Betriebstemperatur
        
        Args:
            value (float): Zieltemperatur in °C
            
        Raises:
            ValueError: Wenn Wert ungültig (nicht numerisch oder außerhalb Range)
            TypeError: Wenn Wert nicht zu float konvertierbar
        """
        # Validierung
        if not isinstance(value, (int, float)):
            raise TypeError(f"Temperatur muss numerisch sein, nicht {type(value).__name__}")
        
        value = float(value)
        
        # Zieltemperatur muss 0 sein oder zwischen MIN und MAX
        if value == self.SHUTDOWN_TEMP:
            self._target_temp = self.SHUTDOWN_TEMP
        elif self.MIN_OPERATING_TEMP <= value <= self.MAX_OPERATING_TEMP:
            self._target_temp = float(value)
        else:
            raise ValueError(
                f"Zieltemperatur muss 0 (Aus) oder {self.MIN_OPERATING_TEMP}-"
                f"{self.MAX_OPERATING_TEMP}°C sein, nicht {value}"
            )
    
    def get_target_temperature(self) -> float:
        """
        Gibt die aktuelle Zieltemperatur zurück.
        
        Returns:
            float: Zieltemperatur in °C
        """
        return self._target_temp
    
    def is_on(self) -> bool:
        """
        Prüft ob Grill eingeschaltet sein soll.
        
        Returns:
            bool: True wenn Zieltemperatur > 0
        """
        return self._target_temp > self.SHUTDOWN_TEMP
    
    def is_valid_value(self, value: float) -> bool:
        """
        Prüft ob ein Wert gültig ist (ohne zu setzen).
        
        Args:
            value (float): Zu prüfender Wert
            
        Returns:
            bool: True wenn gültig
        """
        try:
            value = float(value)
            return (value == self.SHUTDOWN_TEMP or 
                    (self.MIN_OPERATING_TEMP <= value <= self.MAX_OPERATING_TEMP))
        except (ValueError, TypeError):
            return False
    
    def increase(self, delta: float = 10.0) -> None:
        """
        Erhöht die Zieltemperatur um einen Delta-Betrag.
        
        Args:
            delta (float): Erhöhungsbetrag in °C (default: 10)
            
        Raises:
            ValueError: Wenn Resultat außerhalb Range
        """
        new_value = self._target_temp + delta
        self.set_target_temperature(new_value)
    
    def decrease(self, delta: float = 10.0) -> None:
        """
        Senkt die Zieltemperatur um einen Delta-Betrag.
        
        Args:
            delta (float): Senkungsbetrag in °C (default: 10)
            
        Raises:
            ValueError: Wenn Resultat außerhalb Range
        """
        new_value = self._target_temp - delta
        if new_value < self.SHUTDOWN_TEMP:
            new_value = self.SHUTDOWN_TEMP
        self.set_target_temperature(new_value)
    
    def reset(self) -> None:
        """Setzt Zieltemperatur auf 0 (Aus)."""
        self._target_temp = self.SHUTDOWN_TEMP
