import matplotlib.pyplot as plt

# Importieren der Logik-Module aus dem src-Ordner
from src.physics import (Simulation)
from src.visualization import (Design)

def main():
    # Parameter definieren
    v0 = 30.0		# Startgeschwindigkeit
    angle = 45.0	# Winkel
    dt = 0.1		# Zeit zwischen den Schritten
    m = 0.15		# Masse
    r = 0.02		# Radius
    cw = 0.5		# Strömungsstärkewiederstandskoeffizienz
    rho = 1.2		# Luftdichte
    g = 9.81		# Gravitation
    
    # Berechnung starten mit den richtigen Werten
    x_vals, y_vals = Simulation(
        v0=v0,
        angle_deg=angle,
        dt=dt,
        m=m,
        r=r,
        cw=cw,
        rho=rho,
        g=g
        )
    
    # Visualisierung starten
    Design(x_vals, y_vals)
    
if __name__ == "__main__":
    main()
