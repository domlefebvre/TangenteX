# -*- coding: utf-8 -*-

# Programme de tracé du spectre de signaux calculés
# Dominique Lefebvre pour TangenteX.com
# 10 décembre 2014
#

# importation des librairies
from numpy import pi, sin, linspace, where, zeros
from scipy.fftpack import fft, fftfreq
from scipy.signal import square
import matplotlib.pyplot as plt
       

# définition des constantes du signal
K = 2*pi       # facteur conversion période/fréquence

# définition des signaux
def Mono(A,f,T):                 # signal mono-fréquence
  s = A*sin(f*K*T)
  return s

def Composite(A0,f0,A1,f1,t):      # signal composite
  s = A0*sin(f0*K*t) + A1*sin(f1*K*t)
  return s

def Carre(f0,t):                # signal carré symétrique
  # cette fonction génère un signal carré symétrique variant
  # entre -1 et 1, d'une fréquence égale à f0
  s = square(2*pi*f0*t)
  return s
  
def Impulsion(A0,largeur,t):  
  # cette fonction définie une impulsion d'amplitude A0 et
  # de durée égale à largeur ms.  
  s = zeros(t.size)
  for i in range(0,largeur): 
      s[i] = A0
      i=i+1
  return s
  
# paramètres du signal
A0 = 1.0        # amplitude signal
f0 = 10.0       # fréquence signal 
NbPeriode = 2.5  # largeur de la fenêtre exprimée en nb de periodes

# définition de l'échantillonnage
fs = 2*f0
df = 0.01
N = int(fs/df)

# définition temporelle du signal
t0 = 0.0            # dÈbut de l'acquisition du signal
t1 = NbPeriode/f0

# définition du temps
#t = linspace(t0, t1, N)
t = linspace(t0,t1,N)

# Définition du signal traité
signal = Mono(A0,f0,t)

# calcul de la TFD par l'algo de FFT
FFT = abs(fft(signal))    # on ne récupère que les composantes rÈelles

# récupération du domaine fréquentiel
freq = fftfreq(N,1.0/fs)

# extraction des valeurs réelles de la FFT et du domaine frÈquentiel
domaine = where(freq >= 0)

#affichage du signal
plt.subplot(211)
plt.title('Signal et son spectre')
plt.ylim(-A0, A0)
plt.plot(t, signal)
plt.xlabel('Temps (s)'); plt.ylabel('Amplitude')

#affichage du spectre du signal
plt.subplot(212)
plt.xlim(0,f0)
plt.plot(freq[domaine],FFT[domaine]/N)
plt.xlabel('Frequence (Hz)'); plt.ylabel('|FFT|')

plt.tight_layout()
plt.show()
