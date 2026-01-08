"""
GrillController - Controller für Elektrogrill-Steuerung (FIXED Sprint 3.1)

Verantwortlichkeiten:
- Koordiniert alle Model-Komponenten
- Berechnet Grillstatus
- BUGFIX: 10-Sekunden Timer für Auto-AUS bei Zieltemp=0
- BUGFIX: increase() aktiviert Grill NICHT
"""

from src.current_temperature import CurrentTemperature
from src.target_temperature import TargetTemperature
from src.power_state import PowerState
from src.error_handler import ErrorHandler
from src.grill_state_machine import GrillStateMachine


class GrillController:
    """
    Controller für die Elektrogrill-Steuerung.
    
    Koordiniert die drei Model-Komponenten und berechnet den aktuellen
    Grillstatus basierend auf Stromstatus, aktueller und Zieltemperatur.
    
    BUGFIX Sprint 3.1:
    - increase() aktiviert Grill NICHT
    - Zieltemp=0: 10-Sekunden Timer bis Auto-AUS
    - Temperatur stoppt bei Raumtemperatur (20°C)
    
    Attributes:
        current_temp (CurrentTemperature): Aktuelle Temperatur
        target_temp (TargetTemperature): Zieltemperatur
        power_state (PowerState): Stromstatus
        error_handler (ErrorHandler): Fehlerverwaltung
        state_machine (GrillStateMachine): Zustandsverwaltung
        _shutdown_timer (int): Counter für 10-Sekunden Timer
        _is_in_shutdown (bool): Gerade im Shutdown-Prozess?
    """
    
    # Zustände
    STATE_OFF = GrillStateMachine.STATE_OFF
    STATE_HEATING = GrillStateMachine.STATE_HEATING
    STATE_TARGET_REACHED = GrillStateMachine.STATE_TARGET_REACHED
    STATE_COOLING_DOWN = GrillStateMachine.STATE_COOLING_DOWN
    STATE_SENSOR_ERROR = GrillStateMachine.STATE_SENSOR_ERROR
    STATE_WAITING = "WAITING"  # Neuer Zustand für 10-Sekunden Wartezeit
    
    # Konstanten
    TEMP_THRESHOLD_REACHED = 2.0
    TEMP_THRESHOLD_COOLING = 50.0
    ROOM_TEMP = 20.0
    SHUTDOWN_TIMER_SECONDS = 10
    SHUTDOWN_TIMER_UPDATES = 20  # 500ms * 20 = 10 Sekunden
    
    def __init__(self):
        """Initialisiert den Controller mit allen Modellen."""
        self.current_temp = CurrentTemperature()
        self.target_temp = TargetTemperature()
        self.power_state = PowerState()
        self.error_handler = ErrorHandler()
        self.state_machine = GrillStateMachine()
        
        # Timer für 10-Sekunden Auto-AUS
        self._shutdown_timer = 0
        self._is_in_shutdown = False
    
    def update(self) -> None:
        """
        Aktualisiert den Grill-Status (wird regelmäßig aufgerufen alle 500ms).
        
        BUGFIX Sprint 3.1:
        1. Prüft auf Sensorfehler
        2. Prüft auf Shutdown-Timer (Zieltemp=0)
        3. Setzt die Zieltemperatur in CurrentTemperature
        4. Aktualisiert die aktuelle Temperatur
        """
        # Prüfe auf Sensorfehler
        if self.current_temp.has_sensor_error():
            if self.power_state.is_on():
                self.power_state.turn_off()
            return
        
        # BUGFIX: 10-Sekunden Timer für Zieltemp=0
        if self.power_state.is_on() and self.target_temp.get_target_temperature() == 0:
            self._handle_shutdown_timer()
            return
        
        # Timer zurücksetzen wenn Zieltemp nicht 0
        if self.target_temp.get_target_temperature() > 0:
            self._shutdown_timer = 0
            self._is_in_shutdown = False
        
        # Setze Zieltemperatur für Rampenfunktion
        if self.power_state.is_on():
            self.current_temp.set_target_temperature(self.target_temp.get_target_temperature())
        else:
            # Wenn Grill aus: Abkühlen auf Raumtemperatur
            self.current_temp.set_target_temperature(CurrentTemperature.ROOM_TEMP)
        
        # Aktualisiere aktuelle Temperatur
        self.current_temp.update()
    
    def _handle_shutdown_timer(self) -> None:
        """
        Handhabt den 10-Sekunden Timer für Zieltemp=0.
        
        Logik:
        - Setze Zieltemperatur auf Raumtemperatur
        - Zähle Updates
        - Nach 20 Updates (10 Sekunden): Schalte Grill aus
        """
        # Setze Zieltemperatur auf Raumtemperatur für Abkühlung
        self.current_temp.set_target_temperature(self.ROOM_TEMP)
        self.current_temp.update()
        
        # Inkrementiere Timer
        self._shutdown_timer += 1
        self._is_in_shutdown = True
        
        # Wenn Timer abgelaufen: Schalte Grill aus
        if self._shutdown_timer >= self.SHUTDOWN_TIMER_UPDATES:
            self.power_state.turn_off()
            self._shutdown_timer = 0
            self._is_in_shutdown = False
    
    # ============ Getter-Methoden für GUI ============
    
    def get_current_temperature(self) -> float:
        """
        Gibt die aktuelle Temperatur zurück.
        
        Returns:
            float: Aktuelle Temperatur in °C oder -1.0 bei Sensorfehler
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
        - OFF: Grill aus, Temperatur <= 20°C
        - HEATING: Grill an, aktuelle < Zieltemperatur
        - TARGET_REACHED: Grill an, aktuelle >= Zieltemperatur
        - COOLING_DOWN: Grill aus, aber Temperatur > 50°C
        - WAITING: Zieltemp=0, Grill AN, wartet auf Auto-AUS
        - SENSOR_ERROR: Sensorfehler erkannt
        
        Returns:
            str: Aktueller Status
        """
        # Prüfe zuerst Sensorfehler
        if self.current_temp.has_sensor_error():
            return self.STATE_SENSOR_ERROR
        
        current = self.current_temp.get_temperature()
        target = self.target_temp.get_target_temperature()
        power_on = self.power_state.is_on()
        
        # BUGFIX: Wenn Zieltemp=0 und Grill AN → WAITING Status
        if power_on and target == 0:
            # Noch Restwärme? Zeige abhängig von Temperatur
            if current > self.TEMP_THRESHOLD_COOLING:
                return self.STATE_COOLING_DOWN  # Noch heiß, abkühlen
            else:
                return self.STATE_WAITING  # Bei Raumtemperatur, wartet auf AUS
        
        # Normale Logik
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
        
        Returns:
            bool: True wenn Zieltemperatur erreicht
        """
        if not self.power_state.is_on():
            return False
        
        if self.current_temp.has_sensor_error():
            return False
        
        if self.target_temp.get_target_temperature() == 0:
            return False
        
        current = self.current_temp.get_temperature()
        target = self.target_temp.get_target_temperature()
        
        return abs(current - target) < self.TEMP_THRESHOLD_REACHED
    
    def is_cooling_down(self) -> bool:
        """
        Prüft ob der Grill gerade abkühlt.
        
        Returns:
            bool: True wenn abkühlung aktiv
        """
        if self.power_state.is_on():
            return False
        
        if self.current_temp.has_sensor_error():
            return False
        
        current = self.current_temp.get_temperature()
        return current > self.TEMP_THRESHOLD_COOLING
    
    def is_waiting(self) -> bool:
        """
        Prüft ob Grill im WAITING Status ist (Zieltemp=0, bei Raumtemp).
        
        Returns:
            bool: True wenn wartet
        """
        return self.get_status() == self.STATE_WAITING
    
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
        
        # BUGFIX: Timer zurücksetzen bei neuer Zieltemperatur
        if value > 0:
            self._shutdown_timer = 0
            self._is_in_shutdown = False
    
    def increase_target_temperature(self, delta: float = 10.0) -> None:
        """
        Erhöht die Zieltemperatur um delta.
        
        BUGFIX Sprint 3.1:
        - Aktiviert Grill NICHT automatisch!
        - Nur Zieltemperatur erhöhen
        
        Args:
            delta (float): Erhöhungsbetrag in °C
            
        Raises:
            ValueError: Wenn Resultat ungültig
        """
        self.target_temp.increase(delta)
        
        # BUGFIX: Grill wird NICHT automatisch aktiviert!
        # Nur die Zieltemperatur wird erhöht
        # Der Grill bleibt in seinem aktuellen Status
    
    def decrease_target_temperature(self, delta: float = 10.0) -> None:
        """
        Senkt die Zieltemperatur um delta.
        
        Args:
            delta (float): Senkungsbetrag in °C
        """
        self.target_temp.decrease(delta)
    
    def toggle_power(self) -> None:
        """
        Toggled den Stromstatus des Grills.
        
        Ändert NICHT die Zieltemperatur.
        """
        self.power_state.toggle_power()
        
        # Timer zurücksetzen beim Ausschalten
        if not self.power_state.is_on():
            self._shutdown_timer = 0
            self._is_in_shutdown = False
    
    def trigger_sensor_error(self) -> None:
        """Triggert einen Sensorfehler (für Testing)."""
        self.current_temp.trigger_sensor_error()
        self.error_handler.add_error(
            error_type=self.error_handler.ERROR_TYPE_SENSOR,
            message="Sensorfehler: Temperaturanzeige fehlerhaft",
            data={"sensor": "DS18B20"}
        )
    
    def clear_sensor_error(self) -> None:
        """Löscht den Sensorfehler."""
        self.current_temp.clear_sensor_error()
        self.error_handler.clear_active_error()
    
    def has_error(self) -> bool:
        """Prüft ob ein Fehler aktiv ist."""
        return self.error_handler.has_error()
    
    def reset(self) -> None:
        """Setzt Controller auf Initialzustand zurück."""
        self.current_temp.reset()
        self.target_temp.reset()
        self.power_state.reset()
        self.error_handler.clear_errors()
        self._shutdown_timer = 0
        self._is_in_shutdown = False
