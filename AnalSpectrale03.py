# -*- coding: Utf-8 -*-

# Programme d'étude du repliement du spectre
# Dominique Lefebvre pour TangenteX.com
# 18 décembre 2014
#

# importation des librairies
from numpy import pi, sin, linspace
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt
       

# définition des constantes du signal
K = 2*pi       # facteur conversion période/fréquence

# définition du signal
def Composite(A0,f0,A1,f1,A2,f2,BruitHF,t):  
  s = A0*sin(f0*K*t) + A1*sin(f1*K*t) + A2*sin(f2*K*t)
  if BruitHF:
      B = 0.5      
      HF = 2270   
      s += B*sin(HF*K*t)
  return s


# définition temporelle du signal
t0 = 0         # dÈbut de l'acquisition du signal
t1 = 10       # fin de l'acquisition (s)

# Caractéristiques du signal
A0 = 1    
f0 = 10
A1 = 0.5
f1 = 50
A2 = 0.1
f2 = 100

# choix de la fréquence d'échantillonnage
print "La fréquence de Nyquist du signal est : ",f2*2.0, "Hz"
print "La fréquence d'échantillonnage doit être égale à au moins ",f2*2.0," Hz"
FreqEch = float(input("Frequence d'echantillonnage : "))

# définition des paramètres d'échantillonnage
PerEch = 1./FreqEch      # période d'échantillonnage
N = FreqEch*(t1 - t0)    # nombre de points échantillonnés sur l'intervalle

# définition du temps
t = linspace(t0, t1, N)

# Génération du signal
signal = Composite(A0,f0,A1,f1,A2,f2,False,t)

# définition des donnÈes de FFT
FenAcq = signal.size             # taille de la fenetre temporelle
    
# calcul de la TFD par l'algo de FFT
signal_FFT = abs(fft(signal))    # on ne récupère que les composantes réelles

# récupération du domaine fréquentiel
signal_freq = fftfreq(FenAcq,PerEch)

# extraction des valeurs réelles de la FFT et du domaine fréquentiel
signal_FFT = signal_FFT[0:len(signal_FFT)//2]
signal_freq = signal_freq[0:len(signal_freq)//2]

# affichage du signal
plt.subplot(211)
plt.title('Signal et son spectre')
Amax = A0 + 1 
plt.xlim(t0,t1)
plt.ylim(-Amax, Amax)
plt.plot(t, signal)
plt.xlabel('Temps (s)'); plt.ylabel('Amplitude')

# affichage du spectre du signal
plt.subplot(212)
plt.xlim(0,signal_freq.max())
plt.plot(signal_freq,signal_FFT/signal_FFT.max())
plt.xlabel('Frequence (Hz)'); plt.ylabel('Amplitude')

plt.show()
