"""
CurrentTemperature - Modell für aktuelle Temperatur des Grills (FIXED)

Verantwortlichkeiten:
- Speichert die aktuelle Temperatur
- Simuliert Temperaturänderungen
- BUGFIX: Temperatur sinkt nur bis auf Raumtemperatur (20°C)
- Sensorfehler-Simulation (Sprint 3)
"""


class CurrentTemperature:
    """
    Modelliert die aktuelle Temperatur des Elektrogrills.
    
    Die Temperatur startet bei 20.0°C und erhöht sich, wenn der Grill
    eingeschaltet ist (mit Rampenfunktion). Sie sinkt, wenn der Grill
    ausgeschaltet ist.
    
    BUGFIX Sprint 3:
    - Temperatur sinkt NICHT unter Raumtemperatur (20°C)
    
    Attributes:
        _current_temp (float): Aktuelle Temperatur in °C
        _target_temp (float): Zieltemperatur für Rampenfunktion
        _heating_rate (float): Aufheizrate in °C pro Update (500ms)
        _cooling_rate (float): Abkühlrate in °C pro Update (500ms)
        _sensor_error (bool): Sensorfehler aktiv?
    """
    
    # Konstanten
    INITIAL_TEMP = 20.0
    ROOM_TEMP = 20.0        # Raumtemperatur (Minimum)
    MIN_TEMP = 0.0
    MAX_TEMP = 600.0
    SENSOR_ERROR_VALUE = -1.0
    
    # Raten für Simulation (pro 500ms Update)
    HEATING_RATE = 2.0
    COOLING_RATE = 0.5
    
    def __init__(self):
        """Initialisiert die aktuelle Temperatur."""
        self._current_temp = self.INITIAL_TEMP
        self._target_temp = self.INITIAL_TEMP
        self._heating_rate = self.HEATING_RATE
        self._cooling_rate = self.COOLING_RATE
        self._sensor_error = False
    
    def get_temperature(self) -> float:
        """
        Gibt die aktuelle Temperatur zurück.
        
        Returns:
            float: Aktuelle Temperatur in °C oder -1.0 bei Sensorfehler
        """
        if self._sensor_error:
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
        
        BUGFIX Sprint 3:
        - Temperatur stoppt bei Raumtemperatur (20°C), nicht darunter!
        
        Sensorfehler blockieren Updates.
        """
        # Wenn Sensorfehler: nicht updaten
        if self._sensor_error:
            return
        
        diff = self._target_temp - self._current_temp
        
        if diff > 0:
            # Aufheizen
            self._current_temp += min(self._heating_rate, diff)
        elif diff < 0:
            # Abkühlen - aber NICHT unter Raumtemperatur!
            self._current_temp -= min(self._cooling_rate, abs(diff))
            # BUGFIX: Stoppe bei Raumtemperatur
            if self._current_temp < self.ROOM_TEMP:
                self._current_temp = self.ROOM_TEMP
        
        # Sicherstelle dass Grenzen nicht überschritten
        self._current_temp = max(self.MIN_TEMP, min(self._current_temp, self.MAX_TEMP))
    
    def trigger_sensor_error(self) -> None:
        """Triggert einen Sensorfehler."""
        self._sensor_error = True
    
    def clear_sensor_error(self) -> None:
        """Löscht den Sensorfehler."""
        self._sensor_error = False
    
    def has_sensor_error(self) -> bool:
        """
        Prüft ob Sensorfehler aktiv ist.
        
        Returns:
            bool: True wenn Sensorfehler
        """
        return self._sensor_error
    
    def reset(self) -> None:
        """Setzt die Temperatur auf Initialwert zurück."""
        self._current_temp = self.INITIAL_TEMP
        self._target_temp = self.INITIAL_TEMP
        self._sensor_error = False
