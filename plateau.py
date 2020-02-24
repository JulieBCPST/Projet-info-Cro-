## IMPORTATION
from random import *
import time

## FONCTION INITIALISATION

plateau = []

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
    for i in range (0,len(tabCarte)): #on parcourt les lignes
        for j in range (0,len(tabCarte[i])): #on parcourt les collones
            if tabVisi[i][j] == 1:#1=la carte a été révélée
                tabResult[i][j]=tabCarte[i][j]#on rajoute la carte au tableau si elle a été révélée
            else :
                tabResult[i][j]='*'#la carte n'a pas été révélée
    AffichePlateau(tabResult)#on affiche le tableau des cartes révélées


def AffichePionSelectionne(tab,i,j):
    pion = tab[i][j] # récupère le pion
    tab[i][j] = "->" + pion # ajoute à la case une flèche pour montrer à l'utilisateur ce qui est sélectionné
    AffichePlateau(tab) # afficher le tableau avec le pion selectionné
    tab[i][j] = pion # rétablir la case en enlevant la flèche


def AffichePlateauAlterner(typePlateau,plateauPion,plateauCarte,tabVisi):
    if(typePlateau == -1): # si c'est -1 afficher les pions
        AffichePlateau(plateauPion)
    else:# si c'est 1 afficher les carte
        AffichageCarte(plateauCarte,tabVisi)


def AffichePlateauAlternerS(plateauPion,plateauCarte,tabVisi):
    AffichageCarte(plateauCarte,tabVisi) #afficher les cartes
    time.sleep(2) # attendre n secondes
    AffichePlateau(plateauPion) #afficher plateau



## Fonction de jeu

def Choixpion():#demande au joueur s'il veut changer de vision de plateau, jouer le pion qu'on lui propose ou demander qu'on lui propose un autre pion
    rep=-1
    while (rep!=0 and rep!=1 and rep !=2) :#évite que rep prenne une autre valeur que celle demandée
        rep=int(input("0 = jouer ce pion, 1 = choisir un autre pion, 2 = afficher une autre face du plateau"))
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

# version sans sleep
def RecherchePion(plateauPion,plateauCarte,plateauVisible):
    selectionne = False # variable qui détermine si le joueur à selectionné ou non un pion
    i = 0
    j = 0
    typeAff = -1
    while selectionne == False: # continue la fonction tans que aucun pion n'a été séléctionné
        if(j == len(plateauPion)): # si le compteur est arriver au maximum de colonne
            i += 1
            j = 0
        if(i == len(plateauPion)): # si le compteur est arriver au maximum de ligne
            i = 0
        if(plateauPion[i][j] == "J1" or plateauPion[i][j] == "g1"): # si les coordonnées donne sur un pion du joueur
            rep = 2 # initialise une variable reponse
            AffichePionSelectionne(plateauPion,i,j) # Affiche le pion séléctionné
            while(rep == 2):
                rep = Choixpion() # demande au joueur son choix
                if(rep == 0): # le joueur choisit ce pion
                    selectionne = True
                    j -= 1 # sert à compensée le compteur
                if(rep == 2): # afficher un autre plateau (carte ou pion)
                    typeAff *= -1 # permet de connaitre quel plateau afficher
                    AffichePlateauAlterner(typeAff,plateauPion,plateauCarte,plateauVisible) # afficher le plateau demander
        j += 1
    return i,j

# version avec sleep
def RecherchePionS(plateauPion,plateauCarte,plateauVisible):
    selectionne = False
    i = 0
    j = 0
    while selectionne == False:
        if(j == len(plateauPion)):
            i += 1
            j = 0
        if(i == len(plateauPion)):
            i = 0
        if(plateauPion[i][j] == "J1" or plateauPion[i][j] == "g1"):
            rep = 2
            AffichePionSelectionne(plateauPion,i,j)
            while(rep == 2):
                rep = Choixpion()
                if(rep == 0):
                    selectionne = True
                    j -= 1
                if(rep == 2):
                    AffichePlateauAlternerS(plateauPion,plateauCarte,plateauVisible)
        j += 1
    return i,j

def Carte(lig,col,plateauCarte):
    carte = plateauCarte[col][lig]
    if carte == "N":
        return "rejoue"
    if carte == "I":
        return "relais"
    if carte == "M":
        return "male"
    if carte == "M1":
        return "male1"
    if carte == "M2":
        return "male2"
    if carte == "V":
        return "vase"
    if carte == "B":
        return "brochet"

    return "passe"


def Deplacement(plateauPion,plateauCarte,plateauVisible):
    i,j = RecherchePionS(plateauPion,plateauCarte,plateauVisible) # retourne les coordonnée du pion séléctionné
    dirlig, dircol = Deplacementverifjoueur(i, j, plateauPion) # retourne les résultats du déplacements
    plateauPion[i+dirlig][j+dircol] = plateauPion[i][j] # déplace le pion
    plateauPion[i][j] = 0 # retire l'ancien pion
    return plateauPion,plateauCarte,plateauVisible # retourne les plateaux modifiés

def IsFinish(plateauPion): # parcour le plateau de pion est vérifie si toutes les rênes sont présentes
    j1IsHere = False
    j2IsHere = False
    for col in range (0,len(plateauPion)):
        for lig in range (0,len(plateauPion[col])):
            if(plateauPion[col][lig] == "J1"):
                j1IsHere = True
            if(plateauPion[col][lig] == "J2"):
                j2IsHere = True

    if(j1IsHere == True and j2IsHere == True):
        return "continuer"
    if(j1IsHere == False and j2IsHere == False)
        return "egalite"
    if(j1IsHere == False)
        return "j2gagne"
    if(j2IsHere == False)
        return "j1gagne"


## FONCTION DE TEST

plateau = InitPlateau()
plateau = SetUpPlateau(plateau)
carte = CreateTasCarte()
tableVisi = InitPlateau()
tableVisi[0][0] = 1
tableVisi[1][0] = 1
tableVisi[0][1] = 1
plateau,carte,tableVisi = Deplacement(plateau,carte,tableVisi)

AffichePlateau(plateau)
#print("i = ",i," j = ",j," dirlig = ",dirlig," dircol = ",dircol)