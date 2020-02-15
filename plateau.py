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
    C1 = ["Nenuphar"]*17
    C2 = ["Roseau"]*14
    C3 = ["Insecte"]*14
    C4 = ["Vase"]*6
    C5 = ["Brochets"]*6
    C6 = ["Mâle"]*7
    TasC = C1 + C2 + C3 + C4 + C5 + C6

    tailleTas = len(TasC) #taille du tas

    TasMelanger = [0] * tailleTas #Création d'un tas vide (à la même taille du tas précédent)

    #Fonction de mélange
    for i in range(0,tailleTas):
        valAlea = randint(0,len(TasC)-1) #valeur aléatoire
        TasMelanger[i] = TasC[valAlea] #ajout de la carte choisi
        del(TasC[valAlea]) #suppression de la carte

    tableaucarte = InitPlateau() # création d'un tableau vide
    index = 0 # indice suivant la progression sur TasMélanger

    for i in range (0,len(tableaucarte)): # parcours les colonnes
        for j in range (0,len(tableaucarte[i])): #parcours les lignes
            tableaucarte[i][j] = TasMelanger[index][0] #convertir la liste TasMelanger en tableau affichable
            index += 1 #fais évoluer l'indice


    return tableaucarte # retourne le tableau de carte

##Fonction d'affichage


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


def AffichageCarte(tabCarte,tabVisi): # tableau des cartes révélées
    tabResult = InitPlateau() #initialisation du plateau
    for i in range (0,len(tabCarte)): #on parcourt les colonnes
        for j in range (0,len(tabCarte[i])): #on parcourt les lignes
            if tabVisi[i][j] == 1:#1=la carte a été révélée
                tabResult[i][j]=tabCarte[i][j]#on rajoute la carte au tableau si elle a été révélée
            else :
                tabResult[i][j]='*'#la carte n'a pas été révélée
    AffichePlateau(tabResult)#on affiche le tableau des cartes révélées

## Fonction de jeu

def Choixpion():#demande au joueur s'il veut changer de vision de plateau, jouer le pion qu'on lui propose ou demander qu'on lui propose un autre pion
    rep=-1
    while rep!=0 or rep!=1 or rep !=2 :#évite que rep prenne une autre valeur que celle demandée
        rep=input("0 = jouer ce pion, 1 = choisir un autre pion, 2 = afficher une autre face du plateau")
    return rep

def Dircolonne (col):
    possibilite = False
    while possibilite == False:
        dircol=2
        while (dircol != 0 and dircol != 1 and dircol != -1):
            dircol = int(input("-1 = aller à gauche, 0 = rester dans cette colonne, 1 = aller à droite : "))

        if (dircol==-1 and col==0) or (dircol==1 and col==7):
            possibilite = False
            print ("La bataille ne se déroule que dans la mare, veuillez ne pas rejoindre la terre ferme. Choisissez un autre déplacement.")
        else :
            possibilite = True
    return dircol

def Dirligne (lig):
    possibilite = False
    while possibilite == False:
        dirlig=2
        while (dirlig != -1 and dirlig != 0 and dirlig != 1):
            dirlig = int(input("-1 = aller en haut, 0 = rester dans cette ligne, 1 = aller en bas : "))
        if (dirlig == -1 and lig == 0) or (dirlig == 1 and lig == 7):
            possibilite = False
            print ("Vous ne pouvez pas faire ça, veuillez rentrer un autre déplacement")
        else :
            possibilite = True
    return dirlig

def Deplacementverifjoueur (lig, col, plateau):
    collision = True
    while collision :
        possibilite = False

        while possibilite == False :
            dirlig = Dirligne(lig)
            dircol = Dircolonne(col)

            if ( dircol==0 and dirlig==0):
                possibilite = False
                print ("Vous n'êtes pas une vraie grenouille, veuillez ne pas sauter votre tour")
            else :
                possibilite = True

        if plateau[col + dircol][lig + dirlig] == "J1" or plateau[col + dircol][lig + dirlig] == "g1":
            collision = True
            print("Le cannibalisme est autorisé uniquement entre grenouilles rivales" )
        else:
            collision = False
    return dirlig, dircol




## FONCTION DE TEST




tab = InitPlateau()
plateau = SetUpPlateau(tab)
Deplacementverifjoueur(0,0,plateau)