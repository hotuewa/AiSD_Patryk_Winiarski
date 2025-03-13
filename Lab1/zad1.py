import math

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))


if a!=0:
    delta = (b*b)-(4*a*c)
    if delta > 0:
        x1=(-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print(f'Podane równanie ma dwa rozwiązania rzeczywiste x1 = {x1} i x2 = {x2}')
    elif delta == 0:
        x0=-b/(2*a)
        print(f'Podane równanie ma jeden pierwiastek podwójny x0 równy: {x0}')
    else:
        print(f"Podane równanie nie ma pierwiastków rzeczywistych.")

else:
    print("To nie jest rownanie kwadratowe")