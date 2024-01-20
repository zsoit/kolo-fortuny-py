class OdczytywaczPliku:
    def __init__(self, nazwa_pliku):
        self.nazwa_pliku = nazwa_pliku

    def odczytaj_linie(self):
        try:
            with open(self.nazwa_pliku, 'r') as plik:
                linie = plik.readlines()
                return linie
        except FileNotFoundError:
            print(f"Plik '{self.nazwa_pliku}' nie istnieje.")
            return None
        except Exception as e:
            print(f"Wystąpił błąd: {e}")
            return None
