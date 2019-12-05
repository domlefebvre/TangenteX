#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 SineGordon
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "3 mai 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

# Explicit method for the one-dimensional sine-Gordon equation
# u_tt-u_xx+sin(u)=0, 
# where u=u(x,t) with Neumann boundary conditions and u(x,0)=f(x), u_t(x,0)=g(x).
# Analytical solution u(x,t)=4*arctan(exp((x-x_0-ct)/(sqrt(1-c^2))))

import matplotlib.pyplot as plt
import numpy as np

Tend = 200. # t in [0, Tend] with Nt time points
dt = 0.01
Nt=int(Tend/dt)

L = 40. # x in [-L/2, L/2] with Nx space points
dx =0.05
Nx=int(L/dx)
c=0.2 #velocity of the kink

alp = dt / dx # Condition CFL
print("The Courant number alpha = %f" %(alp))

x = (np.arange(Nx)-Nx/2) * dx #x-Array [-L/2 L/2] 
t = (np.arange(Nt)) * dt
      
u=np.zeros(shape=(Nt+1, Nx)) # solution array


# ---------------kink---------------------
#def f0(x):  
#	return 4.0*np.arctan(np.exp(x/np.sqrt(1.0-c**2)))
	
#def g0(x):  # initial condition g(x,0)=g(x)
#	return (-2.0*c)/(np.cosh(x/np.sqrt(1.0-c**2))*np.sqrt(1.0-c**2))

#----------------antikink-----------------
#def f0(x):  
#	return 4.0*np.arctan(np.exp((-x)/np.sqrt(1.0-c**2)))
	
#def g0(x):  # initial condition g(x,0)=g(x)
#	return (-2.0*c)/(np.cosh(x/np.sqrt(1.0-c**2))*np.sqrt(1.0-c**2))

#------------kink-kink collision--------------
#def f0(x):  
#	return 4.0*np.arctan(np.exp((x+L/4.)/np.sqrt(1.0-c**2)))+4.0*np.arctan(np.exp((x-L/4.)/np.sqrt(1.0-c**2)))	
    
#def g0(x):  # initial condition g(x,0)=g(x)
#	return (-2.0*c)/(np.cosh((x+L/4.)/np.sqrt(1.0-c**2))*np.sqrt(1.0-c**2))+(2.0*c)/(np.cosh((x-L/4.)/np.sqrt(1.0-c**2))*np.sqrt(1.0-c**2))


#------------kink-antikink collision--------------
#def f0(x):  
#	return 4.0*np.arctan(np.exp((x+L/4.)/np.sqrt(1.0-c**2)))+4.0*np.arctan(np.exp(-(x-L/4.)/np.sqrt(1.0-c**2)))	
    
#def g0(x):  # initial condition g(x,0)=g(x)
#	return (-2.0*c)/(np.cosh((x+L/4.)/np.sqrt(1.0-c**2))*np.sqrt(1.0-c**2))+(-2.0*c)/(np.cosh((x-L/4.)/np.sqrt(1.0-c**2))*np.sqrt(1.0-c**2))
#------------breather--------------
def f0(x):  
	return 0.0
    
def g0(x):  # initial condition g(x,0)=g(x)
	return (4.0*np.sqrt(1.-c**2))/(np.cosh(x*np.sqrt(1.-c**2)))

#plt.figure(1,figsize=(24, 12))
#plt.plot(x,f0(x),'b',linewidth=2.0)
#plt.plot(x,g0(x),'r',linewidth=2.0)

#
A=(1.-alp**2)*np.diag(np.ones(Nx))+(alp**2/2.)*np.roll(np.diag(np.ones(Nx)),1,axis=1)+(alp**2/2.0)*np.roll(np.diag(np.ones(Nx)),-1,axis=1) 
A[0,Nx-1]=0.0
A[Nx-1,0]=0.0
A[0,1]=alp**2
A[Nx-1,Nx-2]=alp**2
#
B=2.0*A
#
u[0,:]=f0(x)
u[1,:]=dt*g0(x)+np.dot(A,u[0,:])-dt**2*np.sin(g0(x))/2.
#plt.plot(x,u[0,:],'b',linewidth=2.0)
#plt.plot(x,u[1,:],'r',linewidth=2.0)

#
for j in range (1,Nt):
#
	u[j+1,:]=-u[j-1,:]+np.dot(B,u[j,:])-dt**2*np.sin(u[j,:]) # calculate the next time step 
#
	if j % 150 == 0:
        	plt.figure(2,figsize=(24, 12))
#        	
        	plt.cla()
        	plt.plot(x,u[j,:],'b',linewidth=2.0)
#        	plt.plot(x,f0((x-c*j*dt)),'r--',linewidth=2.0)
        	plt.ylabel("$u(x,t)$")
        	plt.xlabel("$x$")
        	plt.title('u(x,'+ str(j) + ')')
        	#plt.axis([-L/2, L/2, 0, 7])
                plt.axis([-L/2, L/2, np.amin(u[j:,])-0.1, np.amax(u[j,:])-0.1])
		plt.axis([-L/2, L/2, -6, 6])
        	plt.pause(0.1)
        	
	

plt.show()


