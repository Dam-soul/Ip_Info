import tkinter as tk
import ipaddress
from tkinter import messagebox


root = tk.Tk()
root.title("Adresse IP")
root.geometry("400x400")
root.resizable(False, False)
root.config(bg="#12AE9B")


def Survol_avant(event):
    event.widget.config(bg="#12AE9B", fg="white")

def Survol_apres(event):
    event.widget.config(bg="white", fg="black")


def Verification():
    try:
        adresse = entree.get()
        ip = ipaddress.IPv4Address(adresse)

        octet1 = int(str(ip).split(".")[0])

        if 1<=octet1<=126:
            masque = ipaddress.IPv4Network("0.0.0.0/8").netmask

            affichage.delete(0, tk.END)
            affichage.insert(0, f"Adresse : {adresse}")
            affichage.insert(1,"Classe A")
            affichage.insert(2,f"Masque de sous réseau : {masque}")
        elif 128<=octet1<=191:
            masque = ipaddress.IPv4Network("0.0.0.0/16").netmask
            affichage.delete(0, tk.END)
            affichage.insert(0, f"Adresse : {adresse}")
            affichage.insert(1,"Classe B")
            affichage.insert(2,f"Masque de sous réseau : {masque}")
        elif 192<=octet1<=223:
            masque = ipaddress.IPv4Network("0.0.0.0/24").netmask

            affichage.delete(0, tk.END)
            affichage.insert(0, f"Adresse : {adresse}")
            affichage.insert(1,"Classe C")
            affichage.insert(2,f"Masque de sous réseau : {masque}")
        elif 224<=octet1<=239:

            affichage.delete(0, tk.END)
            affichage.insert(0, f"Adresse : {adresse}")
            affichage.insert(1, "Classe D")
            affichage.insert(2, "Adresse utilisée pour le multicast, donc pas de masque classique.")
        else:
            classe = 'E'
            affichage.delete(0, tk.END)
            affichage.insert(0, f"Adresse : {adresse}")
            affichage.insert(1, f"Classe :  {classe}")
            affichage.insert(2, "Adresse réservée pour la recherche expérimentale")
    except:
        messagebox.showerror("Erreur", "Votre adresse IP n'est pas correcte")




label = tk.Label(root, text="Adresse IP:", font=("Alcoholics Anonymous", 19), bg="#12AE9B")
label.place(x=0, y=8)
entree = tk.Entry(root, width=20, font=("Arial Black", 12))
entree.place(x=93, y=10, height=30)
entree.focus()

button = tk.Button(root, text="Vérifier", command=Verification, cursor="hand2")
button.place(x=320, y=11, height=30,width=70)
button.bind("<Enter>", Survol_avant)
button.bind("<Leave>", Survol_apres)

affichage = tk.Listbox(root, width=65, height=15)
affichage.place(x=4, y=100)

affichage.config(font=("Arial", 12))






root.mainloop()