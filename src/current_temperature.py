"""
CurrentTemperature - Modell für aktuelle Temperatur des Grills

Verantwortlichkeiten:
- Speichert die aktuelle Temperatur
- Simuliert Temperaturänderungen
- Erkennt Sensorfehler
- Validiert Temperaturwerte
"""


class CurrentTemperature:
    """
    Modelliert die aktuelle Temperatur des Elektrogrills.
    
    Die Temperatur startet bei 20.0°C und erhöht sich, wenn der Grill
    eingeschaltet ist (mit Rampenfunktion). Sie sinkt, wenn der Grill
    ausgeschaltet ist.
    
    Attributes:
        _current_temp (float): Aktuelle Temperatur in °C
        _target_temp (float): Zieltemperatur für Rampenfunktion
        _sensor_ok (bool): Status des Sensors (True = OK, False = Fehler)
        _heating_rate (float): Aufheizrate in °C pro Update (500ms)
        _cooling_rate (float): Abkühlrate in °C pro Update (500ms)
    """
    
    # Konstanten
    INITIAL_TEMP = 20.0
    MIN_TEMP = 0.0
    MAX_TEMP = 600.0
    SENSOR_ERROR_VALUE = -1.0
    
    # Raten für Simulation (pro 500ms Update)
    HEATING_RATE = 2.0      # °C pro Update
    COOLING_RATE = 0.5      # °C pro Update
    
    def __init__(self):
        """Initialisiert die aktuelle Temperatur."""
        self._current_temp = self.INITIAL_TEMP
        self._target_temp = self.INITIAL_TEMP
        self._sensor_ok = True
        self._heating_rate = self.HEATING_RATE
        self._cooling_rate = self.COOLING_RATE
    
    def get_temperature(self) -> float:
        """
        Gibt die aktuelle Temperatur zurück.
        
        Returns:
            float: Aktuelle Temperatur in °C, oder -1.0 bei Sensorfehler
        """
        if not self._sensor_ok:
            return self.SENSOR_ERROR_VALUE
        return self._current_temp
    
    def set_target_temperature(self, target: float) -> None:
        """
        Setzt die Zieltemperatur für die Rampenfunktion.
        
        Die aktuelle Temperatur nähert sich dieser Zieltemperatur
        bei jedem Update an (Aufheizen oder Abkühlen).
        
        Args:
            target (float): Zieltemperatur in °C
        """
        if target < self.MIN_TEMP or target > self.MAX_TEMP:
            raise ValueError(f"Temperatur muss zwischen {self.MIN_TEMP} und {self.MAX_TEMP} sein")
        self._target_temp = float(target)
    
    def update(self) -> None:
        """
        Aktualisiert die aktuelle Temperatur in Richtung Zieltemperatur.
        
        Diese Methode wird regelmäßig aufgerufen (alle 500ms).
        - Wenn Zieltemperatur höher: Aufheizen mit HEATING_RATE
        - Wenn Zieltemperatur niedriger: Abkühlen mit COOLING_RATE
        - Wenn erreicht: Bleibe auf Zieltemperatur
        """
        if not self._sensor_ok:
            return
        
        diff = self._target_temp - self._current_temp
        
        if diff > 0:
            # Aufheizen
            self._current_temp += min(self._heating_rate, diff)
        elif diff < 0:
            # Abkühlen
            self._current_temp -= min(self._cooling_rate, abs(diff))
        
        # Sicherstelle dass Grenzen nicht überschritten
        self._current_temp = max(self.MIN_TEMP, min(self._current_temp, self.MAX_TEMP))
    
    def is_sensor_ok(self) -> bool:
        """
        Prüft ob der Sensor OK ist.
        
        Returns:
            bool: True wenn Sensor OK, False bei Fehler
        """
        return self._sensor_ok
    
    def trigger_sensor_error(self) -> None:
        """Triggered einen Sensorfehler (für Testing)."""
        self._sensor_ok = False
    
    def clear_sensor_error(self) -> None:
        """Hebt einen Sensorfehler auf (für Testing)."""
        self._sensor_ok = True
    
    def reset(self) -> None:
        """Setzt die Temperatur auf Initialwert zurück."""
        self._current_temp = self.INITIAL_TEMP
        self._target_temp = self.INITIAL_TEMP
        self._sensor_ok = True
