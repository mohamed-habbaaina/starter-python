"""
Mohamed HABBAAINA, le 19 oct 2022
Créer un programme job17.py. Le programme devra contenir une fonction qui prend en
paramètres un nombre de paramètres indéfini (uniquement des nombres).
La fonction devra :
- Remplir une liste myList contenant tous ces paramètres.
- Parcourir et afficher dans le terminal uniquement les nombres pairs de la liste.
"""
def Myfonction(*parametres):
    my_list = []
    for param in parametres:
        if isinstance(param, (int)):
           my_list.append(param)
        else:
            print("ERREUR")
    for list in my_list:
        if list %2 == 0:
            print(list)
Myfonction(2, 8, 9, 7, -8, 0, "toto", 122)