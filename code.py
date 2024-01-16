#message de bienvenue sur le jeux + animation
sous = [0]
def miser(sous):
    if sous > 0 and sous <= 300:
        return sous
    else:
        print("Vous ne pouvez pas miser plus de 300 €")
sous = int(input("Combien d'euros souhaitez-vous miser ? "))
miser(sous)
#fonction permettant de donner une mise #(voir à la fin de la partie gains/pertes

import random

cartes=['As', 'Deux', 'Trois', 'Quatre', 'Cinq', 'Six', 'Sept', 'Huit', 'Neuf', 'Dix', 'Valet', 'Dame', 'Roi']
symbole=[' de Pique', ' de Carreaux', ' de Coeur', " de Trèfle"]
random.randint(0, 12)


def tirage():
    val=[As, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand1=random.randint(0, 12)
    rand2=random.randint(0, 3)
    print("Vous avez", points, "points.")
    if rand1==0 and 11+points<21:
        valeur=int(input("Choisir une valeur entre 1 et 11"))
        while valeur!=1:
            valeur=0
            valeur=int(input("Choisir une valeur entre 1 et 11"))
    else:
        valeur=val[rand1]
    carte=cartes[rand1] + symbole[rand2]
    print(carte)
    return valeur

valeur=0
points=0
for i in range(20):
    valeur=(tirage())
    points+=valeur
print("Vous avez", points, "points")
