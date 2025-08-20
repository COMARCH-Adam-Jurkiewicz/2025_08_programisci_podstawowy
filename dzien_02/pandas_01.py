# wczytywanie danych z csv i xls
# https://github.com/abixadamj/helion-python/tree/main/Rozdzial_5

# from sys import exit
import sys


try:
    import pandas as pd

    print("Moduł pandas wczytany.")
except:
    print("Zainstaluj: 'pip install pandas' ")
    sys.exit(0)