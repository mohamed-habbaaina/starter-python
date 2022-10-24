"""
Mohamed HABBAAINA, le 19 oct 2022
Créer un programme job13.py qui demande à l’utilisateur de renseigner un nombre
entier. Le programme devra alors parcourir le contenu du fichier “data.txt” compter le
nombre de mots de la taille renseignée qui s’y trouvent.
"""
nombre = int(input("entrer le nombre SVP: "))
with open('data.txt', "r") as f:
    texte = f.read()
    liste = texte.split()
nub = 0
for test in liste:
    if len(test) == nombre:
        nub = nub + 1
print(nub)