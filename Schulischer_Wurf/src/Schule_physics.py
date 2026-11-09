import math

def Simulation(v0, angle, dt, g):

    # Anfangsbedingungen
    x, y = 0.0, 0.0
    vx = v0 * math.cos(angle)
    vy = v0 * math.sin(angle)
    
    # Listen zum Speichern der Trajektorie
    x_values = [x]
    y_values = [y]
    
    # Schleife läuft, solange der Körper über dem Boden ist
    while y >= 0:
        # Beschleunigungen:
        ax = 0.0
        ay = -g
        
        # Euler-Schritt (Aktualisierung von Ort und Geschwindigkeit)
        x = x + vx * dt
        y = y + vy * dt
        vx = vx + ax * dt
        vy = vy + ay * dt
        
        x_values.append(x)
        y_values.append(y)
    # x und y Werte zurückgeben
    return x_values, y_values