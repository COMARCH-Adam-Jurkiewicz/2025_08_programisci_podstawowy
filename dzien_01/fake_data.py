from faker import Faker
import csv
fake = Faker(["pl_PL", "de_DE"])

tablica = []
for _ in range(200):
    wiersz = [fake.name(), fake.android_platform_token() , fake.ascii_company_email(), fake.phone_number()]
    tablica.append(wiersz)
    print(wiersz)

# Tworzenie pliku CSV otwieranego przez Excela
with open('../dzien_02/dane.csv', 'w', newline='', encoding='utf-8') as plik:
    writer = csv.writer(plik)
    writer.writerows(tablica)