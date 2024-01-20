# importowanie bibliotek
import tkinter as tk
from KoloFortuny import KoloFortuny


class Aplikacja:
    @staticmethod
    def uruchom():
        if __name__ == "__main__":
            root = tk.Tk()
            gra = KoloFortuny(root)
            root.mainloop()

# uruchomienie aplikacji
Aplikacja.uruchom()
