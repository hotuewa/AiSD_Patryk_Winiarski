def wysz_bin(liczby, lewy, prawy, x):
    if x in liczby:
        if lewy > prawy:
            print("Podany element nie zostal znaleziony")

        srodek = (lewy + prawy) // 2
        if liczby[srodek] == x:
            print(f"Szukany element {x} zostal znaleziony i ma indeks {srodek}")
        elif liczby[srodek] > x:
            return wysz_bin(liczby, lewy, srodek - 1, x)
        else:
            return wysz_bin(liczby, srodek + 1, prawy, x)
    else:
        print("Podany element nie znajduje się na liscie")


liczby=[1,44,5,65,4,9]
x=int(input("Podaj liczbe: "))

wysz_bin(sorted(liczby),0,len(liczby),x)
