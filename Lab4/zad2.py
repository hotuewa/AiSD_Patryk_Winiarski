def sprawdz_nawiasy(wyrazenie):
    stos = []

    for znak in wyrazenie:
        if znak == '(':
            stos.append(znak)
        elif znak == ')':
            if not stos:
                return False
            stos.pop()

    return len(stos) == 0

nawiasy = input("Podaj nawiasy: ")

print(sprawdz_nawiasy(nawiasy))