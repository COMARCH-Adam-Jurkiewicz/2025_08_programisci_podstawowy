# mamy plik csv i dodajemy do niego nagłówek
import csv
plik_wejsciowy = "dane_in.csv"
plik_poprawny = "dane_out.csv"
naglowek = [ "imie_nazwisko","android_wersja","email_praca","telefon" ]
dane_out = [ naglowek]

with open(plik_wejsciowy, mode='r', encoding='utf-8') as input_file:
    reader = csv.reader(input_file)
    for wiersz in reader:
        # print(wiersz)
        dane_out.append(wiersz)

    print(dane_out[:4])
    # wycinki opisane https://github.com/abixadamj/helion-python/blob/main/Rozdzial_1/r1_13.py

with open(plik_poprawny, 'w', newline='', encoding='utf-8') as plik:
    writer = csv.writer(plik)
    writer.writerows(dane_out)