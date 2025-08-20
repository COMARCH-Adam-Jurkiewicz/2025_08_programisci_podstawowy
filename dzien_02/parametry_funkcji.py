def pitagoras(a:int,b,c)-> bool:
    """

    :param a:
    :param b:
    :param c:
    :return: true, jesli spełnia pitagorasa
    """
    if a**2 + b**2 == c**2:
        print(f"OK - {a=}, {b=}, {c=}")
    else:
        print(f"ERROR - {a=}, {b=}, {c=}")

pitagoras(2,3,4)
pitagoras(3,4,2)
pitagoras(4,5,6)
pitagoras(3,4,5)
pitagoras(b=3,a=4,c=5)

