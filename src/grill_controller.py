"""
GrillController - Controller für Elektrogrill-Steuerung

Verantwortlichkeiten:
- Koordiniert alle Model-Komponenten (CurrentTemp, TargetTemp, PowerState)
- Berechnet Grillstatus (OFF, AUFHEIZEN, ZIEL ERREICHT, ABKÜHLUNG, FEHLER)
- Simuliert Temperaturänderungen
- Schnittstelle für GUI
"""

from src.current_temperature import CurrentTemperature
from src.target_temperature import TargetTemperature
from src.power_state import PowerState


class GrillController:
    """
    Controller für die Elektrogrill-Steuerung.
    
    Koordiniert die drei Model-Komponenten und berechnet den aktuellen
    Grillstatus basierend auf Stromstatus, aktueller und Zieltemperatur.
    
    Attributes:
        current_temp (CurrentTemperature): Aktuelle Temperatur
        target_temp (TargetTemperature): Zieltemperatur
        power_state (PowerState): Stromstatus
    """
    
    # Zustände
    STATE_OFF = "OFF"
    STATE_HEATING = "HEATING"
    STATE_TARGET_REACHED = "TARGET_REACHED"
    STATE_COOLING_DOWN = "COOLING_DOWN"
    STATE_SENSOR_ERROR = "SENSOR_ERROR"
    
    # Konstanten
    TEMP_THRESHOLD_REACHED = 2.0  # Zieltemperatur als erreicht gelten wenn diff < 2°C
    TEMP_THRESHOLD_COOLING = 50.0  # Abkühlung aktiv wenn > 50°C
    
    def __init__(self):
        """Initialisiert den Controller mit allen Modellen."""
        self.current_temp = CurrentTemperature()
        self.target_temp = TargetTemperature()
        self.power_state = PowerState()
    
    def update(self) -> None:
        """
        Aktualisiert den Grill-Status (wird regelmäßig aufgerufen).
        
        Diese Methode sollte alle 500ms aufgerufen werden.
        Sie:
        1. Setzt die Zieltemperatur in CurrentTemperature
        2. Aktualisiert die aktuelle Temperatur
        """
        # Setze Zieltemperatur für Rampenfunktion
        if self.power_state.is_on():
            # Wenn Grill an: Zieltemperatur vom Benutzer
            self.current_temp.set_target_temperature(self.target_temp.get_target_temperature())
        else:
            # Wenn Grill aus: Abkühlen auf 20°C
            self.current_temp.set_target_temperature(CurrentTemperature.INITIAL_TEMP)
        
        # Aktualisiere aktuelle Temperatur (nähert sich Zieltemperatur)
        self.current_temp.update()
    
    # ============ Getter-Methoden für GUI ============
    
    def get_current_temperature(self) -> float:
        """
        Gibt die aktuelle Temperatur zurück.
        
        Returns:
            float: Aktuelle Temperatur in °C (oder -1.0 bei Sensorfehler)
        """
        return self.current_temp.get_temperature()
    
    def get_target_temperature(self) -> float:
        """
        Gibt die Zieltemperatur zurück.
        
        Returns:
            float: Zieltemperatur in °C
        """
        return self.target_temp.get_target_temperature()
    
    def get_status(self) -> str:
        """
        Berechnet und gibt den aktuellen Grillstatus zurück.
        
        Mögliche Zustände:
        - OFF: Grill aus, Temperatur < 50°C
        - HEATING: Grill an, aktuelle < Zieltemperatur
        - TARGET_REACHED: Grill an, aktuelle >= Zieltemperatur
        - COOLING_DOWN: Grill aus, aber Temperatur > 50°C
        - SENSOR_ERROR: Sensorfehler erkannt
        
        Returns:
            str: Aktueller Status
        """
        # Prüfe Sensorfehler zuerst
        if not self.current_temp.is_sensor_ok():
            return self.STATE_SENSOR_ERROR
        
        current = self.current_temp.get_temperature()
        target = self.target_temp.get_target_temperature()
        power_on = self.power_state.is_on()
        
        # Prüfe Zustände
        if power_on:
            # Grill ist eingeschaltet
            if abs(current - target) < self.TEMP_THRESHOLD_REACHED:
                return self.STATE_TARGET_REACHED
            elif current < target:
                return self.STATE_HEATING
            else:
                return self.STATE_TARGET_REACHED
        else:
            # Grill ist ausgeschaltet
            if current > self.TEMP_THRESHOLD_COOLING:
                return self.STATE_COOLING_DOWN
            else:
                return self.STATE_OFF
    
    def is_target_reached(self) -> bool:
        """
        Prüft ob Zieltemperatur erreicht ist.
        
        Zieltemperatur gilt als erreicht wenn:
        - Grill an ist
        - Aktuelle Temperatur >= Zieltemperatur - THRESHOLD
        
        Returns:
            bool: True wenn Zieltemperatur erreicht
        """
        if not self.power_state.is_on():
            return False
        
        current = self.current_temp.get_temperature()
        target = self.target_temp.get_target_temperature()
        
        return abs(current - target) < self.TEMP_THRESHOLD_REACHED
    
    def is_cooling_down(self) -> bool:
        """
        Prüft ob der Grill gerade abkühlt.
        
        Abkühlung ist aktiv wenn:
        - Grill aus ist
        - Aktuelle Temperatur > THRESHOLD_COOLING
        
        Returns:
            bool: True wenn abkühlung aktiv
        """
        if self.power_state.is_on():
            return False
        
        current = self.current_temp.get_temperature()
        return current > self.TEMP_THRESHOLD_COOLING
    
    # ============ Setter-Methoden für GUI ============
    
    def set_target_temperature(self, value: float) -> None:
        """
        Setzt die Zieltemperatur.
        
        Args:
            value (float): Zieltemperatur in °C (0 oder 50-500)
            
        Raises:
            ValueError: Wenn Wert ungültig
        """
        self.target_temp.set_target_temperature(value)
        
        # Wenn Zieltemperatur > 0 und Grill aus: schalte ein
        if value > 0 and not self.power_state.is_on():
            self.power_state.turn_on()
        
        # Wenn Zieltemperatur = 0: schalte aus
        if value == 0:
            self.power_state.turn_off()
    
    def increase_target_temperature(self, delta: float = 10.0) -> None:
        """
        Erhöht die Zieltemperatur um delta.
        
        Args:
            delta (float): Erhöhungsbetrag in °C
            
        Raises:
            ValueError: Wenn Resultat ungültig
        """
        self.target_temp.increase(delta)
        
        # Wenn neu >= 50: schalte ein
        if self.target_temp.get_target_temperature() >= 50:
            self.power_state.turn_on()
    
    def decrease_target_temperature(self, delta: float = 10.0) -> None:
        """
        Senkt die Zieltemperatur um delta.
        
        Args:
            delta (float): Senkungsbetrag in °C
        """
        self.target_temp.decrease(delta)
        
        # Wenn nun = 0: schalte aus
        if self.target_temp.get_target_temperature() == 0:
            self.power_state.turn_off()
    
    def reset(self) -> None:
        """Setzt Controller auf Initialzustand zurück."""
        self.current_temp.reset()
        self.target_temp.reset()
        self.power_state.reset()
