# programme d'étude de la réponse d'un sismomètre
# en fonction de la pulsation réduite et de Q
# Dominique Lefebvre pour TangenteX.com
# 6 septembre 2014
#

# importation des librairies
from numpy import arange, sqrt
import matplotlib.pyplot as plt

# fonction de calcul de la réponse du sismo
def Reponse(u,Q):
    return (u*u/(sqrt((1 - u*u)**2 + (u/Q)**2)))
            
# définition des vecteurs de calcul
u = arange(0,10,0.01)

# titre et axes
plt.title('Variation de la reponse Zr/Z0 en fonction de u et Q')

axes = plt.gca()
axes.set_xlim(0,10)
axes.set_ylim(0,3)
axes.set_xticks(arange(0,10.0,0.5))
axes.set_yticks(arange(0,3.0,0.5))

#tracé des courbes
Z = Reponse(u,0.2)
plt.plot(u,Z,'b', label='Q = 0.2')
Z = Reponse(u,0.5)
plt.plot(u,Z,'r', label='Q = 0.5')
Z = Reponse(u,1/sqrt(2))
plt.plot(u,Z,'g', label='Q = 1/sqrt(2)')
Z = Reponse(u,1)
plt.plot(u,Z,'y', label='Q = 1')
Z = Reponse(u,2)
plt.plot(u,Z,'c', label='Q = 2')

plt.grid()
plt.legend()
plt.xlabel('Pulsation reduite u'); plt.ylabel('Reponse Zr/Z0')
plt.show()


