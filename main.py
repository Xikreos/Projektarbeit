import matplotlib.pyplot as plt
import math

# Importieren der Logik-Module aus dem src-Ordner
from src.physics import (Simulation)
from src.visualization import (Design)

def main():
    # Parameter definieren
    v0 = 30.0		# Startgeschwindigkeit
    angle = math.radians(45.0)	# Winkel des Abwurfs
    dt = 0.01		# Zeit zwischen den Schritten
    m = 0.15		# Masse
    r = 0.01		# Radius
    cw = 0.47		# Strömungswiderstandskoeffizient
    rho = 1.293		# Luftdichte
    g = 9.81		# Gravitation
    A = math.pi * (r ** 2) #Fläche des Kreises
    
    # Parameter in die physics.py Datei übergeben
    x_vals, y_vals = Simulation(
        v0=v0,
        angle=angle,
        dt=dt,
        m=m,
        r=r,
        cw=cw,
        rho=rho,
        g=g,
        A=A
        )
    
    # Visualisierung starten
    Design(x_vals, y_vals)
    
if __name__ == "__main__":
    main()