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
        print(f"Książka: {self.rodzaj} {self.wpisy}")


    def dodaj_pozycje(self,imie_nazwisko, email, nr_telefonu):
        if self.wpisy is None:
            self.wpisy = {}
        self.wpisy[imie_nazwisko] = [email, nr_telefonu]


ksiazka_prywatna = Ksiazka_telefoniczna("prywatna")
ksiazka_sluzbowa = Ksiazka_telefoniczna("służbowa")

Ksiazka_telefoniczna.dodaj_pozycje(ksiazka_prywatna, "Adrian Kubicki", "adi@wp.pl", "505123123")
Ksiazka_telefoniczna.dodaj_pozycje(ksiazka_prywatna, "Konrad Piwnik", "kondek@wp.pl", "888123123")

ksiazka_prywatna.dodaj_pozycje("Adam_Jurkiewicz","adam@jurkiewicz.tech", "662.144.425")
ksiazka_prywatna.dodaj_pozycje("Beata_Jurkiewicz","beata@jurkiewicz.tech", "662.144.425")
ksiazka_prywatna.dodaj_pozycje("Szymon_Jurkiewicz","szymon@jurkiewicz.tech", "662.144.425")
ksiazka_prywatna.dodaj_pozycje("Adam_Jurkiewicz","xxxxx@jurkiewicz.tech", "662.144.425")

ksiazka_sluzbowa.dodaj_pozycje("S_Adam_Jurkiewicz","adam@jurkiewicz.tech", "662.144.425")
ksiazka_sluzbowa.dodaj_pozycje("S_Beata_Jurkiewicz","beata@jurkiewicz.tech", "662.144.425")
ksiazka_sluzbowa.dodaj_pozycje("S_Szymon_Jurkiewicz","szymon@jurkiewicz.tech", "662.144.425")
ksiazka_sluzbowa.dodaj_pozycje("S_Adam_Jurkiewicz","xxxxx@jurkiewicz.tech", "662.144.425")



Ksiazka_telefoniczna.pokaz_ksiazke()
Ksiazka_telefoniczna.pokaz_ksiazke()





