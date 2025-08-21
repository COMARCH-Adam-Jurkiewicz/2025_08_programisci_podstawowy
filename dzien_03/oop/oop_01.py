#definicja obiektu w Python - wersje minimum

# 1 - definicja klasy
class Telefon_minimum:
    pass

class Telefon:
    def __init__(self, wlasciciel):
        self.kolor = "PUSTY"
        self.cpu = None
        self.os = None
        self.owner = wlasciciel
        print(f"Kolor: {self.kolor}")

    def informacje(self):
        print(f"Telefon {self.owner} ma kolor: {self.kolor} i cpu: {self.cpu} i os: {self.os}")
        if self.os == "iOS":
            print("Pewnie drogi")

    def polepsz_cpu(self, nowy_cpu):
        if self.cpu is None:
            self.cpu = nowy_cpu
            print(f"CPU {self.cpu} i os: {self.os}")
        else:
            print("Niemożliwa opracja")

# 2 - obiket typu klasy

telefon_wojtka = Telefon("Wojtka")
telefon_wojtka.kolor = "silver-grey"
telefon_wojtka.os = "iOS"
telefon_wojtka.cpu = "A15"
telefon_julii = Telefon("Julii")
telefon_julii.kolor = "zielony"
telefon_julii.os = "Android"

print(telefon_julii.kolor)
print(telefon_wojtka.kolor)
telefon_wojtka.informacje()
telefon_julii.informacje()
telefon_wojtka.polepsz_cpu("A22")
telefon_julii.polepsz_cpu("X43")
print(telefon_julii)