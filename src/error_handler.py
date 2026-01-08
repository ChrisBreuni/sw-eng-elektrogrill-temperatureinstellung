"""
ErrorHandler - Zentrale Fehlerbehandlung für Elektrogrill

Verantwortlichkeiten:
- Verwaltet Fehler und Exceptions
- Speichert Fehler mit Timestamp
- Stellt Fehlerinformationen für GUI bereit
"""

from datetime import datetime
from typing import Optional, Dict, Any


class GrillError:
    """
    Repräsentiert einen Fehler im Elektrogrill.
    
    Attributes:
        error_type (str): Typ des Fehlers (z.B. 'SENSOR_ERROR')
        message (str): Fehlermeldung
        timestamp (datetime): Zeitpunkt des Fehlers
        data (dict): Zusätzliche Fehlerinformationen
    """
    
    def __init__(self, error_type: str, message: str, data: Dict[str, Any] = None):
        """
        Initialisiert einen Fehler.
        
        Args:
            error_type (str): Fehlertyp
            message (str): Fehlermeldung
            data (dict): Zusätzliche Daten (optional)
        """
        self.error_type = error_type
        self.message = message
        self.timestamp = datetime.now()
        self.data = data or {}
    
    def __str__(self) -> str:
        return f"[{self.error_type}] {self.message}"
    
    def is_active(self) -> bool:
        """Prüft ob Fehler noch aktiv ist (immer True, bis manual gelöscht)."""
        return True


class ErrorHandler:
    """
    Zentrale Fehlerbehandlung für den Elektrogrill.
    
    Verwaltet alle Fehler und Exceptions im System.
    """
    
    # Fehlertypen
    ERROR_TYPE_SENSOR = "SENSOR_ERROR"
    ERROR_TYPE_VALIDATION = "VALIDATION_ERROR"
    ERROR_TYPE_SYSTEM = "SYSTEM_ERROR"
    
    def __init__(self):
        """Initialisiert den ErrorHandler."""
        self._errors = []
        self._active_error = None
    
    def add_error(self, error_type: str, message: str, data: Dict[str, Any] = None) -> GrillError:
        """
        Fügt einen Fehler hinzu.
        
        Args:
            error_type (str): Fehlertyp
            message (str): Fehlermeldung
            data (dict): Zusätzliche Daten
            
        Returns:
            GrillError: Der hinzugefügte Fehler
        """
        error = GrillError(error_type, message, data)
        self._errors.append(error)
        
        # Wenn es der erste Fehler ist, setze ihn als aktiv
        if self._active_error is None:
            self._active_error = error
        
        return error
    
    def get_active_error(self) -> Optional[GrillError]:
        """
        Gibt den aktiven Fehler zurück (falls vorhanden).
        
        Returns:
            GrillError oder None
        """
        return self._active_error
    
    def has_error(self) -> bool:
        """
        Prüft ob ein aktiver Fehler existiert.
        
        Returns:
            bool: True wenn Fehler aktiv
        """
        return self._active_error is not None
    
    def clear_errors(self) -> None:
        """Löscht alle Fehler."""
        self._errors.clear()
        self._active_error = None
    
    def clear_active_error(self) -> None:
        """Löscht nur den aktiven Fehler."""
        self._active_error = None
    
    def get_error_message(self) -> str:
        """
        Gibt die Fehlermeldung des aktiven Fehlers zurück.
        
        Returns:
            str: Fehlermeldung oder leerer String
        """
        if self._active_error:
            return str(self._active_error)
        return ""
    
    def get_error_type(self) -> Optional[str]:
        """
        Gibt den Typ des aktiven Fehlers zurück.
        
        Returns:
            str oder None
        """
        if self._active_error:
            return self._active_error.error_type
        return None
    
    def get_all_errors(self) -> list:
        """
        Gibt alle Fehler zurück.
        
        Returns:
            list: Liste aller Fehler
        """
        return self._errors.copy()
