"""
TargetTemperature - Modell für Zieltemperatur des Grills (FIXED)

Verantwortlichkeiten:
- Speichert die Zieltemperatur
- Validiert Eingaben
- Erhöhen/Senken mit spezieller 0°C Logik
- BUGFIX: increase() aktiviert Grill NICHT
"""

from src.validator import Validator, TemperatureError


class TargetTemperature:
    """
    Modelliert die Zieltemperatur des Elektrogrills.
    
    Validiert alle Eingaben über die Validator-Klasse.
    
    BUGFIX Sprint 3: increase() aktiviert Grill NICHT automatisch
    
    Attributes:
        _target_temp (float): Aktuelle Zieltemperatur in °C
    """
    
    # Konstanten
    INITIAL_TEMP = 0.0
    
    def __init__(self):
        """Initialisiert die Zieltemperatur."""
        self._target_temp = self.INITIAL_TEMP
    
    def get_target_temperature(self) -> float:
        """
        Gibt die Zieltemperatur zurück.
        
        Returns:
            float: Zieltemperatur in °C
        """
        return self._target_temp
    
    def set_target_temperature(self, value: float) -> None:
        """
        Setzt die Zieltemperatur.
        
        Validiert den Wert über die Validator-Klasse.
        
        Args:
            value (float): Neue Zieltemperatur
            
        Raises:
            TemperatureError: Wenn ungültig
        """
        validated_temp = Validator.validate_target_temperature(value)
        self._target_temp = validated_temp
    
    def increase(self, delta: float = 10.0) -> None:
        """
        Erhöht die Zieltemperatur um delta.
        
        BUGFIX Sprint 3:
        - 0°C + delta: springe auf 50°C (aber aktiviere Grill NICHT!)
        - Sonst: normale Erhöhung um delta
        
        WICHTIG: Diese Methode ändert NICHT den Grill-Status!
        Das ist Aufgabe von grill_controller.py
        
        Args:
            delta (float): Erhöhungsbetrag in °C
            
        Raises:
            TemperatureError: Wenn Resultat ungültig
        """
        new_temp = Validator.validate_temperature_step(self._target_temp, delta)
        self._target_temp = new_temp
    
    def decrease(self, delta: float = 10.0) -> None:
        """
        Senkt die Zieltemperatur um delta.
        
        Args:
            delta (float): Senkungsbetrag in °C (positiv)
            
        Raises:
            TemperatureError: Wenn Resultat ungültig
        """
        negative_delta = -abs(delta)
        new_temp = Validator.validate_temperature_step(self._target_temp, negative_delta)
        self._target_temp = new_temp
    
    def reset(self) -> None:
        """Setzt auf Initialwert zurück."""
        self._target_temp = self.INITIAL_TEMP
