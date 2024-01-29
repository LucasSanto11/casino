ueprint("Bienvenue au Blackjack") #message de bienvenue sur le jeux + animation après
sous = 0
valeur=0
points=0
def miser(sous):
    if sous > 0 and sous <= 300:
        return sous
    else:
        print("Vous ne pouvez pas miser plus de 300 €")
sous = int(input("Combien d'euros souhaitez-vous miser ? "))
miser(sous) #16/01/2024 fonction permettant de donner une mise (voir à la fin de la partie gains/pertes)


import random

As=11 #valeur temporaire à changer

cartes=['As', 'Deux', 'Trois', 'Quatre', 'Cinq', 'Six', 'Sept', 'Huit', 'Neuf', 'Dix', 'Valet', 'Dame', 'Roi']
symbole=[' de Pique', ' de Carreaux', ' de Coeur', " de Trèfle"]
random.randint(0, 12)

def tirage():
    val=[As, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand1=random.randint(0, 12)
    rand2=random.randint(0, 3)
    print("Vous avez", points, "points.")
    if rand1==0 and 11+points<21: #si on tire un as et que nb points + 11 est inférieur à 21
        valeur=int(input("Choisir une valeur entre 1 et 11"))
        while valeur!=1 and valeur!=11:
            valeur=0
            valeur=int(input("Choisir une valeur entre 1 et 11"))
    else:
        valeur=val[rand1]
    carte=cartes[rand1] + symbole[rand2]
    print(carte)
    return valeur

def newgame():
    global points
    global valeur
    print("Voulez vous relancer une partie ?")
    rep1=input("Oui/non")
    while rep1.lower()!="oui" and "non":
        rep1=input("Oui/non")

    if rep1.lower()=="oui":
        points=0
        valeur=0
        print("Nouvelle partie, vous avez 0 points")
        valeur=(tirage())
        points+=valeur
        print("Vous avez", points, "points")
        rejeu()

    elif rep1.lower()=="non":
        print("Merci d'avoir joué.")


def rejeu():
    global points
    print("Tirer ou rester ?") #à la fin de la fonction croupier demander au joueur de jouer
    rep=input("Tirer ou rester ?")
    if rep.lower()=="tirer":
        valeur=(tirage())
        points+=valeur
        if points<21:
            print("Vous avez", points, "points")
            newgame()
        elif points>21:
            print("Vous avez", points, "points, vous avez dépassé 21 points")
            newgame()
        elif points==21:
            print("Vous avez", points, "points, vous avez gagné")
            newgame()

    else:
        if valeur_joueur<valeur_croupier:
             print ('Oh mince, vous avez perdu votre mise, vous n*avez plus rien !')
        else :
             sous=2*sous
             print('Bravo, vous avez gagné :) ! Votre mise est maintenant de', sous,'!')
         rep=input("Voulez vous rejouer et tenter d'obtenir un gain plus conséquent :) ? Répondez par 'OUI' ou 'NON' ")
         if rep=='OUI' :
                 print('On relance une partie alors!')
                 nouvelle_part=rnewgame()
          elif rep=='NON':
                 print('A bientôt! :)')
          else :
               rep=input("Voulez vous rejouer et tenter d'obtenir un gain plus conséquent :) ? Répondez par 'OUI' ou 'NON'")    


    


for i in range(2):
    valeur=(tirage())
    points+=valeur
print("Vous avez", points, "points")

def croupier_coup():
    global points
    valeur=(tirage())
    points+=valeur

    if points<21:
        print("J'ai", points, "points, dit le croupier")

    elif points>21:
        print("J'ai dépassé le nombre de", points, "points, vous avez gagné, dit le croupier")
        print("Voulez vous relancer une partie ?")
#Si le croupier tire des cartes et que la valeur de sa main dépasse 21, il perd automatiquement la partie, et tous les joueurs restants encore en jeu gagnent.


    if valeur == rand1 and points>=17:#Si le croupier reçoit une main contenant un As et un total de 17 points ou plus, il doit également s'arrêter de tirer des cartes (appelé "soft 17 rule").

        print("Vous avez gagné")#importer la fonction qui fructifie la mise
        print("Voulez vous relancer une partie ?")
        break
    print("A votre tour de jouer")
    rejeu()
#il faut mettre une fonction arrêt pour que joueur et croupier compare leurs cartes et se départage

croupier_coup()
#Si la main du croupier a une valeur supérieure à celle du joueur, le croupier remporte la mise du joueur. Si la main du joueur a une valeur supérieure à celle du croupier, le joueur gagne la mise. En cas d'égalité (main de même valeur), c'est un "push", le joueur récupère sa mise initiale sans gagner ni perdre.
#29/01/2024 ben

