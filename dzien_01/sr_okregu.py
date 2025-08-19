# wzor:
# sqrt((x-x_centr)**2 + (y-y_centr)**2)
# round(sqrt((x_point-self.x_center)**2 + (y_point-self.y_center)**2),0)

# sr = (23,35)
# a = (134,24), b = (110,40), c= (50,70)

from math import sqrt

print("Start")

def odleglosc_punktow_od_siebie_pot(srodek, punkt):
    sr_x, sr_y = srodek
    # pk_x = punkt[0]
    # pk_y = punkt[1]
    pk_x, pk_y = punkt
    odl = ((pk_x-sr_x)**2 + (pk_y-sr_y)**2 )**(1/2)
    return odl

def odleglosc_punktow_od_siebie(srodek: tuple[int,int], punkt: tuple) -> float:
    """

    :param srodek: tupla z x, y srodka, np (3,5)
    :param punkt:  j.w.
    :return: odleglosc w pixelach
    """
    sr_x, sr_y = srodek
    # pk_x = punkt[0]
    # pk_y = punkt[1]
    pk_x, pk_y = punkt
    odl = sqrt((pk_x-sr_x)**2 + (pk_y-sr_y)**2)
    return odl


# odl_1 = odleglosc_punktow_od_siebie_pot((23,35),(134,24) )
# print(f"{odl_1=}")

odl_1 = odleglosc_punktow_od_siebie((23,35),(134,24) )
print(f"{odl_1=}")

srodek_test = (23,35)
lista_punktow = [ (134,24),"NIC" , (30,55), (110,40), (50,70) ]
wyniki = [ ]

for leden_punkt in lista_punktow:
    print(f"{leden_punkt=}")
    odleglosc = odleglosc_punktow_od_siebie(srodek_test, leden_punkt)
    print(f"{odleglosc=}")
    wyniki.append(odleglosc)



print(f"{wyniki=} / najlepszy to {min(wyniki)}")
