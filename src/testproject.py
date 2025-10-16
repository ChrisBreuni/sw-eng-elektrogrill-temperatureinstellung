import tkinter as tk
import math
import time

class GrillControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Elektrogrill - Temperaturregelung")

        # Temperaturgrenzen
        self.min_temp = 50      # °C
        self.max_temp = 300     # °C (Einstellbar über Drehrad)
        self.safe_max = 280     # °C (Warnschwelle)

        # Simulation: aktuelle und eingestellte Temperatur
        self.set_temp = 200.0
        self.current_temp = 25.0  # Umgebungstemperatur initial
        self.last_time = time.time()

        # Heizmuster
        self.heating_rate = 40.0   # °C pro Minute maximal (simulierte Leistung)
        self.cooling_rate = 10.0   # °C pro Minute wenn ausgeschaltet

        # Vorheiztoleranz (wann die Lampe angeht)
        self.preheat_tolerance = 3.0  # °C

        # Knob geometry
        self.knob_size = 220
        self.knob_center = (self.knob_size//2 + 10, self.knob_size//2 + 10)
        self.knob_radius = self.knob_size//2 - 10
        self.knob_min_angle = -135  # in degrees
        self.knob_max_angle = 135

        # GUI Aufbau
        self.create_widgets()

        # Knob state
        self.knob_dragging = False

        # Starte Update-Loop
        self.update_loop()

    def create_widgets(self):
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack()

        # Canvas für Drehrad
        self.canvas = tk.Canvas(frame, width=self.knob_size+20, height=self.knob_size+20)
        self.canvas.grid(row=0, column=0, rowspan=4, padx=10, pady=5)
        self.draw_knob()

        # Labels für Temperaturen
        self.lbl_current = tk.Label(frame, text=f"Aktuelle Temperatur: {self.current_temp:.1f} °C", font=("Arial", 12))
        self.lbl_current.grid(row=0, column=1, sticky="w", padx=10)

        self.lbl_set = tk.Label(frame, text=f"Eingestellte Temperatur: {self.set_temp:.1f} °C", font=("Arial", 12))
        self.lbl_set.grid(row=1, column=1, sticky="w", padx=10)

        # Preheat indicator (Lämpchen)
        lamp_frame = tk.Frame(frame)
        lamp_frame.grid(row=2, column=1, sticky="w", padx=10, pady=(5,0))
        tk.Label(lamp_frame, text="Vorheizen:").pack(side="left")
        self.lamp_canvas = tk.Canvas(lamp_frame, width=24, height=24)
        self.lamp_canvas.pack(side="left", padx=(6,0))
        self.lamp = self.lamp_canvas.create_oval(4,4,20,20, fill="grey")

        # Warnung
        self.lbl_warning = tk.Label(frame, text="", font=("Arial", 11), fg="red")
        self.lbl_warning.grid(row=3, column=1, sticky="w", padx=10, pady=(6,0))

        # Slider als Alternative zur Einstellung
        self.slider = tk.Scale(frame, from_=self.max_temp, to=self.min_temp, orient="vertical",
                               command=self.on_slider_change, length=200)
        self.slider.set(self.set_temp)
        self.slider.grid(row=0, column=2, rowspan=4, padx=(10,0))

        # Ereignisbindung für Knob
        self.canvas.bind("<ButtonPress-1>", self.on_knob_press)
        self.canvas.bind("<B1-Motion>", self.on_knob_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_knob_release)

        # Tastatur-Kurzbefehle
        self.root.bind("<Left>", lambda e: self.change_set_temp(-1))
        self.root.bind("<Right>", lambda e: self.change_set_temp(1))
        self.root.bind("<Up>", lambda e: self.change_set_temp(5))
        self.root.bind("<Down>", lambda e: self.change_set_temp(-5))

    def draw_knob(self):
        self.canvas.delete("all")
        cx, cy = self.knob_center
        r = self.knob_radius
        # Knob circle
        self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="#eee", outline="#666", width=2)
        # ticks and labels
        for t in range(0, 11):
            frac = t / 10.0
            angle = math.radians(self.knob_min_angle + frac * (self.knob_max_angle - self.knob_min_angle))
            x1 = cx + (r-8) * math.cos(angle)
            y1 = cy + (r-8) * math.sin(angle)
            x2 = cx + r * math.cos(angle)
            y2 = cy + r * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, fill="#444", width=2)
            # label every other tick
            if t % 2 == 0:
                temp_val = int(self.min_temp + frac*(self.max_temp - self.min_temp))
                xl = cx + (r-24) * math.cos(angle)
                yl = cy + (r-24) * math.sin(angle)
                self.canvas.create_text(xl, yl, text=str(temp_val), font=("Arial", 9))

        # draw pointer based on set_temp
        angle = self.temp_to_angle(self.set_temp)
        angle_rad = math.radians(angle)
        px = cx + (r-40) * math.cos(angle_rad)
        py = cy + (r-40) * math.sin(angle_rad)
        self.canvas.create_line(cx, cy, px, py, fill="#c33", width=4, capstyle="round")
        # center circle
        self.canvas.create_oval(cx-12, cy-12, cx+12, cy+12, fill="#fff", outline="#333", width=2)

        # kleine Anzeige der Solltemperatur im Knob
        self.canvas.create_text(cx, cy+40, text=f"{self.set_temp:.0f} °C", font=("Arial", 12, "bold"))

    def temp_to_angle(self, temp):
        # Map temp (min_temp..max_temp) to angle (knob_min_angle..knob_max_angle)
        frac = (temp - self.min_temp) / (self.max_temp - self.min_temp)
        frac = max(0.0, min(1.0, frac))
        return self.knob_min_angle + frac * (self.knob_max_angle - self.knob_min_angle)

    def angle_to_temp(self, angle):
        # Map angle to temperature
        frac = (angle - self.knob_min_angle) / (self.knob_max_angle - self.knob_min_angle)
        frac = max(0.0, min(1.0, frac))
        return self.min_temp + frac * (self.max_temp - self.min_temp)

    def on_knob_press(self, event):
        # Prüfe, ob im Knob gedrückt wurde (eher großzügig)
        dx = event.x - self.knob_center[0]
        dy = event.y - self.knob_center[1]
        if math.hypot(dx, dy) <= self.knob_radius + 10:
            self.knob_dragging = True
            self.update_knob_from_mouse(event.x, event.y)

    def on_knob_drag(self, event):
        if self.knob_dragging:
            self.update_knob_from_mouse(event.x, event.y)

    def on_knob_release(self, event):
        self.knob_dragging = False

    def update_knob_from_mouse(self, mx, my):
        cx, cy = self.knob_center
        angle = math.degrees(math.atan2(my - cy, mx - cx))
        # atan2 gibt -180..180; wir wollen die Beschränkung auf min..max
        # wenn außerhalb Bereich, clamp
        if angle < self.knob_min_angle:
            angle = self.knob_min_angle
        if angle > self.knob_max_angle:
            angle = self.knob_max_angle
        new_temp = self.angle_to_temp(angle)
        self.set_temp = round(new_temp)
        self.slider.set(self.set_temp)
        self.draw_knob()
        self.update_labels()

    def on_slider_change(self, val):
        try:
            self.set_temp = float(val)
        except:
            return
        self.draw_knob()
        self.update_labels()

    def change_set_temp(self, delta):
        self.set_temp = max(self.min_temp, min(self.max_temp, self.set_temp + delta))
        self.slider.set(self.set_temp)
        self.draw_knob()
        self.update_labels()

    def update_simulation(self, dt_minutes):
        # einfache thermische Simulation:
        # Wenn set_temp > current_temp: heizung an -> erwärmung proportional zur Differenz, begrenzt durch heating_rate
        # Wenn set_temp < current_temp: heizung aus -> Abkühlrate
        diff = self.set_temp - self.current_temp
        if diff > 0.1:
            # Heizen: schneller je größer die Differenz, aber begrenzt
            # Pro Minute Temperaturänderung:
            change = min(self.heating_rate * dt_minutes, diff * 0.8)
        elif diff < -0.1:
            # Abkühlen
            change = -min(self.cooling_rate * dt_minutes, abs(diff))
        else:
            change = 0.0
        self.current_temp += change
        # leichte passivabkühlung zur Umgebung (25°C)
        env = 25.0
        env_effect = (env - self.current_temp) * 0.02 * dt_minutes
        self.current_temp += env_effect

    def update_labels(self):
        self.lbl_current.config(text=f"Aktuelle Temperatur: {self.current_temp:.1f} °C")
        self.lbl_set.config(text=f"Eingestellte Temperatur: {self.set_temp:.1f} °C")

    def update_warning_and_lamp(self):
        # Warnung wenn über safe_max
        if self.current_temp >= self.safe_max:
            self.lbl_warning.config(text=f"Warnung: Temperatur sehr hoch! ({self.current_temp:.0f} °C)")
        elif self.set_temp > self.max_temp:
            self.lbl_warning.config(text="Warnung: Eingestellte Temperatur außerhalb des erlaubten Bereichs!")
        else:
            self.lbl_warning.config(text="")

        # Vorheizen-Lampe: an wenn innerhalb Toleranz oder current_temp > set_temp
        if abs(self.current_temp - self.set_temp) <= self.preheat_tolerance or self.current_temp >= self.set_temp:
            self.lamp_canvas.itemconfig(self.lamp, fill="green")
        else:
            self.lamp_canvas.itemconfig(self.lamp, fill="grey")

    def update_loop(self):
        now = time.time()
        dt = now - self.last_time
        self.last_time = now
        dt_minutes = dt / 60.0

        # Simulation updaten
        self.update_simulation(dt_minutes)

        # GUI aktualisieren
        self.update_labels()
        self.update_warning_and_lamp()
        self.draw_knob()

        # Wiederholen
        self.root.after(200, self.update_loop)  # 5x pro Sekunde

if __name__ == "__main__":
    root = tk.Tk()
    app = GrillControlApp(root)
    root.mainloop()