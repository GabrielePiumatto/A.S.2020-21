import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

mesi_n = []
temp_media = []
videogame = []
giorni_scuola = []
numero_giorni_giacca = []
data_file = open("es.csv")
data_reader = csv.reader(data_file, delimiter=',')
for row in data_reader:
    mesi_n.append(float(row[0]))
    temp_media.append(float(row[1]))
    videogame.append(int(row[2]))
    giorni_scuola.append(int(row[3]))
    numero_giorni_giacca.append(int(row[4]))

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('Dati di temperatura media, giorni di videogame, giorni in cui si indossa la giacca, giorni in cui si va a scuola al mese')

ax1.plot(mesi_n, temp_media, 'o-g')
ax1.set_xlabel('Mese')
ax1.set_ylabel('Temperatura Media (°C)')

ax2.plot(mesi_n, videogame, 'o-r')
ax2.set_xlabel('Mese')
ax2.set_ylabel('Giorni videogame')

ax3.plot(mesi_n, giorni_scuola, 'o-b')
ax3.set_xlabel('Mese')
ax3.set_ylabel('Giorni scuola')

ax4.plot(mesi_n, numero_giorni_giacca, 'o-y')
ax4.set_xlabel('Mese')
ax4.set_ylabel('Giorni con la giacca')

plt.show()