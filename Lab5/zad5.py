kolejka = []

def pokaz_menu():
    print('''
Wybierz dzialanie:
1. Dodaj klienta do kolejki
2. Obsluz klienta
3. Pokaz kolejke i czasy oczekiwania
4. Zakoncz program
''')

def dodaj_klienta():
    imie = input("Podaj imie klienta: ")
    czas = input("Podaj czas obslugi (w minutach): ")
    try:
        czas = int(czas)
        klient = [imie, czas]
        kolejka.append(klient)
        print(f"Dodano klienta {imie} z czasem obslugi {czas} minut.")
    except:
        print("Blad! Czas musi byc liczba calkowita.")

def obsluz_klienta():
    if len(kolejka) > 0:
        klient = kolejka.pop(0)
        print(f"Obsluzono klienta {klient[0]}. Czas obslugi: {klient[1]} minut.")
    else:
        print("Kolejka jest pusta.")

def pokaz_kolejke():
    if len(kolejka) == 0:
        print("Kolejka jest pusta.")
    else:
        print("Kolejka klientow:")
        suma = 0
        for klient in kolejka:
            print(f"- {klient[0]} | Czas oczekiwania: {suma} minut | Czas obslugi: {klient[1]} minut")
            suma += klient[1]

def main():
    while True:
        pokaz_menu()
        wybor = input("Twoj wybor: ")

        if wybor == "1":
            dodaj_klienta()
        elif wybor == "2":
            obsluz_klienta()
        elif wybor == "3":
            pokaz_kolejke()
        elif wybor == "4":
            print("Zamykanie programu...")
            break
        else:
            print("Nie ma takiej opcji. Sprobuj jeszcze raz.")

main()
