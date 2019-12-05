# -*- coding: Latin-1 -*-
# Simulation de la propagation spatiale d'une épidémie
# par un automate cellulaire
# Dominique Lefebvre pour TangenteX.com
# 8 février 2017
#
import numpy as np
from Tkinter import Tk, Canvas, Button, RIGHT, LEFT
from random import random

# Dimension du monde
NbL = 40  # hauteur du tableau
NbC = 40  # largeur du tableau
a = 10    # taille d'une cellule

# Définition des matrices d'évolution de l'automate
cell = np.zeros((NbL,NbC),dtype=int)
etat = np.zeros((NbL,NbC),dtype=int)
NbGen = 0

# Définition de l'alphabet de l'automate dans un dictionnaire Python
state = {"SAIN":0,"MALADE":1,"IMMUN":2}
# Définition des couleurs associées
CoulSain = "white"
CoulImmun = "green"
CoulMal = "red"

# Paramètre de simulation
DensiteImmun = 0.2    # densité d'individus immunisés dans la population
ProbaContag = 0.5     # contagiosité


# Calculer et dessiner la prochaine génération
def iterer(p):
    appliquer_regles(p)
    dessiner()

# Initialisation de l'automate
def initialiser_monde(p):
    # répartition aléatoire sur la grille d'état des individus immunisés
    etat[0:NbL,0:NbC] = state["SAIN"]    
    for x in range(NbL):
        for y in range(NbC):
            if random() < p:
                etat[x,y] = state["IMMUN"]    
    # crétion de la grille d'affichage
    for x in range(NbL):
        for y in range(NbC):
            if etat[x,y]==state["SAIN"]:
                coul = CoulSain
            if etat[x,y]==state["IMMUN"]:
                coul = CoulImmun
            cell[x,y] = canvas.create_rectangle((x*a, y*a, (x+1)*a, \
                         (y+1)*a), outline="gray", fill=coul)

# Calcul de la prochaine génération
# la règle est simple : si un individu est infecté, il 
# infecte tous ses voisins au sens de Von Neumann avec une proba
# égale à la contagiosité
def appliquer_regles(p):
    global etat
    temp = etat.copy()  # sauvegarde de l'état courant
    for x in range(NbL):
        for y in range(NbC):
            if etat[x,y] == state["MALADE"]:                
                if etat[(x-1)%NbL,(y+1)%NbC] == state["SAIN"]:
                    if random() < p:
                        temp[(x-1)%NbL,(y+1)%NbC] = state["MALADE"]                                
                if etat[x,(y+1)%NbC] == state["SAIN"]:
                    if random() < p:
                        temp[x,(y+1)%NbC] = state["MALADE"] 
                if etat[(x+1)%NbL,(y+1)%NbC] == state["SAIN"]:
                    if random() < p:
                        temp[(x+1)%NbL,(y+1)%NbC] = state["MALADE"] 
                if etat[(x-1)%NbL,y] == state["SAIN"]:
                    if random() < p:
                        temp[(x-1)%NbL,y] = state["MALADE"] 
                if etat[(x+1)%NbL,y] == state["SAIN"]:
                    if random() < p:
                        temp[(x+1)%NbL,y] = state["MALADE"] 
                if etat[(x-1)%NbL,(y-1)%NbC] == state["SAIN"]:
                    if random() < p:
                        temp[(x-1)%NbL,(y-1)%NbC] = state["MALADE"] 
                if etat[x,(y-1)%NbC] == state["SAIN"]:
                    if random() < p:
                        temp[x,(y-1)%NbC] = state["MALADE"] 
                if etat[(x+1)%NbL,(y-1)%NbC] == state["SAIN"]:
                    if random() < p:
                        temp[(x+1)%NbL,(y-1)%NbC] = state["MALADE"] 
    etat = temp.copy()  # maj de l'état courant

# Dessiner toutes les cellules
def dessiner():
    for x in range(NbL):
        for y in range(NbC):
            if etat[x,y]==state["SAIN"]:
                couleur = CoulSain
            if etat[x,y]==state["IMMUN"]:
                couleur = CoulImmun
            if etat[x,y]==state["MALADE"]:
                couleur = CoulMal
            canvas.itemconfig(cell[x][y], fill=couleur)
            
# Animation pas à pas
def pasapas():
    global NbGen
    iterer(ProbaContag) 
    NbGen += 1
    print NbGen

# Fonction de traitement du clic gauche de la souris
def  Infecter(event):
    x, y = event.x//a, event.y//a
    # on ne peut pas infecter un individu immunisé
    if etat[x,y] != state["IMMUN"]:
        etat[x,y] = state["MALADE"]
        canvas.itemconfig(cell[x][y], fill=CoulMal)
    
# Définition de l'interface graphique
fenetre = Tk()
fenetre.title("Simulation de la propagation d'une maladie")
canvas = Canvas(fenetre, width=a*NbC+1, height=a*NbL+1, highlightthickness=0)
fenetre.wm_attributes("-topmost", True)
# Allocation de la fonction Infecter sur click gauche
canvas.bind("<Button-1>", Infecter)
canvas.pack()

# Définition des boutons de commande
bou1 = Button(fenetre,text='Exit', width=8, command=fenetre.destroy)
bou1.pack(side=RIGHT)
bou2 = Button(fenetre, text='Step', width=8, command=pasapas)
bou2.pack(side=LEFT)

# lancement de l'automate
initialiser_monde(DensiteImmun)
fenetre.mainloop()


