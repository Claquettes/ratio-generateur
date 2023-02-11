import string  
import random
# on importe le fichier ratio.txt, qui est dans le même dossier que main.py, sachant qu'on sépare le contenu du fichier à chaque caractèrte "+"
with open("ratio.txt", "r") as f:
    ratio = f.read().split("+")

#on génère une chaine de caractère aléatoire contenant 15 des mots de ratio.txt
def ratioUltime():
    ratioUltime = ""
    for i in range(15):
        ratioUltime += random.choice(ratio) + "+"
    return ratioUltime

print('Déguste moi ce délicieux ratio ' +  ratioUltime() + 'polymanu is better than you')



