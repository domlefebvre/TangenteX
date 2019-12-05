# -*- coding: Latin-1 -*-
# Programme de résolution des équations de Maxwell pour
# la propagation des champs électriques et magnétiques
# par différences finies schéma FDTD
# Dominique Lefebvre pour TangenteX.com
# 23 novembre 2016
#

# importation des librairies
from scipy import zeros, arange, sin, pi
from visual import display, curve, color, rate, label

# routine d'affichage des champs E et B
def PlotChamp(t):
    Ec.x = 2*X - Xmax
    Ec.y = Largeur*Ex[X,t]
    Bc.x = 2*X - Xmax
    Bc.z = Largeur*By[X,t]


# fonction source des champs électrique et magnétique
def Source(x):
    A0 = 0.1
    omega = 2*pi/100.0
    s = A0*sin(omega*x)
    return s
    
# taille de la scene
Largeur = 1000
Hauteur = 600
# taille du référentiel
Xmax = 201
Ymax = 100
Zmax = 100

# description de la scène de tracé des courbes
scene = display(title = 'propagation du champ electromagnetique',x=0,y=0,width=Largeur,\
                height=Hauteur,forward=(-1.0,-2.0,-6.0),background=color.white)
# tracé du référentiel Ex,By,Z
curve(pos=[(-Xmax,Ymax),(Xmax,Ymax),(Xmax,-Ymax),(-Xmax,-Ymax),(-Xmax,Ymax)],\
               color = color.red)   
curve(pos=[(-Xmax,0,Zmax),(Xmax,0,Zmax),(Xmax,0,-Zmax),(-Xmax,0,-Zmax),\
                    (-Xmax,0,Zmax)], color = color.green)
curve(pos=[(-Xmax,0),(Xmax,0)], color = color.blue) 
# caractéristiques des courbes de champ E et B
Ec=curve(x = list(range(0,Xmax)),color = color.red,radius = 0.5)
Bc=curve(x = list(range(0,Xmax)),color = color.green,radius = 0.5) 
# définition des labels
label(text='Ex',pos=(-Xmax-20,50),heigth=14,font='sans',color=color.black)
label(text='By',pos=(-Xmax-20,8,50),heigth=14,font='sans',color=color.black)
label(text='Z',pos=(Xmax+10,0),heigth=14,font='sans',color=color.black)
                    
# Paramètres physiques de la simulation
Alpha = 0.01      # Alpha = (c.dt)/dz attention à respecter le critère CFL
        
# Initialisation des vecteurs Ex et By
Ex = zeros((Xmax,2),float)
By = zeros((Xmax,2),float)

# Initialisation des champs électrique et magnétique
X = arange(Xmax)
Ex[:Xmax,0] = Source(X)
By[:Xmax,0] = Source(X)


# boucle de calcul et d'affichage des champs
FreqAff = 400    # vitesse de défilement
PlotChamp(0)
while True:
    rate(FreqAff)
    # application du schéma FDTD
    Ex[1:Xmax-1,1] = Ex[1:Xmax-1,0] + Alpha*(By[0:Xmax-2,0] - By[2:Xmax,0])
    By[1:Xmax-1,1] = By[1:Xmax-1,0] + Alpha*(Ex[0:Xmax-2,0] - Ex[2:Xmax,0])

    # Application des conditions aux limites sur les champs E et B
    Ex[0,1]      = Ex[0,0] + Alpha*(By[Xmax-2,0] - By[1,0])
    Ex[Xmax-1,1] = Ex[Xmax-1,0] + Alpha*(By[Xmax-2,0] - By[1,0])
    By[0,1]      = By[0,0] + Alpha*(Ex[Xmax-2,0] - Ex[1,0])
    By[Xmax-1,1] = By[Xmax-1,0] + Alpha*(Ex[Xmax-2,0] - Ex[1,0])

    # Affichage des champs E et B
    PlotChamp(1)

    # swap des valeurs des champs E et B
    Ex[:Xmax,0] = Ex[:Xmax,1]
    By[:Xmax,0] = Ex[:Xmax,1]

