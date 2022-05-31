'''
Ovo je glavni prozor ove AJNC igrice, koji objedinjuje sav otkucani kod i koristi sve klase stvorene u svrhu igranja.
Uvozi ih kolektivno i zapocinje igricu samim kreiranjem nove instance nase glavne klase "Igra". Odavde se igra pokrece ! 
'''

from classes.KARTA import Karta
from classes.SPIL import Spil
from classes.RUKA import Ruka
from classes.IGRA2 import Igra


if __name__ == "__main__":
    igra = Igra()
