### IMPORTATION
from random import *
import time # pour la fonction sleep


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

## Condition de victoire


def IsFinish(plateauPion): # parcourt le plateau de pion et vérifie si toutes les reines sont présentes
    j1IsHere = False # la reine 1 n'a pas encore été trouvée
    j2IsHere = False # la reine 2 n'a pas encore été trouvée
    for lig in range (0,len(plateauPion)): # parcourt les colonnes une par une
        for col in range (0,len(plateauPion[lig])): # parcourt les lignes sur une colonne
            if(plateauPion[lig][col] == "J1" or plateauPion[lig][col] == "VJ1"): # si l'on rencontre la reine 1 sur une des cases
                j1IsHere = True
            if(plateauPion[lig][col] == "J2" or plateauPion[lig][col] == "VJ2"): # si l'on rencontre la reine 2 sur une des cases
                j2IsHere = True
    if(j1IsHere == True and j2IsHere == True): # les deux reines ont été trouvées
        return ("La bataille se poursuit.")
    if(j1IsHere == False and j2IsHere == False) :#aucune des reines n'a été trouvée
        return ("La bataille est terminée, mais les deux camps sont éléminés, personne ne gagne.")
    if(j1IsHere == False) : # si la reine du joueur 1 n'a pas été trouvée
        return ("La bataille est terminée, vous avez perdu.")
    if(j2IsHere == False) : # si la reine du joueur 2 n'a pas été trouvée
        return ("La bataille est terminée, vous avez gagné.")

### FONCTION D'AFFICHAGE

## Affichage d'un seul plateau
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

## Affichage d'un plateau avec un caractère modifié
#affiche une flèche permettant au joueur de savoir par rapport à quel pion est posé la question
def AffichePionSelectionne(tab,i,j):
    pion = tab[i][j] # récupère le pion
    tab[i][j] = "->" + pion # ajoute à la case une flèche pour montrer à l'utilisateur ce qui est sélectionné
    AffichePlateau(tab) # afficher le tableau avec le pion selectionné
    tab[i][j] = pion # rétablir la case en enlevant la flèche


## Affichage de deux plateaux alternativement
#fonction alternative à sleep permettant d'afficher alternativement le plateau des pions et celui des cartes
def AffichePlateauAlterner(typePlateau,plateauPion,plateauCarte,tabVisi):
    if(typePlateau == -1): # si c'est -1 afficher les pions
        AffichePlateau(plateauPion)
    else:# si c'est 1 afficher les cartes
        AffichageCarte(plateauCarte,tabVisi)

#fonction permettant d'afficher alternativement le plateau des cartes et celui des pions AVEC sleep
def AffichePlateauAlternerS(plateauPion,plateauCarte,tabVisi):
    AffichageCarte(plateauCarte,tabVisi) #afficher les cartes
    time.sleep(2) # attendre n secondes
    AffichePlateau(plateauPion) #afficher plateau


### FONCTION DE JEU

## Fonction de choix de pion à jouer
def Choixpion():#demande au joueur s'il veut changer de vision de plateau, jouer le pion qu'on lui propose ou demander qu'on lui propose un autre pion
    rep=-1
    while rep != 0 and rep != 1 and rep !=2 :#évite que rep prenne une autre valeur que celle demandée
        rep=int(input("0 = jouer ce pion, 1 = choisir un autre pion, 2 = afficher une autre face du plateau"))
        print(rep)
    return rep



