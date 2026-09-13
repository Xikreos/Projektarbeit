import matplotlib.pyplot as plt

def Design(x_vals, y_vals, title="Schiefer Wurf mit Luftwiderstand"):

    plt.figure(figsize=(8, 4.5))
    plt.plot(x_vals, y_vals, label="Wurfparabel", color="blue")
    
    plt.title(title)
    plt.xlabel("Distance x (m)")
    plt.ylabel("Hight y (m)")
    plt.axhline(0, color='black', linewidth=0.8)  # Bodenlinie
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    
    # Öffnen des Fensters
    plt.show()
