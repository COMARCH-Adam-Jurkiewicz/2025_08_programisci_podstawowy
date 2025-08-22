from faker import Faker
import csv

print("START")

fake = Faker(["pl_PL", "de_DE"])

print("START 2")

tablica = [["nazwa","andek","email","telefon"]]
for _ in range(200):
    wiersz = [fake.name(), fake.android_platform_token() , fake.ascii_company_email(), fake.phone_number()]
    tablica.append(wiersz)
    print(wiersz)
with open("plik.csv", 'w', newline='', encoding='utf-8') as plik:
    writer = csv.writer(plik,delimiter=';')
    writer.writerows(tablica)

print("STOP")