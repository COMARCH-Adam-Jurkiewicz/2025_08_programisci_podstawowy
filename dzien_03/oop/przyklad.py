from random import randint, random
from faker import Faker
import csv

class Produkcja:
    def __init__(self, nr_ser, koszt, czas):
        self.nr_ser = nr_ser
        self.koszt = koszt
        self.czas = czas

    def czsokoszt(self):
        return [self.nr_ser, round(self.koszt,2), self.czas, round(self.koszt/self.czas,2)]

fk = Faker("pl_PL")
prod = []
for _ in range(100):
    obiekt = Produkcja(fk.isbn13(), random()*2000, randint(1, 100))
    prod.append(obiekt)
# print(prod)

dane = [ ["nr_ser", "koszt", "czas", "koszt/czas"],]

for dana in prod:
    # print(dana.czsokoszt())
    dane.append(dana.czsokoszt())

with open("dane_prod.csv", 'w', newline='', encoding='utf-8') as plik:
    writer = csv.writer(plik)
    writer.writerows(dane)