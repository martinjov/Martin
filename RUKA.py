'''
Klasa "ruka" predstavlja skup karata koji igrac ili krupije pojedinacno u datom trenutku poseduju.
Ova klasa takodje koristi klasu "karta" i esencijalna je za nasu igru i najvecu klasu "igra".
Poseduje metode dodavanja nove karte u ruku za igraca ili krupijea, racunanja ukupne vrednosti karata
u posedu igraca ili krupijea, kao i prosledjivanja datih vrednosti dalje. Prikaz vrednostii karata
u ruci krupijea ili igraca se vrsi tako sto je prva krupijeova karta po pravilu uvek sakrivena, a druga vidljiva.
'''
from .KARTA import Karta


class Ruka:
    def __init__(self, krupije=False):
        self.krupije = krupije
        self.karte = []
        self.vrednost = 0

    def dodaj_kartu(self, karta):
        self.karte.append(karta)

    def izracunaj_vrednost(self):
        self.vrednost = 0
        ima_keca = False
        for karta in self.karte:
            if karta.vrednost.isnumeric():
                self.vrednost += int(karta.vrednost)
            else:
                if karta.vrednost == "Kec":
                    ima_keca = True
                    self.vrednost += 11
                else:
                    self.vrednost += 10
        if ima_keca and self.vrednost > 21:
            self.vrednost -= 10

    def get_vrednost(self):
        self.izracunaj_vrednost()
        return self.vrednost

    def prikazi(self):
        if self.krupije and self.get_vrednost()==21:
            for karta in self.karte:
                print(karta)
            print("Vrednost:", self.get_vrednost(),'\n')

        elif self.krupije:
            print("Sakrivena karta")
            print(self.karte[1],'\n')
        else:
            for karta in self.karte:
                print(karta)
            print("Vrednost:", self.get_vrednost(),'\n')
