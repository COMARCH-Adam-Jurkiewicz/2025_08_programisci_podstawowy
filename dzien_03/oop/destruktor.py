class Jakas:
    def __init__(self):
        # konstruktor
        print(f"Obiekt o {id(self)=}")
    def __del__(self):
        # destruktor - działa dla del() lub na końcu skryptu
        print(f"DEL Obiekt o {id(self)=}")

zm_1 = Jakas()
zm_2 = Jakas()
zm_3 = Jakas()
del(zm_2)
print("---- END")