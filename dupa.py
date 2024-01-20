import tkinter as tk
from tkinter import simpledialog, messagebox

def pobierz_tekst():
    return pole_tekstowe.get()

def pokaz_alert():
    wprowadzony_tekst = pobierz_tekst()

    if not wprowadzony_tekst:
        messagebox.showerror("Błąd", "Pole tekstowe nie może być puste!")
    else:
        messagebox.showinfo("Wprowadzony Tekst", f"Tekst wprowadzony: {wprowadzony_tekst}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Okno Alertu")

    pole_tekstowe = tk.Entry(root, width=30)
    pole_tekstowe.pack(pady=10)

    przycisk_alertu = tk.Button(root, text="Pokaż Alert", command=pokaz_alert)
    przycisk_alertu.pack()

    root.mainloop()
