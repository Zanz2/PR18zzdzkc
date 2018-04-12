import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from Orange.data.filter import SameValue
from Orange.data import Table
import numpy as np
from csv import DictReader
import pandas as pd
from collections import defaultdict
import csv


# Za vsak mesec iščem število prodanega alkohola
# relevantno gledati po atributu Bottle Volume(ml) ali po  Sale(Dollars)
# podatke shranim v slovar, kjer je ključ posamezen mesec letu(1, 2, 3,..,12)

liquor_reader = DictReader(open('/Users/david/Documents/Faks/2.letnik/PR/Project/BigData/Liquor_Data_filt.csv', 'rt', encoding='utf-8'))
#print(liquor_reader.fieldnames)

alkohol_kolicina = defaultdict(float)
alkohol_denar = defaultdict(float)

for i, liquor in enumerate(liquor_reader):
    try:
        # shranim datum in ceno alkohila, ki pa ji odrežem znak $
        datum = pd.DatetimeIndex([liquor['Date']])
        cena = liquor['Sale (Dollars)'].strip("$")
        # za mesec shranim količino alkohola
        alkohol_kolicina[datum.month[0]] += float(liquor['Volume Sold (Liters)'])
        # za še mesec shranim koliko denarja je bilo porabljeno za alkohol
        alkohol_denar[datum.month[0]] += float(cena)
    except Exception as e:
        pass
        #print(i, e)

    #if i % 10000 == 0:
    #    print(i)

meseci = ['januar', 'februar', 'marec', 'april', 'maj', 'junij', 'julij', 'avgust', 'september', 'oktober', 'november', 'december']
# shranim podatke v csv datoteko
with open('/Users/david/Documents/Faks/2.letnik/PR/Project/litri_cena.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    filewriter.writerow(["Mesec", "Kolicina(l)", "Skupna cena($)"])
    for mesec, _ in sorted(alkohol_kolicina.items()):
        print("Mesec: {}, količina prodanega alkohola: {:.2f} litrov, cena: {:.2f}$".format(meseci[mesec - 1], alkohol_kolicina[mesec], alkohol_denar[mesec]))
        filewriter.writerow([mesec, alkohol_kolicina[mesec], alkohol_denar[mesec]])