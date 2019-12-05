# -*- coding: Latin-1 -*-
# Programme de calcul d'une FFT
# Dominique Lefebvre pour TangenteX.com
# 13 aout 2015
#

# importation des librairies
from scipy import arange, sin, pi
from scipy.fftpack import fft,fftfreq
from matplotlib.pyplot import *
from matplotlib.mlab import magnitude_spectrum

# Fonction de tracé du spectre d'amplitude
# s  : vecteur signal
# Te : période d'échantillonnage
def SpectreAmp(s,Te):
    N = s.size
    # vecteur fréquences
    freq = fftfreq(N,Te)
    freq = freq[range(N/2)]
    # calcul de la FFT normalisée et extraction de la partie réelle positive
    S = abs(fft(s))/N
    S = S[range(N/2)]
    # affichage du spectre d'amplitude 
    plot(freq,S,'ro')
    xlabel('Frequence (Hz)')
    ylabel('Amplitude')
    return
    
def MagSpectrum(s,Fe):
    S,F = magnitude_spectrum(s,Fe,sides='onesided',pad_to=512)
    # affichage du spectre d'amplitude 
    plot(F,S,'r')
    xlabel('Frequence (Hz)')
    ylabel('Amplitude')


# Fonction de définition du signal
def Signal(t):
    A0 = 1.
    A1 = 0.5    
    f0 = 5.  
    f1 = 20.
    K = 2.*pi
    s = A0*sin(K*f0*t) + A1*sin(K*f1*t)
    return s

# définition du signal à traiter
Fe = 200
Te = 1./Fe
# définition du vecteur temps
t0 = 0.
tmax = 1.
t = arange(t0,tmax,Te)
# calcul du signal
s = Signal(t)


# affichage du signal
figure()
subplot(2,1,1)
plot(t,s, 'b')
xlim(t0,tmax)
ylim(s.min(),s.max())
xlabel('Temps (s)')
ylabel('Amplitude')
#Affichage du spectre d'amplitude
subplot(2,1,2)
#SpectreAmp(s,Te)
MagSpectrum(s,Fe)
show()


