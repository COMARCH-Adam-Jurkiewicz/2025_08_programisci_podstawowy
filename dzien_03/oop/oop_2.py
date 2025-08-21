class Statek:
    def __init__(self, nazwa, rodzaj):
        self.nazwa = nazwa
        self.rodzaj = rodzaj

    def opisz(self):
        print(f"Nasz statek jest rodzaju {self.rodzaj} i nazywa się {self.nazwa}")

    def odbijamy(self):
        print(f"Nasz statek odbijamy od brzegu -> {self.nazwa}")


class Zaglowiec(Statek):
    def __init__(self, nazwa, ile_masztow):
        super().__init__(nazwa, "Żaglowiec") #### Metoda SUPER!!!!!!
        self.masztow = ile_masztow

    def opisz(self):
        # super().opisz()
        print(f"Żaglowiec - {self.masztow} masztow i nazwa {self.nazwa}")




statek_1 = Statek("Anna Maria", "Zaglowiecccccccc")
statek_2 = Statek("Sołdek", "Towarowy")
statek_3 = Zaglowiec("Cutty Sark", 5)

statek_1.opisz()
statek_2.opisz()
statek_1.odbijamy()
statek_2.odbijamy()
statek_3.opisz()
statek_3.odbijamy()