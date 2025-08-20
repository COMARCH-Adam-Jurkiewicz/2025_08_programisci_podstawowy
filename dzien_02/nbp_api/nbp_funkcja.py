import requests

def import_from_nbp(kod_waluty='USD'):
    """

    :param waluta: kod waluty, default="USD
    :return: dane_waluty dict
    """
    api_url = "https://api.nbp.pl/api/exchangerates/tables/a/?format=json"
    r = requests.get(api_url)
    dane = r.json()[0]
    data_tabeli = dane['effectiveDate']
    nr_tabeli = dane['no']
    lista_walut = dane['rates']
    kod_waluty = kod_waluty.upper()
    for waluta_rate in lista_walut:
        if waluta_rate['code'] == kod_waluty:
            cur = waluta_rate['currency']
            mid = waluta_rate['mid']
            return (data_tabeli, nr_tabeli, cur, mid)
    return None

dane = import_from_nbp()
print(dane)
chf = import_from_nbp("chf")
print(chf)