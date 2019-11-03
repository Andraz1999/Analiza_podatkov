def vcerajsnji_datum(sez):
    dan = sez[0]
    mesec = sez[1]
    leto = sez[2]
    if dan != 1:
        dan -= 1
    else:
        if mesec == 3:
            if leto % 4 == 0:
                dan = 29
            else:
                dan = 28
            mesec = 2
        elif mesec in [2, 4, 6, 8, 9, 11]:
            dan = 31
            mesec -= 1
        elif mesec == 1:
            dan = 31
            mesec = 12
            leto -= 1
        else:
            mesec -=1
            dan = 30
    return [dan, mesec, leto]

def sedem_dni_nazaj(sez):
    for _ in range(7):
        sez = vcerajsnji_datum(sez)
    return sez

def pretvori_v_niz(sez):
    niz = ''
    for i in sez:
        if i < 10:
            i = '0' + str(i)
        else: 
            i = str(i)
        niz += i + '-'
    return niz[:-1]

def povezava(sez):
    datum = sedem_dni_nazaj(sez)
    return pretvori_v_niz(datum)



#iskani = [23, 3, 2012]
#datum = [1, 3, 2019]
#i = 1
#for i in range(450):
#    datum = sedem_dni_nazaj(datum)
#    print(i, datum)
# pri 360    

#iskani = [23, 3, 2012]
#datum = [25, 10, 2019]
#niz = '25-10-2019'
#for i in range(397):
#    print (i, niz )
#    datum = sedem_dni_nazaj(datum)
#    niz = pretvori_v_niz(datum)
#    #2.8.2019


#
#nov_slovar = {'datum': en_slovar['datum'], 'id': en_slovar['id'], 'winners': en_slovar['jackpot_winners'], 'total': en_slovar['total_winners'], 'amount': en_slovar['jackpot_amount'] }
#
#stevilke_slovar = {'stevilke': en_slovar['stevilke']['ball']}
#euro_slovar = {'stevilke': en_slovar['stevilke']['euro']}
#
#def razgnezdi(slovar, datum):
#    nov = {}
#    for i in slovar:
#        vmesni = {}
#        for j in range(len(slovar[i])):
#            vmesni[i] = slovar[i][j]
#            vmesni['datum'] = datum
#            nov[j] = vmesni.copy()
#    return nov
#
#stevilke_slovar = razgnezdi(stevilke_slovar, '123')
#euro_slovar = razgnezdi(euro_slovar, '123')
#
#
#

#total_slovar = {
#    'Match 5 and 2 Euro Numbers': en_slovar['total'][0],
#    'Match 5 and 1 Euro Number': en_slovar['total'][1],
#    'Match 5': en_slovar['total'][2],
#    'Match 4 and 2 Euro Numbers': en_slovar['total'][3],
#    'Match 4 and 1 Euro Number': en_slovar['total'][4],
#    'Match 4': en_slovar['total'][5],
#    'Match 3 and 2 Euro Numbers': en_slovar['total'][6],
#    'Match 2 and 2 Euro Numbers': en_slovar['total'][7],
#    'Match 3 and 1 Euro Number': en_slovar['total'][8],
#    'Match 3': en_slovar['total'][9],
#    'Match 1 and 2 Euro Numbers': en_slovar['total'][10],
#    'Match 2 and 1 Euro Number': en_slovar['total'][11]
#}
#
#
#drzave_slovar = {'drzave': en_slovar['drzave']}
#
#def razgnezdi2(slovar, datum):
#    nov = {}
#    for i in slovar:
#        vmesni = {}
#        j = 0
#        for drzava in slovar[i]:
#            for kategorija in slovar[i][drzava]:  
#              vmesni['datum'] = datum
#              vmesni['država'] = drzava
#              vmesni['Katera nagrada'] = kategorija[0]
#              vmesni['Nagrada na zmagovalca'] = kategorija[1]
#              vmesni['Zmagovalci iz države'] = kategorija[2]
#              vmesni['Sklad'] = kategorija[3]
#              nov[j] = vmesni.copy()
#              j += 1
#    return nov 
#
#
#            
#
#po_drzavah = razgnezdi2(drzave_slovar, 'datum')
#
#def zapisi_csv(slovarji, imena_polj, ime_datoteke='euro.csv'):
#    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
#    with open(ime_datoteke, 'a', encoding='utf-8') as csv_datoteka:
#        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
#        writer.writeheader()
#        writer.writerow(slovarji)
#
#def zapisi_csv2(slovarji, imena_polj, ime_datoteke='euro.csv' ):
#    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
#    with open(ime_datoteke, 'a', encoding='utf-8') as csv_datoteka:
#        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
#        writer.writeheader()
#        for slovar in slovarji:
#            writer.writerow(slovarji[slovar])
#
#zapisi_csv(nov_slovar, [i for i in nov_slovar])
#zapisi_csv2(stevilke_slovar, ['datum','stevilke'], 'stevilke.csv')
#zapisi_csv2(euro_slovar, ['datum','stevilke'], 'stevilke_euro.csv')
#zapisi_csv(total_slovar, [i for i in total_slovar], 'total_euro.csv')
#zapisi_csv2(euro_slovar, ['datum','stevilke'], 'stevilke_euro.csv')
#zapisi_csv2(po_drzavah, [i for i in po_drzavah[0]], 'po_drzavah_euro.csv')
#
