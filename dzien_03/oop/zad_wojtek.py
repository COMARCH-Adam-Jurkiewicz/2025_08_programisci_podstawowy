class Ksiazka_telefoniczna:
    def __init__(self, rodzaj):
        self.rodzaj = rodzaj
        self.wpisy = None

    def pokaz_ksiazke(self):
        if self.wpisy is None:
            print(f"PUSTO tu...{self.rodzaj}")
        else:
            print(f"\nKsiązka telefoniczna ({self.rodzaj})")
            for imie_nazwisko, dane in self.wpisy.items():
                email, nr_tel = dane
                print(f" - {imie_nazwisko} | email: {email} | tel: {nr_tel}")


    def dodaj_pozycje(self, imie_nazwisko, email, nr_telefonu):
        if self.wpisy is None:
            self.wpisy = {}

        self.wpisy[imie_nazwisko] = [email, nr_telefonu]


ksiazka_prywatna = Ksiazka_telefoniczna("priv")
ksiazka_sluzbowa = Ksiazka_telefoniczna("company")

ksiazka_prywatna.dodaj_pozycje("Jan Kowalski", "jan.kowalski@mail.com", "123-456-789")
ksiazka_prywatna.dodaj_pozycje("Anna Nowak", "anna.nowak@mail.com", "987-654-321")



ksiazka_sluzbowa.dodaj_pozycje("Marek Wiśniewski", "marek.wisniewski@firma.pl", "22-111-222")
ksiazka_sluzbowa.dodaj_pozycje("Ewa Kaczmarek", "ewa.kaczmarek@firma.pl", "22-333-444")

ksiazka_prywatna.pokaz_ksiazke()
ksiazka_sluzbowa.pokaz_ksiazke()


# Pokaż oryginalną wiadomość