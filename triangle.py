"""
Mohamed HABBAAINA, le 18 oct 2022
Écrire un programme triangle.py qui affiche dans le terminal un triangle avec des ‘_’, des
‘\’ et des ‘/’
en fonction de l’input entré, qui représentera la hauteur.
"""
H = int(input("Entrée la hauteur du triangle svp: "))
if H == 0:
    print("ERREUR")
    exit()

s = 1
y, z = H - 1, 0
while s <= H:

    if s == H:
        print(y*" ", end="")
        print("/",end="")
        print(z*"_",end="")
        print("\\")
    else:
        print(y*" ", end="")
        print("/",end="")
        print(z*" ",end="")
        print("\\")
    s+=1
    y-=1
    z+=2