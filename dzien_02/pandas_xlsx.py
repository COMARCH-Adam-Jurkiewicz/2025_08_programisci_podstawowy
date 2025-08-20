# wczytywanie xlsx do pandas
import pandas as pd

plik = "dane_2.xlsx"

df = pd.read_excel(plik)

df['numer'] = range(len(df))
df['kolejna'] = df['numer']+5

print(df[:5])

df.to_excel("dodany_4.xlsx", index=False)
