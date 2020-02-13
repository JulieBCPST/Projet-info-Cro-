## IMPORTATION
from random import *


## FONCTION INITIALISATION

#initialiser un tableau
def InitPlateau():
    #création du tableau avec une case
    tab = [0]*8

    #assignation sur chaque cases un tableau
    for i in range (0,8):
        tab[i] = [0]*8

    return tab

#initialiser les valeurs initiales
def SetUpPlateau(tab):
    #Extremitée haut gauche
    tab[0][0] = "J1" #J1
    tab[1][0] = "g1"
    tab[0][1] = "g1"

    #Extremitée bas droit
    extremite = len(tab)-1
    extremite2 = len(tab[extremite])-1

    tab[extremite][extremite2] = "J2" #J2
    tab[(extremite-1)][extremite2] = "g2"
    tab[extremite][(extremite2-1)] = "g2"

    return tab


def CreateTasCarte():
    #Initialisation des cartes
    C1 = ["nenuphar"]*17
    C2 = ["roseau"]*14
    C3 = ["insecte"]*14
    C4 = ["vase"]*6
    C5 = ["brochets"]*6
    C6 = ["mâle"]*7
    TasC = C1 + C2 + C3 + C4 + C5 + C6

    tailleTas = len(TasC) #taille du tas

    TasMelanger = [0] * tailleTas #Création d'un tas vide (à la même taille du tas précédent)

    #Fonction de mélange
    for i in range(0,tailleTas):
        valAlea = randint(0,len(TasC)-1) #valeur aléatoire
        TasMelanger[i] = TasC[valAlea] #ajout de la carte choisi
        del(TasC[valAlea]) #suppression de la carte

    return TasMelanger


#Affichage du plateau
def AffichePlateau(tab):
    ESPACE = 4 #nombres d'espaces entre les collones
    RETOUR_LIGNE = 2 #nombres d'espaces entre les lignes
    print("")
    for i in range (0,len(tab)):
        for j in range (0,len(tab[i])):
            nbChar = len(str(tab[i][j])) #compte le nombre de caractères dans cette case

            #Ajoute les espaces manquants
            while(ESPACE > nbChar):
                print("",end=" ")
                nbChar = nbChar+1
            #EndWhile

            #Affiche le contenue du résultat
            print(tab[i][j],end="")
        #EndFor

        for r in range(0,RETOUR_LIGNE):
            print("")
        #EndFor
    #EndFor


## FONCTION DE TEST

# A NE PAS PRENDRE EN COMPTE
def AfficheTab(tab):
    for i in range (0,len(tab)):
        print(tab[i])

# A NE PAS PRENDRE EN COMPTE
def AfficheTabColumn(tab):
    for i in range (0,len(tab)):
        for j in range (0,len(tab[i])):
            print(tab[i][j],end="")
        print("")



tab = InitPlateau()
#AfficheTab(tab)
tab = SetUpPlateau(tab)
AffichePlateau(tab)
