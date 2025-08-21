import csv
import sys
from dateutil.parser import *

def parsuj_wiersz(wiersz:str, pattern:tuple) -> tuple:
    """

    :param wiersz:
    :param pattern:
    :return:
    """
    data = wiersz[:24].strip()
    zdarzenie = wiersz[26:34].strip()
    rodzaj = wiersz[34:47].strip()
    opis = wiersz[47:].strip()
    for p in pattern:
        if p in opis:
            return True, [data, zdarzenie, rodzaj, opis]

    return False, "None"


def parsuj_plik_log(nazwa_pliku:str) -> tuple:
    """

    :param nazwa_pliku:
    :return: lista pozycji zgodnych z wyszukiwanym patternem
    """
    wszystkie_wiersze = [["lp", "data","zdarzenie", "rodzaj", "opis"],]
    search_pattern = ("Login:", "Program Saved", "Loaded Program")
    numerek_lp = 0
    plik_wynikowy = nazwa_pliku.replace(".LOG", ".csv")
    with open(nazwa_pliku, mode="r", encoding="utf-8") as plik:
        for line in plik:
            wynik, dane_wiersza = parsuj_wiersz(line, pattern=search_pattern)
            if wynik:
                # założenie - wiersze w logu są w kolejności czasowej...
                dodaje = [numerek_lp] + dane_wiersza
                wszystkie_wiersze.append(dodaje)
                numerek_lp += 1

    if len(wszystkie_wiersze) == 1:
        return False, "Brak danych"


    with open(plik_wynikowy, 'w', newline='', encoding='utf-8') as plik:
        writer = csv.writer(plik, delimiter=';')
        writer.writerows(wszystkie_wiersze)

    # tworzymy tabelę z obiektami datetieme
    # https://dateutil.readthedocs.io/en/stable/examples.html#parse-examples
    dane_datetime = []
    for row in wszystkie_wiersze[1:]:
        czas = parse(row[1])
        dane_datetime.append([ row[0], czas, row[4] ])

    return True, dane_datetime # bez nagłówka

def szukaj_program_saved(tabela_zdarzen:list)-> list:
    """

    :param tabela_zdarzen: [ [time, zdarzenie] ]
    :return:
    """
    zdarzenia = []
    for row in tabela_zdarzen:
        if "Program Saved" in row[2]:
            zdarzenia.append(row)

    return zdarzenia



if __name__ == "__main__":
    q, tabela_zdarzen = parsuj_plik_log("ECW20250805.LOG")
    if not q:
        sys.exit(1)
    szukamy_zdarzen = szukaj_program_saved(tabela_zdarzen)
    print(szukamy_zdarzen)
    ostatnie_szukanie = None

    print("-------------------------")
    for szukanie in szukamy_zdarzen:
        nr_szukania = szukanie[0]
        if ostatnie_szukanie is None:
            zawez_szukanie = tabela_zdarzen[0:nr_szukania]
            print(nr_szukania)
            ostatnie_szukanie = nr_szukania
            print("First: ______________")
        else:
            zawez_szukanie = tabela_zdarzen[ostatnie_szukanie:nr_szukania]
            print(nr_szukania,"new",zawez_szukanie)
            ostatnie_szukanie = nr_szukania
            print("Next: ______________")
            # i co dalej?????