import math

def Simulation(v0, angle_deg, dt, m, r, cw, rho, g):

    # Umrechnung Winkel in Radians
    angle_rad = math.radians(angle_deg)
    
    # Anfangsbedingungen
    x, y = 0.0, 0.0
    vx = v0 * math.cos(angle_rad)
    vy = v0 * math.sin(angle_rad)
    
    A = math.pi * (r ** 2)  # Querschnittsfläche der Kugel
    
    # Listen zum Speichern der Trajektorie
    x_values = [x]
    y_values = [y]
    
    # Schleife läuft, solange der Körper über dem Boden ist
    while y >= 0:
        v = math.sqrt(vx**2 + vy**2)
        
        # Luftwiderstandskraft: F_w = 0.5 * rho * A * cw * v^2
        F_w = 0.5 * rho * A * cw * (v**2)
        
        # Beschleunigungen
        ax = -(F_w / m) * (vx / v)
        ay = -g - (F_w / m) * (vy / v)
        
        # Euler-Schritt
        x = x + vx * dt
        y = y + vy * dt
        vx = vx + ax * dt
        vy = vy + ay * dt
        
        x_values.append(x)
        y_values.append(y)
        
    return x_values, y_values
