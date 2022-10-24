"""
Mohamed HABBAAINA, le 17 oct 2022
Écrire un programme rectangle.py qui attend deux inputs : la largeur puis la hauteur.
Votre programme devra ensuite dessiner un rectangle avec les éléments suivants :
- des “|” pour dessiner les côtés droite et gauche
- des “-” pour dessiner le haut et le bas
- des espaces pour remplir le rectangle 
"""
from mimetypes import init


L = int(input("Entrée la langueur du rectangle SVP:  "))
H = int(input("Entrée la hauteur de rectangle SVP  "))
for i in range(H):
    for j in range(L):
        if i == 0 or i == H-1:
            print("-",end="")
        elif j==0 or j==L-1:
            print("|",end="")
        else:
            print(" ",end="")

    print()

        