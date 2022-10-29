"""
Mohamed HABBAAINA, le 19 oct 2022
Créer un programme job19.py. Le programme devra contenir une seule fonction qui
prend en paramètres un nombre de paramètres indéfini (uniquement des nombres).
La fonction devra :
- Remplir une liste myList contenant tous ces paramètres.
- Trier par ordre croissant la liste sans *la fonction sort*
- Afficher la liste dans un terminal
"""
from itertools import permutations


def myFunction ( *params ):
    myList = []

    for param in params:
        if isinstance(param,(int)):
            myList.append(param)
        else:
            print("Le programme reconnaît uniquemnt les nombres")
    
    permutation = True
    passage =0
	
    while permutation == True:
        
        permutation = False
        passage = passage + 1
        
        for en_cours in range(0, len(myList) - passage):
            if myList[en_cours] > myList[en_cours + 1]:
                permutation = True
                myList[en_cours],  myList[en_cours + 1] =\
                myList[en_cours + 1],myList[en_cours]
    print (myList)

Myfonction(2, 8, 9, 7, -8, "lkl", 0, 122)
