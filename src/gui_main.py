"""
GrillGUI - Benutzeroberfläche für Elektrogrill-Steuerung

Implementiert die View-Schicht (Präsentationsschicht) mit Tkinter.
Kommuniziert ausschließlich über den GrillController mit der Model-Schicht.

Features:
- 4 Frames: Header, Temperatur, Status, Power
- 13 Widgets für Anzeige und Interaktion
- Periodische Aktualisierung (500ms)
- Farbcodierte Status
- Fehlerbehandlung mit Messageboxen
"""

import tkinter as tk
from tkinter import messagebox
from src.grill_controller import GrillController


class GrillGUI:
    """
    Tkinter-basierte GUI für die Steuerung des Elektrogrills.
    
    Implementiert die Präsentationsschicht nach MVC-Pattern.
    """

    # ============ Design Konstanten ============
    # Farben (Material Design)
    COLOR_PRIMARY = "#2196F3"       # Blau
    COLOR_SUCCESS = "#4CAF50"       # Grün
    COLOR_WARNING = "#FF9800"       # Orange
    COLOR_ERROR = "#F44336"         # Rot
    COLOR_BG_MAIN = "#F5F5F5"       # Grau
    COLOR_BG_CARD = "#FFFFFF"       # Weiß
    
    # Fenster
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 500
    
    # Timing
    UPDATE_INTERVAL = 500  # ms

    def __init__(self, controller: GrillController):
        """
        Initialisiert die GUI mit einem GrillController.
        
        Args:
            controller (GrillController): Controller für Business-Logik
        """
        self.controller = controller
        
        # Tkinter Hauptfenster
        self.root = tk.Tk()
        self.root.title("Elektrogrill - Temperatursteuerung")
        self.root.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.root.resizable(False, False)
        self.root.configure(bg=self.COLOR_BG_MAIN)
        
        # Widget-Referenzen
        self._ui_refs = {}
        
        # Erstelle Widgets
        self._create_widgets()
        
        # Starte Updates
        self._schedule_update()

    def _create_widgets(self) -> None:
        """Erstellt alle UI-Komponenten."""
        
        # ==================== Header Frame ====================
        header_frame = tk.Frame(self.root, bg=self.COLOR_PRIMARY)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        
        header_label = tk.Label(
            header_frame,
            text="Elektrogrill - Temperatursteuerung",
            font=("Arial", 16, "bold"),
            bg=self.COLOR_PRIMARY,
            fg="white",
            pady=15
        )
        header_label.pack()

        # ==================== Temperature Frame ====================
        temp_frame = tk.LabelFrame(
            self.root,
            text="Temperaturanzeige",
            font=("Arial", 11, "bold"),
            bg=self.COLOR_BG_CARD,
            padx=15,
            pady=15
        )
        temp_frame.pack(fill=tk.BOTH, padx=15, pady=10)
        
        # Aktuelle Temperatur
        tk.Label(
            temp_frame,
            text="Aktuelle Temperatur:",
            font=("Arial", 10),
            bg=self.COLOR_BG_CARD
        ).grid(row=0, column=0, sticky="w", pady=5)
        
        self._ui_refs['current_temp_label'] = tk.Label(
            temp_frame,
            text="20.0 °C",
            font=("Arial", 13, "bold"),
            bg=self.COLOR_BG_CARD,
            fg=self.COLOR_PRIMARY
        )
        self._ui_refs['current_temp_label'].grid(row=0, column=1, sticky="e", pady=5)
        
        # Zieltemperatur
        tk.Label(
            temp_frame,
            text="Zieltemperatur:",
            font=("Arial", 10),
            bg=self.COLOR_BG_CARD
        ).grid(row=1, column=0, sticky="w", pady=5)
        
        self._ui_refs['target_temp_label'] = tk.Label(
            temp_frame,
            text="0 °C",
            font=("Arial", 13, "bold"),
            bg=self.COLOR_BG_CARD,
            fg=self.COLOR_PRIMARY
        )
        self._ui_refs['target_temp_label'].grid(row=1, column=1, sticky="e", pady=5)
        
        # Input-Bereich
        tk.Label(
            temp_frame,
            text="Neue Zieltemperatur (50-500 °C):",
            font=("Arial", 9),
            bg=self.COLOR_BG_CARD
        ).grid(row=2, column=0, columnspan=2, sticky="w", pady=(15, 5))
        
        # Input-Frame mit Buttons
        input_frame = tk.Frame(temp_frame, bg=self.COLOR_BG_CARD)
        input_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=5)
        
        self._ui_refs['temp_input'] = tk.Entry(
            input_frame,
            font=("Arial", 10),
            width=12,
            justify="center"
        )
        self._ui_refs['temp_input'].pack(side=tk.LEFT, padx=5)
        
        # Buttons
        button_frame = tk.Frame(input_frame, bg=self.COLOR_BG_CARD)
        button_frame.pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="+10 °C",
            font=("Arial", 9),
            width=7,
            command=self._increase_target,
            bg=self.COLOR_SUCCESS,
            fg="white"
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Button(
            button_frame,
            text="-10 °C",
            font=("Arial", 9),
            width=7,
            command=self._decrease_target,
            bg=self.COLOR_WARNING,
            fg="white"
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Button(
            input_frame,
            text="Setzen",
            font=("Arial", 9),
            width=7,
            command=self._set_target,
            bg=self.COLOR_PRIMARY,
            fg="white"
        ).pack(side=tk.LEFT, padx=5)

        # ==================== Status Frame ====================
        status_frame = tk.LabelFrame(
            self.root,
            text="Status",
            font=("Arial", 11, "bold"),
            bg=self.COLOR_BG_CARD,
            padx=15,
            pady=15
        )
        status_frame.pack(fill=tk.BOTH, padx=15, pady=10)
        
        # Grillstatus
        tk.Label(
            status_frame,
            text="Grillstatus:",
            font=("Arial", 10),
            bg=self.COLOR_BG_CARD
        ).grid(row=0, column=0, sticky="w", pady=5)
        
        self._ui_refs['status_label'] = tk.Label(
            status_frame,
            text="OFF",
            font=("Arial", 11, "bold"),
            bg=self.COLOR_BG_CARD,
            fg=self.COLOR_ERROR
        )
        self._ui_refs['status_label'].grid(row=0, column=1, sticky="e", pady=5)
        
        # Zieltemperatur erreicht
        tk.Label(
            status_frame,
            text="Zieltemperatur erreicht:",
            font=("Arial", 10),
            bg=self.COLOR_BG_CARD
        ).grid(row=1, column=0, sticky="w", pady=5)
        
        self._ui_refs['target_reached_label'] = tk.Label(
            status_frame,
            text="Nein",
            font=("Arial", 11),
            bg=self.COLOR_BG_CARD,
            fg=self.COLOR_ERROR
        )
        self._ui_refs['target_reached_label'].grid(row=1, column=1, sticky="e", pady=5)
        
        # Abkühlphase
        tk.Label(
            status_frame,
            text="Restwärme (Abkühlung):",
            font=("Arial", 10),
            bg=self.COLOR_BG_CARD
        ).grid(row=2, column=0, sticky="w", pady=5)
        
        self._ui_refs['cooling_label'] = tk.Label(
            status_frame,
            text="Nein",
            font=("Arial", 11),
            bg=self.COLOR_BG_CARD,
            fg=self.COLOR_ERROR
        )
        self._ui_refs['cooling_label'].grid(row=2, column=1, sticky="e", pady=5)
        
        # Sensor
        tk.Label(
            status_frame,
            text="Sensor Status:",
            font=("Arial", 10),
            bg=self.COLOR_BG_CARD
        ).grid(row=3, column=0, sticky="w", pady=5)
        
        self._ui_refs['sensor_label'] = tk.Label(
            status_frame,
            text="OK",
            font=("Arial", 11),
            bg=self.COLOR_BG_CARD,
            fg=self.COLOR_SUCCESS
        )
        self._ui_refs['sensor_label'].grid(row=3, column=1, sticky="e", pady=5)

        # ==================== Power Frame ====================
        power_frame = tk.LabelFrame(
            self.root,
            text="Stromversorgung",
            font=("Arial", 11, "bold"),
            bg=self.COLOR_BG_CARD,
            padx=15,
            pady=15
        )
        power_frame.pack(fill=tk.BOTH, padx=15, pady=10)
        
        button_frame = tk.Frame(power_frame, bg=self.COLOR_BG_CARD)
        button_frame.pack(fill=tk.X)
        
        self._ui_refs['toggle_power_btn'] = tk.Button(
            button_frame,
            text="Grill EIN-/AUS",
            font=("Arial", 11, "bold"),
            width=20,
            height=2,
            command=self._toggle_power,
            bg=self.COLOR_ERROR,
            fg="white"
        )
        self._ui_refs['toggle_power_btn'].pack(side=tk.LEFT, padx=10, pady=10)
        
        self._ui_refs['power_status_label'] = tk.Label(
            button_frame,
            text="Status: AUS",
            font=("Arial", 10, "bold"),
            bg=self.COLOR_BG_CARD,
            fg=self.COLOR_ERROR
        )
        self._ui_refs['power_status_label'].pack(side=tk.LEFT, padx=20)

    # ============ Event Handler ============

    def _set_target(self) -> None:
        """Handler für [Setzen] Button."""
        try:
            value = float(self._ui_refs['temp_input'].get())
            self.controller.set_target_temperature(value)
            self._ui_refs['temp_input'].delete(0, tk.END)
            messagebox.showinfo("Erfolg", f"Zieltemperatur auf {value:.1f} °C gesetzt.")
        except ValueError as e:
            messagebox.showerror("Fehler", f"Ungültige Eingabe: {str(e)}")

    def _increase_target(self) -> None:
        """Handler für [+10°C] Button."""
        try:
            self.controller.increase_target_temperature(10.0)
            new_temp = self.controller.get_target_temperature()
            messagebox.showinfo("Erfolg", f"Zieltemperatur auf {new_temp:.1f} °C erhöht.")
        except ValueError as e:
            messagebox.showerror("Fehler", f"Nicht möglich: {str(e)}")

    def _decrease_target(self) -> None:
        """Handler für [-10°C] Button."""
        try:
            self.controller.decrease_target_temperature(10.0)
            new_temp = self.controller.get_target_temperature()
            messagebox.showinfo("Erfolg", f"Zieltemperatur auf {new_temp:.1f} °C gesenkt.")
        except ValueError as e:
            messagebox.showerror("Fehler", f"Nicht möglich: {str(e)}")

    def _toggle_power(self) -> None:
        """Handler für [EIN/AUS] Button."""
        self.controller.power_state.toggle_power()
        
        # Wenn eingeschaltet und keine Zieltemp: setze 180°C
        if self.controller.power_state.is_on() and self.controller.get_target_temperature() == 0:
            self.controller.set_target_temperature(180.0)

    # ============ Display Update ============

    def _update_display(self) -> None:
        """Aktualisiert alle Anzeigen basierend auf Controller-Status."""
        
        current = self.controller.get_current_temperature()
        target = self.controller.get_target_temperature()
        status = self.controller.get_status()
        power_on = self.controller.power_state.is_on()
        sensor_ok = self.controller.current_temp.is_sensor_ok()
        target_reached = self.controller.is_target_reached()
        cooling = self.controller.is_cooling_down()
        
        # Aktuelle Temperatur
        if current < 0:
            self._ui_refs['current_temp_label'].config(text="ERROR", fg=self.COLOR_ERROR)
        else:
            self._ui_refs['current_temp_label'].config(
                text=f"{current:.1f} °C",
                fg=self.COLOR_PRIMARY
            )
        
        # Zieltemperatur
        self._ui_refs['target_temp_label'].config(text=f"{target:.1f} °C")
        
        # Grillstatus mit Farb-Mapping
        status_map = {
            "OFF": ("AUS", self.COLOR_ERROR),
            "HEATING": ("AUFHEIZEN", self.COLOR_WARNING),
            "TARGET_REACHED": ("ZIEL ERREICHT", self.COLOR_SUCCESS),
            "COOLING_DOWN": ("ABKÜHLUNG", self.COLOR_WARNING),
            "SENSOR_ERROR": ("SENSOR FEHLER", self.COLOR_ERROR),
        }
        
        status_text, status_color = status_map.get(status, (status, self.COLOR_PRIMARY))
        self._ui_refs['status_label'].config(text=status_text, fg=status_color)
        
        # Zieltemperatur erreicht
        self._ui_refs['target_reached_label'].config(
            text="Ja" if target_reached else "Nein",
            fg=self.COLOR_SUCCESS if target_reached else self.COLOR_ERROR
        )
        
        # Abkühlphase
        self._ui_refs['cooling_label'].config(
            text="Ja" if cooling else "Nein",
            fg=self.COLOR_WARNING if cooling else self.COLOR_ERROR
        )
        
        # Sensor
        self._ui_refs['sensor_label'].config(
            text="OK" if sensor_ok else "FEHLER",
            fg=self.COLOR_SUCCESS if sensor_ok else self.COLOR_ERROR
        )
        
        # Power-Status
        self._ui_refs['toggle_power_btn'].config(
            bg=self.COLOR_SUCCESS if power_on else self.COLOR_ERROR
        )
        self._ui_refs['power_status_label'].config(
            text="Status: AN" if power_on else "Status: AUS",
            fg=self.COLOR_SUCCESS if power_on else self.COLOR_ERROR
        )

    def _schedule_update(self) -> None:
        """Plant die nächste Aktualisierung ein."""
        # Update Controller (Temperaturänderung simulieren)
        self.controller.update()
        
        # Update Display (alle Labels)
        self._update_display()
        
        # Plane nächsten Update
        self.root.after(self.UPDATE_INTERVAL, self._schedule_update)

    def run(self) -> None:
        """Startet die GUI (Mainloop)."""
        self.root.mainloop()
