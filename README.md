# Projektarbeit: Numerische Simulation des Wurfs unter Luftwiderstand

**Thema:** Numerische Simulation des Wurfs unter Luftwiderstand per Euler-Verfahren mit mathematischer Analyse  
**Art der Arbeit:** Projekt mit Portfolio  

---

### Fächer
* **Leistungskurs (LK):** Physik  
* **Grundkurs (GK):** Mathematik  

---

### Beteiligte Schüler:innen
* Maximilian Norbach
* Silas Schikker

---

## Projektstruktur

```text
Projektarbeit/
│
├── .gitignore               # Steuert, welche Dateien nicht auf GitHub geladen werden
├── LICENSE                  # Lizenzinformationen zum Projekt
├── Portfolio.odt            # Portfolio / Dokumentation der Projektarbeit
├── README.md                # Diese Übersicht und Projektbeschreibung
├── main.py                  # Hauptprogramm und Startpunkt der Simulation
├── notizen                  # notizen für die Projektarbeit
│
├── Vorgaben                                                 # Vorgaben der Schule
│    ├── Erläuterung zu Projekt in der Q1 2026.pdf           # Erläuterung der Projektarbeit
│    ├── KI Nutzung Projektarbeit.pdf                        # KI Nutzung zum ausfüllen
│    ├── Laufzettel Projektarbeit 2026-27.pdf                # Laufzettel für die Projektarbeit
│    ├── Schulinterne Vorgaben zur Projektarbeit 2026.pdf    # Vorgaben der Projektarbeit
│    └── ZeitrasterPA 2026-27.pdf                            # Zeitplan für die Projektarbeit
│
├── Schulischer_Wurf      # Simulation vom Schulischen / Simpleren Wurf
│   ├── Schule_main.py    # Hauptprogramm und Startpunkt der Schulischen Simulation
│   └── src/                      # Quellcode-Ordner (Source)
│        ├── __init__.py          # Signaldatei für Python (bleibt leer)
│        ├── physics.py           # Physikalische Logik
│        └── visualization.py     # Erstellung der Diagramme und Plots
│
└── src/                     # Quellcode-Ordner (Source)
    ├── __init__.py          # Signaldatei für Python (bleibt leer)
    ├── physics.py           # Physikalische Logik
    └── visualization.py     # Erstellung der Diagramme und Plots
