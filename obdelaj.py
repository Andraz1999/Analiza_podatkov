import csv
import os
import requests
import re
import tedni
import json

# definiratje URL glavne strani bolhe za oglase z mačkami
euro_frontpage_url = 'https://www.euro-jackpot.net/en/results/'
# mapa, v katero bomo shranili podatke
euro_directory = 'euro_out'
# ime datoteke v katero bomo shranili glavno stran
frontpage_filename = 'index.html'
# ime CSV datoteke v katero bomo shranili podatke
csv_filename = 'euro_CSV'

def read_file_to_string(filename):
    """Funkcija vrne celotno vsebino datoteke "directory"/"filename" kot niz"""
    #full_path = os.path.join(directory, filename)
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()
    



def page_to_ads(page_content):
    """Funkcija poišče posamezne oglase, ki se nahajajo v spletni strani in
    vrne njih seznam"""
    exp = r'<div class="coloumn content">(.*?)<div class="clear">'
    return re.findall(exp, page_content, re.DOTALL)

vzorec_bloka = re.compile(
    r'<ul class="balls">.*?'
    r'<h2>Related Eurojackpot Results Links</h2>',
    flags=re.DOTALL
)

vzorec_zmagovalne_številke = re.compile(
    r'<li class="ball" id="ball_\d">.*<span>(\d.*)</span></li>',
)
vzorec_euro_številke = re.compile(
    r'<li class="euro" id="ball_\d">.*<span>(\d.*)</span></li>',
)

vzorec_jackpot_winner = re.compile(
    r'<div class="elem1">Jackpot<br/>Winners</div>\n\n\s+<div class="elem2">(.*)</div>'
)
vzorec_total_winner = re.compile(
    r'<div class="elem1">Total<br/>Winners</div>\n\n\s+<div class="elem2">(\d.*)</div>',
)
vzorec_jackpot_amount = re.compile(
    r'<div class="elem1">Jackpot<br/>Amount</div>\n\n\s+<div class="elem2">(.*\d.*)</div>',
)

vzorec_za_države = re.compile(
    r'<th>Numbers Matched</th>.*<th>Prize Per Winner</th>.*<th>Winners from.+<div class',
    flags=re.DOTALL
)

vzorec_id = re.compile(
    r'<p>The winning numbers for the (\d+)<sup>'
)


vzorec_drzava3 = re.compile(r'\s+(?P<Match>.*)<br ?/>\n\n<img.+>\s+</td>\n\n\s+<td>(?P<na_zmagovalca>.*)</td>\n\n\s+<td>(?P<v_drzavi>.*)</td>\n\n\s+<td>(?P<sklad>.*)</td>\n\n\s+<td>(?P<vsi_zmagovalci>.*)</td>')



def stevilka(niz):
    while not niz[0].isdigit():
        niz = niz[1:]
    return float(niz.replace(',', ''))



vzorec_druge_drzave = re.compile(r'<th>Winners from(?P<druge_drzave>.*)</th>\n\n\s*<th>Prize Fund Amount</th>\n\n\s+<th>Total Winners</th>\n\n\s+</tr>\n\n\s+</thead>\n\n\s*<tbody>\n\n\s+<tr>\n\n\s+<td>\n\n\s+(?P<Match>.*)<br ?/>\n\n<img.+>\s+</td>\n\n\s+<td>(?P<na_zmagovalca>.*)</td>\n\n\s+<td>(?P<v_drzavi>.*)</td>\n\n\s+<td>(?P<sklad>.*)</td>\n\n\s+<td>(?P<vsi_zmagovalci>.*)</td>')


#def islandija(niz):
#    return round(stevilka(niz) / 138.12, 2)
#
#def norveska(niz):
#    return round(stevilka(niz) / 10.19, 2)
#    
#def svedska(niz):
#    return round(stevilka(niz) / 10.72, 2)

