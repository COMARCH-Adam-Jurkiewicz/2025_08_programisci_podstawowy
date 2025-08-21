# OPIS klasy: class Ksiazka_telefoniczna
#
# pola:
#     rodzaj : str - priv | company
#     wpisy: dict {imie_nazwisko : [email, nr_telefonu],
#                 imie_nazwisko : [email, nr_telefonu],
#                 imie_nazwisko : [email, nr_telefonu],
#                 ....}
# metody:
#     pokaz_ksiazke - wypisuje wszystkie pozycje po kolei
#     dodaj_pozycje(imie_nazwisko, email, nr_telefonu)
class Ksiazka_telefoniczna:
    def __init__(self, rodzaj):
        # rodzaj książki: np. "priv" (prywatna) albo "company" (służbowa)
        self.rodzaj = rodzaj
        # wpisy zapisujemy w słowniku (dict) w postaci:
        # {"Jan Kowalski": ["email", "telefon"], ...}
        self.wpisy = { }

    def pokaz_ksiazke(self):
        # Jeśli książka jest pusta, wypisujemy komunikat
        if  self.wpisy == {} :
            print(f"Nie mamy kontaktów w książce o typie... ({self.rodzaj})")
        else:
            # Jeśli są wpisy, pokazujemy wszystkie
            print(f"\nKsiążka: {self.rodzaj}")
            # przechodzimy po wszystkich elementach słownika (osoba -> dane)
            for imie_nazwisko, dane in self.wpisy.items():
                email, nr_tel = dane  # rozbijamy listę na email i telefon
                print(f"- {imie_nazwisko}, email: {email}, tel: {nr_tel}")

    def dodaj_pozycje(self, imie_nazwisko, email, nr_telefonu):
        self.wpisy[imie_nazwisko] = [email, nr_telefonu]

ksiazka_prywatna = Ksiazka_telefoniczna("priv")
ksiazka_sluzbowa = Ksiazka_telefoniczna("company")

# Wyświetlamy zawartość książek
ksiazka_prywatna.pokaz_ksiazke()
ksiazka_sluzbowa.pokaz_ksiazke()

# Dodajemy 3 wpisy do książki prywatnej
ksiazka_prywatna.dodaj_pozycje("Adam", "Adam@dom.pl", "111-222-333")
ksiazka_prywatna.dodaj_pozycje("Julia", "Julia@dom.pl", "444-555-666")
ksiazka_prywatna.dodaj_pozycje("Adrian", "Adrian@dom.pl", "777-888-999")

# Dodajemy 3 wpisy do książki służbowej
ksiazka_sluzbowa.dodaj_pozycje("Konrad", "Konrad@abc.pl", "12-345-678")
ksiazka_sluzbowa.dodaj_pozycje("Paulina", "Paulina@xyz.pl", "98-765-432")

# Wyświetlamy zawartość książek
ksiazka_prywatna.pokaz_ksiazke()
ksiazka_sluzbowa.pokaz_ksiazke()