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
        elif mesec in [2, 4, 6, 9, 11]:
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

#datum = [1, 3, 2019]
#for _ in range(10):
#    datum = sedem_dni_nazaj(datum)
#    print(datum)
    






