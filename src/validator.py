"""
Validator - Zentrale Validierungslogik für Elektrogrill

Verantwortlichkeiten:
- Validiert Temperaturen
- Prüft Eingaben
- Wirft standardisierte Exceptions
"""


class ValidationError(Exception):
    """Basis-Exception für Validierungsfehler."""
    pass


class TemperatureError(ValidationError):
    """Exception für ungültige Temperaturen."""
    pass


class Validator:
    """
    Zentrale Validierungslogik für den Elektrogrill.
    
    Alle Eingaben werden hier validiert, bevor sie in Models/Controller gehen.
    """
    
    # Konstanten für Validierung
    MIN_VALID_TEMP = 0.0
    MAX_VALID_TEMP = 500.0
    MIN_HEATING_TEMP = 50.0
    
    @staticmethod
    def validate_target_temperature(value: float) -> float:
        """
        Validiert eine Zieltemperatur.
        
        Erlaubte Werte:
        - 0 (Aus)
        - 50-500 (Heizen)
        
        Args:
            value (float): Zu validierende Temperatur
            
        Returns:
            float: Validierte Temperatur
            
        Raises:
            TemperatureError: Wenn ungültig
        """
        try:
            temp = float(value)
        except (ValueError, TypeError):
            raise TemperatureError(
                f"Temperatur muss eine Zahl sein, erhielt '{value}'"
            )
        
        # Erlaubt 0 (Aus) oder 50-500 (Heizen)
        if temp == Validator.MIN_VALID_TEMP:
            return temp
        
        if temp < Validator.MIN_HEATING_TEMP or temp > Validator.MAX_VALID_TEMP:
            raise TemperatureError(
                f"Temperatur muss 0 oder zwischen {Validator.MIN_HEATING_TEMP} "
                f"und {Validator.MAX_VALID_TEMP}°C sein, erhielt {temp}°C"
            )
        
        return float(temp)
    
    @staticmethod
    def validate_temperature_step(current: float, step: float) -> float:
        """
        Validiert einen Temperatur-Schritt (Erhöhung/Senkung).
        
        Args:
            current (float): Aktuelle Zieltemperatur
            step (float): Schritt in °C (positiv oder negativ)
            
        Returns:
            float: Neue Zieltemperatur
            
        Raises:
            TemperatureError: Wenn Resultat ungültig
        """
        if current == 0 and step > 0:
            # Spezial: 0°C + positive Schritte = 50°C, dann 10er-Schritte
            return Validator.MIN_HEATING_TEMP
        
        new_temp = current + step
        return Validator.validate_target_temperature(new_temp)
