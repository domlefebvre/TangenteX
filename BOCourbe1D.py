# Boite � outils Python pour le numericien
# trac� de courbes 1D
# Dominique Lefebvre pour TangenteX.com
# 29 juillet 2015
#

# importation des librairies
from scipy import arange, pi, sin  # import des fonctions et constantes utilis�es
from matplotlib.pyplot import *    # fonction de trac� de courbe

# construction du vecteur x
debut = 0.0
fin = 2*pi
pas = 0.01
x = arange(debut, fin, pas)

# construction du vecteur y = sin(x)
y = sin(x)

# affichage de la courbe des r�sultats
figure()            # s�lection de la fen�tre par d�faut

# titre de la courbe et l�gende des axes
title("Fonction sinus(x)")
xlabel('x')
ylabel('y')

# d�finition des axes
grid(True)           # grille affich�e
axis([x.min(),x.max(), y.min(), y.max()])  # xmin, xmax, ymin, ymax

# calcul et affichage de la courbe dans la fen�tre par d�faut
plot(x,y, 'r')       # trac� de la courbe en rouge
show()


