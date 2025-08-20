import requests

api_url = "https://api.nbp.pl/api/exchangerates/tables/a/?format=json"

r = requests.get(api_url)
dane = r.json()[0]

print(f"{dane['effectiveDate']=}")
lista_walut = dane['rates']
print(lista_walut[:3])
for waluta_rate in lista_walut:
    if waluta_rate['code'] == "USD":
        print(f"{waluta_rate=}")

    if waluta_rate['code'] in szukane_waluty:
        print(f"Szukana {waluta_rate=} / {waluta_rate['mid']=} zł")
