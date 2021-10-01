import csv #SERVE PER IL FILE CSV
import pygame #SERVE PER FAR APPARIRE IL QR CODE SU UNA SCHERMATA

#DIZIONARIO CHE ATTRIBUISCE AD OGNI CARATTERE UN CODICE BINARIO A 5 BIT
#TUTTI I NUMERI, LE LETTERE MINUSCOLE DELL'ALFABETO ITALIANO, LO SPAZIO
dizionario = {"0":"0,0,0,0,0", "1":"0,0,0,0,1", "2":"0,0,0,1,0", "3":"0,0,0,1,1", "4":"0,0,1,0,0", "5":"0,0,1,0,1", "6":"0,0,1,1,0", "7":"0,0,1,1,1",
              "8":"0,1,0,0,0", "9":"0,1,0,0,1", " ":"0,1,0,1,0", "a":"0,1,0,1,1", "b":"0,1,1,0,0", "c":"0,1,1,0,1", "d":"0,1,1,1,0", "e":"0,1,1,1,1",
              "f":"1,0,0,0,0", "g":"1,0,0,0,1", "h":"1,0,0,1,0", "i":"1,0,0,1,1", "l":"1,0,1,0,0", "m":"1,0,1,0,1", "n":"1,0,1,1,0", "o":"1,0,1,1,1",
              "p":"1,1,0,0,0", "q":"1,1,0,0,1", "r":"1,1,0,1,0", "s":"1,1,0,1,1", "t":"1,1,1,0,0", "u":"1,1,1,0,1", "v":"1,1,1,1,0", "z":"1,1,1,1,1"}

#LE DIMENSIONI DELLA SCHERMATA
DIMENSIONI = (600,600)
#IMPOSTAZIONE RGB PER COLORI BIANCO E NERO
BIANCO = (255,255,255)
NERO = (0,0,0)

#INSERISCE LA STRINGA
stringa = input('Inserisci una stringa lunga 12 caratteri al massimo : ')

#PARTE GRAFICA DEL QR CODE
def qrcode():
    dimensionex = DIMENSIONI[0]//COLONNE
    dimensioney = DIMENSIONI[1]//NRIGHE
    dimensione = 50

#DIVIDE LA STRINGA IN LETTERE
def dividi(lettere): 
    return [char for char in lettere]

#PRENDE I PARAMENTRI DI ARRAY E DIZIONARIO
#new array is the input word split into letters
def StampaInBinario(dict, chiave): 
  for lista in dict: 
    if lista in chiave:
        #PRENDE IL CODICE BINARIO ASSOCIATO ALLA LETTERA E 
        #LO SALVA NELLA VARIABILE x
        x = chiave.get(lista)
        #STAMPA LA LETTERA CON IL CODICE BINARIO ASSOCIATO
        with open('file.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            print(lista + ' : ' + x)
            csvwriter.writerow(lista + ' : '+ x)

#DIVIDE LA PAROLA
array = dividi(stringa)
#SERVE PER STAMPARE LE LETTERE CON IL CODICE BINARIO ASSOCIATO
StampaInBinario(array, dizionario)
