### IMPORTATION
from random import *
import time


### FONCTION INITIALISATION

##Plateau initial
#initialiser un tableau
def InitPlateau(): #crée un tableau vide pouvant être utilisé pour créer les différents plateaux
    tab = [0]*8

    #on assigne  aux 64 cartes du plateau
    for i in range (0,8):
        tab[i] = [0]*8

    return tab

##Plateaux de jeu
#initialiser les valeurs initiales
def Plateauemplacement(tab):
    #Extremitée haut gauche
    tab[0][0] = "J1" #reine du joueur 1
    tab[1][0] = "g1" #grenouille du joueur 1
    tab[0][1] = "g1"

    #Extremitée bas droit
    extremite = len(tab)-1
    extremite2 = len(tab[extremite])-1

    tab[extremite][extremite2] = "J2" #reine du joueur 2
    tab[(extremite-1)][extremite2] = "g2"#grenouille du joueur 2
    tab[extremite][(extremite2-1)] = "g2"

    return tab #retourne le tableau initial des emplacements


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
        TasMelanger[i] = TasC[valAlea] #ajout de la carte choisie
        del(TasC[valAlea]) #suppression de la carte
    tableaucarte = InitPlateau() # création d'un tableau vide
    index = 0 # indice suivant la progression sur TasMélanger
    for i in range (0,len(tableaucarte)): # parcourt les colonnes
        for j in range (0,len(tableaucarte[i])): #parcourt les lignes
            tableaucarte[i][j] = TasMelanger[index][0] #convertir la liste TasMelanger en tableau affichable
            index += 1 #fais évoluer l'indice
    return tableaucarte # retourne le tableau de carte

###Fonction d'affichage


#Affichage du plateau (fonction générale)
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
            #Affiche le contenu du résultat
            print(tab[i][j],end="")#end permet de ne pas revenir à la ligne
        #EndFor
        for r in range(0,RETOUR_LIGNE):
            print("")
        #EndFor
    #EndFor

#Affichage des cartes révélées
def AffichageCarte(tabCarte,tabVisi): # tableau des cartes révélées
    tabResult = InitPlateau() #initialisation du plateau
    for i in range (0,len(tabCarte)): #on parcourt les colonnes
        for j in range (0,len(tabCarte[i])): #on parcourt les lignes
            if tabVisi[i][j] == 1:#1=la carte a été révélée
                tabResult[i][j]=tabCarte[i][j]#on rajoute la carte au tableau si elle a été révélée
            else :
                tabResult[i][j]='*'#la carte n'a pas été révélée
    AffichePlateau(tabResult)#on affiche le tableau des cartes révélées



### Fonction de jeu

## Fonction de choix de pion à jouer
def Choixpion():#demande au joueur s'il veut changer de vision de plateau, jouer le pion qu'on lui propose ou demander qu'on lui propose un autre pion
    rep=-1
    while rep!=0 or rep!=1 or rep !=2 :#évite que rep prenne une autre valeur que celle demandée
        rep=input("0 = jouer ce pion, 1 = choisir un autre pion, 2 = afficher une autre face du plateau")
    return rep

## Fonction de choix et de vérification des déplacements

def Dircolonne (col): #demande un déplacement sur les colonnes au joueur et vérifie qu'il ne sort pas du plateau
    possibilite = False #variable vérifiant la possibilité de déplacement
    while possibilite == False:
        dircol=2 #variable prenant en compte le déplacement
        while (dircol != 0 and dircol != 1 and dircol != -1):#tant que le joueur ne rentre pas un déplacement valide, c'est à dire d'une case
            dircol = int(input("-1 = aller à gauche, 0 = rester dans cette colonne, 1 = aller à droite : "))#demande de rentrer le déplacement

        if (dircol==-1 and col==0) or (dircol==1 and col==7):#vérifie que le déplacement ne fait pas sortir du plateau
            possibilite = False
            print ("La bataille ne se déroule que dans la mare, veuillez ne pas rejoindre la terre ferme. Choisissez un autre déplacement.")
        else :
            possibilite = True #le déplacement est vérifié comme possible
    return dircol

def Dirligne (lig):#demande un déplacement sur les lignes au joueur et vérifie qu'il ne sort pas du plateau
    possibilite = False #variable vérifiant la possibilité de déplacement
    while possibilite == False:
        dirlig=2 #variable prenant en compte le déplacement
        while (dirlig != -1 and dirlig != 0 and dirlig != 1): #tant que le joueur ne rentre pas un déplacement valide, c'est à dire d'une case
            dirlig = int(input("-1 = aller en haut, 0 = rester dans cette ligne, 1 = aller en bas : "))#demande de rentrer le déplacement
        if (dirlig == -1 and lig == 0) or (dirlig == 1 and lig == 7): #vérifie que le déplacement ne fait pas sortir du plateau
            possibilite = False
            print ("La bataille ne se déroule que dans la mare, veuillez ne pas rejoindre la terre ferme. Choisissez un autre déplacement")
        else :
            possibilite = True #le déplacement est vérifié comme possible
    return dirlig

