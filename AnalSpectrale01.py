# -*- coding: utf-8 -*-

# Programme de tracé du spectre de signaux calculés
# Dominique Lefebvre pour TangenteX.com
# 10 décembre 2014
#

# importation des librairies
from numpy import pi, sin, linspace, random, zeros
from scipy.fftpack import fft, fftfreq
from scipy.signal import square
import matplotlib.pyplot as plt
       

# définition des constantes du signal
K = 2*pi       # facteur conversion période/fréquence

# définition des signaux
def Mono(A0,f0,t):                 # signal mono-fréquence
  s = A0*sin(f0*K*t)
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
  
def BruitageAmplitude(A0,Ab,f0,fb,t):    
    s = A0*sin(f0*K*t) + Ab*random.random(t.size)*sin(fb*K*t)
    return s
    
def BruitageFrequence(A0,Ab,f0,fb,t):    
    s = A0*sin(f0*K*t) + Ab*sin(random.random(t.size)*fb*K*t)
    return s

# définition temporelle du signal
t0 = 0         # dÈbut de l'acquisition du signal
t1 = 10        # fin de l'acquisition (s)

# définition des paramËtres d'échantillonnage
FreqEch = 1024                  # fréquence d'échantillonage
PerEch = 1./FreqEch             # période d'échantillonnage
N = FreqEch*(t1 - t0)           # nombre de points échantillonnés sur l'intervalle

# définition du temps
t = linspace(t0, t1, N)

# Définition du signal traité
A0 = 1     # amplitude signal
f0 = 10    # fréquence signal 
Ab = 0.5   # amplitude bruit
fb = 50    # fréquence bruit 
signal = Carre(f0,t)

# calcul de la TFD par l'algo de FFT
signal_FFT = abs(fft(signal))    # on ne récupère que les composantes rÈelles

# récupération du domaine fréquentiel
signal_freq = fftfreq(N,PerEch)

# extraction des valeurs réelles de la FFT et du domaine frÈquentiel
signal_FFT = signal_FFT[0:len(signal_FFT)//2]
signal_freq = signal_freq[0:len(signal_freq)//2]

#affichage du signal
plt.subplot(211)
plt.title('Signal et son spectre')
#Amax = max(A0,A1) + 3
Amax = A0 + 1 
plt.ylim(-Amax, Amax)
plt.plot(t, signal)
plt.xlabel('Temps (s)'); plt.ylabel('Amplitude')

#affichage du spectre du signal
plt.subplot(212)
#Fmax = max(f0,f1)+5
Fmax = 100
plt.xlim(0,Fmax)
plt.plot(signal_freq,signal_FFT)
plt.xlabel('Frequence (Hz)'); plt.ylabel('Amplitude')

plt.show()
