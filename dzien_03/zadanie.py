"""
OPIS klasy: class Ksiazka_telefoniczna

pola:
    rodzaj : str - priv | company
    wpisy: dict {imie_nazwisko : [email, nr_telefonu],
                imie_nazwisko : [email, nr_telefonu],
                imie_nazwisko : [email, nr_telefonu],
                ....}
metody:
    pokaz_ksiazke - wypisuje wszystkie pozycje po kolei
    dodaj_pozycje(imie_nazwisko, email, nr_telefonu)
"""

class Ksiazka_telefoniczna:
    def __init__(self, rodzaj):
        self.rodzaj = rodzaj
        self.wpisy = None

    def pokaz_ksiazke(self):
        if self.wpisy is None:
            print(f"PUSTO tu.... {self.rodzaj}")
        # a tu pokazemy wpisy

    def dodaj_pozycje(self,imie_nazwisko, email, nr_telefonu):
        if self.wpisy is None:
            self.wpisy = {}

        self.wpisy[imie_nazwisko] = [email, nr_telefonu]


ksiazka_prywatna = Ksiazka_telefoniczna("priv")
ksiazka_sluzbowa = Ksiazka_telefoniczna("company")

ksiazka_prywatna.pokaz_ksiazke()
