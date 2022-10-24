"""
Mohamed HABBAAINA, le 19 oct 2022
Créer un programme job12.py qui parcourt le contenu du fichier “data.txt” et qui compte
le nombre de mots (sans caractère spéciaux) qui s’y trouvent.
"""
import re
with open('data.txt', "r") as f:
    texte = f.read()
    paramtr = '[a-zA-Z]+'
    reg = re.findall(paramtr,texte)
    print(len(reg))