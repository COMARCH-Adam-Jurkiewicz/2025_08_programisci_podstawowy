import snakemd
from datetime import datetime
import subprocess

doc = snakemd.new_doc()
waluta = 'USD'
nr_tabeli = None
data_tabeli = None
kurs = None
waluta_nazwa = None
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

doc.dump(nazwa_md)

subprocess.run(polecenia)