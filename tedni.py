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







