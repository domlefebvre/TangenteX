# programme de simulation de l'experience de Millikan
# Dominique Lefebvre pour TangenteX.com
# 12 f�vrier 2014
#

# importation des librairies
from scipy.integrate import odeint # on importe uniquement ce dont on a besoin
from pylab import *                # fonction de trac� de courbe

# param�tres physiques de l'exp�rience
eta  = 1.81e-5  # viscosit� de l'air (en Pas.s � 293K)
rhoA = 1.29     # masse volumique de l'air (en kg.m-3 � 293K et 1013 hPa)
rhoH = 875.3    # masse volumique de l'huile (en kg.m-3 � 293K)
rg = 1e-6       # rayon de la gouttelette (en m)
q = 1.6e-19     # charge �lectrique port�e par la gouttelette (1 e en Coulomb)
g = 9.81        # acc�l�ration de la pesanteur
Vg = (4 * pi * rg**3)/3  # volume de la gouttelette
m = Vg * rhoH           # masse de la gouttelette

# saisie de la valeur du champ �lectrique (en V.m-1)
E = input('Valeur du champ �lectrique (V.m-1): ')


# calcul des coefficents de l'�quation diff�rentielle
K = (6 * pi * eta * rg)/ m
C = (Vg*g*(rhoH - rhoA))/m - (q*E/m)

# definition de l'�quation diff�rentielle
def Millikan(v,t):
    return -K*v + C

# conditions initiales de l'exp�rience
t0 = 0.0
v0 = 0.0

# d�finition du vecteur temps de l'exp�rience
tmax = 0.001
pastemps = tmax/100
time = arange(t0, tmax, pastemps) # cr�� un vecteur de pastemps points entre t0 et tmax

# solution analytique
#vr = (C/K)*(1 - exp(-time*K))

# calcul de la vitesse limite en l'absence de champ �lectrique
vls = (Vg*g*(rhoH - rhoA))/(6 * pi * eta * rg)
print 'Vitesse limite pour un champ �lectrique nul: ',vls

# calcul de la vitesse de chute avec champ �lectrique
ve = odeint(Millikan,v0,time)
vle = vls - q*E/(6 * pi * eta * rg)
print 'Vitesse limite dans un champ �lectrique: ',vle
print 'Champ pour une vitesse limite nulle: ', vls*(6 * pi * eta * rg)/q

# calcul de la vitesse de chute sans champ �lectrique
C = (Vg*g*(rhoH - rhoA))/m
vs = odeint(Millikan,v0,time)


# trace des r�sultats
figure()
plot(time,vs,'b-',label='E = 0')
#plot(time,vr,'r-',label='analytique')
plot (time,ve,'g-',label=' E <> 0')

xlabel('temps (s)')
ylabel('vitesse (m.s-1)')
legend(loc='best')
show()
