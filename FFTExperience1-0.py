# programme d'experimentation FFT FFTExperience1-0
# Dominique Lefebvre pour TangenteX.com
# 12 aout 2014
#

# importation des librairies
from numpy import pi, sin, linspace, log10
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt       

# définition des constantes du signal
K = 2*pi       # facteur conversion période/fréquence
A0 = 4         # amplitude fréquence fondamentale
A1 = 8         # amplitude première harmonique
f0 = 2         # fréquence fondamentale (Hz)
f1 = 8         # fréquence première harmonique (Hz)

# définition temporelle du signal
t0 = 0         # début de l'acquisition du signal
t1 = 10        # fin de l'acquisition (s)

# définition des paramètres d'échantillonnage
FreqEch = 1024                  # fréquence d'échantillonage
PerEch = 1./FreqEch             # période d'échantillonnage
N = FreqEch*(t1 - t0)           # nombre de points échantillonnés sur l'intervalle

# définition du temps
t = linspace(t0, t1, N)

# définition du signal
signal = A0*sin(f0*K*t) + A1*sin(f1*K*t)

# définition des données de FFT
FenAcq = signal.size             # taille de la fenetre temporelle
    
# calcul de la TFD par l'algo de FFT
signal_FFT = abs(fft(signal))    # on ne récupère que les composantes réelles

# récupération du domaine fréquentiel
signal_freq = fftfreq(FenAcq,PerEch)

# extraction des valeurs réelles de la FFT et du domaine fréquentiel
signal_FFT = signal_FFT[0:len(signal_FFT)//2]
signal_freq = signal_freq[0:len(signal_freq)//2]

#affichage du signal
plt.subplot(211)
plt.title('Signal et son spectre')
plt.ylim(-(A1+5), A1+5)
plt.plot(t, signal)
plt.xlabel('Temps (s)'); plt.ylabel('Amplitude')

#affichage du spectre du signal
plt.subplot(212)
plt.xlim(0,f1+5)
plt.plot(signal_freq,signal_FFT)
plt.xlabel('Frequence (Hz)'); plt.ylabel('Amplitude')
#plt.title('Signal et son spectre')
plt.show()
