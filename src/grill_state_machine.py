"""
GrillStateMachine - Deterministische Zustandsverwaltung für Elektrogrill

Verantwortlichkeiten:
- Definiert alle gültigen Zustände
- Definiert gültige Zustandsübergänge
- Prüft Zustandsübergänge
"""


class GrillStateMachine:
    """
    Implementiert die Zustandsmachine für den Elektrogrill.
    
    Definiert alle Zustände und gültigen Übergänge zwischen ihnen.
    
    Zustände:
    - OFF: Grill aus, Temperatur niedrig (<50°C)
    - HEATING: Grill an, Temperatur < Zieltemperatur
    - TARGET_REACHED: Grill an, Temperatur >= Zieltemperatur
    - COOLING_DOWN: Grill aus, aber Temperatur hoch (>50°C)
    - SENSOR_ERROR: Sensorfehler erkannt (Sprint 3)
    """
    
    # Zustände
    STATE_OFF = "OFF"
    STATE_HEATING = "HEATING"
    STATE_TARGET_REACHED = "TARGET_REACHED"
    STATE_COOLING_DOWN = "COOLING_DOWN"
    STATE_SENSOR_ERROR = "SENSOR_ERROR"
    
    # Alle gültigen Zustände
    ALL_STATES = [
        STATE_OFF,
        STATE_HEATING,
        STATE_TARGET_REACHED,
        STATE_COOLING_DOWN,
        STATE_SENSOR_ERROR,
    ]
    
    # Gültige Zustandsübergänge
    # Aus welchem Zustand kann man in welche Zustände übergehen?
    VALID_TRANSITIONS = {
        STATE_OFF: [
            STATE_HEATING,
            STATE_COOLING_DOWN,
            STATE_SENSOR_ERROR,
        ],
        STATE_HEATING: [
            STATE_TARGET_REACHED,
            STATE_OFF,
            STATE_COOLING_DOWN,
            STATE_SENSOR_ERROR,
        ],
        STATE_TARGET_REACHED: [
            STATE_HEATING,
            STATE_OFF,
            STATE_COOLING_DOWN,
            STATE_SENSOR_ERROR,
        ],
        STATE_COOLING_DOWN: [
            STATE_OFF,
            STATE_HEATING,
            STATE_SENSOR_ERROR,
        ],
        STATE_SENSOR_ERROR: [
            STATE_OFF,
            STATE_HEATING,
            STATE_TARGET_REACHED,
            STATE_COOLING_DOWN,
        ],
    }
    
    @staticmethod
    def is_valid_state(state: str) -> bool:
        """
        Prüft ob ein Zustand gültig ist.
        
        Args:
            state (str): Zu prüfender Zustand
            
        Returns:
            bool: True wenn gültig
        """
        return state in GrillStateMachine.ALL_STATES
    
    @staticmethod
    def is_valid_transition(from_state: str, to_state: str) -> bool:
        """
        Prüft ob ein Zustandsübergang gültig ist.
        
        Args:
            from_state (str): Aktueller Zustand
            to_state (str): Zielzustand
            
        Returns:
            bool: True wenn Übergang erlaubt
        """
        if from_state not in GrillStateMachine.VALID_TRANSITIONS:
            return False
        
        return to_state in GrillStateMachine.VALID_TRANSITIONS[from_state]
    
    @staticmethod
    def get_valid_next_states(current_state: str) -> list:
        """
        Gibt alle gültigen nächsten Zustände zurück.
        
        Args:
            current_state (str): Aktueller Zustand
            
        Returns:
            list: Liste gültiger nächster Zustände
        """
        return GrillStateMachine.VALID_TRANSITIONS.get(current_state, [])
    
    @staticmethod
    def is_error_state(state: str) -> bool:
        """
        Prüft ob ein Zustand ein Fehlerzustand ist.
        
        Args:
            state (str): Zu prüfender Zustand
            
        Returns:
            bool: True wenn Fehlerzustand
        """
        return state == GrillStateMachine.STATE_SENSOR_ERROR
    
    @staticmethod
    def is_operational_state(state: str) -> bool:
        """
        Prüft ob ein Zustand ein operativer Zustand ist (kein Fehler).
        
        Args:
            state (str): Zu prüfender Zustand
            
        Returns:
            bool: True wenn operativ
        """
        return state != GrillStateMachine.STATE_SENSOR_ERROR
