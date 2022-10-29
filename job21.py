"""
Mohamed HABBAAINA, le 19 oct 2022
Créer un programme job21.py. Reprenez l’exercice 19, mais modifiez le de façon à
utiliser deux fonctions :
- Une fonction mySort, qui prendra en paramètre une liste. Elle retourne une liste
avec les valeurs de celle passée en paramètre, triés par ordre croissant.
- Une fonction myDisplay qui prendra en paramètre une liste. Elle affichera dans le
terminal le contenu de cette liste.
"""
def my_function(*nombre:int):
    #Ma liste de nombre      
    num = [*nombre]
    #Création des boucles 
    for i in range(len(num)):
        for j in range(len(num)):

            #If ce nombre i est plus petit que le nombre j dans une liste
            if num[i] < num[j]:

                #Puis on inverse les nombres de la liste par ordre croissant
                num[i], num[j] = num[j], num[i]
    #Résultat
    return num
def myDisplay(nombre2):
        print(nombre2)
#Test
myDisplay(my_function(78, 15, 27, 23))