def Deplacementverifjoueur (lig, col, plateau):
    collision = True #variable vérifiant si le pion ne se déplace pas sur une case déjà occupée par une grenouille alliée
    while collision : #tant que la collision est vrai
        possibilite = False

        while possibilite == False :#vérifie que le joueur ne saute pas son tour
            dirlig = Dirligne(lig) # demande et vérifie le déplacement sur les lignes
            dircol = Dircolonne(col) #demande et vérifie le déplacement sur les colonnes

            if ( dircol==0 and dirlig==0): # si le joueur chosit de ne pas bouger le pion qu'il a décide de jouer
                possibilite = False
                print ("Les grenouilles bien élevées ne sautent pas leur tour") #indique qu'il n'a pas le droit de jouer son tour
            else :
                possibilite = True # le joueur bouge réellement

        if plateau[col + dircol][lig + dirlig] == "J1" or plateau[col + dircol][lig + dirlig] == "g1" or plateau[col + dircol][lig + dirlig] == "Vg1" or plateau[col + dircol][lig + dirlig] == "VJ1": #si la case sur laquelle arrive le pion joué est déjà occupé par un allié
            collision = True
            print("Manger ses alliés est une mauvaise stratégie pour arriver jusqu'à la victoire" ) #indique que la case est déjà occupée
        else:
            collision = False #la case n'est pas occupée
    return dirlig, dircol #retourne les déplacements qui ont été vérifiés comme valides

### EFFET CARTE

## Carte nouvel emplacement

def Carte (lig, col, plateaucarte): #retourne la carte sur laquelle le pion arrive
    carte=plateaucarte[col][lig]
    if carte==N:#nénuphar
        return "Rejoue"
    elif carte==I:#insecte
        return "Relai"
    elif carte==M:#mâle non utilisé
        return "Male"
    elif carte==M1:#mâle utilisé par le joueur 1
        return "Male1"
    elif carte==M2:#mâle utilisé par le joueur 2
        return "Male2"
    elif carte==V:#vase
        return "Vase"
    elif carte==B:#brochet
        return "Brochet"
    return "Fin"#roseau

## Fonctions des cartes

# Brochet

def Brochet (lig,col,plateauemplacement):
    plateauemplacement[lig][col]=0

#Mâle


def MaleJ1 (lig,col,plateauemplacement,plateaucarte):#le mâle peut être utilisé par le joueur 1
    j=0#colonne où l'on va placer la nouvelle grenouille
    i=0#igne où l'on va placer la nouvelle grenouille
    while plateauemplacement[j][i]!=0:#tant que la place sur laquelle la nouvelle grenouille naît est occupée on parcourt la plateau pour trouver une place libre
        if j == len (plateauemplacement): #si la colonne est est la dernière
            j=0#on revient à la premiere collonne
            i+=1#on passe à la ligne suivante
        else :#si la colonne n'est pas la dernière
            j+=1#on passe à la colonne de droite
    plateauemplacement[j][i]="g1"#la grenouille naît sur une place libre
    if plateaucarte[col][lig]=="M":#si le mâle n'a été utilisé par personne
        plateaucarte[col][lig]="M1"
    else :
        plateaucarte[col][lig]="roseau"#si le mâle avait déjà été utilisé par le joueur 2, la carte devient inutile



def MaleJ2 (lig,col,plateauemplacement,plateaucarte):#le mâle peut être utilisé par le joueur 2
    j=0#colonne où l'on va placer la nouvelle grenouille
    i=0#igne où l'on va placer la nouvelle grenouille
    while plateauemplacement[j][i]!=0:#tant que la place sur laquelle la nouvelle grenouille naît est occupée on parcourt la plateau pour trouver une place libre
        if j == len (plateauemplacement): #si la colonne est est la dernière
            j=0#on revient à la premiere collonne
            i+=1#on passe à la ligne suivante
        else :#si la colonne n'est pas la dernière
            j+=1#on passe à la colonne de droite
    plateauemplacement[j][i]="g2"#la grenouille naît sur une place libre
    if plateaucarte[col][lig]=="M":#si le mâle n'a été utilisé par personne
        plateaucarte[col][lig]="M2"
    else :
        plateaucarte[col][lig]="roseau"#si le mâle avait déjà été utilisé par le joueur 2, la carte devient inutile

#Vase

def Vase (lig,col,plateauemplacement):
    if plateauemplacement[col][lig]=="J1":
        plateauemplacement[col][lig]="VJ1"#change le nom du pion ce qui permettra qu'il sera ignoré au tour suivant par la fonction Recherchepion et permet de réénitialiser l'état à la fin du tour suivant
    elif plateauemplacement[col][lig]=="g1":
        plateauemplacement[col][lig]="Vg1"
    elif plateauemplacement[col][lig]=="g2":
        plateauemplacement[col][lig]="Vg2"
    elif plateauemplacement[col][lig]=="J2":
        plateauemplacement[col][lig]="VJ2"

### FONCTION DE TEST




tab = InitPlateau()
plateau = Plateauemplacement(tab)
Deplacementverifjoueur(0,0,plateau)

time.sleep(2)
