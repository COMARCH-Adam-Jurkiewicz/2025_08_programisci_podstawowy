# """
# Opis klasy: class Ksiązka_telefoniczna
#
# pola:
# rodzaj: str - priv |company
# wpis: dict {imie_nazwisko: [email, nr_telefonu],
#             imie_nazwisko: [email, nr_telefonu],
#             imie_nazwisko: [email, nr_telefonu],
#             imie_nazwisko: [email, nr_telefonu],
#             ...}
# metody:
# pokaz_ksiazke - wypisuje wszytskie pozycje po kolei
# dodaj_pozycje(imie_nazwisko, email, nr_telefonu)
#
# """
# import email


class Ksiazka_telefoniczna:
    def __init__(self, rodzaj):
        self.rodzaj = rodzaj
        self.wpisy = None
    def pokaz_ksiazke(self):
        if self.wpisy is None:
            print(f"PUSTO tu....{self.rodzaj}")
        # a tu pokazemy wpisy
        else:
            print(f"Wpisy w książce ({self.rodzaj}):")
            for imie_nazwisko, dane in self.wpisy.items():
                email, nr_telefonu = dane
                print(f"{imie_nazwisko}: Email: {email}, Tel: {nr_telefonu}")
    def dodaj_pozycje(self, imie_nazwisko, email, nr_telefonu):
    # dwa rodzaje - jak nie mamy jeszcze żadnego wpisu i jak dodajemy kolejny
        if self.wpisy is None:
            self.wpisy = {}
        self.wpisy[imie_nazwisko] = [email, nr_telefonu]



ksiazka_prywatna = Ksiazka_telefoniczna("priv")
ksiazka_sluzbowa = Ksiazka_telefoniczna("company")

#dodanie wpisów
ksiazka_prywatna.dodaj_pozycje("Jan Kowalski", "jan.kowalski@example.com", "123456789")
ksiazka_prywatna.dodaj_pozycje("Anna Nowak", "anna.nowak@example.com", "987654321")
ksiazka_sluzbowa.dodaj_pozycje("Anna Gorska", "anna.gorska@com", "123456789")
ksiazka_prywatna.dodaj_pozycje("Jan Kowalski", "jan.kowalski@example.com", "123456789")
ksiazka_sluzbowa.dodaj_pozycje("Anna Nowak", "ganna.nowak@example.com", "3597063")
ksiazka_sluzbowa.dodaj_pozycje("Danna Zagorska", "anna.zagorska@com", "56748941")

ksiazka_prywatna.pokaz_ksiazke()
ksiazka_sluzbowa.pokaz_ksiazke()