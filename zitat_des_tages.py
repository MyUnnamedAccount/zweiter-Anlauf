import random
import os

def zeige_zufälliges_zitat():
    if not os.path.exists("zitate.txt"):
        print("Fehler: Die Datei 'zitate.txt' wurde nicht gefunden!")
        return

    with open("zitate.txt", "r", encoding="utf-8") as datei:
        zitate = datei.readlines()

    if zitate:
        zufall = random.choice(zitate).strip()
        print("\n--- Dein Zitat des Tages ---")
        print(f'"{zufall}"')
        print("----------------------------\n")
    else:
        print("Die Datei ist leer.")

if __name__ == "__main__":
    zeige_zufälliges_zitat()