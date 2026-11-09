import matplotlib.pyplot as plt
import math

# Importieren der Logik-Module aus dem src-Ordner
from src.Schule_physics import (Simulation)
from src.Schule_visualization import (Design)

def main():
    # Parameter definieren
    v0 = 30.0   				# Startgeschwindigkeit
    angle = math.radians(45.0)	# Winkel des Abwurfs
    dt = 0.01					# Zeit zwischen den Schritten
    g = 9.81					# Gravitation
    
    # Parameter in die physics.py Datei übergeben
    x_vals, y_vals = Simulation(
        v0=v0,
        angle=angle,
        dt=dt,
        g=g,
        )
    
    # Visualisierung starten
    Design(x_vals, y_vals)
    
if __name__ == "__main__":
    main()