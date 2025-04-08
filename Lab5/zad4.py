import heapq

def start():
    menu = '''\nWybierz dzialanie:
    1. Dodaj zadanie z priorytetem
    2. Obsluz zadanie o najwyższym priorytecie
    3. Pokaz kolejke zadan
    4. Zakoncz dzialanie programu'''
    print(menu)

    while True:
        op = int(input("Co chcesz zrobic? "))
        if op == 1:
            dodaj_zadanie()
        if op == 2:
            obsluz_zadanie()
        if op == 3:
            pokaz_kolejke()
        if op == 4:
            break

def dodaj_zadanie():
    nazwa = input("Podaj nazwe zadania: ")
    priorytet = int(input("Podaj priorytet (nizsza liczba = wyzszy priorytet): "))
    heapq.heappush(kolejka_zadan, (priorytet, nazwa))
    print(f"Zadanie '{nazwa}' zostalo dodane z priorytetem {priorytet}.")


def obsluz_zadanie():
    if kolejka_zadan:
        priorytet, nazwa = heapq.heappop(kolejka_zadan)
        print(f"Obsluzono zadanie: {nazwa} (priorytet: {priorytet})")
    else:
        print("Kolejka zadan jest pusta.")

def pokaz_kolejke():
    if kolejka_zadan:
        print("Aktualna kolejka zadan (od najwyzszego priorytetu):")
        for priorytet, nazwa in sorted(kolejka_zadan):
            print(f"- {nazwa} (priorytet: {priorytet})")
    else:
        print("Kolejka zadan jest pusta.")



kolejka_zadan = []

start()