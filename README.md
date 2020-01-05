# Analiza_podatkov

## Pogoste številke na EuroJackpotu ##


Analiziral bom zmagovalne številke na EuroJackpotu ter število zmagovalcev.
[Euro Jackpot](https://www.euro-jackpot.net/en/results).

Za vsak datum bom zajel:
* zmagovalne številke
* število zmagovalcev
* zmagovalce po posameznih državah

Delovne hipoteze:
* Ali obstaja povezava med določenimi številkami in številom zmagovalcev?
* Ali je mogoče kakšna številka *srečna* za katero državo?
* Ali države z večjim številom prebivalcev tudi večkrat zadanejo EuroJackpot?

Vsebina:
* tedni.py je pomožen program, za določevanje datuma.
* zajemi_in_shrani.py je program, s katerim sem zajel in shranil internetne strani.
* V euro_out mapi, so internetne strani.
* obdelaj.py je program, s katerim sem naredil json in csv datoteke.
* euro.csv vsebuje osnovne podatke o žrebanju
* stevilke.csv vsebuje podatke o tem, katere številke so bile kdaj izžrebane.
* stevilke_euro.csv vsebuje podatke o tem, katere euro številke so bile kdaj izžrebane.
* total_euro.csv vsebuje podatke o zmagovalcih po datumu.
* po_drzavah_euro.csv vsebuje podatke o posameznih državah.
