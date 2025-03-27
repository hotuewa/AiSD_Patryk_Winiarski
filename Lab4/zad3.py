stos = []

while True:
    co = str(input("Co chcesz zrobic: ")).lower()
    if co=="dodaj":
        tekst=str(input("Podaj tekst: "))
        stos.append(tekst)
        print(stos)
    elif co=="cofnij":
        stos.pop()
        print(stos)
    elif co=="exit":
        break
    else: print("Wpisz poprawna operacje")