"""
Mohamed HABBAAINA, le 18 oct 2022.
Écrire un programme qui parcourt les nombres entiers de 1 à 100. Pour les multiples de
trois, afficher "Fizz" au lieu du nombre et pour les multiples de cinq afficher "Buzz". Pour
les nombres qui sont des multiples de trois et cinq, afficher "FizzBuzz".
"""
for i in range(1,101):
#multiples de 3 et 5 au meme tempt.
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
#multiples de 3.
    elif i%3 == 0:
        print("Fizz")
#multiples de 5.
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)