# version avec sleep
def RecherchePionS(plateauPion,plateauCarte,plateauVisible): #parcourt le plateau tant que le joueur ne choisit pas de pion
    selectionne = False #le joueur n'a toujours pas sséletionné de pion
    col = 0 #démarre à (0,0)
    lig = 0
    while selectionne == False:#tant que le joueur ne sélectionne pas de pion on parcourt le plateau
        if(col == len(plateauPion)):#si l'on est en bout de ligne
            lig += 1 #on saute une ligne
            col = 0 #on revient à une première colonne
        if(lig == len(plateauPion)): # si l'on est en (7,7)
            lig = 0 # on revient à (0,0)
        if(plateauPion[lig][col] == "J1" or plateauPion[lig][col] == "g1"):#si la case sur laquelle est arrivée est occupé par un pion allié
            rep = 2
            AffichePionSelectionne(plateauPion,lig,col) # affiche au joueur sur quel pion est posé la question
            while(rep == 2):
                rep = Choixpion() #demande au joueur s'il veut jouer ce pion
                if(rep == 0):#si le joueur choisit de jouer ce pion
                    selectionne = True
                    col -= 1 #permet de retourner la bonne colonnne à la fin
                if(rep == 2): # affiche le plateau des cartes et des pions alternativement si le joueur le souhaite
                    AffichePlateauAlternerS(plateauPion,plateauCarte,plateauVisible) #version avec sleep
        col += 1 # modifie la colonne pour parcourir le pateau
    return col,lig


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

#demande les choix de déplacement du joueur et vérifie s'ils sont valides
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

        if plateau[lig + dirlig][col + dircol] == "J1" or plateau[lig + dirlig][col + dircol] == "g1" or plateau[lig + dirlig][col + dircol] == "Vg1" or plateau[lig + dirlig][col + dircol] == "VJ1": #si la case sur laquelle arrive le pion joué est déjà occupé par un allié
            collision = True
            print("Manger ses alliés est une mauvaise stratégie pour arriver jusqu'à la victoire" ) #indique que la case est déjà occupée
        else:
            collision = False #la case n'est pas occupée
    return dirlig, dircol #retourne les déplacements qui ont été vérifiés comme valides

## Fonction de déplacement

# déplace le pion en fonction du choix du joueur et supprime l'ancien emplacement
def Deplacement(plateauPion,plateauCarte,plateauVisible):
    col,lig = RecherchePionS(plateauPion,plateauCarte,plateauVisible) # retourne les coordonnées du pion séléctionné
    dirlig, dircol = Deplacementverifjoueur(lig, col, plateauPion) # retourne les résultats du déplacements
    plateauPion[lig+dirlig][col+dircol] = plateauPion[lig][col] # déplace le pion en fonction des choix
    plateauPion[lig][col] = 0 # retire l'ancien pion
    newLig = lig+dirlig
    newCol = col+dircol
    return plateauPion,plateauCarte,plateauVisible,newLig,newCol # retourne les plateaux modifiés


## Fonction de tour

def TourJoueur(plateauPion,plateauCarte,plateauVisible):
    newLig = 0
    newCol = 0
    plateauPion,plateauCarte,plateauVisible,newLig,newCol = Deplacement(plateauPion,plateauCarte,plateauVisible)
    plateauVisible[newLig][newCol] = 1
    reponse = Carte (newLig, newCol, plateauCarte)
    print("carte retourné : ",reponse)
    time.sleep(2)
    if reponse == "Brochet":
        plateauPion = Brochet(newLig,newCol,plateauPion)
    elif reponse == "Relai":
        print("!!! fonction relais non actif !!!")
    elif reponse == "Male2" or reponse == "Male":
        plateauPion,plateauCarte = MaleJ1 (newLig,newCol,plateauPion,plateauCarte)
    elif reponse == "Vase":
        plateauPion = Vase (newLig,newCol,plateauPion)
    elif reponse == "Rejoue":
        print("!!! fonction rejouer non actif !!!")
    return plateauPion,plateauCarte,plateauVisible


def Jeu():
    #initialisation
    plateauVisible = InitPlateau()
    plateauPion = Plateauemplacement(InitPlateau())
    plateauCarte = CreateTasCarte()
    rep = "La bataille se poursuit."
    plateauVisible[0][0] = 1
    plateauVisible[1][0] = 1
    plateauVisible[0][1] = 1
    plateauVisible[7][7] = 1
    plateauVisible[6][7] = 1
    plateauVisible[7][6] = 1
    while rep == "La bataille se poursuit.":
        plateauPion,plateauCarte,plateauVisible = TourJoueur(plateauPion,plateauCarte,plateauVisible)
        rep = IsFinish(plateauPion)

    print(rep)
    print("////fin du jeu")

