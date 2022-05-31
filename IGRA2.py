'''
Klasa "Igra" je glavna klasa ovog projekta i pokretac same kartaske igrice.
Implementira sve klase projekta u celinu i koristi algoritam za prolazak kroz mnostvo potencijalnih slucajeva
i ishoda koji se mogu javiti u igrici. Sam konstruktor klase je pokretac igrice, tako da se pri samom instanciranju
ove klase pokrece igrica. Sastoji se od dve ugnjezdene petlje. Unutrasnja kontrolise tok jedne runde igre,
dok spoljasnja regulise mogucnost produzetka igranja, u skladu sa zeljama igraca.
Ova klasa ima na raspolaganju 3 metode. Prva metoda proverava mogucnost da igrac prebaci vrednost od 21 tokom igre
i samim tim se prekida tok runde jer je igrac izgubio, a krupije pobednik. Druga klasa proverava mogucnost da neko
od ucesnika(sam igrac ili krupije) imaju ukupno u ruci vrednost 21, sto automatski prekida datu rundu.
Treca klasa sluzi za ispis konacnog ishoda runde u slucaju njenog zavrsetka. Koristi drugu klasu u svrhu odluke.
BITNO JE NAPOMENUTI da AJNC moze da se igra i sa vise igraca (i jednim krupijeom),
ali ova igrica daje mogucnost igranja samo jednom igracu pored krupijea istovremeno.
'''
from .KARTA import Karta
from .SPIL import Spil
from .RUKA import Ruka


class Igra:
    def __init__(self):
        igra_se = True
        while igra_se:
            self.spil = Spil()
            self.spil.promesaj()
            self.igrac_ruka = Ruka()
            self.krupije_ruka = Ruka(krupije=True)
            for i in range(2):
                self.igrac_ruka.dodaj_kartu(self.spil.podeli())
                self.krupije_ruka.dodaj_kartu(self.spil.podeli())
            print()
            print("Tvoja ruka je:\n")
            self.igrac_ruka.prikazi()
            print("\nKrupijeova ruka je:\n")
            self.krupije_ruka.prikazi()

            kraj_igre = False
            while not kraj_igre:
                igrac_ima21, krupije_ima21 = self.ima_li_21()

                if igrac_ima21 or krupije_ima21:
                    kraj_igre = True
                    self.pokazi_rezultate_ajnca(igrac_ima21, krupije_ima21)
                    continue
                izbor = input("Molim vas izaberite da li uzimate sledecu kartu (Uzimam) ili (Preskacem): ").lower()
                while izbor not in ["u", "p", "uzimam", "preskacem"]:
                    izbor = input("Molim vas izaberite da li uzimate sledecu kartu (Uzimam) ili (Preskacem): ").lower()
                if izbor in ['u', 'uzimam']:
                    self.igrac_ruka.dodaj_kartu(self.spil.podeli())
                    self.igrac_ruka.prikazi()
                    if self.igrac_prebacio():
                        print("Prebacili ste 21 ! Izgubili ste rundu !\n")
                        print('______________________________________')
                        kraj_igre = True
                else:
                    vrednost_igraceve_ruke = self.igrac_ruka.get_vrednost()
                    vrednost_krupijeove_ruke = self.krupije_ruka.get_vrednost()
    
                    print("\nKONACAN REZULTAT: \n")
                    print("Tvoja ruka je:", vrednost_igraceve_ruke)
                    print("Krupijeova ruka je:", vrednost_krupijeove_ruke)
    
                    if vrednost_igraceve_ruke > vrednost_krupijeove_ruke:
                        print("Cestitamo ! Pobedili ste rundu !\n")
                        print('______________________________________')
                    elif vrednost_igraceve_ruke == vrednost_krupijeove_ruke:
                        print("Rezultat ove runde je izjednacen !\n")
                        print('______________________________________')
                    else:
                        print("Na vasu zalost, krupije je pobedio !\n")
                        print('______________________________________')
                    kraj_igre = True
                    
            print()
            ponovo = input("Zelite li novu rundu? (DA) ili (NE): ")
            while ponovo.lower() not in ["d", "n", "da", "ne"]:
                ponovo = input("Zelite li novu rundu? (DA) ili (NE): ")
            print('______________________________________\n')
            if (ponovo.lower() == "n") or (ponovo.lower() == "ne"):
                print("Hvala vam sto ste igrali AJNC ! Vidimo se opet !")
                igra_se = False

    def ima_li_21(self):
        igrac = False
        krupije = False
        if self.igrac_ruka.get_vrednost() == 21:
            igrac = True
        if self.krupije_ruka.get_vrednost() == 21:
            krupije = True
        return (igrac, krupije)

    def pokazi_rezultate_ajnca(self, igrac_ima21, krupije_ima21):
        if igrac_ima21 and krupije_ima21:
            print("\nOBA igraca imaju po 21 ! NERESENO JE !\n")
            print('______________________________________')
        elif igrac_ima21:
            print("\nIMATE 21 ! POBEDILI STE !\n")
            print('______________________________________')
        elif krupije_ima21:
            print("\nKrupije ima 21 ! Nazalost, izgubili ste.\n")
            print('______________________________________')
            kraj_igre = False

    def igrac_prebacio(self):
        return self.igrac_ruka.get_vrednost() > 21
