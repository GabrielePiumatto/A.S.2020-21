import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

year = []
total = []
gas_fuel = []
liquid_fuel = []
solid_fuel = []
cement = []
gas_flaring = []
per_capita = []
year_d = []
value = []
data_file = open("CO2_emissions.csv")
data_reader = csv.reader(data_file, delimiter=',')
data_file_d = open("Temperature_Anomaly.csv")
data_reader_d = csv.reader(data_file_d, delimiter=',')
for row in data_reader:
    year.append(float(row[0]))
    total.append(float(row[1]))
    gas_fuel.append(int(row[2]))
    liquid_fuel.append(int(row[3]))
    solid_fuel.append(int(row[4]))
    cement.append(int(row[5]))
    gas_flaring.append(int(row[6]))
    per_capita.append(float(row[7]))

for row in data_reader_d:
    year_d.append(int(row[0]))
    value.append(float(row[1]))

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('Emissioni di CO2 causate da :')

ax1.plot(year, total, '-g')
ax1.set_xlabel('Anno')
ax1.set_ylabel('Totale Emissioni all anno (10^9*kg)')

ax2.plot(year, gas_fuel, '-r')
ax2.set_xlabel('Anno')
ax2.set_ylabel('Combustibili Gassosi (10^9*kg)')

ax3.plot(year, liquid_fuel, '-b')
ax3.set_xlabel('Anno')
ax3.set_ylabel('Combustibili Liquidi (10^9*kg)')

ax4.plot(year, solid_fuel, '-y')
ax4.set_xlabel('Anno')
ax4.set_ylabel('Combustibili Liquidi (10^9*kg)')

plt.show()