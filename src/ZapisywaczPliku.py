class ZapisywaczDoPliku:
    def __init__(self, sciezka_do_pliku):
        self.sciezka_do_pliku = sciezka_do_pliku

    def zapisz_linie(self, linia_tekstu):
        with open(self.sciezka_do_pliku, 'a') as plik:
            plik.write(f"{linia_tekstu}\n")