import random

if __name__ == "__main__":
    n = int(input("Podaj ile liczb: "))
    if n>0:
        liczby = []
        for i in range(n):
            liczba = random.randint(1,100)
            liczby.append(liczba)

        print(liczby)
        liczba_uzytkownika = int(input("Podaj liczbe: "))
        if liczba_uzytkownika in liczby:
            print(f"Podana liczba {liczba_uzytkownika} występuje w wylosowanym ciągu {liczby} i ma indeks {liczby.index(liczba_uzytkownika)}")

        else:
            print(f"Podana wartość {liczba_uzytkownika} nie występuje w wylosowanym ciągu {liczby}")

    else:
        print("n musi być większe od zera.")