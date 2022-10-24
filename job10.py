"""
Mohamed HABBAAINA, le 18 oct 2022
Écrire un programme job10.py qui demande à l’utilisateur d’entrer un texte. Le
programme devra récupérer ce texte, et l’écrire dans un fichier “output.txt”.
Écrire un programme qui lit le contenu de fichier “output.txt”, et qui l’écrit dans le
terminal."""
#la lecture du texte
texte = input("Entrer le texte ici SVP: ")
#criation du fichier output.txt
file = open('output.txt', 'w')
file.write(texte)
file.close()
#l'affichage de contenue du fichier 
print(texte)