'''
Klasa "spil" predstavlja skup od 52 karte predstavljene klasom "karta"(koju ova klasa koristi),
a koje se definisu komprehencijom lista znakova i njihovih vrednosti.
Ova klasa ima metodu mesanja karata i deljenja karata igracu i krupijeu.
'''
import random
from .KARTA import Karta


class Spil:
    def __init__(self):
        self.karte = [Karta(znak, broj) for znak in ["Pik", "Tref", "Srce",
                                                      "Karo"] for broj in ["Kec", "2", "3", "4", "5", "6",
                                                                                 "7", "8", "9", "10", "Dzoker", "Kraljica", "Kralj"]]

    def promesaj(self):
        if len(self.karte) > 1:
            random.shuffle(self.karte)

    def podeli(self):
        if len(self.karte) > 1:
            return self.karte.pop(0)