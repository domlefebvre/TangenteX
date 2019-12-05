#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Régression linéaire avec Python """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "12 janvier 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import size, array, mean
from matplotlib.pyplot import figure,plot,xlim,ylim,xlabel,ylabel,title,scatter,show

from scipy.stats import linregress

  
def CalculCoefficients(x, y): 
    n = size(x)    
    m_x, m_y = mean(x), mean(y) 
    Somme_xy = sum(y*x) - n*m_y*m_x 
    Somme_xx = sum(x*x) - n*m_x*m_x 
    a = Somme_xy / Somme_xx 
    b = m_y - a*m_x   
    return(a, b) 
  
def TraceRegressionLineaire(x, y, coeff): 
    figure(1)
    xlabel('x'); ylabel('y')
    xlim(0,max(x)); ylim(0,max(y))
    title("Regression lineaire")
    # tracé des points de mesure
    scatter(x, y, color = "red", marker = "o", s = 30)   
    # tracé de la droite de régression 
    y_reg = coeff[0]*x + coeff[1]  
    plot(x, y_reg, color = "g") 
    show()    
    return
    
# mesures  
x = array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) 
y = array([0,9,19,29,41,50,62,69,83,95,101,109,119,130,142,149]) 
  
# calcul des coefficients a et b
coeff = CalculCoefficients(x, y) 
         
# tracé de la courbe de regression
TraceRegressionLineaire(x,y,coeff)  
print('Coefficients de regression : a=%.5f b=%.5f'  % (coeff[0],coeff[1]))

# calcul des coefficients avec scipy.stats.linregress
(a_s, b_s, r, tt, stderr) = linregress(x,y)
print('Coefficients de regression calculés par linregress : a=%.5f b=%.5f'  % (a_s,b_s))