def v_euro(niz, i):
    if i == 8:
        return round(stevilka(niz) / 138.12, 2)
    elif i == 13:
        return round(stevilka(niz) / 10.19, 2)
    elif i == 17:
        return round(stevilka(niz) / 10.72, 2)
 #   elif i == 16:
 #       return round(stevilka(niz) / 10.72, 2)
    elif niz[0] == '€':
        return stevilka(niz)
    elif niz[:2] == 'kn':
        return round(stevilka(niz) / 7.46, 2)
    elif niz[:2] == 'Kc':
        return round(stevilka(niz) / 25.53, 2)
    elif niz[:2] == 'Kč':
        return round(stevilka(niz) / 25.53, 2)
    elif niz[:3] == 'kr.':
        return round(stevilka(niz) / 7.47, 2)
    elif niz[:2] == 'Ft':
        return round(stevilka(niz) / 328.01, 2)
    elif niz[:2] == 'zł':
        return round(stevilka(niz) / 4.26, 2)
    elif niz[:2] == 'zł':
        return round(stevilka(niz) / 4.26, 2)

def seznam_int(sez):
    seznam = []
    for i in sez:
        seznam.append(int(i))
    return seznam

##################csv######################################3

def zapisi_csv(slovarji, imena_polj, ime_datoteke='euro.csv'):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    with open(ime_datoteke, 'w', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in slovarji:
            writer.writerow(slovar)

###########################################################################

# Pred 8.9.2017 Poljska še ni sodelovala, zato je tam malo drugace

###########################################################################

# csv ##
def razgnezdi(slovar, datum):
    nov = {}
    for i in slovar:
        vmesni = {}
        for j in range(len(slovar[i])):
            vmesni[i] = slovar[i][j]
            vmesni['datum'] = datum
            nov[j] = vmesni.copy()
    return nov



def razgnezdi2(slovar, datum):
    nov = {}
    for i in slovar:
        vmesni = {}
        j = 0
        for drzava in slovar[i]:
            for kategorija in slovar[i][drzava]:  
              vmesni['datum'] = datum
              vmesni['država'] = drzava
              vmesni['Katera nagrada'] = kategorija[0]
              vmesni['Nagrada na zmagovalca'] = kategorija[1]
              vmesni['Zmagovalci iz države'] = kategorija[2]
              vmesni['Sklad'] = kategorija[3]
              nov[j] = vmesni.copy()
              j += 1
    return nov 

def zapisi_csv(slovarji, imena_polj, kljuc, ime_datoteke='euro.csv'):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    with open(ime_datoteke, 'a', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        if kljuc:
            writer.writeheader()
        writer.writerow(slovarji)

def zapisi_csv2(slovarji, imena_polj, kljuc, ime_datoteke='euro.csv' ):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    with open(ime_datoteke, 'a', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        if kljuc:
            writer.writeheader()
        for slovar in slovarji:
            writer.writerow(slovarji[slovar])

######################################################################



#datum = [8, 9, 2017]
#niz = '08-09-2017'
datum = [25, 10, 2019]
niz = '25-10-2019'
directory = euro_directory
#with open('euro111.json', 'w') as f:
if True:



    for st in range(397): #range 111
        filename = 'euro_' + niz + frontpage_filename
        path = os.path.join(directory, filename)
        if os.path.isfile(path):


    ##########################
            text = read_file_to_string(path)
            id = int(vzorec_id.findall(text)[0])
            isci = vzorec_bloka.findall(text)
            jackpot_winner = int(stevilka(vzorec_jackpot_winner.findall(isci[0])[0]))
            jackpot_amount = int(stevilka(vzorec_jackpot_amount.findall(isci[0])[0]))
            total_winner = int(stevilka(vzorec_total_winner.findall(isci[0])[0]))
            stevilke = seznam_int(vzorec_zmagovalne_številke.findall(isci[0]))
            euro_stevilke = seznam_int(vzorec_euro_številke.findall(isci[0]))
            zmagovalne_stevilke = {'stevilke': stevilke, 'euro': euro_stevilke}
            zmagovalci = vzorec_jackpot_winner.findall(isci[0])
            vsi_zmagovalci = vzorec_total_winner.findall(isci[0])
            znesek = vzorec_jackpot_amount.findall(isci[0])
            idrzava = vzorec_drzava3.findall(isci[0])
            drzava = vzorec_druge_drzave.findall(isci[0])

            total = []
            for i in range(12):
                total.append(int(stevilka(idrzava[i][4])))
            total = tuple(total)

            slovar = {}
            j = 0
            for i in range(len(drzava)):
                ime = (drzava[i][0]).strip()
                nagrada = v_euro(idrzava[j][1].replace('&#269;', 'č'), i)
                zmagovalci = int(stevilka(idrzava[j][2]))
                sklad = v_euro(idrzava[j][3].replace('&#269;', 'č'), i)
                slovar[ime] = [(idrzava[j][0], nagrada, zmagovalci, sklad)]
                j += 1
                while idrzava[j][0] != 'Match 5 and 2 Euro Numbers':
                    nagrada = v_euro(idrzava[j][1].replace('&#269;', 'č'), i)
                    zmagovalci = int(stevilka(idrzava[j][2]))
                    sklad = v_euro(idrzava[j][3].replace('&#269;', 'č'), i)
                    slovar[ime].append((idrzava[j][0], nagrada, zmagovalci, sklad))
                    j += 1
                    if j == len(idrzava):
                        break

            to = niz.replace('-', '.')
            vse = {'datum': to, 
            'id': id, 
            'stevilke':{'ball': stevilke, 'euro': euro_stevilke}, 
            'jackpot_winners': jackpot_winner,
            'total_winners': total_winner,
            'jackpot_amount': jackpot_amount,
            'total': total,
            'drzave': slovar
            }   
  ##################################################################
  #  za csv
  # 
            kljuc = (st == 0)
            nov_slovar = {'datum': vse['datum'], 'id': vse['id'], 'winners': vse['jackpot_winners'], 'total': vse['total_winners'], 'amount': vse['jackpot_amount'] }
            stevilke_slovar = {'stevilke': vse['stevilke']['ball']}
            euro_slovar = {'stevilke': vse['stevilke']['euro']}  
            stevilke_slovar = razgnezdi(stevilke_slovar, vse['datum'])
            euro_slovar = razgnezdi(euro_slovar, vse['datum'])
            total_slovar = {
            'Match 5 and 2 Euro Numbers': vse['total'][0],
            'Match 5 and 1 Euro Number': vse['total'][1],
            'Match 5': vse['total'][2],
            'Match 4 and 2 Euro Numbers': vse['total'][3],
            'Match 4 and 1 Euro Number': vse['total'][4],
            'Match 4': vse['total'][5],
            'Match 3 and 2 Euro Numbers': vse['total'][6],
            'Match 2 and 2 Euro Numbers': vse['total'][7],
            'Match 3 and 1 Euro Number': vse['total'][8],
            'Match 3': vse['total'][9],
            'Match 1 and 2 Euro Numbers': vse['total'][10],
            'Match 2 and 1 Euro Number': vse['total'][11]
            }
            drzave_slovar = {'drzave': vse['drzave']}
            po_drzavah = razgnezdi2(drzave_slovar, vse['datum'])

            zapisi_csv(nov_slovar, [i for i in nov_slovar], kljuc)
            zapisi_csv2(stevilke_slovar, ['datum','stevilke'], kljuc, 'stevilke.csv')
            zapisi_csv2(euro_slovar, ['datum','stevilke'], kljuc, 'stevilke_euro.csv')
            zapisi_csv(total_slovar, [i for i in total_slovar], kljuc, 'total_euro.csv')
            zapisi_csv2(po_drzavah, [i for i in po_drzavah[0]], kljuc, 'po_drzavah_euro.csv')

####################################################################
            #json.dump(vse, f, indent=2, ensure_ascii=True)           
            print((st, '...shranjeno!'))
        else:
            print(st, 'ne obstaja')
        datum = tedni.sedem_dni_nazaj(datum)
        niz = tedni.pretvori_v_niz(datum)
        




