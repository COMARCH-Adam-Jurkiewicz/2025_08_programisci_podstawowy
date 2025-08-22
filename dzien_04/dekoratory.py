from datetime import datetime
from functools import lru_cache

start = datetime.now()

@lru_cache(maxsize=60000)
def suma_liczb(a,b=40,c=50):
    return a+b+c

@lru_cache(maxsize=60000)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# for _ in range(100000):
#     x = suma_liczb(2,2)
ciag_fib = [fib(n) for n in range(36)]

q = suma_liczb(4)
q1 = suma_liczb(4,5)
q2 = suma_liczb(4,6)

koniec = datetime.now()

print("aa")

print(f"Czas wykonania: {koniec-start} = {ciag_fib=}")