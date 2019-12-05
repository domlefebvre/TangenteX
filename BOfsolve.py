# programme BOfsolve

from scipy import sin, pi, linspace
from scipy.optimize import fsolve
from matplotlib.pyplot import figure, grid,plot,show

g = 9.81
v0 = 10.0
z0 = 0.0
alpha0 = pi/4.0

def f(t):
    z = -0.5*g*t**2 + v0*sin(alpha0)*t + z0
    return z

t0 = 0.
tmax = 2.0
nbpoint = 100

t = linspace(t0, tmax, nbpoint)
z = f(t)

tvol = fsolve(f,1.0)
print tvol

figure()
grid(True)
plot(t,z)
show()




