import random

x=random.randint(1,100)

licznik=0

while True:
    liczbaUzytkownika=int(input("Podaj liczbe: "))
    if liczbaUzytkownika == x:
        break
    if liczbaUzytkownika > x:
        print("Podana liczba jest większa")
        licznik+=1
    if liczbaUzytkownika < x:
        print("Podana liczba jest mniejsza")
        licznik+=1

print(f"Poprawna liczba to {x}")
print(f"Twoja ilość prób wynosi: {licznik}")