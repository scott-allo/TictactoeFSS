"""Morpion en Python : Terminal Edition"""

"""Pas de POO pour le moment."""

"""Séléction du mode de jeu."""

status = False

while status != True:

    print( 

        "Séléctionnez le mode de jeu : " "\n"
        "1 : Joueur contre Joueur." "\n"
        "2 : Joueur contre IA" "\n"

    )

    #Séléction du mode
    select = int(input("Mode choisi : "))


    if select == 2:
        print("En développement. Veuillez patientez...")
        break

    """Mode Joueur contre Joueur"""

    """Séléction camp"""

    print(
        "\n"
        "Veuillez séléctionner votre camp : " "\n"
        "Croix = O" "\n"
        "Ronds = X"
    )

    joueur_1 = input("Joueur 1 : ")
    joueur_2 = None

    if joueur_1 == "X":
        joueur_2 = "O"

    if joueur_1 == "O":
        joueur_2 = "X"

    print("Joueur 2 :",joueur_2)

    """Formation de la grille"""

    grille = [0,1,2,3,4,5,6,7,8]

    def grille():
        pass

    """Gestion de la partie"""
    win = False #Par défault, personne ne gagne.
    tour = 1 #Note : il y a 9 tours

    def positions():
        pass

    def check_win():
        """Vérifie si il y a un alignement de croix/ronds."""
        global win #On ramène la variable win dans la fonction
        return win