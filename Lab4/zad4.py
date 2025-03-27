def onp(wyrazenie):
    operacje={
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: y / x if x != 0 else "Blad: Dzielenie przez zero",
        "^": lambda x, y: x ** y
    }
    stos = []
    for element in wyrazenie.split():
        if element.isdigit():
            stos.append(int(element))
        elif element in operacje:
            if len(stos) < 2:
                return "Blad: Za mało argumentow do operacji"
            y = stos.pop()
            x = stos.pop()
            wynik = operacje[element](x, y)
            stos.append(wynik)
        elif element == "=":
            return f" Wynik wyrazenia onp {wyrazenie} to: {stos.pop()}" if stos else "Blad: Brak wyniku"
        else:
            return f"Blad: Nieznany element '{element}'"
    return "Blad: Brak znaku '=' na koncu"

wyrazenie = "5 3 - ="

print(onp(wyrazenie))