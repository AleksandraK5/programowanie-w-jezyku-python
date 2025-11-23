def czy_parzysta(a: int) -> bool:
    return a % 2 == 0
result=czy_parzysta(5)
if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")