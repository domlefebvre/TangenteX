# -*- coding: Latin-1 -*-
# Recherche de racines d'une fonction à une variable réelle
# par la méthode Newton-Raphson
# Dominique Lefebvre pour TangenteX.com
# 31 juillet 2017
#

# Routine de Newton-Raphson
def NewtonRaphson(f,df,x,eps,NbMaxIter):
    X = f(x)
    n = 0
    while abs(X) > eps and n <= NbMaxIter:
        Xpoint = df(x)
        try:
            x = x - X/Xpoint
            n += 1
            X = f(x)
        except ZeroDivisionError:
            x = 0.0
            n =0
    return x,n
    

# Fonction dont on cherche les racines
def f(x):
    return x**3 + 4*x**2 + 5
    
# Dérivée de la fonction cible
def df(x):
    return 3*x**2 + 8*x
    
# programme principal
    
# paramètres de calcul
xi = -4.0
epsilon = 1.0e-6
NbIter = 100

x0,n = NewtonRaphson(f,df,xi,epsilon,NbIter)

print'racine : ',x0, ' nb iterations : ',n