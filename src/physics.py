import math

def Simulation(v0, angle, dt, m, r, cw, rho, g, A):
    
    # Anfangsbedingungen
    x, y = 0.0, 0.0
    vx = v0 * math.cos(angle)
    vy = v0 * math.sin(angle)
    
    # Listen zum Speichern der Trajektorie
    x_values = [x]
    y_values = [y]
    
    # Schleife läuft, solange der Körper über dem Boden ist
    while y >= 0:
        v = math.sqrt(vx**2 + vy**2)	# Satz des Pythagoras
        
        # Luftwiderstandskraft
        F_w = 0.5 * rho * A * cw * (v**2)
        
        # Beschleunigungen (F_w wirkt entgegen der aktuellen Flugrichtung)
        ax = -(F_w / m) * (vx / v)
        ay = -g - (F_w / m) * (vy / v)
        
        # Euler-Schritt (Aktualisierung von Ort und Geschwindigkeit)
        x = x + vx * dt
        y = y + vy * dt
        vx = vx + ax * dt
        vy = vy + ay * dt
        
        x_values.append(x)
        y_values.append(y)
        
    return x_values, y_values