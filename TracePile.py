# programme de trac� d'une courbe de d�charge d'une pile saline
# Dominique Lefebvre pour TangenteX.com
# 18 septembre 2014
#

# importation des librairies
import matplotlib.pyplot as plt

# routine de lecture du fichier de donn�es
def Read_Data(filename):
    datafile = open(filename,'r')
    Ltension = []
    for line in datafile:
        data = line.split(";")
        tension = float(data[1])
        Ltension.append(tension)
    datafile.close()
    return Ltension


# extraction des donn�es
CourbeDecharge = Read_Data('Pile.txt')

# trac� de la courbe de d�charge
plt.title('Courbe de decharge de la pile')
plt.plot (CourbeDecharge[:-1])
plt.xlabel('Temps (pas de 2 mn)'); plt.ylabel('Tension (V)')

plt.show()

