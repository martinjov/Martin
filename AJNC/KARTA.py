'''
Klasa "karta" je najmanja klasa u projektu. Sluzi definisanju pojedinacnih karata spila
i davanju podataka o njihovom znaku i vrednosti(misli se na vizuelnu vrednost, ne onu u igri)
'''
class Karta:
    def __init__(self, znak, vrednost):
        self.znak = znak
        self.vrednost = vrednost

    def __repr__(self):
        return " ".join((self.vrednost, self.znak))
