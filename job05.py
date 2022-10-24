"""
mohamed, le 17 oct 2022
Créez un script job05.py
L’utilisateur devra entrer deux valeurs en input.
A l’aide d’une boucle for et d’une fonction system, affichez uniquement les nombres se
trouvant entre l’input 1 et l’input 2. Le programme doit toujours partir de l’input 1 et
aller jusqu’à l’input 2.
Si les deux sont égaux, le programme devra écrire “Valeurs égales”.
"""
#declaration des variable a rentrer
x = input("entré le premier chiffre SVP  ")
x = int(x)
y = input("entré le deuxième chiffre SVP  ")
y = int(y)
#si les variable sont egaux
if (x==y):
   print("Valeurs égales")
#si il doit faire un affichage croissan
elif (x < y):
    for i in range(x+1,y):
        print(i)
#si il doit faire un affichage decroissan
elif (x > y):
    for i in range(x-1,y,-1):
        print(i)