def NettoyageVase(plateauPion):
    return plateauPion

### EFFET CARTE

## Carte nouvel emplacement

def Carte (lig, col, plateaucarte): #retourne la carte sur laquelle le pion arrive
    carte=plateaucarte[lig][col]
    if carte=="N":#nénuphar
        return "Rejoue"
    elif carte=="I":#insecte
        return "Relai"
    elif carte=="M":#mâle non utilisé
        return "Male"
    elif carte=="M1":#mâle utilisé par le joueur 1
        return "Male1"
    elif carte=="M2":#mâle utilisé par le joueur 2
        return "Male2"
    elif carte=="V":#vase
        return "Vase"
    elif carte=="B":#brochet
        return "Brochet"
    return "Fin"#roseau

## Fonctions des cartes

# Brochet

def Brochet (lig,col,plateauemplacement):
    plateauemplacement[lig][col]=0 #supprime le pion tombé sur cette carte
    return plateauemplacement

#Mâle


def MaleJ1 (lig,col,plateauemplacement,plateaucarte):#le mâle peut être utilisé par le joueur 1
    j=0#colonne où l'on va placer la nouvelle grenouille
    i=0#igne où l'on va placer la nouvelle grenouille
    while plateauemplacement[i][j]!=0:#tant que la place sur laquelle la nouvelle grenouille naît est occupée on parcourt la plateau pour trouver une place libre
        if j == len (plateauemplacement): #si la colonne est est la dernière
            j=0#on revient à la premiere collonne
            i+=1#on passe à la ligne suivante
        else :#si la colonne n'est pas la dernière
            j+=1#on passe à la colonne de droite
    plateauemplacement[i][j]="g1"#la grenouille naît sur une place libre
    if plateaucarte[lig][col]=="M":#si le mâle n'a été utilisé par personne
        plateaucarte[lig][col]="M1"
    else :
        plateaucarte[lig][col]="R"#si le mâle avait déjà été utilisé par le joueur 2, la carte devient inutile

    return plateauemplacement,plateaucarte



def MaleJ2 (lig,col,plateauemplacement,plateaucarte):#le mâle peut être utilisé par le joueur 2
    j=0#colonne où l'on va placer la nouvelle grenouille
    i=0#igne où l'on va placer la nouvelle grenouille
    while plateauemplacement[i][j]!=0:#tant que la place sur laquelle la nouvelle grenouille naît est occupée on parcourt la plateau pour trouver une place libre
        if j == len (plateauemplacement): #si la colonne est est la dernière
            i=0#on revient à la premiere collonne
            j+=1#on passe à la ligne suivante
        else :#si la colonne n'est pas la dernière
            i+=1#on passe à la colonne de droite
    plateauemplacement[j][i]="g2"#la grenouille naît sur une place libre
    if plateaucarte[lig][col]=="M":#si le mâle n'a été utilisé par personne
        plateaucarte[lig][col]="M2"
    else :
        plateaucarte[lig][col]="R"#si le mâle avait déjà été utilisé par le joueur 2, la carte devient inutile

#Vase

def Vase (lig,col,plateauemplacement):
    if plateauemplacement[lig][col]=="J1":
        plateauemplacement[lig][col]="VJ1"#change le nom du pion ce qui permettra qu'il sera ignoré au tour suivant par la fonction Recherchepion et permet de réénitialiser l'état à la fin du tour suivant
    elif plateauemplacement[lig][col]=="g1":
        plateauemplacement[lig][col]="Vg1"
    elif plateauemplacement[lig][col]=="g2":
        plateauemplacement[lig][col]="Vg2"
    elif plateauemplacement[lig][col]=="J2":
        plateauemplacement[lig][col]="VJ2"

    return plateauemplacement

### FONCTION DE TEST

Jeu()