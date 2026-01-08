"""
main.py - Haupteinstiegspunkt der Elektrogrill-Steuerungsanwendung

Startet den Elektrogrill mit GUI.

Struktur:
- Model-Schicht: CurrentTemperature, TargetTemperature, PowerState
- Controller-Schicht: GrillController
- View-Schicht: GrillGUI
"""

from src.grill_controller import GrillController
from src.gui_main import GrillGUI


def main():
    """
    Startet die Elektrogrill-Steuerungsanwendung mit GUI.
    """
    # Erstelle Controller (Model + Business-Logic)
    controller = GrillController()
    
    # Erstelle GUI (View-Schicht)
    gui = GrillGUI(controller)
    
    # Starte GUI (Mainloop)
    gui.run()


if __name__ == "__main__":
    main()
