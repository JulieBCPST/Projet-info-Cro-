###importation des modules
from random import shuffle
import numpy as np
###initialisation
## condition de victoire/défaite
NBREINE=1
nbreine=1
NBGRENOUILLE =2
nbgrenouille=2
NBREINE #nombre de reines du joueur 1
nbreine #nombre de reines du joueur 2
NBGRENOUILLE # nombre de grenouilles du joueur 1
nbgrenouille # nombre de grenouilles du joueur 2


def fin_du_jeu(nbreine,NBREINE):
    if nbreine==0:
        return "Victoire"
    elif NBREINE==0:
        return "Défaite"
## plateau
L1 = ["nenuphar"]*17
L2 = ["roseau"]*14
L3 = ["moustique"]*14
L4 = ["vase"]*6
L5 = ["brochets"]*6
L6 = ["mâle"]*7
L = L1 + L2 + L3 + L4 + L5 + L6

def plateau(): #création d'un plateau alétoire à chaque partie
    P=L.copy()
    shuffle(P) #on mélange aléatoirement les éléments de la liste
    return [P[0:8],P[8:16],P[16:24],P[24:32],P[32:40],P[40:48],P[48:56],P[56:64]]

L7 = [0]*8
L8=[100,1,0,0,0,0,0,0]
L9=[1,0,0,0,0,0,0,0]
L10=[0,0,0,0,0,0,0,2]
L11=[0,0,0,0,0,0,2,200]
L12=L8+L9+L7+L7+L7+L7+L10+L11

def plateaubis():
    D=L12.copy()
    return [D[0:8],D[8:16],D[16:24],D[24:32],D[32:40],D[40:48],D[48:56],D[56:64]]

plateau=plateau()
plateaubis=plateaubis()

## deplacement

i=0#ligne du plateau sur lequel est le pion du joueur 1
j=0#colonne du plateau sur lequel est le pion du joueur 1
I=plateau[i][j]
c=7#ligne du plateau sur lequel est le pion du joueur 2
d=7#colonne du plateau sur lequel est le pion du joueur 2
J=plateau[c][d]
plateausuivi=plateaubis.copy() #copie de plateaubis qui est modifiée à chaque déplacement

'dirlig' # variable qui permet le déplacement d'une ligne à une autre
'dircol' # variable qui permet le déplacement d'une colonne à une autre

def recoreine1 (plateaubis,lig,col): #détecte la présence de la reine du joueur 1 sur la case choisie
    return plateaubis[lig][col]==100

def recoreine2 (plateaubis,lig,col):#détecte la présence de la reine du joueur 2 sur la case choisie
    return plateaubis[lig][col]==200

def recogrenouille1 (plateaubis,lig,col):#détecte la présence d'une des grenouilles du joueur 1 sur la case choisie
    return plateaubis[lig][col]==1

def recogrenouille2 (plateaubis,lig,col):#détecte la présence d'une des grenouilles du joueur 2 sur la case choisie
    return plateaubis[lig][col]==2

def suivi (lig,col,dirlig,dircol,plateaubis,plateausuivi):#permet de suivre les pions sur le plateau en prenant en compte leur nature
    if recoreine1(plateaubis,lig,col):
        plateaubis[lig+dirlig][col+dircol]=100
    elif recoreine2(plateaubis,lig,col):
        plateaubis[lig+dirlig][col+dircol]=200
    elif recogrenouille1(plateaubis,lig,col):
        plateaubis[lig+dirlig][col+dircol]=1
    elif recogrenouille2(plateaubis,lig,col):
        plateaubis[lig+dirlig][col+dircol]=2
    plateaubis[lig][col]=0
    return plateausuivi



def deplacement(plateau,col,lig,dirlig,dircol,plateaubis): #déplace le pion du joueur en fonction de ce qu'il a choisi et retourne la carte sur laquelle il arrive
    lig+=dirlig
    col+=dircol
    carte=plateau[lig][col]
    return carte

def modifj(plateau,col,dircol,plateaubis):
    "modifie la colonne pour cela soit pris en compte par la suite"
    col+=dircol
    return col


def modifi(plateau,lig,dirlig,plateaubis):
    "modifie la ligne pour cela soit pris en compte par la suite"
    lig+=dirlig
    return lig




## déroulement d'un tour
def tour (a,i,j,K,I):#obsolète
    "fonction qui prend en compte le choix de déplacement du joueur, renvoie la carte sur laquelle il arrive et enregistre sa nouvelle position"
    return déplacement(K,I,a),modifi(K,i,a),modifj(K,j,a)

## actions des cartes

def brochet(pion,NBreine,NBgrenouille):
    if pion=="reine":
        NBreine-=1
    else :
        NBgrenouille-=1
