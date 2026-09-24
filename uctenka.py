import tkinter as tk
from tkinter import messagebox

# JÍDLA A CENY

jidla = {
   "Hamburger": {
       "cena": 120,
       "popis": "Hovězí maso, houska, salát a omáčka."
   },
   "Cheeseburger": {
       "cena": 140,
       "popis": "Hovězí maso, sýr, houska a omáčka."
   },
   "Pizza": {
       "cena": 180,
       "popis": "Pizza se šunkou, sýrem a rajčatovým základem."
   },
   "Hranolky": {
       "cena": 60,
       "popis": "Křupavé smažené hranolky."
   },
   "Cola": {
       "cena": 40,
       "popis": "Chlazený nápoj Coca-Cola."
   },
   "Voda": {
       "cena": 25,
       "popis": "Neperlivá balená voda."
   }
}

kosik = []

# -------------------------
# OKNO S INFORMACEMI O JÍDLE
# -------------------------
def zobraz_jidlo(nazev):
   okno_jidla = tk.Toplevel(okno)
   okno_jidla.title(nazev)
   okno_jidla.geometry("350x250")
   tk.Label(
       okno_jidla,
       text=nazev,
       font=("Arial", 20, "bold")
   ).pack(pady=15)
   tk.Label(
       okno_jidla,
       text=jidla[nazev]["popis"],
       wraplength=300
   ).pack(pady=10)
   tk.Label(
       okno_jidla,
       text=f"Cena: {jidla[nazev]['cena']} Kč",
       font=("Arial", 14)
   ).pack(pady=10)
   tk.Button(
       okno_jidla,
       text="Přidat do košíku",
       command=lambda: pridat_do_kosiku(nazev, okno_jidla)
   ).pack(pady=10)

# -------------------------
# PŘIDÁNÍ DO KOŠÍKU
# -------------------------
def pridat_do_kosiku(nazev, okno_jidla):
   kosik.append(nazev)
   aktualizuj_kosik()
   okno_jidla.destroy()

# -------------------------
# AKTUALIZACE KOŠÍKU
# -------------------------
def aktualizuj_kosik():
   seznam.delete(0, tk.END)
   for jidlo in kosik:
       cena = jidla[jidlo]["cena"]
       seznam.insert(tk.END, f"{jidlo} - {cena} Kč")
   celkem = sum(jidla[jidlo]["cena"] for jidlo in kosik)
   cena_label.config(
       text=f"Celkem: {celkem} Kč"
   )

# -------------------------
# VYMAZÁNÍ KOŠÍKU
# -------------------------
def vymazat_kosik():
   kosik.clear()
   aktualizuj_kosik()

# -------------------------
# KOUPIT
# -------------------------
def koupit():
   if len(kosik) == 0:
       messagebox.showinfo(
           "Košík",
           "Košík je prázdný."
       )
       return
   celkem = sum(
       jidla[jidlo]["cena"]
       for jidlo in kosik
   )
   ucet = "ÚČTENKA\n\n"
   for jidlo in kosik:
       ucet += f"{jidlo} - {jidla[jidlo]['cena']} Kč\n"
   ucet += f"\nCelkem: {celkem} Kč"
   messagebox.showinfo(
       "Účtenka",
       ucet
   )

# =========================
# HLAVNÍ OKNO
# =========================
okno = tk.Tk()
okno.title("Pokladna")
okno.geometry("800x600")

# NADPIS
tk.Label(
   okno,
   text="RESTAURACE",
   font=("Arial", 28, "bold")
).pack(pady=20)

# HLAVNÍ ČÁST
hlavni_frame = tk.Frame(okno)
hlavni_frame.pack()

# LEVÁ STRANA - JÍDLA
jidla_frame = tk.Frame(hlavni_frame)
jidla_frame.grid(row=0, column=0, padx=30)

tk.Label(
   jidla_frame,
   text="Nabídka",
   font=("Arial", 18, "bold")
).pack(pady=10)

for nazev in jidla:
   tk.Button(
       jidla_frame,
       text=f"{nazev}\n{jidla[nazev]['cena']} Kč",
       width=20,
       height=2,
       command=lambda n=nazev: zobraz_jidlo(n)
   ).pack(pady=5)

# PRAVÁ STRANA - KOŠÍK
kosik_frame = tk.Frame(hlavni_frame)
kosik_frame.grid(row=0, column=1, padx=30)

tk.Label(
   kosik_frame,
   text="Košík",
   font=("Arial", 18, "bold")
).pack(pady=10)

seznam = tk.Listbox(
   kosik_frame,
   width=35,
   height=15
)
seznam.pack()

# CELKOVÁ CENA
cena_label = tk.Label(
   kosik_frame,
   text="Celkem: 0 Kč",
   font=("Arial", 16, "bold")
)
cena_label.pack(pady=10)

# TLAČÍTKA
tk.Button(
   kosik_frame,
   text="KOUPIT",
   width=25,
   height=2,
   command=koupit
).pack(pady=5)

tk.Button(
   kosik_frame,
   text="VYMAZAT KOŠÍK",
   width=25,
   height=2,
   command=vymazat_kosik
).pack(pady=5)

# SPUŠTĚNÍ
okno.mainloop()