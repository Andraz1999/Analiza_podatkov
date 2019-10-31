import csv
import os
import requests
import re
import tedni

###############################################################################
# Najprej definirajmo nekaj pomožnih orodij za pridobivanje podatkov s spleta.
###############################################################################

# definiratje URL glavne strani bolhe za oglase z mačkami
euro_frontpage_url = 'https://www.euro-jackpot.net/en/results/'
# mapa, v katero bomo shranili podatke
euro_directory = 'euro_out'
# ime datoteke v katero bomo shranili glavno stran
frontpage_filename = 'index.html'
# ime CSV datoteke v katero bomo shranili podatke
csv_filename = 'euro_CSV'


def download_url_to_string(url):
    """Funkcija kot argument sprejme niz in puskuša vrniti vsebino te spletne
    strani kot niz. V primeru, da med izvajanje pride do napake vrne None.
    """
    try:
        # del kode, ki morda sproži napako
        page_content = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('stran ne obstaja!')
        return 'Ne'
    #except Exception as e:
        # koda, ki se izvede pri napaki
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
     #   print(e)
    # nadaljujemo s kodo če ni prišlo do napake
    return page_content.text

def save_string_to_file(text, directory, filename):
    """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
    locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
    niz "directory" prazen datoteko ustvari v trenutni mapi.
    """
    if text == 'Ne':
        return None
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    print('........shranjeno')
    return None


# Definirajte funkcijo, ki prenese glavno stran in jo shrani v datoteko.


def save_frontpage(page, directory, filename):
    """Funkcija shrani vsebino spletne strani na naslovu "page" v datoteko
    "directory"/"filename"."""

    page_data = download_url_to_string(page)
    save_string_to_file(page_data, directory, filename)


datum = [25, 10, 2019]
niz = '25-10-2019'
directory = euro_directory
#filename = 'euro_' + niz + frontpage_filename  
#path = os.path.join(directory, filename)

for i in range(397):
    page = euro_frontpage_url + niz
    filename = 'euro_' + niz + frontpage_filename
    path = os.path.join(directory, filename)
    if os.path.isfile(path):
        print('shranjeno že od prej!')    
    else:
        save_frontpage(page, directory, filename) 
    datum = tedni.sedem_dni_nazaj(datum)
    niz = tedni.pretvori_v_niz(datum)
