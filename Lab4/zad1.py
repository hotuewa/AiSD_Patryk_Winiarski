stos = []
start = "tak"

while start=="tak":
    liczba = int(input("Podaj liczbe: "))
    stos.append(liczba)
    start=input("Chcesz cos jeszcze dodac?(tak albo nie): ").lower()


print(stos[::-1], end=" ")