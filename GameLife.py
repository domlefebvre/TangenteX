# -*- coding: Latin-1 -*-
# Un exemple d'automate cellulaire : le jeu de la vie
# Dominique Lefebvre pour TangenteX.com
# 19 janvier 2017
#
import numpy as np
from Tkinter import Tk, Canvas, Button, RIGHT, LEFT

# Dimension du monde
NbL = 30  # hauteur du tableau
NbC = 30  # largeur du tableau
a = 15    # taille d'une cellule

# Définition des matrices d'évolution de l'automate
cell = np.zeros((NbL,NbC),dtype=int)
etat = np.zeros((NbL,NbC),dtype=int)

# Définition de l'alphabet de l'automate dans un dictionnaire Python
state = {"OFF":0,"ON":1}

# Calculer et dessiner la prochaine génération
def iterer():
    global flag
    appliquer_regles()
    dessiner()
    if flag==1:
        fenetre.after(100, iterer)
    else:
        flag=0

# Initialisation de l'automate
def initialiser_monde():   
    etat[0:NbL,0:NbC] = state["OFF"]
    # création de la grille
    for x in range(NbL):
        for y in range(NbC):
            cell[x,y] = canvas.create_rectangle((x*a, y*a, (x+1)*a, \
                         (y+1)*a), outline="gray", fill="white")

# Calcul de la prochaine génération
def appliquer_regles():
    global etat
    temp = np.zeros((NbL,NbC))
    for x in range(NbL):
        for y in range(NbC):
            nb_voisins = voisinageMoore(x,y)
            # Règle 1 - Mort de solitude
            if etat[x][y] == state["ON"] and nb_voisins < 2:
                temp[x][y] = state["OFF"]
            # Règle 2 - Toute cellule avec 2 ou 3 voisins survit.
            if etat[x][y] == state["ON"] and (nb_voisins == 2 or nb_voisins == 3):
                temp[x][y] = state["ON"]
            # Règle 3 - Mort par asphyxie
            if etat[x][y] == state["ON"] and nb_voisins > 3:
                temp[x][y] = state["OFF"] 
            # Règle 4 - Naissance
            if etat[x][y] == state["OFF"] and nb_voisins == 3:
                temp[x][y] = state["ON"]                
    # copier la matrice temporaire dans l'automate
    etat = temp.copy()

# Compter les voisins vivants - tableau torique
def voisinageMoore(i,j):
    nb_voisins = 0
    if etat[(i-1)%NbL][(j+1)%NbC] == state["ON"]:
        nb_voisins += 1
    if etat[i][(j+1)%NbC] == state["ON"]:
        nb_voisins += 1
    if etat[(i+1)%NbL][(j+1)%NbC] == state["ON"]:
        nb_voisins += 1
    if etat[(i-1)%NbL][j] == state["ON"]:
        nb_voisins += 1
    if etat[(i+1)%NbL][j] == state["ON"]:
        nb_voisins += 1
    if etat[(i-1)%NbL][(j-1)%NbC] == state["ON"]:
        nb_voisins += 1
    if etat[i][(j-1)%NbC] == state["ON"]:
        nb_voisins += 1
    if etat[(i+1)%NbL][(j-1)%NbC] == state["ON"]:
        nb_voisins += 1
    return nb_voisins

# Dessiner toutes les cellules
def dessiner():
    for x in range(NbL):
        for y in range(NbC):
            if etat[x,y]==state["OFF"]:
                coul = "white"
            else:
                coul = "blue"
            canvas.itemconfig(cell[x,y], fill=coul)

# Arrêt de l'animation
def stop():
    global flag
    flag=0

# Démarrage de l'animation
def start():
    global flag
    if flag==0: 
        flag=1
    iterer()

# Animation pas à  pas
def pasapas():
    global flag
    flag=2
    iterer()

# Fonction de traitement du clic gauche de la souris
def  SelectionCellule(event):
    x, y = event.x//a, event.y//a
    etat[x,y] = (etat[x,y]+1)%2
    if etat[x,y]==state["OFF"]:
        color = "white"
    else:
        color = "blue"
    canvas.itemconfig(cell[x][y], fill=color)

# Définition de l'interface graphique
fenetre = Tk()
fenetre.title("Jeu de la vie - Conway")
canvas = Canvas(fenetre, width=a*NbC+1, height=a*NbL+1, highlightthickness=0)
fenetre.wm_attributes("-topmost", True) # afficher la fenetre on top

# Appelle la fonction SelectionCellule sur click gauche
canvas.bind("<Button-1>", SelectionCellule)
canvas.pack()

# Définition des boutons de commande
bou1 = Button(fenetre,text='Exit', width=8, command=fenetre.destroy)
bou1.pack(side=RIGHT)
bou2 = Button(fenetre, text='Start', width=8, command=start)
bou2.pack(side=LEFT)
bou3 = Button(fenetre, text='Stop', width=8, command=stop)
bou3.pack(side=LEFT)
bou4 = Button(fenetre, text='Step', width=8, command=pasapas)
bou4.pack(side=LEFT)

# lancement de l'automate
flag = 0
initialiser_monde()
dessiner()
iterer()
fenetre.mainloop()


