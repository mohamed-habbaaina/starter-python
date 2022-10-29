"""
Mohamed HABBAAINA, le 19 oct 2022
Créer un programme job18.py. Le programme devra contenir une fonction qui prend en
paramètres un nombre de paramètres indéfini (uniquement des nombres).
La fonction devra :
- Remplir une liste myList contenant tous ces paramètres.
- Trier par ordre croissant la liste à l’aide de la fonction sort
- Afficher la liste dans un terminal
"""
def Myfonction(*parametres):
    my_list = []
    for param in parametres:
        if isinstance(param, (int)):
            my_list.append(param)
            my_list.sort()
        else:
            print("ERREUR")
    print(my_list)

Myfonction(2, 8, 9, 7, -8, "lkl", 0, 122)