if __name__ == "__main__":
    n = int(input("Podaj ile liczb: "))
    if n>0:
        liczby = []
        for i in range(n):
            liczba = int(input("Podaj liczbe: "))
            liczby.append(liczba)
        suma=0
        for j in liczby:
            if j%2==0:
                suma+=1

        print(f"Pośród {n} podanych liczb znalazło się {suma} liczb parzystych. ")
    else:
        print("n musi być większe od zera.")

