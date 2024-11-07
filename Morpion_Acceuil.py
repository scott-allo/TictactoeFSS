"""Morpion en Python : Terminal Edition"""

"""Séléction du mode de jeu."""

#Début de la "boucle de démarrage"
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

    status = True #Fin de la boucle de séléction