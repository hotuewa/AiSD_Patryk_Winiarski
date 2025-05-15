graf = {
    'A': {'B','C','E'},
    'B':{},
    'C':{'D','E'},
    'D':{'B'},
    'E':{'B'}
}
print("Wpisz 'OFF' zeby zakonczyć działanie programu")
while True:

    wierzcholek = input("Podaj wierzchołek: ").upper()

    if wierzcholek in graf.keys():
        sasiedzi = graf[wierzcholek]
        print(f'Sąsiedzi wierzchołka {wierzcholek} to {sasiedzi}')
    elif wierzcholek == "OFF":
        break
    else:
        print("Podany wierzchołek nie istnieje")
           