# Boite à outils Python pour le numericien
# tracé de courbes 1D
# Dominique Lefebvre pour TangenteX.com
# 29 juillet 2015
#

# importation des librairies
from scipy import arange, pi, sin  # import des fonctions et constantes utilisées
from matplotlib.pyplot import *    # fonction de tracé de courbe

# construction du vecteur x
debut = 0.0
fin = 2*pi
pas = 0.01
x = arange(debut, fin, pas)

# construction du vecteur y = sin(x)
y = sin(x)

# affichage de la courbe des résultats
figure()            # sélection de la fenêtre par défaut

# titre de la courbe et légende des axes
title("Fonction sinus(x)")
xlabel('x')
ylabel('y')

# définition des axes
grid(True)           # grille affichée
axis([x.min(),x.max(), y.min(), y.max()])  # xmin, xmax, ymin, ymax

# calcul et affichage de la courbe dans la fenêtre par défaut
plot(x,y, 'r')       # tracé de la courbe en rouge
show()


