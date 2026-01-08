"""
main.py - Einstiegspunkt für die Elektrogrill-Steuerung

Startet die Anwendung:
1. Erstellt GrillController (Model + Controller)
2. Erstellt GrillGUI (View)
3. Startet die GUI
"""

from src.grill_controller import GrillController
from src.gui_main import GrillGUI


def main():
    """Startet die Elektrogrill-Steuerung."""
    
    # Erstelle Controller mit allen Models
    controller = GrillController()
    
    # Erstelle GUI (View) mit Controller
    gui = GrillGUI(controller)
    
    # Starte GUI (Mainloop)
    gui.run()


if __name__ == "__main__":
    main()
