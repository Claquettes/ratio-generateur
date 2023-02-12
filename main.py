from tkinter import *

import string  
import random
# on importe le fichier ratio.txt, qui est dans le même dossier que main.py, sachant qu'on sépare le contenu du fichier à chaque caractèrte "+"
with open("leratio.txt", "r") as f:
    ratio = f.read().split("+")

#on génère une chaine de caractère aléatoire contenant 15 des mots de ratio.txt
def ratioUltime():
    ratioUltime = ""
    for i in range(20):
        ratioUltime += random.choice(ratio) + "+"
    return ratioUltime

##print('Déguste moi ce délicieux ratio ' +  ratioUltime() + 'polymanu is better than you')

# on crée la fenêtre
window = Tk()
window.title("Ratio Ultime")
window.geometry("200x500")

#on ajoute un bouton pour quitter l'application
button2 = Button(window, text="Quitter", command=window.quit).pack()

label = Label(window, text=ratioUltime(), wraplength=100).pack()
#on ajoute un bouton pour coier le ratio dans le presse papier de l'utilisateur, sous forme de texte
button3 = Button(window, text="Copier le ratio", command=window.clipboard_append(ratioUltime())).pack()

window.mainloop()