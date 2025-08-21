import sys
import snakemd
from datetime import datetime
import subprocess

from nbp_funkcja import import_from_nbp

doc = snakemd.new_doc()
waluta = 'BAT'
nr_tabeli = None
data_tabeli = None
kurs = None
waluta_nazwa = None
wynik, dane_o_walucie = import_from_nbp(waluta)
if wynik is True:
    data_tabeli, nr_tabeli, waluta_nazwa, kurs = dane_o_walucie

if wynik is False:
    print(f"ERROR - {dane_o_walucie}")
    sys.exit(15)

nazwa_md = f"plik_{waluta}_{data_tabeli}"
plik_md = f"{nazwa_md}.md"
plik_docx = f"{nazwa_md}.docx"
polecenie = ["pandoc", "-o", plik_docx, plik_md ]

doc.add_heading("RAPORT stanu kursu waluty", level=2)
doc.add_horizontal_rule()
doc.add_heading(f"Waluta: {waluta}", level=3)
doc.add_raw(f"""
W tabeli NBP nr: {nr_tabeli}

w dniu: {datetime.now().date()}

z dnia {data_tabeli}

kurs 1 {waluta_nazwa} wynosi {kurs} zł.
""")
doc.add_horizontal_rule()

try:
    doc.dump(nazwa_md)
except Exception as e:
    print(f"ERROR - {e}")
    sys.exit(2)

try:
    subprocess.run(polecenie,capture_output=True)
except Exception as e:
    print(f"ERROR on running - {e}")
    sys.exit(3)