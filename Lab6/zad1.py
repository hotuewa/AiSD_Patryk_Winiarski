
liczbaGraczy = int(input("Podaj liczbę graczy: "))

wynikiPunktowe = []

for i in range(liczbaGraczy):
    if liczbaGraczy > 0:
        wynik = int(input(f'Podaj wynik gracza {i}: '))
        wynikiPunktowe.append(wynik)
    else:
        print("Liczba graczy musi być większa do 0")    

print(wynikiPunktowe)

def bubbleSort(tablica):
    for n in range(len(tablica)):
        for i in range(len(tablica)-1):
            if tablica[i]>tablica[i+1]:
                tablica[i],tablica[i+1]=tablica[i+1],tablica[i]
    return tablica

wynikBubbleSort = bubbleSort(wynikiPunktowe)
print(f'Posortowana tablica: {wynikBubbleSort}')
print(f'Wynik min: {wynikBubbleSort[0]}')
print(f'Wynik max: {wynikBubbleSort[-1]}')
