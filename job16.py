"""
Mohamed HABBAAINA, le 19 oct 2022
Créer un programme job16.py. Le programme devra contenir une fonction qui prend en
paramètres un nombre de paramètres indéfini.
La fonction écrira tous les paramètres dans le terminal.
"""
def MyFonction(*parametres):
    print(parametres)
MyFonction("coucou", "5", "allo")