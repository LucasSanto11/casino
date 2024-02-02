#ceci est mon code fonctionnel avec la fonction croupier fonctionnelle mais sans mise ni sans la partie "rester":
print("Bienvenue au Blackjack") #message de bienvenue sur le jeux + animation après
#définition des variables
sous = 0
valeur=0
points=0
points_croupier=0
saut='' #saut de ligne pour une meilleure visibilité dans la console, temporaire jusqu'à l'interface codée
def miser(sous):
    if sous > 0 and sous <= 300:
        return sous
    else:
        print("Vous ne pouvez pas miser plus de 300 €")
sous = int(input("Combien d'euros souhaitez-vous miser ? "))

miser(sous) #16/01/2024 fonction permettant de donner une mise (voir à la fin de la partie gains/pertes)


import random

As=0 #valeur temporaire à changer

cartes=['As', 'Deux', 'Trois', 'Quatre', 'Cinq', 'Six', 'Sept', 'Huit', 'Neuf', 'Dix', 'Valet', 'Dame', 'Roi']
symbole=[' de Pique', ' de Carreaux', ' de Coeur', " de Trèfle"]
random.randint(0, 12)



def tirage_croupier(): #finir + faire en sorte qu'il perde si il tire un as avec + de 17 points
    global points_croupier
    global valeur
    valeur=0
    val=[As, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand1=random.randint(0, 12)
    rand2=random.randint(0, 3)
    if: points_croupier>=17: #Si le croupier a 17 points, il ne tire plus de cartes
        #aucune action du croupier

    else: #Si le croupier a moins de 17 points, il tire une carte
        if rand1==0 and 11+points<21: #si on tire un as et que nb points + 11 est inférieur à 21
            if random.randint(1,2) == 1: #choisit aléatoirement une valeur pour l'as
                valeur=1
            elif random.randint(1,2) == 2:
                valeur=11
            else:
                valeur=1
        else:
            valeur=val[rand1]
        carte=cartes[rand1] + symbole[rand2]
        print("////////")
        print("Le croupier a tiré:", carte)
        points_croupier+=valeur
        print("Le croupier a", points_croupier, "points.")
        print("////////")
        print('')
        valeur_croupier=0 #réinitialise la valeur avant le prochain tirage
        return valeur

def tirage(): #fonction permettant de tirer une carte, annonce la carte et le nombre de points
    global points
    val=[As, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand1=random.randint(0, 12)
    rand2=random.randint(0, 3)
    if rand1==0 and 11+points<21: #si on tire un as et que nb points + 11 est inférieur à 21
        print(saut) #Saute une ligne > pour la visibilité
        print("Vous avez tiré un AS, choisissez une valeur entre 1 et 11")
        valeur=int(input("Choisir une valeur entre 1 et 11"))
        while valeur!=1 and valeur!=11:
            valeur=0
            valeur=int(input("Choisissez une valeur, 1 OU 11"))
    elif rand1==0 and 11+points>21:
        valeur=1
    else:
        valeur=val[rand1]
    carte=cartes[rand1] + symbole[rand2]
    print(saut) #Saute une ligne > pour la visibilité
    print("Vous avez tiré:", carte)
    points+=valeur
    print("Vous avez", points, "points.")
    valeur=0 #réinitialise la valeur avant le prochain tirage
    tirage_croupier()
    return valeur

    #mettre la fonction tirage croupier pour faire tirer une carte au croupier automatiquement après que le joueur ait tiré une carte

def newgame():
    global points
    global valeur
    points=0
    valeur=0
    points_croupier=0
    print("Voulez vous relancer une partie ?")
    rep1=input("Oui/non")
    while rep1.lower()!="oui" and "non":
        rep1=input("Oui/non")

    if rep1.lower()=="oui":
        print(saut) #Saute une ligne > pour la visibilité
        print("Nouvelle partie, vous avez 0 points")
        for i in range(2):
            valeur=(tirage())
            points+=valeur
        rejeu()

    elif rep1.lower()=="non":
        print("Merci d'avoir joué.")


def rejeu():
    global points
    print(saut) #Saute une ligne > pour la visibilité
    print("Tirer ou rester ?") #à la fin de la fonction croupier demander au joueur de jouer
    rep=input("Tirer ou rester ?")
    while rep.lower()!="tirer" and rep.lower()!="rester":
        rep=input("Tirer ou rester ?")
    if rep.lower()=="tirer": #si le joueur décide de tirer une carte
        print(saut) #Saute une ligne > pour la visibilité
        valeur=(tirage())
        points+=valeur
        if points<21:
            rejeu()
        elif points>21:
            print("Vous avez dépassé 21 points")
            newgame()
        elif points==21:
            print("Vous avez", points, "points, vous avez gagné")
            newgame()

    else: #si le joueur décide de rester
        if points<points_croupier: #Si le joueur a moins de points que le croupier
             print ('Oh mince, vous avez perdu votre mise, vous n*avez plus rien !')
        else : #Si le joueur a plus de points que le croupier
             sous=2*sous
             print('Bravo, vous avez gagné :) ! Votre mise est maintenant de', sous,'!')

        rep=input("Voulez vous rejouer et tenter d'obtenir un gain plus conséquent :) ? Répondez par 'OUI' ou 'NON' ") #Le joueur choisit si il veut relancer
        while upper.rep()!="OUI" and upper.rep()!="NON":
            rep=input("Voulez vous rejouer et tenter d'obtenir un gain plus conséquent :) ? Répondez par 'OUI' ou 'NON' ")
        if rep=='OUI' :
                 print('On relance une partie alors!')
                 newgame()
        elif rep=='NON':
                 print('A bientôt! :)')
        else :
            rep=input("Voulez vous rejouer et tenter d'obtenir un gain plus conséquent :) ? Répondez par 'OUI' ou 'NON'")




#Lance la partie et tire deux cartes
for i in range(2):
    valeur=(tirage())
    points+=valeur
rejeu()
