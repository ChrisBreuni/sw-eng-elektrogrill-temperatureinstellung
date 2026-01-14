from src.grill_controller import GrillController


def print_state(controller: GrillController, label: str) -> None:
    print(f"--- {label} ---")
    print(f"Aktuelle Temperatur: {controller.get_current_temperature()} °C")
    print(f"Zieltemperatur:     {controller.get_target_temperature()} °C")
    print(f"Power an?:          {controller.power_state.is_on()}")
    print(f"Ziel erreicht?:     {controller.is_target_reached()}")
    print(f"Cooling down?:      {controller.is_cooling_down()}")
    print(f"Status:             {controller.get_status()}")
    print()


if __name__ == "__main__":
    controller = GrillController()

    # 1) Zieltemperatur setzen
    controller.set_target_temperature(180.0)
    controller.set_current_temperature(20.0)
    print_state(controller, "Start mit Ziel 180 °C")

    # 2) Aufheizen simulieren
    for temp in [50.0, 120.0, 170.0, 180.0]:
        controller.set_current_temperature(temp)
        print_state(controller, f"Aufheizen")

    # 3) Grill ausschalten – Restwärme
    controller.set_target_temperature(0.0)  # schaltet Power aus
    for temp in [150.0, 80.0, 40.0]:
        controller.set_current_temperature(temp)
        print_state(controller, f"Nach Ausschalten")
