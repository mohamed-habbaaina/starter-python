"""
Mohamed HABBAAINA, le 18 oct 2022
Créer un programme job11.py qui parcourt le contenu du fichier “domains.xml” et qui
compte le nombre de noms de domaine.
"""
with open('domains.xml', "r") as f:
    cc = f.read()
a = cc.count('name="domain">')
print(a)
f.close()