# programme BORacine2

from scipy.optimize import fsolve

def f(x):
    return x**2 - 2

racine2 = fsolve(f,1.0)
print racine2





