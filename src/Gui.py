# importowanie bibliotek
import tkinter as tk
from tkinter import ttk

from src.konfiguracja import NAZWA_APLIKACJI, AUTOR

class Gui:
      def __init__(self, root):
        self.root = root
        self.okno_aplikacji(root)
        self.naglowek_informacyjny(root)
        self.przycisk_obroc(root)
        self.przycisk_zgadywania(root)

        # pola z etykietami
        self.label_haslo(root)
        self.label_pieniadze(root)
        self.label_runda(root)
        self.label_nieprawidlowe_litery(root)
        self.label_ruchy_w_rundzie(root)

        self.nowa_gra()
      
      def okno_aplikacji(self, root):
          self.root.title(NAZWA_APLIKACJI + " - " + AUTOR)
          self.kolo = tk.Canvas(root, width=200, height=150)
          self.kolo.pack()
          
      def naglowek_informacyjny(self,root):
          self.label_naglowek = tk.Label(root, text=NAZWA_APLIKACJI, font=("Helvetica", 20))
          self.label_info = tk.Label(root, text=AUTOR, font=("Helvetica", 10))
          self.label_info.pack(pady=50)

          self.label_naglowek.pack(pady=50)

      def przycisk_obroc(self,root):
          self.przycisk_obrotu = tk.Button(root, text="Obróć kołem", command=self.obroc_kolo)
          self.przycisk_obrotu.pack()

      def przycisk_zgadywania(self, root):
        self.przycisk_zgadywania = tk.Button(root, text="Zgadnij literę", command=self.zgadnij_litere)
        self.przycisk_zgadywania.pack()

        self.entry_zgadywania = ttk.Entry(root)
        self.entry_zgadywania.pack(pady=50)

      def label_haslo(self, root):
        self.label_haslo = tk.Label(root, text="Hasło: ", font=("Helvetica", 30))
        self.label_haslo.pack(pady=50)

      def label_pieniadze(self, root):
          self.label_pieniadze = tk.Label(root, text="Pieniądze: 0")
          self.label_pieniadze.pack()
         
      def label_runda(self, root):
          self.label_runda = tk.Label(root, text="Runda: 1")
          self.label_runda.pack()
         
      def label_nieprawidlowe_litery(self, root):
          self.label_nieprawidlowe_litery = tk.Label(root, text="Nieprawidłowe litery: ")
          self.label_nieprawidlowe_litery.pack()
         
      def label_ruchy_w_rundzie(self, root):
          self.label_ruchy_w_rundzie = tk.Label(root, text="Ruchy w rundzie: 0")
          self.label_ruchy_w_rundzie.pack()   
      

