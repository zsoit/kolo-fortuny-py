# importowanie bibliotek

import tkinter as tk
from tkinter import messagebox
import random

from src.Gui import Gui
from src.konfiguracja import KATEGORIE, HASLA, SEKTORY

class KoloFortuny(Gui):
    def __init__(self, root):

        self.kategorie = KATEGORIE
        self.hasla = HASLA
        self.kategoria = ""
        self.haslo = ""
        self.aktualne_haslo = []

        self.pieniadze = 0
        self.runda = 1
        self.litery_odgadniete = set()
        self.nieprawidlowe_litery = set()
        self.ruchy_w_rundzie = 0  # Licznik ruchów w danej rundzie
        self.limit_ruchow = 1  # Limit ruchów na jedną rundę

        super().__init__(root) #dziedziczenie konstruktora z klasy Gui

    def alert(self, tytul, tresc):
        messagebox.showinfo(tytul,tresc)

    def nowa_gra(self):
        self.kategoria = random.choice(self.kategorie)
        self.haslo = random.choice(self.hasla[self.kategoria]).upper()
        self.aktualne_haslo = ["_" if litera.isalpha() else litera for litera in self.haslo]
        self.litery_odgadniete.clear()
        self.nieprawidlowe_litery.clear()
        self.ruchy_w_rundzie = 0
        self.limit_ruchow = 1  # Resetujemy limit ruchów
        self.aktualizuj_interfejs()
        self.przycisk_obrotu.config(state=tk.NORMAL)  # Ustawiamy przycisk "Obróć kołem" na aktywny

    def obroc_kolo(self):
        if self.ruchy_w_rundzie < self.limit_ruchow:
            sektory = SEKTORY
            wylosowany_sektor = random.choice(sektory)

            self.alert("Wynik", f"Wylosowany sektor: {wylosowany_sektor}")

            if wylosowany_sektor == "Bankrut":
                self.pieniadze = 0
                self.ruchy_w_rundzie = 0  # Resetujemy licznik ruchów po bankructwie
                self.limit_ruchow = 1  # Resetujemy limit ruchów po bankructwie
            elif wylosowany_sektor.isdigit():
                self.pieniadze += int(wylosowany_sektor)
            elif wylosowany_sektor == "Dodatkowy Ruch":
                self.limit_ruchow += 1

            self.ruchy_w_rundzie += 1
            self.aktualizuj_interfejs()

    def zgadnij_litere(self):
        wprowadzona_litera = self.entry_zgadywania.get().upper()
        self.entry_zgadywania.delete(0, tk.END)

        if wprowadzona_litera not in self.litery_odgadniete and wprowadzona_litera not in self.nieprawidlowe_litery:
            if self.sprawdz_poprawnosc(wprowadzona_litera):
                self.litery_odgadniete.add(wprowadzona_litera)
                self.ruchy_w_rundzie += 1
            else:
                self.nieprawidlowe_litery.add(wprowadzona_litera)
        else:
            self.alert("Błąd", "Ta litera została już wprowadzona!")

        self.aktualizuj_interfejs()

    def sprawdz_poprawnosc(self, litera):
        if litera.isalpha() and len(litera) == 1:
            if litera in self.haslo:

                self.alert("Wynik", f"Poprawna literka")
                self.pieniadze += 50  # Przyznajemy punkty za poprawną literę
                for i in range(len(self.haslo)):
                    if self.haslo[i] == litera:
                        self.aktualne_haslo[i] = litera
                if "_" not in self.aktualne_haslo:
                    if self.runda < 3:  # Możesz dostosować liczbę rund


                        self.alert("Gratulacje!", f"Hasło odgadnięte: {self.haslo}\nPieniądze: {self.pieniadze}")
                        self.runda += 1
                        self.label_runda.config(text=f"Runda: {self.runda}")
                        self.nowa_gra()
                    else:
                        self.alert("Gratulacje!", f"Hasło odgadnięte: {self.haslo}\nKoniec gry!\nPieniądze: {self.pieniadze}")
                        # self.root.quit()
                return True
            else:
                self.alert("Wynik", f"Niepoprawna literka")
                return False
        else:
            self.alert("Błąd", "Wprowadź pojedynczą literę!")
            return False

    def aktualizuj_interfejs(self):
        self.label_haslo.config(text=f"Hasło: {' '.join(self.aktualne_haslo)}\nKategoria: {self.kategoria}")
        self.label_pieniadze.config(text=f"Pieniądze: {self.pieniadze}")
        self.label_nieprawidlowe_litery.config(text=f"Nieprawidłowe litery: {' '.join(self.nieprawidlowe_litery)}")
        self.label_ruchy_w_rundzie.config(text=f"Ruchy w rundzie: {self.ruchy_w_rundzie}")
        self.przycisk_obrotu.config(state=tk.NORMAL if self.ruchy_w_rundzie < self.limit_ruchow else tk.DISABLED)