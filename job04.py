"""
mohamed, le 17 oct 2022
Créez un script job04.py
L’utilisateur devra entrer une valeur en input.
A l’aide d’une boucle while et d’une fonction system, affichez nombres se trouvant de 0
(inclus) à l’input (inlus).
"""
x = input("entré un chiffre SVP   ")
x = int(x)
i = 0
while i < x+1:
    print(i)
    i += 1