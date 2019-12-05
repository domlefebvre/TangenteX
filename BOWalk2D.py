# Programme de simulation d'une marche aléatoire 2D
# Dominique Lefebvre pour TangenteX.com
# 18 aout 2015
#

# importation des librairies
from scipy import sqrt, zeros
from random import gauss
from matplotlib.pyplot import *              

# paramètres de la simulation
T = 5.
N = 1000
sh = sqrt(T/N)

# définition des tableaux
x = zeros(N)
y = zeros(N)

# construction des vecteurs de bruit gaussien sur x et y
bruitX = [gauss(0.,sqrt(T)) for i in range(N)]
bruitY = [gauss(0.,sqrt(T)) for i in range(N)]

# calcul de la trajectoire
for i in range(1,N):
    x[i] = x[i-1] + sh*bruitX[i-1]
    y[i] = y[i-1] + sh*bruitY[i-1]
    
# affichage de la courbe des résultats
figure()
title('Marche aleatoire 2D')
xlabel('x')
ylabel('y')
axis('equal')
plot(x,y)

show()


