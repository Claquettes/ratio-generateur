import random
from tkinter import Tk, Button, Label

# on importe le fichier ratio.txt, qui est dans le même dossier que main.py
# on sépare le contenu du fichier à chaque caractèrte "+"
with open("leratio.txt", "r") as f:
    ratio = f.read().split("+")


# on génère une chaine de caractère aléatoire contenant 15 des mots de ratio.txt
def ratio_ultime():
    return "+".join(random.choices(ratio, k=20))


window = Tk()
window.title("Ratio Ultime")
window.geometry("200x500")

# on ajoute un bouton pour quitter l'application
Button(window, text="Quitter", command=window.quit).pack()

Label(window, text=ratio_ultime(), wraplength=100).pack()
# on ajoute un bouton pour coier le ratio dans le presse papier de l'utilisateur, sous forme de texte
Button(window, text="Copier le ratio", command=lambda: window.clipboard_append(ratio_ultime())).pack()

window.mainloop()
